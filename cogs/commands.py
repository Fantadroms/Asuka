import random
import discord
from discord.ext import commands

gifs = {
    't': ['bIhHcZYtaWrsJhLwOn0', 'VjgKS1cmwYsWtP8SyN', 'eSZHdKNRKPBf9n62Ux', 'J4eHalq440CRmCKfHW', '9UsK1zvxpJh4YHXC4Y', 'aNkGzZJbDozZtmdZ7D', 'YVT4w8N5O7qSiftMNq', 'mtRDnQYsOA5DyMxsgn'],
    'f': ['lVrwaz7p7aSoCiPLHl', '8Yf8E09iJGOR4HjWQx', 'UCqCTLr6T1WtJatsLn', 'jUOKWgovxabx5JmlJu', 'DMVPvOIRovYfc2jYMO', 'UpGRkVDCBSTPS3Sd5b', 'Ij5kcfI6YwcPCN26U2']
}
pitty = {}

class Commands(commands.Cog):
    def __init__(self, asuka):
        self.asuka = asuka

    @commands.command() # Number guessing game
    async def play(self, ctx, num: str):
        if not num.isdigit():
            await ctx.send('That is not a number idiot!')
            return
        
        user_id = ctx.author.id
        pitty[user_id] = pitty.get(user_id, 0)

        if pitty[user_id] >= 333:
            pitty[user_id] = 0
            gif = random.choice(gifs['t'])
        else:
            won = int(num) == random.randint(1, 999)
            if won:
                pitty[user_id] = 0
            else:
                pitty[user_id] += 1

            gif = random.choice(gifs['t' if won else 'f'])
        
        await ctx.send(f'https://giphy.com/embed/{gif}')
    
    @commands.command() # Reply with the same message
    async def echo(self, ctx, *, message):
        await ctx.send(message)
    
    @commands.command() # Reply with the users avatar
    async def fetch(self, ctx, user_name: discord.Member):
        await ctx.send(user_name.display_avatar)
    
    @commands.command() # Reply with the users pitty
    async def pitty(self, ctx):
        user_id = ctx.author.id
        await ctx.send(f'Your pitty is: {pitty[user_id]}')
    
def setup(asuka):
    asuka.add_cog(Commands(asuka))