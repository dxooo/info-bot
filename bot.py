# This bot requires no permissions in order to work besides being able to read and write in whatever channel it's left in

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
	
# Greet new users and provide helpful information	
@bot.event
async def on_member_join(member):
    print('User Joined')
    embed = discord.Embed(title="__Welcome to the San Andreas State Police Discord!__", description="_Here are a few tips & tricks to get you started!_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
	
    embed.add_field(name="Signing In", value="Make sure you head over to the #signing-in channel in order to be granted your tags, you will be asked for your Name and Unit Number, if you're a Cadet your callsign will start with an R-, otherwise it will be a P-", inline=False)
    embed.add_field(name="Information", value="There are two main sources of important information within the discord, they can be found in two places. You can either find them in the top 6 text channels, (information - library,) or through this bot. !help to get started.", inline=False)
    embed.add_field(name="Channels", value="Regardless if you're a Cadet or Trooper you will have access to the 'SASP General' category of channels, these are general hangout places with some self explanatory names, please make sure you're using each channel appropriately", inline=False)
    embed.add_field(name="Questions?", value="If at any point you have any other questions please check our !faq or ask around, I am sure anyone would be willing to help!", inline=False)
    embed.add_field(name="Bot Help", value="Please contact brandon#9658 (Sergeant Cortez,) if you need any assistance with the bot and using !help, !faq and !cmds doesn't get you to where you need to be, thanks!", inline=False)
	
    
    await member.send(embed=embed)

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
    embed.add_field(name="Transfers", value="[Click Here](http://sasp.highspeed-gaming.com/index.php?/forum/68-transfers/)", inline=False)
	
    await ctx.send(embed=embed)

@bot.command()
async def searchpc(ctx, *, arg):
    temporary = """1.01 Inadmissible Defences
1.02 Admissible Defences
1.03 Persons Liable to Punishment
2.01 Principals and Accessories
2.02 Principles to a Crime
2.03 Accessories to a Crime
3.01 Bribery
3.02 Felony Bribery
3.03 Reception of a Bribe
3.04 Felony Reception of a Bribe
3.05 Obstruction of a Public Official
3.06 Aggravated Obstruction of a Public Official
4.01 Rescue
4.02 Escape
4.03 Aiding Escape
4.04 Resisting Arrest
4.05 Failure to Identify
4.06 Obstruction of a Government Employee
4.07 Misuse of a Government Hotline
4.08 Tampering With Evidence
4.09 Forgery of Public Record
4.10 Perjury
4.11 Falsification of Evidence
4.12 Dissuading a Witness
4.13 Evading
4.14 Felony Reckless Evading
4.15 Refusal to Sign
4.16 Failure to Pay Fine
4.17 Contempt of Court
4.18 Provision of False Information to A State Employee
4.19 False Complaint
4.20 Human Trafficking
4.21 Violation of Parole or Probation
4.22 False Personation
4.23 Peace Officer Refusing to Arrest
4.24 False Report of Crime or Emergency
4.25 Street Gang Membership
5.01 Intimidation
5.02 Assault
5.03 Assault With a Deadly Weapon
5.04 Mutual Combat
5.05 Battery
5.06 Aggravated Battery
5.07 Attempted Murder
5.08 Manslaughter
5.09 Murder
5.10 False Imprisonment
5.11 Kidnapping
5.12 Mayhem
5.13 Hate Crime
5.14 Hostage Taking
6.01 Indecent Exposure
6.02 Obscene Exhibition
6.03 Bawdy or Disorderly House
6.04 Prostitution
6.05 Solicitation
6.06 Pandering
6.07 Sexual Assault
6.08 Sexual Battery
6.09 Rape
6.10 Stalking
6.11 Disorderly Conduct
7.01 Possession of a Controlled Substance
7.02 Possession of a Controlled Substance with Intent to Distribute
7.03 Possession of Drug Paraphernalia
7.04 Maintaining a Place for Purpose of Distribution
7.05 Manufacture of a Controlled Substance
7.06 Sale of a Controlled Substance
7.07 Possession of an Open Container
7.08 Public Intoxication
7.09 Public Influence of a Controlled Substance
7.10 Possession in Excess
7.11 Criminal Threats
7.12 Reckless Endangerment
7.13 Trafficking of a Controlled Substance
8.01 Obstruction of Assembly
8.02 Riot
8.03 Incitement to Riot
8.04 Unlawful Assembly
8.05 Breach of the Peace
8.06 Obstruction of Rightful Passage
9.01 Arson
9.02 Burglary
9.03 Possession of Burglary Tools
9.04 Forgery
9.05 Petty Theft
9.06 Grand Theft
9.07 Embezzlement
9.08 Trespassing
9.09 Robbery
9.10 Armed Robbery
9.11 Receiving Stolen Property
9.12 Vandalism
9.13 Criminal Damage
9.14 Grand Larceny
10.01 Hate Crime
11.01 Extortion
11.02 Money Laundering
12.01 Unlawful Possession of a Firearm
12.02 Unlawful Concealment of a Firearm
12.03 Unlawful Carry of a Firearm
12.04 Unlawful Display of a Firearm
12.05 Unlawful Discharge of a Firearm
12.06 Unlawful Possession of a Deadly Weapon
12.07 Unlawful Display of a Deadly Weapon
12.08 Unlawful Concealment of a Deadly Weapon
12.09 Unlawful Possession of An Explosive Device
12.10 Manufacture of an Explosive Device
12.11 Unlawful Distribution of a Firearm
12.12 Unlawful Possession of Firearms with Intent to Sell
12.13 Unlawful Modification of a Firearm"""
    us_inpt = arg  
    found_list = []

    for line in temporary.splitlines():
      if us_inpt.lower() in line.lower():
        found_list.append(line)	  
    embed = discord.Embed(title="__San Andreas Penal Code Lookup__", description=("It looks like you searched for "+us_inpt), color=0x3D59AB)
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
    embed.add_field(name="Here's what we found based on your search:", value=', '.join(found_list), inline=False)
    await ctx.send(embed=embed)
	
@bot.command()
async def searchvc(ctx, *, arg):
    temporary = """13.01 Reckless Driving
13.01(b) Reckless Driving Causing Bodily Injury
13.02 Eluding / Evading a Peace Officer
13.03 Hit and Run
13.03(b) Hit and Run With Injury
13.04 Failure to Yield to a TCD
13.05 Speeding
13.06 Driving Wrong Way
13.07 Illegal Window Tint
13.08 Failure to Maintain Lane
13.09 Impeding Traffic
13.10 Open Alcohol Container
13.10(b) Open Alcohol Container Under 21
13.10(c) Driving in Possession of Marijuana
13.11 Exhibition of Speed
13.12 Illegal Vehicle Modifications
13.13 Operating an Unroadworthy Vehicle
13.14 Failure to display License Plate
13.15 Failure to Yield to Emergency Vehicle(s)
13.16 Unsafe Vehicle Load
13.17 Driving on Sidewalk
13.18 Interfering with Driver's Control of Vehicle
13.19 Following too Closely
13.20 Motorcycles: Lane Splitting
13.21 Illegal Passing
13.22 Unsafe Operation of Emergency Vehicle
13.23 Driving Without Headlights at Night
13.24 Failure to Dim Lights
13.25 Driving Without a Valid License
13.26 Failure to Show a Driver's License
13.27 Illegal Parking
13.28 Driving Under the Influence of Alcohol
13.28(b) Driving Under the Influence of Drugs
13.29 Broken Tail Light / Headlights
13.30 Jaywalking
13.31 Possession of Sirens & Emergency Lighting
13.31(b) Possession of Sirens & Emergency Lighting With Intent to Impersonate
13.32 Failure to Wear Motorcycle Helmet
13.33 Hitchhiking
13.34 Driving with a Suspended License
13.35 Failure to Signal Lane Change
13.36 Use of Hydraulics on Public Roads
13.37 Intentionally Altering or Destroying a VIN
13.38 Buying or Possessing a Vehicle with an Altered VIN
13.39 Felony Speeding"""
    us_inpt = arg  
    found_list = []

    for line in temporary.splitlines():
      if us_inpt in line:
        found_list.append(line)	  
    embed = discord.Embed(title="__San Andreas Vehicle Code Lookup__", description=("It looks like you searched for "+us_inpt), color=0x3D59AB)
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")
    embed.add_field(name="Here's what we found based on your search:", value=', '.join(found_list), inline=False)
    await ctx.send(embed=embed)
   
	
	
	
	
# This command prints out info about the bot itself
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="__State Police Information Bot__", description="_Used to convey information about HighSpeed-Gaming's State Police_", color=0x3D59AB)
	
    embed.set_author(name="State Police Info Bot", icon_url="https://cdn.discordapp.com/attachments/393324031505465344/471855906699739136/sasp_logo_updated_2018.png")

    embed.add_field(name="Author", value="Sergeant M. Cortez (brandon#9648), Sergeant R. Reddington (Raymond#2592)")
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

    embed.add_field(name="!searchpc", value="Allows a user to search through the list of Penal Codes", inline=False)
    embed.add_field(name="!searchvc", value="Allows a user to search through the list of Vehicle Codes", inline=False)	
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
    embed.add_field(name="03 Traffic Enforcement Division (!ted)", value="Lead by Sgt A. Mattis", inline=False)
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
	
    embed.add_field(name="Leaders", value="Sergeant A. Mattis", inline=False)
    embed.add_field(name="Description", value="The Traffic Enforcement Division is a specialized division within the San Andreas State Police that was originally created to combat driving under the influence and careless driving in general", inline=False)
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
    embed.add_field(name="Application Status", value="Closed", inline=False)
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
