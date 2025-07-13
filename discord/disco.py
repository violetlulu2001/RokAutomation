import discord
import os
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == '!random_msg':
            messages = [
                "Hello there!",
                "How's everyone doing?",
                "Have a great day!",
                "Time for some fun!",
                "Discord is awesome!"
            ]
            await message.channel.send(random.choice(messages))



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])