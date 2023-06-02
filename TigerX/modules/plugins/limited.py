from TigerX import *
from TigerX.lib import *

from pykillerx.help import *

@randydev(command(["limit", "limited"], cmd) & owner)
async def spamban_command(client: Client, m: Message):
    await spamban(client, m)

add_command_help(
    "limited", [["limit or .limited", "Check Limit telegram from @SpamBot."]]
)
