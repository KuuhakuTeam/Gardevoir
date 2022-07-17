# Gardevoir PokeBot
# Copyright (C) 2022 KuuhakuTeam
#
# This file is a part of < https://github.com/KuuhakuTeam/Gardevoir/ >
# PLease read the GNU v3.0 License Agreement in 
# <https://www.github.com/KuuhakuTeam/Gardevoir/blob/master/LICENSE/>

import time

from gardevoir import Config, START_TIME


def time_formatter(seconds: float) -> str:
    """ humanize time """
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]


def uptime() -> str:
    """ return uptime """
    return time_formatter(time.time() - START_TIME)


def is_dev(user_id: int) -> bool:
    """ return if is dev """
    return user_id in Config.DEV_USERS


def input_str(message) -> str:
    """ filter text """
    return " ".join(message.text.split()[1:])