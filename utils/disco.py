import discord
import os
import time

from mouse_code import (change_city, join_rally)


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself
        if message.content.startswith('!rally_farms'):
            await message.channel.send('-------------------------------------------------------------------------------------- ')
            list_acc = [2, 3]
            for i in list_acc:
                await message.channel.send(f'Change city to LuluBot{i}')
                change_city(int(i))
                time.sleep(1)
                join_rally()
                await message.channel.send(f'Account LuluBot{i} from matrix joined rally.')
            await message.channel.send('Finish!')
            await message.channel.send('-------------------------------------------------------------------------------------- ')
        if message.content.startswith('!rally_main'):
            await message.channel.send(
                '-------------------------------------------------------------------------------------- ')
            list_acc = [1, 2, 3, 4, 5]
            for i in list_acc:
                await message.channel.send(f'Change city to LuluBot{i}')
                change_city(int(i))
                time.sleep(1)
                join_rally()
                await message.channel.send(f'Account LuluBot{i} from matrix joined rally.')
            await message.channel.send('Finish!')
            await message.channel.send(
                '-------------------------------------------------------------------------------------- ')
        if message.content.startswith("!slow_bui;l"):
            await message.channel.send('-------------------------------------------------------------------------------------- ')
            list_acc = [2, 3]
            for i in list_acc:
                await message.channel.send(f'Change city to LuluBot{i}')
                change_city(int(i))
                time.sleep(1)
                # Assuming there's a function to handle gold pit
                # join_gold_pit()  # Uncomment this line if you have a function for gold pit
                await message.channel.send(f'Account LuluBot{i} from matrix joined gold pit.')
            await message.channel.send('Finish!')
            await message.channel.send('-------------------------------------------------------------------------------------- ')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])