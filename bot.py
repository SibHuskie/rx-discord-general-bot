print("Starting...")
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix = ["xg!", "}"]
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[Realm X] - [X General]"
limit = 100000000000000000
version = "2.0"

owners_role = "510748756858109953"
xbots_role = "510749122257485835"
staff_role = "510748890883031050"
support_role = "510749024114966528"
members_role = "510749251777855488"
announcement_role = "510752070522109952"
partners_role = "510787027051085834"
muted_role = "510753281945894923"
splitter = "**~~`====================`~~**"

loading_e = "<a:loading:484705261609811979>"
error_e = "<:error:506846074917486592>"
joined_e = "<:joined:506846074657439776>"
left_e = "<:left:506846074712096828>"
serverinfo_e = "<:serverinfo:506846075102035968>"
userinfo_e = "<:userinfo:506846074992984075>"
avatar_e = "<:avatar:506846074464501771>"
suggestion_e = "<:suggestion:506846075504689152>"
upvote_e = "<:upvote:506846074699513885>"
downvote_e = "<:downvote:506846074867286019>"
lookup_e = "<:lookup:506846075177533450>"
partner_e = "<:partner:506846074829537301>"
log_e = "<:log:506846075148304399>"
roleme_e = "<:roleme:506846075886370826>"
pinggood_e = "<:pinggood:506846075219476481>"
pingok_e = "<:pingok:506846075227996160>"
pingbad_e = "<:pingbad:506846075076739072>"
rep_e = "<:rep:510795018785783819>"
reload_e = "<:reload:510803370001432578>"
apply_e = "<:apply:510813958756892682>"

reps_chnl = "510801918449287178"
log_chnl = "510765922152218637"
reputations = []
reped = []

''''''

# START UP SYSTEM
started = []
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(reps_chnl), limit=limit):
        reputations.append(i.content)
    print("[START UP] Loaded reputations.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="}help | }invite"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel('510765922152218637'))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    m += "\n{} Reputations: `{}`".format(rep_e, len(reputations))
    await client.send_message(client.get_channel(log_chnl), m)

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    embed.set_image(url='https://i.imgur.com/QyY8owZ.png')
    emojis = ["<a:bobo:474228327734050826>", "<a:ThumbsUpParrot:476294787285254144>", "<a:CatDance:476294788576968705>"]
    m = "Welcome to **Realm ✘**, <@{}>! We hope you enjoy your stay.".format(userName.id)
    m2 = "**~~`= = = = = = = = = ✘ = = = = = = = = =`~~**"
    m2 += "\n{} Welcome to **Realm ✘**, <@{}>! We hope you enjoy your stay here.".format(random.choice(emojis), userName.id)
    m2 += "\n:clipboard: All the information are in the <#510747462445826056> channel, but feel free to ask the staff about anything."
    m2 += "\n**~~`= = = = = = = = = ✘ = = = = = = = = =`~~**"
    m2 += "\n:handshake:  If you want to partner please DM a staff member."
    m2 += "\n**~~`= = = = = = = = = ✘ = = = = = = = = =`~~**"
    m2 += "\n:white_check_mark: Thank you for joining!"
    m2 += "\n**~~`= = = = = = = = = ✘ = = = = = = = = =`~~**"
    m2 += "\n:shield: *__Hey, you should also check out our cool public bots.__*"
    m2 += "\n:link: *__Just use `}invite` to get the invite links.__*"
    m2 += "\n**~~`= = = = = = = = = ✘ = = = = = = = = =`~~**"
    embed.description = m2
    await client.send_message(client.get_channel("510747587071180801"), "{} {}".format(random.choice(emojis), m))
    server = userName.server
    await client.send_message(client.get_channel("510747536823418880"), "{} `{}` joined the server! We now have **{}** members.".format(joined_e, userName, len(server.members)))
    try:
        await client.add_roles(server.get_member(userName.id), discord.utils.get(server.roles, id=members_role))
        await asyncio.sleep(1.25)
        await client.add_roles(server.get_member(userName.id), discord.utils.get(server.roles, id=announcement_role))
        await client.send_message(userName, embed=embed)
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    server = client.get_server('452865346081128448')
    await client.send_message(client.get_channel("510747536823418880"), "{} `{}` left the server! We now have **{}** members.".format(left_e, userName, len(server.members)))



