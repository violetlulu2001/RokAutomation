import discord
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

CHANNEL_ID = 1393861723647377528  # Your channel ID
WATCH_DIR = r'D:\logs\violeta_logs'  # Folder to watch

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.channel = self.get_channel(CHANNEL_ID)

class FileCreatedHandler(FileSystemEventHandler):
    def __init__(self, client):
        self.client = client

    def on_created(self, event):
        if not event.is_directory:
            discord_file = discord.File(event.src_path)
            coro = self.client.channel.send(file=discord_file)
            discord.utils.run_coroutine_threadsafe(coro, self.client.loop)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

def start_watcher():
    event_handler = FileCreatedHandler(client)
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=False)
    observer.start()

start_watcher()
client.run(os.environ['discorbot'])