import os
import random
import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def moneda(ctx):
    x=random.randint(1,2)
    await ctx.send(x)
    if x==1:
        await ctx.send(f"GANASTE {x}")
    else:
        await ctx.send(f"PERDISTE {x}")
@bot.command()
async def meme(ctx):
    with open('clase 5/memes/meme1.jpg', 'rb') as f:
        #¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

    with open('clase 5/memes/meme2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    with open('clase 5/memes/meme3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    with open('clase 5/memes/meme4.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def lista_memes(ctx):
    carpeta = os.listdir("memes")
    enviar_meme = random.choice(carpeta)

    with open(f'clase 5/memes/{enviar_meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    if res.text.strip():
        data = res.json()
        if "url" in data:
            return data["url"]
    else:
        return None

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    if image_url:  # Verificar que se haya obtenido una URL válida
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener una imagen")

@bot.command('animales')
async def random_animales(ctx):
    # Enviar un meme aleatorio de la carpeta de animales
    carpeta = os.listdir('clase 5/animales')  # Asegúrate de tener esta carpeta
    enviar_meme = random.choice(carpeta)

    with open(f'clase 5/animales/{enviar_meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("YOUR SECRET TOKEN")
