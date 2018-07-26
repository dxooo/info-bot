# This bot requires no permissions in order to work besides being able to read and write in whatever channel it's left in
# This bot was created for HighSpeed-Gaming's State Police Discord
# This bot was created by brandon#9648 aka Sergeant Cortez
# This bot is released as-is and further changes made are only to benefit the State Police

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# This command prints out a list of quick links for ease of user
@bot.command()
async def links(ctx):
    embed = discord.Embed(title="__State Police Quick Links__", description="_Used to convey quick links to important information about the State Police_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Standard Operating Procedures", value="[Click Here](https://docs.google.com/document/d/1KSx0TRJNOxV519Fn7saWGD6E9rIEKA2hWOa6U0BSWYY/edit)", inline=False)
    embed.add_field(name="Uniform and Vehicle Guidelines", value="[Click Here](https://docs.google.com/document/d/1KrCscKX3FfANuiBJadci9ElmYpFkz4BPlmNPLMYTir0/edit)", inline=False)
    embed.add_field(name="Penal Codes", value="[Click Here](https://docs.google.com/spreadsheets/d/1_HbwpqX9-QhGZ7oZkT3dmzW_O448hD86c-PqfmpvYIY/edit#gid=0)", inline=False)
    embed.add_field(name="Roster", value="[Click Here](http://sasp.highspeed-gaming.com/index.php?/topic/22-san-andreas-state-police-roster/)", inline=False)
    embed.add_field(name="Divisional Placements", value="[Click Here](http://sasp.highspeed-gaming.com/index.php?/topic/21-san-andreas-state-police-division-placements/)", inline=False)
    embed.add_field(name="Punitive Articles/Disciplinary Policy", value="[Click Here](http://sasp.highspeed-gaming.com/index.php?/topic/79-san-andreas-state-police-punitive-articles-and-disciplinary-policy/)", inline=False)
	
    await ctx.send(embed=embed)
	
	
	
	
# This command prints out info about the bot itself
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="__State Police Information Bot__", description="_Used to convey information about HighSpeed-Gaming's State Police_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")

    embed.add_field(name="Author", value="Sergeant M. Cortez (brandon#9648)")
    embed.add_field(name="Suggestions", value ="DM brandon#9648 to make suggestions about the future of the bot.")
    embed.add_field(name="Disclaimer", value="If the bot stops working an update is being pushed to it or I broke something.")
    embed.set_footer(text="'neat, i made a bot to incentivize lazyness' - brandon")


    await ctx.send(embed=embed)

	
	
	
	
# This command removes the default help command
bot.remove_command('help')

# This command is the reworked help command once the default one is removed
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__Help Box__", description="_You appear to need help, let me get you started._", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="!cmds", value="Type this command in chat to get started, this should get you where you need to go.", inline=False)
	
    await ctx.send(embed=embed)

	
# This command lists the base of commands for users to utilize
@bot.command()
async def cmds(ctx):
    embed = discord.Embed(title="__State Police Information Bot__", description="_List of commands are:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")

    embed.add_field(name="!links", value="Gives a list of important links for the State Police", inline=False)
    embed.add_field(name="!divisions", value="Gives the list of State Police Divisions and their Division Heads", inline=False)
    embed.add_field(name="!faq", value="Gives a list of info about Frequently Asked Questions", inline=False)
    embed.add_field(name="!info", value="Gives information about the bot", inline=False)
    embed.add_field(name="!cmds", value="Gives a message containing important commands for the bot", inline=False)

    await ctx.send(embed=embed)

	
	
	
