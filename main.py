import discord, os, alive
from discord.ext import commands
#from discord.utils import get

client = commands.Bot(
  command_prefix = "ANY PREFIX YOU WANT"
)
@client.event
async def on_ready():
    print('bot success')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOUR WATCHING HERE"))
    #await bot.change_presence(activity=discord.Game(name="YOUR GAME HERE"))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="YOUR SONG HERE"))
    #await bot.change_presence(activity=discord.Streaming(name="STREAM TITLE HERE", url="TWITCH URL HERE"))
    #Only one at a time and only delete the '#' to change it (Fun Fact: Watching status is only for bots right now, but users can use it too!)


@client.command()
async def ping(ctx):
  print('\'Ping\' command executed')
  await ctx.send(f'Ping: {round(client.latency*1000)}ms')

alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
