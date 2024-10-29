from types import FunctionType
from typing import Optional
from collections.abc import Callable

from nonebot.permission import SuperUser
from nonebot.internal.rule import Rule

SuperUserObj = SuperUser()
SuperUserRule = Rule(SuperUserObj)


def patch(obj, pre: Optional[Callable] = None, name: Optional[str] = None):
    def _patch(func: FunctionType):
        if pre:
            func = pre(func)
        setattr(obj, name if name else func.__name__, func)
        return func

    return _patch
