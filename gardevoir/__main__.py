# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import asyncio

from . import ralts
from pyrogram import idle
from .helpers.database.core import _close_db

async def main():
    await ralts.start()
    await idle()
    await ralts.stop()
    _close_db()


if __name__ == "__main__" :
    asyncio.get_event_loop().run_until_complete(main())
