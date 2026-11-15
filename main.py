from typing import List
import requests as requests
import json
import discord
from discord.ext import commands

RC_OK = "OK"
RC_FAIL = "FAIL"

KEY_USERNAME = "username"
KEY_PASSWORD = "password"
KEY_RESULT = "result"
KEY_PAYLOAD = "payload"
KEY_RECIPIENT = "recipient"
KEY_AMOUNT = "amount"

VERB_HELLO = "hello"
VERB_LOGIN = "login"
VERB_CREATE = "create"
VERB_DELETE = "delete"
VERB_PAY = "pay"

user_map = {}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Logged in as: " + str(bot.user))
    
async def spheem_cmd(ctx, verb, request, success_callback):
    responseRaw = requests.post("https://meowcle.net/cgi-bin/Spheem/endpoints/" + verb + ".js", json=request)
    response = json.loads(responseRaw.content)
    result = response[KEY_RESULT]
    payload = response[KEY_PAYLOAD]
    reply = "Failed: " + str(payload)
    if result == RC_OK:
        reply = success_callback(payload)
    await ctx.response.send_message(reply)
    
async def spheem_user_cmd(ctx, verb, request, success_callback):
    user_id = ctx.user.id
    if user_id not in user_map:
        await ctx.response.send_message("Must be logged in.")
        return
    request.update(user_map[user_id])
    await spheem_cmd(ctx, verb, request, success_callback)
    
# *** Hello ***
@bot.tree.command(name="hello", description="Hello, Spheem!")
async def hello(ctx):
    def callback(payload):
        return payload
    await spheem_cmd(ctx, VERB_HELLO, {}, callback)
  
# *** Create Account ***
@bot.tree.command(name="create_account", description="Create a new Spheem account.")
async def create_account(ctx, username: str, password: str):
    request = { KEY_USERNAME: username, KEY_PASSWORD: password }
    def callback(payload):
        user_map[ctx.user.id] = request
        return "Account created: " + username
    await spheem_cmd(ctx, VERB_CREATE, request, callback)
    
# *** Delete Account ***
@bot.tree.command(name="delete_account", description="Delete your Spheem account.")
async def delete_account(ctx, username: str, password: str):
    request = { KEY_USERNAME: username, KEY_PASSWORD: password }
    def callback(payload):
        user_id = ctx.user.id
        if user_id in user_map:
            del user_map[user_id]
        return "Account deleted: " + username
    await spheem_cmd(ctx, VERB_DELETE, request, callback)

# *** Login ***
@bot.tree.command(name="login", description="Login to Spheem.")
async def login(ctx, username: str, password: str):
    request = { KEY_USERNAME: username, KEY_PASSWORD: password }
    def callback(payload):
        user_map[ctx.user.id] = request
        return "Logged in as: " + username
    await spheem_cmd(ctx, VERB_LOGIN, request, callback)
    
# *** Logout ***
@bot.tree.command(name="logout", description="Logout of Spheem.")
async def logout(ctx):
    user_id = ctx.user.id
    reply = "Not logged in."
    if user_id in user_map:
        del user_map[user_id]
        reply = "Successfuly Logged out."
    await ctx.response.send_message(reply)

# *** Balance ***
@bot.tree.command(name="bal", description="Check your Spheem balance.")
async def bal(ctx):
    def callback(payload):
        return "Balance: " + str(payload)
    await spheem_user_cmd(ctx, VERB_LOGIN, {}, callback)

# *** Pay ***
@bot.tree.command(name="pay", description="Transfer funds.")
async def pay(ctx, recipient: str, amount: int,):
    request = { KEY_RECIPIENT: recipient, KEY_AMOUNT: amount }
    def callback(payload):
        return "Transaction successful."
    await spheem_user_cmd(ctx, VERB_PAY, request, callback)
    
try:
    with open("apikey", "r") as file:
        bot.run(file.read())
except:
    print("Failed to read API key file!")
