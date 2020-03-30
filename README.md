# Digital_Terrain_Helper_Bot
Repo for the Digital Terrain Minecraft Discord server helper bot

## Setup

`clone` or fork repo

Python 3.5 or greater required

### Create Discord bot user
Follow instructions here to create your own bot user, get a bot token, and invite the user to your server
https://discordpy.readthedocs.io/en/latest/discord.html

### Setup config file
Make a copy of [TEMPLATE_config.py](TEMPLATE_config.py) named `config.py` and save into root directory of the bot.
At minimum you must supply a bot token in this file. All others are optional. Documentation provides information on how options
are utilized and what to supply.

### Install requirements
Install the requirements to run the project from [requirements.txt](requirements.txt) with
`pip install requirements.txt`

## Run the bot
### For development:
`python python_bot.py`

### always on and auto updating
Run the bot always and automatically get updates from git repo:
`python auto_update_git.py`
(NOTE: This also requires you to install [GitPython](https://gitpython.readthedocs.io/en/stable/), `pip install GitPython`)

## Contributing
Contributions to the code base should be in the form a pull request. Issues can be raised as an issue here on Github.

## Notes
This bot was originally designed specifically, and only for, Digital Terrain minecraft server. I will attempt to investigate and fix reported bugs but I will not necessarily add any enhancements to try accomdate your specific use-case.