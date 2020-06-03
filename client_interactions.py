import sys

import globals_file

async def send_message(message, message_to_send, force_author = False):
  try:
    message_destination = determine_destination(message, force_author)
    await message_destination.send(message_to_send)
  except:
    print('Failed to send message')
    print(sys.exc_info()[0])
    error_message = "Failed to send message. %s" % sys.exc_info()[0]
    globals_file.log_information(error_message)

async def delete_message(message):
  try:
    await message.channel.fetch_message(message.id)
    if(message.channel.name and globals_file.commands_config and message.channel.id == globals_file.commands_config['commands_channel'].id):
      return 0
    if(message.channel.name):
      await message.delete()
  except:
    print('Failed to delete message')
    print(sys.exc_info()[0])
    error_message = "Failed to delete message. %s" % sys.exc_info()[0]
    globals_file.log_information(error_message)

def determine_destination(message, force_author):
  return message.channel if message.channel.name and not force_author else message.author

def is_command_allowed(message, trigger):
  min_role = None
  if(globals_file.permissions and globals_file.permissions[trigger]):
    if(globals_file.permissions[trigger] == 0):
      return True

    for role in message.guild.roles:
      if role.id == globals_file.permissions[trigger]:
        min_role = role
    if(min_role == None):
      return True
    try:
      min_role_level = message.guild.roles.index(min_role)
      allowed_roles = message.guild.roles[min_role_level:]
    except:
      return True
    for role in message.author.roles:
      for allowed_role in allowed_roles:
        if(allowed_role == role):
          return True
    return False
  else:
    True