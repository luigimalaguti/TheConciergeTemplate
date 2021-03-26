from telethon import events


@events.register(events.NewMessage())
async def handler(event):
    await event.respond(event.text)
