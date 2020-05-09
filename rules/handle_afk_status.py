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
  if(globals_file.tps_booster['waiting_on_player_status']['time_started']):
    now = datetime.datetime.now()
    time_delta = now - globals_file.tps_booster['waiting_on_player_status']['time_started']
    if(time_delta > datetime.timedelta(minutes=5)):
      globals_file.tps_booster['waiting_on_player_status']['time_started'] = None
      return 0

  not_afk_matches = re.search("(]\s.+( is not AFK))", message.content)
  afk_matches = re.search("(]\s.+( has been AFK since))", message.content)
  if(not_afk_matches):
    player = not_afk_matches.groups()[0].split(' ')[1]
    if(globals_file.tps_booster['waiting_on_player_status']['players'][player]):
      if(globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']):
        globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting'] = False
        globals_file.tps_booster['waiting_on_player_status']['players'][player]['is_afk'] = False
  elif(afk_matches):
    player = afk_matches.groups()[0].split(' ')[1]
    if(globals_file.tps_booster['waiting_on_player_status']['players'][player]):
      if(globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']):
        globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting'] = False
        globals_file.tps_booster['waiting_on_player_status']['players'][player]['is_afk'] = True
        await globals_file.moderation['moderation_channel'].send("Kicking %s due to being AFK during low TPS" % player)
        await globals_file.console_logs_channel.send(u"kick %s %s" % (player.replace('\\', ''), globals_file.tps_booster['kick_reason']))

  for player in globals_file.tps_booster['waiting_on_player_status']['players']:
    if globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting']:
      return 0
  globals_file.tps_booster['waiting_on_player_status']['is_waiting'] = False
