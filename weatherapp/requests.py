import aiohttp
import os
import asyncio


async def get_weather_data(city_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://api.openweathermap.org/data/2.5/weather'
                f'?q={city_name}&appid={os.environ.get("WEATHER_KEY")}') as response:
            return await response.text()
