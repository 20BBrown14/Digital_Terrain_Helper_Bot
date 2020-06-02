#handle_afk_status.py

import re
import datetime
import time

import globals_file

"""
handle whether a player is afk or not

@param message: The message that triggered
@result: Sets some global variables to be used later and sends commands to the console
"""

async def apply(message):
  try:
    if(globals_file.tps_booster['waiting_on_player_status']['time_started']):
      now = datetime.datetime.now()
      time_delta = now - globals_file.tps_booster['waiting_on_player_status']['time_started']
      if(time_delta > datetime.timedelta(minutes=5)):
        globals_file.tps_booster['waiting_on_player_status']['time_started'] = None
        log_message = "Time expired for handling afk status. Time delta:%s, tps_booster:%s" % (time_delta, globals_file.tps_booster)
        globals_file.log_information(log_message)
        return 0

    not_afk_matches = re.search("(]\s.+( is not AFK))", message.content)
    afk_matches = re.search("(]\s.+( has been AFK since))", message.content)
    if(not_afk_matches):
      player = not_afk_matches.groups()[0].split(' ')[1]
      if(globals_file.tps_booster['waiting_on_player_status']['players'][player]):
        if(globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']):
          globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting'] = False
          globals_file.tps_booster['waiting_on_player_status']['players'][player]['is_afk'] = False
          log_message = "Updated tps_booster: %s" % globals_file.tps_booster
          globals_file.log_information(log_message)
    elif(afk_matches):
      player = afk_matches.groups()[0].split(' ')[1]
      if(globals_file.tps_booster['waiting_on_player_status']['players'][player]):
        if(globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']):
          globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting'] = False
          globals_file.tps_booster['waiting_on_player_status']['players'][player]['is_afk'] = True
          await globals_file.moderation['moderation_channel'].send("Kicking %s due to being AFK during low TPS" % player)
          await globals_file.console_logs_channel.send(u"kick %s %s" % (player.replace('\\', ''), globals_file.tps_booster['kick_reason']))
          log_message = "Kicked afk player: %s, tps_booster: %s" % (player.replace('\\', ''), globals_file.tps_booster)
          globals_file.log_information(log_message)

    for player in globals_file.tps_booster['waiting_on_player_status']['players']:
      if globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']:
        return 0
    globals_file.tps_booster['waiting_on_player_status']['is_waiting'] = False
    log_message = "No longer waiting to handle afk status: %s" % globals_file.tps_booster
    globals_file.log_information(log_message)
  except:
    log_message = "Error: %s" % sys.exc_info()[0]
    globals_file.log_information(log_message)
