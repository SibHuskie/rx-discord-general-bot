import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='414089074870321153')
footer_text = "[Realm X] - [X General]"

member_role = '453194601247801354'
bot1_role = '453194562379186176'
bot2_role = '453195460346380288'
owner_role = '453194638077984768'
partner_role = '453194705732239360'
lvl2_role = '453194792457732096'
lvl5_role = '453195170662449152'
lvl10_role = '453195184327491594'
lvl15_role = '453195194607861761'
lvl20_role = '453195205416321034'
lvl25_role = '453195220192854027'
lvl35_role = '453195231517474826'
lvl40_role = '453195258675855361'
lvl50_role = '453195292376825856'
vip_role = '453195303403913227'
legend_role = '453195358575656986'
punished_role = '453195421611982848'
helper_role = '453195469309476877'
mod_role = '453195518785486858'
admin_role = '453195993987416064'
manager_role = '453196026547929088'
cbot_role = '453247674674577408'
hell_role = '453247719067090944'
nsfw_role = '453247786637590570'
lvl0_role = '453653105696047105'
error_img = ':octagonal_sign:'
release_date = '25th of June, 2018'
banner = "https://i.imgur.com/rzWqGdW.png"
logs = '453219479963303936'
default_invite = 'https://discord.gg/UBh9FpK'

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("X - GENERAL")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name="General Tasks.exe"))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    joins = ["**{}** joined the game!".format(userName.name),
             "**{}**, we've been expecting you...".format(userName.name),
             "**{}**, hey! We hope you brought pizza!".format(userName.name),
             "**{}**, welcome!".format(userName.name),
             "**{}** is here! Everyone, look busy!".format(userName.name),
             "It's dangerous to go alone, take **{}** with you!".format(userName.name),
             "Shut up! **{}** is here!".format(userName.name),
             "A wild **{}** has appeared!".format(userName.name),
             "**{}** has been summoned!".format(userName.name),
             "Everyone, gather around. **{}** came to visit us!".format(userName.name),
             "**{}** has joined your party!".format(userName.name),
             "**{}** has spawned!".format(userName.name),
             "Holy shit! **{}** is here!".format(userName.name),
             "Roses are red, violets are blue, **{}** joined the server, you should invite your friends too!".format(userName.name),
             "**{}** just slid into the server!".format(userName.name),
             "**{}** is ready and waiting!".format(userName.name),
             "Achievement earned: Find **{}**.".format(userName.name),
             "**{}** joined your team! Can I get a heal?".format(userName.name),
             "**{}** is here! Leave your weapons by the door.".format(userName.name),
             "Brace yourselves, here comes **{}**!".format(userName.name),
             "**{}** joined the server! Seems OP - please nerf.".format(userName.name),
             "Hey, **{}**! About time you joined.".format(userName.name),
             "Welcome **{}**. Make yourself at home.".format(userName.name),
             "**{}** joined! Please no hacks!".format(userName.name),
             "**{}** joined the server! Seems legit.".format(userName.name)]
    await client.send_message(client.get_channel("453192466716164137"), ":chart_with_upwards_trend: {}".format(random.choice(joins)))
    server = client.get_server('452865346081128448')
    await client.send_message(client.get_channel("453192385795588096"), ":large_blue_circle: `{}` joined the server! Now we have {} members.".format(userName, len(server.members)))
    try:
        await client.send_message(userName, "https://i.imgur.com/KIhV6UG.png\n \nWelcome to **{}**, {}! We hope you enjoy your stay and have fun.\n \nAll information is in the `#rules-and-info` channel, but feel free to ask the staff about anything you want to know.".format(server.name, userName.name))
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["**{}** left! Please insert a coin to continue.".format(userName.name),
              "We lost **{}**! Do not give up yet!".format(userName.name),
              "**{}** died!".format(userName.name),
              "**{}** left the server! Everyone, get back to work.".format(userName.name),
              "We will miss you, **{}**!".format(userName.name),
              "Achievement get: Loose **{}**!".format(userName.name),
              "Good luck, **{}**, you'll need it on your journey!".format(userName.name),
              "**{}** left the server!".format(userName.name),
              "Wait, where did **{}** go?".format(userName.name),
              "Our **{}** has been killed!".format(userName.name),
              "Your **{}** was destroyed!".format(userName.name),
              "And so **{}** went on their journey to become the wizard king!".format(userName.name),
              "No, **{}**! We lost them...".format(userName.name),
              "**{}** left the game!".format(userName.name),
              "**{}** left your party!".format(userName.name),
              "**{}** left the server! Shut up and listen.".format(userName.name),
              "**{}**, you will be remembered.".format(userName.name),
              "**{}**, wait! What about our deal?!".format(userName.name),
              "Damn! Not **{}** too!".format(userName.name),
              "**{}** left the server! Did I do something wrong?".format(userName.name),
              "Swoooosh, **{}** just flew away.".format(userName.name),
              "Hey, **{}**! Where do you- too late...".format(userName.name),
              "You'll be back, **{}**! I'll be waiting!".format(userName.name),
              "Error 404: **{}** not found!".format(userName.name),
              "No one really liked you anyway, **{}**... except me...".format(userName.name)]
    await client.send_message(client.get_channel("453192466716164137"), ":chart_with_downwards_trend: {}".format(random.choice(leaves)))
    server = client.get_server('452865346081128448')
    await client.send_message(client.get_channel("453192385795588096"), ":red_circle: `{}` left the server! Now we have {} members.".format(userName, len(server.members)))

