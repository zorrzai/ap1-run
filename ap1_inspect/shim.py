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


class ShimError(Exception):
    """Shim conversion failure -- mirrors engine.EngineError."""


def inspect_tc_to_runner(tc, *, turn=1, return_value=None):
    """Convert an Inspect ToolCall to the runner's dict shape.

    Args:
        tc: An inspect_ai.tool.ToolCall object.
        turn: The tool-loop turn number.
        return_value: str or None -- the tool return text extracted
            via ChatMessageTool.text (which handles both str and
            list[Content]).  Must be a JSON string parseable by
            provenance_classify._parse_return_value.  Matches the
            shape engine.py attaches at L217.

    Returns:
        dict matching engine.py's tool_calls_record format.

    Raises:
        ShimError: if return_value is not None and is not a valid
            JSON string.  engine.py raises EngineError when it
            cannot attach a return value; the shim must not be
            quieter.
    """
    record = {
        'turn': turn,
        'id': tc.id,
        'type': getattr(tc, 'type', 'function'),
        'function': {
            'name': tc.function,
            'arguments': json.dumps(tc.arguments),
        },
    }
    if return_value is not None:
        # Validate: return_value must be a str containing valid JSON.
        # engine.py stores the raw result of _execute_tool, which is
        # always json.dumps({...}).  _parse_return_value calls
        # json.loads on it.  If this is not parseable, something is
        # wrong with the extraction and it must fail loudly.
        if not isinstance(return_value, str):
            raise ShimError(
                'return_value must be str, got '
                + type(return_value).__name__
                + '; ChatMessageTool.text should have been used, '
                + 'not .content')
        try:
            json.loads(return_value)
        except (json.JSONDecodeError, TypeError) as e:
            raise ShimError(
                'return_value is not valid JSON: '
                + repr(return_value)
                + '; provenance_classify._parse_return_value will '
                + 'fail: ' + str(e)
            ) from e
        record['return_value'] = return_value
    return record


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
