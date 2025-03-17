#  Copyright (C) 2021 The Authors

from . import *
import asyncio


@BotzHub.on(events.NewMessage(from_users=719195224, pattern="^/broadcast"))
async def _broadcast(event):
    await BotzHub.send_message(
        event.chat_id, "Envoyez le message que vous voulez diffuser !\nEnvoyez /cancel pour arrêter."
    )
    async with BotzHub.conversation(719195224) as conv:
        response = conv.wait_event(events.NewMessage(chats=719195224))
        response = await response
        themssg = response.message.message
    if themssg is None:
        await BotzHub.send_message(event.chat_id, "Une erreur s'est produite...")
    if themssg == "/cancel":
        await BotzHub.send_message(event.chat_id, "Diffusion annulée !")
        return
    targets = await all_users()
    users_cnt = len(targets)
    err = 0
    success = 0
    lmao = await BotzHub.send_message(
        event.chat_id, "Début de la diffusion vers {} utilisateurs.".format(users_cnt)
    )
    for ok in targets:
        try:
            await BotzHub.send_message(int(ok["user"]), themssg)
            success += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            err += 1
            print(e)
    done_mssg = """
Diffusion terminée !\n
Envoyé à `{}` utilisateurs.\n
Échec pour `{}` utilisateurs.\n
Nombre total d'utilisateurs du bot : `{}`.\n
""".format(
        success, err, users_cnt
    )
    await lmao.edit(done_mssg)


@BotzHub.on(events.NewMessage(from_users=719195224, pattern="^/stats"))
async def statt(event):
    users = len(await all_users())
    await event.reply(f"Statistiques :\nUtilisateurs : {users}")