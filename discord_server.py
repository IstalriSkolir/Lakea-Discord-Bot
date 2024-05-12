from Monster_Battles.monster_battle_scoreboards import monster_battles_scoreboard
import discord_server_config, logger

class server:
    settings = {}
    guild = {}
    client = {}
    scoreboard = {}
    id = ""
    name = ""
    member_join_channel = -1
    member_join_message = ""
    monster_battles_scoreboard_enabled = False

    def __init__(self, settings, guild, client, event_loop):
        self.settings = settings
        config = discord_server_config.load_server_config(guild.id, settings.path_seperator, settings.resource_path)
        self.client = client
        self.guild = guild
        self.id = guild.id
        self.name = guild.name
        if (config["member_join_channel"] != "-1"):
            self.member_join_channel = int(config["member_join_channel"])
            self.member_join_message = config["member_join_message"]
        if(config["monster_battles_scoreboard_channel"] != "DISABLED"):
            self.monster_battles_scoreboard_enabled = True
            self.scoreboard = monster_battles_scoreboard(settings, client, self.name, int(config["monster_battles_scoreboard_channel"]), config["monster_battles_characters_path"], event_loop)

    async def send_welcome_message(self, member):
        if (self.member_join_channel != -1):
            try:
                message = self.member_join_message
                if r"{member}" in message:
                    message = message.replace(r"{member}", member.mention)
                channel = self.client.get_channel(self.member_join_channel)
                await channel.send(message)
            except Exception as error:
                print("Error sending welcome message: " + str(error))
                logger.log(error)