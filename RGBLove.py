from pyrogram import Client, filters
import asyncio

hearts = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🤎", "🖤"]

def register(app: Client):  # <<—— BU YERDA NOM TO‘G‘RILANDI
    @app.on_message(filters.me & filters.private & filters.text & filters.regex(r"^\*RGBLove$"))
    async def rgb_love_handler(client, message):
        await message.delete()
        edited_msg = await client.send_message(chat_id=message.chat.id, text="❤️")
        last_heart = "❤️"
        for _ in range(10):
            for heart in hearts:
                if heart != last_heart:
                    try:
                        await edited_msg.edit_text(heart)
                        last_heart = heart
                        await asyncio.sleep(0.2)
                    except Exception as e:
                        print(f"Xatolik: {e}")
                        continue
