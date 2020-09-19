import discord, os, alive
from discord.ext import commands
#from discord.utils import get

client = commands.Bot(
  command_prefix = "2"
)
@client.event
async def on_ready():
    print('bot success')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you 24/7"))


@client.command()
async def ping(ctx):
  print('\'Ping\' command executed')
  await ctx.send(f'Ping: {round(client.latency*1000)}ms')

alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)