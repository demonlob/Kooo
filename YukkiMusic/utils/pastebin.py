#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import aiohttp, asyncio
from nekobin import Nekobin

nb = Nekobin()

async def Yukkibin(text):
    result = await nb.paste(text)
    if result.ok:
        return(result.url)
    else:
        print("Nekobin Error:",  result.message)
        return
