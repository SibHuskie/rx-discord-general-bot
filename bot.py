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
pmanager_role = '473812644021927946'
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
lvl0_role = '453653105696047105'
announcement_role = '473173927213137921'
giveaway_role = '473173863698661386'
error_e = ':octagonal_sign:'
release_date = '25th of June, 2018'
banner = "https://i.imgur.com/rVvSG5L.png"
logs = '453219479963303936'
default_invite = 'https://discord.gg/UBh9FpK'

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("[][][][][][][][][][][][][][]")
    print("[]Logged in!              []")
    print("[][][][][][][][][][][][][][]")
    print("[]Name: X General         []")
    print("[]ID: 453210550399401984  []")
    print("[][][][][][][][][][][][][][]")
    await client.change_presence(game=discord.Game(name="with Task Manager"))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("[]Ping: {}".format(round((t2-t1)*1000)))
    print("[][][][][][][][][][][][][][]")

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    m = "Welcome to **Realm ✘**, <@{}>! We hope you enjoy your stay.".format(userName.id)
    m2 = "https://i.imgur.com/QyY8owZ.png"
    m2 += "\n**~~= = = = = = = = = = = = = = = = = = =~~**"
    m2 += "\nWelcome to **Realm ✘**, {}! We hope you enjoy your stay here."
    m2 += "\nAll the information are in the <#453192283286667264> channel, but feel free to ask the staff about anything."
    m2 += "\n**~~= = = = = = = = = = = = = = = = = = =~~**"
    m2 += "\nThank you for joining!"
    e = ["<a:bobo:474228327734050826>", "<a:ThumbsUpParrot:476294787285254144>", "<a:CatDance:476294788576968705>"]
    await client.send_message(client.get_channel("453192466716164137"), "{} {}".format(random.choice(e), m))
    server = userName.server
    await client.send_message(client.get_channel("453192385795588096"), ":large_blue_circle: `{}` joined the server! Now we have {} members.".format(userName, len(server.members)))
    try:
        dr = discord.utils.get(server.roles, id=member_role)
        member = server.get_member(userName.id)
        await client.add_roles(member, dr)
        await client.send_message(userName, m2)
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    server = client.get_server('452865346081128448')
    await client.send_message(client.get_channel("453192385795588096"), ":red_circle: `{}` left the server! Now we have {} members.".format(userName, len(server.members)))

''' COMMANDS FOR EVERYONE '''
# }help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=0x210150, description= ":incoming_envelope: You can see all commands in the <#453857880588943374> channel.")
    embed.set_footer(text=footer_text)
    await client.say(embed=embed)

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    channel = ctx.message.channel
    msg = discord.Embed(colour=0x210150, title= "")
    msg.set_footer(text=footer_text)
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    if option == None:
        msg.description = "{} Please specify which bot's ping you want to check.\nOptions: `g`, `f`, `s`, `c`, `all`.".format(error_e)
        await client.say(embed=msg)
    elif option == "g":
        msg.description = ":satellite: My ping: `{}ms`.".format(round((t2-t1)*1000))
        await client.say(embed=msg)
    elif option == "f":
        print("")
    elif option == "s":
        print("")
    elif option == "c":
        print("")
    elif option == "all":
        msg.description = ":satellite: My ping: `{}ms`.".format(round((t2-t1)*1000))
        await client.say(embed=msg)
    else:
        msg.description("{} Invalid option given!\nOptions: `g`, `f`, `s`, `c`, `all`.".format(error_e))
        await client.say(embed=msg)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    msg.description = ":link: Here is the default server invite:\n{}".format(default_invite)
    await client.say(embed=msg)

# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    role = discord.utils.get(ctx.message.server.roles, id=lvl5_role)
    role2 = discord.utils.get(ctx.message.server.roles, id=lvl10_role)
    role3 = discord.utils.get(ctx.message.server.roles, id=lvl15_role)
    role4 = discord.utils.get(ctx.message.server.roles, id=lvl20_role)
    role5 = discord.utils.get(ctx.message.server.roles, id=lvl25_role)
    role6 = discord.utils.get(ctx.message.server.roles, id=lvl35_role)
    role7 = discord.utils.get(ctx.message.server.roles, id=lvl40_role)
    role8 = discord.utils.get(ctx.message.server.roles, id=lvl50_role)
    if role in author.roles or role2 in author.roles or role3 in author.roles or role4 in author.roles or role5 in author.roles or role6 in author.roles or role7 in author.roles or role8 in author.roles:
        if args == None:
            msg.description = "{} Please give a suggestion.".format(error_e)
        else:
            if len(str(args)) > 250:
                msg.description = "{} The suggestion cannot be longer than 250 characters.".format(error_e)
            else:
                m = discord.Embed(colour=0x04FF00, title="")
                m.set_footer(text=footer_text)
                m.description = ":speech_balloon: \n{}\n**===============**\nSuggested by: `{}` ### `{}`\nIf you like this suggestion, react with :white_check_mark: and if you don't like it, react with :x:.".format(args, author, author.id)
                message = await client.send_message(client.get_channel('453192365096697897'), embed=m)
                await client.add_reaction(message, '\u2705')
                await client.add_reaction(message, '\u274C')
                msg.description = ":speech_balloon: Suggestion sent!\nYou can see it in <#453192365096697897>."
    else:
        msg.description = "{} This command can only be used by members with 5+ levels.".format(error_e)
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member = None):
    punish = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    if user == None:
        msg.description = "{} Please tag the user you want to get information on.".format(error_e)
    else:
        imageurl = user.avatar_url
        msg.set_thumbnail(url=imageurl)
        m = ":page_with_curl: USER INFORMATION"
        m += "\n**NAME:** `{}`".format(user)
        m += "\n**ID:** `{}`".format(user.id)
        m += "\n**CREATED AT:** `{}`".format(user.created_at)
        m += "\n**JOINED AT:** `{}`".format(user.joined_at)
        m += "\n**STATUS:** `{}`".format(user.status)
        m += "\n**IS BOT:** `{}`".format(user.bot)
        m += "\n**GAME:** `{}`".format(user.game)
        m += "\n**NICKNAME:** `{}`".format(user.nick)
        m += "\n**TOP ROLE:** `{}`".format(user.top_role)
        m += "\n**VOICE CHANNEL:** `{}`".format(user.voice_channel)
        if punish in user.roles:
            m += "\n**PUNISHED:** `True`"
        else:
            m += "\n**PUNISHED:** `False`"
        msg.description = m
    await client.say(embed=msg)

# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    imageurl = ctx.message.server.icon_url
    msg.set_thumbnail(url=imageurl)
    m = ":page_with_curl: SERVER INFORMATION"
    m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
    m += "\n**CHANNELS:** `{}`".format(len(ctx.message.server.channels))
    m += "\n**EMOJIS:** `{}`".format(len(ctx.message.server.emojis))
    m += "\n**ID:** `{}`".format(ctx.message.server.id)
    m += "\n**REGION:** `{}`".format(ctx.message.server.region)
    m += "\n**ROLES:** `{}`".format(len(ctx.message.server.roles))
    m += "\n**OWNER:** `{}`".format(ctx.message.server.owner)
    m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
    m += "\n**RELEASE DATE:** `{}`".format(release_date)
    msg.description = m
    msg.set_image(url="{}".format(banner))
    await client.say(embed=msg)

