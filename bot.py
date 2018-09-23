import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[Realm X] - [X General]"

pm_role = '473812644021927946'
helper_role = '453195469309476877'
mod_role = '453195518785486858'
admin_role = '453195993987416064'
manager_role = '453196026547929088'
owner_role = '453194638077984768'
member_role = '453194601247801354'
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
partner_role = '453194705732239360'
muted_role = '453195421611982848'
x_role = '453196094332076045'
error_e = ":octagonal_sign:"
logs = '490437065930965003'

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    print("[+] Logged in!")
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    print("[+] Name: General")
    print("[+] ID: {}".format(client.user.id))
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel('453193096335720479'))
    t2 = time.perf_counter()
    print("[+] Ping: {}".format(round((t2-t1)*1000)))
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    await client.change_presence(game=discord.Game(name="with your privacy"))

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
    emojis = ["<a:bobo:474228327734050826>", "<a:ThumbsUpParrot:476294787285254144>", "<a:CatDance:476294788576968705>"]
    await client.send_message(client.get_channel("453192466716164137"), "{} {}".format(random.choice(emojis), m))
    server = userName.server
    user = server.get_member(userName.id)
    await client.send_message(client.get_channel("453192385795588096"), ":large_blue_circle: `{}` joined the server! Now we have {} members.\n__`Created at: {} | Joined at: {}`__".format(userName, len(server.members), userName.created_at, user.joined_at))
    try:
        await client.add_roles(server.get_member(userName.id), discord.utils.get(server.roles, id=member_role))
        #await client.send_message(userName, m2)
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    server = client.get_server('452865346081128448')
    await client.send_message(client.get_channel("453192385795588096"), ":red_circle: `{}` left the server! Now we have {} members.".format(userName, len(server.members)))



''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=0x2F007F, description = "You can see all commands in the <#453857880588943374> channel.")
    embed.set_footer(text=footer_text)
    await client.say(embed=embed)

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    options = ["g", "m", "w", "f"]
    if option == None:
        embed.description = "{} Please specify which bot's ping you want to see.\nOptions: `g`, `m`, `w`, `f`, `all`.".format(error_e)
        await client.say(embed=embed)
    elif option not in options:
        embed.description = "{} Invalid option.\nOptions: `g`, `m`, `w`, `f`, `all`.".format(error_e)
        await client.say(embed=embed)
    elif option == "all" or option == "g":
        t1 = time.perf_counter()
        await client.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        embed.description = "My ping is `{}`ms.".format(round((t2-t1)*1000))
        await client.say(embed=embed)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(colour=0x2F007F, description = "Here is the default invite link for the server: https://discord.gg/UBh9FpK")
    embed.set_footer(text=footer_text)
    await client.say(embed=embed)

# }userinfo [user]
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    punish = discord.utils.get(ctx.message.server.roles, id=muted_role)
    if user == None:
        author = ctx.message.author
    else:
        author = user
    embed.set_thumbnail(url=author.avatar_url)
    m = "USER INFORMATION"
    m += "\n**NAME:** `{}`".format(author)
    m += "\n**ID:** `{}`".format(author.id)
    m += "\n**CREATED AT:** `{}`".format(author.created_at)
    m += "\n**JOINED AT:** `{}`".format(author.joined_at)
    m += "\n**STATUS:** `{}`".format(author.status)
    m += "\n**IS BOT:** `{}`".format(author.bot)
    m += "\n**GAME:** `{}`".format(author.game)
    m += "\n**NICKNAME:** `{}`".format(author.nick)
    m += "\n**TOP ROLE:** `{}`".format(author.top_role)
    m += "\n**VOICE CHANNEL:** `{}`".format(author.voice_channel)
    if punish in author.roles:
        m += "\n**PUNISHED:** `True`"
    else:
        m += "\n**PUNISHED:** `False`"
    embed.description = m
    await client.say(embed=embed)

# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    m = "SERVER INFORMATION"
    m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
    m += "\n**CHANNELS:** `{}`".format(len(ctx.message.server.channels))
    m += "\n**EMOJIS:** `{}`".format(len(ctx.message.server.emojis))
    m += "\n**ID:** `{}`".format(ctx.message.server.id)
    m += "\n**REGION:** `{}`".format(ctx.message.server.region)
    m += "\n**ROLES:** `{}`".format(len(ctx.message.server.roles))
    m += "\n**OWNER:** `{}`".format(ctx.message.server.owner)
    m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
    m += "\n**RELEASE DATE:** `25th of June, 2018`"
    embed.description = m
    embed.set_image(url='https://i.imgur.com/rVvSG5L.png')
    await client.say(embed=embed)

