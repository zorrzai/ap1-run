"""Shim: convert Inspect ToolCall to runner's tool-call dict shape.

The runner's engine.py accumulates tool calls as dicts:
    {'turn': int, 'id': str, 'type': str,
     'function': {'name': str, 'arguments': str}}

Inspect's generate_loop() returns ChatMessageAssistant objects whose
.tool_calls are ToolCall dataclasses:
    ToolCall(id: str, function: str, arguments: dict, type: str)

This module converts one to the other. Nothing else.
"""

import json


def inspect_tc_to_runner(tc, *, turn=1):
    """Convert an Inspect ToolCall to the runner's dict shape.

    Args:
        tc: An inspect_ai.tool.ToolCall object.
        turn: The tool-loop turn number.

    Returns:
        dict matching engine.py's tool_calls_record format.
    """
    return {
        'turn': turn,
        'id': tc.id,
        'type': getattr(tc, 'type', 'function'),
        'function': {
            'name': tc.function,
            'arguments': json.dumps(tc.arguments),
        },
    }


def build_final_response(text_content, *, tool_calls_present):
    """Build a minimal response dict for classify_invocation's shape check.

    The runner's evidence._extract_model_tool_calls expects:
        {'choices': [{'message': {'tool_calls': [...], 'content': str}}]}

    For a completed tool loop, the final response has no tool_calls.
    """
    msg = {'content': text_content or '', 'role': 'assistant'}
    if not tool_calls_present:
        msg['tool_calls'] = None
    return {'choices': [{'message': msg}]}
