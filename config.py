from nonebot.plugin import PluginMetadata
from zhenxun.configs.utils import PluginExtraData, RegisterConfig
from typing import Any
__plugin_meta__ = PluginMetadata(
    name="维维语录",
    description="通过API获取维维语录图片",
    usage="""
使用方式：
1. 直接搜索：
/vv语录 <标题> [数量/参数]
2. 引用消息搜索：
引用某条消息 + /vv语录 [数量/参数]
3. 设置默认数量：
/vv_set_default_num <数量>
4. 支持本地API：
在配置中设置 api_base 项，填写完整API地址（如 http://localhost:8000/search）
""",
    extra=PluginExtraData(
        author="author",
        version="0.1",
        is_show=True,
        configs=[
            RegisterConfig(
                module="vvquest",
                key="max_num",
                value=10,
                help="最大返回图片数量限制 (1-50)",
                default_value=10,
                type=int,
                arg_parser=lambda x: max(1, min(50, int(x))) 
            ),
            RegisterConfig(
                module="vvquest",
                key="use_forward",
                value=True,
                help="是否使用合并转发消息",
                default_value=False,
                type=bool
            ),
            RegisterConfig(
                module="vvquest",
                key="api_base",
                value="",
                help="本地API完整地址（如 http://localhost:8000/search），留空使用默认在线API",
                default_value="",
                type=str
            ),
            RegisterConfig(  
                module="vvquest",
                key="cooldown",
                value=30,
                help="API请求冷却时间（秒），防止频繁请求 (1-300)",
                default_value=30,
                type=int,
                arg_parser=lambda x: max(1, min(300, int(x)))
            )
        ],
    ).dict()
)