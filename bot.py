import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!minecraft-server'):
        command = message.content.split()[1]

        if command == 'start':
            await message.channel.send('Starting Minecraft server')
        elif command == 'stop':
            await message.channel.send('Stopping Minecraft server')
        else:
            await message.channel.send("Unknown command '{command}'".format(command=command))

client.run(os.getenv('BOT_TOKEN'))