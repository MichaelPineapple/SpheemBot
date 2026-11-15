from typing import List
from CommandHandler import CommandHandler
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as: " + client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    txt = message.content
    print(txt)
    await message.channel.send(txt)

#    if txt.startswith('$'):
#        print(messageText)
#        author: str = str(message.author)
#        print(author)
#        cmd: str = messageText[1:]
#        args: List[str] = cmd.split(' ')
#        reply: str = "Unknown Command"
#        func = CommandHandler.getFunction(args[0])
#        if func is not None:
#
#            reply: str = "An unexpected error occurred."
#            reply: str = func(author, args[1:])
#            try:
#               pass
#            except:
#                print("ERROR!")
#        await message.channel.send(reply)

try:
    with open("apikey", "r") as file:
        client.run(file.read())
except:
    print("Failed to read API key file!")