# }apply
@client.command(pass_context=True)
async def apply(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    role3 = discord.utils.get(ctx.message.server.roles, id=lvl15_role)
    role4 = discord.utils.get(ctx.message.server.roles, id=lvl20_role)
    role5 = discord.utils.get(ctx.message.server.roles, id=lvl25_role)
    role6 = discord.utils.get(ctx.message.server.roles, id=lvl35_role)
    role7 = discord.utils.get(ctx.message.server.roles, id=lvl40_role)
    role8 = discord.utils.get(ctx.message.server.roles, id=lvl50_role)
    if role3 in author.roles or role4 in author.roles or role5 in author.roles or role6 in author.roles or role7 in author.roles or role8 in author.roles:
        try:
            mg = "***__STAFF APPLICATION TEMPLATE__***"
            mg += "\n:exclamation: Before applying make sure you are at least level 15 on the Mee6 leveling system."
            mg += "\n```md"
            mg += "\n# =================================== #"
            mg += "\n```"
            mg += "\n:grey_question: How to apply:"
            mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
            mg += "\n`-` When you finish answering the questions post the application in the <#457855606670229505> channel."
            mg += "\n```md"
            mg += "\n# =================================== #"
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
            mg += "\n`-` Why should we accept you?"
            await client.send_message(author, mg)
            msg.description = ":pencil: The `helper` template has been sent to your DMs!".format(error_e)
        except:
            msg.description = "{} I was unable to DM you, please try again once you allowed DMs from me.".format(erorr_e)
    else:
        msg.description = "{} This command can only be used by members with 15+ levels.".format(error_e)
    await client.say(embed=msg)
    
''' COMMANDS FOR VIPS '''
# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if args == None:
            msg.description = "{} Please give a message that you want the bot to say.".format(error_e)
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.description = "{} The message cannot be longer than 1990 characters.".format(error_e)
                await client.say(embed=msg)
            else:
                await client.say("`{}`".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.description = "{] This command can only be used by VIPs and Legends.".format(error_e)
        await client.say(embed=msg)

''' COMMANDS FOR STAFF '''
# }p <user>
@client.command(pass_context=True)
async def p(ctx, userName: discord.Member = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    partner = discord.utils.get(ctx.message.server.roles, id=partner_role)
    pmanager = discord.utils.get(ctx.message.server.roles, id=pmanager_role)
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles or pmanager in author.roles:
        if userName == None:
            msg.description = "{} Please mention the person you want to give/remove the partner role to/from.".format(error_e)
        else:
            try:
                a = []
                if partner in userName.roles:
                    await client.remove_roles(userName, partner)
                    msg.description = ":handshake: <@{}> removed the partner role from <@{}>.".format(author.id, userName.id)
                    a.append("+1")
                else:
                    await client.add_roles(userName, partner)
                    msg.description = ":handshake: <@{}> gave the partner role to <@{}>.".format(author.id, userName.id)
                m = "```diff"
                if len(a) == 0:
                    m += "\n- PARTNER (add) -"
                else:
                    m += "\n- PARTNER (remove) -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n```"
                await client.send_message(client.get_channel(logs), m)
            except:
                msg.description = "{} There was an error while trying to give/take the partner role to/from that user.".format(error_e)
    else:
        msg.description = "{} This command can only be used by the staff and partner managers!".format(error_e)
    await client.say(embed=msg)

''' COMMANDS FOR ADMINS '''
# }rawsay <text>
@client.command(pass_context=True)
async def rawsay(ctx, *, args = None):
    author = ctx.message.author
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    msg = discord.Embed(colour=0x210150, title= "")
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            msg.description = "{} No text given!".format(error_e)
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.description = "{} The text cannot be longer than 1990 characters.".format(error_e)
                await client.say(embed=msg)
            else:
                await client.say("{}".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.description = "{} This command can only be used by Administrators, Managers and Owners!".format(error_e)
        await client.say(embed=msg)

# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0x210150, title="")
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            msg.description = "{} Not all arguments were given.\nProper usage: `Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.".format(error_e)
            await client.say(embed=msg)
        else:
            a = str(args)
            if '|' in a:
                b = a.split('|')
                try:
                    color = discord.Color(random.randint(0x000000, 0xFFFFFF))
                    msg2 = discord.Embed(colour=color, description="{}".format(b[1]))
                    msg2.title = "{}".format(b[0])
                    msg2.set_footer(text=b[4])
                    msg2.add_field(name="{}".format(b[2]), value="{}".format(b[3]))
                    await client.say(embed=msg2)
                except:
                    msg.description = "The command was used incorrectly.\nProper usage: `Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.".format(error_e)
                    await client.say(embed=msg)
            else:
                msg.description = "The command was used incorrectly.\nProper usage: `Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.".format(error_e)
                await client.say(embed=msg)
    else:
        msg.description = "This command can only be used by Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=msg)

#######################
client.run(os.environ['BOT_TOKEN'])
