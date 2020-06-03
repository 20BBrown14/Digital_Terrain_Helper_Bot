from datetime import datetime

from client_interactions import send_message, delete_message, is_command_allowed

"""
Help Command
Returns a help message
ex: !ping

@param message: The triggering message
@result: deletes triggering message always
@result: sends message always with help text if user was allowed to invoke command.
"""

async def command(message):
  await delete_message(message)
  if(not is_command_allowed(message, TRIGGER)):
    return 0
  
  help_message = """**Here are list of available commands:**
  < !help >: *Displays a list of available commands*
  < !status >: *Whether or not that bot is live*
  < !version >: *Shows the current running version*
  < !ping >: *Lets you know the ping*
  < !joinMessageTest >: *Sends a copy of the message new members get when joining*
  I am a little open source whore. See my birthday suit here: <https://github.com/20BBrown14/Digital_Terrain_Helper_Bot>
  Nibikk#8335 is the creator of me, contact him if you have any questions.
  Last updated June 03, 2020"""
  await send_message(message, help_message, True)


def is_triggered(command_body):
  return command_body == TRIGGER

TRIGGER = 'help'