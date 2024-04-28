import discord
from discord.ext import commands
import aiohttp
from aiohttp import web

# Tworzenie klienta Discord
bot = commands.Bot(command_prefix="!")

# Definicja komendy !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive.")

# Handler dla strony głównej dashboarda
async def dashboard(request):
    return web.FileResponse('dashboard.html')

# Handler dla zapisywania ustawień
async def save_settings(request):
    data = await request.post()
    # Tutaj możesz dodać kod obsługujący zapisywanie ustawień
    print(data)  # Wyświetlanie danych formularza w konsoli
    return web.Response(text="Settings saved successfully!")

# Uruchomienie serwera HTTP dla dashboarda
async def start_server():
    app = web.Application()
    app.router.add_get('/', dashboard)  # Obsługa strony głównej
    app.router.add_post('/save_settings', save_settings)  # Obsługa zapisywania ustawień
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # Ustawienie adresu i portu
    await site.start()

# Uruchomienie bota i serwera HTTP
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Uruchomienie serwera HTTP po zalogowaniu bota
    await start_server()

# Uruchomienie bota
bot.run("MTIzNDA1NjI4NzkyNzQwNjYwMw.GDi5JG.g4bgM9DT-JXpucmiKandnfDfyR4L8cXQwEBfyc")