''' COMMANDS FOR EVERYONE '''
# }help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.add_field(name=":incoming_envelope: ", value="You can see all commands in the <#453857880588943374> channel!")
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    channel = ctx.message.channel
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    if option == None:
        msg.add_field(name=error_img, value="Please specify which bot's ping you want to check.\nOptions: `g`, `f`, `s`, `all`.")
    elif option == "g":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    elif option == "f":
        print("")
    elif option == "s":
        print("")
    elif option == "all":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    else:
        msg.add_field(name=error_img, value="Invalid option given!\nOptions: `g`, `f`, `s`, `all`.")
        await client.say(embed=msg)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x210150, url=default_invite, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":link: ", value="Here is the default server invite:\n{}".format(default_invite))
    await client.say(embed=msg)

# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    channel = client.get_channel('453192365096697897')
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give a suggestion.\nExample: `}suggest Create a new role called 'Hella Gey'.`.")
    else:
        if len(str(args)) > 500:
            msg.add_field(name=error_img, value="The suggestion cannot be longer than 500 characters.")
        else:
            m = discord.Embed(colour=0x04FF00, description= "")
            m.title = ""
            m.set_footer(text=footer_text)
            m.add_field(name=":speech_balloon: ", value="{}".format(args))
            m.add_field(name="===============", value="Suggested by: `{}` ### `{}`\nIf you like this suggestion, react with :white_check_mark: and if you don't like it, react with :x:.".format(author, author.id))
            await client.send_message(channel, embed=m)
            async for message in client.logs_from(channel):
                if len(message.reactions) == 0:
                    await client.add_reaction(message, '\u2705')
                    await client.add_reaction(message, '\u274C')
                    break
                else:
                    print("")
            msg.add_field(name=":speech_balloon: ", value="Suggestion sent!\nYou can see it in <#453192365096697897>.")
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    punish = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=error_img, value="Please tag the user you want to get information on.")
    else:
        imageurl = userName.avatar_url
        msg.title = ":page_with_curl: USER INFORMATION"
        msg.set_thumbnail(url=imageurl)
        msg.add_field(name="NAME:", value="`{}`".format(userName), inline=True)
        msg.add_field(name="ID:", value="`{}`".format(userName.id), inline=True)
        msg.add_field(name="CREATED AT:", value="`{}`".format(userName.created_at), inline=True)
        msg.add_field(name="JOINED AT:", value="`{}`".format(userName.joined_at), inline=True)
        msg.add_field(name="STATUS:", value="`{}`".format(userName.status), inline=True)
        msg.add_field(name="IS BOT:", value="`{}`".format(userName.bot), inline=True)
        msg.add_field(name="GAME:", value="{}".format(userName.game), inline=True)
        msg.add_field(name="NICKNAME:", value="`{}`".format(userName.nick), inline=True)
        msg.add_field(name="TOP ROLE:", value="`{}`".format(userName.top_role), inline=True)
        msg.add_field(name="VOICE CHANNEL:", value="`{}`".format(userName.voice_channel), inline=True)
        if punish in userName.roles:
            msg.add_field(name="PUNISHED:", value="True", inline=True)
        else:
            msg.add_field(name="PUNISHED:", value="False", inline=True)
    await client.say(embed=msg)

# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    imageurl = ctx.message.server.icon_url
    msg.set_thumbnail(url=imageurl)
    msg.add_field(name="MEMBERS", value="`{}`".format(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value="`{}`".format(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value="`{}`".format(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value="`{}`".format(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value="`{}`".format(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value="`{}`".format(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value="`{}`".format(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value="`{}`".format(ctx.message.server.created_at), inline=True)
    msg.add_field(name="RELEASE DATE:", value="`{}`".format(release_date), inline=True)
    msg.set_image(url="{}".format(banner))
    await client.say(embed=msg)

# }ad
@client.command(pass_context=True)
async def ad(ctx):
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    m = "So you want to advertise your server?"
    m += "\nOne of the fastest ways to advertise your server is by partnering. But we all know that it takes time and it's very boring."
    m += "\nThat's why we created <@439051827384680449>! This bot will advertise your server on other servers automatically!"
    m += "\nWith this bot you can get up to 72 advertisements per day and even more security for your server. All of the bot's features are completely free!"
    m += "\nFor more information you can use `ad!help`."
    msg.set_image(url='https://i.imgur.com/FQwGkH3.png')
    msg.add_field(name=":a: :regional_indicator_d: ", value=m)
    await client.say(embed=msg)

# }apply <helper/mod/admin/manager/adbot>
@client.command(pass_context=True)
async def apply(ctx, option = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if option == None:
        msg.add_field(name=error_img, value="No option given.\nOptions: `helper`, `mod`, `admin`, `manager`, `adbot`.\n \nExample: `}apply helper`.")
    else:
        if option == "helper":
            try:
                mg = "***__HELPER APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements. They can be found in the #rules-and-info channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions post the application in the #applications channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become a helper?"
                mg += "\n`-` Rate your knowlage of discord and the X Bots (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc.)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `helper` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        elif option == "mod":
            try:
                mg = "***__MODERATOR APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements. They can be found in the #rules-and-info channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions post the application in the #applications channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become a moderator?"
                mg += "\n`-` Rate your knowlag of discord and the X Bots (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server? If yes, what role do you have?"
                mg += "\n`-` Do you know how partnerships work on this server?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `moderator` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        elif option == "admin":
            try:
                mg = "***__ADMINISTRATOR APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements. They can be found in the #rules-and-info channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions post the application in the #applications channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become an administrator"
                mg += "\n`-` Rate your knowlag of discord and the X Bots (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server? If yes, what role do you have?"
                mg += "\n`-` Do you know how partnerships work on this server?"
                mg += "\n`-` Have you ever been muted/punished, banned or kicked and why?"
                mg += "\n`-` Rate your knowlage of administrating discord servers (from 1-10)."
                mg += "\n`-` What do you think your job would be as an administrator?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `administrator` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        elif option == "manager":
            try:
                mg = "***__MANAGER APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements. They can be found in the #rules-and-info channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions post the application in the #applications channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become a manager?"
                mg += "\n`-` Rate your knowlag of discord and the X Bots (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server? If yes, what role do you have?"
                mg += "\n`-` Do you know how partnerships work on this server?"
                mg += "\n`-` Have you ever been muted/punished, banned or kicked and why?"
                mg += "\n`-` Rate your knowlage of administrating discord servers (from 1-10)."
                mg += "\n`-` What do you think your job would be as a manager?"
                mg += "\n`-` Why should we accept you?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `manager` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        elif option == "adbot":
            try:
                mg = "***__ADVERTISER BOT MODERATOR TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements. They can be found in the #rules-and-info channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions post the application in the #applications channel."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been using Advertiser Bot?"
                mg += "\n`-` Rate your knowlage of discord and the bot (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc)?"
                mg += "\n`-` What would you do if another ADbot moderator/administrator is abusing their powers?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server? If yes, what role do you have?"
                mg += "\n`-` Why do you want to become an ADbot moderator?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `advertiser bot moderator` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        else:
            msg.add_field(name=error_img, value="Invalid option given.\nOptions: `helper`, `mod`, `admin`, `manager`, `adbot`.\n \nExample: `}apply helper`.")
    await client.say(embed=msg)

''' COMMANDS FOR VIPS '''
# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="Please give a message that you want the bot to say.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.add_field(name=error_img, value="The message cannot be longer than 1990 characters.")
                await client.say(embed=msg)
            else:
                await client.say("`{}`".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by VIPs and Legends!")
        await client.say(embed=msg)

''' COMMANDS FOR STAFF '''
# }p <user> <message>
@client.command(pass_context=True)
async def p(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    partner = discord.utils.get(ctx.message.server.roles, id=partner_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel('453192314714849290')
    l = client.get_channel(logs)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if userName == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given!\nExample: `}p @Jimmy A badass server where you can't do much but you should totally join, we got free candy and wifi.`.")
        else:
            if len(str(args)) > 1900:
                msg.add_field(name=error_img, value="The message cannot be longer than 1900 characters.")
            else:
                try:
                    a = ctx.message.server.get_member(userName.id)
                    await client.add_roles(userName, partner)
                    m = discord.Embed(colour=0x009BFF, description= "")
                    m.title = ""
                    m.set_footer(text=footer_text)
                    m.add_field(name=":handshake: ", value="{}".format(args))
                    await client.send_message(chnl, embed=m)
                    msg.add_field(name=":handshake: ", value="<@{}> partnered with <@{}>!".format(author.id, userName.id))
                    o = "```diff"
                    o += "\n- PARTNERSHIP -"
                    o += "\n+ Author: {} ### {}".format(author, author.id)
                    o += "\n+ Target: {} ### {}".format(userName, userName.id)
                    o += "\n```"
                    await client.send_message(l, o)
                except:
                    msg.add_field(name=error_img, value="That user has not been found!\nYou can use `}fp <message>` to force the bot to send the partnership message.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)

# }fp <message>
@client.command(pass_context=True)
async def fp(ctx, *, args = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel('453192314714849290')
    l = client.get_channel(logs)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="No message given!\nExample: `}fp A badass server where you can't do much but you should totally join, we got free candy and wifi.`.")
        else:
            if len(str(args)) > 1900:
                msg.add_field(name=error_img, value="The message cannot be longer than 1900 characters.")
            else:
                m = discord.Embed(colour=0x009BFF, description= "")
                m.title = ""
                m.set_footer(text=footer_text)
                m.add_field(name=":handshake: ", value="{}".format(args))
                await client.send_message(chnl, embed=m)
                msg.add_field(name=":handshake: ", value="<@{}> forced a partnership!".format(author.id))
                o = "```diff"
                o += "\n- FORCED PARTNERSHIP -"
                o += "\n+ Author: {} ### {}".format(author, author.id)
                o += "\n```"
                await client.send_message(l, o)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)

# }dp <user> <message id>
@client.command(pass_context=True)
async def dp(ctx, target = None, userName: discord.Member = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    partner = discord.utils.get(ctx.message.server.roles, id=partner_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel('453192314714849290')
    l = client.get_channel(logs)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if userName == None and target == None:
            msg.add_field(name=error_img, value="No arguments given!\nExamples:\n`}dp 453923823272722442 @Jimmy `.\n`}dp 453923823272722442`.\n`}dp # @Jimmy`.")
        else:
            try:
                await client.remove_roles(userName, partner)
                msg.add_field(name=":wave: ", value="<@{}> deleted a partnership made with <@{}>!".format(author.id, userName.id))
            except:
                msg.add_field(name=":wave: ", value="<@{}> deleted a partnership!".format(author.id))
            try:
                async for message in client.logs_from(chnl):
                    if message.id == target:
                        await client.delete_message(message)
                        break
                    else:
                        print("")
            except:
                print("")
            o = "```diff"
            o += "\n- DELETED PARTNERSHIP -"
            o += "\n+ Author: {} ### {}".format(author, author.id)
            o += "\n+ Target: {}".format(userName)
            o += "\n+ Message: {}".format(target)
            o += "\n```"
            await client.send_message(l, o)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)
    
''' COMMANDS FOR ADMIN '''
# }rawsay <text>
@client.command(pass_context=True)
async def rawsay(ctx, *, args = None):
    author = ctx.message.author
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="No text given!")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.add_field(name=error_img, value="The text cannot be longer than 1990 characters.")
                await client.say(embed=msg)
            else:
                await client.say("{}".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Managers and Owners!")
        await client.say(embed=msg)

#######################
client.run(os.environ['BOT_TOKEN'])
