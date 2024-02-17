import discord
from discord.ext import commands

def build_discord_client():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    return discord.Client(intents=intents)

def build_discord_bot(character):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    return commands.Bot(command_prefix=character, intents=intents)