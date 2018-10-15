import random
from discord import Game
from discord.ext.commands import Bot
import requests
import asyncio
import os
from discord import Channel
from discord import Role
from discord import Server
import discord


BOT_PREFIX = "!"
TOKEN = os.environ['TOKEN']

team_roles = [
	"499807766865510410",
	"499808342546317312",
	"499808421164482561",
	"499808472804753410"
]

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('!team'):
    	for r in message.author.roles:
    		if r.id in team_roles:
    # If a role in the user's list of roles matches one we're checking
    			await client.send_message(message.channel, "You already have a team role. If you want to switch, message a moderator.")
    			return
    	msg = "{0.author.mention}, what team do you wish to join? !Zoo, !DNA, !Hunter, !Tech are available options.".format(message)
    	await client.send_message(message.channel, msg)

    if message.content.lower().startswith('!zoo'):
    	for r in message.author.roles:
    		if r.id in team_roles:
    # If a role in the user's list of roles matches one we're checking
    			await client.send_message(message.channel, "You already have a team role. If you want to switch, message a moderator.")
    			return
    	msg = "The Zookeepers' Alliance would be happy to have you! Setting role now!".format(message)
    	await client.send_message(message.channel, msg)
    	role = discord.utils.get(message.server.roles, name='Zookeeper')
    	try:
    		await client.add_roles(message.author, role)
    		await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
    	except discord.Forbidden:
    		await client.send_message(message.channel, "I don't have perms to add roles.")
    	msg = "{0.author.mention} has joined the Zookeeper Team.".format(message)
    	await client.send_message(client.get_channel('499817122663235625'), msg)
    
    if message.content.lower().startswith('!tech'):
    	for r in message.author.roles:
    		if r.id in team_roles:
    # If a role in the user's list of roles matches one we're checking
    			await client.send_message(message.channel, "You already have a team role. If you want to switch, message a moderator.")
    			return
    	msg = "Tech Lovers United would be happy to have you! Setting role now!".format(message)
    	await client.send_message(message.channel, msg)
    	role = discord.utils.get(message.server.roles, name='Tech')
    	try:
    		await client.add_roles(message.author, role)
    		await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
    	except discord.Forbidden:
    		await client.send_message(message.channel, "I don't have perms to add roles.")
    	msg = "{0.author.mention} has joined the Tech Lovers Team.".format(message)
    	await client.send_message(client.get_channel('499817122663235625'), msg)

    if message.content.lower().startswith('!dna'):
    	for r in message.author.roles:
    		if r.id in team_roles:
    # If a role in the user's list of roles matches one we're checking
    			await client.send_message(message.channel, "You already have a team role. If you want to switch, message a moderator.")
    			return
    	msg = "The DNA Bashers would be happy to have you! Setting role now!".format(message)
    	await client.send_message(message.channel, msg)
    	role = discord.utils.get(message.server.roles, name='DNA')
    	try:
    		await client.add_roles(message.author, role)
    		await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
    	except discord.Forbidden:
    		await client.send_message(message.channel, "I don't have perms to add roles.")
    	msg = "{0.author.mention} has joined the DNA Team.".format(message)
    	await client.send_message(client.get_channel('499817122663235625'), msg)

    if message.content.lower().startswith('!hunter'):
    	for r in message.author.roles:
    		if r.id in team_roles:
    # If a role in the user's list of roles matches one we're checking
    			await client.send_message(message.channel, "You already have a team role. If you want to switch, message a moderator.")
    			return
    	msg = "The Sport Hunters Guild would be happy to have you! Setting role now!".format(message)
    	await client.send_message(message.channel, msg)
    	role = discord.utils.get(message.server.roles, name='Hunter')
    	try:
    		await client.add_roles(message.author, role)
    		await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
    	except discord.Forbidden:
    		await client.send_message(message.channel, "I don't have perms to add roles.")
    	msg = "{0.author.mention} has joined the Hunter Team.".format(message)
    	await client.send_message(client.get_channel('499817122663235625'), msg)

    # command meant for dev only to clear annoying discord spam from bot testing, comment out when going live.
    if message.content.startswith('!clear'):
    	tmp = await client.send_message(message.channel, 'Clearing messages...')
    	async for msg in client.logs_from(message.channel):
    		await client.delete_message(msg)

@client.event
async def on_member_join(member):
	msg = 'Welcome, {0.mention}! Which team are you on? Say !team for a list.'.format(member)
	await client.send_message(client.get_channel('499807356327297037'), msg)


@client.listen()
async def on_raw_message_delete(messsage):
	await client.send_message(client.get_channel('499817122663235625'), message)

# @client.listen()
# async def on_message_edit(before, after):
# 	msg = before
# 	await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with SWC's Server"))
	print("Logged in as " + client.user.name)
	# for server in client.servers:
	# 	for channel in server.channels:
	# 		print(channel.id + " " + channel.name)
	# print(Server.roles)
 #    	for server in client.servers:
 #    		for role in server.roles:
 #    			print(role.id + " " + role.name)


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

#client.get_channel('499807356327297037') Genera channel

client.loop.create_task(list_servers())
client.run(TOKEN)