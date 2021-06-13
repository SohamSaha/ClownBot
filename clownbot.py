import discord
from discord.ext import commands
import mongodb as mongo
import os

client = commands.Bot(command_prefix='c.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def regrets(ctx):
    e = discord.Embed(description='Foolish mortal, shed your consciousness and place thy useless mortal coil on the cushioned horizontal surface plebians call a bed')
    formattedURL = str(list(mongo.get_link('Sneer', 'name', 'sneer_cat').values()))
    formattedURL = formattedURL.strip('[]').strip("''")
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def clown(ctx):
    e = discord.Embed()
    formattedURL = str(list(mongo.get_link('Clown', 'name', 'clown_shoes').values()))
    formattedURL = formattedURL.strip('[]').strip("''")
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def high(ctx):
    e = discord.Embed()
    formattedURL = str(list(mongo.get_link('Cats', 'name', 'high_cat').values()))
    formattedURL = formattedURL.strip('[]').strip("''")
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def sad(ctx):
    e = discord.Embed()
    formattedURL = str(list(mongo.get_link('Cats', 'name', 'sad_cat').values()))
    formattedURL = formattedURL.strip('[]').strip("''")
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

client.run(os.environ['CLOWNBOT_API_KEY'])