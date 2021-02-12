import discord
import requests
import re
import os

bot_token = os.getenv('BOT_TOKEN')
api_id = os.getenv('API_ID')

api_url = 'https://{api_id}.execute-api.us-east-1.amazonaws.com/prod/'.format(api_id=api_id)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.match(r'^!minecraft-server(?!\S)', message.content):
        try:
            command = message.content.split()[1]
        except:
            await message.channel.send(':angry: No input given')
            return

        if command == 'start':
            await message.channel.send(':sunrise_over_mountains: Starting Minecraft server')
            response = requests.post(api_url + 'start')
            print(response)
        elif command == 'stop':
            await message.channel.send(':city_sunset: Stopping Minecraft server')
            response = requests.post(api_url + 'stop')
            print(response)
        else:
            await message.channel.send(':angry: Unknown command given')

client.run(bot_token)