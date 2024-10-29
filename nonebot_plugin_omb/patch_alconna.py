from typing import Union

from nonebot import Bot
from arclet.alconna import Alconna
from nonebot.typing import T_PermissionChecker
from nonebot.permission import SUPERUSER
import nonebot_plugin_alconna
from nonebot.internal.adapter import Event
from nonebot.internal.permission import Permission
from nonebot_plugin_alconna.extension import Extension, ExtensionExecutor

from nonebot_plugin_omb.util import SuperUserObj, patch

_raw_on_alconna = nonebot_plugin_alconna.on_alconna


@patch(nonebot_plugin_alconna, name="on_alconna")
def patch_on_alconna(*args, **kwargs):
    if (permission := kwargs.get("permission")) is None:
        kwargs["permission"] = SUPERUSER
    else:
        permission: Union[Permission, T_PermissionChecker]
        kwargs["permission"] = permission | SUPERUSER
    return _raw_on_alconna(*args, **kwargs)


class MyExtension(Extension):
    @property
    def id(self) -> str:
        return "OmbExtension"

    @property
    def priority(self) -> int:
        return 0

    async def permission_check(self, bot: Bot, event: Event, command: Alconna) -> bool:
        return await SuperUserObj(bot, event)


ExtensionExecutor.globals.append(MyExtension)
