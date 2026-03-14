# Asuka is the greatest
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

asuka = commands.Bot(command_prefix='>', intents = discord.Intents.all())

asuka.load_extension('cogs.events')
asuka.load_extension('cogs.commands')
asuka.run(str(os.getenv('token')))