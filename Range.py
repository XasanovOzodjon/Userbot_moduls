from pyrogram import Client, filters
import re
import asyncio

def register(app: Client):
    @app.on_message(filters.me)
    async def range_handler(client, message):
        if not message.text:
            return

        match = re.search(r"\*range\s+(\d+)", message.text)
        if match:
            try:
                repeat_count = int(match.group(1))

                # Agar reply qilingan bo‘lsa — o‘sha xabarni ko‘paytirish
                if message.reply_to_message:
                    for _ in range(repeat_count):
                        await client.copy_message(
                            chat_id=message.chat.id,
                            from_chat_id=message.chat.id,
                            message_id=message.reply_to_message.id
                        )
                        await asyncio.sleep(0.1)
                    await message.delete()
                else:
                    # Oddiy matnni ko‘paytirish
                    text_to_send = re.sub(r"\*Range\s+\d+", "", message.text).strip()
                    if text_to_send:
                        await message.delete()
                        for _ in range(repeat_count):
                            await client.send_message(message.chat.id, text_to_send)
                            await asyncio.sleep(0.1)

            except Exception as e:
                print(f"Xatolik: {e}")

    @app.on_message(filters.command("Range_help", prefixes="*") & filters.me)
    async def range_help(client, message):
        await message.reply(
            "🔁 `*Range <son>` — Xabarni <son> marta yuboradi.\n"
            "- Agar siz xabarga reply qilsangiz — reply qilingan xabarni nusxalaydi.\n"
            "- Agar reply bo‘lmasa — shu xabar matnini yuboradi.\n"
            "✅ Guruh va shaxsiy chatlarda ishlaydi.",
            quote=True
        )
        await message.delete()
