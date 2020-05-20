#set_playerlist.py

import re
import datetime
import time

import globals_file

"""
Set playerlist for currently online players

@param message: The message that triggered
@result: Sets some global variables to be used later and sends commands to the console
"""

async def apply(message):
  if(globals_file.tps_booster and globals_file.tps_booster['waiting_on_player_list'] and globals_file.tps_booster['waiting_on_player_list']['is_waiting']):
    if(globals_file.tps_booster['waiting_on_player_list']['is_waiting']):
      time_delta = datetime.datetime.now() - globals_file.tps_booster['waiting_on_player_list']['time_started']
      if((time_delta > datetime.timedelta(minutes=5))):
        globals_file.tps_booster['waiting_on_player_list']['is_waiting'] = False
        globals_file.tps_booster['waiting_on_player_list']['time_started'] = None
        return 0
  matches = re.search("(There are \d+ of a max \d+ players online: .+)", message.content)
  if(matches):
    globals_file.tps_booster['waiting_on_player_list'] = False
    players = matches.groups()[0].split(': ')[1].split(', ')
    globals_file.tps_booster['waiting_on_player_status'] = {}
    if(players):
      globals_file.tps_booster['waiting_on_player_status']['players'] = {}
      globals_file.tps_booster['waiting_on_player_status']['is_waiting'] = True
      globals_file.tps_booster['waiting_on_player_status']['time_started'] = datetime.datetime.now()
    else:
      globals_file.tps_booster['waiting_on_player_status']['players'] = None
      globals_file.tps_booster['waiting_on_player_status']['is_waiting'] = False
      globals_file.tps_booster['waiting_on_player_status']['time_started'] = None
      return 0
    for player in players:
      globals_file.tps_booster['waiting_on_player_status']['players'][player] = {}
      globals_file.tps_booster['waiting_on_player_status']['players'][player]['waiting'] = True
      globals_file.tps_booster['waiting_on_player_status']['players'][player]['start_time'] = datetime.datetime.now()
      globals_file.tps_booster['waiting_on_player_status']['players'][player]['is_afk'] = False
      time.sleep(1)
      await globals_file.console_logs_channel.send(u'afkplus player %s' % player.replace('\\', ''))
