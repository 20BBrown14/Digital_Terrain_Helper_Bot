# Library imports
from discord import Client, Game, User, Member
import time
import logging

# local imports
import config
import globals_file
from commands import version, status, ping, join_message_test, help
from events import member_joined, member_left, member_banned, guild_channel_updated
from rules import set_playerlist, handle_afk_status

# Last time bot's code was updated
# Printed out by !version
# eg. 2019-03-31_1 is the first change on March 31, 2019
current_version = '2020-06-03_2'

client = Client()

@client.event
async def on_member_join(member):
  log_message = "Member Joined\nMember: name:%s, nick:%s, id:%d" % (member.name, member.nick, member.id)
  globals_file.log_information(log_message)
  await member_joined.handle(member)

@client.event
async def on_member_remove(member):
  log_message = "Member Remove Event\nMember: name:%s, nick:%s. id:%d" % (member.name, member.nick, member.id)
  globals_file.log_information(log_message)
  await member_left.handle(member)

@client.event
async def on_member_ban(guild, user):
  log_message = "Guild Member Ban Event\nGuild: name:%s\nUser: name:%s, id:%d" % (guild.name, user.name, user.id)
  globals_file.log_information(log_message)
  await member_banned.handle(guild, user)

@client.event
async def on_guild_channel_update(before, after):
  log_message = "Guild Channel Update Event\nBefore: name:%s, id:%d, topic:%s\nAfter: name:%s, id:%d, topic:%s" % (before.name, before.id, before.topic, after.name, after.id, after.topic)
  globals_file.log_information(log_message)
  await guild_channel_updated.handle(before, after)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('-----')
  client_game = Game(name=config.game_played)
  await client.change_presence(activity = client_game)
  globals_file.init(client, config)
  globals_file.log_information("Bot Started")

@client.event
async def on_message(message):
  if(not message.author == client.user and globals_file.console_logs_channel and message.channel.id == globals_file.console_logs_channel.id and globals_file.tps_booster and globals_file.tps_booster['waiting_on_player_list'] and globals_file.tps_booster['waiting_on_player_list']['is_waiting']):
    log_message = "Setting playerlist\ntps_booster: %s" % globals_file.tps_booster
    globals_file.log_information(log_message)
    await set_playerlist.apply(message)

  if(not message.author == client.user and globals_file.console_logs_channel and message.channel.id == globals_file.console_logs_channel.id and globals_file.tps_booster and globals_file.tps_booster['waiting_on_player_status'] and globals_file.tps_booster['waiting_on_player_status']['is_waiting']):
    log_message = "Handling afk statuses\ntps_booster: %s" % globals_file.tps_booster
    globals_file.log_information(log_message)
    await handle_afk_status.apply(message)

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
    log_message = "Command detected. messageContent:%s, messageAuthor:%s" % (message.content, message.author)
    globals_file.log_information(log_message)
    command_body = message.content[1:].lower()

    if(version.is_triggered(command_body)):
      await version.command(message, current_version)

    elif(status.is_triggered(command_body)):
      await status.command(message)

    elif(ping.is_triggered(command_body)):
      await ping.command(message)

    elif(join_message_test.is_triggered(command_body)):
      await join_message_test.command(message)

    elif(help.is_triggered(command_body)):
      await help.command(message)


client.run(config.bot_token)

