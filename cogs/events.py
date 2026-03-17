import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, asuka):
        self.asuka = asuka

    @commands.Cog.listener() # Log bot activity
    async def on_ready(self):
        await self.asuka.change_presence(
            status = discord.Status.dnd,
            activity = discord.Activity(type = discord.ActivityType.watching, name = 'Neon Genesis Evangelion')
            )
        print('Asuka is awake!\n')

    @commands.Cog.listener() # Log messages
    async def on_message(self, message):
        if message.author == self.asuka.user:
            return

        print(f'From {message.author}: {message.content}')

    @commands.Cog.listener() # Disable error output in console
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return

def setup(asuka):
    asuka.add_cog(Events(asuka))