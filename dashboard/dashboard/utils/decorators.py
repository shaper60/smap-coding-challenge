from functools import wraps

def default_context(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        context = {}
        kwargs['context'] = context
        return view_func(*args, **kwargs)
    return wrapper