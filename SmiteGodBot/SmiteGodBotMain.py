import asyncio

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

from numpy import random as random
import numpy as np
import os

Gods = [['Achilles',        'Warrior',  'Greek',        'No'],
        ['Agni',            'Mage',     'Hindu',        'No'],
        ['Ah Muzen Cab',    'Hunter',   'Mayan',        'No'],
        ['Ah Puch',         'Mage',     'Mayan',        'No'],
        ['Amaterasu',       'Warrior',  'Japanese',     'No'],
        ['Anhur',           'Hunter',   'Egyptian',     'No'],
        ['Anubis',          'Mage',     'Egyptian',     'No'],
        ['Ao Kuang',        'Mage',     'Chinese',      'No'],
        ['Aphrodite',       'Mage',     'Greek',        'Yes'],
        ['Apollo',          'Hunter',   'Greek',        'No'],
        ['Arachne',         'Assassin', 'Greek',        'No'],
        ['Ares',            'Guardian', 'Greek',        'No'],
        ['Artemis',         'Hunter',   'Greek',        'No'],
        ['Artio',           'Guardian', 'Celtic',       'No'],
        ['Athena',          'Guardian', 'Greek',        'No'],
        ['Awilix',          'Assassin', 'Mayan',        'No'],
        ['Baba Yaga',       'Mage',     'Slavic',       'No'],
        ['Bacchus',         'Guardian', 'Roman',        'No'],
        ['Bakasura',        'Assassin', 'Hindu',        'No'],
        ['Baron Samedi',    'Mage',     'Voodoo',       'Yes'],
        ['Bastet',          'Assassin', 'Egyptian',     'No'],
        ['Bellona',         'Warrior',  'Roman',        'No'],
        ['Cabrakan',        'Guardian', 'Mayan',        'No'],
        ['Camazotz',        'Assassin', 'Mayan',        'No'],
        ['Cerberus',        'Guardian', 'Greek',        'No'],
        ['Cernunnos',       'Hunter',   'Celtic',       'No'],
        ['Chaac',           'Warrior',  'Mayan',        'No'],
        ["Chang'e",         'Mage',     'Chinese',      'Yes'],
        ['Chernobog',       'Hunter',   'Slavic',       'No'],
        ['Chiron',          'Hunter',   'Greek',        'No'],
        ['Chronos',         'Mage',     'Greek',        'No'],
        ['Cthulhu',         'Guardian', 'GreatOldOnes', 'No'],
        ['Cu Chulainn',     'Warrior',  'Celtic',       'No'],
        ['Cupid',           'Hunter',   'Roman',        'No'],
        ['Da Ji',           'Assassin', 'Chinese',      'No'],
        ['Danzaburou',       'Hunter',   'Japanese',    'No'],
        ['Discordia',       'Mage',     'Roman',        'No'],
        ['Erlang Shen',     'Warrior',  'Chinese',      'No'],
        ['Fafnir',          'Guardian', 'Norse',        'No'],
        ['Fenrir',          'Assassin', 'Norse',        'No'],
        ['Freya',           'Mage',     'Norse',        'No'],
        ['Ganesha',         'Guardian', 'Hindu',        'No'],
        ['Geb',             'Guardian', 'Egyptian',     'No'],
        ['Guan Yu',         'Warrior',  'Chinese',      'Yes'],
        ['Hachiman',        'Hunter',   'Japanese',     'No'],
        ['Hades',           'Mage',     'Greek',        'No'],
        ['He Bo',           'Mage',     'Chinese',      'No'],
        ['Heimdallr',       'Hunter',   'Norse',        'No'],
        ['Hel',             'Mage',     'Norse',        'Yes'],
        ['Hera',            'Mage',     'Greek',        'No'],
        ['Hercules',        'Warrior',  'Roman',        'No'],
        ['Horus',           'Warrior',  'Egyptian',     'Yes'],
        ['Hou Yi',          'Hunter',   'Chinese',      'No'],
        ['Hun Batz',        'Assassin', 'Mayan',        'No'],
        ['Isis',            'Mage',     'Egyptian',     'No'],
        ['Izanami',         'Hunter',   'Japanese',     'No'],
        ['Janus',           'Mage',     'Roman',        'No'],
        ['Jing Wei',        'Hunter',   'Chinese',      'No'],
        ['Jormungandr',     'Guardian', 'Norse',        'No'],
        ['Kali',            'Assassin', 'Hindu',        'No'],
        ['Khepri',          'Guardian', 'Egyptian',     'No'],
        ['King Arthur',     'Warrior',  'Arthurian',    'No'],
        ['Kukulkan',        'Mage',     'Mayan',        'No'],
        ['Kumbhakarna',     'Guardian',  'Hindu',       'No'],
        ['Kuzenbo',         'Guardian', 'Japanese',     'No'],
        ['Loki',            'Assassin', 'Norse',        'No'],
        ['Medusa',          'Hunter',   'Greek',        'No'],
        ['Mercury',         'Assassin', 'Roman',        'No'],
        ['Merlin',          'Mage',     'Arthurian',    'No'],
        ['Mulan',           'Warrior',  'Chinese',      'No'],
        ['Ne Zha',          'Assassin', 'Chinese',      'No'],
        ['Neith',           'Hunter',   'Egyptian',     'No'],
        ['Nemesis',         'Assassin', 'Greek',        'No'],
        ['Nike',            'Warrior',  'Greek',        'No'],
        ['Nox',             'Mage',     'Roman',        'No'],
        ['Nu Wa',           'Mage',     'Chinese',      'No'],
        ['Odin',            'Warrior',  'Norse',        'No'],
        ['Olorun',          'Mage',     'Yoruba',       'No'],
        ['Osiris',          'Warrior',  'Egyptian',     'No'],
        ['Pele',            'Assassin', 'Polynesian',   'No'],
        ['Persephone',      'Mage',     'Greek',        'No'],
        ['Poseidon',        'Mage',     'Greek',        'No'],
        ['Ra',              'Mage',     'Egyptian',     'Yes'],
        ['Raijin',          'Mage',     'Japanese',     'No'],
        ['Rama',            'Hunter',   'Hindu',        'No'],
        ['Ratatoskr',       'Assassin', 'Norse',        'No'],
        ['Ravana',          'Assassin', 'Hindu',        'No'],
        ['Scylla',          'Mage',     'Greek',        'No'],
        ['Serqet',          'Assassin', 'Egyptian',     'No'],
        ['Set',             'Assassin', 'Egyptian',     'No'],
        ['Skadi',           'Hunter',   'Norse',        'No'],
        ['Sobek',           'Guardian', 'Egyptian',     'No'],
        ['Sol',             'Mage',     'Norse',        'No'],
        ['Sun Wukong',      'Warrior',  'Chinese',      'No'],
        ['Susano',          'Assassin', 'Japanese',     'No'],
        ['Sylvanus',        'Guardian', 'Roman',        'Yes'],
        ['Terra',           'Guardian', 'Roman',        'Yes'],
        ['Thanatos',        'Assassin', 'Greek',        'No'],
        ['The Morrigan',    'Mage',     'Celtic',       'No'],
        ['Thor',            'Assassin', 'Norse',        'No'],
        ['Thoth',           'Mage',     'Egyptian',     'No'],
        #['Tiamat',          'Mage',     'Babylonian',   'No'],
        ['Tsukuyomi',       'Assassin', 'Japanese',     'No'],
        ['Tyr',             'Warrior',  'Norse',        'No'],
        ['Ullr',            'Hunter',   'Norse',        'No'],
        ['Vamana',          'Warrior',  'Hindu',        'No'],
        ['Vulcan',          'Mage',     'Roman',        'No'],
        ['Xbalanque',       'Hunter',   'Mayan',        'No'],
        ['Xing Tian',       'Guardian', 'Chinese',      'No'],
        ['Yemoja',          'Guardian', 'Yoruba',       'Yes'],
        ['Ymir',            'Guardian', 'Norse',        'No'],
        ['Zeus',            'Mage',     'Greek',        'No'],
        ['Zhong Kui',       'Mage',     'Chinese',      'No']]



