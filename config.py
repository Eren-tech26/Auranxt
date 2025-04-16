import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "22947486"))
API_HASH = getenv("API_HASH", "8dd4fdb161d4db0b7e3c9125face91e4)
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-lumimaxprobot-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7950194495:AAGZXkp45pJNlJvswNZKOlaSkDHxZWhqkXs")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://anandcollage245:ZehHlJTPgnFr8AjH@cluster0.t7w7l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002314716068))

OWNER_ID = int(getenv("OWNER_ID", 8101159354))

OWNER = int(getenv("OWNER", 8101159354))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-244ce902-f5e3-4c52-94d6-b5c4bb4ab7e5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SONGSONG220/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aethonixsupport")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/igrischatsupport")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQFeJp4AGW82QD5BnswNjVMGpDh6GyuNwYknSN5HREvGZjgdoa3rw_u8wV2JBXu2ZAXjDUiXne0lzWzs9JUyz0bPuEOWxyNpK1AI0EYHuL8f3S8JmelGDaWmIHJ4YBZvFE3E7YxVtSCZinXYVh_hx5RYnTSSG5rIn4oWn74PwORlEiCeuycEZG2JdVcyFzdtxMKyZj5atDWz_5GZ-MHcEahuxRq3r2MKqu7nWlOYKCZuWx6H_ZdVaOx3-KehSK213uf1EEH03Gom_LT7wekKDGOfuW0Uv0vtefgXyXUXIiQnMV8RMUhJf0GGuKPabeLwx3-hm3Pmmjfzp0uGOvtjL4eaBzHPFgAAAAHiBHksAA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://i.ibb.co/gM5BWMWk/photo-2025-03-08-03-25-47-7479274723772203012.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://i.ibb.co/mFTrdF86/photo-2025-03-08-03-26-14-7479274839736320004.jpg")
PLAYLIST_IMG_URL = "https://i.ibb.co/B28pqqm2/photo-2025-03-08-03-24-55-7479274496138936324.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://i.ibb.co/VYH59y7G/photo-2025-03-08-03-26-39-7479274942815535116.jpg")
TELEGRAM_AUDIO_URL = "https://i.ibb.co/LzB1Ttxg/photo-2025-03-08-03-28-36-7479275445326708748.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/39Sr0kgJ/photo-2025-03-08-03-29-42-7479275728794550280.jpg"
STREAM_IMG_URL = "https://i.ibb.co/C56snX9W/photo-2025-03-08-03-27-11-7479275084549455876.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/HLkP8Y4L/photo-2025-03-08-03-30-04-7479275827578798084.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/PzD50GJy/photo-2025-03-08-03-30-41-7479275982197620744.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/kgBYJwNq/photo-2025-03-08-03-33-08-7479276617852780548.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/kgBYJwNq/photo-2025-03-08-03-33-08-7479276617852780548.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/kgBYJwNq/photo-2025-03-08-03-33-08-7479276617852780548.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
