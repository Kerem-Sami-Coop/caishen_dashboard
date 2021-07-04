from flask import session, redirect, url_for
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("_user_id") is None:
            return redirect(url_for("auth.login"))
        return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function
