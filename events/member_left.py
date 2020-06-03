#member_left.py

import globals_file

"""
Handle member leaving event

@param member: The member who left
@result: Sends moderation messages and messages to console_log
"""
async def handle(member):
  if(globals_file.moderation and globals_file.console_logs_channel):
    if(member.nick):
      await globals_file.moderation['moderation_channel'].send('Removing "%s" from whitelist. You should double check that it was actually completed.' % member.nick)
      await globals_file.console_logs_channel.send('whitelist remove %s' % member.nick)
    await globals_file.moderation['moderation_channel'].send('Removing "%s" from whitelist. You should double check that it was actually completed.' % member.name)
    await globals_file.console_logs_channel.send('whitelist remove %s' % member.name)