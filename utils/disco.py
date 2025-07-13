import time
import discord
import os

from utils.util_function import get_random_fiddle_stick

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = self.get_channel("1393749793591001118")
        while channel:
            time.sleep(5)
            await channel.send(get_random_fiddle_stick())

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')





intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])