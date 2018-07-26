import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

	
	
	
	
# This command prints out a link to the SASP SOP	
@bot.command()
async def sop(ctx):
	await ctx.send("Here are the Standard Operating Procedures for the San Andreas State Police: https://docs.google.com/document/d/1KSx0TRJNOxV519Fn7saWGD6E9rIEKA2hWOa6U0BSWYY/edit")

# This command prints out a link to the SASP Uni & Veh Guides	
@bot.command()
async def vguide(ctx):
	await ctx.send("Here are the Uniform and Vehicle Guidelines for the San Andreas State Police: https://docs.google.com/document/d/1KrCscKX3FfANuiBJadci9ElmYpFkz4BPlmNPLMYTir0/edit")

	
	
	
	
# This command prints out info about the bot itself
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="__State Police Information Bot__", description="_Used to convey information about HighSpeed-Gaming's State Police_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")

    embed.add_field(name="Author", value="Sergeant M. Cortez (brandon#9648)")
    embed.add_field(name="Disclaimer", value="If the bot stops working an update is being pushed to it or I broke something.")

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

    embed.add_field(name="!sop", value="Gives the Standard Operating Procedures for the State Police", inline=False)
    embed.add_field(name="!vguide", value="Gives the Vehicle and Uniform Guidelines for the State Police", inline=False)
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
	
    embed.add_field(name="I want to report someone", value="Contact your Field/Troop or Unit Supervisor first, if you think it's a large issue and needs to be handled outside of your division contact IA here: http://sasp.highspeed-gaming.com/index.php?/forum/49-complaints-office/", inline=False)
    embed.add_field(name="What Troop am I in?/Who is my Supervisor(s)?", value="Utilize this (http://sasp.highspeed-gaming.com/index.php?/topic/21-san-andreas-state-police-division-placements/) to figure out what troop you're in, if you can't find yourself, utilize #support", inline=False)
    embed.add_field(name="What are the different Divisions?", value="!divisions to learn more", inline=False)
    embed.add_field(name="Where do I apply for Divisions?", value="!divinfo to learn more", inline=False)
	
	
    await ctx.send(embed=embed)
	
	
	
