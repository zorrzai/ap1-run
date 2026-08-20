"""AP-1 Inspect Solver.

Custom solver that calls generate_loop(), walks the returned message
list, and pairs ChatMessageAssistant.tool_calls with ChatMessageTool
responses by tool_call_id.

Stores per-round tool-call records in state.metadata for the scorer.

D7.9 HANDLING: if a tool call has no matching ChatMessageTool response,
that is a partial-failure case and maps to D7.9. The round shape is
recorded as unrecognised.
"""

from inspect_ai.solver import Solver, solver, TaskState
from inspect_ai.model import get_model, ChatMessageAssistant, ChatMessageTool

from .shim import inspect_tc_to_runner, build_final_response


@solver
def ap1_solver(tools=None):
    """AP-1 measurement solver.

    Runs generate_loop with the provided tools, then extracts the
    structural tool-call record for the scorer.
    """
    async def solve(state: TaskState, generate) -> TaskState:
        # Resolve tools from the task if not provided
        solve_tools = tools or state.tools

        # Run the Inspect tool loop
        output = await get_model().generate(
            state.messages,
            tools=solve_tools,
            cache=False,
        )
        state.output = output

        # Walk the output to extract tool calls
        tool_calls_record = []
        round_shapes = []
        turn = 0

        # The output.message is the final assistant message
        # For multi-round, we need to check state.messages which
        # were extended by generate
        final_text = ''
        if output.message and output.message.content:
            if isinstance(output.message.content, str):
                final_text = output.message.content
            elif isinstance(output.message.content, list):
                final_text = ' '.join(
                    getattr(c, 'text', str(c))
                    for c in output.message.content
                )

        # Extract tool calls from the output
        # In a single generate() call, tool_calls are on the message
        if output.message and output.message.tool_calls:
            turn = 1
            round_shapes.append((True, 'structural response'))
            for tc in output.message.tool_calls:
                tool_calls_record.append(
                    inspect_tc_to_runner(tc, turn=turn)
                )

        # Check for multi-round: walk all messages looking for
        # assistant messages with tool calls
        all_tool_calls_from_messages = []
        for i, msg in enumerate(state.messages):
            if isinstance(msg, ChatMessageAssistant) and msg.tool_calls:
                turn_num = len(all_tool_calls_from_messages) + 1
                round_shapes_entry = (True, 'structural response')

                for tc in msg.tool_calls:
                    # D7.9: check for matching tool response
                    has_response = False
                    tool_return_content = None
                    for j in range(i + 1, len(state.messages)):
                        if isinstance(state.messages[j], ChatMessageTool):
                            if state.messages[j].tool_call_id == tc.id:
                                has_response = True
                                tool_return_content = state.messages[j].text
                                break
                        elif isinstance(state.messages[j], ChatMessageAssistant):
                            break

                    if not has_response:
                        # D7.9: partial failure
                        round_shapes_entry = (
                            False,
                            f'tool call {tc.id} has no matching response '
                            f'(D7.9 partial failure)')

                    record = inspect_tc_to_runner(
                        tc, turn=turn_num,
                        return_value=tool_return_content,
                    )
                    all_tool_calls_from_messages.append(record)

                round_shapes.append(round_shapes_entry)

        # Use multi-round records if available, else single-round
        if all_tool_calls_from_messages:
            tool_calls_record = all_tool_calls_from_messages

        # If no tool calls at all, record one shape check for the final
        if not round_shapes:
            round_shapes.append((True, 'no tool calls in response'))

        # Build the final response dict for shape checking
        final_response = build_final_response(
            final_text, tool_calls_present=False)

        # Store everything the scorer needs
        state.metadata['ap1_tool_calls'] = tool_calls_record
        state.metadata['ap1_round_shapes'] = round_shapes
        state.metadata['ap1_final_response'] = final_response
        state.metadata['ap1_final_text'] = final_text
        state.metadata['ap1_tools_offered'] = bool(solve_tools)

        return state

    return solve
