import discord, praw, random, requests, utils, http
from discord.ext import commands

reddit = praw.Reddit(client_id='GKg9xGGzV4vM9Q',
                     client_secret='FutzuRgQ-0-fFTlOsbbDeJPdcUg',
                     user_agent='Eternal City Bot by u/RedPhantomIRP')

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  @commands.command()
  async def memes(self, ctx):
    memes_submissions = reddit.subreddit(f'memes').hot()
    post_number = random.randint(1, 100)
    for i in range(0, post_number):
      submission = next(x for x in memes_submissions if not x.stickied)
    
    embed=discord.Embed(title=submission.title, colour=discord.Colour.green())
    embed.set_image(url=submission.url)
    all_comments = submission.comments
    embed.set_footer(text=f"Comments: {all_comments}")
    await ctx.send(embed=embed)

  @commands.command(aliases=['comp'])
  async def compliment(self, ctx, member : discord.User):
    response = requests.get("https://complimentr.com/api")
    pass_times = response.json()['compliment']

    embed=discord.Embed(title=pass_times, colour=discord.Colour.purple())
    embed.set_footer(text=f"{ctx.message.author} shared a little love to {member.name}")
    await member.send(embed=embed)
    await ctx.send("I've sent a bit of love their way!")
    
  
    
    
def setup(bot):
  bot.add_cog(Fun(bot))