client = commands.Bot(command_prefix='.')
global voice
global mute
global rLoki
global currentMatch
global orderRerolls
global chaosRerolls

#0 = Name, 1 = Role, 2 = Pantheon, 3 = Healer (Yes/No)
@client.event
async def on_ready():
    global mute
    mute = 1
    print('Bot is ready and connected')

"""
@client.event
async def on_voice_state_update(member,before,after):
    global mute
    if before.channel is None and after.channel is not None and mute == 0:
        if member.name == "BigMaple":
            print("BigMaple Spotted")
            channel = member.voice.channel
            voice = get(client.voice_clients)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio("Voicelines/BigMaple.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20
"""

@client.command()
async def commands(ctx):
    await ctx.send(f'Smite God Bot Help Page\n'
                   f'Commands:\n'
                   f'.help - a page listing all current commands\n\n'
                   f'.commands - shows this message\n\n'
                   f'.[rTeam|rteam|rt) "# players"\n'
                   f'   Rolls two randoms teams for a game of X players\n'
                   f'   Example: .rTeam 10\n\n'
                   f'.[rAssault|rassault|ra) "# players"\n'
                   f'   Rolls two randoms teams for an assault game of X players\n'
                   f'   The game currently has an 20% chance of healers appearing\n'
                   f'   Example: .rAssault 10\n\n'
                   f'.[rGod|rgod|rg]\n'
                   f'   Rolls a single god from all gods currently in the game.\n'
                   f'   Example: .rGod\n\n'
                   f'.[rGodRole|rgodrole|rgr] "Role"\n'
                   f'   Rolls a single god from the given role\n'
                   f'   Example: .rGodRole Mage\n\n'
                   f'.[rGodPantheon|rgodpantheon|rgp]\n'
                   f'   Rolls a single god from the given pantheon\n'
                   f'   Example: .rGodPantheon Hindu\n\n'
                   f'.[rGodRolePantheon|rgodrolepantheon|rgrp] "pantheon" "role"\n'
                   f'   Rolls a single god from the given pantheon and role\n'
                   f'   Example: .rGodRolePantheon greek guardian\n')

