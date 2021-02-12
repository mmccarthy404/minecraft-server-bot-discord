import discord
import os

HELP_MESSAGE = """
I'm a bot used to interact with the Minecraft server!
-----------------------------------------------------

Example:
    !minecraft-server <command>

Commands:
    start - Start Minecraft server
    stop  - Stop Minecraft server
    help - Bring up this menu
""""

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!minecraft-server'):
        content_split = message.content.split()

        if len(content_split) == 1:
            await message.channel.send('ERROR: No input given' + HELP_MESSAGE)
            return

        command = content_split[1]

        if command == 'start':
            await message.channel.send('Starting Minecraft server')
        elif command == 'stop':
            await message.channel.send('Stopping Minecraft server')
        elif command == 'help':
            await message.channel.send(HELP_MESSAGE)
        else:
            await message.channel.send("ERROR: Unknown command '{command}'".format(command=command) + HELP_MESSAGE)
            return

client.run(os.getenv('BOT_TOKEN'))