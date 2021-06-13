import discord
import mongodb as mongo
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix='c.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def regrets(ctx):
    e = discord.Embed(description='Foolish mortal, shed your consciousness and place thy useless mortal coil on the cushioned horizontal surface plebians call a bed')
    formattedURL = mongo.get_value('Sneer', 'name', 'sneer_cat', 'link')
    formattedURL = formattedURL['link']
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def clown(ctx):
    e = discord.Embed()
    formattedURL = mongo.get_value('Clown', 'name', 'clown_shoes', 'link')
    formattedURL = formattedURL['link']
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def high(ctx):
    e = discord.Embed()
    formattedURL = mongo.get_value('Cats', 'name', 'high_cat', 'link')
    formattedURL = formattedURL['link']
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def sad(ctx):
    e = discord.Embed()
    formattedURL = mongo.get_value('Cats', 'name', 'sad_cat', 'link')
    formattedURL = formattedURL['link']
    e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def londa(ctx):
    e = discord.Embed()
    selection = random.randint(1, mongo.get_collection_length('Londa'))
    selection = str(selection)
    data_type = mongo.get_value('Londa', 'internal_id', selection, 'type')
    if (data_type['type'] == 'text'):
        db_text = mongo.get_value('Londa', 'internal_id', selection, 'text')
        e.description = db_text['text']
    if (data_type['type'] == 'picture'):
        formattedURL = mongo.get_value('Londa', 'internal_id', selection, 'link')
        formattedURL = formattedURL['link']
        e.set_image(url=formattedURL)
    await ctx.send(embed = e)

@client.command()
async def pun(ctx):
    e = discord.Embed()
    selection = random.randint(1, mongo.get_collection_length('Puns'))
    selection = str(selection)
    db_text = mongo.get_value('Puns', 'internal_id', selection, 'text')
    e.description = db_text['text']
    await ctx.send(embed = e)

@client.command()
async def callout(ctx, target: discord.Member, *, reason):
    return

client.run(os.environ['CLOWNBOT_API_KEY'])