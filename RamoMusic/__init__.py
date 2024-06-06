from RamoMusic.core.bot import Mody
from RamoMusic.core.dir import dirr
from RamoMusic.core.git import git
from RamoMusic.core.userbot import Userbot
from RamoMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Mody()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
