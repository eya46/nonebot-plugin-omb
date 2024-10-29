from typing import Union, Optional

import nonebot
from nonebot import logger, on_message
from nonebot.rule import command
from nonebot.typing import T_RuleChecker
from nonebot.internal.rule import Rule
from nonebot.internal.matcher import Matcher

from .util import SuperUserRule, patch


@patch(nonebot, name="on_command")
@patch(nonebot.plugin, name="on_command")
def patch_on_command(
    cmd: Union[str, tuple[str, ...]],
    rule: Optional[Union[Rule, T_RuleChecker]] = None,
    aliases: Optional[set[Union[str, tuple[str, ...]]]] = None,
    force_whitespace: Optional[Union[str, bool]] = None,
    _depth: int = 0,
    **kwargs,
) -> type[Matcher]:
    """注册一个消息事件响应器，并且当消息以指定命令开头时响应。

    命令匹配规则参考: `命令形式匹配 <rule.md#command-command>`_

    参数:
        cmd: 指定命令内容
        rule: 事件响应规则
        aliases: 命令别名
        force_whitespace: 是否强制命令后必须有指定空白符
        permission: 事件响应权限
        handlers: 事件处理函数列表
        temp: 是否为临时事件响应器（仅执行一次）
        expire_time: 事件响应器最终有效时间点，过时即被删除
        priority: 事件响应器优先级
        block: 是否阻止事件向更低优先级传递
        state: 默认 state
    """

    commands = {cmd} | (aliases or set())
    kwargs.setdefault("block", False)
    rule = rule & SuperUserRule if rule else SuperUserRule
    return on_message(
        command(*commands, force_whitespace=force_whitespace) & rule,
        **kwargs,
        _depth=_depth + 1,  # type:ignore
    )


logger.success("Patch nonebot on_command successfully.")
