import os
import datetime
import git
import subprocess
import time
import sys

#local imports
import config
from minecraft_stats import minecraftStatsRemoteUpdate

mcstats_update_file_Location = os.path.realpath(os.path.join(os.getcwd(), config.mcstats_config['projectDirectory'], 'update.py'))
mcstats_update_config_location = os.path.realpath(os.path.join(os.getcwd(), config.mcstats_config['projectDirectory'], 'config.json'))

print(mcstats_update_file_Location)

global python_bot_pid

def kill_bot():
  global python_bot_pid
  if(python_bot_pid > 0):
    subProcess = subprocess.call(["kill", "-9", str(python_bot_pid)], cwd=os.getcwd())
    time.sleep(5)


def start_bot():
  global python_bot_pid
  subProcess = subprocess.Popen(["python3", "python_bot.py"], cwd=os.getcwd())
  time.sleep(5)
  python_bot_pid = subProcess.pid
  print("Python bot id: " + str(python_bot_pid))

def check_for_git_update():
  repo = git.Repo(os.getcwd())
  currentBranch = repo.head.reference
  for remote in repo.remotes:
      remote.fetch()
  commits_behind = repo.iter_commits('master..origin/master')
  count = sum(1 for c in commits_behind)
  if(count > 0):
    kill_bot()
    repo.remotes.origin.pull()
    print("Updated git repo to " + repo.head.reference.commit.hexsha + " @ " + str(datetime.datetime.now()))
    start_bot()

def updateMCStats():
  mcstats_config = config.mcstats_config
  print(mcstats_config)
  minecraftStatsRemoteUpdate.getMinecraftStatsFilesWithFTP(mcstats_config['projectDirectory'], mcstats_config['serverPath'], mcstats_config['worldName'], mcstats_config['ftpHost'], mcstats_config['ftpUser'], mcstats_config['ftpPassword'])
  os.system('python3 %s %s' % (mcstats_update_file_Location, mcstats_update_config_location))
  minecraftStatsRemoteUpdate.uploadMinecraftStatsFilesWithFTP(mcstats_config['ftpHost'], mcstats_config['ftpUser'], mcstats_config['ftpPassword'])


def main():
  global python_bot_pid
  python_bot_pid = -1
  start_bot()
  start_time = datetime.datetime.now()
  while(1):
    mcstats_config = config.mcstats_config
    if(config.mcstats_config['isActive']):
      updateMCStats()
    time.sleep(60*240)
    now = datetime.datetime.now()
    time_delta = now - start_time
    if(time_delta > datetime.timedelta(days=1)):
      kill_bot()
      start_bot()
      start_time = now

main()
