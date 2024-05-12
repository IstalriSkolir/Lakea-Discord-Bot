import os

class bot_settings:
    discord_token = ""
    path_seperator = ""
    twitch_app_id = ""
    twitch_app_secret = ""
    resource_path = ""

    def __init__(self) -> None:
        settings_dict = {}
        reader = open("setting_config.txt")
        lines = reader.read().splitlines()
        reader.close()
        for line in lines:
            parts = line.split(":", 1)
            settings_dict.update({parts[0]: parts[1]})
        self.discord_token = os.environ["DISCORD_BOT_TOKEN"]
        self.path_seperator = settings_dict["PATH_SEPERATOR"]
        self.resource_path = settings_dict["RESOURCE_PATH"]
        #self.twitch_app_id = os.environ["TWITCH_APP_ID"]
        #self.twitch_app_secret = os.environ["TWITCH_APP_SECRET"]