import time
import logging


def get_request_args(ctx, include=None, exclude=None):
    default_include = ('args', 'json', 'form', 'data')
    if include is None:
        include = default_include
    if exclude is not None:
        include = include - exclude

    args_dict = {}
    if 'args' in include:
        if ctx.req.args:
            args_dict['args'] = ctx.req.args.to_dict()
    if 'json' in include:
        try:
            if ctx.req.json:
                args_dict['json'] = ctx.req.json
        except:
            pass
    if 'form' in include:
        if ctx.req.form:
            args_dict['form'] = ctx.req.form
    if 'data' in include:
        if ctx.req.data:
            args_dict['data'] = ctx.req.data
    return args_dict
