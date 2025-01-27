# {color=#f6d6bd}Elah{/color} the carpenter - Efren’s brother, more serious and less energetic. Brown skin, leather pants, jacket, a yellow elk shoulder cape, a cudgel with a rock - overweight and often leans on things # pocięte dłonie, bardzo białe zęby, często się opiera o rzeczy, "flashes you a disarming, white smile", squeezes nie tylko brzuch ale też "lower part of his jacket"

default elah_friendship = 0
default elah_efren_siblings = 0
default elah_lastseen = 0
default elah_fluff = 0
default elah_locked = 0

default elah_about_efren = 0
default elah_about_asterion = 0
default elah_about_asterion_found = 0
default elah_about_asterion_friendship = 0
default elah_about_himself = 0
default elah_about_plague1 = 0
default elah_about_plague2 = 0
default elah_about_bronzerod = 0
default elah_about_bandits = 0
default elah_about_creeks = 0
default elah_about_peninsula = 0
default elah_about_greenmountaintribe = 0
default elah_about_steephouse = 0
default elah_about_steephouse_canceled = 0
default elah_about_steephouse_gray = 0
default elah_about_steephouse_friendship = 12
default elah_about_steephouse_friendship_thais = 0
default elah_about_nomoreundead = 0
default elah_about_traps = 0

default elah_about_makingalantern = 0
default elah_about_makingalantern_made = 0
define elah_about_makingalantern_threshhold = 5

default elah_quest_easternpath_reward = 0
default elah_quest_easternpath_rewardisnotfair = 0
default elah_quest_easternpath_lies = 0
default elah_quest_easternpath_hint1 = 0
default elah_quest_easternpath_hint2 = 0
default elah_quest_easternpath_whynotwest = 0
default elah_quest_easternpath_lumberjacks = 0
default elah_quest_easternpath_fallentree_day = 0
default elah_quest_easternpath_fallentree_roadknown = 0
default elah_quest_easternpath_goblins_coin = 0

label creekselah01:
    if elah_lastseen != day:
        $ elah_lastseen = day
        $ elah_fluff = renpy.random.choice(['He’s preparing the planks for a simple tabletop. ', 'He is trying to carve something on the surface of a wooden mug, but you don’t recognize the shape. ', 'He’s testing a new chair, which wobbles a bit too much. ', 'He’s in the middle of his break, leaning against the top of his working bench. ', 'He’s removing bark from a large log, throwing it into the pile of wood in the center of the square. ', 'He’s cutting a plank into smaller slats. ', 'He’s rounding a block of wood, preparing a future club. ', 'He’s polishing the surface of a new cudgel. ', 'He orders a few kids around, and when one of them gives him a confused look, he squeezes his belly. “Hwat are you waiting for? There’s work to be done!” '])
        if elah_friendship >= 8:
            $ custom1 = "He smiles and puts away his tools. “Welcome back, friend. Good to see that you stay safe on the roads.”"
        elif elah_friendship >= 4:
            $ custom1 = "He waves to you with a chisel. “Hi there, friend! I see you’ve taken a liking to our village.”"
        elif elah_friendship >= 0:
            $ custom1 = "He nods to you and wipes the sweat off his forehead. “Welcome to {color=#f6d6bd}Creeks{/color}, friend!”"
        else:
            $ custom1 = "He’s focused on his work. “Greetings.”"
    else:
        $ elah_lastseen = day
        $ elah_fluff = ""
        if elah_friendship >= 8:
            $ custom1 = "He smiles and puts away his tools. “Hwat d’ye need, friend?”"
        elif elah_friendship >= 4:
            $ custom1 = "He pauses his work. “Did you forget something?”"
        elif elah_friendship >= 0:
            $ custom1 = "He nods to you, but mostly pays attention to the woodwork at hand."
        else:
            $ custom1 = "He’s focused on his tools, and doesn’t look in your direction."
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    # if SPECIAL EVENT:
    #     menu:
    #         '
    #         \n\n
    #         '
    #         '':
    #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
    #             jump z
    # else:
    $ questionpreset = "elah1"
    menu:
        '[elah_fluff][custom1]
        '
        '(elah1 set)':
            pass

label creekselahafterinteraction01:
    $ questionpreset = "elah1"
    $ elah_fluff = renpy.random.choice(['He reaches for an adze. “Anything else?”', 'He leans against the table, sweating. “The days are getting shorter, aye?”', 'He sighs, looking at the amount of work ahead of him. “So...”', 'He blows at the shavings, sending them flying to settle on the ground, then considers the next tool to select.'])
    menu:
        '[elah_fluff]
        '
        '(elah1 set)':
            pass

label creeksleavingelah01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you later.”')
    jump creeksafterinteraction01

label creekselahonsupplies01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for supplies.”')
    $ oldhava_known = 1
    $ questionpreset = "elah1"
    menu:
        'At first he offers you a “fine barrel” or a stool, but after you explain you’d prefer something useful for a traveler, he returns to his work. “Then you should speak with {color=#f6d6bd}Foggy{/color} at her tavern, you rode past it before you got here, aye? Maybe {color=#f6d6bd}Old Hava{/color} has some food to spare, but I doubt it.”
        '
        '(elah1 set)':
            pass

