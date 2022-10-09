import os                           # classis Python library
import json                         # json
import requests                     # cat facts
import discord                      # the name says it all..
from discord import app_commands    # we use a 'tree' containing 'commands'. commands can be user by users to trigger an action on the bot
from dotenv import load_dotenv      # we will use a file called .env in which we save data that we do not want to show in code, such as 'your-discord-api-token' 

""" retrieve the token from your .env file => good practice """
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

""" some general variables => if you want others (non-devs) to be able to change things, consider to put some in your .env or even TXT, XLSX file and read it """
all_commands_for_this_tutorial = \
    f"The users from Medium can only use:\n\
    /mediumcats"

class dClient(discord.Client):
    """ 
    we initiate the 'client' here which is the bot 
    on __initilization__ we tell discord that we would like to use most of it's feautures by providing Intents.Default
    self.synced = False -> is self made and makes sure that on __init__ the (tree)commands will be synced

    on_ready is a discord function of this class which we will use to add some empty dictionairies which will serve to store our data in

    the __str__ method let's us see what's inside the bot whenever we use print(bot) in the script

    """

    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='/')
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()

        if not self.synced:
            await tree.sync()
            self.synced = True

        self.tempChannels = {}
        self.voiceChannels = {}
        self.openGroupRequests = {}
    
    def __str__(self):

        return(
            f'\n{self.user} is connected\n'
            f'Server ID: {self.ownServerID}\n'
            f'Server Guilds: {self.guilds}\n'
            #f'Server Roles: {self.guildRoles}\n'
            f'Temp Voice Channels: {self.tempChannels}\n'
            f'Open Requests Msgs: {self.openGroupRequests}\n'
        )

""" we initiate the Client, and add the Tree Commands"""
bot = dClient()
tree = app_commands.CommandTree(bot)

@tree.command(name='mediumcats')
async def cats(ctx):

    """ 
    provides the user a random cat fact fetched from an API
    the user can use /mediumcats on any server where the bot is added :)
    """

    request = requests.get('https://catfact.ninja/fact')
    response = json.loads(request.content)['fact']
    print(f'cat fact of the day:\n{response}\n')

    await ctx.response.send_message(f'Here is your cat fact of the day, besides that they are cool:\n{response}')
    return


bot.run(TOKEN)
print(f'Bot is ready for use:\n{bot}')