''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        embed.description = "Use `xg!help` to see a list of general/utility commands.\nUse `xm!help` to see a list of moderation commands.\nUse `xf!help` to see a list of fun commands.\nUse `xp!help` to see a list of protection commands.\nUse `xw!help` to see a list of wars commands."
        await client.say(embed=embed)

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        options = ["g", "m", "w", "f", "p", "all"]
        if '}' in ctx.message.content:
            if option == None:
                embed.description = "{} Please specify which bot's ping you want to see.\nOptions: `g`, `m`, `w`, `f`, `p`, `all`.".format(error_e)
                await client.say(embed=embed)
            elif option not in options:
                embed.description = "{} Invalid option.\nOptions: `g`, `m`, `w`, `f`, `p`, `all`.".format(error_e)
                await client.say(embed=embed)
            elif option == "all" or option == "g":
                t1 = time.perf_counter()
                await client.send_typing(ctx.message.channel)
                t2 = time.perf_counter()
                ping = round((t2-t1)*1000)
                if ping > 300:
                    m = "{} The bot is lagging.".format(pingbad_e)
                elif ping > 200:
                    m = "{} The bot might be lagging.".format(pingok_e)
                else:
                    m = "{} The bot isn't lagging.".format(pinggood_e)
                embed.description = "My ping is `{}`ms.\n{}".format(ping, m)
                await client.say(embed=embed)
        else:
            embed.description = "My ping is `{}`ms.\n{}".format(ping, m)
            await client.say(embed=embed)

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        embed.description = "Here is the default link for the server: https://discord.gg/yr7WHYB\n\n[Click here](https://discordapp.com/oauth2/authorize?client_id=453210408384462848&scope=bot&permissions=8) to invite **✘ Fun**.\n[Click here](https://discordapp.com/oauth2/authorize?client_id=499840342464397312&scope=bot&permissions=8) to invite **✘ Protect**."
        await client.say(embed=embed)