label elah_about_plague1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Old Págos{/color} is suffering from a plague. The village is isolating itself from outsiders.”')
    $ elah_about_plague1 = 1
    $ oldpagos_plague_warnedplaces += 1
    $ questionpreset = "elah1"
    $ quarters += 1
    $ minutes += 5
    $ creeks_reputation += 1
    menu:
        'He freezes, puts away his tools, then looks at you with wide eyes. “Wait for a bit, will you?” Without waiting for your response, he springs up and knocks down a few planks as he lurches away, asking his neighbors to call the entire tribe.
        \n\nPeople surround you, asking what’s going on, and once the news spreads, you answer dozens of questions, though most of what you have to say could be summed up with “I’m not sure.” Aside from the worried faces, there are also more pragmatic ones - hunters mention that they won’t be able to deliver their autumn pelts, while one of the farmers wonders about her cousin. “She was always so pious,” she says with an accent you remember from {color=#f6d6bd}Old Págos{/color}. “May The Wright reward her prayers, or else!”
        \n\nAfter some time, the crowd pays you little attention, and {color=#f6d6bd}Elah{/color} leads you back to his workshop. “They and I will discuss this later,” he says with an absent voice, then sits down and glances at his neighbors.
        '
        '(elah1 set)':
            pass
    label elah_about_plague2:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve helped to clear the plague from {color=#f6d6bd}Old Págos{/color}. It may not be a safe place, but it will survive.”')
        $ elah_about_plague2 = 1
        $ creeks_reasonstojoin_healedtheplague = 1
        $ questionpreset = "elah1"
        $ creeks_reputation += 1
        $ description_howlersdell04 = "According to {color=#f6d6bd}Elah{/color}, the locals are unwilling to help others, and are led by a tyrant."
        $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
        menu:
            '{color=#f6d6bd}Elah’s{/color} grin is soon followed by his raised voice. “And you’re serious? Everyone!” He addresses other people working near the square. “Tell the others! The plague is gone! We’re safe!” After his eyes return to you, he clears his throat and turns away again. “{color=#f6d6bd}Old Págos{/color} is safe!”
            \n\nYou explain briefly what happened and he spends a good few moments considering the old druid’s part. “I wouldn’t expect someone from {color=#f6d6bd}Howler’s{/color} to help another soul in need,” he says while his hand clenches the bottom part of his cloak. “Not since they’re ruled by a tyrant. But it’s not the first time this forest speaker has protected the peninsula from a grave threat,” he smiles at you. “And so did you, I guess.”
            '
            '(elah1 set)':
                pass
    label elah_about_plague2alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There are many things occuring at {color=#f6d6bd}Old Págos{/color}... The village was suffering from a plague, but I helped to clear it. It now isolates itself from outsiders.”')
        $ elah_about_plague1 = 1
        $ elah_about_plague2 = 1
        $ oldpagos_plague_warnedplaces += 1
        $ creeks_reasonstojoin_healedtheplague = 1
        $ questionpreset = "elah1"
        $ creeks_reputation += 1
        $ quarters += 1
        $ minutes += 5
        $ description_howlersdell04 = "According to {color=#f6d6bd}Elah{/color}, the locals are unwilling to help others, and are led by a tyrant."
        $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
        menu:
            'He freezes, puts away his tools, then looks at you with wide eyes. “Slow down... A plague?” You get into more detail, and he’s unsure if he needs to gather the others, or just let you speak. As he asks about the well-being of the people of {color=#f6d6bd}Old Págos{/color}, his eyes are concerned, but the following relief sparks his wide grin - until you mention the part of the old druid.
            \n\n“I wouldn’t expect someone from {color=#f6d6bd}Howler’s{/color} to help another soul in need,” he says while his hand clenches the lower edge of his cloak. “Not since they’re ruled by a tyrant. But it’s not the first time this forest speaker has protected the peninsula from a grave threat,” he smiles at you. “And so did you, I guess.”
            '
            '(elah1 set)':
                pass

label creekselah_about_bandits01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about the bandits. Have they caused you any trouble?”')
    if (elah_friendship+appearance_charisma) < 4:
        $ elah_about_bandits = 1
        $ questionpreset = "elah1"
        menu:
            'He makes an awkward cut with a chisel and lets out a quiet {i}shit{/i}, then starts to rub the plank with his thumb. “Bandits, you say? Soldiers from the city have already taken care of them.”
            '
            '(elah1 set)':
                pass
    else:
        $ elah_about_bandits = 2
        $ quest_intelforpeltnorth_description04b = "{color=#f6d6bd}Creeks{/color} has had no issues with the bandits."
        if quest_intelforpeltnorth == 1:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ description_bandits02 = "According to {color=#f6d6bd}Elah{/color}, all of them were born in the local villages."
        $ banditshideout_villagesasked_aboutattacks += 1
        $ questionpreset = "elah1"
        menu:
            'He makes an awkward cut with a chisel and lets out a quiet {i}shit{/i}, then starts to rub the plank with his thumb. “Bandits, you say? Soldiers from the city have already taken care of them.”
            \n\nYou pressure him for a bit and after he glances at you, he nods slowly. “{i}Bandit{/i} is a strong word. Those are not some strangers, but folks of the North, our neighbors. One of them is from our very own tribe. And they don’t target us, just strangers.” You ask him again if he’s sure no one from his village has been targeted so far, and after a cold {i}aye{/i} he reaches for a carving knife.
            '
            '(elah1 set)':
                pass
    label creekselah_about_bandits02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m worried about those bandits, {color=#f6d6bd}Elah{/color}.”')
        $ custom1 = "He looks at you for a bit, then nods slowly."
        jump creekselah_about_bandits03
    label creekselah_about_bandits02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pressure him about the bandits. “I already met with {color=#f6d6bd}Glaucia{/color}, {i}friend{/i}. Don’t hide things from me.”')
        $ elah_friendship -= 1
        $ custom1 = "He gives you an angry look and clenches his stomach, but then nods."
        jump creekselah_about_bandits03
    label creekselah_about_bandits02alt2:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pressure him about the bandits. “You told me yourself about {color=#f6d6bd}Glaucia{/color}, {i}friend{/i}. Don’t hide things from me.”')
        $ elah_friendship -= 1
        $ custom1 = "He gives you an angry look and clenches his stomach, but then nods."
        jump creekselah_about_bandits03
    label creekselah_about_bandits03:
        $ elah_about_bandits = 2
        $ quest_intelforpeltnorth_description04b = "{color=#f6d6bd}Creeks{/color} has had no issues with the bandits."
        if quest_intelforpeltnorth == 1:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ description_bandits02 = "According to {color=#f6d6bd}Elah{/color}, all of them were born in the local villages."
        $ banditshideout_villagesasked_aboutattacks += 1
        $ questionpreset = "elah1"
        menu:
            '[custom1] “Those are not some strangers, but folks of the North, our neighbors. One of them is from our very own tribe. And they don’t target us, just strangers.” You ask him again if he’s sure no one from his village has been targeted so far, and after a cold {i}aye{/i} he reaches for a carving knife.
            '
            '(elah1 set)':
                pass

label elah_about_bronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to place this rod somewhere high. It belongs to {color=#f6d6bd}Eudocia{/color}, the enchantress.”')
    $ elah_about_bronzerod = 1
    $ questionpreset = "elah1"
    $ quarters += 2
    if (creeks_reputation+elah_friendship+appearance_charisma) >= 10 or creeks_feast:
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ item_bronzerod -= 1
        $ eudocia_bronzerod_rodin_creeks = 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
            if eudocia_bronzerod_installed < 4:
                $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
            elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
            elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
            else:
                $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
        else:
            if eudocia_bronzerod_installed >= 4:
                if not quest_bronzerod_description04:
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        menu:
            'He grabs the rod and looks at it with caution. “I wouldn’t call her our {i}friend{/i}, exactly. You’d do better selling this.” Swinging it left and right like a club, he tells you to wait. “It can’t be just my decision. I’m going to ask the others, at least a few of them.”
            \n\nYou rest at a table and observe how the man approaches various souls and exchanges a few words with them. It takes him so long you manage to get bored enough to indulge a little girl who’d like to pet {color=#f6d6bd}[horsename]{/color}.
            \n\nThe man returns without the rod. “Well, my tribe calls you a {i}fair soul{/i},” he smiles and wipes the sweat off his forehead. “We’ll put it at the watchtower, there aren’t that many birds that would steal something of this size.”
            '
            '(elah1 set)':
                pass
    else:
        menu:
            'He grabs the rod and looks at it with caution. “I wouldn’t call her our {i}friend{/i}, exactly. You’d do better selling this.” Swinging it left and right like a club, he tells you to wait. “It can’t be just my decision. I’m going to ask the others, at least a few of them.”
            \n\nYou rest at a table and observe how the man approaches various souls and exchanges a few words with them. It takes him so long you manage to get bored enough to indulge a little girl who’d like to pet {color=#f6d6bd}[horsename]{/color}.
            \n\nThe man returns and gives you the rod back. “Well, my tribe is far from convinced,” he wipes the sweat off his forehead. “We’d rather stay away from it.”
            '
            '(elah1 set)':
                pass
    label elah_about_bronzerod02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want you to discuss the issue of the enchantress’ rod with the village. You should know by now I can be trusted.”')
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ item_bronzerod -= 1
        $ eudocia_bronzerod_rodin_creeks = 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
            $ renpy.notify("Journal updated: Bronze Rods")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
            if eudocia_bronzerod_installed < 4:
                $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
            elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
            elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
            else:
                $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
        else:
            if eudocia_bronzerod_installed >= 4:
                if not quest_bronzerod_description04:
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        $ questionpreset = "elah1"
        menu:
            'He takes the rod and smiles. “There’s no need, I already know hwat they’ll say. My tribe calls you a {i}fair soul{/i}, we’ll put it at the watchtower, there aren’t that many birds that would steal something of this size.”
            '
            '(elah1 set)':
                pass

label elahaboutorentius01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know who {color=#f6d6bd}Thais{/color} is, right? She may need your help. It’s about {color=#f6d6bd}Orentius{/color}.”')
    menu:
        'You vaguely describe her plan, but he doesn’t meet your eyes, focused on the work at hand. You offer to address his tribe, but for a few breaths you only hear the sound of the hammer, which {color=#f6d6bd}Elah{/color} is using to put together two blocks of wood with a fancy joint, without nails.
        \n\nHe brings it close to his stomach and starts to pressure it with his scarred hands, making sure it holds. “And hwat are your thoughts on {color=#f6d6bd}Thais{/color}, friend?”
        '
        '“She’s a strong leader.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s a strong leader.”')
            $ description_thais_pcopinion = "strongleader"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without binding myself to any specific leader."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship += 0
            $ creeks_reputation -= 1
            $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
            $ questionpreset = "elah1"
            menu:
                '“Don’t even start,” he puts the frame on the workbench with a loud thud. “A strong {i}tyrant{/i}, aye. Follow her and you’ll become one of many souls who she’s betrayed before you gain anything. And she won’t be reached by justice, behind her walls and guards,” he looks at the cuts on his hands.
                \n\n“If you want to get out of her plots unscarred, deal with {color=#f6d6bd}Orentius{/color} on your own, without the villages. The tribe of {color=#f6d6bd}Creeks{/color} already agreed to not step in, and if I were to tell everyone that {color=#f6d6bd}Thais{/color} wants to stain her hands through us, they would refuse twice.”
                '
                '(elah1 set)':
                    pass
        '“She’s worthy of our trust.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s worthy of our trust.”')
            $ description_thais_pcopinion = "trustworthy"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship -= 1
            $ creeks_reputation -= 1
            $ questionpreset = "elah1"
            $ quest_ruins_10yclue07 = "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
            menu:
                '“Then you know nothing ‘bout her,” his fists clench the pieces of wood. “After hwat she did ten years ago, my tribesfolk would refuse her twice. We’ve already discussed the trouble with {color=#f6d6bd}Orentius{/color} and we will {i}not{/i} step in.”
                '
                '(elah1 set)':
                    pass
        '“There may be an evil spirit in her.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There may be an evil spirit in her.”')
            $ description_thais_pcopinion = "wicked"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without binding myself to any specific leader."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship += 1
            $ creeks_reputation += 1
            $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
            $ quest_ruins_10yclue07 = "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
            $ questionpreset = "elah1"
            menu:
                'He measures his words before speaking. “No, just a cruel, cold soul. Ever since she became the leader her village has changed, but...” He looks at the frame in his hands and puts it away, still without turning toward you. “It was ten years ago when she became a tyrant. My tribesfolk won’t ever agree to another one of her {i}pacts{/i}.”
                \n\n“If you want to get out of her plots unscarred, deal with {color=#f6d6bd}Orentius{/color} on your own, without the villages. The tribe of {color=#f6d6bd}Creeks{/color} already agreed to not step in, and if I were to tell everyone that {color=#f6d6bd}Thais{/color} wants to stain her hands through us, they would refuse twice.”
                '
                '(elah1 set)':
                    pass
        '“She’s a liar. Better to keep her at a distance.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s a liar. Better to keep her at a distance.”')
            $ description_thais_pcopinion = "dishonest"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without binding myself to any specific leader."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship += 2
            $ creeks_reputation += 1
            $ description_thais09 = "I was advised to have the druids on my side if I were to confront her."
            $ quest_ruins_10yclue07 = "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
            $ questionpreset = "elah1"
            menu:
                'He looks you in the eyes and rests the wooden frame on his stomach. “Aye, better to. After the things she did ten years ago, there’s no going back. My tribesfolk won’t ever agree to another one of her {i}pacts{/i}.”
                \n\n“If you want to get out of her plots unscarred, deal with {color=#f6d6bd}Orentius{/color} on your own, without the villages. The tribe of {color=#f6d6bd}Creeks{/color} already agreed to not step in, and if I were to tell everyone that {color=#f6d6bd}Thais{/color} wants to stain her hands through us, they would refuse twice.”
                \n\nHe puts the wood on the ground. “And better not to say anything to her, unless there are druids at your side.”
                 '
                '(elah1 set)':
                    pass
        '“She has her flaws, but she’s useful to me.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She has her flaws, but she’s useful to me.”')
            $ description_thais_pcopinion = "useful"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without binding myself to any specific leader."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship -= 1
            $ creeks_reputation += 0
            $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
            $ questionpreset = "elah1"
            menu:
                'He puts the frame on the workbench with a loud thud. “Don’t be an ape. If she’s agreeing to work with you, it means she gains more from it than you do. Follow this tyrant and be one of many souls who she’s have betrayed before you gain anything. And she won’t be reached by justice, behind her walls and guards,” he looks at the cuts on his hands.
                \n\n“If you want to get out of her plots unscarred, deal with {color=#f6d6bd}Orentius{/color} on your own, without the villages. The tribe of {color=#f6d6bd}Creeks{/color} already agreed to not step in, and if I were to tell everyone that {color=#f6d6bd}Thais{/color} wants to stain her hands through us, they would refuse twice.”
                '
                '(elah1 set)':
                    pass
        '“I enjoy her company.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I enjoy her company.”')
            $ description_thais_pcopinion = "friend"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without binding myself to any specific leader."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship -= 1
            $ creeks_reputation += 0
            $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
            $ quest_ruins_10yclue07 = "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
            $ questionpreset = "elah1"
            menu:
                'He frowns at the frame and raises it slightly, observing it with care. “Then you’re getting played, friend. There’s not a word, not a smile of that tyrant that isn’t meant to stab you in the back. We learned this ten years ago.” He rests the blocks of wood on his stomach and looks at you with pity. “Maybe cityfolk just find the same tongue. One that our parents left behind when they set off North.”
                \n\n“If you want to get out of her plots unscarred, deal with {color=#f6d6bd}Orentius{/color} on your own, without the villages. The tribe of {color=#f6d6bd}Creeks{/color} already agreed to not step in, and if I were to tell everyone that {color=#f6d6bd}Thais{/color} wants to stain her hands through us, they would refuse twice.”
                '
                '(elah1 set)':
                    pass
        '“I’m not sure.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not sure.”')
            $ description_thais_pcopinion = "notsure"
            $ quest_orentius_thais_description03a05 = "{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            $ elah_friendship += 0
            $ creeks_reputation += 0
            $ description_thais08 = "{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
            $ quest_ruins_10yclue07 = "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
            $ questionpreset = "elah1"
            menu:
                'He puts the frame on the workbench slowly. “Then you’re slow, and you’re getting played by a tyrant who {i}never{/i} hesitates, even if they should. After hwat she did ten years ago, my tribesfolk would refuse her twice. We’ve already discussed the trouble with {color=#f6d6bd}Orentius{/color} and we will {i}not{/i} step in.”
                '
                '(elah1 set)':
                    pass

label creekselah_about_asterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Asterion{/color} around?”')
    $ elah_about_asterion = 1
    $ questionpreset = "elah1"
    menu:
        'He halts his work and looks at you with an exaggerated frown. “That’s a weird question. You’re the first roadwarden I’ve seen in, well, this season, I think. Did you check in the western villages? You’ll get to {color=#f6d6bd}Howler’s Dell{/color} simply staying on the road.”
        \n\nHis right hand, still holding a tool, is now squeezing his stomach gently.
        '
        '(elah1 set)':
            pass
    label creekselah_about_asterion02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “People say that {color=#f6d6bd}Asterion{/color} has spent a lot of time in your village. You’re hiding something.”')
        $ elah_about_asterion = 2
        $ questionpreset = "elah1"
        $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
        menu:
            'He adjusts his shoulder cape and clears his throat with a grunt. “{i}People{/i}, aye? Well, there’s some truth to that, but {color=#f6d6bd}Asterion{/color} isn’t here, and we don’t know hwere he is. He took our coins, but for fair labor. He moved wares to other settlements, patrolled the roads, escorted an old woman to a druid and back. Did you know you can get good prices for iron at {color=#f6d6bd}Howler’s Dell{/color}, but even better at {color=#f6d6bd}Hwite Marshes{/color}?”
            \n\nSeeing your look, he turns away and rests his elbow on his workbench. “His plans are his own problem, and I’ve no reason to believe he wanted to be found. Nor can I help you.”
            '
            '(elah1 set)':
                pass
    label creekselah_about_asterion03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Be serious now, {color=#f6d6bd}Elah{/color}. I need to know what happened to {color=#f6d6bd}Asterion{/color}.”')
        $ elah_about_asterion = 3
        $ banditshideout_bandits_pchearedabout = 1
        $ quest_asterion_description12 = "{color=#f6d6bd}Elah{/color} told me that {color=#f6d6bd}Asterion{/color} was seeking something of great value, and {color=#f6d6bd}Glaucia{/color}, the leader of the bandits, was aiming to help him."
        $ description_glaucia11 = "According to {color=#f6d6bd}Elah{/color}, she was involved with {color=#f6d6bd}Asterion’s{/color} disappearance."
        $ renpy.notify("Journal updated: Find the Roadwarden")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        $ elah_locked = day
        menu:
            'He springs up, still holding his tools and demonstrating his threatening physique, and raises his voice. “I {i}am{/i} serious! I don’t know!” He looks behind him and even takes a step back, but with every few gestures his breath gets a bit slower.
            \n\n“He said there’s something of great value hidden in the wilderness, roadwarden. A treasure, I think. And that treasure would {i}change the North{/i}.” He rubs his forearms, but there is still tension in his shell. “He needed help we couldn’t give him, and told us to prepare for {color=#f6d6bd}Glaucia{/color} and her bandits to come for supplies. He paid for them upfront. But she never came, neither did he.”
            \n\nWhen he sits down again, he doesn’t look at you. “I never saw him like that before. He was tired and worried, friend. His words lacked confidence. It may very well be that something caught him. But {i}we{/i} weren’t a part of this. Now please, let me be.”
            '
            '“Very well.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                jump creeksafterinteraction01

    label creekselahaboutfindingasterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color} is dead. I found his shell.”')
        $ elah_about_asterion_found = 1
        $ creeks_reputation += 1
        $ elah_friendship += 1
        $ questionpreset = "elah1"
        menu:
            'He sits down. You consider walking away, but he finally speaks, though with hesitation. “I’ll pass this story to the tribe... Though in a bit of a {i}gentler{/i} way,” he sighs and looks at your boots. “I can’t believe he found nothing. Hwy would he listen to a legend? Didn’t he know there’s so many of them they can’t all be true?” He adjusts his jacket, scratching his side with an absent look. “To think he told us nothing, and ‘bout such’ goblin-brained thing...” He raises his eyes slightly, and seeing his clenched lips, you realize there’s nothing else he can tell you about it.
            '
            '(elah1 set)':
                pass

label elah_about_creeks01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This village isn’t much older than you are... What’s its story?”')
    $ elah_about_creeks += 1
    $ quarters += 1
    $ description_galerocks09 = "I heard that it was the people of {color=#f6d6bd}Gale Rocks{/color} who helped establish {color=#f6d6bd}Creeks{/color}, and they used to be of a much more welcoming nature."
    menu:
        'He proudly raises a carving knife and gestures for you to look around. “It may be a young village, but there’s a lot to say!” While his story is bloated with names, relationships, a step-by-step description of the growth of the settlement, and bothersome creatures, you get the gist of it.
        \n\nThe settlers arrived here twenty-five years ago, soon after one of The Ten Cities had fallen to The Southern Invasion. Most of them came from the capital, while some joined them along the way. They soon came to realize that none of the villages had enough space or the will to host a few dozen refugees. The folks of {color=#f6d6bd}Gale Rocks{/color} used to have a much kinder attitude toward strangers than they do now, and they offered the newcomers to stay at the beach behind their village.
        \n\nYet there was nothing for them to eat other than what they caught in the salt waters. They soon started their search for a land remote enough to not compete with the locals, and with the help of kind folks from “{color=#f6d6bd}Gale Rocks{/color}, {color=#f6d6bd}Hwite Marshes{/color}, {color=#f6d6bd}Old Págos{/color}... and others,” as {color=#f6d6bd}Elah{/color} vaguely states, they received enough wood and tools to turn a scrap of this plateau into a clearing, then a camp, a hamlet, and finally - a village.
        '
        'I try to pay attention.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to pay attention.')
            jump elah_about_creeks02
        '“Fascinating stuff!”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fascinating stuff!”')
            label elah_about_creeks02:
                $ quarters += 1
                menu:
                    'The tale is assisted by walking around the village, introducing you to the original settlers or their offspring, and showing you some of the {i}treasures{/i} displayed in the house of gatherings - a unicorn’s horn found at the heart of the woods; a blue rock that’s shaped and hollow like an egg, and is darker inside; an arrow that “hit a frightape in an eye, and knocked it down!” Behind each of them, there are names, stories, and memories.
                    \n\nAt the very end, {color=#f6d6bd}Elah{/color} leads you back to his workbench, holding a hand on his conspicuous stomach. To give his throat some rest, he turns the topic around. “And hwat are the folks in {color=#f6d6bd}Hovlavan{/color} like, friend? {color=#f6d6bd}Foggy{/color} says there are {i}thousands{/i} of souls at the capital, and one can go their entire life still finding new faces in the crowd.”
                    '
                    '“It may be so, but {i}my{/i} city feels lonely. There are many people around, but all of them are too busy with their duties to share their lives with others.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be so, but {i}my{/i} city feels lonely. There are many people around, but all of them are too busy with their duties to share their lives with others.”')
                        menu:
                            'He nods. “A few years back we had a visitor who hoped to move in with us, saying they were a {i}stranger in their own land{/i}. We agreed, and they departed to {color=#f6d6bd}Hovlavan{/color} to pick up their things, but never came back.”
                            \n\nHe sits down next to his tools. “Does this bother you? This loneliness?”
                            '
                            '“Very much so.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very much so.”')
                                $ elah_friendship += 1
                                $ hovlavan_humaninteraction = "trueloneliness"
                                $ questionpreset = "elah1"
                                menu:
                                    '“So your soul is healthy, and close to ours,” his eyes and voice are solemn, at first, but his bright smile returns quickly. He adjusts his shoulder cloak and asks if you need anything else.
                                    '
                                    '(elah1 set)':
                                        pass
                            '“I’ve learned to live with that. It’s already a part of my nature.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve learned to live with that. It’s already a part of my nature.”')
                                $ hovlavan_humaninteraction = "okloneliness"
                                $ questionpreset = "elah1"
                                menu:
                                    '“Aye, I couldn’t. I {i}need{/i} these folks.” He looks at a few young people on the opposite side of the square. They were also observing the two of you, and now give you awkward smiles. {color=#f6d6bd}Elah{/color} adjusts his shoulder cloak and asks if you need anything else.
                                    '
                                    '(elah1 set)':
                                        pass
                    '“People spend time with their families and close friends, especially ones they work with. They are close to each other, but no soul knows what happens behind doors. In the evenings, the streets feel empty.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “People spend time with their families and close friends, especially ones they work with. They are close to each other, but no soul knows what happens behind doors. In the evenings, the streets feel empty.”')
                        $ hovlavan_humaninteraction = "onlyfamilies"
                        $ questionpreset = "elah1"
                        menu:
                            '“Here, folks stay inside only to sleep or shag, and even that’s not a rule,” he adjusts his shoulder cloak and smiles. “That’s the only way I know, but I like it.”
                            '
                            '(elah1 set)':
                                pass
                    '“It’s hard to get to know new people when everyone’s so busy, but kids spend a lot of time together, and build long-time friendships.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s hard to get to know new people when everyone’s so busy, but kids spend a lot of time together, and build long-time friendships.”')
                        $ hovlavan_humaninteraction = "closefriendships"
                        $ questionpreset = "elah1"
                        menu:
                            '“Being an outsider must be harsh, then. Especially a {i}poor{/i} one,” lost in his thoughts, he reaches for the piece of wood he was working with. “On the other hand, I don’t envy those who bind themselves to folks that may, or may not, turn into beasts one day. Here,” he looks around, “ties tighten and loosen with time, and change isn’t so scary.”
                            '
                            '(elah1 set)':
                                pass
                    '“One can easily find groups to hang out with. People shop together, work, take baths, pray, and when one has nothing to do in the evening, they just go outside and seek company. It’s not easy to build a strong friendship, though.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “One can easily find groups to hang out with. People shop together, work, take baths, pray, and when one has nothing to do in the evening, they just go outside and seek company. It’s not easy to build a strong friendship, though.”')
                        $ hovlavan_humaninteraction = "thinfriendships"
                        $ elah_friendship += 1
                        $ questionpreset = "elah1"
                        menu:
                            '“Other than the last part, it sounds similar to our way of living. Folks stay inside only to sleep or shag, and even that’s not a rule,” he adjusts his shoulder cloak and smiles. “But we also form bonds, one big family and all.”
                            '
                            '(elah1 set)':
                                pass
                    '“Hard to say. The merchants are getting richer, the priests have their games, craft guilds decide who goes in and out, and the workers have to compete. There are no monsters on the streets, at least not every day, but there is distrust in many souls.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hard to say. The merchants are getting richer, the priests have their games, craft guilds decide who goes in and out, and the workers have to compete. There are no monsters on the streets, at least not every day, but there is distrust in many souls.”')
                        $ hovlavan_humaninteraction = "distrust"
                        menu:
                            'He looks at you with a sigh. “I know folks go there to be safe... But hwat you describe, friend, sounds like a place darker than the heart of the woods.”
                            '
                            '“It’s not... if you’re at the top.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s not... if you’re at the top.”')
                                $ elah_friendship -= 1
                                $ hovlavan_humaninteraction = "okdistrust"
                                $ questionpreset = "elah1"
                                menu:
                                    'He adjusts his shoulder cloak and reaches for the next plank, without saying anything.
                                    '
                                    '(elah1 set)':
                                        pass
                            '“It’s exactly that.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very much so.”')
                                $ elah_friendship += 1
                                $ hovlavan_humaninteraction = "truedistrust"
                                $ questionpreset = "elah1"
                                menu:
                                    '“So your soul is healthy, and close to ours,” his eyes and voice are solemn at first, but his bright smile returns quickly. He adjusts his shoulder cloak and asks if you need anything else.
                                    '
                                    '(elah1 set)':
                                        pass

label elah_about_peninsula01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the peninsula.”')
    $ elah_about_peninsula = 1
    $ questionpreset = "elah1"
    menu:
        '“Our tribe won’t be much of a help there,” he admits while judging the harsh surface of a small plank. “It was our parents who did all the traveling, and they did so hwile we were kids, or not yet born. Most of them are already gone, and most of us travel no farther than to Foggy’s, and only when we have to.”
        '
        '(elah1 set)':
            pass

label elah_about_greenmountaintribe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”')
    $ elah_about_greenmountaintribe = 1
    $ questionpreset = "elah1"
    menu:
        'A chisel falls out of his hand. When he reaches for it, he looks around, making sure there’s no one around. “Not really. When I was a kid, I saw the older tribesfolk speaking with them, in the Old Speech, I think. They aren’t around anymore, but I’ve heard we owe them a lot.”
        '
        '(elah1 set)':
            pass

label creekselahonefren01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think about {color=#f6d6bd}Efren{/color}?”')
    $ elah_about_efren = 1
    if elah_friendship+appearance_charisma < 4:
        $ questionpreset = "elah1"
        menu:
            'He gives you a surprised look. “I care for him deeply, he’s brave and has a big heart. But both of our pasts were rough, I don’t think you need to hear ‘bout them.”
            '
            '(elah1 set)':
                pass
    else:
        $ elah_about_efren = 2
        if efren_about_elah == 2 and elah_about_efren == 2:
            $ creeks_reasonstojoin_beastattacks += 1
        $ questionpreset = "elah1"
        menu:
            'He gives you a surprised look. “I care for him deeply, he’s brave and has a big heart... But his soul is clouded. He thinks we have no right to waste hwat the dead have sacrificed for our sake, and that we disrespect them by staying {i}weak{/i}, but all of it is just a cloak that hides him. He cares not ‘bout respect, but ‘bout his guilt.”
            \n\nIt takes a bit of convincing before he explains what he means by that. “Our father died from claws, our mother from a bad birth. We used to have five brothers and sisters, all of them dead now. Some maybe could have been saved, but not all, and surely not by being {i}stronger{/i}. Yet {color=#f6d6bd}Efren{/color} keeps thinking he had every opportunity to fix the tragedies, and he’s to blame for letting them down. Him and I, both,” he falls silent. “But at least {i}I{/i} put my shame to use,” he reaches for his tools again.
            \n\n“We already have everything that we need. A beautiful home, enough food, fewer beasts than ever. It’s going to be a rough lifetime for us,” he takes a swing, “but our kids will be fine.”
            '
            '(elah1 set)':
                pass
    label creekselahonefren02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was wondering about {color=#f6d6bd}Efren{/color}...”')
        $ elah_about_efren = 2
        if efren_about_elah == 2 and elah_about_efren == 2:
            $ creeks_reasonstojoin_beastattacks += 1
        $ questionpreset = "elah1"
        menu:
            'He slowly starts to speak, making sure his tribesfolk don’t eavesdrop. “His soul is clouded. He thinks we have no right to waste hwat the dead have sacrificed for our sake, and that we disrespect them by staying {i}weak{/i}, but all of it is just a cloak that hides him. He cares not ‘bout respect, but ‘bout his guilt.”
            \n\nIt takes a bit of convincing before he explains what he means by that. “Our father died from claws, our mother from a bad birth. We used to have five brothers and sisters, all of them dead now. Some maybe could have been saved, but not all, and surely not by being {i}stronger{/i}. Yet {color=#f6d6bd}Efren{/color} keeps thinking he had every opportunity to fix the tragedies, and he’s to blame for letting them down. Him and I, both,” he falls silent. “But at least {i}I{/i} put my shame to use,” he reaches for his tools again.
            \n\n“We already have everything that we need. A beautiful home, enough food, fewer beasts than ever. It’s going to be a rough lifetime for us,” he takes a swing, “but our kids will be fine.”
            '
            '(elah1 set)':
                pass

label elah_about_himself01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I imagine being a carpenter in this part of the realm isn’t easy.”')
    $ elah_about_himself = 1
    $ quarters += 1
    menu:
        '“You have a healthy imagination,” he rests his elbow on the workbench and smiles. “I have patience, and I’m getting better with tools, and these are some {i}shoddy tools{/i},” he says singingly, and it’s hard to disagree with him. They have been used for many years, with only the wooden parts being somewhat in shape since they seem to have been recently replaced. The steel chisels and saws are jagged and dull, the hammers and axes are made of stone. “Some of them were brought here by the settlers, and we can’t buy any more right now. There’s work to be done, but I do have a plan.”
        \n\nYou ask him to explain, and he’s all too eager to do so. He enters the nearby house and shows you his more successful works, each of which has some shortcomings, noticeable even to a layperson. A bowl engraved with fish was poorly planned, with animals too large to fit into the entire space, and so a part of it is blank; a simple relief of two naked people in their embrace looks almost believable, but the legs are in one case too long, and in the other - too short; one chair has a broken leg, and the remaining three show that they are a bit too ambitiously shaped, and got dangerously thin; the chest seems fine, but equipment sticks out of it, and the man acknowledges that he wrongly estimated the required size.
        '
        '“So you want to be an artist.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want to be an artist.”')
            $ questionpreset = "elah1"
            menu:
                '“Better! I want to turn pots, cups, weapons, cupboards... Everyday stuff into things of beauty!” Seeing your look, he pats his stomach. “I know I’m far from mastering it, but trust me, these are so much better than the ones I did this winter, and I started only three years ago!” His pride makes him look even larger, especially in the shoulders. “There aren’t many carpenters in the peninsula, folks do things for their own use, but I’ll be a specialist, it’s the {i}city thing{/i}, {color=#f6d6bd}Foggy{/color} told me so. Not just a jointer, but someone who does only a few things, but better than others. The tribe supports me with food and time, and I’ll pay them back with dragon bones. And prettier houses!”
                \n\nWhen he leads you outside, you start to share some of his excitement, but most of it dwindles away after you sit down at his workbench again - on wobbly stools, surrounded by broken planks and crude tools.
                '
                '(elah1 set)':
                    pass

label creekselahontraps01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say you would need to place some traps in an old tunnel...”')
    $ elah_about_traps = 1
    $ questionpreset = "elah1"
    menu:
        '“Do I look like someone who crawls through tunnels?” He smiles and pats his stomach. “You want {color=#f6d6bd}Efren{/color}, he catches everything that doesn’t fly or swim.”
        '
        '(elah1 set)':
            pass

label elah_about_makingalanternALL:
    label elah_about_makingalantern01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a wooden lantern, one useful for an adventurer.”')
        $ elah_about_makingalantern = 1
        if (elah_friendship+appearance_charisma) >= elah_about_makingalantern_threshhold:
            menu:
                '“Dreaming of caves and treasures?” He glances at the nearest pile of planks. “I {i}should{/i} have some glue and leather to spare, but making a lantern would take me half a day, and I’ve got a lot of sawing ahead.” He points at a broken chair behind him with his thumb. “If you {i}really{/i} need it, friend, you can give it a try. I’ll lead you through the difficult steps. But it will take us almost half a day”
                '
                'It’s too late for that. (disabled)' if quarters > (world_daylength-28):
                    pass
                '“Let’s get to it.”' if quarters <= (world_daylength-28):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get to it.”')
                    jump elah_about_makingalantern03
                '“I’ll let you know when I’m ready.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know when I’m ready.”')
                    $ questionpreset = "elah1"
                    menu:
                        '“No hurry, believe me,” he chuckles.
                        '
                        '(elah1 set)':
                            pass
        else:
            $ questionpreset = "elah1"
            menu:
                '“Dreaming of caves and treasures?” He glances at the nearest pile of planks. “I {i}should{/i} have some glue and leather to spare, but making a lantern would take me half a day, and I’ve got a lot of sawing ahead.” He points at a broken chair behind him with his thumb. “Maybe another time.”
                '
                '(elah1 set)':
                    pass

    label elah_about_makingalantern02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have time now. Want to help me build a lantern?”')
        menu:
            'He spares you a shrug. “If you {i}really{/i} need it, friend, you can give it a try. I’ll lead you through the difficult steps. But it will take us almost half a day.”
            '
            'It’s too late for that. (disabled)' if quarters > (world_daylength-28):
                pass
            '“Let’s get to it.”' if quarters <= (world_daylength-28):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get to it.”')
                jump elah_about_makingalantern03
            '“I’ll let you know when I’m ready.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know when I’m ready.”')
                $ questionpreset = "elah1"
                menu:
                    '“No hurry, believe me,” he chuckles.
                    '
                    '(elah1 set)':
                        pass

    label elah_about_makingalantern03:
        $ elah_about_makingalantern_made = 1
        $ quarters += 24
        $ item_lantern = 1
        $ elah_friendship += 1
        $ renpy.notify("You built a lantern.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You built a lantern.{/i}')
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
        $ questionpreset = "elah1"
        menu:
            'Cutting and shaping the slats seems to go on without end, and while {color=#f6d6bd}Elah’s{/color} instructions help you keep your hands safe, the blunt, jagged tools are merciless. You have little to show after the first hour, and the carpenter puts his own work aside. “At such a pace you’ll have to return to this tomorrow. Let’s try something different.”
            \n\nHe leads you into the chamber storing all of his projects, most of them crooked or half-completed, and invites you to search through a chest filled with wooden disks, boards, and rods, with even more trash stored behind it. “Some of them {i}must{/i} be salvageable,” his chuckle carries a hint of irritation, but indeed, you both leave the room with many pieces that will take little hardly any sawing.
            \n\nThe remaining adjustments still present a challenge, but, having the locals to chat and a warm nettle tisane always at hand, you stick the last piece of parchment to the frame much sooner than you expected.
            '
            '(elah1 set)':
                pass

label creekselahonquest_easternpathALL:
    label creekselahonquest_easternpath01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any work for a roadwarden?”')
        if not creeks_feast:
            $ custom1 = "pile of wood"
        else:
            $ custom1 = "pile of ash"
        menu:
            '“But of course!” He stands up with a bright smile, walks away, leaps over one of the log-made tables and looks for something in the [custom1]. “In this part of The Land there’s always going to be something to do for a roadwarden!” He straightens up with a piece of charred wood in his hand and gets back to you. As he draws black lines on the workbench, he mentions a few names - {color=#f6d6bd}Creeks{/color}, {color=#f6d6bd}Foggy’s{/color}, “{color=#f6d6bd}Gale Rocks{/color} there”, “Here’s the lake...” The map is simplistic and doesn’t align with your own understanding of local distances, but you follow his description without issues.
            \n\n“The path from here to the South is getting too wild for us,” he repines, making another few strokes. “The merchants travel through the other route, through {color=#f6d6bd}Howler’s Dell{/color}, passing by {color=#f6d6bd}Old Págos{/color} and {color=#f6d6bd}Hwite Marshes{/color}. Once they reach {color=#f6d6bd}Foggy{/color}, they already have full stomachs and many deals closed. And when they travel back, they visit the same places again... Folks already know that trading here takes a long time.”
            '
            '“So you want me to give them an option to get to you first and move west without backtracking, and do so all by myself... How, exactly?”':
                label creekselahonquest_easternpath01part2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want me to give them an option to get to you first and west without backtracking, and do so all by myself... How, exactly?”')
                    $ quest_easternpath_description01 = "{color=#f6d6bd}Elah{/color} wants me to get to know the roads that connect {color=#f6d6bd}Foggy Lake{/color} with both {color=#f6d6bd}the western crossroads{/color} and {color=#f6d6bd}the southern crossroads{/color} and do as much as I can to make them more secure, or at least bring him news about what can be done to make them so."
                    if not quest_easternpath:
                        $ quest_easternpath = 1
                        $ renpy.notify("New entry: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Eastern Path{/i}')
                    else:
                        $ quest_easternpath = 1
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    menu:
                        '“Well, I’m sure you can find {i}some{/i} help!” He pats his stomach without noticing that he leaves a few black dots on his leather jacket. “There’s a few things you could do. Follow the eastern road and see if it’s clear. Are there any safe shelters left? Any blockades to get rid of? Is there an overgrown path to burn? Maybe see if the road from here to the western crossroads is safe, or if the carts could get through the heart of the woods, if you’re brave enough? I hope you’re a soul with sage judgement.”
                        \n\nSeeing your puzzled look, he rests his palms on the table with a shy smile. “I know I’m vague, but I bet you already know more ‘bout these roads than I do, friend.” His eyes return to the map and after a moment of hesitation he rubs an uneven line with his thumb.
                        '
                        '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                            jump creekselah_quest_easternpath_reward01
                        '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                            jump creekselah_quest_easternpath_reward02
                        '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                            jump creekselah_quest_easternpath_lies01
                        '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                            jump creekselahonquest_easternpathhints01
                        '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                            jump creekselahonquest_easternpathhints02
                        '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                            jump creekselah_quest_easternpath_whynotwest01
                        '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                            $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                            jump creekselahonquest_easternpath01after
                        '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                            $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                            jump creekselahonquest_easternpath01after

    label creekselahonquest_easternpath01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard you have some issues with the eastern path.”')
        if not creeks_feast:
            $ custom1 = "pile of wood"
        else:
            $ custom1 = "pile of ash"
        $ elah_friendship += 1
        menu:
            'At first he gives you a bright smile, but then nods with a sigh. “Aye, aye. So our issues are so clear that folks gossip on them? I’m glad you came to our help, friend, but it doesn’t feel right to admit we need help from an outsider.” He stands up slowly, walks away, and leaps over one of the log-made tables and looks for something in the [custom1]. “In this part of The Land there’s always going to be something to do for a roadwarden!” He straightens up with a piece of charred wood in his hand and gets back to you. As he draws black lines on the workbench, he mentions a few names - {color=#f6d6bd}Creeks{/color}, {color=#f6d6bd}Foggy’s{/color}, “{color=#f6d6bd}Gale Rocks{/color} there”, “Here’s the lake...” The map is simplistic and doesn’t align with your own understanding of local distances, but you follow his description without issues.
            \n\n“The path from here to the South is getting too wild for us,” he repines, making another few strokes. “The merchants travel through the other route, through {color=#f6d6bd}Howler’s Dell{/color}, passing by {color=#f6d6bd}Old Págos{/color} and {color=#f6d6bd}Hwite Marshes{/color}. Once they reach {color=#f6d6bd}Foggy{/color}, they already have full stomachs and many deals closed. And when they travel back, they visit the same places again... Folks already know that trading here takes a long time.”
            '
            '“So you want me to give them an option to get to you first and move west without backtracking, and do so all by myself... How, exactly?”':
                jump creekselahonquest_easternpath01part2

    label creekselah_quest_easternpath_reward01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my pay.”')
        $ elah_quest_easternpath_reward = 1
        $ quest_easternpath_description02 = "I’ll receive dragon bones depending on what I accomplish."
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        menu:
            '“That depends on hwat you’re ‘bout to do, aye? The tribe has but a few dragons,” to confirm his words, he enters the nearby house, from which he picks up an old, wooden case, crude in shape and with an unsightly engraving of a three-headed hydra on its lid. Inside it, you see maybe two dozen dragon bones. “Let’s say you’ll get a dragon for any news ‘bout cleared or blocked areas, and more if it takes {i}real{/i} effort from you.”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselah_quest_easternpath_reward02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want me to act first and pick up my reward after? You’re playing with my patience.”')
        $ elah_quest_easternpath_rewardisnotfair = 1
        menu:
            '“Are you... Not paid by the rich folks from {color=#f6d6bd}Hovlavan{/color}?” His voice once again gets apologetic. “I believe hwat I’m asking you for is your very job. I just try to {i}motivate you{/i} to do it well, roadwarden. I’m not your master, you’ll do as you please.”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselah_quest_easternpath_lies01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can you know if I’ll be honest with you?”')
        $ elah_quest_easternpath_lies = 1
        menu:
            '“I...” He looks at you in silence, then clenches his stomach. “Can’t, most likely? But the more news you bring us, the farther away from the village our foragers and hunters will be willing to roam. {color=#f6d6bd}Foggy’s boys{/color} as well, I expect. Sooner or later, the truth will surface, and I’ll advise my tribe to take a lesson from hwatever we’re ‘bout to find.”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselahonquest_easternpathhints01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you like me to start?”')
        $ elah_quest_easternpath_hint1 = 1
        menu:
            '“Go to the shelters set just at the side of the roads. There’s a ruined campsite west of {color=#f6d6bd}Foggy’s{/color},” he makes a small circle on his {i}map{/i}, “or you could go south, to a cabin our elders built,” he makes a larger square. “It’s halfway from here to the river. Take a look around, see hwat’s their condition, if there are any beasts around. You can handle a few small creatures, can’t you?”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselahonquest_easternpathhints02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So two shelters, and then... You just want me take care of anything I find?”')
        $ elah_quest_easternpath_hint2 = 1
        $ description_asterion13 = "According to {color=#f6d6bd}Elah{/color}, Asterion was a very confident and self-reliant person."
        menu:
            'He laughs, but not with his eyes. “Forgive me, friend, but you don’t sound like someone with much experience behind them. You’re nothing like {color=#f6d6bd}Asterion{/color}. He took pride in his self-reliance.”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselah_quest_easternpath_whynotwest01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”')
        $ elah_quest_easternpath_whynotwest = 1
        menu:
            '“They can’t be trusted, especially {i}some{/i} of them,” he crosses the western side of his map with a long, thin line. “Even a paved route would force merchants to add a day of pointless travel to their plans, and that’s a big loss in their trade. Having our path clear gives everyone more options, and more convenience.”
            '
            '“You forgot to mention my pay.”' if not elah_quest_easternpath_reward:
                jump creekselah_quest_easternpath_reward01
            '“So you want me to act first and pick up my reward after? You’re playing with my patience.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                jump creekselah_quest_easternpath_reward02
            '“How can you know if I’ll be honest with you?”' if not elah_quest_easternpath_lies:
                jump creekselah_quest_easternpath_lies01
            '“Where would you like me to start?”' if not elah_quest_easternpath_hint1:
                jump creekselahonquest_easternpathhints01
            '“So two shelters, and then... You just want me take care of anything I find?”' if elah_quest_easternpath_hint1 and not elah_quest_easternpath_hint2:
                jump creekselahonquest_easternpathhints02
            '“Wouldn’t it be better for you to put work into the western road? You could split the labor with the other settlements.”' if not elah_quest_easternpath_whynotwest:
                jump creekselah_quest_easternpath_whynotwest01
            '“We have a deal.”' if elah_quest_easternpath_reward and not elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                $ custom1 = "He flashes you a wide smile and pats his stomach. “You won’t regret this!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after
            '“I don’t like the way you handle the payment... But fine.”' if elah_quest_easternpath_rewardisnotfair:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the way you handle the payment... But fine.”')
                $ custom1 = "He lets out a sigh of relief and squeezes his stomach. “You almost made me worried there, friend!” He then throws away the charred wood, returns to his stool, and looks for his tools."
                jump creekselahonquest_easternpath01after

    label creekselahonquest_easternpath01after:
        menu:
            '[custom1]
            '
            '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                jump creekselahaboutquesteasternroadduskfoxes01
            '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                jump creekselahaboutquesteasternroadduskfoxes02
            'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                pass
            'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                pass
            'I still need to look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                pass
            '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                jump creekselahaboutquesteasternroadclearedbrook01
            'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                pass
            '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                jump creekselahaboutquesteasternroadhunterscabin01
            'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                pass
            '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                jump creekselahaboutquesteasternroadstonebridge01
            '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                jump creekselahaboutquesteasternroadstonebridge02
            'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                pass
            '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                jump creekselahaboutquesteasternroadwanderer01
            '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                jump creekselahaboutquesteasternroadwatchtower01
            '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                jump creekselahaboutquesteasternroadwatchtower01alt
            '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                jump creekselahaboutquesteasternroad_eudociadeal01
            'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                pass
            'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                pass
            '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                jump creekselahaboutquesteasternroaddolmen01
            '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                jump creekselahaboutquesteasternroadfallentree01
            '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                jump creekselahaboutquesteasternroadfallentree02
            'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                pass
            'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                pass
            'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                pass
            'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                pass
            '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                jump creekselahaboutquesteasternroadshortcut01
            '“I’ll let you know if there’s anything else.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                jump creekselahafterinteraction01

    label creekselahonquest_easternpath02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the eastern path...”')
        menu:
            '“Did you face any troubles?”
            '
            '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                jump creekselahaboutquesteasternroadduskfoxes01
            '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                jump creekselahaboutquesteasternroadduskfoxes02
            'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                pass
            'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                pass
            'I still need to look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                pass
            '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                jump creekselahaboutquesteasternroadclearedbrook01
            'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                pass
            '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                jump creekselahaboutquesteasternroadhunterscabin01
            'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                pass
            '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                jump creekselahaboutquesteasternroadstonebridge01
            '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                jump creekselahaboutquesteasternroadstonebridge02
            'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                pass
            '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                jump creekselahaboutquesteasternroadwanderer01
            '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                jump creekselahaboutquesteasternroadwatchtower01
            '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                jump creekselahaboutquesteasternroadwatchtower01alt
            '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                jump creekselahaboutquesteasternroad_eudociadeal01
            'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                pass
            'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                pass
            '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                jump creekselahaboutquesteasternroaddolmen01
            '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                jump creekselahaboutquesteasternroadfallentree01
            '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                jump creekselahaboutquesteasternroadfallentree02
            'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                pass
            'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                pass
            'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                pass
            'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                pass
            '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                jump creekselahaboutquesteasternroadshortcut01
            '“I’ll let you know if there’s anything else.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                jump creekselahafterinteraction01

    label creekselahonquest_easternpath03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have made some additional progress with the eastern path.”')
        menu:
            '“There were even more issues? I’m listening.”
            '
            '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                jump creekselahaboutquesteasternroadduskfoxes01
            '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                jump creekselahaboutquesteasternroadduskfoxes02
            'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                pass
            'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                pass
            'I need to still look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                pass
            '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                jump creekselahaboutquesteasternroadclearedbrook01
            'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                pass
            '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                jump creekselahaboutquesteasternroadhunterscabin01
            'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                pass
            '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                jump creekselahaboutquesteasternroadstonebridge01
            '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                jump creekselahaboutquesteasternroadstonebridge02
            'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                pass
            '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                jump creekselahaboutquesteasternroadwanderer01
            '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                jump creekselahaboutquesteasternroadwatchtower01
            '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                jump creekselahaboutquesteasternroadwatchtower01alt
            '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                jump creekselahaboutquesteasternroad_eudociadeal01
            'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                pass
            'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                pass
            '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                jump creekselahaboutquesteasternroaddolmen01
            '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                jump creekselahaboutquesteasternroadfallentree01
            '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                jump creekselahaboutquesteasternroadfallentree02
            'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                pass
            'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                pass
            'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                pass
            'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                pass
            'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                pass
            '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                jump creekselahaboutquesteasternroadshortcut01
            '“I’ll let you know if there’s anything else.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                jump creekselahafterinteraction01

    label creekselahaboutquesteasternroadduskfoxes01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”')
        $ creeks_reputation += 1
        $ elah_friendship += 1
        $ quarters += 1
        menu:
            '“{i}Dusk foxes{/i}?” After he meets your silence, he carries on. “I don’t know hwat that is.”
            \n\nYou describe their looks and the threat they present as {color=#f6d6bd}Elah{/color} observes the clouds, sometimes asking you to explain more. He finally taps his stomach. “Well, better than a tribe of goblins! And hwat ‘bout the ruins? Is the wood standing strong?”
            \n\nHe thinks about your brief tale and looks inside his wooden case. “I admit, restoring this place right away would be a waste of time and effort. We may need your help with it, but maybe next spring, or even the one after that. I’ll give you one dragon for the news, and another two for handling the... {i}foxes{/i}.”
            '
            '“Fair.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fair.”')
                $ coins += 3
                show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                $ quest_easternpath_points += 2
                $ quest_easternpath_description03a = "I received my reward for getting rid of the dusk foxes."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadduskfoxes02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”')
        $ creeks_reputation += 0
        $ elah_friendship += 1
        menu:
            '“{i}Dusk foxes{/i}?” After he meets your silence, he carries on. “I don’t know hwat that is.”
            \n\nYou describe their looks and the threat they present as {color=#f6d6bd}Elah{/color} observes the clouds, sometimes asking you to explain more. He finally squeezes his cloak and reaches for a coin that’s been resting on the workbench. “Well, sounds not as dangerous as a tribe of goblins, but it may be better for us to hunt them down in spring... We may need your help then. For now, a single dragon bone will be fair pay for the news.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                $ coins += 1
                show screen notifyimage( "Journal updated: The Eastern Path.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description03aalt = "I received my reward for bringing news about the dusk foxes."
                jump creekselahonquest_easternpathcalculatingresults00
            '“...Sure.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Sure.”')
                $ coins += 1
                show screen notifyimage( "Journal updated: The Eastern Path.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description03aalt = "I received my reward for bringing news about the dusk foxes."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadclearedbrook01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve restored the brook ford that connects the eastern road with the heart of the forest.”')
        $ creeks_reputation += 1
        $ elah_friendship += 1
        menu:
            '“Aye, I know the place. I don’t think we’re going to see that many wagons going through there in the next few seasons, but it must have been quite a few hours of work for a single shell. And quite close to the beasts...” You realize he’s not as much addressing you as thinking out loud while reaching for the wooden case. His fingers play with the contents for a bit, until he takes two dragon bones out of it. “One for the labor, another one for the threat. You must say, not too bad for carrying rocks.”
            '
            'I smile. “True, true.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “True, true.”')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description04a = "I received my reward for fixing the brook ford leading to the heart of the forest."
                jump creekselahonquest_easternpathcalculatingresults00
            'I scowl at him without a word.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scowl at him without a word.')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description04a = "I received my reward for fixing the brook ford leading to the heart of the forest."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadshortcut01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spent a lot of time in the heart of the woods. Do you want to hear about it?”')
        $ creeks_reputation += 1
        $ elah_friendship += 2
        $ quarters += 1
        menu:
            'He tilts his head left and right, then reaches for a single dragon bone from the case. “I mean, hwy not. Surprise me.”
            \n\nYour tale starts disjointed, with mentions of various creatures and paths, but you then get back to the beginning, describing the main route and the way you cleared it, but also the more treacherous turns. {color=#f6d6bd}Elah’s{/color} expression keeps swinging between approval and disbelief, and once you’re done, he reaches for yet another coin. “Quite a life you’re leading, I’d say.”
            '
            '“It could be worse.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It could be worse.”')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description11 = "I received my reward for sharing the detailed description of the shortcut."
                jump creekselahonquest_easternpathcalculatingresults00
            '“You don’t know the half of it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t know the half of it.”')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description11 = "I received my reward for sharing the detailed description of the shortcut."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadhunterscabin01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There was a big spider at the hunter’s cabin, but it’s gone now.”')
        $ creeks_reputation += 0
        $ efren_friendship += 1
        $ quarters += 1
        menu:
            'He observes your cheeks and hands, then smiles. “I’m glad to see you’re fine, friend. How’s the cabin doing?”
            \n\nYou answer him a few times and he stretches his arms, then puts his hands on the back of his head. His eyes are absent. “So it will be an easy restoration, maybe a few logs to swap, and the roof won’t do much good anymore...”
            \n\nIt takes your pronounced grunt for him to blink a few times and raise the lid of the case. “One for the news,” he puts the first dragon on the tabletop, then another one next to it. “And this one for taking care of the beast.”
            '
            'It’s not a fair price, but I let it go. “Thanks a lot.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not a fair price, but I let it go. “Thanks a lot.”')
                $ elah_friendship += 1
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description05a = "I received my reward for removing the spider from the hunter’s cabin."
                jump creekselahonquest_easternpathcalculatingresults00
            '“Come on, {color=#f6d6bd}Elah{/color}. I could have died in its trap.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, {color=#f6d6bd}Elah{/color}. I could have died in its trap.”')
                if (elah_friendship+creeks_reputation-appearance_price) >= 10:
                    $ coins += 3
                    show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                    $ quest_easternpath_points += 1
                    $ quest_easternpath_description05a = "I received my reward for removing the spider from the hunter’s cabin."
                    menu:
                        'After a few breaths, he reaches for another dragon.
                        '
                        '“Thanks.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                            jump creekselahonquest_easternpathcalculatingresults00
                else:
                    $ coins += 2
                    show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                    $ quest_easternpath_points += 1
                    $ quest_easternpath_description05a = "I received my reward for removing the spider from the hunter’s cabin."
                    menu:
                        'After a few breaths, he frowns. “Spiders aren’t that much of a threat, roadwarden. They even crawl into our houses from time to time.”
                        '
                        'I shake my head. “You say that because you haven’t seen it. We’ll see.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake my head. “You say that because you haven’t seen it. We’ll see.”')
                            jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadstonebridge01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I cleared the bushes leading east of the old stone bridge.”')
        menu:
            'His eyes widen and he looks left and right, then whispers. “Hwy would you do such’ thing? Someone may now think there’s a path there!”
            '
            '“Uhm... Is that really an issue?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Uhm... Is that really an issue?”')
                $ quest_easternpath_description06a = "I was asked to place a new sign at the path leading east of the old stone bridge."
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ item_signpost = 1
                $ quarters += 1
                $ elah_friendship -= 1
                $ description_greenmountaintribe08 = "The locals have made a pact with other villages that’s meant to keep The Tribe’s presence a secret."
                menu:
                    '“Shit,” he reacts both to your question and the awkward cut he made with his chisel. He puts away the tool loudly. “Folks aren’t supposed to go to {color=#f6d6bd}The Green Mountain{/color}! We’ve made a pact to leave them alone. And hwat, you think there’s a trader out there who’ll climb up the mountain?” He stands up, accompanying his rising voice. “Next time think before you act!”
                    \n\nAfter a few minutes, he returns with a wooden plank, but doesn’t meet your eyes. “I’m sorry, friend, forgive my cowardice. Take this and leave it somehwere on the trail at the bridge, will you? Maybe tie it to a tree?” He hands you an old sign covered with dark-reddish paint. “Blood there,” you think, then ask him if it’s not {i}too{/i} dark. “It’s the only paint we can squeeze out from the plants of our meadows,” he admits and gets back to his work.
                    '
                    '“Fine, I’ll do it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, I’ll do it.”')
                        $ quest_easternpath_description06a = "I was asked to place a new sign at the path leading east of the old stone bridge."
                        $ renpy.notify("You received a painted sign.\nJournal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a painted sign. Journal updated: The Eastern Path{/i}')
                        $ item_signpost = 1
                        jump creekselahonquest_easternpathcalculatingresults00
            'I frown. “{i}I{/i} need that path.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown. “{i}I{/i} need that path.”')
                $ quarters += 1
                menu:
                    'He observes you in silence, then gives up. “Well, I’ll trust a roadwarden’s judgment. Wait here for a bit, if you may.” He puts away his tools and heads to a distant building. Once he returns, he’s holding a wooden plank. “Take this and leave it somehwere on the trail at the bridge, will you? Maybe tie it to a tree?”
                    \n\nHe hands you an old sign covered with dark-reddish paint. “Blood there,” you think, then ask him if it’s not {i}too{/i} dark. “It’s the only paint we can squeeze out from the plants of our meadows,” he admits and gets back to his work.
                    '
                    '“Very well.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                        $ quest_easternpath_description06a = "I was asked to place a new sign at the path leading east of the old stone bridge."
                        $ renpy.notify("You received a painted sign.\nJournal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a painted sign. Journal updated: The Eastern Path{/i}')
                        $ item_signpost = 1
                        jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadstonebridge02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I placed the sign, just like you asked.”')
        $ elah_friendship += 2
        menu:
            'He exhales and nods gently. “Thanks, friend. I was thinking ‘bout it and... It may be a good opportunity for us to visit that mountain after all. There’s a lot to talk about, and there will be even more in spring. Here.” He hands you two dragon bones that he already held in a pocket of his pants.
            '
            'I grab them without a word.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab them without a word.')
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ coins += 2
                $ quest_easternpath_points += 2
                $ quest_easternpath_description06aalt = "I received my reward for placing the sign."
                jump creekselahonquest_easternpathcalculatingresults00
            '“I’m glad to see you got your senses back.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad to see you got your senses back.”')
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ coins += 2
                $ quest_easternpath_points += 2
                $ quest_easternpath_description06aalt = "I received my reward for placing the sign."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadwanderer01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”')
        menu:
            '“That woman with a stick?” Seeing your nods, he stops his work. “...Hwat for?”
            '
            '“Haven’t you heard about {color=#f6d6bd}The Wanderer{/color}? It’s a tutelary spirit that keeps travelers from harm.”' if wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Haven’t you heard about {color=#f6d6bd}The Wanderer{/color}? It’s a tutelary spirit that keeps travelers from harm.”')
                $ item_rations += 1
                $ renpy.notify("You received a food ration.\nJournal updated: The Eastern Path.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a food ration. Journal updated: The Eastern Path.{/i}')
                $ quest_easternpath_description07a = "I received my reward for clearing the statue."
                $ elah_friendship += 1
                menu:
                    'The carpenter’s eyes are filled with doubt, but he finally shrugs. “Well, it won’t hurt us to have a pretty statue on our good side.” He asks one of the kids from the square to “bring our guest some dried meat and nuts.” Seeing your look, he pats his stomach. “Hwat? I’m not paying for that.”
                    '
                    '“My patience has its limits, you know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My patience has its limits, you know.”')
                        jump creekselahonquest_easternpathcalculatingresults00
                    'I bite my tongue.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bite my tongue.')
                        jump creekselahonquest_easternpathcalculatingresults00
            '“Maybe you can pray at it or something.”' if wanderer_name != "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you can pray at it or something.”')
                $ quest_easternpath_description07a = "I won’t get a reward for clearing the statue."
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                menu:
                    'He frowns. “This... Isn’t something that matters to us much, friend. We have no priests, nor druids. We don’t care much for mysterious spirits.”
                    '
                    'I smirk. “Yet.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Yet.”')
                        jump creekselahonquest_easternpathcalculatingresults00
                    '“If you say so.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you say so.”')
                        jump creekselahonquest_easternpathcalculatingresults00
            '“It increases the chances that animals will see her as a human shell and feel threatened by it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It increases the chances that animals will see her as a human shell and feel threatened by it.”')
                $ quest_easternpath_description07a = "I won’t get a reward for clearing the statue."
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                menu:
                    'He snorts. “Hwat?” You repeat yourself, but he gestures with his knife for you to stop. “Don’t be dumb, friend! Birds sit on it all the time, and I see no cats jumping on it! Beasts,” he taps his nose, “have other senses than we do.”
                    '
                    '“You may be right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right.”')
                        jump creekselahonquest_easternpathcalculatingresults00
            '“Well, you can admire her, you can turn it into rocks. I thought you may care.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, you can admire her, you can turn it into rocks. I thought you may care.”')
                $ item_rations += 1
                $ renpy.notify("You received a food ration.\nJournal updated: The Eastern Path.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a food ration. Journal updated: The Eastern Path.{/i}')
                $ quest_easternpath_description07a = "I received my reward for clearing the statue."
                menu:
                    'The carpenter glances at his workbench. “I don’t think we need a pile of rocks, but I see hwat you mean. I’ll ask around.” He tells one of the kids from the square to “bring our guest some dried meat and nuts.” Seeing your look, he pats his stomach. “Hwat? I’m not paying for that.”
                    '
                    '“My patience has its limits, you know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My patience has its limits, you know.”')
                        jump creekselahonquest_easternpathcalculatingresults00
                    'I bite my tongue.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bite my tongue.')
                        jump creekselahonquest_easternpathcalculatingresults00
            '“The road is prettier now.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The road is prettier now.”')
                $ quest_easternpath_description07a = "I won’t get a reward for clearing the statue."
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                menu:
                    'He bursts into laughter. “I don’t think merchants care much ‘bout the views, friend! The statue may fall into the lake, for hwat I care.”
                    '
                    'I scowl at him.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scowl at him.')
                        jump creekselahonquest_easternpathcalculatingresults00
                    'I smile. “Views are half the pleasure of a journey.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Views are half the pleasure of a journey.”')
                        $ elah_friendship += 1
                        jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadwatchtower01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The watchtower is clear and ready for new guards.”')
        $ creeks_reputation += 1
        $ elah_friendship += 2
        menu:
            '“That’s a relief!” He reaches for the case so quickly that he misestimates the distance. It falls on the ground with a clatter like a fistful of dice, and instead of collecting everything right away, he picks up two of the dragon bones that are rolling toward him. “I need to make another one anyway,” he says to himself and pays you, asking about the place.
            \n\nYou mention the bugs, the rotten barrels, the moisture. The man nods with enthusiasm. “So we can hide there at any point! We’ll need to discuss it with our friends at {color=#f6d6bd}Gale Rocks{/color}.”
            '
            '“And it was quite an expensive balm, you know. The one for the bugs.” I give him a meaningful look.' if thyrsus_shop:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And it was quite an expensive balm, you know. The one for the bugs.” I give him a meaningful look.')
                menu:
                    'He nods without even listening, but once he notices your eyes, he sighs and reaches for another coin.
                    '
                    'I smile.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile.')
                        $ coins += 3
                        show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                        $ quest_easternpath_points += 2
                        $ quest_easternpath_description08a = "I received my reward for bringing the news about the watchtower."
                        jump creekselahonquest_easternpathcalculatingresults00
            '“And it was quite a difficult balm to make, you know. The one for the bugs.” I give him a meaningful look.' if pc_class == "scholar" and achievement_alchemy_bugrepellent and not thyrsus_shop:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And it was quite a difficult balm to make, you know. The one for the bugs.” I give him a meaningful look.')
                menu:
                    'He nods without even listening, but once he notices your eyes, he sighs and reaches for another coin.
                    '
                    'I smile.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile.')
                        $ coins += 3
                        show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                        $ quest_easternpath_points += 2
                        $ quest_easternpath_description08a = "I received my reward for bringing the news about the watchtower."
                        jump creekselahonquest_easternpathcalculatingresults00
            '“Yep. It’s ready for you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yep. It’s ready for you.”')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description08a = "I received my reward for bringing the news about the watchtower."
                $ elah_friendship += 1
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadwatchtower01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The watchtower is clear, kind of.”')
        $ creeks_reputation += 1
        menu:
            '“That’s a relief!” He reaches for the case so quickly that he misestimates the distance. It falls on the ground with a clatter like a fistful of dice, and instead of collecting everything right away, he picks up two of the dragon bones that are rolling toward him. “I need to make another one anyway,” he says to himself and pays you, asking about the place.
            \n\nYou mention the bugs, the rotten barrels, the moisture. Once you describe the broken door, the man sighs. “So we can’t hide there for long. I’ll need to build a new door myself, but I have no iron for a lock...” He adjusts his furry cloak and starts to think out loud.
            '
            '“And it was quite an expensive balm, you know. The one for the bugs.” I give him a meaningful look.' if thyrsus_shop:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And it was quite an expensive balm, you know. The one for the bugs.” I give him a meaningful look.')
                menu:
                    '“I’m sorry to say that, but you’ve wasted your time,” his voice is hesitant. “Without the entrance, many awful creatures may hide there now, insect empresses included. This is all this message is worth for me.”
                    '
                    'I reach for the dragons slowly.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the dragons slowly.')
                        $ coins += 2
                        show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                        $ quest_easternpath_points += 1
                        $ quest_easternpath_description08aalt = "I received my reward for bringing the news about the watchtower."
                        jump creekselahonquest_easternpathcalculatingresults00
            '“And it was quite a difficult balm to make, you know. The one for the bugs.” I give him a meaningful look.' if pc_class == "scholar" and achievement_alchemy_bugrepellent and not thyrsus_shop:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And it was quite a difficult balm to make, you know. The one for the bugs.” I give him a meaningful look.')
                menu:
                    '“I’m sorry to say that, but you’ve wasted your time,” his voice is hesitant. “Without the entrance, many awful creatures may hide there now, insect empresses included. This is all this message is worth for me.”
                    '
                    'I reach for the dragons slowly.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the dragons slowly.')
                        $ coins += 2
                        show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                        $ quest_easternpath_points += 1
                        $ quest_easternpath_description08aalt = "I received my reward for bringing the news about the watchtower."
                        jump creekselahonquest_easternpathcalculatingresults00
            '“It shouldn’t be too difficult.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It shouldn’t be too difficult.”')
                $ coins += 2
                show screen notifyimage( "Journal updated: The Eastern Path.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +2 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description08aalt = "I received my reward for bringing the news about the watchtower."
                $ elah_friendship += 1
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroaddolmen01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I took a look at the dolmen in the south. It’s safe.”')
        $ elah_friendship += 1
        menu:
            'He keeps sculpting wood and asks you about the size and the entrance of the chapel. “I’ve heard it’s small, but not {i}that{/i} small... Not enough for a group, but maybe a lone traveler, without a mount...” He looks at you with a smile. “Pick a dragon bone from the case, will you? I don’t want to stop now.”
            \n\nYou reach toward the ugly head of a hydra.
            '
            'I grab a coin.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab a coin.')
                $ coins += 1
                show screen notifyimage( "Journal updated: The Eastern Path.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description10a = "I received my reward for bringing the news about the dolmen."
                jump creekselahonquest_easternpathcalculatingresults00
            'If he’s not looking... Nah, he’ll know.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If he’s not looking... Nah, he’ll know.')
                $ coins += 1
                show screen notifyimage( "Journal updated: The Eastern Path.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description10a = "I received my reward for bringing the news about the dolmen."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroad_eudociadeal01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”')
        $ elah_friendship += 1
        menu:
            'The description of the golems makes him tighten his shoulder cloak. When he grabs the casket, he holds it tightly. “And you’re {i}sure{/i} they aren’t going to attack anyone?” Seeing your unconvinced smile, he counts down three bones without looking at them, lost in his thoughts.
            '
            'I take them from his hand.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take them from his hand.')
                $ coins += 3
                show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description13 = "I received my reward for making a deal with {color=#f6d6bd}Eudocia{/color}."
                jump creekselahonquest_easternpathcalculatingresults00
            'One day he’ll be grateful for what I’ve done.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- One day he’ll be grateful for what I’ve done.')
                $ coins += 3
                show screen notifyimage( "Journal updated: The Eastern Path.\n+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +3 {image=cointest}{/i}')
                $ quest_easternpath_points += 1
                $ quest_easternpath_description13 = "I received my reward for making a deal with {color=#f6d6bd}Eudocia{/color}."
                jump creekselahonquest_easternpathcalculatingresults00

    label creekselahaboutquesteasternroadfallentree01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I encountered a fallen tree in the far south.”')
        $ elah_quest_easternpath_fallentree_day = day
        menu:
            'You describe its exact location. “I guess it was unavoidable for this to happen at one point or the other, too bad it’s so far away from here,” he stops his work and turns toward you. “So... Would you like to help us with that, friend?”
            \n\nYou ask him what he proposes, and he describes what he calls “a day of honest work”. “Just come to me some day in the early hours. I still need to discuss this with the tribe, but I’ll ask the stronger folks to travel with you to the tree. They’ll agree if they feel like the roads can be trusted. Split it into blocks, get it on wagons, bring it here. It won’t go to waste, and the road will be cleaned.”
            \n\nWhen you mention it’s going to take an entire day, he agrees. “And you’ll get five dragon bones for it. Just come to me when you’re healthy, and only if you already know what’s on the route from here to that point. We’ll put a lot of trust into your guidance and protection, [pcname].”
            '
            '“So you want me to get to know the entire route, make sure it’s safe enough for your tribe to follow it, and come here in the morning, but only if I can handle the journey... Quite a list, but fine. We’ll see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want me to get to know the entire route, make sure it’s safe enough for your tribe to follow it, and come here in the morning, but only if I can handle the journey... Quite a list, but fine. We’ll see.”')
                menu:
                    'He thinks about your words, then reaches for his case. “You’re right, that’s a lot. I can’t help you much, but at least you deserve one bone right away, for bringing me the message. Maybe buy some rations for it, or a good rest... Actually, we {i}also{/i} need at least one day to prepare ourselves.”
                    '
                    '“Thanks.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                        $ quest_easternpath_description09a = "I was asked to assist the villagers in their travel to the fallen tree. I should meet with them some day before noon, but only if I know the entire route and it’s safe enough to travel in a large group. To make the road safer, I should improve it further."
                        $ coins += 1
                        show screen notifyimage( "Journal updated: The Eastern Path.\n+1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                        jump creekselahonquest_easternpathcalculatingresults00
            '“I’m not going to waste an entire day on a dangerous journey just to see how your tribe beats a trunk. You can do that on your own once the spring comes, and the roads get safer.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not going to waste an entire day on a dangerous journey just to see how your tribe beats a trunk. You can do that on your own once the spring comes, and the roads get safer.”')
                menu:
                    'He opens the case and looks inside. “Then one dragon it is. For bringing me the news.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        $ quest_easternpath_description09b = "I received my reward for informing the villagers about the fallen tree."
                        $ coins += 1
                        $ quest_fallentree = 3
                        show screen notifyimage( "Quest completed: The Fallen Tree.\nJournal updated: The Eastern Path.\n+1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Fallen Tree. Journal updated: The Eastern Path. +1 {image=cointest}{/i}')
                        jump creekselahonquest_easternpathcalculatingresults00

    label creekselahonquest_easternpathcalculatingresults00:
        if quest_easternpath_points >= 3 and not creeks_mundanework:
            menu:
                '“Well, friend! Thanks to your tales, the hunters and foragers feel more confident ‘bout the meadows from here to {color=#f6d6bd}Foggy’s{/color}, and even beyond. When you have a day to spare, come here any morning, ask our tribesfolk ‘bout a job for a roadwarden, unless it rains. You’ll get two dragons and enough stew to fill your belly for a day of patrolling the roads and assisting us and our wagons, so the things you are meant to do anyway, aye?”
                '
                '“I know from {color=#f6d6bd}Old Hava{/color} that your tribe needs your contact with {color=#f6d6bd}Foggy{/color} more than I need your coin. Two dragons for a day isn’t enough.”' if oldhava_about_foggy >= 2 and not creeks_mundanework_betterpay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know from {color=#f6d6bd}Old Hava{/color} that your tribe needs your contact with {color=#f6d6bd}Foggy{/color} more than I need your coin. Two dragons for a day isn’t enough.”')
                    $ creeks_mundanework_betterpay = 1
                    $ creeks_mundanework_payment = 3
                    $ creeks_mundanework = 1
                    $ renpy.notify("New mundane job available.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New mundane job available.{/i}')
                    menu:
                        'He thinks about your words for a few moments before he surrenders. “So be it, friend. Three it is. Just remember to come with a healthy shell, it won’t be a stroll.”
                        '
                        '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                            jump creekselahaboutquesteasternroadduskfoxes01
                        '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                            jump creekselahaboutquesteasternroadduskfoxes02
                        'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                            pass
                        'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                            pass
                        'I need to still look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                            pass
                        '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                            jump creekselahaboutquesteasternroadclearedbrook01
                        'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                            pass
                        '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                            jump creekselahaboutquesteasternroadhunterscabin01
                        'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                            pass
                        '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                            jump creekselahaboutquesteasternroadstonebridge01
                        '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                            jump creekselahaboutquesteasternroadstonebridge02
                        'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                            pass
                        '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                            jump creekselahaboutquesteasternroadwanderer01
                        '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                            jump creekselahaboutquesteasternroadwatchtower01
                        '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                            jump creekselahaboutquesteasternroadwatchtower01alt
                        '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                            jump creekselahaboutquesteasternroad_eudociadeal01
                        'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                            pass
                        'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                            pass
                        '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                            jump creekselahaboutquesteasternroaddolmen01
                        '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                            jump creekselahaboutquesteasternroadfallentree01
                        '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                            jump creekselahaboutquesteasternroadfallentree02
                        'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                            pass
                        'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                            pass
                        'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                            pass
                        'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                            pass
                        'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                            pass
                        'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                            pass
                        '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                            jump creekselahaboutquesteasternroadshortcut01
                        '“I’ll let you know if there’s anything else.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                            jump creekselahafterinteraction01
                '“Maybe, maybe.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe, maybe.”')
                    $ creeks_mundanework = 1
                    $ renpy.notify("New mundane job available.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New mundane job available.{/i}')
                    menu:
                        '“Just remember to come with a healthy shell, it won’t be a stroll.”
                        '
                        '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                            jump creekselahaboutquesteasternroadduskfoxes01
                        '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                            jump creekselahaboutquesteasternroadduskfoxes02
                        'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                            pass
                        'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                            pass
                        'I need to still look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                            pass
                        '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                            jump creekselahaboutquesteasternroadclearedbrook01
                        'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                            pass
                        '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                            jump creekselahaboutquesteasternroadhunterscabin01
                        'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                            pass
                        '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                            jump creekselahaboutquesteasternroadstonebridge01
                        '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                            jump creekselahaboutquesteasternroadstonebridge02
                        'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                            pass
                        '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                            jump creekselahaboutquesteasternroadwanderer01
                        '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                            jump creekselahaboutquesteasternroadwatchtower01
                        '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                            jump creekselahaboutquesteasternroadwatchtower01alt
                        '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                            jump creekselahaboutquesteasternroad_eudociadeal01
                        'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                            pass
                        'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                            pass
                        '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                            jump creekselahaboutquesteasternroaddolmen01
                        '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                            jump creekselahaboutquesteasternroadfallentree01
                        '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                            jump creekselahaboutquesteasternroadfallentree02
                        'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                            pass
                        'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                            pass
                        'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                            pass
                        'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                            pass
                        'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                            pass
                        'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                            pass
                        '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                            jump creekselahaboutquesteasternroadshortcut01
                        '“I’ll let you know if there’s anything else.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                            jump creekselahafterinteraction01
        elif (quest_easternpath == 1 and quest_easternpath_points >= quest_easternpath_points_max and quest_easternpath_description09aa) or (quest_easternpath == 1 and quest_easternpath_points >= quest_easternpath_points_max and quest_easternpath_description09b):
            $ creeks_reputation += 1
            $ elah_friendship += 1
            menu:
                '{color=#f6d6bd}The carpenter{/color} pauses for a longer while, then starts to draw an invisible map on the workbench with his fingers, muttering to himself. “Yes,” he says slowly, “you’ve already done more on the road than I’ve expected, friend. I dare say more than any outsider in this generation. The tribe can take it from here.”
                \n\nHe reaches for something resting on a log beneath the table, then turns toward you. “You already received your pay, but maybe you’d like to take a hare pelt as a gift? {color=#f6d6bd}Foggy{/color} doesn’t need it, but you’ll get a dragon or two for it in another village.”
                \n\nYou take a look at the fine fur and roll it into a more mobile shape. Seeing how {color=#f6d6bd}Elah{/color} observes you, you tell him to just ask. “I can’t figure out hwat pushed you to be this much of a help to us, friend. I know some of the things you’ve seen were just on your path, but others took a true risk.”
                '
                '“It’s just what a roadwarden ought to do.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just what a roadwarden ought to do.”')
                    $ item_harepelt += 1
                    $ renpy.notify("You received a hare pelt.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a hare pelt.{/i}')
                    $ description_oldpagos04a = "According to {color=#f6d6bd}Elah{/color}, the locals value those who fulfil their “duty.”"
                    menu:
                        '“You speak as if you’re from {color=#f6d6bd}Old Págos{/color},” he rests one hand on his stomach and reaches out to you with the other one. “It may be just another day of work for you, but come here another spring, or later. You’ll see a real change in the peninsula.”
                        '
                        'I shake his hand. “I’m sure I will.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand. “I’m sure I will.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship += 1
                            $ questionpreset = "elah1"
                            menu:
                                'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and looks at his tools with a big smile.
                                '
                                '(elah1 set)':
                                    pass
                        'I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship -= 1
                            $ questionpreset = "elah1"
                            menu:
                                'Stuck in an awkward pose, he clears his throat and reaches for the heavy cloak on his shoulders. “And we’ll welcome you warmly. So... I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and glances at his tools awkwardly, waiting for you to step away.
                                '
                                '(elah1 set)':
                                    pass
                '“Your pay was fair and I needed it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your pay was fair and I needed it.”')
                    $ item_harepelt += 1
                    $ renpy.notify("You received a hare pelt.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a hare pelt.{/i}')
                    menu:
                        '“We don’t have much left,” he chuckles and pats his stomach, “but my tribe agrees it’s a good deal for us.” His other hand reaches out to you. “We may not have much, but come here another spring, or later. You’ll see a real change in the peninsula.”
                        '
                        'I shake his hand. “I’m sure I will.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand. “I’m sure I will.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship += 1
                            $ questionpreset = "elah1"
                            menu:
                                'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and looks at his tools with a big smile.
                                '
                                '(elah1 set)':
                                    pass
                        'I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship -= 1
                            $ questionpreset = "elah1"
                            menu:
                                'Stuck in an awkward pose, he clears his throat and reaches for the heavy cloak on his shoulders. “And we’ll welcome you warmly. So... I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and glances at his tools awkwardly, waiting for you to step away.
                                '
                                '(elah1 set)':
                                    pass
                '“{color=#f6d6bd}Creeks{/color} is a lovely place. I hope it succeeds.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} is a lovely place. I hope it succeeds.”')
                    $ item_harepelt += 1
                    $ renpy.notify("You received a hare pelt.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a hare pelt.{/i}')
                    $ creeks_reputation += 1
                    $ elah_friendship += 1
                    menu:
                        'His proud smile is followed by a victorious stance. “It’s one of a kind, aye? And living here is only going to get better, I’ll put my whole life into making sure of that!” He rests one hand on his stomach and reaches out to you with the other one. “Come here another spring, or later. You’ll see a real change in the peninsula!”
                        '
                        'I shake his hand. “I’m sure I will.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand. “I’m sure I will.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship += 1
                            $ questionpreset = "elah1"
                            menu:
                                'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and looks at his tools with a big smile.
                                '
                                '(elah1 set)':
                                    pass
                        'I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship -= 1
                            $ questionpreset = "elah1"
                            menu:
                                'Stuck in an awkward pose, he clears his throat and reaches for the heavy cloak on his shoulders. “And we’ll welcome you warmly. So... I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and glances at his tools awkwardly, waiting for you to step away.
                                '
                                '(elah1 set)':
                                    pass
                'I smirk. “Oh, I do have my reasons.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Oh, I do have my reasons.”')
                    $ item_harepelt += 1
                    $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                    $ elah_friendship += 1
                    menu:
                        '“I bet you do!” He bursts into laughter and pats his stomach. “You proved to be a capable soul.” His other hand reaches out to you. “If you ever decide we have a part in these plans, come here another spring, or later. You’ll see a real change in the peninsula.”
                        '
                        'I shake his hand. “I’m sure I will.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand. “I’m sure I will.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship += 1
                            $ questionpreset = "elah1"
                            menu:
                                'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and looks at his tools with a big smile.
                                '
                                '(elah1 set)':
                                    pass
                        'I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pretend to be focused on the pelt. “If I’m ever around, I’ll be sure to see how it’s progressed.”')
                            $ quest_easternpath_description_final = "My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."
                            $ quest_easternpath = 2
                            if pc_goal == "iwanttohelp":
                                $ pc_goal_iwanttohelppoints += 2
                            if pc_goal == "iwanttoberemembered":
                                $ pc_goal_iwanttoberememberedpoints += 1
                            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                            else:
                                $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ renpy.notify("Quest completed: The Eastern Path\nJournal updated: Explore the Peninsula")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Eastern Path. Journal updated: Explore the Peninsula{/i}')
                            $ quest_explorepeninsula_description08 = "The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
                            $ elah_friendship -= 1
                            $ questionpreset = "elah1"
                            menu:
                                'Stuck in an awkward pose, he clears his throat and reaches for the heavy cloak on his shoulders. “And we’ll welcome you warmly. So... I doubt you’ll find much more to do on this route, but if I turn out to be wrong, let me know.”
                                \n\nHe then sits down on the stool and glances at his tools awkwardly, waiting for you to step away.
                                '
                                '(elah1 set)':
                                    pass
        else:
            if quest_easternpath_points <= 0:
                $ custom1 = "“There’s no dragons without results, friend.”"
            elif quest_easternpath_points == 1:
                $ custom1 = "“Well, that’s a start! Keep it up.”"
            elif quest_easternpath_points == 2:
                $ custom1 = "“Good to see you don’t idle around, roadwarden.”"
            elif quest_easternpath_points == 3:
                $ custom1 = "“I’m never tired of good news!”"
            elif quest_easternpath_points == 4:
                $ custom1 = "He pats his stomach and looks at you with a smile. “Keep up the good work, friend!”"
            elif quest_easternpath_points == 5:
                $ custom1 = "“I’m glad you keep moving forward. My tribe was worried I’d throw our dragon bones away, but we’re already planning our next move.”"
            elif quest_easternpath_points == 6:
                $ custom1 = "“The more I tell my tribesfolk ‘bout your good work, the more often I hear them talking ‘bout you.”"
            elif quest_easternpath_points == 7:
                $ custom1 = "“We’ve started sending the foragers and hunters to farther parts of the peninsula. The monsters are still there, but the fewer surprises there are ahead of us, the easier it is to adapt.”"
            elif quest_easternpath_points == 8:
                $ custom1 = "“Believe it or not, my tribesfolk say the roads truly {i}are{/i} getting safer. Beasts are learning this road is not just theirs anymore."
            elif quest_easternpath_points == 9:
                $ custom1 = "He laughs. “You took almost all of the savings we had, but I’m sure it’s a good investment!”"
            else:
                $ custom1 = "“I’m surprised you keep finding something to do! This land really is a mess.”"
            menu:
                '[custom1]
                '
                '“I got rid of a small pack of dusk foxes that lived in the ruined shelter in the west.”' if quest_easternpath_description03 and not quest_easternpath_description03a:
                    jump creekselahaboutquesteasternroadduskfoxes01
                '“The shelter in the west isn’t safe. Better to stay away from it until the dusk foxes move out.”' if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                    jump creekselahaboutquesteasternroadduskfoxes02
                'I was at the ruined shelter in the west, but I know nothing about this place. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d:
                    pass
                'The dusk foxes at the shelter in the west are a bit of a problem. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                    pass
                'I need to still look inside the ruined shelter in the west. (disabled)' if ruinedshelter_firsttime and not quest_easternpath_description03 and not quest_easternpath_description03alt and not ruinedshelter_firsttime00d:
                    pass
                '“I’ve restored the brook ford that connects the eastern road with the heart of the forest.”' if quest_easternpath_description04 and not quest_easternpath_description04a:
                    jump creekselahaboutquesteasternroadclearedbrook01
                'The brook ford leading to the heart of the woods won’t support wagons and carts. (disabled)' if not quest_easternpath_description04 and shortcut_easternentrance_firsttime and not shortcut_easternentrance_ford_ignored:
                    pass
                '“There was a big spider at the hunter’s cabin, but it’s gone now.”' if quest_easternpath_description05 and not quest_easternpath_description05a:
                    jump creekselahaboutquesteasternroadhunterscabin01
                'The big spider from the hunter’s cabin is a threat to travelers. (disabled)' if not quest_easternpath_description05 and huntercabin_spider_seen:
                    pass
                '“I cleared the bushes leading east of the old stone bridge.”' if quest_easternpath_description06 and not quest_easternpath_description06a:
                    jump creekselahaboutquesteasternroadstonebridge01
                '“I placed the sign, just like you asked.”' if quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                    jump creekselahaboutquesteasternroadstonebridge02
                'I was asked to place a wooden sign at the old bridge in the south. (disabled)' if not quest_easternpath_description06alt and item_signpost:
                    pass
                '“I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place.”' if quest_easternpath_description07 and not quest_easternpath_description07a:
                    jump creekselahaboutquesteasternroadwanderer01
                '“The watchtower is clear and ready for new guards.”' if quest_easternpath_description08 and not quest_easternpath_description08a and not quest_easternpath_description08aalt:
                    jump creekselahaboutquesteasternroadwatchtower01
                '“The watchtower is clear, kind of.”' if quest_easternpath_description08alt and not quest_easternpath_description08aalt and not quest_easternpath_description08a:
                    jump creekselahaboutquesteasternroadwatchtower01alt
                '“I made a deal with {color=#f6d6bd}Eudocia{/color}. Her sentinels are going to look after the roads that surround the watchtower.”' if eudocia_about_roadclearing_cleared and not quest_easternpath_description13:
                    jump creekselahaboutquesteasternroad_eudociadeal01
                'I still don’t know the condition of the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and not watchtower_open:
                    pass
                'I should take care of the swarm of bugs that crawl in the watchtower. (disabled)' if not quest_easternpath_description08 and not quest_easternpath_description08alt and watchtower_firsttime and watchtower_open and not watchtower_tower_bugs_cleared:
                    pass
                '“I took a look at the dolmen in the south. It’s safe.”' if quest_easternpath_description10 and not quest_easternpath_description10a:
                    jump creekselahaboutquesteasternroaddolmen01
                '“I encountered a fallen tree in the far south.”' if quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b:
                    jump creekselahaboutquesteasternroadfallentree01
                '“I’m ready to help you with the fallen tree.”' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and pc_hp >= 2 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day < day:
                    jump creekselahaboutquesteasternroadfallentree02
                'The locals need one more day before they get ready for a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and elah_quest_easternpath_fallentree_roadknown and elah_quest_easternpath_fallentree_day >= day:
                    pass
                'I don’t fully know the road leading to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters <= 44 and quest_easternpath_points >= 5 and not elah_quest_easternpath_fallentree_roadknown:
                    pass
                'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and not creeks_mundanework:
                    pass
                'Elah wants me to bring him more news from the eastern road before we travel to the fallen tree. I could also run a few mundane patrols for the village. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quest_easternpath_points < 5 and creeks_mundanework:
                    pass
                'It’s too late to start a journey to the fallen tree. (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and quarters > 44:
                    pass
                'I’m too tired to assist them in a journey to the fallen tree. (Required vitality: 2) (disabled)' if quest_easternpath_description09a and not quest_easternpath_description09aa and not quest_easternpath_description09b and pc_hp < 2:
                    pass
                '“I spent a lot of time in the heart of the woods. I can tell you about its threats.”' if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11:
                    jump creekselahaboutquesteasternroadshortcut01
                '“I’ll let you know if there’s anything else.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if there’s anything else.”')
                    jump creekselahafterinteraction01

label creekselahonmundaneworkbetterpay01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about the patrols you want to pay me for.”')
    menu:
        'His carving slows down slightly. “Hwat’s the matter, friend?”
        '
        '“I know from {color=#f6d6bd}Old Hava{/color} that your tribe needs your contact with {color=#f6d6bd}Foggy{/color} more than I need your coin. Two dragons for a day isn’t enough.”' if oldhava_about_foggy >= 2 and not creeks_mundanework_betterpay:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know from {color=#f6d6bd}Old Hava{/color} that your tribe needs your contact with {color=#f6d6bd}Foggy{/color} more than I need your coin. Two dragons for a day isn’t enough.”')
            $ creeks_mundanework_betterpay = 1
            $ creeks_mundanework_payment = 3
            $ questionpreset = "elah1"
            menu:
                'He thinks about your words for a few moments before he surrenders. “So be it. Three it is.”
                '
                '(elah1 set)':
                    pass

label elah_about_steephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the ruins of the village in the south?”')
    $ elah_about_steephouse_gray = 1
    $ questionpreset = "elah1"
    menu:
        'He freezes for a good moment and finally takes a deep breath, puts away his tools, and looks you in the eyes. His fingers are moving slowly, as if he’s trying to warm them up before playing on a lute. “Don’t push me onto those dark grounds, [pcname]. I’ve been stepping on them for years, but I still struggle. Please.”
        '
        '(elah1 set)':
            pass

    label elah_about_steephouse01reduction:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know that your tribe witnessed nefarious deeds ten years ago. You must know more than what you said about the ruins.”')
        $ elah_about_steephouse_friendship_thais = 1
        $ elah_about_steephouse_friendship -= 2
        $ questionpreset = "elah1"
        menu:
            '“Aye, yet...” He scowls at you, but then reaches to his shoulder cloak and loosens it. He hesitates for a few breaths, then meets your eyes. “We’d rather let these deeds rot in our souls, until death arrives.”
            '
            '(elah1 set)':
                pass

    label elah_about_steephouse02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elah{/color}, I {i}need{/i} to know what happened ten years ago. Don’t you trust me?”')
        menu:
            '“I do, [pcname], I do,” his voice is close to a whimper. “But can’t you see I’m in pain? I beg you, let me die with this shame. Aren’t we friends?”
            \n\nHis hands are clasped on his stomach, putting pressure on it, as if he’s trying to stop some invisible bleeding.
            '
            '“Stop it. Deal with your shame by being honest with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Stop it. Deal with your shame by being honest with me.”')
                $ elah_about_steephouse = 1
                $ ruinedvillage_truth = 1
                $ ruinedvillage_name = "Steep House"
                $ elah_friendship -= 4
                $ creeks_reputation -= 1
                $ elah_locked = day
                $ quest_ruins_description_truestory = "{color=#f6d6bd}Elah{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to his story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                $ quest_ruins_description_creeksparticipated = "{color=#f6d6bd}Elah{/color} admitted that the people of {color=#f6d6bd}Creeks{/color} helped {color=#f6d6bd}Thais{/color} during the raid."
                $ description_creeks09 = "{color=#f6d6bd}Elah{/color} admitted that the people of {color=#f6d6bd}Creeks{/color} helped {color=#f6d6bd}Thais{/color} during the raid."
                $ description_ruinedvillage02 = "{color=#f6d6bd}Elah{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to his story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                $ description_thais06 = "{color=#f6d6bd}Elah{/color} blames her for destroying the southern village."
                $ description_elah_efren05 = "{color=#f6d6bd}Elah{/color} admitted to participating in the raid on {color=#f6d6bd}Steep House{/color}."
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                menu:
                    'He bites his lower lip and looks away. “Troll piss and shit, {i}roadwarden{/i}. Fine!” He stands up, pointing at you with his clenched fist, suddenly filled by a spirit you’ve never seen before. “Hwat do you want me to say? That I was there, as well as my parents, and parents of others from our village? That {color=#f6d6bd}Thais{/color} wanted to make an example of {color=#f6d6bd}Steep House{/color} and told us to either help her, or be next in line?”
                    \n\nHe spreads his arms. “Aye, the {i}great uniter{/i} of the North! We went there with her myrmidons, left dust and hunger behind, and the beast herds came after us, angry for the burnt and cut trees. {i}Too bad{/i} once that happened no soul wanted to deal with that two-faced weasel,” his voice cracks. “We cut the flesh of innocents to save our own, and we got nothing from it.”
                    \n\nYou flinch when he raises his hand and moves toward you, even though his gesture is not so much an attack, as a way for him to let out some of his fire. Seeing your reaction, he slows down, but that only makes his voice louder. “You already knew all of that, didn’t you? And you just {i}had to{/i} test my last wits for your games?! Hwat, you think you’ll take the blood from my blade and wake up that fucking boy?”
                    \n\nOther people in the yard cease their work and observe you. You hear a child crying.
                    '
                    'I raise my voice. “I didn’t know you had killed anyone, {color=#f6d6bd}Elah{/color}, but you’re lucky that you faced no consequences, even if you deserve them. Now step away.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my voice. “I didn’t know you had killed anyone, {color=#f6d6bd}Elah{/color}, but you’re lucky that you faced no consequences, even if you deserve them. Now step away.”')
                        $ elah_friendship -= 2
                        $ creeks_reputation -= 1
                        menu:
                            '“Oh, fuck off!” He waves at you and enters the building with his tools, disappearing behind the shut door.
                            \n\nThe angry looks of others still follow you, but the life returns slowly to the small village of {color=#f6d6bd}Creeks{/color}.
                            '
                            'I return to {color=#f6d6bd}[horsename]{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}%s{/color}.' %horsename)
                                jump creeksafterinteraction01
                    'I speak softly. “You’re a victim, not a villain. {color=#f6d6bd}Thais{/color} would have struck them with or without you, and maybe kill you as well. But you’re alive, and you try to put your life to good use.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak softly. “You’re a victim, not a villain. {color=#f6d6bd}Thais{/color} would have struck them with or without you, and maybe kill you as well. But you’re alive, and you try to put your life to good use.”')
                        menu:
                            '“There are no words,” he starts, swallowing his tears, then flounders through sounds. “No words that can wash my dreams, [pcname]. I can’t be forgiven, and I can’t fix {i}anything{/i}.” He turns around and lurches into the building with his tools.
                            \n\nThe sad looks of others still follow you, but the life returns slowly to the small village of {color=#f6d6bd}Creeks{/color}.
                            '
                            '“We’ll speak another time.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll speak another time.”')
                                jump creeksafterinteraction01
                    'I try to stay quiet. “I wasn’t there, I’ve no clue what you went through. Maybe you deserve your pain, maybe not. I won’t judge you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to stay quiet. “I wasn’t there, I’ve no clue what you went through. Maybe you deserve your pain, maybe not. I won’t judge you.”')
                        $ elah_friendship += 1
                        menu:
                            'He looks at you through his tears, then raises his head, absently staring at the clouds. “Aye, you weren’t there. My eyes and hands are cursed, but...” He looks at the gathered crowd, then at you again. “They’re not alone.” He turns around and lurches into the building with his tools.
                            \n\nThe sad looks of others still follow you, but the life returns slowly to the small village of {color=#f6d6bd}Creeks{/color}.
                            '
                            '“We’ll speak another time.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll speak another time.”')
                                jump creeksafterinteraction01
            '“...Fine, friend. Keep it to yourself.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Fine, friend. Keep it to yourself.”')
                $ elah_about_steephouse_canceled = 1
                $ elah_friendship += 2
                $ creeks_reputation += 1
                $ questionpreset = "elah1"
                $ minutes += 5
                menu:
                    'He lets out something between a cough and a weep, then covers his eyes. You take a step away, but he wipes his tears and nods toward you, giving you a weak smile. After a few breaths, he regains his composure. “Thank you.”
                    '
                    '(elah1 set)':
                        pass

