import os
import discord
from discord.ext import commands

ADMIN_ROLE_ID = 1457121772515098779  # Admin rol ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
async def dm(ctx, member: discord.Member, *, mesaj):

    # Admin kontrol
    if not any(role.id == ADMIN_ROLE_ID for role in ctx.author.roles):
        await ctx.send("❌ Bu komutu kullanamazsın.")
        return

    try:
        await member.send(mesaj)
        await ctx.send(f"✅ {member.mention} kişisine DM gönderildi.")
    except:
        await ctx.send("❌ Bu kişiye DM gönderilemiyor.")

bot.run(os.getenv("TOKEN"))
