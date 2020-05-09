#member_banned.py

import globals_file

"""
Handle member being banned

@param guild: The guild the member was banned from
@param user: The user who was banned
@result: Sends moderation messages and messages to console_log
"""
async def handle(guild, User):
  if(globals_file.moderation and globals_file.console_logs_channel):
    if(isinstance(user, User)):
      await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.name)
      await globals_file.console_logs_channel.send("ban %s Banned from Discord server" % user.name)
    elif(isinstance(user, Member)):
      if(user.nick):
        await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.nick)
        await globals_file.console_logs_channel.send("ban %s Banned from Discord Server" % user.nick)
      await globals_file.moderation['moderation_channel'].send('Adding "%s" to the blacklist due to being banned from the Discord server. You should double check this was actually completed.' % user.name)
      await globals_file.console_logs_channel.send("ban %s Banned from Discord Server" % user.name)