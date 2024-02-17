import discord_object_builder, asyncio
from bot_settings import bot_settings
from discord_server import server
from commands import commands
from Twitch.twitch_class import twitch_class

settings = bot_settings()
servers = {}
client = discord_object_builder.build_discord_client()
bot = discord_object_builder.build_discord_bot('!')
command = commands(client, servers)
#twitch = twitch_class(settings.twitch_app_id, settings.twitch_app_secret)

@client.event
async def on_guild_join(guild):
    print(f'Lakea joined {guild.name}')
    pass

client.event
async def on_guild_remove(guild):
    print(f'Lakea left {guild.name}')
    pass

@client.event
async def on_member_join(member):
    global servers
    print(f'{member.name} joined {member.guild}')
    await servers[member.guild.id].send_welcome_message(member)

@client.event
async def on_member_remove(member):
    print(f'{member.name} left {member.guild}')
    pass

@client.event
async def on_message(message):
    if(len(message.content) > 0 and message.content[0] == '!'):
        await command.check_commands_list(message)

@client.event
async def on_ready():
    global servers
    event_loop = asyncio.get_running_loop()
    print("Getting Servers...")
    x = 0
    for guild in client.guilds:
        x = x + 1
        print(f'{x}. {guild.name} -> {guild.member_count} members')
        servers.update({guild.id: server(settings, guild, client, event_loop)})
    print("Servers Connected: " + str(len(servers)))

@bot.command(name='testing')
async def test(ctx):
    pass

print("Starting Lakea...")
client.run(settings.discord_token)
bot.run(settings.discord_token)