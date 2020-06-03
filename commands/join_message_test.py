import globals_file
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
  await send_message(message, globals_file.welcome_message, True)


def is_triggered(command_body):
  return command_body.lower() == TRIGGER

TRIGGER = 'joinmessagetest'