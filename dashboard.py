from aiohttp import web
import aiohttp

# Obsługa wysyłania danych do bota
async def send_data_to_bot(data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/dashboard_handler', json=data) as resp:
            return await resp.json()

# Przykładowe dane, które chcesz wysłać do bota
data_to_send = {
    "setting1": "value1",
    "setting2": "value2"
}

# Wywołanie funkcji do wysłania danych
response = await send_data_to_bot(data_to_send)
print(response)  # Odpowiedź od bota