# }apply
@client.command(pass_context=True)
async def apply(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
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
        await client.send_message(ctx.message.author, mg)
        embed.description = "The staff application information was sent to your DMS!"
        await client.say(embed=embed)
    except:
        embed.description = "{} Make sure I have permission to DM you.".format(error_e)
        await client.say(embed=embed)

# }nothing
@client.command(pass_context=True)
async def nothing(ctx):
    h = await client.say("` `")
    await client.delete_message(h)

''' COMMANDS FOR LEVEL 5+ '''

# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
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
            embed.description = "{} No suggestion given.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The suggestion text cannot be longer than 250 characters. Please make it simple and short.".format(error_e)
            await client.say(embed=embed)
        else:
            msg = discord.Embed(colour=0x2F007F)
            msg.set_footer(text=footer_text)
            msg.description = "{}\n**~~__= = = = = = = = = =__~~**\nSuggested by: `{} ### {}`\nIf you like this suggestion react with :white_check_mark: and if you don't like it react with :x:.".format(args, ctx.message.author, ctx.message.author.id)
            message = await client.send_message(client.get_channel('453192365096697897'), embed=msg)
            await client.add_reaction(message, '\u2705')
            await client.add_reaction(message, '\u274C')
            embed.description = "Suggestion sent! You can see it in the <#453192365096697897> channel."
            await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by members with 5+ levels.".format(error_e)
        await client.say(embed=embed)

# }lookup <id>
@client.command(pass_context=True)
async def lookup(ctx, ID = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    role = discord.utils.get(ctx.message.server.roles, id=lvl5_role)
    role2 = discord.utils.get(ctx.message.server.roles, id=lvl10_role)
    role3 = discord.utils.get(ctx.message.server.roles, id=lvl15_role)
    role4 = discord.utils.get(ctx.message.server.roles, id=lvl20_role)
    role5 = discord.utils.get(ctx.message.server.roles, id=lvl25_role)
    role6 = discord.utils.get(ctx.message.server.roles, id=lvl35_role)
    role7 = discord.utils.get(ctx.message.server.roles, id=lvl40_role)
    role8 = discord.utils.get(ctx.message.server.roles, id=lvl50_role)
    if role in author.roles or role2 in author.roles or role3 in author.roles or role4 in author.roles or role5 in author.roles or role6 in author.roles or role7 in author.roles or role8 in author.roles:
        if ID == None:
            embed.description = "{} Please give a user ID you want to look up.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                user = await client.get_user_info(ID)
                embed.set_thumbnail(url=user.avatar_url)
                m = "USER INFORMATION"
                m += "\n**NAME:** `{}`".format(user)
                m += "\n**ID:** `{}`".format(user.id)
                m += "\n**CREATED AT:** `{}`".format(user.created_at)
                m += "\n**IS BOT:** `{}`".format(user.bot)
                embed.description = m
                await client.say(embed=embed)
            except:
                embed.description = "{} User with that ID has not been found.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by members with 5+ levels.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR VIP '''

# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, id=vip_role)
    legend = discord.utils.get(ctx.message.server.roles, id=legend_role)
    if vip in author.roles or legend in author.roles:
        if args == None:
            embed.description = "{} Please give a message that you want me to say.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 1900:
            embed.description = "{} The message cannot be longer than 1900 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            await client.say("`{}`".format(args))
            await client.delete_message(ctx.message)
    else:
        embed.description = "{} This command can only be used by VIPs and Legends.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR PARTNER MANAGERS '''

# }p <user>
@client.command(pass_context=True)
async def p(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    partner = discord.utils.get(ctx.message.server.roles, id=partner_role)
    pmanager = discord.utils.get(ctx.message.server.roles, id=pm_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles or pmanager in author.roles:
        if user == None:
            embed.description = "{} No user was mentioned.".format(error_e)
            await client.say(embed=embed)
        elif user.bot:
            embed.description = "{} Bots can't be partners.".format(error_e)
            await client.say(embed=embed)
        elif partner in user.roles:
            await client.remove_roles(user, partner)
            embed.description = "<@{}> removed the partner role from <@{}>.".format(author.id, user.id)
            await client.say(embed=embed)
            m = "```diff"
            m += "\n- REMOVE PARTNER ROLE -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
        else:
            await client.add_roles(user, partner)
            embed.description = "<@{}> gave the partner role to <@{}>.".format(author.id, user.id)
            await client.say(embed=embed)
            m = "```diff"
            m += "\n- ADD PARTNER ROLE -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
    else:
        msg.description = "{} This command can only be used by Partner Managers and staff.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR MANAGERS '''

# }rawsay <text>
@client.command(pass_context=True)
async def rawsay(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    if owner in author.roles or manager in author.roles:
        if args == None:
            embed.description = "{} Please give a message that you want me to say.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 1900:
            embed.description = "{} The message cannot be longer than 1900 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            await client.say(args)
            await client.delete_message(ctx.message)
    else:
        embed.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            embed.description = "{} No arguments were given.\nProper usage: `title/none | description/none | name/none | value/none | footer/none`.".format(error_e)
            await client.say(embed=embed)
        elif ' | ' in str(args):
            a = args.split(' | ')
            try:
                color = discord.Color(random.randint(0x000000, 0xFFFFFF))
                msg = discord.Embed(colour=color)
                if a[0] == "none":
                    msg.title=""
                else:
                    msg.title=a[0]
                if a[1] == "none":
                    msg.description=""
                else:
                    msg.description=a[1]
                if a[4] == "none":
                    msg.set_footer(text="")
                else:
                    msg.set_footer(text=a[4])
                if a[2] != "none" or a[3] != "none":
                    msg.add_field(name=a[2], value=a[3])
                await client.say(embed=msg)
            except:
                embed.description = "{} There was an error while creating or sending the embed.".format(error_e)
                await client.say(embed=embed)
        else:
            embed.description = "{} The command was used incorrectly.\nProper usage: `title/none | description/none | name/none | value/none | footer/none`.".format(error_e)
            await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

#######################
client.run(os.environ['BOT_TOKEN'])
