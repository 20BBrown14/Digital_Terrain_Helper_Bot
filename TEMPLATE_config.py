import json

# config.py
# save a copy of this template file as config.py with your BOT TOKEN from discord app settings 

# Required Bot token. Keep Secret.
bot_token = "BOT TOKEN HERE"

# Optional game played to display on discord
game_played = 'Some Game'

# Optional logs information to log messages
# logs_channel (Int): channel id to log messages to
# log_all_messages (Bool): Whether to log all messages the bot sees except for ignored_channels
# logs_ignored_channels (Array(Int)): Array of channel ids to not log messages from
logs = json.loads('{"logs_channel": 0, "log_all_messages": false, "logs_ignored_channels": []}')

# Optional moderation information to log automated moderations
# moderation_channel (Int): channel id to log moderations to
# log_moderations (Bool): Whether to log all moderation decisions the bot makes
moderation = json.loads('{"moderation_channel": 0, "log_moderations": false}')

# Optional tps booster config
# active (Bool): If the tps_booster is active
# minimum_tps (Int): Minimum tps that the booster is activated at
# kick_reason (String): Kick reason to send kicked users
tps_booster = json.loads('{"active": false, "minimum_tps": 18, "kick_reason": ""}')

# Optional bot commands channel.
# commands_channel (Int): Channel id for the bot commands channel
# only_commands_here (Bool): Only allow commands to be used in this channel. (Overrides ignored_channels option)
# ignored_channels (Array(Int)): Array of channel ids to ignore commands in
bot_commands = json.loads('{"commands_channel": 0, "only_commands_here": false, "ignored_channels": []}')

# Console logs channel from DISCORDSRV discord bot minecraft plugin
console_channel = 0

# permissions for the minimum role to use command. Empty stirng for no restrictions
# not providing this assumes all commands are available to all members
# if invalid ids are given assumes there is permission to use command
permissions = json.loads("""
{
  "version": "MINIMUM_ROLE_ID"
  "status": "MINIMUM_ROLE_ID"
  "ping": "MINIMUM_ROLE_ID"
  "joinmessagetest": "MINIMUM_ROLE_ID",
  "help": "MINIMUM_ROLE_ID"
}
""".replace('\n', ' '))