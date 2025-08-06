from pyrogram import filters

def register_test_cmd(app):
    @app.on_message(filters.me & filters.command("ping", prefixes="*"))
    async def ping(_, message):
        await message.reply("🏓 Pong!")
