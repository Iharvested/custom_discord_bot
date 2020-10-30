import discord, praw, random
from discord.ext import commands


class Mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.member, *reason):
    if member == ctx.author:
      embedusererror=discord.Embed(title="Moff bot | Error!", description="You cannot ban yourself, sorry bud.")
      await ctx.send(embed=embedusererror)
    try:
      sucsessfulembed=discord.Embed(title=f"Banned {0}".format(member.name), description="")
    
    
def setup(bot):
  bot.add_cog(Mod(bot))