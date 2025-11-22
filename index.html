import discord
from discord.ext import commands

# ----- CONFIG -----
TOKEN = "MTQ0MTc5OTM3Njk2Mjk3Nzg2NQ.Gvo4dn.kkclAggeCm-yRlhXUKPvml-fLoH4GvsuRYRuaI"
GUILD_ID = 1431584219766718484  # Replace with your server ID
VRTEX_PLUS_ROLE_ID = 1431632890005028864  # Replace with your VRTEX+ role ID

intents = discord.Intents.default()
intents.members = True  # Needed to detect member updates and joins
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----- EVENT: Member Joins -----
@bot.event
async def on_member_join(member):
    # Check if member already has the VRTEX+ role
    role = discord.utils.get(member.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role in member.roles:
        try:
            await member.send(
                f"🎉 Welcome {member.name}! Thanks for subscribing to VRTEX+! "
                "Here’s your premium code and perks link: [YOUR_LINK_HERE]"
            )
        except discord.Forbidden:
            print(f"Cannot DM {member.name}. They might have DMs disabled.")

# ----- EVENT: Role Added -----
@bot.event
async def on_member_update(before, after):
    role = discord.utils.get(after.guild.roles, id=VRTEX_PLUS_ROLE_ID)
    if role not in before.roles and role in after.roles:
        # Role added -> Send DM
        try:
            await after.send(
                f"🎉 Hey {after.name}, you now have VRTEX+! "
                "Here’s your premium code and perks link: [YOUR_LINK_HERE]"
            )
        except discord.Forbidden:
            print(f"Cannot DM {after.name}. They might have DMs disabled.")

bot.run(TOKEN)
