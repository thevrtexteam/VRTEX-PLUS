# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ----- CONFIG -----
GUILD_ID = 1431584219766718484  # Replace with your server ID
VRTEX_PLUS_ROLE_ID = 1431632890005028864  # Replace with your VRTEX+ role ID
PERKS_LINK = "https://your-perks-link.com"  # Replace with your premium perks link

# ----- INTENTS -----
intents = discord.Intents.default()
intents.members = True  # Needed to detect member updates and joins
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----- EVENT: Member Joins -----
@bot.event
async def on_member_join(member):
    if member.guild.id != GUILD_ID:
        return

    role = discord.utils.get(member.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role in member.roles:
        try:
            await member.send(
                f"🎉 Welcome {member.name}! Thanks for subscribing to VRTEX+!\n"
                f"Here’s your premium perks link: {PERKS_LINK}"
            )
        except discord.Forbidden:
            print(f"Cannot DM {member.name}. They might have DMs disabled.")

# ----- EVENT: Role Added -----
@bot.event
async def on_member_update(before, after):
    if after.guild.id != GUILD_ID:
        return

    role = discord.utils.get(after.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role not in before.roles and role in after.roles:
        try:
            await after.send(
                f"🎉 Hey {after.name}, you now have VRTEX+!\n"
                f"Here’s your premium perks link: {PERKS_LINK}"
            )
        except discord.Forbidden:
            print(f"Cannot DM {after.name}. They might have DMs disabled.")

# ----- READY EVENT -----
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    print("VRTEX+ bot is running...")

# Run the bot
bot.run(TOKEN)