@client.command(aliases=['rgodrolepantheon', 'rgrp'])
async def rGodRolePantheon(ctx, *, rolepantheon):
    list = rolepantheon.split(" ")
    role = list[1]
    pantheon = list[0]
    godList = []
    for n in Gods:
        if n[2].lower() == pantheon.lower() and n[1].lower() == role.lower():
            godList.append(n[0])
    if len(godList) > 0:
        god = random.choice(godList)
        print(f'Rolled {god} from {godList}. ({pantheon}, {role})')
        await ctx.send(f'{ctx.author.name} rolled the {pantheon} {role} {god}!')
    else:
        await ctx.send(f'No {role} exists in the {pantheon} pantheon currently.\n')

@client.command(aliases=['rgodpantheon', 'rgp'])
async def rGodPantheon(ctx, *, pantheon):
    pantheonList = []
    for n in Gods:
        if n[2].lower() == pantheon.lower():
            pantheonList.append(n[0])
    if len(pantheonList) > 0:
        god = random.choice(pantheonList)
        print(f'Rolled {god} from {pantheonList}. ({pantheon})')
        await ctx.send(f'{ctx.author.name} rolled the {pantheon} god {god}!')
    else:
        await ctx.send(f'No gods exist in the {pantheon} pantheon currently.\n'
                       f'Try again with Arthurian, Celtic, Chinese, Egyptian, Greek, Hindu, Japanese, Mayan, Norse,'
                       f'Polynesian, Roman, Slavic, Voodoo or Yoruba.')

@client.command(aliases=['rgodrole', 'rgr'])
async def rGodRole(ctx, *, role):
    roleList = []
    for n in Gods:
        if n[1].lower() == role.lower():
            roleList.append(n[0])
    if len(roleList) > 0:
        god = random.choice(roleList)
        print(f'Rolled {god} from {roleList}. ({role})')
        await ctx.send(f'{ctx.author.name} rolled the {role} {god}!')
    else:
        await ctx.send(f'No gods exist in the {role} role.\n'
                       f'Try again with Mage, Assassin, Warrior, Guardian or Hunter.')

