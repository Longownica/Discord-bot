import os
import pathlib
from dotenv import load_dotenv

load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
BASE_DIR = pathlib.Path(__file__).parent
MCOG_DIR = BASE_DIR / "music-cog"
CMDS_DIR = BASE_DIR / "cmds"
EVENT_DIR = BASE_DIR / "event-cog"