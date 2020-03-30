from client_interactions import send_message, delete_message, is_command_allowed

import globals_file

"""
Version Command
Returns current version the bot is running
ex: !version

@param message: The triggering message
@param version: The version
@result: deletes triggering message always
@result: sends message always with version if user was allowed to invoke command.
"""

async def command(message, version):
  await delete_message(message)
  if(not is_command_allowed(message, TRIGGER)):
    return 0
  await send_message(message, "I am running version: %s" % version)

def is_triggered(command_body):
  return command_body == TRIGGER

TRIGGER = 'version'