label elah_about_nomoreundeadALL:
    label elah_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The north will be a bit safer. The priest of {color=#f6d6bd}White Marshes{/color} has agreed to no longer use the undead.”')
        $ elah_about_nomoreundead = 1
        $ elah_friendship += 2
        $ creeks_reputation += 1
        $ minutes += 5
        $ questionpreset = "elah1"
        menu:
            'He stops in his work and looks at you in silence, waiting for you to carry on. “I can’t say I was all that familiar with any of this,” he says once you’re done with your tale, “but I’m happy you managed to avoid violence. You truly are our roadwarden, friend.”
            '
            '(elah1 set)':
                pass

    label elah_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The north will be a bit safer. {color=#f6d6bd}White Marshes{/color} no longer uses undead, though they had to be persuaded with force.”')
        $ elah_about_nomoreundead = 2
        $ creeks_reputation += 1
        $ minutes += 5
        $ questionpreset = "elah1"
        menu:
            'He stops in his work and looks at you in silence, waiting for you to carry on. “I can’t say I was all that familiar with any of this,” he says once you’re done with your tale, “but I’d expect a roadwarden should solve such matters without violence.” With a sigh, he looks at his tools again. “You’ll regret tying yourself to folks like {color=#f6d6bd}Thais{/color}. Be careful, friend.”
            '
            '(elah1 set)':
                pass

    label elah_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hard days may soon come. {color=#f6d6bd}White Marshes{/color} is destroyed, a large group of undead may strike after just a few fogs.”')
        $ elah_about_nomoreundead = 3
        $ elah_friendship -= 2
        $ creeks_reputation -= 1
        $ minutes += 5
        $ elah_locked = day
        menu:
            'He freezes, then his tools drop on the ground. “Hwat are you talking ‘bout?” Even though you try to avoid the more {i}sensitive{/i} details, he stares at you with fury, heavily breathing with his broad chest. “Leave me alone,” he turns around and walks away. “I need to think!”
            '
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump creeksafterinteraction01

label creekselahonfeast01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was told to speak with you about the funeral rites. Let’s begin the preparations.”')
    if quarters < (world_daylength-12):
        menu:
            '“We won’t start the fire before dusk,” he puts away his tools. “Our hearts are ready, but are you sure you have time, friend?”
            '
            '“Give me a few more hours, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Give me a few more hours, then.”')
                jump creekselahafterinteraction01
            '“I am. Come, I’ll help you with the food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I am. Come, I’ll help you with the food.”')
                $ elah_friendship += 1
                menu:
                    'He stands up with a smile and leads you to the house of gatherings.
                    '
                    'We talk about this and that.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We talk about this and that.')
                        jump creekthegrandfeast01
    else:
        menu:
            '“Everything’s ready, friend. We’ll be glad to have you at our side.”
            '
            '“I’m honored to be invited.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m honored to be invited.”')
                jump creekthegrandfeast01
            'I think about {color=#f6d6bd}Hovlavan{/color} and its goals for the peninsula.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about {color=#f6d6bd}Hovlavan{/color} and its goals for the peninsula.')
                jump creekthegrandfeast01

