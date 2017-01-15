# betterEmbedBot 1.0 by @isy#0669

#### -- CONFIG -- ###

# Here you can set the invoker.
# Example: invoker = "."
# That will make your commands start with ., Like .embeds
invoker = "."

# Replace asdf with your email and password. Put them in quotes.
# Example:
# email = "mufin@is.cute"
# password = "iwannahughim"
email = asdf
password = asdf

# If you like tokens
# bot.run(asdf, bot=False)
# To get your token, press CTRL + SHIFT + I, Click on "Application", under "Storage" click on "Local storage", Click the link under that.
# Copy the token part (Don't show anyone your token), and replace asdf in "token = asdf" with your actual token.
# Make sure to put it in quotes.

### - Text arguments - ###
# If you want stuff like "hello {hug}" to be replaced with "hello \(^.^\)", leave this on.
textargs = True
#textargs = False

# Don't touch below this line.

import discord
from discord.ext import commands
import asyncio
import inspect

bot = commands.Bot(command_prefix=invoker, self_bot=True)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name.encode("ascii","backslashreplace").decode())
    print(bot.user.id)
    print('------')
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")

@bot.event
async def on_message(message):
    if textargs == True:
        if message.author == bot.user:	
            messagereplace = message.content.replace("{blob}","(b0w0)b").replace("{hug}","\\\\(^.^\\\\)").replace("{lenny}","( ͡° ͜ʖ ͡°)").replace("{disapprove}","ಠ\_ಠ").replace("{tableflip}","(╯°□°）╯︵ ┻━┻").replace("{unflip}","┬─┬﻿ ノ( ゜-゜ノ)").replace("{unflip2}","​┬─┬ノ( º ⁓ ºノ)").replace("{unflip3}","┬─┬ノ( º _ ºノ)").replace("{cute}","(◕‿◕✿)").replace("{zwsp}","​").replace("{rtl}","\u202e")
            if not message.content == messagereplace:
                await bot.edit_message(message, messagereplace)
    await bot.process_commands(message)
						
@bot.command(pass_context=True, name="print")
async def _print(ctx, asdf):
    print(asdf.encode("ascii","backslashreplace").decode())

@bot.command(pass_context=True)
async def kill(ctx):
    await bot.edit_message(ctx.message, ":ok_hand:")
    await asyncio.sleep(1)
    await bot.logout()

@bot.command(pass_context=True)
async def lewd(ctx):
    await bot.edit_message(ctx.message, "`o-oh, aAh! mm, l-lewd...`")

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

@bot.command(pass_context=True)
async def e(ctx):
    emoji = ctx.message.content.split(" ",1)[1]
    if emoji == "sop":
        await bot.delete_message(ctx.message)
        await bot.send_file(channel, "sop.png")

@bot.command(pass_context=True)
async def p(ctx):
    cmdarg = ctx.message.content.split(" ",1)[1]
    await bot.change_presence(game=discord.Game(name=cmdarg))
    await bot.edit_message(ctx.message, ":thumbsup:")
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def f(ctx):
    await bot.edit_message(ctx.message, "`respects have been paid.`")
    await bot.add_reaction(ctx.message, '\U0001f1eb')

@bot.command(pass_context=True)
async def reboot(ctx):
    await bot.say("rebooting...")
    await asyncio.sleep(1)
    await bot.logout()
    await bot.run(email, password, bot=False)
    await asyncio.sleep(1)
    await bot.say("owo")

@bot.command(pass_context=True)
async def n(ctx):
    cmdarg = ctx.message.content.split(" ",1)[1]
    await bot.change_nickname(ctx.message.server.me, cmdarg)
    await bot.edit_message(ctx.message, ":thumbsup:")
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hi! o/")

@bot.command(pass_context=True)
async def u(ctx):
    cmdarg = ctx.message.content.split(" ",1)[1]
    await bot.edit_profile(password="", username=cmdarg) #add your password in the empty quotes
    await bot.edit_message(ctx.message, ":thumbsup:")
    await asyncio.sleep(1)
    await bot.delete_message(ctx.message)
@bot.command(pass_context=True)
async def embeds(ctx, *, asdf):
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
