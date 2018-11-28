print("Starting X General...")
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
version = "3.0"
splitter = "**~~`====================`~~**"


owner_roles = []
manager_roles = []
admin_roles = []
mod_roles = []
helper_roles = []
partner_manager_roles = []
partner_roles = []
muted_roles = []
member_roles = []
self_roles = []
logs = []
joins_leaves = []

owner_roles_chnl = '516605295816867871'
manager_roles_chnl = '516606147558506507'
admin_roles_chnl = '516605310203592704'
mod_roles_chnl = '516605319665680405'
helper_roles_chnl = '516605337248464906'
partner_manager_roles_chnl = '516606847323734064'
partner_roles_chnl = '516606872896405520'
muted_roles_chnl = '516607156813037608'
member_roles_chnl = '516607267127164942'
self_roles_chnl = '516611549427793930'
logs_chnl = '516614512657563658'
log_chnl = '516594957432389632'
joins_leaves_chnl = '516616002012839936'

loading_e = "<a:loading:484705261609811979>"
error_e = "<:error:516609910356574212>"
joined_e = "<:joined:516609910318956552>"
left_e = "<:left:516609910318956553>"
serverinfo_e = "<:serverinfo:516609910088400922>"
userinfo_e = "<:userinfo:516609910465757184>"
avatar_e = "<:avatar:516609910008578049>"
suggestion_e = "<:suggestion:516609910088138772>"
upvote_e = "<:upvote:516609910235201536>"
downvote_e = "<:downvote:516609910214230016>"
lookup_e = "<:lookup:516609910553837578>"
partner_e = "<:partner:516609910390390815>"
log_e = "<:log:516609910415425536>"
roleme_e = "<:roleme:516609911006691338>"
pinggood_e = "<:pinggood:516609909819965441>"
pingok_e = "<:pingok:516609909832417296>"
pingbad_e = "<:pingbad:516609910168092682>"
reload_e = "<:reload:516609910235070472>"
worked_e = "<:worked:516609910310699042>"
roles_e = "<:roles:516614182045614080>"

help1 = "```diff"
help1 += "\n--- COMMANDS FOR EVERYONE ---"
help1 += "\nxg!help"
help1 += "\n-    Gives information about command lists."
help1 += "\nxg!ping"
help1 += "\n-    Pings the bot. Used to check if the bot is lagging."
help1 += "\nxg!invite"
help1 += "\n-    Gives invite links for the X bots and the official invite link for the server."
help1 += "\nxg!staff"
help1 += "\n-    Gives a list of staff."
help1 += "\nxg!userinfo [user]"
help1 += "\n-    Gives information about you or the mentioned user."
help1 += "\nxg!serverinfo"
help1 += "\n-    Gives information about the server."
help1 += "\nxg!avatar [user]"
help1 += "\n-    Shows a bigger version of your or the mentioned user's avatar."
help1 += "\nxg!nothing"
help1 += "\n-    Does nothing. Very essential for discord bots."
help1 += "\nxg!roleme <role name>"
help1 += "\n-    Used to self assign roles."
help1 += "\nxg!suggest <text>"
help1 += "\n-    Sends a suggestion."
help1 += "\nxg!lookup <user ID>"
help1 += "\n-    Gives information for any discord user, even if they aren't in the server."
help1 += "\nxg!say <text>"
help1 += "\n-    Forces the bot to say something. Does not support formatting."
help1 += "\nxg!tos"
help1 += "\n-    Gives you information about rules and TOS."
help1 += "\n```"

help2 = "```diff"
help2 += "\n--- COMMANDS FOR PARTNER MANAGERS ---"
help2 += "\nxg!p <user>"
help2 += "\n-    Gives or removes the partner role for the mentioned user."
help2 += "\n"
help2 += "\n--- COMMANDS FOR MANAGERS ---"
help2 += "\nxg!rawsay <text>"
help2 += "\n-    Forces the bot to say something. Supports formatting."
help2 += "\nxg!embed <title> | <description> | <field name> | <field value> | <footer>"
help2 += "\n-    Creates embeds."
help2 += "\n"
help2 += "\n--- COMMANDS FOR OWNERS ---"
help2 += "\nxg!setrole <option> <role name>"
help2 += "\n-    Used to manage roles in the bot's database."
help2 += "\nxg!selfroles <role name>"
help2 += "\n-    Used to manage self-roles."
help2 += "\nxg!log <channel name>"
help2 += "\n-    Sets the logs channel."
help2 += "\n```"

