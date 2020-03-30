import json

global logs

global moderation

global commands_config

global console_logs_channel

global permissions

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