
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
LIKE_EMOJI = "👍"
DISLIKE_EMOJI = "👎"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

print("{0.user}".format(bot))




@bot.command()
async def poll(ctx: commands.Context, que, opt1, opt2):
    msg=f"{que}\n {LIKE_EMOJI}{opt1} \n {DISLIKE_EMOJI}{opt2}   "
    
    sent_msg=await ctx.send(msg)

    await sent_msg.add_reaction("👍")
    await sent_msg.add_reaction("👎")

bot.run(TOKEN)