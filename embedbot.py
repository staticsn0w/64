#### 64 by isy ####

import discord
from discord.ext import commands
import asyncio
import aiohttp
import inspect
import os
import io
import json
import wand.image
import subprocess as sp
import codecs
import time

### /-- CONFIG --\ ###

### - here you can set the invoker. - ###
invoker = "+"

### - json shit - ###
with open('config.json') as c:
    jsonofabitch = json.load(c)
    email = jsonofabitch['email']
    password = jsonofabitch['password']

### - text arguments - ###
textargs = True

### - other shit - ###
bot = commands.Bot(command_prefix=invoker, self_bot=True)
startTime = time.time()


### - the good shit - ###
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name.encode("ascii","backslashreplace").decode())
    print(bot.user.id)
    print('------')
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    if textargs == True:
        if message.author == bot.user:	
            messagereplace = message.content.replace("{blob}","(b0w0)b").replace("{hug}","\\\\(^.^\\\\)").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)

async def getargs(content,splitby=1,pos=1):
    if len(content.split(' ', splitby)) >= pos + 1:
        return content.split(' ', splitby)[pos]
    return None

@bot.command(pass_context=True)
async def prefix(ctx):
   input = getargs(ctx.message.channel)
   invoker = input
   await bot.edit_message(ctx.message, ":thumbsup:")
   await ayncio.sleep(1)
   await bot.delete_message(ctx.message)

@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii","backslashreplace").decode())

@bot.command(pass_context=True)
async def sixtyfour(ctx):
    await bot.edit_message(ctx.message, "`Greetings, I am 64. I sometimes follow 35 around places.`")

def getargs(content,splitby=1,pos=1):
    if len(content.split(' ', splitby)) >= pos + 1:
        return content.split(' ', splitby)[pos]
    return None

@bot.command(pass_context=True)
async def clean(ctx, number: int, match_pattern: str = None):
    # Recources
    author = ctx.message.author
    channel = ctx.message.channel
    author = ctx.message.author
        
    if type(author) is discord.Member:
        me = channel.server.me
    # For Content Check
    use_re = (match_pattern and match_pattern.startswith('r(') and
              match_pattern.endswith(')'))
    if use_re:
        match_pattern = match_pattern[1:]  # strip 'r'
        match_re = re.compile(match_pattern)
        def content_match(c):
            return bool(match_re.match(c))
    elif match_pattern:
        def content_match(c):
            return match_pattern in c
    else:
        def content_match(_):
            return True

    def check(m):
        if m.author.id != bot.user.id:
            return False
        elif content_match(m.content):
            return True
        return False


    to_delete = []


    if author == bot.user:
        to_delete.append(ctx.message)
        number += 1

    tries_left = 5
    tmp = ctx.message

    while tries_left and len(to_delete) < number:
        async for message in bot.logs_from(channel, limit=100, before=tmp):
            if len(to_delete) < number and check(message):
                to_delete.append(message)
            tmp = message
        tries_left -= 1
    await slow_deletion(to_delete)



async def slow_deletion(messages):
    for message in messages:
        try:
            await bot.delete_message(message)
        except:
            pass

@bot.command(pass_context=True)
async def kill(ctx):
    await bot.edit_message(ctx.message, ":ok_hand:")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def lewd(ctx):
    await bot.edit_message(ctx.message, "`o-oh, aAh! mm...l-lewd...`")

@bot.command(pass_context=True)
async def gya(ctx):
    await bot.edit_message(ctx.message, "`road is gya`")
    await asyncio.sleep(0.2)
    await bot.edit_message(ctx.message, "`road's a girl`")
    await asyncio.sleep(0.2)
    await bot.edit_message(ctx.message, "`mufina is a cutie`")
    await asyncio.sleep(0.2)
    await bot.edit_message(ctx.message, "`ur`")
    await asyncio.sleep(0.2)
    await bot.add_reaction(ctx.message, '\U0001f1ec')
    await bot.add_reaction(ctx.message, '\U0001f1fe')
    await bot.add_reaction(ctx.message, '\U0001f1e6')
    gya = gya+1

@bot.command(pass_context=True)
async def p(ctx):
    cmdarg = ctx.message.content.split(" ",1)[1]
    await bot.change_presence(game=discord.Game(name=cmdarg))
    await bot.edit_message(ctx.message, ":thumbsup:")
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)
    p = p+1

@bot.command(pass_context=True)
async def f(ctx):
    await bot.edit_message(ctx.message, "`respects have been paid.`")
    await bot.add_reaction(ctx.message, '\U0001f1eb')
    f = f+1

@bot.command(pass_context=True)
async def n(ctx):
    cmdarg = ctx.message.content.split(" ",1)[1]
    await bot.change_nickname(ctx.message.server.me, cmdarg)
    await bot.edit_message(ctx.message, ":thumbsup:")
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def uptime(ctx):
    await bot.say(time.time() - startTime + " seconds.")

@bot.command(pass_context=True)
async def embed(ctx, *, asdf):
    if type(ctx.message.channel) == discord.PrivateChannel:
            em = discord.Embed(description=asdf, colour=0xFFFFFF)
            await bot.edit_message(ctx.message, "​", embed=em)
    else:
        if ctx.message.server.me.permissions_in(ctx.message.channel).embed_links == True:
            em = discord.Embed(description=asdf, colour=ctx.message.author.color)
            await bot.edit_message(ctx.message, "​", embed=em)
        else:
            await bot.say("I need the `embed links` permission to send an embed.")
			
@bot.command(pass_context=True, name='eval')
async def _eval(ctx, *, code : str):
    """Evaluates code."""
    code = code.strip('` ')
    python = '```py\n{}\n```'
    result = None

    env = {
        'ctx': ctx,
        'message': ctx.message,
        'server': ctx.message.server,
        'channel': ctx.message.channel,
        'author': ctx.message.author
    }

    env.update(globals())
 
    try:
        result = eval(code, env)
        if inspect.isawaitable(result):
            result = await result
    except Exception as e:
        await bot.say(python.format(type(e).__name__ + ': ' + str(e)))
        return
    await bot.say(python.format(result))
		
bot.run(email, password, bot=False)
