#!/usr/bin/env python3
import python_weather
import asyncio
import emoji

async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client()

    # fetch a weather forecast from a city
    weather = await client.find("Kyiv")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    print (emoji.emojize(":sun: :cloud:  The weather in Kyiv is: "))
    loop = asyncio.new_event_loop() # for Python >= 3.10, otherwise use get_event_loop
    loop.run_until_complete(getweather())
