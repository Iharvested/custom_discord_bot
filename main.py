import discord, os, webserver
from webserver import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot



bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
  bot.load_extension('cogs.Fun')
  bot.load_extension('cogs.Mod')


keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
bot.run(TOKEN)