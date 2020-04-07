# Library imports
from discord import Client, Game, User, Member
import time

# local imports
import config
import globals_file
from commands import version, status, ping, join_message_test

# Last time bot's code was updated
# Printed out by !version
# eg. 2019-03-31_1 is the first change on March 31, 2019
current_version = '2020-03-29_1'

client = Client()

@client.event
async def on_member_join(member):
  if(member.dm_channel == None):
    await member.create_dm()
  dm_channel = member.dm_channel
  welcome_string = globals_file.welcome_message
  await dm_channel.send(welcome_string)

@client.event
async def on_member_remove(member):
  if(member.nick):
    await globals_file.moderation['moderation_channel'].send('Removing "%s" from whitelist. You should double check that it was actually completed.' % member.nick)
    await globals_file.console_logs_channel.send('whitelist remove %s' % member.nick)
  await globals_file.moderation['moderation_channel'].send('Removing "%s" from whitelist. You should double check that it was actually completed.' % member.name)
  await globals_file.console_logs_channel.send('whitelist remove %s' % member.name)

@client.event
async def on_member_ban(guild, user):
  if(isinstance(user, User)):
    await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.name)
    await globals_file.console_logs_channel.send("ban %s Banned from Discord server" % user.name)
  elif(isinstance(user, Member)):
    if(user.nick):
      await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.nick)
      await globals_file.console_logs_channel.send("ban %s Banned from Discord Server" % user.nick)
    await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.name)
    await globals_file.console_logs_channel.send("ban %s Banned from Discord Server" % user.name)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-----')
  client_game = Game(name=config.game_played)
  await client.change_presence(activity = client_game)
  globals_file.init(client, config)

@client.event
async def on_message(message):
  # Ignore everything in the logs channel
  if(globals_file.logs):
    if(message.channel.id == globals_file.logs['logs_channel'].id or message.channel.id in globals_file.logs['ignored_channels']):
      return 0
  
    # Ignore any private messages or own messages for logs
    if(message.author != client.user and globals_file.logs['log_all_messages'] and message.channel.name):
      author = message.author.nick if message.author.nick else message.author.name
      log_message = ('%s said \"%s\" in %s#%s at %s') % (author, message.clean_content, message.guild.name, message.channel.name, message.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
      await globals_file.logs['logs_channel'].send(log_message)

  # Ignore commands outside of commands channel or in ignored channels if set
  if(globals_file.commands_config):
    if(globals_file.commands_config['only_commands_here'] and message.channel.id != globals_file.commands_config['commands_channel'].id):
      return 0
    if(message.channel.id in globals_file.commands_config['ignored_channels']):
      return 0

  # listen to command attempt
  if(message.content.startswith('!')):
    command_body = message.content[1:].lower()

    if(version.is_triggered(command_body)):
      await version.command(message, current_version)

    elif(status.is_triggered(command_body)):
      await status.command(message)

    elif(ping.is_triggered(command_body)):
      await ping.command(message)

    elif(join_message_test.is_triggered(command_body)):
      await join_message_test.command(message)


client.run(config.bot_token)

