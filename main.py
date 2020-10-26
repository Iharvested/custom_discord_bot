import discord, os, webserver
from webserver import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot



bot = commands.Bot(command_prefix="!")





keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
bot.run(TOKEN)