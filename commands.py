from DnD.get_dnd_data import get_dnd_data
from time import sleep
import logger

class commands:
    client = {}
    servers = {}

    def __init__(self, client, servers):
        self.client = client
        self.servers = servers

    async def check_commands_list(self, message):
        command_string = message.content[1:]
        command_array = command_string.split(" ")
        if command_array[0].lower() in self.commands_dict:
            for x in range(0, len(command_array)):
                command_array[x] = command_array[x].lower()
            print(f'{message.author.name} used !{command_array[0]} in {message.guild.name}')
            await self.commands_dict[command_array[0]](self, message, command_array)

    async def dnd(self, message, command_array):
        try:
            channel = self.client.get_channel(message.channel.id)
            sent_message = await channel.send("Give me a moment...")
            reply_dict = get_dnd_data(command_array)
            if("message" in reply_dict):
                for reply in reply_dict['message']:
                    sleep(0.1)
                    await channel.send(reply)
                await sent_message.delete()
            elif("error" in reply_dict):
                await sent_message.edit(content=reply_dict['error'])
        except Exception as error:
            logger.log(error)

    async def hello(self, message, command_array):
        try:
            reply = f'Hello {message.author.mention}!'
            channel = self.client.get_channel(message.channel.id)
            await channel.send(reply)
        except Exception as error:
            logger.log(error)

    async def update_monster_battle_scoreboard(self, message, command_array):
        try:
            server_id = message.guild.id
            server = self.servers[server_id]
            channel = self.client.get_channel(message.channel.id)
            if server.monster_battles_scoreboard_enabled is False:
                await channel.send("The Monster Battle Scoreboard isn't enabled in this server!")
            else:
                sent_message = await channel.send("Updating the Monster Battles Scoreboard...")
                server.scoreboard.update_scoreboard()
                await sent_message.edit(content="The Monster Battles Scoreboard has been updated!")
        except Exception as error:
            logger.log(error)

    commands_dict = { 
        "dnd": dnd,
        "hello": hello,
        "monsterbattles": update_monster_battle_scoreboard
    }