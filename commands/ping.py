from datetime import datetime

from client_interactions import send_message, delete_message, is_command_allowed

"""
Ping Command
Returns ping from discord to bot
ex: !ping

@param message: The triggering message
@result: deletes triggering message always
@result: sends message always with ping if user was allowed to invoke command.
"""

async def command(message):
  await delete_message(message)
  if(not is_command_allowed(message, TRIGGER)):
    return 0
  d = datetime.utcnow() - message.created_at
  s = d.seconds*1000 + d.microseconds//1000
  response = 'Ping: %sms' % str(s)
  await send_message(message, response)


def is_triggered(command_body):
  return command_body == 'ping'

TRIGGER = 'ping'