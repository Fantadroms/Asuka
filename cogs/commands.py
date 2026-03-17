import random
import discord
from discord.ext import commands

gifs = {
    't': ['0WxwM99JwOWxEv3wm4', 'ENXpjGPv1WO5ih4LkI', 'aDyXJgRw5Mlx3KZHNh', 'A0GS45ysBOw0uRdVH2', 'qnGlzxPVKauJdZeU7A'],
    'f': ['lVrwaz7p7aSoCiPLHl', '8Yf8E09iJGOR4HjWQx', 'UCqCTLr6T1WtJatsLn', 'jUOKWgovxabx5JmlJu', 'DMVPvOIRovYfc2jYMO', 'UpGRkVDCBSTPS3Sd5b', 'Ij5kcfI6YwcPCN26U2', 'uZUSOIa6L70qIPFNAQ', ]
}
usr_data = {}

class Commands(commands.Cog):
    def __init__(self, asuka):
        self.asuka = asuka

    @commands.command(name='play', description='A game where you guess a number.') # Number guessing game
    async def play(self, ctx, num: str):
        if not num.isdigit():
            await ctx.send('That is not a number idiot!')
            return
        
        usr_id = ctx.author.id
        if usr_id not in usr_data:
            usr_data[usr_id] = {'pity': 999, 'wins': 0}
        
        winning_number = random.randint(1, 999)

        if not (1 <= int(num) <= 999):
            await ctx.send('Idiot!')
            return
        
        if winning_number == int(num) or usr_data[usr_id]['pity'] <= 0:
            usr_data[usr_id]['pity'] = 999
            usr_data[usr_id]['wins'] += 1
            await ctx.send(f'https://giphy.com/embed/{random.choice(gifs['t'])}')
        else:
            usr_data[usr_id]['pity'] -= 1
            await ctx.send(f'https://giphy.com/embed/{random.choice(gifs['f'])}')
    
    @commands.command(name='echo', description='Asuka will reply with your message.') # Reply with the same message
    async def echo(self, ctx, *, message):
        await ctx.send(message)
    
    @commands.command(name='fetch', description='Asuka will reply with a users avatar.') # Reply with the users avatar
    async def fetch(self, ctx, user_name: discord.Member):
        await ctx.send(user_name.display_avatar)
    
    @commands.command(name='stats', description='Asuka will reply with your pity and wins.') # Reply with the users pity and wins
    async def stats(self, ctx):
        usr_id = ctx.author.id

        if usr_id not in usr_data:
            await ctx.send('Stupid idiot! Go play my game!')
            return

        await ctx.send(f'Your pity is {usr_data[ctx.author.id]['pity']} and you have {usr_data[ctx.author.id]['wins']} wins.')
        print(usr_data)
    
    @commands.command(name='choose', description='Asuka will choose on of the two.') # Reply with the users avatar
    async def choose(self, ctx, option1, option2):
        await ctx.reply(random.choice([option1, option2]))
    
def setup(asuka):
    asuka.add_cog(Commands(asuka))