#guild_channel_updated.py
import datetime
import time

import globals_file

"""
Handle guild channel being updated. Requires "console_channel", "tps_booster", and "moderation" to be set in the config

@param before: Guild info before update
@param after: Guild info after update
@result: Sends messages to moderation and console_logs if guild topic was updated with a tps number low enough
"""
async def handle(before, after):
  if(globals_file.console_logs_channel and globals_file.tps_booster and globals_file.moderation):
    if(before.id == globals_file.console_logs_channel.id and after.id == globals_file.console_logs_channel.id):
      tps = float(after.topic.split('|')[0].split(' ')[1])
      if(tps < globals_file.tps_booster['minimum_tps']):
        await globals_file.moderation['moderation_channel'].send("TPS is %s. Starting process to kick afk members." % tps)
        globals_file.tps_booster['waiting_on_player_list'] = {"is_waiting": True, "time_started": datetime.datetime.now()}
        time.sleep(1)
        await globals_file.console_logs_channel.send('list')


