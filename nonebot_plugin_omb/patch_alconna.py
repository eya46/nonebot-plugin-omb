from typing import Union

from nonebot import Bot, logger
from arclet.alconna import Alconna
from nonebot.typing import T_RuleChecker
from nonebot.internal.rule import Rule
import nonebot_plugin_alconna
from nonebot_plugin_alconna import Extension
from nonebot.internal.adapter import Event
from nonebot_plugin_alconna.extension import ExtensionExecutor

from nonebot_plugin_omb.util import SuperUserObj, SuperUserRule, patch

_raw_on_alconna = nonebot_plugin_alconna.on_alconna


@patch(nonebot_plugin_alconna, name="on_alconna")
def patch_on_alconna(*args, **kwargs):
    if (rule := kwargs.get("rule")) is None:
        kwargs["rule"] = SuperUserRule
    else:
        rule: Union[Rule, T_RuleChecker]
        kwargs["rule"] = rule & SuperUserRule
    return _raw_on_alconna(*args, **kwargs)


class OmbExtension(Extension):
    @property
    def id(self) -> str:
        return "OmbExtension"

    @property
    def priority(self) -> int:
        return 0

    async def permission_check(self, bot: Bot, event: Event, command: Alconna) -> bool:
        return await SuperUserObj(bot, event)


ExtensionExecutor.globals.append(OmbExtension)


logger.success("Patch alconna on_alconna successfully.")