# }staff
@client.command(pass_context=True)
async def staff(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        support = discord.utils.get(ctx.message.server.roles, id=support_role)
        embed.description = "Loading staff list... {}".format(loading_e)
        k = await client.say(embed=embed)
        try:
            o = "<@&{}> (? Reps)".format(owner.id)
            s = "<@&{}> (30 Reps)".format(staff.id)
            xp = "<@&510752051400278028> (50 Reps)"
            xf = "<@&510752018982371338> (50 Reps)"
            su = "<@&{}> (15 Reps)".format(support.id)
            for i in ctx.message.server.members:
                if owner in i.roles:
                    o += "\n{}".format(i.name)
                elif staff in i.roles:
                    s += "\n{}".format(i.name)
                elif support in i.roles:
                    su += "\n{}".format(i.name)
            embed.description = "**__STAFF LIST:__**\n{}\n\n{}\n\n{}\n\n{}\n\n{}".format(o, s, xp, xf, su)
            await client.edit_message(k, embed=embed)
        except:
            embed.description = "{} There was an error while loading the staff list. Please try again.".format(error_e)
            await client.edit_message(k, embed=embed)

# }userinfo [user]
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        punish = discord.utils.get(ctx.message.server.roles, id=muted_role)
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed.set_thumbnail(url=author.avatar_url)
        m = "{} USER INFORMATION".format(userinfo_e)
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
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        m = "{} SERVER INFORMATION".format(serverinfo_e)
        m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
        m += "\n**CHANNELS:** `{}`".format(len(ctx.message.server.channels))
        m += "\n**EMOJIS:** `{}`".format(len(ctx.message.server.emojis))
        m += "\n**ID:** `{}`".format(ctx.message.server.id)
        m += "\n**REGION:** `{}`".format(ctx.message.server.region)
        m += "\n**ROLES:** `{}`".format(len(ctx.message.server.roles))
        m += "\n**OWNER:** `{}`".format(ctx.message.server.owner)
        m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
        m += "\n**RELEASE DATE:** `25th of June, 2018`"
        m += "\n**REBIRTH DATE:** `10th of November, 2018`"
        embed.description = m
        embed.set_image(url='https://image.ibb.co/hzfvqq/banner.png')
        await client.say(embed=embed)

# }avatar [user]
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed = discord.Embed(colour=0x2F007F)
        embed.set_footer(text=footer_text)
        embed.description = "{} Here is **{}**'s avatar:".format(avatar_e, author.name)
        embed.set_image(url=author.avatar_url)
        await client.say(embed=embed)

# }nothing
@client.command(pass_context=True)
async def nothing(ctx):
    await client.send_typing(ctx.message.channel)

# }roleme <role>
@client.command(pass_context=True)
async def roleme(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        if args == None:
            embed.description = "{} No role given.\nSelf roles: `Announcement Notify`, `XP Notify`, `XF Notify`.".format(error_e)
            await client.say(embed=embed)
        else:
            roles = ['510751732767129620', '510751970345222146', '510752070522109952']
            a = []
            for i in ctx.message.server.roles:
                if args.lower() in str(i.name.lower()) and i.id in roles:
                    if i in author.roles:
                        await client.remove_roles(author, i)
                        embed.description = "{} Removed the `{}` role from **{}**.".format(roleme_e, i.name, author.name)
                        await client.say(embed=embed)
                        a.append("+1")
                        break
                    else:
                        await client.add_roles(author, i)
                        embed.description = "{} Given the `{}` role to **{}**.".format(roleme_e, i.name, author.name)
                        await client.say(embed=embed)
                        a.append("+1")
                        break
            if len(a) == 0:
                embed.description = "{} Role not found in the self-roles list.\nSelf roles: `Announcement Notify`, `XP Notify`, `XF Notify`.".format(error_e)
                await client.say(embed=embed)

# }rep <user>
@client.command(pass_context=True)
async def rep(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if ctx.message.author.id in reped:
            embed.description = "{} You've already given a reputation point today.".format(error_e)
            await client.say(embed=embed)
        elif user == None:
            embed.description = "{} No user mentioned.".format(error_e)
            await client.say(embed=embed)
        elif user.bot:
            embed.description = "{} You cannot give reputation points to bots.".format(error_e)
            await client.say(embed=embed)
        elif user.id == ctx.message.author.id:
            embed.description = "{} You cannot give reputation points to yourself.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "{} **{}** has given a reputation point to **{}**.".format(rep_e, ctx.message.author.name, user.name)
            await client.say(embed=embed)
            reped.append(ctx.message.author.id)
            reputations.append(user.id)
            await client.send_message(client.get_channel(reps_chnl), user.id)

# }reps [user]
@client.command(pass_context=True)
async def reps(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed.description = "{} **{}** has `{}` reputation points.".format(rep_e, author.name, reputations.count(author.id))
        await client.say(embed=embed)

# }apply <support/staff/bot>
@client.command(pass_context=True)
async def apply(ctx, option = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        options = ["support", "staff", "bot"]
        if option == None:
            embed.description = "{} No option given.\nChoose:\n`support` to apply for a support team member.\n`staff` to apply for a server staff member.\n`bot` to apply for bot staff member.".format(error_e)
            await client.say(embed=embed)
        elif option.lower() not in options:
            embed.description = "{} Invalid option.\nChoose:\n`support` to apply for a support team member.\n`staff` to apply for a server staff member.\n`bot` to apply for bot staff member.".format(error_e)
            await client.say(embed=embed)
        else:
            if reputations.count(ctx.message.author.id) >= 15 and option == "support":
                embed.description = "{} **{}** sent an application for `Support Team Member`.\n{} They currently have `{}` reputation points.".format(apply_e, ctx.message.author.name, rep_e, reputations.count(ctx.message.author.id))
                await client.send_message(client.get_channel('510782409374040086'), embed=embed)
                embed.description = "{} Application sent!".format(apply_e)
                await client.say(embed=embed)
            elif reputations.count(ctx.message.author.id) >= 30 and option == "staff":
                embed.description = "{} **{}** sent an application for `Server Staff Member`.\n{} They currently have `{}` reputation points.".format(apply_e, ctx.message.author.name, rep_e, reputations.count(ctx.message.author.id))
                await client.send_message(client.get_channel('510782409374040086'), embed=embed)
                embed.description = "{} Application sent!".format(apply_e)
                await client.say(embed=embed)
            elif reputations.count(ctx.message.author.id) >= 50 and option == "bot":
                embed.description = "{} **{}** sent an application for `Bot Staff Member`.\n{} They currently have `{}` reputation points.".format(apply_e, ctx.message.author.name, rep_e, reputations.count(ctx.message.author.id))
                await client.send_message(client.get_channel('510782409374040086'), embed=embed)
                embed.description = "{} Application sent!".format(apply_e)
                await client.say(embed=embed)
            else:
                embed.description = "{} You do not have enough reputation points to apply for that role.\nUse `xg!staff` to see how many reputation points you need.".format(error_e)
                await client.say(embed=embed)
                
# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if args == None:
            embed.description = "{} No suggestion given.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The suggestion text cannot be longer than 250 characters. Please make it simple and short.".format(error_e)
            await client.say(embed=embed)
        else:
            msg = discord.Embed(colour=0x2F007F)
            msg.set_footer(text=footer_text)
            msg.description = "{} {}\n**~~= = = = = = = = = = = = = = = = = = = =~~**\nSuggested by: `{} ### {}`\nIf you like this suggestion react with <:upvote:506846074699513885> and if you don't like it react with <:downvote:506846074867286019>.".format(suggestion_e, args, ctx.message.author, ctx.message.author.id)
            message = await client.send_message(client.get_channel('510747496008646667'), embed=msg)
            await client.add_reaction(message, ':downvote:506846074867286019')
            await client.add_reaction(message, ':upvote:506846074699513885')
            embed.description = "{} Suggestion sent! You can see it in the <#510747496008646667> channel.".format(suggestion_e)
            await client.say(embed=embed)

# }lookup <id>
@client.command(pass_context=True)
async def lookup(ctx, ID = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if ID == None:
            embed.description = "{} Please give a user ID you want to look up.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                user = await client.get_user_info(ID)
                embed.set_thumbnail(url=user.avatar_url)
                m = "{} USER INFORMATION".format(lookup_e)
                m += "\n**NAME:** `{}`".format(user)
                m += "\n**ID:** `{}`".format(user.id)
                m += "\n**CREATED AT:** `{}`".format(user.created_at)
                m += "\n**IS BOT:** `{}`".format(user.bot)
                embed.description = m
                await client.say(embed=embed)
            except:
                embed.description = "{} User with that ID has not been found.".format(error_e)
                await client.say(embed=embed)

# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if args == None:
            embed.description = "{} Please give a message that you want me to say.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 1900:
            embed.description = "{} The message cannot be longer than 1900 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            await client.say("`{}`".format(args))
            await client.delete_message(ctx.message)

''' COMMANDS FOR STAFF '''

# }p <user>
@client.command(pass_context=True)
async def p(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        partner = discord.utils.get(ctx.message.server.roles, id=partners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if owner in author.roles or staff in author.roles:
            if user == None:
                embed.description = "{} No user was mentioned.".format(error_e)
                await client.say(embed=embed)
            elif user.bot:
                embed.description = "{} Bots can't be partners.".format(error_e)
                await client.say(embed=embed)
            elif partner in user.roles:
                await client.remove_roles(user, partner)
                embed.description = "{} **{}** removed the partner role from **{}**.".format(partner_e, author.name, user.name)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__Removed Partner Role__** {}".format(log_e, partner_e)
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                await client.send_message(client.get_channel(log_chnl), m)
            else:
                await client.add_roles(user, partner)
                embed.description = "{} **{}** gave the partner role to **{}**.".format(partner_e, author.name, user.name)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__Added Partner Role__** {}".format(log_e, partner_e)
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                await client.send_message(client.get_channel(log_chnl), m)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR OWNERS '''

# }rawsay <text>
@client.command(pass_context=True)
async def rawsay(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        if owner in author.roles:
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
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        if owner in author.roles:
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
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

#######################
client.run(os.environ['BOT_TOKEN'])