''''''

# START UP SYSTEM
started = []
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(owner_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        owner_roles.append(role)
    print("[START UP] Loaded owner roles.")
    async for i in client.logs_from(client.get_channel(manager_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        manager_roles.append(role)
    print("[START UP] Loaded manager roles.")
    async for i in client.logs_from(client.get_channel(admin_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        admin_roles.append(role)
    print("[START UP] Loaded administrator roles.")
    async for i in client.logs_from(client.get_channel(mod_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        mod_roles.append(role)
    print("[START UP] Loaded moderator roles.")
    async for i in client.logs_from(client.get_channel(helper_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        helper_roles.append(role)
    print("[START UP] Loaded helper roles.")
    async for i in client.logs_from(client.get_channel(partner_manager_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        partner_manager_roles.append(role)
    print("[START UP] Loaded partner manager roles.")
    async for i in client.logs_from(client.get_channel(partner_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        partner_roles.append(role)
    print("[START UP] Loaded partner roles.")
    async for i in client.logs_from(client.get_channel(member_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        member_roles.append(role)
    print("[START UP] Loaded member roles.")
    async for i in client.logs_from(client.get_channel(self_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        self_roles.append(role)
    print("[START UP] Loaded self roles.")
    async for i in client.logs_from(client.get_channel(muted_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        muted_roles.append(role)
    print("[START UP] Loaded muted roles.")
    async for i in client.logs_from(client.get_channel(logs_chnl), limit=limit):
        logs.append(i.content)
    print("[START UP] Loaded logs channels.")
    async for i in client.logs_from(client.get_channel(joins_leaves_chnl), limit=limit):
        joins_leaves.append(i.content)
    print("[START UP] Loaded join-leave channels.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="}help | }invite"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel(log_chnl))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    await client.send_message(client.get_channel(log_chnl), m)

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(user: discord.User):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if user.server.id == '452865346081128448':
        link = "[You can also click here to join the X bots' support server.](https://discord.gg/geVrByH)"
    elif user.server.id == '516573414664962050':
        link = "[You can also click here to join the community server.](https://discord.gg/yr7WHYB)"
    embed.description = "Welcome to **{}**, <@{}>! We hope you enjoy your stay.\nYou can use `xg!invite` to check out our public bots.\n\n{}".format(user.server.name, user.id, link)
    if user.server.id == '452865346081128448':
        await client.send_message(client.get_channel("510747587071180801"), ":wave: Welcome to **{}**, <@{}>! We hope you enjoy your stay.".format(user.server.name, user.id))
    elif user.server.id == '516573414664962050':
        await client.send_message(client.get_channel("516575864884953129"), ":wave: Welcome to **{}**, <@{}>! We hope you enjoy your stay.".format(user.server.name, user.id))
    for i in joins_leaves:
        a = i.split(' | ')
        if a[0] == user.server.id:
            await client.send_message(client.get_channel(a[1]), "{} `{}` joined the server! We now have **{}** members.".format(joined_e, user, len(user.server.members)))
            break
    for i in member_roles:
        if i in user.server.roles:
            try:
                server = user.server
                await client.add_roles(server.get_member(user.id), i)
                await asyncio.sleep(1.25)
                await client.send_message(user, embed=embed)
            except:
                print("[JOIN EVENT] Error.")

@client.async_event
async def on_member_remove(user: discord.User):
    for i in joins_leaves:
        a = i.split(' | ')
        if a[0] == user.server.id:
            await client.send_message(client.get_channel(a[1]), "{} `{}` left the server! We now have **{}** members.".format(left_e, user, len(user.server.members)))
            break

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
        if 'xg!' not in str(ctx.message.content):
            embed.description = "Use `xg!help` to see a list of general/utility commands.\nUse `xm!help` to see a list of moderation commands.\nUse `xf!help` to see a list of fun commands.\nUse `xp!help` to see a list of protection commands.\nUse `xw!help` to see a list of wars commands."
            await client.say(embed=embed)
        else:
            try:
                await client.send_message(ctx.message.author, help1)
                await client.send_message(ctx.message.author, help2)
                embed.description = "{} A list of commands has been sent to your DMs.".format(worked_e)
                await client.say(embed=embed)
            except:
                embed.description = "{} I was unable to DM you my list of commands.".format(error_e)
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
        options = ["g", "m", "s", "f", "p", "all"]
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
                p = round((t2-t1)*1000)
                if p > 300:
                    m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
                elif p > 200:
                    m = "{} The bot might be lagging.".format(pingok_e)
                else:
                    m = "{} The bot isn't lagging.".format(pinggood_e)
                embed.description = "My ping is `{}`ms.\n{}".format(p, m)
                await client.say(embed=embed)
        else:
            t1 = time.perf_counter()
            await client.send_typing(ctx.message.channel)
            t2 = time.perf_counter()
            p = round((t2-t1)*1000)
            if p > 300:
                m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
            elif p > 200:
                m = "{} The bot might be lagging.".format(pingok_e)
            else:
                m = "{} The bot isn't lagging.".format(pinggood_e)
            embed.description = "My ping is `{}`ms.\n{}".format(p, m)
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
        embed.description = "Community server: https://discord.gg/yr7WHYB\n\nSupport server: https://discord.gg/geVrByH\n\n[Click here](https://discordapp.com/oauth2/authorize?client_id=453210408384462848&scope=bot&permissions=8) to invite **✘ Fun**.\n[Click here](https://discordapp.com/oauth2/authorize?client_id=499840342464397312&scope=bot&permissions=8) to invite **✘ Protect**."
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
        embed.description = "{} Loading staff list... {}".format(roles_e, loading_e)
        k = await client.say(embed=embed)
        
        try:
            roles = {"owners" : owner_roles,
                     "managers" : manager_roles,
                     "admins" : admin_roles,
                     "mods" : mod_roles,
                     "helpers" : helper_roles,
                     "pms" : partner_manager_roles}
            owners = ""
            managers = ""
            admins = ""
            mods = ""
            helpers = ""
            pms = ""
            roles_l = {"owners" : owners,
                       "managers" : managers,
                       "admins" : admins,
                       "mods" : mods,
                       "helpers" : helpers,
                       "pms" : pms}
            for i in roles:
                for u in roles[i]:
                    if u in ctx.message.server.roles:
                        for o in ctx.message.server.members:
                            if u in o.roles:
                                roles_l[i] += "\n`{}`".format(o.name)
                        embed.add_field(name="{}".format(u.name), value=roles_l[i], inline=True)
            embed.description = "{} **__STAFF LIST:__**".format(roles_e)
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
        a = []
        for i in muted_roles:
            if i in ctx.message.server.roles:
                a.append(i)
                break
        if user == None:
            author = ctx.message.author
        else:
            author = user
        embed.set_thumbnail(url=author.avatar_url)
        m = "{} **__USER INFORMATION:__**".format(userinfo_e)
        m += "\n"
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
        if len(a) != 0:
            if a[0] in author.roles:
                m += "\n**MUTED:** `True`"
            else:
                m += "\n**MUTED:** `False`"
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
        m = "{} **__SERVER INFORMATION:__**".format(serverinfo_e)
        m += "\n"
        m += "\n**MEMBERS:** `{}`".format(len(ctx.message.server.members))
        m += "\n**CHANNELS:** `{}`".format(len(ctx.message.server.channels))
        m += "\n**EMOJIS:** `{}`".format(len(ctx.message.server.emojis))
        m += "\n**ID:** `{}`".format(ctx.message.server.id)
        m += "\n**REGION:** `{}`".format(ctx.message.server.region)
        m += "\n**ROLES:** `{}`".format(len(ctx.message.server.roles))
        m += "\n**CREATED BY:** `{}`".format(ctx.message.server.owner)
        m += "\n**CREATED AT:** `{}`".format(ctx.message.server.created_at)
        embed.description = m
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
        m = ""
        for i in self_roles:
            if i in ctx.message.server.roles:
                m += "\n`{}`".format(i.name)
        if args == None:
            embed.description = "{} No role given.\nSelf roles:\n{}".format(error_e, m)
            await client.say(embed=embed)
        else:
            a = []
            for i in ctx.message.server.roles:
                if args.lower() in str(i.name.lower()) and i in self_roles:
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
                embed.description = "{} Role not found in the self-roles list.\nSelf roles:\n{}".format(error_e, m)
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
            msg.description = "{} {}\n**~~= = = = = = = = = = = = = = = = = = = =~~**\nSuggested by: `{} ### {}`\nIf you like this suggestion react with <:upvote:516609910235201536> and if you don't like it react with <:downvote:516609910214230016>.".format(suggestion_e, args, ctx.message.author, ctx.message.author.id)
            if ctx.message.server.id == '516573414664962050':
                message = await client.send_message(client.get_channel('516575777974648835'), embed=msg)
                embed.description = "{} Suggestion sent! You can see it in the <#516575777974648835> channel.".format(suggestion_e)
            elif ctx.message.server.id == '452865346081128448':
                message = await client.send_message(client.get_channel('510747496008646667'), embed=msg)
                embed.description = "{} Suggestion sent! You can see it in the <#510747496008646667> channel.".format(suggestion_e)
            await client.add_reaction(message, ':downvote:516609910214230016')
            await client.add_reaction(message, ':upvote:516609910235201536')
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
                m = "{} **__USER INFORMATION:__**".format(lookup_e)
                m += "\n"
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

# }tos
@client.command(pass_context=True)
async def tos(ctx):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        embed.description = "Use `xp!tos` to see X protect's rules and TOS.\nUse `xf!tos` to see X fun's rules and TOS.\n\nThe other X bots don't have rules and TOS because they are not public yet."
        await client.say(embed=embed)

''' COMMANDS FOR PARTNER MANAGERS '''

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
        partner = []
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles, partner_manager_roles]
        for i in partner_roles:
            if i in ctx.message.server.roles:
                partner.append(i)
                break
        if len(partner) != 0:
            a = []
            for i in roles:
                for u in i:
                    if u in ctx.message.server.roles and u in ctx.message.author.roles:
                        if user == None:
                            embed.description = "{} No user was mentioned.".format(error_e)
                            await client.say(embed=embed)
                        elif user.bot:
                            embed.description = "{} Bots can't be partners.".format(error_e)
                            await client.say(embed=embed)
                        elif partner[0] in user.roles:
                            await client.remove_roles(user, partner[0])
                            embed.description = "{} **{}** removed the partner role from **{}**.".format(partner_e, author.name, user.name)
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Removed Partner Role__** {}".format(log_e, partner_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                        else:
                            await client.add_roles(user, partner[0])
                            embed.description = "{} **{}** gave the partner role to **{}**.".format(partner_e, author.name, user.name)
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Added Partner Role__** {}".format(log_e, partner_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                        a.append("+1")
                        break
            if len(a) == 0:
                embed.description = "{} This command can only be used by partner managers and staff.".format(error_e)
                await client.say(embed=embed)
        else:
            embed.description = "{} No partner role found in the database.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR MANAGERS '''

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
        roles = [owner_roles, manager_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if args == None:
                        embed.description = "{} Please give a message that you want me to say.".format(error_e)
                        await client.say(embed=embed)
                    elif len(str(args)) > 1900:
                        embed.description = "{} The message cannot be longer than 1900 characters.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        await client.say(args)
                        await client.delete_message(ctx.message)
                    a.append("+1")
                    break
        if len(a) == 0:
            embed.description = "{} This command can only be used by managers and owners.".format(error_e)
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
        roles = [owner_roles, manager_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by managers and owners.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR OWNERS '''
# }setrole <option> <role name>
@client.command(pass_context=True)
async def setrole(ctx, option = None, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                options = ["owner", "manager", "admin", "mod", "helper", "partner-manager", "partner", "muted", "member"]
                if option == None or args == None:
                    embed.description = "{} Not all arguments were given.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `partner-manager`, `partner`, `muted`, `member`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                elif option.lower() not in options:
                    embed.description = "{} Invalid option.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `partner-manager`, `partner`, `muted`, `member`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                else:
                    t = {"owner" : owner_roles_chnl,
                         "manger" : manager_roles_chnl,
                         "admin" : admin_roles_chnl,
                         "mod" : mod_roles_chnl,
                         "helper" : helper_roles_chnl,
                         "partner-manager" : partner_manager_roles_chnl,
                         "partner" : partner_roles_chnl,
                         "muted" : muted_roles_chnl,
                         "member" : member_roles_chnl}
                    k = {"owner" : owner_roles,
                         "manger" : manager_roles,
                         "admin" : admin_roles,
                         "mod" : mod_roles,
                         "helper" : helper_roles,
                         "partner-manager" : partner_manager_roles,
                         "partner" : partner_roles,
                         "muted" : muted_roles,
                         "member" : member_roles}
                    embed.description = "{} Editing roles database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    r = []
                    for u in ctx.message.server.roles:
                        if ' | ' in args:
                            y = args.split(' | ')
                            args = y[0]
                            r.append(y[1])
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            if " | none" in r:
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id and b[1] == u.id:
                                        await client.delete_message(o)
                                        k[option].remove(u)
                                        break
                                embed.description = "{} **{}** removed `{}` from the `{}` roles database.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Removed role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Role type:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                break
                            elif option.lower() != "member":
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        k[option].remove(discord.utils.get(ctx.message.server.roles, id=b[1]))
                                        await client.delete_message(o)
                                        break
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                break
                            else:
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`/`auto role`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}/auto role".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                break
                    if len(p) == 0:
                        embed.description = "{} Role not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

# }selfroles <role name>
@client.command(pass_context=True)
async def selfroles(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                if args == None:
                    embed.description = "{} No role name given.".format(error_e)
                    await client.say(embed=embed)
                else:
                    embed.description = "{} Editing self roles database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    for u in ctx.message.server.roles:
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            if u in self_roles:
                                async for i in client.logs_from(client.get_channel(self_roles_chnl), limit=limit):
                                    if i.content == "{} | {}".format(ctx.message.server.id, u.id):
                                        await client.delete_message(i)
                                        self_roles.remove(u)
                                        break
                                embed.description = "{} **{}** removed `{}` from the self roles list.".format(roles_e, author.name, u.name)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Self Roles__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Removed role:` {} ### {}".format(u.name, u.id)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                break
                            else:
                                await client.send_message(client.get_channel(self_roles_chnl), "{} | {}".format(ctx.message.server.id, u.id))
                                self_roles.append(u)
                                embed.description = "{} **{}** added `{}` to the self roles list.".format(roles_e, author.name, u.name)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Self Roles__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Added role:` {} ### {}".format(u.name, u.id)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                break
                    if len(p) == 0:
                        embed.description = "{} Role not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

# }log <channel name>
@client.command(pass_context=True)
async def log(ctx, *, args = None):
    embed = discord.Embed(colour=0x2F007F)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                if args == None:
                    embed.description = "{} No channel name given.".format(error_e)
                    await client.say(embed=embed)
                else:
                    embed.description = "{} Editing log channels database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    for u in ctx.message.server.channels:
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            try:
                                k = await client.send_message(u, "test log message")
                                async for i in client.logs_from(client.get_channel(logs_chnl), limit=limit):
                                    b = i.content.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        logs.remove(i.content)
                                        await client.delete_message(i)
                                        break
                                await client.send_message(client.get_channel(logs_chnl), "{} | {}".format(ctx.message.server.id, u.id))
                                logs.append("{} | {}".format(ctx.message.server.id, u.id))
                                embed.description = "{} **{}** set `{}` as the new logs channel.".format(log_e, author.name, u.name)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Log Channel__** {}".format(log_e, log_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`New channel:` {} ### {}".format(u.name, u.id)
                                await client.edit_message(k, m)
                                break
                            except:
                                embed.description = "{} Unable to send logs in that channel ( `{}` ).".format(error_e, u.name)
                                await client.edit_message(h, embed=embed)
                                break
                    if len(p) == 0:
                        embed.description = "{} Channel not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

#######################
client.run(os.environ['BOT_TOKEN'])
