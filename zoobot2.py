import random
from discord import Game
from discord.ext.commands import Bot
import requests
import asyncio
import os

BOT_PREFIX = "!"
TOKEN = os.environ['TOKEN']

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!team'):
    	msg = "{0.author.mention}, what team do you wish to join? !Zoo, !DNA, !Hunter, !Tech are available options.".format(message)
    	await client.send_message(message.channel, msg)

    if message.content.startswith('!Zoo'):
    	msg = "The Zookeepers' Alliance would be happy to have you! (Function coming soon)".format(message)
    	await client.send_message(message.channel, msg)
    	

# @client.event
# async def on_message_delete(msg):
# 	await client.send_message(channel(logs), msg)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with SWC's Server"))
	print("Logged in as " + client.user.name)

# @client.command()
# async def bitcoin():
# 	url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
# 	response = requests.get(url)
# 	value = response.json() ['bpi'] ['USD'] ['rate']
# 	await client.say("Bitcoin price is: $" + value)

# @client.command(pass_context=True)
# async def eight_ball(context):
# 	possible_responses = [
# 		'That is a resounding no',
# 		'It is not looking likely',
# 		'Too hard to tell',
# 		'It is quite possible',
# 		'Most definetly',
# 		'Ask again later'
# 	]
# 	await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

# @client.command()
# async def square(num):
# 	squared_value = int(num) * int(num)
# 	await client.say(str(number) + " squared is " + str(squared_value))

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print("Current servers:")
		for server in client.servers:
			print(server.name)
		print("------")
		await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)