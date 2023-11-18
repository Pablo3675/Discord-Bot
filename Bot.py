import discord
import os 
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Help(ctx):
    await ctx.send("Mi lista de conandos es:\n1- $hello\n2- $heh\n3- $coin\n4- $userinfo\n5- $mem")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def coin(ctx, coin_game = ["cara", "sello"]):
    await ctx.send(random.choice(coin_game))

@bot.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    user_id = user.id
    username = user.name
    avatar = user.display_avatar.url
    await ctx.send(f'User found: {user_id} -- {username}\n{avatar}')

@bot.command()
async def mem(ctx):
    meme_carpeta = "Kodland Python\Memes"
    meme_archivos = [f for f in os.listdir(meme_carpeta)]
    meme_random = os.path.join(meme_carpeta, random.choice(meme_archivos))
    with open(meme_random, 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


bot.run("TOKEN HERE")
