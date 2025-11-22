import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# Load .env variables (optional if using Render environment variables)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Make sure this is set in Render

# ----- CONFIG -----
GUILD_ID = 1431584219766718484       # Replace with your server ID
VRTEX_PLUS_ROLE_ID = 1431632890005028864  # Replace with your VRTEX+ role ID

# ----- DISCORD SETUP -----
intents = discord.Intents.default()
intents.members = True  # Needed to detect member updates and joins
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----- EVENTS -----
@bot.event
async def on_ready():
    print(f"✅ {bot.user} has connected to Discord!")

@bot.event
async def on_member_update(before, after):
    """Send DM when someone receives the VRTEX+ role."""
    role = discord.utils.get(after.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role not in before.roles and role in after.roles:
        try:
            await after.send(
                f"🎉 Hey {after.name}, you now have VRTEX+! "
                "Here’s your premium code and perks link: [YOUR_LINK_HERE]"
            )
        except discord.Forbidden:
            print(f"Cannot DM {after.name}. They might have DMs disabled.")

@bot.event
async def on_member_join(member):
    """Send DM if member already has VRTEX+ role."""
    role = discord.utils.get(member.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role in member.roles:
        try:
            await member.send(
                f"🎉 Welcome {member.name}! Thanks for subscribing to VRTEX+! "
                "Here’s your premium code and perks link: [YOUR_LINK_HERE]"
            )
        except discord.Forbidden:
            print(f"Cannot DM {member.name}. They might have DMs disabled.")

# ----- OPTIONAL: KEEP-ALIVE WEB SERVER -----
app = Flask('')

@app.route('/')
def home():
    return "VRTEX+ Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run_web)
t.start()

# ----- RUN BOT -----
bot.run(TOKEN)
