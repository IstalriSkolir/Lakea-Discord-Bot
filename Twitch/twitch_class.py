from twitchAPI.twitch import Twitch
from twitchAPI import eventsub
import asyncio

class twitch_class:
    twitch = {}
    chat = {}
    app_id = ""
    app_secret = ""

    def __init__(self, app_id, app_secret) -> None:
        self.app_id = app_id
        self.app_secret = app_secret
        asyncio.run(self.create_socket_connection())

    async def create_socket_connection(self):
        self.twitch = await Twitch(self.app_id, self.app_secret)
        hook = eventsub("86.14.105.77:25565", self.app_id, 25565, self.twitch)
        hook.unsubscribe_all()
        hook.start()
        hook.listen_stream_online(887604311, self.streamer_goes_live)
        #Lakea Channel ID - 887604311
        #self.twitch.authenticate_app([])
        #events = twitchAPI.eventsub(self.twitch)
        print("RTEST")
        #eventsub.start()
        #self.chat = await Chat(self.twitch)

    async def streamer_goes_live(self, data: dict):
        print("TEST")
        print(data)