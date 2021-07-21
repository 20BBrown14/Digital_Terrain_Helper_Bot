import os

from client_interactions import send_message, delete_message, is_command_allowed
from minecraft_stats import minecraftStatsRemoteUpdate
import config

"""
Update Minecraft Stats Command
Command to run the update minecraft stats script if it's active in the config.
ex: !updateWebStats

@param message: The triggering message
@result: deletes triggering message always
@result: sends message when update has started and when it finishes.
"""

async def command(message):
  await delete_message(message)
  if(not is_command_allowed(message, TRIGGER)):
    return 0

  await send_message(message, "Updating web stats...")

  mcstats_config = config.mcstats_config
  mcstats_update_file_Location = os.path.realpath(os.path.join(os.getcwd(), mcstats_config['projectDirectory'], 'update.py'))
  mcstats_update_config_location = os.path.realpath(os.path.join(os.getcwd(), mcstats_config['projectDirectory'], 'config.json'))

  print(mcstats_config)
  minecraftStatsRemoteUpdate.getMinecraftStatsFilesWithFTP(mcstats_config['projectDirectory'], mcstats_config['serverPath'], mcstats_config['worldName'], mcstats_config['ftpHost'], mcstats_config['ftpUser'], mcstats_config['ftpPassword'])
  os.system('python3 %s %s' % (mcstats_update_file_Location, mcstats_update_config_location))
  minecraftStatsRemoteUpdate.uploadMinecraftStatsFilesWithFTP(mcstats_config['ftpHost'], mcstats_config['ftpUser'], mcstats_config['ftpPassword'])
  
  await send_message(message, "Finished updated web stats!")



def is_triggered(command_body):
  return command_body == TRIGGER

TRIGGER = 'updatewebstats'