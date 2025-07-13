import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = self.get_channel(1393861723647377528)
        file_path = r'D:\RokAutomation\logs\violeta_logs\donate_techs_rss_163653653215.txt'
        if channel and os.path.exists(file_path):
            await channel.send(file=discord.File(file_path))
        else:
            print('Channel not found or file does not exist.')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])