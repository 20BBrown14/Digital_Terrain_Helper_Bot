import os
import shutil
import urllib.request as request
from contextlib import closing

def getMinecraftStatsFilesWithFTP(mcStatsDirectory, serverPath, worldName, ftpHost, ftpUser, ftpPass):
    print('Started Minecraft Stats file fetching')
    if(not os.path.isdir(os.path.join(os.getcwd(), serverPath))):
        os.mkdir(os.path.join(os.getcwd(), serverPath))
    
    if(not os.path.isdir(os.path.join(os.getcwd(), serverPath, worldName))):
        os.mkdir(os.path.join(os.getcwd(), serverPath, worldName))
    else:
        shutil.rmtree((os.path.join(os.getcwd(), serverPath, worldName)))
        os.mkdir(os.path.join(os.getcwd(), serverPath, worldName))

    world_dir = os.path.join(os.getcwd(), serverPath, worldName)
    os.mkdir(os.path.join(world_dir, 'stats'))
    os.mkdir(os.path.join(world_dir, 'advancements'))

    os.system('wget -P %s ftp://%s:%s@%s/world/stats/*' % (os.path.join(world_dir, 'stats'), ftpUser, ftpPass, ftpHost))
    os.system('wget -P %s ftp://%s:%s@%s/world/advancements/*' % (os.path.join(world_dir, 'advancements'), ftpUser, ftpPass, ftpHost))
    os.system('wget -O %s ftp://%s:%s@%s/banned-players.json' % (os.path.join(world_dir, '..', 'banned-players.json'), ftpUser, ftpPass, ftpHost))
    os.system('wget -O %s ftp://%s:%s@%s/usercache.json' % (os.path.join(world_dir, '..', 'usercache.json'), ftpUser, ftpPass, ftpHost))
    os.system('wget -O %s ftp://%s:%s@%s/server.properties' % (os.path.join(world_dir, '..', 'server.properties'), ftpUser, ftpPass, ftpHost))
    print('Completed Minecraft Stats file fetching')

def uploadMinecraftStatsFilesWithFTP(ftpHost, ftpUser, ftpPass):
    print('Started Minecraft Stats file upload')
    mcstats_dir = os.path.join(os.getcwd(), 'data/')
    for (dirpath, dirnames, filenames) in os.walk(mcstats_dir):
        if(dirpath.endswith('/data/')):
            continue
        if(dirpath.endswith('/events')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/events/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
        if(dirpath.endswith('/playercache')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/playercache/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
        if(dirpath.endswith('/playerdata')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/playerdata/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
        if(dirpath.endswith('/playerlist')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/playerlist/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
        if(dirpath.endswith('/rankings')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/rankings/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
        if(dirpath.endswith('/events')):
            os.system('find %s -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/rankings/ \;' % (dirpath, ftpUser, ftpPass, ftpHost))
    os.system('find data/ -maxdepth 1 -type f -exec curl --ftp-create-dirs -T {} ftp://%s:%s@%s/plugins/dynmap/web/mcstats/data/ \;' % (ftpUser, ftpPass, ftpHost))
    print('Finished Minecraft Stats file upload')
