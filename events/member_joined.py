#member_joined.py
import sys
import globals_file

"""
Handle member join event

@param member: The member who joined
@result: Sends a DM to the member with the welcome string
"""
async def handle(member):
  try:
    if(globals_file.welcome_message):
      if(member.dm_channel == None):
        await member.create_dm()
      dm_channel = member.dm_channel
      welcome_string = globals_file.welcome_message
      await dm_channel.send(welcome_string)
  except:
    log_message = "Error: %s" % sys.exc_info()[0]
    globals_file.log_information(log_message)