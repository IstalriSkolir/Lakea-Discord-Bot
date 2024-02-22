import threading, os, logger, asyncio, discord
from Monster_Battles.character import character
from Monster_Battles.create_scoreboard_image import *

class monster_battles_scoreboard:
    settings = {}
    client = {}
    ticker = {}
    event_loop = {}
    characters_path = ""
    guild_name = ""
    channel = -1
    update_delay = 86400

    def __init__(self, settings, client, guild, channel, characters_path, event_loop):
        self.settings = settings
        self.client = client
        self.guild_name = guild
        self.channel = channel
        self.characters_path = characters_path
        self.event_loop = event_loop
        new_thread = threading.Thread(target=self.initialise, args=[])
        new_thread.daemon = True
        new_thread.start()

    def initialise(self):
        self.ticker = threading.Event()
        while not self.ticker.wait(self.update_delay):
            try:
                self.update_scoreboard()
            except Exception as error:
                logger.log(error)
                print(str(error))

    def update_scoreboard(self):
        print("Updating Scoreboard in " + self.guild_name + "...")
        characters = self.get_character_list(self.characters_path)
        print("Sorting by Level...")
        characters = sorted(characters, key = lambda x: (x.level, x.xp), reverse=True)
        characters = characters[:10]
        print("Creating New Scoreboard...")
        image = create_scoreboard(characters, self.settings.path_seperator)
        print("Updating Scoreboard Message...")
        asyncio.run_coroutine_threadsafe(self.update_scoreboard_message(image), self.event_loop)

    def get_character_list(self, characters_path):
        characters = []
        for file in os.listdir(characters_path):
            try:
                print("Loading " + file)
                seperator = self.settings.path_seperator
                new_character = character(f"{characters_path}{seperator}{file}")
                characters.append(new_character)
            except Exception as error:
                print("Error Getting Character " + file + ": " + str(error))
                logger.log(error)
        return characters
    
    def create_message_string(self, characters):
        message = "# __*RANGER LEVEL SCOREBOARD*__\n"
        for x in range(len(characters)):
            message = message + "\n" + str(x + 1) + ". " + characters[x].name + " - Level " + str(characters[x].level) + " - XP: " + str(characters[x].xp)    
        return message
    
    async def update_scoreboard_message(self, message):
        try:
            channel = self.client.get_channel(self.channel)
            last_message = await channel.fetch_message(channel.last_message_id)
            if(last_message.author.id == self.client.user.id):
                await last_message.edit(attachments=[discord.File(message)])
            else:       
                await channel.send(file=discord.File(message))
            print("Scoreboard in " + self.guild_name + " Updated")
        except Exception as error:
            print(str(error))
            logger.log(error)
