from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Assalamualaikum Dulu Sayang**")


@man_cmd(pattern="acu(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ACU ACU**")


@man_cmd(pattern="test(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**TEST TEST 1.. 2.. 3..**")


@man_cmd(pattern="plosok(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**PLOSOK DELAY TEROOOSS**")


@man_cmd(pattern="ck(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**CEWEK CEWEK DI CK PACAR GW SEMUA🐟**")

@man_cmd(pattern="bau(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**BAUUUUUUUUUUU MANDI DLU SANA**")


@man_cmd(pattern="cyg(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Minot🐻 cyg mana ya**")
    sleep(2)
    await xx.edit("**Apa cyg😱**")


@man_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**Wa'alaikumsalam Sayang**")


@man_cmd(pattern="maap(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Maap Yah**")
    sleep(2)
    await xx.edit("**Tapi Boong 😛**")


@man_cmd(pattern="bgst(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**KALO BISA BANYAK**")
    sleep(3)
    await xx.edit("**KENAPA HARUS SATU 🐟**")


@man_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Gw {owner}**")
    sleep(2)
    await xx.edit("**LU SEMUA BAU 🐟**")


@man_cmd(pattern="gtw(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Mana Saya Tau**")
    sleep(2)
    await xx.edit("**Saya Kan Cuma Ikan🐟**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
