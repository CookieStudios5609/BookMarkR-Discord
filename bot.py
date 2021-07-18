import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bm = commands.Bot(command_prefix=os.getenv("PREFIX"))


@bm.event
async def on_ready():
    print(f"{bm.user} has connected. Thanks for using BookMarkR.")

bm.load_extension("marker")

bm.run(os.getenv("TOKEN"))