# This command is to show answers to FAQ
@bot.command()
async def faq(ctx):
    embed = discord.Embed(title="__Frequently Asked Questions__", description="_Answers and links to FAQ:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="I want to report someone", value="Contact your Field/Troop or Unit Supervisor first, if you think it's a large issue and needs to be handled outside of your division contact IA [here](http://sasp.highspeed-gaming.com/index.php?/forum/49-complaints-office/)", inline=False)
    embed.add_field(name="What Troop am I in?/Who is my Supervisor(s)?", value="Utilize [this](http://sasp.highspeed-gaming.com/index.php?/topic/21-san-andreas-state-police-division-placements/) to figure out what troop you're in, if you can't find yourself, utilize #support", inline=False)
    embed.add_field(name="What are the different Divisions?", value="!divisions to learn more", inline=False)
    embed.add_field(name="How do I get promoted?", value="Complete [this](https://docs.google.com/forms/d/e/1FAIpQLSdTN9DGGpIFcUX1rIOBJTimyEhE06oBtcIxvRVTt6PNCj09Qw/viewform) exam and wait to hear back from Command in regards to the status of it", inline=False)
	
	
    await ctx.send(embed=embed)
	
	
	
# This command prints out a list of divisions and their divisional heads, as well as how to learn more info about them	
@bot.command()
async def divisions(ctx):
    embed = discord.Embed(title="__State Police Divisions__", description="_Divisions within the State Police are:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="01 Administration (!adm)", value="Lead by MT J. Loggins and MT A. Vyrilis", inline=False)
    embed.add_field(name="02 Patrol (!pat)", value="Lead by Lt. E. Burnett and 1stSgt A. Spahalski", inline=False)
    embed.add_field(name="03 Traffic Enforcement Division (!ted)", value="Lead by Sgt A. Mattis and Sgt R. Westhouse", inline=False)
    embed.add_field(name="04 K-9 Unit (!k9)", value="Lead by Cpl J. Boudreaux (Acting) and MT M. Anderson", inline=False)
    embed.add_field(name="05 Crime Suppression Unit (!csu)", value="Lead by Sgt R. Reddington and MT A. Vyrilis", inline=False)
    embed.add_field(name="06 Aviation and Marine Unit (!amu)", value="Lead by 1stSgt A. Spahalski and Col R. Brooks", inline=False)
    embed.add_field(name="07 Criminal Investigations Unit (!ciu)", value="Lead by Cpl E. Cane (Acting) and Sgt M. Anderson", inline=False)
    embed.add_field(name="08 Tactical Response Unit (!tru)", value="Lead by Sgt M. Cortez and Cpl T. Woods", inline=False)
    embed.add_field(name="09 Training Academy (!aca)", value="Lead by Cpl B. Vance and MT J. Brown", inline=False)
    embed.set_footer(text="For more info: Utilize the commands posted next to each division")
	
    await ctx.send(embed=embed)
	
	
	
# This command lists information about the Administration Division	
@bot.command()
async def adm(ctx):
    embed = discord.Embed(title="__Administration Information__", description="_Some important information regarding the Administration division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Master Trooper J. Loggins and Master Trooper A. Vyrilis", inline=False)
    embed.add_field(name="Description", value="The Administration Division was created to handle most of the duties regarding paperwork and behind the scene personas of the Department. This team ensures to keep the department up to date.", inline=False)
    embed.add_field(name="Application Status", value="Closed", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Patrol Division	
@bot.command()
async def pat(ctx):
    embed = discord.Embed(title="__Patrol Information__", description="_Some important information regarding the Patrol division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Lieutenant E. Burnett and First Sergeant A. Spahalski", inline=False)
    embed.add_field(name="Description", value="The main division within the State Police, housing every member of the State Police regardless of status within other divisions", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](http://sasp.highspeed-gaming.com/index.php?/topic/25-san-andreas-state-police-application-format/)", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Traffic Enforcement Division	
@bot.command()
async def ted(ctx):
    embed = discord.Embed(title="__Traffic Enforcement Information__", description="_Some important information regarding the Traffic Enforcement division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant A. Mattis and Sergeant R. Westhouse", inline=False)
    embed.add_field(name="Description", value="This division cracks down on traffic laws and pursuit techniques. T.E.D. has access to motorcycle and sports car units for pursuits", inline=False)
    embed.add_field(name="Application Status", value="Closed", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSf2rLH6NgRqE9-IgNjgEJNc-68b-u1OYA_y08EkBKFDw2Y51w/closedform)", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the K9 Division	
@bot.command()
async def k9(ctx):
    embed = discord.Embed(title="__K9 Information__", description="_Some important information regarding the K9 division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal J. Boudreaux (Acting Commander) and Master Trooper M. Anderson", inline=False)
    embed.add_field(name="Description", value="The mission of the K-9 unit is to provide assistance to on duty law enforcement using teamwork and a superior sense of smell and hearing. The K-9 unit works as a cohesive unit providing assistance in apprehension, searches, obtaining warrants,  locating narcotics, weapons, or even explosive devices.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSdnkJYL-0QZI0WOfrd-kC68TOWPkKtA4HPQrUnpLQoSYRB_SQ/viewform)", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Crime Suppression Division	
@bot.command()
async def csu(ctx):
    embed = discord.Embed(title="__Crime Suppression Information__", description="_Some important information regarding the Crime Suppression division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant R. Reddington and Master Trooper A. Vyrilis", inline=False)
    embed.add_field(name="Description", value="The Crime Suppression Unit is a specialized investigative unit within the San Andreas State Police Department whose primary role is to monitor, document, investigate the crime, attempt to identify and arrest perpetrators, and prevent further criminal activity.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSeAKv_TobhZFomfHyl-oUpTN2i5wHxjvsXND9AJCCbfZz7urA/viewform)", inline=False)
	
    await ctx.send(embed=embed)	
	
# This command lists information about the Aviation and Marine Division
@bot.command()
async def amu(ctx):
    embed = discord.Embed(title="__Aviation and Marine Information__", description="_Some important information regarding the Aviation and Marine division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant A. Spahalski and Colonel R. Brooks", inline=False)
    embed.add_field(name="Description", value="This unit is capable of utilising aircraft and watercraft to assist ground units in situations such as high speed vehicle pursuits, search operations and general patrols from both sea and air", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSedXP7YPHIExyo6JS1X-4tTbi14NoJIF4sCW9Q1SyPyO3konQ/viewform)", inline=False)
	
    await ctx.send(embed=embed)
		
# This command lists information about the Criminal Investigations Division
@bot.command()
async def ciu(ctx):
    embed = discord.Embed(title="__Criminal Investigations Information__", description="_Some important information regarding the Criminal Investigations division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal E. Cane (Acting Commander) and Sergeant M. Anderson", inline=False)
    embed.add_field(name="Description", value="The Criminal Investigations Unit is a group of highly trained investigators who investigate vast amount of crimes. We investigate fraudulent action, crime scenes and other criminal actions. We take our investigations seriously, do you?", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSfmznYvwyrIesdVWKy0_oshviC7Xswj49utcygyGnwKFw1ukw/viewform)", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Tactical Response Unit
@bot.command()
async def tru(ctx):
    embed = discord.Embed(title="__Tactical Response Information__", description="_Some important information regarding the Tactical Response division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant M. Cortez and Corporal T. Woods", inline=False)
    embed.add_field(name="Description", value="The Tactical Response unit is a group comprised of highly trained marksmen, negotiators and specialists prepared to take on high priority situations with the utmost care and expertise.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSdDHdUCCGoGmoNdHNja9g7pFHhWLIIsTe6irmvJxCFEJpcfOg/viewform)", inline=False)
	
    await ctx.send(embed=embed)
		
# This command lists information about the Academy Division
@bot.command()
async def aca(ctx):
    embed = discord.Embed(title="__Training Academy Information__", description="_Some important information regarding the Training Academy division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal B. Vance and Master Trooper J. Brown", inline=False)
    embed.add_field(name="Description", value="Training Academy provides a training pipeline for the freshly accepted Cadets to prepare them.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application: (FTO)", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSfL3z6xym5di9cqYERnRmvfygD4BRCuHv1mYB3p1e_icqGPdQ/viewform)", inline=False)
    embed.add_field(name="Application: (Instructor)", value="[Click Here](https://docs.google.com/forms/d/e/1FAIpQLSfD4awywhouEzHnNNi6hRQBrjYXdgcd9ZpcXieWRcUF3aYehw/viewform)", inline=False)
	
    await ctx.send(embed=embed)
			
	
	
	

	
	
bot.run('NDcxNzgwODg0MDE4ODg4NzE2.DjrfPw.QmjFc2hXFQIAQopyRNSSjwicY_M')
