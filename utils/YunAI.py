import discord
import os
import time

from mouse_code import (send_slow_build_af, change_city, join_rally, change_acct, open_game, close_game)


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself
        if message.content.startswith('main'):
            await message.channel.send('-------------------------------------------------------------------------------------- ')
            list_acc = [2, 3, 4, 5, 6, 7, 8]
            for i in list_acc:
                change_city(i)
                time.sleep(5)
                await message.channel.send(f'Change city to LuluBot{i}')
                join_rally()
            await message.channel.send(f'Account LuluBot{i} from matrix joined rally.')
            await message.channel.send('Finish!')
            await message.channel.send('-------------------------------------------------------------------------------------- ')

        if message.content.startswith("slowbuild"):
            await message.channel.send('-------------------------------------------------------------------------------------- ')
            list_acc = [1, 2, 3, 4, 5, 6, 7, 8]
            for i in list_acc:
                change_city(i)
                time.sleep(5)
                send_slow_build_af()
            change_acct()

        if message.content.startswith("opengame"):
            open_game()
            await message.channel.send('Game opened!')

        if message.content.startswith("vl"):
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")
            await message.channel.send("I've applied in VL61 alliance! Waiting for acceptation!")

        if message.content.startswith("closegame"):
            close_game()
            await message.channel.send('Game closed!')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])