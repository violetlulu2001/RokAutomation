import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = self.get_channel(1393861723647377528)  # Replace with your channel ID
        file_path = r'D:\RokAutomation\logs\violeta_logs\donate_techs_rss_163653653215.txt'  # Update with your file path
        if channel and os.path.exists(file_path):
            with open(file_path, 'r') as fp:
                await channel.send(file=discord.File(fp.read(), file_path))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['discorbot'])