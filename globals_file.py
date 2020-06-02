import json
import logging
import time

global logs

global moderation

global commands_config

global console_logs_channel

global permissions

global app_template

global welcome_message

global tps_booster

global logger
logging.basicConfig(filename="DigitalTerrainHelperBotLogs.log", level=logging.INFO)
logger = logging.getLogger('Digital_Terrain_Helper_Bot')

def log_information(log_message):
  logger.info("%s - %s" % (time.strftime("%d/%m/%Y %H:%M:%S"), log_message))

def init(client, config):

  # Setup logs
  global logs
  logs = None
  if(config.logs and config.logs['log_all_messages']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.logs['logs_channel']:
          logs = config.logs
          logs['logs_channel'] = channel
  else:
    logs = None

  log_message = "Logs config setup: %s" % logs
  log_information(log_message)

  # Setup mooderation
  global moderation
  moderation = None
  if(config.moderation and config.moderation['moderation_channel']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.moderation['moderation_channel']:
          moderation = config.moderation
          moderation['moderation_channel'] = channel
  else:
    moderation = None

  log_message = "Moderation config setup: %s" % moderation
  log_information(log_message)

  # Setup bot commands
  global commands_config
  commands_config = None
  if(config.bot_commands and config.bot_commands['commands_channel']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.bot_commands['commands_channel']:
          commands_config = config.bot_commands
          commands_config['commands_channel'] = channel
  else:
    commands_config = None

  log_message = "Commands config setup: %s" % commands_config
  log_information(log_message)

  global console_logs_channel
  console_logs_channel = None
  if(config.console_channel):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.console_channel:
          console_logs_channel = channel

  log_message = "Console Logs Config setup: %s" % console_logs_channel
  log_information(log_message)

  global permissions
  permissions = None
  permissions = config.permissions if config.permissions else None

  log_message = "Permissions config setup: %s" % permissions
  log_information(log_message)

  global app_template
  app_template = """
In game name:
Location:
Age:
What you're looking for by joining this server:
Your ideal play-style on this server:
What do you do in your free time or for work (just want to know a little about you. Has no bearing on your actual application):
  """

  global welcome_message
  welcome_message = """
  Welcome to the Digital Terrain Minecraft server Discord! We're happy to have you here!
  Be sure to checkout the information doc that's pinned in both the #landing and #information channel.
  We'll be sure to give you roles and whitelist you as soon as we notice you've joined the Discord. You can mention the gigabytes
  or megabytes role in the #default to get our attention. If you make your Discord nickname match your IGN it'll make things go faster for you.
  Direct any questions you might have to a Gigabyte or Megabyte and we'll make sure to help you as much as possible.
  Note: If you've joined the Discord without sending an app first be sure to post your app in the #default channel using the template below.
  %s
  """ % app_template

  global tps_booster
  tps_booster = None
  if(config.tps_booster):
    tps_booster = config.tps_booster
    tps_booster['waiting_on_player_list'] = None
    tps_booster['waiting_on_player_status'] = None
  else:
    tps_booster = None

  log_message = "TPS booster config setup: %s" % tps_booster
  log_information(log_message)