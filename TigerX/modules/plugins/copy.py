# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea
# Don't remove credits

from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command("copy", cmd) & owner)
async def nothing(client: Client, message: Message):
    await copy_message(client, message)

@randydev(command("take", cmd) & owner)
async def lmao_this(client: Client, message: Message):
    await take_corret(client, message)

add_command_help("copy", [["copy [link]", "to copy link of public channel"]])