# This command prints out a list of divisions and their divisional heads, as well as how to learn more info about them	
@bot.command()
async def divisions(ctx):
    embed = discord.Embed(title="__State Police Divisions__", description="_Divisions within the State Police are:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="01 Administration", value="Lead by MT J. Loggins and MT A. Vyrilis", inline=False)
    embed.add_field(name="02 Patrol", value="Lead by Lt. E. Burnett and 1stSgt A. Spahalski", inline=False)
    embed.add_field(name="03 Traffic Enforcement Division", value="Lead by Sgt A. Mattis and Sgt R. Westhouse", inline=False)
    embed.add_field(name="04 K-9 Unit", value="Lead by Cpl J. Boudreaux (Acting) and MT M. Anderson", inline=False)
    embed.add_field(name="05 Crime Suppression Unit", value="Lead by Sgt R. Reddington and MT A. Vyrilis", inline=False)
    embed.add_field(name="06 Aviation and Marine Unit", value="Lead by 1stSgt A. Spahalski and Col R. Brooks", inline=False)
    embed.add_field(name="07 Criminal Investigations Unit", value="Lead by Cpl E. Cane (Acting) and Sgt M. Anderson", inline=False)
    embed.add_field(name="08 Tactical Response Unit", value="Lead by Sgt M. Cortez and Cpl T. Woods", inline=False)
    embed.add_field(name="09 Training Academy", value="Lead by Cpl B. Vance and MT J. Brown", inline=False)
    embed.add_field(name="Divisional Info", value="!divinfo to learn more about each division", inline=False)
	
    await ctx.send(embed=embed)
	
# This command prints out a list of each division and info regarding them
@bot.command()
async def divinfo(ctx):
    embed = discord.Embed(title="__State Police Divisional Info__", description="_List of commands to learn more about each division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="!adm", value="Command for more info about Administration", inline=False)
    embed.add_field(name="!pat", value="Command for more info about Patrol", inline=False)
    embed.add_field(name="!ted", value="Command for more info about Traffic Enforcement", inline=False)
    embed.add_field(name="!k9", value="Command for more info about K9", inline=False)
    embed.add_field(name="!csu", value="Command for more info about Crime Suppression", inline=False)
    embed.add_field(name="!amu", value="Command for more info about Aviation and Marine", inline=False)
    embed.add_field(name="!ciu", value="Command for more info about Criminal Investigations", inline=False)
    embed.add_field(name="!tru", value="Command for more info about Tactical Response", inline=False)
    embed.add_field(name="!aca", value="Command for more info about Training", inline=False)
	
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
    embed.add_field(name="Application:", value="http://sasp.highspeed-gaming.com/index.php?/topic/25-san-andreas-state-police-application-format/", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Traffic Enforcement Division	
@bot.command()
async def ted(ctx):
    embed = discord.Embed(title="__Traffic Enforcement Information__", description="_Some important information regarding the Traffic Enforcement division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant A. Mattis and Sergeant R. Westhouse", inline=False)
    embed.add_field(name="Description", value="This division cracks down on traffic laws and pursuit techniques. T.E.D. has access to motorcycle and sports car units for pursuits", inline=False)
    embed.add_field(name="Application Status", value="Closed", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSf2rLH6NgRqE9-IgNjgEJNc-68b-u1OYA_y08EkBKFDw2Y51w/closedform", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the K9 Division	
@bot.command()
async def k9(ctx):
    embed = discord.Embed(title="__K9 Information__", description="_Some important information regarding the K9 division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal J. Boudreaux (Acting Commander) and Master Trooper M. Anderson", inline=False)
    embed.add_field(name="Description", value="The mission of the K-9 unit is to provide assistance to on duty law enforcement using teamwork and a superior sense of smell and hearing. The K-9 unit works as a cohesive unit providing assistance in apprehension, searches, obtaining warrants,  locating narcotics, weapons, or even explosive devices.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSdnkJYL-0QZI0WOfrd-kC68TOWPkKtA4HPQrUnpLQoSYRB_SQ/viewform", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Crime Suppression Division	
@bot.command()
async def csu(ctx):
    embed = discord.Embed(title="__Crime Suppression Information__", description="_Some important information regarding the Crime Suppression division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant R. Reddington and Master Trooper A. Vyrilis", inline=False)
    embed.add_field(name="Description", value="The Crime Suppression Unit is a specialized investigative unit within the San Andreas State Police Department whose primary role is to monitor, document, investigate the crime, attempt to identify and arrest perpetrators, and prevent further criminal activity.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSeAKv_TobhZFomfHyl-oUpTN2i5wHxjvsXND9AJCCbfZz7urA/viewform", inline=False)
	
    await ctx.send(embed=embed)	
	
# This command lists information about the Aviation and Marine Division
@bot.command()
async def amu(ctx):
    embed = discord.Embed(title="__Aviation and Marine Information__", description="_Some important information regarding the Aviation and Marine division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant A. Spahalski and Colonel R. Brooks", inline=False)
    embed.add_field(name="Description", value="This unit is capable of utilising aircraft and watercraft to assist ground units in situations such as high speed vehicle pursuits, search operations and general patrols from both sea and air", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSedXP7YPHIExyo6JS1X-4tTbi14NoJIF4sCW9Q1SyPyO3konQ/viewform", inline=False)
	
    await ctx.send(embed=embed)
		
# This command lists information about the Criminal Investigations Division
@bot.command()
async def ciu(ctx):
    embed = discord.Embed(title="__Criminal Investigations Information__", description="_Some important information regarding the Criminal Investigations division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal E. Cane (Acting Commander) and Sergeant M. Anderson", inline=False)
    embed.add_field(name="Description", value="Investigates fraudulent action, crime scenes and criminal actions. We take our job seriously, will you?", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSfmznYvwyrIesdVWKy0_oshviC7Xswj49utcygyGnwKFw1ukw/viewform", inline=False)
	
    await ctx.send(embed=embed)
	
# This command lists information about the Tactical Response Unit
@bot.command()
async def tru(ctx):
    embed = discord.Embed(title="__Tactical Response Information__", description="_Some important information regarding the Tactical Response division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Sergeant M. Cortez and Corporal T. Woods", inline=False)
    embed.add_field(name="Description", value="The Tactical Response unit is a group comprised of highly trained marksmen, negotiators and specialists prepared to take on high priority situations with the utmost care and expertise.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application:", value="https://docs.google.com/forms/d/e/1FAIpQLSdDHdUCCGoGmoNdHNja9g7pFHhWLIIsTe6irmvJxCFEJpcfOg/viewform", inline=False)
	
    await ctx.send(embed=embed)
		
# This command lists information about the Academy Division
@bot.command()
async def aca(ctx):
    embed = discord.Embed(title="__Training Academy Information__", description="_Some important information regarding the Training Academy division:_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Leaders", value="Corporal B. Vance and Master Trooper J. Brown", inline=False)
    embed.add_field(name="Description", value="Training Academy provides a training pipeline for the freshly accepted Cadets to prepare them.", inline=False)
    embed.add_field(name="Application Status", value="Open", inline=False)
    embed.add_field(name="Application: (FTO)", value="https://docs.google.com/forms/d/e/1FAIpQLSfL3z6xym5di9cqYERnRmvfygD4BRCuHv1mYB3p1e_icqGPdQ/viewform", inline=False)
    embed.add_field(name="Application: (Instructor)", value="https://docs.google.com/forms/d/e/1FAIpQLSfD4awywhouEzHnNNi6hRQBrjYXdgcd9ZpcXieWRcUF3aYehw/viewform", inline=False)
	
    await ctx.send(embed=embed)
			
	
	
	

	
	
bot.run('NDcxNzgwODg0MDE4ODg4NzE2.Djp07A.hXNPasOxBnfLjTRqlLdPFc-NRYU')
