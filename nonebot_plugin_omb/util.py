from types import FunctionType
from typing import Optional
from collections.abc import Callable

from nonebot import get_driver

SUPERUSERS = get_driver().config.superusers


def patch(obj, pre: Optional[Callable] = None, name: Optional[str] = None):
    def _patch(func: FunctionType):
        if pre:
            func = pre(func)
        setattr(obj, name if name else func.__name__, func)
        return func

    return _patch
