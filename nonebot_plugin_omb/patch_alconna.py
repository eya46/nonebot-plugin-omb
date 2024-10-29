from typing import Union

from nonebot import logger
from nonebot.typing import T_RuleChecker
from nonebot.internal.rule import Rule
import nonebot_plugin_alconna

from nonebot_plugin_omb.util import SuperUserRule, patch

_raw_on_alconna = nonebot_plugin_alconna.on_alconna


@patch(nonebot_plugin_alconna, name="on_alconna")
def patch_on_alconna(*args, **kwargs):
    if (rule := kwargs.get("rule")) is None:
        kwargs["rule"] = SuperUserRule
    else:
        rule: Union[Rule, T_RuleChecker]
        kwargs["rule"] = rule & SuperUserRule
    return _raw_on_alconna(*args, **kwargs)


logger.success("Patch alconna on_alconna successfully.")
