#  Copyright (C) 2021 The Authors

from . import *


@BotzHub.on(
    events.NewMessage(incoming=True, pattern="^/start$", func=lambda e: e.is_private)
)
async def starter(event):
    user = await BotzHub.get_entity(event.sender_id)
    if not await check_user(event.sender_id):
        await add_user(event.sender_id)
    await event.reply(
        f"Salut {user.first_name} !\nJe peux encoder les fichiers Telegram en x265, envoie-moi simplement une vidéo.",
        buttons=[
            Button.url("Chaîne", url="https://t.me/BotzHub"),
            Button.url("Source", url="https://github.com/xditya/video-encoder-bot"),
        ],
    )