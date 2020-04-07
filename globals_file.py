import json

global logs

global moderation

global commands_config

global console_logs_channel

global permissions

global app_template

global welcome_message

def init(client, config):

  # Setup logs
  global logs
  if(config.logs and config.logs['log_all_messages']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.logs['logs_channel']:
          logs = config.logs
          logs['logs_channel'] = channel
  else:
    logs = None

  # Setup mooderation
  global moderation
  if(config.moderation and config.moderation['moderation_channel']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.moderation['moderation_channel']:
          moderation = config.moderation
          moderation['moderation_channel'] = channel
  else:
    moderation = None

  # Setup bot commands
  global commands_config
  if(config.bot_commands and config.bot_commands['commands_channel']):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.bot_commands['commands_channel']:
          commands_config = config.bot_commands
          commands_config['commands_channel'] = channel
  else:
    commands_config = None

  global console_logs_channel
  if(config.console_channel):
    for guild in client.guilds:
      for channel in guild.channels:
        if channel.id == config.console_channel:
          console_logs_channel = channel

  global permissions
  permissions = config.permissions if config.permissions else None

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
  Note: If you're coming from Planet Minecraft be sure to post your app in the #default channel using the template below.
  %s
  """ % app_template