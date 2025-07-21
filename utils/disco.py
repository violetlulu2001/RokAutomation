import discord
import os
import time

from utils.mouse_code import (change_city, join_rally)


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself
        if message.content.startswith('!rally'):
            await message.channel.send('Rally ')
            list_acc = [2, 3]
            for i in list_acc:
                change_city(int(i))
                time.sleep(1)
                join_rally()
            await message.channel.send('Finish!')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])