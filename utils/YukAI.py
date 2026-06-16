import discord
import os
import time

from mouse_code import (send_slow_build_af, change_city, join_rally, change_acct, open_game, close_game)



class MyClient(discord.Client):
    server_mc_status = False

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages from the bot itself
        if message.content.startswith('main'):
            await message.channel.send('-------------------------------------------------------------------------------------- ')
            list_acc = [1, 2, 3, 4, 5]
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
            list_acc = [1, 2, 3, 4, 5, ]
            for i in list_acc:
                change_city(i)
                time.sleep(5)
                send_slow_build_af()
            await message.channel.send('-------------------------------------------------------------------------------------- ')

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

        if message.content.startswith("!start_mc"):
            if not self.server_mc_status:
                await message.channel.send('Starting Minecraft server...')
                # Here you can add the code to start your Minecraft server
                time.sleep(6)
                await message.channel.send('starting port 62411')
                time.sleep(2)
                await message.channel.send('Minecraft server started!')
                await message.channel.send("IP: 192.168.0.174:62411")
                self.server_mc_status = True

        if message.content.startswith("!status_mc"):
            if self.server_mc_status:
                await message.channel.send('Minecraft server is running.')
            else:
                await message.channel.send('Minecraft server is not running.')

        if message.content.startswith("!stop_mc"):
            if self.server_mc_status:
                await message.channel.send('Stopping Minecraft server...')
                # Here you can add the code to stop your Minecraft server
                time.sleep(5)
                await message.channel.send('kill port 62411')
                time.sleep(2)
                await message.channel.send('Minecraft server stopped!')
                self.server_mc_status = False

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])