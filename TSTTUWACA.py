from telethon import TelegramClient, events, functions, types #Not sure if all these are required but whatever
from openai import OpenAI
import subprocess
import tempfile
import asyncio
import config
import os

client = TelegramClient('tsttuwaca', config.app_id, config.app_hash, connection_retries=None, retry_delay=15).start(bot_token=config.token)
ai_client = OpenAI(api_key=config.api_key)

async def process_message(event):
    msg = event.message
    if msg.voice or msg.video_note:
        message = await event.reply("📥")
    else:
        return
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        await msg.download_media(file=tmp_file.name)
        tmp_path = await convert_to_mp3(tmp_file.name)
        await message.edit("🔄")
    try:
        response = await asyncio.to_thread(transcribe, tmp_path)
        print(response)
        if response.text == "":
            await message.edit("❌️")
        else:
            await message.edit(response.text)
    except Exception as e:
        await message.edit("⚠️")
        print(e)

def transcribe(file_path):
    with open(file_path, "rb") as audio_file:
        return ai_client.audio.transcriptions.create(
            file=audio_file, 
            model="gpt-4o-transcribe",
        )

async def convert_to_mp3(input_path):
    output_path = input_path.replace(".mp3", "_conv.mp3")
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vn",
        "-acodec", "libmp3lame",
        "-ar", "44100",
        "-ac", "1",
        output_path
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    await process.communicate()
    os.remove(input_path)
    return output_path

async def main():
    me = await client.get_me()
    config.bot_name = me.first_name
    config.bot_username = me.username
    config.bot_id = me.id
    print(f'Connected to {config.bot_name} in @{config.bot_username}')

@client.on(events.NewMessage())
async def handle_messages(event):
    await process_message(event)

try:
    print('(Press Ctrl+C to stop this)')
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
finally:
    client.disconnect()