#random loki
@client.command()
async def loki(ctx):
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(discord.FFmpegPCMAudio("Voicelines/LokiCloak.mp3"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.20

    while True:
        await asyncio.sleep(1)
        rNum = random.randint(0,250)
        if rNum == 1:
            voice.play(discord.FFmpegPCMAudio("Voicelines/Loki3.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20
            break

    while voice.is_playing():
        await asyncio.sleep(0.5)
    if not voice.is_playing():
        await voice.disconnect()

#Mute bot
@client.command()
async def mute(ctx):
    global mute
    mute = 1
    await ctx.send(f'Bot has been muted')

#UnMute bot
@client.command()
async def unmute(ctx):
    global mute
    mute = 0
    await ctx.send(f'Bot has been unmuted')


@client.command()
async def voiceline(ctx, *, god):
    global mute
    if mute == 0:
        channel = ctx.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        godName = god.replace(" ", "")
        voiceLine_there = os.path.isfile("Voicelines/" + godName + ".mp3")

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if voiceLine_there:
            print("Found " + godName + ".mp3")
            voice.play(discord.FFmpegPCMAudio("Voicelines/" + godName + ".mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20
        else:
            print(godName + ".mp3 not found")
            voice.play(discord.FFmpegPCMAudio("Voicelines/RaijinJump.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20

        while voice.is_playing():
            await asyncio.sleep(0.5)
        if not voice.is_playing():
               await voice.disconnect()
    else:
        await ctx.send(f'Bot has been muted\n Use the command .unmute to allow audio')

@client.command(aliases=['rgod', 'rg'])
async def rGod(ctx):
    global mute
    all = []
    for n in Gods:
        all.append(n[0])
    god = random.choice(all)
    print(f'Rolled {god} from all gods.')
    await ctx.send(f'{ctx.author.name} rolled {god}!')

    if mute == 0:
        channel = ctx.author.voice.channel
        voice = get(client.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        godName = god.replace(" ", "")
        voiceLine_there = os.path.isfile("Voicelines/"+godName+".mp3")
        if voiceLine_there:
            print("Found " + godName+".mp3")
            voice.play(discord.FFmpegPCMAudio("Voicelines/"+godName+".mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20
        else:
            print(godName + ".mp3 not found")
            voice.play(discord.FFmpegPCMAudio("Voicelines/RaijinJump.mp3"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.20

        while voice.is_playing():
            await asyncio.sleep(0.5)
        if not voice.is_playing():
               await voice.disconnect()

@client.command(aliases=['Leave'])
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send(f'Bot is not currently in any voice channel')

##def rGod_Voice(channel):


@client.command(aliases=['rteam', 'rt'])
async def rTeam(ctx, *, players):
    if int(players) % 2 != 0 or int(players) < 1:
        await ctx.send(f'Please input an even amount of players between 2 and 10')
    else:
        all = []
        for n in Gods:
            all.append(n[0])
        Team1 = random.choice(all,int(int(players)/2),replace=False)
        Team2 = random.choice(all,int(int(players)/2),replace=False)
        await ctx.send(f'{players} Player Game \nOrder: {", ".join(Team1)} \nChaos: {", ".join(Team2)}')

@client.command(aliases=['rassault', 'ra'])
async def rAssault(ctx, *, players):
    global currentMatch
    global chaosRerolls
    global orderRerolls
    if int(players) % 2 != 0 or int(players) < 1:
        await ctx.send(f'Please input an even amount of players between 2 and 10')
    else:
        orderRerolls = 5
        chaosRerolls = 5
        noHeal = []
        Heal = []
        for n in Gods:
            if n[3] == 'Yes':
                Heal.append(n[0])
            else:
                noHeal.append(n[0])

        Chance = random.choice(100,1)
        if Chance[0] > 80:
            #Healer Game
            Team1 = random.choice(noHeal, (int(int(players) / 2)-1), replace=False)
            Team2 = random.choice(noHeal, (int(int(players) / 2)-1), replace=False)
            Team1a = random.choice(Heal, 1, replace=False)
            Team2a = random.choice(Heal, 1, replace=False)
            Team1 = np.append(Team1, Team1a)
            Team2 = np.append(Team2, Team2a)
            currentMatch = [Team1, Team2]
            print(f'Assault Healer game created with {Team1} vs {Team2}')

            embedAssaultHealerGame = discord.Embed(title=players + " Player Healer Assault Game",
                                               color=0x00ff00)
            embedAssaultHealerGame.add_field(name="Order Team",
                                         value=", ".join(currentMatch[0]),
                                         inline=False)
            embedAssaultHealerGame.add_field(name="Chaos Team",
                                             value=", ".join(currentMatch[1]),
                                             inline=False)

            await ctx.send(embed=embedAssaultHealerGame)
            #await ctx.send(f'{players} Player Healer Assault Game\nOrder:\t{", ".join(Team1)}\nChaos:\t{", ".join(Team2)}')
        else:
            #No Healer Game
            Team1 = random.choice(noHeal, int(int(players) / 2), replace=False)
            Team2 = random.choice(noHeal, int(int(players) / 2), replace=False)
            currentMatch = [Team1, Team2]
            print(f'Assault No-Healer game created with {Team1} vs {Team2}')

            embedAssaultHealerGame = discord.Embed(title=players + " Player Non-Healer Assault Game",
                                                   color=0x00ff00)
            embedAssaultHealerGame.add_field(name="Order Team",
                                             value=", ".join(currentMatch[0]),
                                             inline=False)
            embedAssaultHealerGame.add_field(name="Chaos Team",
                                             value=", ".join(currentMatch[1]),
                                             inline=False)

            await ctx.send(embed=embedAssaultHealerGame)
            #await ctx.send(f'{players} Player Non-Healer Assault\nOrder:\t{", ".join(Team1)}\nChaos:\t{", ".join(Team2)}')

@client.command(aliases=[])
async def reroll(ctx, *, rerollGod):
    global currentMatch
    global orderRerolls
    global chaosRerolls
    if currentMatch == None:
        await ctx.send(f'No match exists to reroll from.')
    else:

        rerollGod = rerollGod.lower()
        if "order" in rerollGod:
            if orderRerolls <= 0:
                changeGod = 1
                await ctx.send(f'No rerolls remain for the Order Team')
            else:
                #Search order team for god
                rerollGod = rerollGod.replace("order", "")
                rerollGod = rerollGod.strip()
                changeGod = 0
                for n in currentMatch[0]:
                    if rerollGod in n.lower():
                        changeGod = 1
                        orderRerolls = orderRerolls - 1
                        #Get List of Gods
                        noHeal = []
                        Heal = []
                        for listGod in Gods:
                            if listGod[3] == 'Yes':
                                Heal.append(listGod[0])
                            else:
                                noHeal.append(listGod[0])

                        #Get new god
                        god = random.choice(noHeal)
                        #If random god already on team then reroll until you get one that isnt

                        originalGod = n
                        currentMatch[0] = [w.replace(n, god) for w in currentMatch[0]]

                        print(f'{ctx.author.name} rerolled {originalGod} into {god}\n'
                              f'New teams are:\n'
                              f'Order:\t{", ".join(currentMatch[0])}\nChaos:\t{", ".join(currentMatch[1])}')

                        embedAssaultReroll = discord.Embed(title="God Reroll",
                                                           color=0x00ff00,
                                                           description=ctx.author.name + ' rerolled ' +
                                                                       originalGod + ' into ' + god)
                        embedAssaultReroll.add_field(name="Current Teams",
                                                     value="Order: " + ", ".join(currentMatch[0]) +
                                                           '\n' + "Chaos: " + ", ".join(currentMatch[1]),
                                                     inline=True)
                        embedAssaultReroll.add_field(name="Rerolls Remaining",
                                                     value="Order: " + str(orderRerolls) + '\n' + "Chaos: " + str(
                                                         chaosRerolls),
                                                     inline=True)
                        await ctx.send(embed=embedAssaultReroll)

            if changeGod == 0:
                await ctx.send(f' God could not be found on the Order Team.')
        elif "chaos" in rerollGod:
            if chaosRerolls <= 0:
                changeGod = 1
                await ctx.send(f'No rerolls remain for the Order Team')
            else:
                # Search chaos team for god
                rerollGod = rerollGod.replace("chaos", "")
                rerollGod = rerollGod.strip()
                changeGod = 0
                for n in currentMatch[1]:
                    if rerollGod in n.lower():
                        changeGod = 1
                        chaosRerolls = chaosRerolls - 1
                        # Get List of Gods
                        noHeal = []
                        Heal = []
                        for listGod in Gods:
                            if listGod[3] == 'Yes':
                                Heal.append(listGod[0])
                            else:
                                noHeal.append(listGod[0])

                        # Get new god
                        god = random.choice(noHeal)
                        # If random god already on team then reroll until you get one that isnt
                        originalGod = n

                        print(f'{ctx.author.name} rerolled {originalGod} into {god}\n'
                              f'New teams are:\n'
                              f'Order:\t{", ".join(currentMatch[0])}\nChaos:\t{", ".join(currentMatch[1])}')

                        currentMatch[1] = [w.replace(n, god) for w in currentMatch[1]]

                        embedAssaultReroll = discord.Embed(title="God Reroll",
                                                           color=0x00ff00,
                                                           description=ctx.author.name + ' rerolled ' +
                                                                       originalGod + ' into ' + god)
                        embedAssaultReroll.add_field(name="Current Teams",
                                                     value="Order: " + ", ".join(currentMatch[0]) +
                                                           '\n' + "Chaos: " + ", ".join(currentMatch[1]),
                                                     inline=True)
                        embedAssaultReroll.add_field(name="Rerolls Remaining",
                                                     value="Order: " + str(orderRerolls) + '\t' + "Chaos: " + str(chaosRerolls),
                                                     inline=True)
                        await ctx.send(embed=embedAssaultReroll)

            if changeGod == 0:
                await ctx.send(f' God could not be found on the Chaos Team.')

load_dotenv()
client.run(os.getenv('SMITEGODBOT_TOKEN'))

