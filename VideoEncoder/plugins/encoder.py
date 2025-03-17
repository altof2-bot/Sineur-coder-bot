#  Copyright (C) 2021 The Authors

from . import *


@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def encoder(event):
    if not (event.media or event.document):
        return
    if event.text and event.text.startswith("/"):
        return
    if event.media.document and event.media.document.mime_type not in video_mimetype:
        return await event.reply("`Vidéo invalide !\nAssurez-vous qu'il s'agit d'un fichier vidéo valide.`")
    await event.reply(
        f"`Ajouté à la file d'attente en position {len(data)}...\nVeuillez patienter...`"
    )
    data.append(event)
    if len(data) == 1:
        await add_task(event)