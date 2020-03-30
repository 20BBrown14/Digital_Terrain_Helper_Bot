from client_interactions import send_message, delete_message, is_command_allowed

"""
Status Command
Command to use to help know if the bot is running
ex: !status

@param message: The triggering message
@result: deletes triggering message always
@result: sends message always if user was allowed to invoke command.
"""

async def command(message):
  await delete_message(message)
  if(not is_command_allowed(message, TRIGGER)):
    return 0
  await send_message(message, "I'm here and ready to rumble!")


def is_triggered(command_body):
  return command_body == 'status'

TRIGGER = 'status'