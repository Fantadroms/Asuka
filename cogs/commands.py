import random
from discord.ext import commands

gifs = {
    't': ['bIhHcZYtaWrsJhLwOn0', 'VjgKS1cmwYsWtP8SyN', 'eSZHdKNRKPBf9n62Ux', 'J4eHalq440CRmCKfHW', '9UsK1zvxpJh4YHXC4Y', 'aNkGzZJbDozZtmdZ7D', 'YVT4w8N5O7qSiftMNq'],
    'f': ['lVrwaz7p7aSoCiPLHl', '8Yf8E09iJGOR4HjWQx', 'UCqCTLr6T1WtJatsLn', 'jUOKWgovxabx5JmlJu', 'DMVPvOIRovYfc2jYMO', 'UpGRkVDCBSTPS3Sd5b']
}

class Commands(commands.Cog):
    def __init__(self, asuka):
        self.asuka = asuka

    @commands.command()
    async def play(self, ctx, *, num: str):
        if not num.isdigit():
            await ctx.send('That is not a number idiot!')
            return

        won = int(num) == random.randint(1, 999)
        gif = random.choice(gifs['t' if won else 'f'])
        await ctx.send(f'https://giphy.com/embed/{gif}')
    
def setup(asuka):
    asuka.add_cog(Commands(asuka))