label creekselahaboutquesteasternroadfallentree02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to help you with the fallen tree.”')
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'He springs up and leads you to the square. “Gather folks for the woodcutting,” he orders the children and waves to the adults to gain their attention. He looks at you with a smile. “We have sharp axes, full stomachs, spare wheels, and you can leave your mount at a creek. Nothing like a day of grazing, napping, and shitting, aye?” Without waiting for your response, he addresses the approaching souls. None of them are older than thirty.
        '
        'I approach {color=#f6d6bd}[horsename]{/color} and scratch its neck. “Don’t worry. I’ll be back soon.”' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}%s{/color} and scratch its neck. “Don’t worry. I’ll be back soon.”' %horsename)
            jump creekselahaboutquesteasternroadfallentree03
        'I take from the saddle only what’s going to be useful on the road.' if not pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take from the saddle only what’s going to be useful on the road.')
            jump creekselahaboutquesteasternroadfallentree03

    label creekselahaboutquesteasternroadfallentree03:
        $ elah_quest_easternpath_lumberjacks = 1
        $ quarters += 1
        menu:
            'After a few minutes the crowd gathers next to the bridge, organizing their simple carts and wagons that are held only by ropes, joints, and leather straps. You notice that one of them carries a pile of a few bulky sacks, so you ask [shoshi_namesmall] with a massive axe about their contents.
            \n\n“Just food, friend!” She’s looking at you with excitement, moving her hips to an inaudible melody. “Hwat’s on hweels’s light as a feather, no need to hunt in the woods.” To illustrate her point, she throws her tool into the cart next to her.
            '
            'I pile my belongings in a wagon’s corner, covering them with my heavy cloak.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pile my belongings in a wagon’s corner, covering them with my heavy cloak.')
                $ travel_destination = "foggylake"
                jump finaldestinationafterevent
            '...Just in case, I keep my axe at my belt.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...Just in case, I keep my axe at my belt.')
                $ travel_destination = "foggylake"
                jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree04:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture foggylaketocreeks02 at basicfade
        menu:
            'It doesn’t take long for the sounds of wheels and boots to cut through the songs of birds and insects. Your loud journey is accompanied not just by the sounds of trampled and kicked rocks, but also the conversations of the woodcutters, who are spread around without many worries.
            \n\nYou cross the thin gorge where {color=#f6d6bd}Efren, the hunter{/color}, is waiting on the side of the road. He stands still, looking around like a gate guard from the city, but once you get closer, he joins you with an excited look and light steps, shaking the wolf’s head. “Don’t worry, friend! You may be here to protect us, but {i}my{/i} destiny is to keep you breathing to the very end!”
            '
            '“You seem happy to leave the village.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You seem happy to leave the village.”')
                $ custom1 = "“Oh, I’ve been around!” He reaches for his obsidian club and swings it left and right, trying to both move forward and demonstrate a few defensive stances. “But there’s always more to see, and a land as wild as this one changes with every season!”\n\n"
                jump creekselahaboutquesteasternroadfallentree04b
            '“And what happens after the end?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what happens after the end?”')
                $ custom1 = "“There may never be one, or we may not see it coming,” his tone is cheerful as he glances at the humble caravan. “But don’t worry, I have a feeling a good day is ahead of us!”\n\n"
                jump creekselahaboutquesteasternroadfallentree04b
            '“Good.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good.”')
                $ custom1 = "He smiles, looks at the humble caravan behind him, and allows you to keep to your own thoughts."
                jump creekselahaboutquesteasternroadfallentree04b

        label creekselahaboutquesteasternroadfallentree04b:
            show areapicture wanderertofoggylake at basicfade
            if foragers_firsttime:
                $ custom2 = "{color=#f6d6bd}Ilan{/color} and {color=#f6d6bd}Tzvi{/color}, the foragers"
            else:
                $ custom2 = "{color=#f6d6bd}Foggy’s foragers{/color}"
            if foragers_firsttime:
                $ custom3 = "{color=#f6d6bd}Ilan{/color}"
            else:
                $ custom3 = "{color=#f6d6bd}the large man{/color}"
            menu:
                '[custom1] You move past the tavern and head south, where you encounter [custom2]. They move through the meadows with long sticks in hand and baskets on their backs, seeking food in the meadows while also scaring away any potential snakes. Once they notice your expedition, they run up to the road, where the larger man asks the others about their health and days.
                \n\nAfter a few minutes they reach you and {color=#f6d6bd}Efren{/color}. “You look both like a flock of vagabonds {i}and{/i} a squad of guards, with all these axes and spears,” says [custom3]. “Weird to see you all in one place, without the walls to hide you, crude as they are.”
                '
                'This catches my interest. “The palisade isn’t that bad.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This catches my interest. “The palisade isn’t that bad.”')
                    if foragers_friendship >= 2:
                        $ creeks_reasonstojoin_creeksaboutlackingwall += 1
                        $ elah_efren_siblings = 1
                        if foragers_firsttime:
                            $ custom1 = "{color=#f6d6bd}Ilan{/color}"
                        else:
                            $ custom1 = "{color=#f6d6bd}The large man{/color}"
                        if foragers_firsttime:
                            $ custom2 = "{color=#f6d6bd}Tzvi{/color}"
                        else:
                            $ custom2 = "{color=#f6d6bd}the man in a black cloak{/color}"
                        menu:
                            '[custom1] looks at you with an open mouth, then glances at [custom2], who simply shrugs. “It rots a lot, and some creatures squeeze through the beams, especially in the back. They steal food, and this one time they took a baby.”
                            \n\n{color=#f6d6bd}Efren’s{/color} voice is unusually tired. “My brother often says he’d like to make a wall of stone, but who knows when we’ll have enough to buy it.” After that, the foragers speak briefly about the plans your group has for the rest of the journey, then announce it’s time for them to get back home.
                            '
                            'I wish them a safe walk.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish them a safe walk.')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                            'I sigh and turn to {color=#f6d6bd}Efren{/color}. “A hostile path is ahead of us. Be sure to observe the bushes.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh and turn to {color=#f6d6bd}Efren{/color}. “A hostile path is ahead of us. Be sure to observe the bushes.”')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                    else:
                        menu:
                            '[custom1] looks at you with an open mouth, then glances at [custom2], who shakes his head slowly. “You’re right,” he says without conviction. “It just can never be too safe, aye?” He then asks {color=#f6d6bd}Efren{/color} about the plans your group has for the rest of the journey, then announces it’s time for them to get back home.
                            '
                            'I wonder what they were hiding.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder what they were hiding.')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                            'I wish them a safe walk.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish them a safe walk.')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                            'I sigh and turn to {color=#f6d6bd}Efren{/color}. “A hostile path is ahead of us. Be sure to observe the bushes.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh and turn to {color=#f6d6bd}Efren{/color}. “A hostile path is ahead of us. Be sure to observe the bushes.”')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                '“How’s today’s {i}hunt{/i} going?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How’s today’s {i}hunt{/i} going?”')
                    if foragers_firsttime:
                        $ custom2 = "{color=#f6d6bd}Ilan{/color}"
                    else:
                        $ custom2 = "{color=#f6d6bd}The large man{/color}"
                    if foragers_firsttime:
                        $ custom1 = "{color=#f6d6bd}Tzvi{/color}"
                    else:
                        $ custom1 = "{color=#f6d6bd}The man in a dark cloak{/color}"
                    $ foragers_friendship += 1
                    menu:
                        '[custom2], careful as usual, reaches for his throwing club and makes a slow throw-like gesture. His polished and lacquered weapon shines in the sun. “I hit a blue grouse, it didn’t have a chance.” [custom1] scoffs: “Aye, on the third try,” but his companion ignores it. “And we have a few snake eggs, a good dinner awaits us.”
                        \n\nAfter that, they mostly speak with {color=#f6d6bd}Efren{/color} about the mouflon he recently delivered to them, then turn back before you get to the stone statue, wishing you a safe journey.
                        '
                        'It’s nice to see that people are relaxed. I continue to chit chat with the hunter.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s nice to see that people are relaxed. I continue to chit chat with the hunter.')
                            $ travel_destination = "foragingground"
                            jump finaldestinationafterevent
                        'I sigh. “A hostile path ahead of us. Be sure to look at the bushes.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “A hostile path ahead of us. Be sure to look at the bushes.”')
                            $ travel_destination = "foragingground"
                            jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree05:
        show areapicture cabintoforagingground at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if shoshi_namebig == "The dark-haired woodcutter":
            $ custom6 = "the voice of the woman with whom you’d spoken about the sacks before"
        else:
            $ custom6 = "{color=#f6d6bd}Shoshi’s{/color} voice"
        menu:
            'The farther away you get from the foraging ground, the more quiet the tribesfolk grow. The hours of wayfaring are getting to your legs, and the atmosphere grows tense as some of your weaker companions are asking to be pulled on the carts for at least a few minutes.
            \n\n{color=#f6d6bd}Efren{/color} looks behind, then at you. “D’ye ever sing in {color=#f6d6bd}Hovlavan{/color} during work?” His words are so loud you have no doubt that the rest of the group also heard them.
            '
            '“We sing the songs of the sea. Sailors bring them to fishers and dockhands, and it spreads from taverns to homes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We sing the tunes of the sea. Sailors bring them to fishers and dockhands, and it spreads from taverns to homes.”')
                $ hovlavan_music = "shanties"
                menu:
                    '“How do they go?” You recognize [custom6]. You start with your favorite shanty, leading the group through the quick, repetitive melody as a lead, then giving them time to repeat the last few words.
                    \n\nOnce everyone learns how to follow, the woman replaces you, giving your poor throat some rest, but also adjusting the words slightly. {i}Ships{/i} turn into {i}boats{/i}, {i}krakens{/i} into {i}dragons{/i}. It’s hard to tell anymore if it’s a song about missing home from the waves of the ocean, or being lost in the woods.
                    '
                    'I stop singing altogether, annoyed that they reject the proper way.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is how stories grow, annoyed that they reject the proper way.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
                    'This is how stories grow.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is how stories grow.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
            '“We still remember the tunes from before the war. The cityfolk find strength when they hear tales of The Ten Cities.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We still remember the tunes from before the war. The cityfolk find strength when they hear tales of The Ten Cities.”')
                $ custom1 = "“How does”"
                $ hovlavan_music = "oldtunes"
                menu:
                    '“It will be easier to show us than describe it,” you recognize [custom6]. Having little breath to spare, you can’t be sure your voice reaches the last row of the expedition, but you do your best to portray the emperor Adir and the “fresh pork and bread” he brought to the tribes. It balances between solemnity and playfulness, and portrays a realm that has its worst days behind it.
                    \n\nOnce you’re done, the tribesfolk don’t say much until the woman with a big axe gets to your row and pats your back, then starts her own song that turns out to have an almost identical tune, yet the lyrics have almost nothing in common. It’s now a tale that indeed includes {i}pork{/i} and {i}bread{/i}, but they are just two of many foods that are now referencing either shell parts, or sexual acts.
                    \n\nShe keeps smiling throughout the entire tune and rests her hand on your shoulder. Some of the other wayfarers either laugh or sing along, and you hear two people clapping to the rhythm.
                    '
                    'For a bit, we move forward with our arms around each other’s backs.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- For a bit, we keep traveling with our arms around each other’s backs.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
                    'Without getting too awkward, I wait a moment and move away. I wonder which song is actually older.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without getting too awkward, I wait a moment and move away. I wonder which song is actually older.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
            '“Our songs are a bit more... {i}tame{/i} than the ones from the villages. Some themes sound too awkward when the priests are around.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Our songs are a bit more... {i}tame{/i} than the ones from the villages. Some themes sound too awkward when the priests are around.”')
                $ hovlavan_music = "tame"
                menu:
                    'You hear laughter, then [custom6]. “Not all songs need to be ‘bout shagging! Give us one or two, friend!”
                    \n\nYou pick a tune that has a noticeable rhythm, putting utility above meaning. “The Baker’s Chant,” as you know it, is a long, embellished instruction on preparing a proper loaf of bread, and while the steps keep changing, they are usually repeated twice, allowing the tribesfolk to join you. Many of them also clap, and the more confident you get with singing, the more goofy the situation gets, sparking a lot of laughter.
                    '
                    'I’m glad they’re having a good time.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m glad they’re having a good time.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
                    'I wish I had a better tune to offer.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish I had a better tune to offer.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent
            '“No. It would slow down the laborers.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. It would slow down the laborers.”')
                $ hovlavan_music = "no"
                $ creeks_reputation -= 1
                menu:
                    '“That’s stupid,” he lowers the wolf’s mouth. “Working gives folks rhythm, they get things done in the order they need.”
                    \n\nOnce you mention that everyone here just needs to keep up and that beasts won’t be so nice as to sneak up on you with steps louder than your singing, the man scoffs and drops the topic.
                    '
                    'I keenly observe all of the shrubs and tree crowns.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keenly observe all of the shrubs and tree crowns.')
                        $ travel_destination = "watchtower"
                        jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree07:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not watchtower_open:
            menu:
                '“We can eat here,” declares the hunter as you approach the watchtower, and asks the people behind him to spread the news. The carts and travelers gather in the middle of the crossroads, forming a defensive circle, while some of the folks unpack food rations. Before you sit down on the grass, {color=#f6d6bd}Efren{/color} hands you a large pear and asks you to follow him.
                \n\nHe pushes the locked door of the watchtower, to no success. “If there’s one spot on the eastern path we need the most, it’s this one, you understand,” he raises the wolf’s head. “Find a key if you can, there used to be some at the villages, though not too many of them. Not enough iron.”
                '
                '“I’ll speak with {color=#f6d6bd}Elah{/color} if I learn anything.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll speak with {color=#f6d6bd}Elah{/color} if I learn anything.”')
                    $ custom1 = "He nods and leads you back to one of the wagons, inviting you to sit down. Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                    jump creekselahaboutquesteasternroadfallentree07b
        elif watchtower_open == "axe":
            if quest_easternpath_description08aalt:
                menu:
                    '“We can eat here,” declares the hunter as you approach the watchtower, and asks the people behind him to spread the news. The carts and travelers gather in the middle of the crossroads, forming a defensive circle, while some of the folks unpack food rations. Before you sit down on the grass, {color=#f6d6bd}Efren{/color} gestures for you to join him. “Help me, aye?”
                    \n\nThe two of you approach a wagon covered with a rawhide. After the hunter pushes it aside, you instantly realize what the man plans to do. “It’s not much, but enough for the winter. Watch out for splinters.”
                    \n\nA few breaths later, you lean the new door against the wall, then start removing the old pieces of wood, throwing them away.
                    '
                    'It’s not hard work.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not hard work.')
                        $ quarters += 1
                        $ watchtower_open = "key"
                        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
                        menu:
                            'You make sure the door stands, and that the doorknob works. “Let’s put the old wood back on the cart. {color=#f6d6bd}Elah{/color} will play with it a bit, maybe we’ll put it back here in the spring.”
                            '
                            '“Sure.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure.”')
                                $ custom1 = "Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                                jump creekselahaboutquesteasternroadfallentree07b
                    '“I’m surprised {color=#f6d6bd}the carpenter{/color} built it so quickly.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised {color=#f6d6bd}the carpenter{/color} built it so quickly.”')
                        $ quarters += 1
                        $ watchtower_open = "key"
                        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
                        menu:
                            '“He didn’t,” the hunter points at the marks left by a spilt beverage. “It used to be a table. We have no way of making a lock, but maybe bears won’t learn how to turn a knob. Let’s put the old wood back on the cart, {color=#f6d6bd}Elah{/color} will play with it for a bit.”
                            '
                            '“Sure.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure.”')
                                $ custom1 = "Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                                jump creekselahaboutquesteasternroadfallentree07b
            else:
                if not watchtower_tower_bugs_cleared:
                    menu:
                        '“We can eat here,” declares the hunter as you approach the watchtower, and asks the people behind him to spread the news. The carts and travelers gather in the middle of the crossroads, forming a defensive circle, while some of the folks unpack food rations. Before you sit down on the grass, {color=#f6d6bd}Efren{/color} hands you a large pear and asks you to follow him.
                        \n\nOnce he gets to the broken door of the watchtower, he reaches for one of the planks and tries to move it. “Hwat? Shag me, that’s bad news, now a bear can move in,” he pushes it and gets inside, looking around. “And it’s swarming already...” He crosses the room and observes the furniture, especially the rotting barrels. “We’re here for the tree, so we won’t waste strength here. If you can, friend, try to get rid of, you know,” he points at a few large cockroaches. “If there’s one spot on the eastern path we need the most, it’s this one, you understand.”
                        '
                        '“I’ll speak with {color=#f6d6bd}Elah{/color} if I figure something out.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll speak with {color=#f6d6bd}Elah{/color} if I figure something out.”')
                            $ custom1 = "He nods and leads you back to one of the wagons, inviting you to sit down. Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                            jump creekselahaboutquesteasternroadfallentree07b
                else:
                    menu:
                        '“We can eat here,” declares the hunter as you approach the watchtower, and asks the people behind him to spread the news. The carts and travelers gather in the middle of the crossroads, forming a defensive circle, while some of the folks unpack food rations. Before you sit down on the grass, {color=#f6d6bd}Efren{/color} hands you a large pear and asks you to follow him.
                        \n\nOnce he reaches the broken door of the watchtower, he reaches for one of the planks and tries to move it. “Hwat? Shag me, that’s bad news, now a bear can move in,” he pushes it and gets inside, looking around. “At least nothing else lives here...” He crosses the room and observes the furniture, especially the rotting barrels. “We’re here for the tree, so we won’t waste strength here. But {color=#f6d6bd}Elah{/color} will be glad to learn we can start our work in spring, maybe summer.”
                        '
                        '“I’ll speak with him when we get back to the village.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll speak with him when we get back to the village.”')
                            $ custom1 = "He nods and leads you back to one of the wagons, inviting you to sit down. Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                            jump creekselahaboutquesteasternroadfallentree07b
        else:
            $ efren_friendship += 1
            $ pc_food = limit_pc_food(pc_food+1)
            show plus1food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
            menu:
                '“We can eat here,” declares the hunter as you approach the watchtower, and asks the people behind him to spread the news. The carts and travelers gather in the middle of the crossroads, forming a defensive circle, while some of the folks unpack food rations. Before you sit down on the grass, {color=#f6d6bd}Efren{/color} hands you a humble set of pears and cold, roasted meat, then steps away with a smile.
                \n\nYou hear him entering and exploring the tower. Once he gets back, he triumphantly raises his sharpened cudgel. “If there’s one spot on the eastern path we need the most, it’s this one, you understand,” the wolf’s head drops on his back, so he adjusts it. “And with your help, the tower is ours!”
                '
                'I smile back. “That’s right!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I smile back. “That’s right!”')
                    $ custom1 = "Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                    jump creekselahaboutquesteasternroadfallentree07b
                'I consider his words. The locals may not be too eager to give the tower back to the city soldiers.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider his words. The locals may not be too eager to give the tower back to the city soldiers.')
                    $ custom1 = "Some of the tribesfolk wander a bit farther away, searching the tall grasses for food, as if their habits are stronger than fear, but after the hunter orders them to regroup, they stay disciplined."
                    jump creekselahaboutquesteasternroadfallentree07b

        label creekselahaboutquesteasternroadfallentree07b:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            $ quarters += 1
            hide watchtowerbronzerod
            hide watchtower_campfire_fire
            if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                show areapicture fallentreetowatchtower_fixed at basicfade
            else:
                show areapicture fallentreetowatchtower at basicfade
            menu:
                '[custom1] After a short break, the expedition starts to restore its previous shape, while you and the hunter leave them behind, scouting ahead.
                \n\nThe overgrown path twists between the hills and bushes. “This route has issues much larger than a fallen tree,” your companion’s voice is tired and quiet. “Two, maybe three more years and it will be safer to block it completely.”
                \n\nBoth of you reach for your blades when a sudden cry comes from down the road. It resembles an ape, a young troll, or a human tormented by visions. It lasts for a few breaths and ends as abruptly as it started, but isn’t followed by any attack, or even footsteps.
                '
                '“Stay here.” I crawl my way up a hill, and observe the area through the shrubs.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Stay here.” I crawl my way up a hill, and observe the area through the shrubs.')
                    $ bestiary_goblins_mourn = 1
                    menu:
                        'You push away the leaves and once again hear the cry. It comes from one of the goblins gathered at the side of the road, none of which looks in your direction. Their thick furs in shades of brown and black make you realize that you’ve encountered the very same pack in this area before.
                        \n\nMost of them stand still and in silence, either on all fours or using their crude sticks and clubs to remain upright. Two, however, are hitting the ground with their fists and shaking the empty shell of yet another goblin, an {i}elder{/i} covered with gray fur, whose upper half is leaning against a tree, while the bottom half is a few feet away, in a puddle of blood. The guts spilling out of its stomach don’t suggest a promising diagnosis.
                        \n\nYou get back to {color=#f6d6bd}Efren{/color}, who’s too focused on his cudgel to adjust the tilted wolf’s head. “So?”
                        '
                        '“Goblins, more than a dozen. They’re mourning their dead leader.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Goblins, more than a dozen. They’re mourning their dead leader.”')
                            $ custom1 = "“So it’s been wailing? I didn’t know they cared, I mean they get caught by beasts as often as we do.” He then frowns, as if his words make him unsure, but after he shakes his head and adjusts his “hat”, his confident self returns. “Well, there’s more of them among the trees, keeping watch. Let’s gather a fair group of fighters and strike them first.”"
                            jump creekselahaboutquesteasternroadfallentree07bb
                        '“A small pack of goblins is too stupid to realize their leader is dead.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A small pack of goblins is too stupid to realize their leader is dead.”')
                            $ custom1 = "“Let’s hope they don’t know any dark magic,” he looks at you, as if seeking confirmation, and after a few quiet breaths he waves at you to follow him. “Well, there’s more of them among the trees, keeping watch. Let’s gather a fair group of fighters and strike them first.”"
                            label creekselahaboutquesteasternroadfallentree07bb:
                                menu:
                                    '[custom1]
                                    '
                                    '“Agreed. You know who to pick, and it won’t take long before the pack is crushed.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Agreed. You know who to pick, and it won’t take long before the pack is crushed.”')
                                        label creekselahaboutquesteasternroadfallentree07cnoafter:
                                            $ creeks_reputation += 1
                                            $ elah_quest_easternpath_goblins_coin = 1
                                            menu:
                                                'Once everyone’s ready, the battle takes not even a minute. The hunters, foragers, and woodcutters may not be experienced soldiers, but their light equipment allows them to get close to the pack, and once they’re noticed, their long, sharp spears and axes make their charge devastating. A few of the beasts, unaware of the scale of the threat, die before they can land a single hit, while the rest of them drop whatever they were holding and disappear among the leaves, too nimble for any human to catch up with them.
                                                \n\nA few of the tribesfolk are searching the area, removing goblin tusks from their jaws and pushing the corpses deeper into the bushes so that they won’t get caught in the wheels. {color=#f6d6bd}Efren{/color} takes a look at the weapons, but decides to only keep what seems like a human-made axe head and a rusty dagger.
                                                '
                                                '“Anything worth picking up?”':
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything worth picking up?”')
                                                    menu:
                                                        '“Not really, their furs smell like shit,” he considers handing you the dagger, but you realize it’s worth is negligible. “All of it needs some extra work. I’ll tell {color=#f6d6bd}Elah{/color} to pay you another dragon bone once we’re back.”
                                                        \n\nHe then orders his people to tell the carts and wagons to regroup, and you step away from the blood that reaches your boots slowly.
                                                        '
                                                        'I make sure no one got left behind.':
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure no one got left behind.')
                                                            $ travel_destination = "fallentree"
                                                            jump finaldestinationafterevent
                                    '“What? There’s no need to hurt them. They’ll flee from our loud wheels and large numbers.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What? There’s no need to hurt them. They’ll flee from our loud wheels and large numbers.”')
                                        if pc_class == "scholar":
                                            $ at_unlock_knowledge = 1
                                            $ at = 0
                                        menu:
                                            '“And hwy would you care?” His whisper gets louder, and you catch a hint of disgust. “The more of these vile creatures we take down, the more merciful the woods become for us.”
                                            '
                                            '“Fine, let’s do it your way.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, let’s do it your way.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                jump creekselahaboutquesteasternroadfallentree07cnoafter
                                            '“It’s a pointless risk.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a pointless risk.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "“Fighting monsters isn’t pointless,” he grabs the wolf’s mouth angrily, closing it for a few moments, “and we have long spears and heavy axes. We have nothing to fear.”"
                                                jump creekselahaboutquesteasternroadfallentree07cno
                                            '“The spirits will be angry if we murder wild creatures for no good reason.”' ( condition="(at != 'knowledge' and pc_religion == 'pagan') or (at != 'knowledge' and pc_religion == 'unknown')" ):
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The spirits will be angry if we murder wild creatures for no good reason.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "“All the {i}spirits{/i} of The Land wouldn’t wither a single daisy, even if they were fed with a pond of human blood. Don’t make me listen to dead stories.”"
                                                jump creekselahaboutquesteasternroadfallentree07cno
                                            'The people of Creeks don’t care much about gods and spirits. (disabled)' ( condition="(at == 'knowledge' and pc_religion == 'pagan') or (at == 'knowledge' and pc_religion == 'unknown')" ):
                                                pass
                                            '“Leaving blood and corpses will teach predators that there’s free food to pick here.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Leaving blood and corpses will teach predators that there’s free food to pick here.”')
                                                $ creeks_reputation += 1
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "He observes you for a bit, then hides his cudgel. “Good call. Let’s tell the others to have weapons at hand, and to make as much noise as they can.”"
                                                $ custom2 = "While one of the woodcutters mentions it’s {i}too bad{/i} there will be no goblin tusks for necklaces, he’s quickly told to use his wit. “Roadwarden says that blood lures beasts,” says a forager. “It’s better for us this way.”\n\nHearing the following “aye, aye” makes you confident in your judgment."
                                                jump creekselahaboutquesteasternroadfallentree07cyes
                                            '“Let’s not waste our strength before the actual work.”' ( condition="at != 'knowledge'" ):
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s not waste our strength before the actual work.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "“We are well prepared for goblins, don’t worry ‘bout that,” he points at your blade. “We have a few axes that are three times as long, and many spears. The beasts won’t know hwat hit them.”"
                                                jump creekselahaboutquesteasternroadfallentree07cno
                                            '“We don’t know how many of them there are. They may seek revenge once we reach the river.”' ( condition="at != 'knowledge'" ):
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We don’t know how many of them there are. They may seek revenge once we reach the river.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "“I would know if there were any massive packs of goblins in the peninsula. This one must be little, and we are well prepared for it,” he points at your blade. “We have a few axes that are three times as long, and many spears. The beasts won’t know hwat hit them.”"
                                                jump creekselahaboutquesteasternroadfallentree07cno
                                            'This pack is too small to present a real threat. (disabled)' ( condition="at == 'knowledge'" ):
                                                pass
                                            '“Beasts need goblins for food. Getting rid of them puts humans in danger.”' ( condition="at != 'knowledge'" ):
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Beasts need goblins for food. Getting rid of them puts humans in danger.”')
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "“Hwat difference will a few short apes make? These forests are full of wild beasts and plants, even the hills are green. We could kill a hundred goblins and it would change nothing.”"
                                                jump creekselahaboutquesteasternroadfallentree07cno
                                            'There’s plenty of food in the forest, a few goblins won’t make any difference. (disabled)' ( condition="at == 'knowledge'" ):
                                                pass
                                            '“Having this pack around sustains the road, even if only slightly.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Having this pack around sustains the road, even if only slightly.”')
                                                $ creeks_reputation += 1
                                                $ at_unlock_knowledge = 0
                                                $ at = 0
                                                $ custom1 = "He listens to the brief story of your previous encounter with the creatures, and crouches to inspect the beaten path. “Their footprints are here,” he says to himself, then stands up and fixes the wolf’s head. “Good call. Let’s tell the others to have weapons at hand, and to make as much noise as they can.”"
                                                $ custom2 = "While one of the woodcutters mentions it’s {i}too bad{/i} there will be no goblin tusks for necklaces, he’s quickly told to use his wit. “Roadwarden says the goblins scare beasts away from this road,” says a forager. “It’s better for us this way.”\n\nHearing the following “aye, aye” makes you confident in your judgment."
                                                jump creekselahaboutquesteasternroadfallentree07cyes

        label creekselahaboutquesteasternroadfallentree07cno:
            menu:
                '[custom1]
                '
                '“Fine, let’s do it your way.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, let’s do it your way.”')
                    jump creekselahaboutquesteasternroadfallentree07cnoafter
                '“Please, {color=#f6d6bd}Efren{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Please, {color=#f6d6bd}Efren{/color}.”')
                    $ custom1 = "The man squeezes the wolf’s head, taking it off for a few breaths. “Fine!” The sudden break of his whisper sounds to you like a shout. “But I see no wit in hwat you’re saying.”"
                    $ efren_friendship -= 1
                    $ custom2 = "One of the woodcutters mentions it’s {i}too bad{/i} there will be no goblin tusks for necklaces, and the others nod in agreement. “Roadwarden {i}asked{/i} for it,” a forager responds, starting a wave of chuckles."
                    jump creekselahaboutquesteasternroadfallentree07cyes

        label creekselahaboutquesteasternroadfallentree07cyes:
            $ achievement_animalssavedpoints += 1
            menu:
                '[custom1]
                \n\nOnce you reach the rest of the expedition, the instructions are clear and simple, though a few voices argue it would be better to fight. {color=#f6d6bd}Efren{/color} mentions your conversation and says that “we pay the roadwarden for guiding us, so we won’t ignore direct instructions.”
                \n\nYou make sure to be louder than you need, adding the occasional shout and the sounds of wooden handles hitting the wagons to the noise of boots and wheels. When you reach the bloody spot, you only find the legs and loins of the gray goblin.
                \n\n[custom2] {color=#f6d6bd}The hunter{/color} seems grumpy.
                '
                '“Don’t worry, {color=#f6d6bd}Efren{/color}. You have many journeys ahead of you.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry, {color=#f6d6bd}Efren{/color}. You have many journeys ahead of you.”')
                    $ travel_destination = "fallentree"
                    jump finaldestinationafterevent
                'I stay out of his way.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay out of his way.')
                    $ travel_destination = "fallentree"
                    jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree08:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ elah_quest_easternpath_lumberjacks = 2
        menu:
            '“That’s not too bad,” says [shoshi_namesmall] as you reach the fallen tree. “It’s thin, we can surround it.” The workers divide the tools and use the carts and wagons to form a barricade, explaining that they’ll move them once again when it comes to loading timber on them. You prepare your own belongings, when you notice that the tribe awaits your command.
            '
            '“You can start whenever you’re ready. I’ll keep an eye on our surroundings.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can start whenever you’re ready. I’ll keep an eye on our surroundings.”')
                show areapicture fallentree01alt behind fishtrap at basicfade
                $ quarters += 2
                if not fallentree_investigated_bushes:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found an arrow.{/i}')
                    if pc_class != "scholar":
                        $ custom2 = "You don’t know what type of bird would have such feathers."
                    else:
                        $ custom2 = "These feathers originally belonged to one of the local pheasants."
                    menu:
                        'The broken wagon is the first task that the workers take care of. The few dozen souls that arrived here would be enough to simply push the tree to one side, and what would be an exhausting task for lesser numbers will take them little time.
                        \n\nYou use the crags to observe the area, moving around without haste. The distracting noises of your group scare away many creatures - the eyes that observe you are mostly spread among tree crowns and the highest points of the hills. You spot a few ibexes, monkeys, and many birds, but no cats, runners, dragonlings, or wolves.
                        \n\nAfter some time, a forager approaches you, clearing her throat. “We found an arrow, too soggy to be used. But maybe you’ll know hwy it’s here?” You reach for it, and notice a head made of horn and black-orange fletching. [custom2]
                        '
                        '“Thanks.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                            $ item_arrow = 1
                            $ renpy.notify("You received an arrow.")
                            jump creekselahaboutquesteasternroadfallentree08b
                        '“M-hm. I’ll think about it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “M-hm. I’ll think about it.”')
                            $ item_arrow = 1
                            $ renpy.notify("You received an arrow.")
                            jump creekselahaboutquesteasternroadfallentree08b
                else:
                    menu:
                        'The broken wagon is the first task that the workers take care of. The few dozen souls that arrived here would be enough to simply push the tree to one side, and what would be an exhausting task for lesser numbers will take them little time.
                        \n\nYou use the crags to observe the area, moving around without haste. The distracting noises of your group scare away many creatures - the eyes that observe you are mostly spread among tree crowns and the highest points of the hills. You spot a few ibexes, monkeys, and many birds, but no cats, runners, dragonlings, or wolves.
                        '
                        'I miss sitting in a saddle.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I miss sitting in a saddle.')
                            jump creekselahaboutquesteasternroadfallentree08b

        label creekselahaboutquesteasternroadfallentree08b:
            $ fallentree_cleared = 1
            show areapicture fallentree02 behind fishtrap at basicfade
            $ quarters += 8
            $ quest_fallentree = 2
            $ quest_fallentree_description06 = "The road is now passable."
            $ renpy.notify("Quest completed: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fallen Tree{/i}')
            menu:
                'The saws and axes split the tree in a few spots at once, while the less experienced members of the group trim the branches and carry loads of wood, until they’re asked to replace the exhausted woodcutters. Then the work slows down, but never stops, and while the constant noise finally lures the presence of a small dragon that’s walking on four legs, each one as large as a human, seeing your large group makes it turn back - even though you would most likely be unable to pierce through its skin.
                \n\nAfter another few hours, no one has enough fortitude to start another conversation. Once the carts and wagons are ready, the crew demands a half an hour break.
                '
                'We can’t really avoid it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We can’t really avoid it.')
                    $ travel_destination = "stonebridge"
                    jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree09:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ pc_hp = limit_pc_hp(pc_hp-1)
        show minus1hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
        menu:
            'The road back is rough. The heavy blocks of wood require the dragging crew to takes turns every few minutes or so, hoping that no one will be pushed to exhaustion. Crossing the bridge is the worst part - lifting and dropping the vehicles is too dangerous for the primitive wheels, and one of them breaks, needing to be replaced on the spot. One of the foragers finally proposes heaping up soil into temporary, gentle slopes, which once again takes a lot of time.
            \n\nYou and {color=#f6d6bd}Efren{/color} sit down at the stream bank, observing the water. “Let’s hope we reach the tavern before nightfall,” he states simply.
            \n\nYou’re so exhausted that seeking an answer takes you a bit of a time.
            '
            '“{color=#f6d6bd}Elah{/color} asked me to put this painted plank somewhere around here,” I mutter and get up.' if not stonebridge_signpost and item_signpost:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elah{/color} asked me to put this painted plank somewhere around here,” I mutter and get up.')
                $ quarters += 2
                $ item_signpost = 0
                $ stonebridge_signpost = 1
                show areapicture stonebridge03 at basicfade
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                else:
                    $ renpy.notify("You built a signpost")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You built a signpost{/i}')
                $ quest_easternpath_description06alt = "I placed the sign at the path leading east of the old stone bridge."
                menu:
                    'The convenient remains of a shrub help you tie the plank above the ground. After a few minutes, you step away and take a look at the new sign.
                    '
                    'It may save someone’s life.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may save someone’s life.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
                    'I’d rather see people building new paths, not hide them.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather see people building new paths, not hide them.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
                    'I wonder if the days of iron nails are ever coming back.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if the days of iron nails are ever coming back.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
                    'What soul would enter a path that looks like this, anyway?':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- What soul would enter a path that looks like this, anyway?')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
                    'Well, that was easy.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, that was easy.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
            'I look at the workers. “You could use a better bridge. Maybe one made of wood.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the workers. “You could use a better bridge. Maybe one made of wood.”')
                menu:
                    '“Keeping it fixed would take many dangerous journeys. I’d rather see a {i}proper{/i} bridge made of stone, but the folks at {color=#f6d6bd}Old Págos{/color} haven’t made one in... however long they’ve been around,” he leans back, putting the weight of his back onto his arms and observing the darkening sky. “So maybe one day, when we have enough savings to buy the materials ourselves.”
                    \n\nOnce you’re ready for the rest of the journey, you really don’t feel like getting on your feet.
                    '
                    '“{i}Five{/i} dragons, huh,” I mutter.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Five{/i} dragons, huh,” I mutter.')
                        $ travel_destination = "foggylake"
                        $ quarters += 2
                        jump finaldestinationafterevent
                    '“Almost there!” I do my best trying to sound cheerful.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Almost there!” I do my best trying to sound cheerful.')
                        $ travel_destination = "foggylake"
                        $ quarters += 2
                        jump finaldestinationafterevent
            '“Where does this stream go, actually?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where does this stream go, actually?”')
                menu:
                    '“Oh, I don’t know. The sea, maybe? I think it goes through the heart of the woods, but the terrain here is so uneven I’ve no clue. Maybe it fills a big hole beneath a cave somehwere.”
                    \n\nOnce you’re ready for the rest of the journey, you really don’t feel like getting on your feet.
                    '
                    '“{i}Five{/i} dragons, huh,” I mutter.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Five{/i} dragons, huh,” I mutter.')
                        $ travel_destination = "foggylake"
                        $ quarters += 2
                        jump finaldestinationafterevent
                    '“Almost there!” I do my best trying to sound cheerful.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Almost there!” I do my best trying to sound cheerful.')
                        $ travel_destination = "foggylake"
                        $ quarters += 2
                        jump finaldestinationafterevent
            'I don’t feel like talking. I just listen to the water.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t feel like talking. I just listen to the water.')
                $ travel_destination = "foggylake"
                $ quarters += 2
                jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree10:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        nvl clear
        show areapicture foggylakeoutsideopen01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            '{color=#f6d6bd}Foggy{/color} and her crew welcome you at the gate, with their few tables, benches, and chairs moved outside the palisade, inviting everyone to sit down and eat, though more than a half of the crew has to sit down on the wagons. Two of the foragers refuse the meal, instead laying on the soft grass.
            \n\nYou all get a bowl of warm stew, heavy in fat, with snake eggs placed on top of a piece of pheasant meat. The vegetables are properly seasoned and juicy, though you’d love to have an extra pinch of salt. The worst part of the road is behind you, and while people remain quiet, they eat with enthusiasm.
            \n\n{color=#f6d6bd}The tavern keeper{/color} approaches you and {color=#f6d6bd}Efren{/color}. It may be dark, but you feel as if she’s covering you with a devouring shadow. “Well, loves, how’s the road? Worth the effort?”
            '
            'I try to keep the conversation going.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to keep the conversation going.')
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ foggy_friendship += 1
                $ quarters += 1
                menu:
                    'While {color=#f6d6bd}the hunter{/color} sighs, too tired to say a word, you indulge her appetite for gossip. You describe what you’ve seen, and as she scratches her large chin, she seems unsure what to say. “So the real gloom is behind the tower, but even before it we’d need more work...”
                    \n\nYou chit chat until {color=#f6d6bd}Efren{/color} starts to wake up the napping workers with his boot.
                    '
                    'I smile at her. “No time to waste, I guess.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile at her. “No time to waste, I guess.”')
                        $ travel_destination = "creeks"
                        jump finaldestinationafterevent
            'I say nothing, hoping for a bit of silence.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing, hoping for a bit of silence.')
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ efren_friendship += 1
                menu:
                    'As neither you nor {color=#f6d6bd}Efren{/color} speak up, he finally lets out a weak chuckle. “See, {color=#f6d6bd}Foggy{/color}? Don’t push us now, I’ll visit you soon and we’ll have a good talk.”
                    \n\nShe pats your backs with surprising strength, and you can’t tell if that’s because of her size, or rather the fact that you’re too weak to resist her hits. “Rest, rest,” her laughter attacks your ears. “I’ll see you when you have your tongues back.”
                    \n\nYour eyelids are already growing heavy when {color=#f6d6bd}Efren{/color} gets up and starts to wake up the napping workers with his boot.
                    '
                    'I make sure there’s nothing left in my bowl.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure there’s nothing left in my bowl.')
                        $ travel_destination = "creeks"
                        jump finaldestinationafterevent

    label creekselahaboutquesteasternroadfallentree11:
        $ elah_lastseen = day
        $ efren_lastseen = day
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ elah_quest_easternpath_lumberjacks = 0
        $ creeks_reputation += 1
        $ elah_friendship += 1
        $ efren_friendship += 0
        $ cleanliness = limit_cleanliness(cleanliness-3)
        show minus3appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
        menu:
            '“Saved!” A woman with a big axe crosses the gorge with laughter, and the expedition leaves the carts and wagons in front of the bridge. Seeing how dark it is, you’re not surprised to learn the unloading will occur after dawn. “Not like anyone’s going to steal it,” says one of the foragers, though everyone makes sure to take the remaining food rations. “We were lucky, but let’s not tempt the beasts,” says a hunter.
            \n\nThe rest of the tribe welcomes your group from the open gate, and relieved laughter fills the little village. They seem surprised to learn that no one got seriously wounded.
            \n\n{color=#f6d6bd}Elah{/color} and {color=#f6d6bd}Efren{/color} share a brief embrace, but {color=#f6d6bd}the carpenter{/color} doesn’t hesitate to mention {color=#f6d6bd}the hunter’s{/color} smell. You realize you also need a long bath.
            '
            'Time to collect my reward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to collect my reward.')
                jump creekselahaboutquesteasternroadfallentree11a
            'If they betray me now I’ll kill them all.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If they betray me now I’ll kill them all.')
                jump creekselahaboutquesteasternroadfallentree11a

        label creekselahaboutquesteasternroadfallentree11a:
            $ creeks_reputation += 1
            $ elah_friendship += 1
            $ quarters += 1
            if not elah_quest_easternpath_goblins_coin:
                $ custom1 = "“Five dragons is a lot, but I’d pay four times as much for keeping everyone safe. You did a good job, friend.”"
            else:
                $ custom1 = "“I’m meant to pay you one more dragon... So be it, I’d pay four times as much for keeping everyone safe. You did a good job, friend.”"
            menu:
                '{color=#f6d6bd}The carpenter{/color} reaches for a lit torch and asks you to follow him. [custom1]
                \n\nHe opens the wooden cask and counts down the pieces of bone. “Tell me, [pcname], hwat d’you think? How’s the road? You now know how a merchant may feel on it.”
                '
                '“It could be worse.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It could be worse.”')
                    $ custom1 = "“Oh, I bet!” He pats his stomach and pushes the coins toward you. “It’s all just a beginning, but so far I’ve no doubt we’re moving in the right direction.”"
                    jump creekselahaboutquesteasternroadfallentree11b
                '“It’s shit. You need a year-long roadwarden, or a group of soldiers.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s shit. You need a year-long roadwarden, or a group of soldiers.”')
                    $ custom1 = "He clenches his stomach and taps the coins before he pushes them to you. “So I need to get {i}really good{/i} with the saw and chisel this winter, good enough to start selling my work to other tribes. Dragons won’t grow in our fields.”"
                    jump creekselahaboutquesteasternroadfallentree11b
                '“It’s empty, but beautiful. Even the old, abandoned structures.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s empty, but beautiful. Even the old, abandoned structures.”')
                    $ custom1 = "He gives you a surprised look. “Not an answer I was expecting,” he pushes the coins toward you with a single, confident gesture. “The few times I traveled to {color=#f6d6bd}Gale Rocks{/color} I mostly saw rocks to crush, trees to chop, meadows to forage at. Though I’d expect you need to feel {i}some{/i} pleasure from traveling, or you’d go insane.”"
                    jump creekselahaboutquesteasternroadfallentree11b
                '“You realize I’ve seen many, {i}many{/i} roads? There’s nothing unique about this one. Protect it, and it’ll be safer. Neglect it, and it will be lost.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You realize I’ve seen many, {i}many{/i} roads? There’s nothing unique about this one. Protect it, and it’ll be safer. Neglect it, and it will be lost.”')
                    $ custom1 = "He gives you a long look and finally nods. His lips are pursed, until they shape a sad smile. “You’re right, it was just one of many days in the wilderness for you. I often forget that there’s a vast world outside of the peninsula. Maybe we {i}can{/i} shape this small scrap of land with hard work.”"
                    $ elah_friendship += 1
                    jump creekselahaboutquesteasternroadfallentree11b

    label creekselahaboutquesteasternroadfallentree11b:
        if not elah_quest_easternpath_goblins_coin:
            $ coins += 5
            show screen notifyimage( "Journal updated: The Eastern Path.\n+5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +5 {image=cointest}{/i}')
        else:
            $ coins += 6
            show screen notifyimage( "Journal updated: The Eastern Path.\n+6", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path. +6 {image=cointest}{/i}')
        $ quest_easternpath_points += 3
        $ quest_easternpath_description09aa = "I received my reward for assisting the villagers in removing the fallen tree."
        menu:
            '[custom1]
            '
            '“I’m a bit tired, {color=#f6d6bd}Elah{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m a bit tired, {color=#f6d6bd}Elah{/color}.”')
                jump creekselahonquest_easternpathcalculatingresults00
            'I wait patiently.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait patiently.')
                jump creekselahonquest_easternpathcalculatingresults00
