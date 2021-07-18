import discord
from discord.ext import commands


class Marker(commands.Cog):
    def __init__(self, bm):
        self.bm = bm

    @commands.command(name="bookmark", help="Bookmarks a message", aliases=["bm", "mark", "save"])
    async def bookmark(self, ctx, message):
        to_mark = message.content
        await ctx.member.send()
