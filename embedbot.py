# Embedbot 1.0 made by -Kiwi Catnip ♡#1540s

#### -- CONFIG -- ###

# Here you can set the invoker.
# Example: invoker = "*"
# That will make your commands start with *. Like *embeds
invoker = "*"

# Replace asdf with your email and password. Put them in quotes.
# Example:
# email = "Killer@keem.star"
# password = "heywhatsupguysitsscarcehere"
email = asdf
password = asdf

# If you like tokens
# bot.run(asdf, bot=False)
# To get your token, press CTRL + SHIFT + I, Click on "Application", under "Storage" click on "Local storage", Click the link under that.
# Copy the token part (Don't show anyone your token), and replace asdf in "token = asdf" with your actual token.
# Make sure to put it in quotes.



# Don't touch below this line.

import discord
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix=invoker, self_bot=True)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.remove_command("help")
    bot.remove_command("HelpFormatter")


@bot.command(pass_context=True)
async def kill(ctx):
    await bot.say("Killed. You can run the bot again by clicking on the file.")
    await asyncio.sleep(1)
    await bot.logout()

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

bot.run(email, password, bot=False)
