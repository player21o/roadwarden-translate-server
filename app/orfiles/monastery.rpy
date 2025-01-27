###################### Monastery
# Kapłani - distanced do stukania w patyk. Prelate Prisca - vulnerable, bardzo stara, okryta cieniem, słaby głos, nie przemieszcza się
# mnich Aeli - hoarse voice, liver spots, pale face, snorts
# młoda mniszka? - Decima. humble, black hair, short, small, doesn't talk

default monastery_name = "The Monastery"
default monastery_firsttime = 0
default monastery_firsttime_badimpression = 0
default monastery_cave_firsttime = 0
default monastery_sleep_unlocked = 0
default monastery_fluff = ""
default monastery_fluff_old = ""
default monastery_friendship = 0
default monastery_betrayal_available = 0
default monastery_betrayal_blocked = 0
default monastery_betrayal_done = 0

default monastery_lies_decima = 0
default monastery_prelate_invited = 0
default monastery_promise = 0 # 1 = można odebrać nagrodę, 2 - już odebrana

default aeli_quest_pens = 0
default aeli_quest_pens_gray = 0
default aeli_quest_pens_question = 0
default aeli_quest_pens_question2 = 0
default aeli_quest_pens_question_eudocia = 0
default aeli_quest_pens_question_reward = 0
default aeli_quest_pens_reward = 0

default aeli_about_monastery = 0
default aeli_about_plague1 = 0
default aeli_about_plague2 = 0
default aeli_about_sleeping1 = 0
default aeli_about_bronzerod = 0
default aeli_about_bronzerod_ignored = 0
default aeli_about_bronzerod_honored = 0
default aeli_about_asterion = 0
default aeli_about_asterion_help = 0
default aeli_about_buyingorselling = 0
default aeli_about_buyingorselling_alt = 0
default aeli_about_buyingorselling2 = 0
default aeli_about_buyingorselling_chicken_firsttime = 0
default aeli_about_buyingorselling_chicken_day = 0
default aeli_about_buyingorselling_chicken_friendship_counter = 0
default aeli_about_sharpeningpotion = 0
default aeli_about_sharpeningpotion_timer = 0
default aeli_about_sharpeningpotion_collected = 0
default aeli_about_alchemytable = 0
default aeli_about_powderedbasalt = 0
default aeli_about_powderedbasalt_gray = 0
default aeli_about_necromancers = 0
default aeli_about_necromancers_question01 = 0
default aeli_about_necromancers_question02 = 0
default aeli_about_necromancers_question03 = 0
default aeli_about_necromancers_question04 = 0
default aeli_about_necromancers_question05 = 0
default aeli_about_necromancers_bloodmagic = 0
default aeli_about_nomoreundead = 0
default aeli_about_asteriontablet = 0
default aeli_about_thaisletter = 0
default aeli_about_shortcut = 0
default aeli_about_missinghunters = 0
default aeli_about_steephouse = 0
default aeli_about_bandits = 0
default aeli_about_highisland = 0
default aeli_about_spiritrock = 0
default aeli_about_fulvia = 0
default aeli_about_copper = 0

default aeli_about_monasteryname = 0
default aeli_about_thisplace = 0
default aeli_about_leader = 0
default aeli_about_theirfaith = 0
default aeli_about_hiddenknowledge = 0
default aeli_about_aeli = 0

default aeli_about_secret_highisland = 0
default aeli_about_secret_asterion = 0
default aeli_about_secret_cave = 0
default aeli_about_snakebait = 0

default aeli_golems_learned01 = 0
default aeli_golems_learned03 = 0
default aeli_golems_learned03b = 0
default aeli_golems_learned04b = 0
default aeli_golems_clues_counter = 0
default aeli_golems_clues_three = 0
default aeli_golems_reward_available = 0

label monastery01:
    nvl clear
    $ pc_area = "monastery"
    $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
    play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    label monastery_fluffloop:
        $ monastery_fluff = renpy.random.choice(['The river is attacking its banks fiercely, filling the valleys with its roar.', 'Hit by the cold, howling wind, you adjust your cloak.', 'A white-and-black eagle is circling around you, but leaves you alone before you reach the monastery.', 'A large, red saurian is lying in the middle of the path, basking in the sun, but flees at your sight, climbing down the rocks as if they’re a floor.', 'You spot a movement in the thicket far below you. A massive bear is hunting for fish in the river.', 'A carcass of an ibex floats down the river, nervously followed by rooks. They eat it one dab at a time.', 'A brown-and-golden monkey is sneaking around the hourglass, avoiding the looks of the dwellers.'])
        if monastery_fluff_old == monastery_fluff:
            jump monastery_fluffloop
        else:
            $ monastery_fluff_old = monastery_fluff
    if quarters < 32:
        $ monastery_monks_fluff = "You spot only a few hooded figures. Two youngsters help an elder on her walk through the fields, one is running up and down the stairs, another one washes himself in the brook."
    elif quarters < ((world_daylength/2)+11)-4:
        $ monastery_monks_fluff = "You spot more than a dozen hooded figures absorbed by their work in the fields and among the fruit trees. One of them is hanging by the hourglass, polishing it with a cloth."
    elif quarters < ((world_daylength/2)+11):
        $ monastery_monks_fluff = "A few hooded figures are climbing up the paths. Their tired, exalted singing mixes with the wind."
    elif quarters < (((world_daylength/2)+11)+8):
        $ monastery_monks_fluff = "There’s no soul in sight. From the mountain comes a cheerful singing of a woman, though you can’t understand a single word."
    elif quarters < (world_daylength-12):
        $ monastery_monks_fluff = "You spot just a few hooded figures by the brook. The loud thudding of tools that comes from the cave mouths echoes through the valley."
    elif quarters < (world_daylength-4):
        $ monastery_monks_fluff = "A few monks are training in the yard, clashing their wooden staves loudly. A colorful smoke leaves one of the cave mouths."
    else:
        $ monastery_monks_fluff = "You spot two groups of hooded figures with lanterns in their hands, either patrolling the area, or strolling around."
    if not monastery_firsttime:
        show areapicture monastery01 at basicfade
    else:
        show areapicture monastery01gateopen at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not monastery_firsttime:
        $ world_known_npcs += 1
        $ world_known_areas += 1
        $ monastery_firsttime = 1
        $ world_known_areas += 1
        $ oldpagos_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        jump monasteryfirsttime01
    else:
        show areapicture monastery01gateopen at basicfade
        jump monasteryregular01

######################################################
label monasteryfirsttimeALL:
    label monasteryfirsttime01:
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'You approach the raised drawbridge and observe the face of the mountain. The hooks holding the hourglass are as large as a person, displaying their devotion to The Wright proudly.
            '
            'It took tremendous wealth and labor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It took tremendous wealth and labor.')
                jump monasteryfirsttime01a
            'What a waste of steel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- What a waste of steel.')
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth":
                    $ pc_faithpoints -= 1
                if pc_religion == "pagan":
                    $ pc_faithpoints += 1
                jump monasteryfirsttime01a
            'I wonder who’s responsible for polishing it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder who’s responsible for polishing it.')
                jump monasteryfirsttime01a
            'The temples in the city are even grander.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The temples in the city are even grander.')
                label monasteryfirsttime01a:
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        'The rustling of leaves carries no songs of birds, shouts of apes, or whines of hunted critters. The river attacks its banks with a fierce roar. You get off your palfrey.
                        \n\nThe cave mouths are connected by paths, stairs, and bridges. You don’t see any people, but there’s smoke coming from one of the entrances, and you hear muffled thuds of a hammer. The gardens are weeded, the buildings firm. The green trees on the top of the mountain bear red and brown fruits.
                        \n\nTwo rounded sticks are tied with a rope to a nearby rock. You grab them and take a closer look - they’re claves.
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        'I make a few firm hits and shout a greeting at anyone who shows up near the building.' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I make a few firm hits and shout a greeting at anyone who shows up near the building.')
                            $ at_activate = 0
                            $ at = 0
                            $ monastery_friendship += 0
                            $ minutes += 10
                            jump monasteryfirsttime02friendly
                        'I play a tune from a silly counting-out rhyme.' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I play a tune from a silly counting-out rhyme.')
                            $ at_activate = 0
                            $ at = 0
                            $ monastery_friendship -= 1
                            $ minutes += 5
                            jump monasteryfirsttime02playful
                        'I make a few firm hits, then wait patiently.' ( condition="at == 'distanced' and pc_religion != 'ordersoftruth'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I make a few firm hits, then wait patiently.')
                            $ at_activate = 0
                            $ at = 0
                            $ monastery_friendship += 1
                            $ minutes += 10
                            jump monasteryfirsttime02distanced
                        'I know an Order of Truth when I see one. I make a few firm hits, then wait patiently.' ( condition="at == 'distanced' and pc_religion == 'ordersoftruth'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I know an Order of Truth when I see one. I make a few firm hits, then wait patiently.')
                            $ at_activate = 0
                            $ at = 0
                            $ monastery_friendship += 1
                            $ minutes += 10
                            jump monasteryfirsttime02distanced
                        'I keep hitting them until someone lowers the bridge.' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I keep hitting them until someone lowers the bridge.')
                            $ at_activate = 0
                            $ monastery_friendship -= 1
                            $ minutes += 4
                            jump monasteryfirsttime02intimidating
                        'I hit them just three times, not too loud.' ( condition="at == 'vulnerable'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I hit them just three times, not too loud.')
                            $ at_activate = 0
                            $ at = 0
                            $ monastery_friendship += 0
                            $ quarters += 1
                            jump monasteryfirsttime02vulnerable

    label monasteryfirsttime02friendly:
        show areapicture monastery01gateopen at basicfade
        menu:
            'The echo of your hits cuts through the swashing stream. After a few minutes, {color=#f6d6bd}two hooded figures{/color} leave a cave mouth at the top of the mountain and give you a long look from the edge of the cliff, then walk down the path with caution.
            \n\nYou smile and wave to them before they disappear behind the buildings, which are made of bricks, not logs, and are covered with tiles instead of thatch.
            \n\nLittle by little, the bridge gets looser, then it hits the grass gently. The taller figure, now covered with shadows, invites you with a gesture.
            '
            'I lead {color=#f6d6bd}[horsename]{/color} inside. “Greetings!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead {color=#f6d6bd}%s{/color} inside. “Greetings!”' %horsename)
                menu:
                    '“And greetings to ye...” He hesitates. His voice is hoarse, but sonorous. “Salutations to {i}thou{/i}, traveler.” He puts his bandaged hand on his waist. “You’re at Wright’s haven.”
                    \n\nThe greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03

    label monasteryfirsttime02playful:
        show areapicture monastery01gateopen at basicfade
        menu:
            'The echo of your hits cuts through the swashing stream. Soon, {color=#f6d6bd}two hooded figures{/color} leave a cave mouth at the top of the mountain and give you a quick look from the edge of the cliff, then walk down the path, quickly, but with caution. It takes them a while to reach the buildings, made of bricks, not logs, and covered with tiles instead of thatch.
            \n\nLittle by little, the bridge gets looser, then it hits the grass gently. The shorter figure stays in the shadows, while the taller one steps outside.
            \n\n“This is the place of reflection and prayer, traveler!” The man’s voice is hoarse, but sonorous. The echo gives it an eerie sound. “Ye...” He hesitates, but then points at you with his bandaged hand. “{i}Thou{/i} shalt show the due reverence!”
            '
            'I nod and apologize.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and apologize.')
                menu:
                    'He lowers his hand. “You’re at Wright’s haven. Come.” He turns around and returns to {color=#f6d6bd}his companion{/color}. You lead {color=#f6d6bd}[horsename]{/color} inside.
                    \n\nThe greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03
            'I shrug.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                $ monastery_friendship -= 1
                $ monastery_firsttime_badimpression = 1
                menu:
                    'He stands in silence for a few heartbeats, then finally turns around and returns to {color=#f6d6bd}his companion{/color}. You lead {color=#f6d6bd}[horsename]{/color} inside.
                    \n\nThe greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03

    label monasteryfirsttime02distanced:
        show areapicture monastery01gateopen at basicfade
        menu:
            'The echo of your hits cuts through the swashing stream. After a few minutes, {color=#f6d6bd}two hooded figures{/color} leave a cave mouth at the top of the mountain and give you a long look from the edge of the cliff, then walk down the path with caution. It takes them a while to reach the buildings, made of bricks, not logs, and covered with tiles instead of thatch.
            \n\nLittle by little, the bridge gets looser, then it hits the grass gently. The taller figure, now covered with shadows, invites you with a gesture.
            '
            'I lead {color=#f6d6bd}[horsename]{/color} inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead {color=#f6d6bd}%s{/color} inside.' %horsename)
                menu:
                    'The greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    \n\n“Salutations, traveler, and thank ye...” He hesitates. His voice is hoarse, but sonorous. “Thank {i}thou{/i} for thy patience. This is the place of reflection and prayer, we sh... We {i}shan’t{/i} abandon our duties.” He puts his bandaged hand on his stomach and bows. “You’re at Wright’s haven, the last place of peace in the North. As long as thy tongue is clean of lies and thy hands bring no harm, thou wilt not be hurt.”
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03

    label monasteryfirsttime02intimidating:
        show areapicture monastery01gateopen at basicfade
        menu:
            'The echo of your hits cuts through the swashing stream. Soon, {color=#f6d6bd}two hooded figures{/color} leave a cave mouth at the top of the mountain and give you a quick look from the edge of the cliff, then walk down the path, quickly, but with caution. It takes them a while to reach the buildings, made of bricks, not logs, and covered with tiles instead of thatch.
            \n\nLittle by little, the bridge gets looser, then it hits the grass gently. The shorter figure stays in the shadows, while the taller one steps outside.
            \n\n“This is the place of reflection and prayer, traveler!” The man’s voice is hoarse, but sonorous. The echo gives it an eerie sound. “Ye...” He hesitates, but then points at you with his bandaged hand. “{i}Thou{/i} shalt show the due reverence!”
            '
            'I nod.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                menu:
                    'He lowers his hand. “You’re at Wright’s haven. Come.” He turns around and returns to {color=#f6d6bd}his companion{/color}. You lead {color=#f6d6bd}[horsename]{/color} inside.
                    \n\nThe greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03
            'I don’t say anything.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t say anything.')
                $ monastery_friendship -= 1
                $ monastery_firsttime_badimpression = 1
                menu:
                    'He stands in silence for a few heartbeats, then finally turns around and returns to {color=#f6d6bd}his companion{/color}. You lead {color=#f6d6bd}[horsename]{/color} inside.
                    \n\nThe greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03

    label monasteryfirsttime02vulnerable:
        show areapicture monastery01gateopen at basicfade
        menu:
            'The echo of your hits hardly cuts through the swashing stream. After a few minutes without a response, you try again, and then once more.
            \n\nFinally, {color=#f6d6bd}two hooded figures{/color} leave a cave mouth at the top of the mountain and give you a long look from the edge of the cliff, then walk down the path with caution. It takes them a while to reach the buildings, made of bricks, not logs, and covered with tiles instead of thatch.
            \n\nLittle by little, the bridge gets looser, then it hits the grass gently. The taller figure, now covered with shadows, invites you with a gesture.
            '
            'I lead {color=#f6d6bd}[horsename]{/color} inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead {color=#f6d6bd}%s{/color} inside.' %horsename)
                menu:
                    'The greeters take off their hoods. They wear brown, dark, simple, worn robes, and ropes instead of belts. They’ve no jewelry or ornaments, just small bags made of fabric on their shoulders.
                    \n\nThe larger shell belongs to a strong, barefoot man in his fifties. Despite having no weapon, his eyes are audacious, and could belong to a muscle standing in the door of a harbor tavern. His wrinkles are subtle, but there are only a few tufts of gray hair left on his greasy head. His skin is pale, covered with liver spots, though at a closer look you realize a few of them are just stains left by ink.
                    \n\n“Salutations, traveler, but next time be a bit louder. This is the place of reflection and prayer, we may not always hear ye...” He hesitates. His voice is hoarse, but sonorous. “Hear {i}thou{/i}.” He puts his bandaged hand on his stomach and bows gently. “You’re at Wright’s haven.”
                    '
                    'I look at the second monk.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the second monk.')
                        jump monasteryfirsttime03

    label monasteryfirsttime03:
        menu:
            'The girl is about fourteen, with unsightly acne on her forehead and a robe that brushes the ground whenever she takes a step. Her black hair is tied into a humble ponytail. She observes your horse curiously, cocking her head to a side, but once she catches your look, she meets your eyes boldly, raising her chin as if to challenge you.
            \n\n“Thy mount is free to help itself with hay and water, we’ll wait outside. Ye... {i}Thou{/i} canst stay here for now, but leave before the night. The plague is nearby, the struggle ahead.” While they indeed leave the room, their trust only goes so far - they observe you through the open door.
            \n\nThe building is a single store room, filled with crates and barrels, a stack of firewood and another one of bricks, a pile of straw, a chest, two wheelbarrows, and finally the racks, shelves, tools, clothing, and utensils. The light comes from the open gates, accompanied by the sharp draft.
            '
            'I tether {color=#f6d6bd}[horsename]{/color} near the water trough and join the monks.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} near the water trough and join the monks.' %horsename)
                menu:
                    'The lack of walls makes you feel exposed. A few pairs of eyes observe you from the paths above you, while others either climb to the very top, or approach the unremarkable vegetable beds. Most of the dwellers wear hoods, and all of them wear similar, worn robes.
                    \n\nA chilling wind touches your neck.
                    '
                    'I’m not afraid of some wind.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not afraid of some wind.')
                        jump monasteryfirsttime03c
                    'I put on my hood.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put on my hood.')
                        jump monasteryfirsttime03c

    label monasteryfirsttime03c:
        menu:
            'They keep their distance. The man greets you by raising his open palm, wrapped with bandages that disappear underneath his sleeve. His lips form something between a sneer and a smile. “What brings thee here? Art thou a go-between?”
            \n\nThe girl keeps an eye on your axe and occasionally glances at your boot - the one that hides a knife.
            '
            '“I’m [pcname], the new roadwarden.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, the new roadwarden.”' %pcname)
                menu:
                    '“Good, well. The roads need their wardens, the folks need their roads. But there are none behind this mountain, and we take care of the one that you’ve just crossed. Ye... {i}thou{/i} dost not need to bother. Thy services are not required.”
                    \n\nHe gestures for you to wait. “But where’s the man with a red beard? There isn’t enough work here for the two of you.”
                    '
                    '“{color=#f6d6bd}Asterion{/color}. I was hoping to find him here.”' if not asterion_found:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color}. I was hoping to find him here.”')
                        $ description_aeli00 = "The monk who speaks in the name of the local monastery introduced himself as {color=#f6d6bd}Aeli{/color}."
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "monastery1"
                        menu:
                            '“I’m sorry to disappoint thee,” he rubs a liver spot on his hand, “but he hasn’t been here in months. We rarely have visitors different than our friends from {color=#f6d6bd}Old Págos{/color}. We don’t invite the outside world, and we don’t care much for it. Hast thou checked in {color=#f6d6bd}Pelt of the North{/color} on the southern road? If he’s wounded, it’s a safe shelter, I’ve heard.”
                            \n\nThe girl scratches the ground with her boot, though it remains hidden underneath her robe. The man looks at her with amusement. “Looks like {color=#f6d6bd}Decima{/color} here is {i}eager{/i} to return to her duties. I’m {color=#f6d6bd}Aeli{/color}, but I’ll not shake thy hand. One of us could carry the plague in our flesh. Who can know, who can tell. What brings thee to our monastery?”
                            '
                            '(monastery1 preset)':
                                pass
                    '“{color=#f6d6bd}Asterion{/color}. He’s gone, I’m afraid.”' if asterion_found:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color}. He’s gone, I’m afraid.”')
                        $ description_aeli00 = "The monk who speaks in the name of the local monastery introduced himself as {color=#f6d6bd}Aeli{/color}."
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "monastery1"
                        menu:
                            'You begin your tale, but the man waves it off. “We don’t invite the outside world, nor do we crave rumors. Gone means gone. All of this is beyond our duties.”
                            \n\nThe girl scratches the ground with her boot, though it remains hidden underneath her robe. The man looks at her with amusement. “Looks like {color=#f6d6bd}Decima{/color} here is {i}eager{/i} to return to her duties. I’m {color=#f6d6bd}Aeli{/color}, but I’ll not shake thy hand. One of us could carry the plague in our flesh. Who can know, who can tell. What brings thee to our monastery?”
                            '
                            '(monastery1 preset)':
                                pass
                    '“Have you seen the roads here? They’re messy enough for ten more.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you seen the roads here? They’re messy enough for ten more.”')
                        $ description_aeli00 = "The monk who speaks in the name of the local monastery introduced himself as {color=#f6d6bd}Aeli{/color}."
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "monastery1"
                        menu:
                            '“Ha! That may very well be. It’s been many years since I touched the paths beyond these mountains. Few Northerners care about Wright’s teachings, the real wisdom. Their deeds and gossip will soon not matter. {i}This{/i} is the place of eternal tales, of stories that shape us all. Not of little lives and simple words.”
                            \n\nThe girl scratches the ground with her boot, though it remains hidden underneath her robe. The man looks at her with amusement. “Looks like {color=#f6d6bd}Decima{/color} here is {i}eager{/i} to return to her duties. I’m {color=#f6d6bd}Aeli{/color}, but I’ll not shake thy hand. One of us could carry the plague in our flesh. Who can know, who can tell. What brings thee to our monastery?”
                            '
                            '(monastery1 preset)':
                                pass

######################################################

label monasteryregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if monastery_friendship < 0:
        $ custom1 = "steps on the wooden beams, not inviting you to come inside. “Warden. What art thou looking for?”"
    elif monastery_friendship < 8:
        $ custom1 = "gestures for you to enter the storage house with his bandaged hand. “Warden,” he nods. “Is all alright?”"
    else:
        $ custom1 = "welcomes you with a cheerful wave of his bandaged hand. “Salutations. Glad to see thee in one piece.”"
    if monastery_friendship < 0:
        $ custom2 = "observing you with an unpleasant smirk."
    elif monastery_friendship < 8:
        $ custom2 = "observing your palfrey."
    else:
        $ custom2 = "observing the sky with a wide grin."
    $ questionpreset = "monastery1"
    menu:
        '[monastery_fluff] [monastery_monks_fluff]
        \n\nYou call the monks by hitting the sticks, and the drawbridge lowers. {color=#f6d6bd}Aeli{/color} [custom1] His {color=#f6d6bd}young companion{/color} is right next to him, [custom2]
        '
        '(monastery1 preset)':
            pass

label monasteryafterinteractions01a:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s return to my other questions.”')
    label monasteryafterinteractions01:
        $ custom1 = renpy.random.choice(['“I don’t promise you any answers.”', '“What bothers ye... {i}Thou{/i}?”', '“Well?”', 'He rubs his bandaged wrist.', '“What else?”'])
        label monasteryafterinteractions01alt:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "monastery1"
            menu:
                '[custom1]
                '
                '(monastery1 preset)':
                    pass

label monasterywakingupshed:
    nvl clear
    show areapicture monastery01gateopen at basicfade
    $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
    play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ questionpreset = "monastery1"
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        'Your shell feels weaker than your soul. During your morning routine, your eyes remain a bit cloudy. You keep looking around, time and time again making sure that no one is watching you.
        \n\nThe first few monks are entering the yard, carrying their tools and whispering lazy conversations as they wash themselves in the brook. Soon after that, {color=#f6d6bd}Aeli{/color} knocks on the door of the shed and opens it. {color=#f6d6bd}His companion{/color} is holding her hands behind her back, giving you the charming smile of an innocent child.
        '
        '(monastery1 preset)':
            pass

######################################################

label aeli_about_monasteryALL:
    label aeli_about_monastery01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the monastery.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ questionpreset = "monastery1aboutmonastery"
        menu:
            '“And what could those be?”
            '
            '(monastery1aboutmonastery preset)':
                pass

    label aeli_about_name01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does this place have a name? Or is it just {i}the monastery{/i}?”')
        $ aeli_about_monasteryname = 1
        $ aeli_about_monastery += 1
        $ description_galerocks15 = "According to {color=#f6d6bd}Aeli{/color}, the village has a small temple dedicated to The Wright."
        $ questionpreset = "monastery1aboutmonastery"
        menu:
            '“Depends on who thou ask...est. It’s the largest temple on this side of {color=#f6d6bd}Hag Hills{/color}, and the only one beside the sacred cave in {color=#f6d6bd}Gale Rocks{/color}.” He points at the huge hourglass. “Is it Wright’s Summit? Or The Temple of Old Págos? Or High Caves, like they used to be for my nana?”
            \n\nHe rests his thumbs behind the rope on his waist. “The tribes come and go, the names shift. For now, we all know what we mean by {i}the monastery{/i}.”
            '
            '(monastery1aboutmonastery preset)':
                pass

    label aeli_about_thisplace01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about your order?”')
        $ aeli_about_thisplace = 1
        $ aeli_about_monastery += 1
        $ minutes += 5
        $ questionpreset = "monastery1aboutmonastery"
        menu:
            '“How does one describe the air they swallow, the water they draw each day?” His contemptuous, yet playful smile makes it clear he doesn’t seek your answer. “I can tell thee it’s not old, but older than thou, and that its monks work and pray. But it’s not a place, nor a congregation. Words don’t reflect our purpose, for human tongue is meager and stupid, and so are our ears.
            \n\nHe straightens up and puts on a more serious tone. “We look for knowledge, knowing we’ll not uncover The Truth. We study herbs, mushrooms, rocks, and winds. {color=#f6d6bd}Old Págos{/color} feeds us, and we take care of its orphans,” he glances at {color=#f6d6bd}Decima{/color}, “heal its sick, write down its stories. We silence our thoughts, fix our past wrongdoings, seek peace in understanding. I’ve seen and touched stuff I can’t even name, and they were delightful. I now find no difference between what I do to keep my shell alive, and what to fulfill The Wright’s will.”
            \n\nAn old woman without her hood, who leans forward while walking, exits one of the caves and walks along the rock face, from time to time stopping in place to watch the garden. The scars on her face can’t distort her kind smile.
            '
            '(monastery1aboutmonastery preset)':
                pass

    label aeli_about_leader01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does this place have any {i}leader{/i} of sorts?”')
        $ custom1 = "{color=#f6d6bd}our prelate{/color} was"
        label aeli_about_leader01after:
            $ aeli_about_leader = 1
            $ aeli_about_monastery += 1
            menu:
                'He crosses his arms and takes a look at the cave mouth behind him, then gives you a harsh look.
                \n\n“If [custom1] willing to see thee, they’d let thee know.”
                '
                '“I’m willing to prove that I’m trustworthy.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m willing to prove that I’m trustworthy.”')
                    $ questionpreset = "monastery1aboutmonastery"
                    menu:
                        '“We’ll see. Maybe.”
                        '
                        '(monastery1aboutmonastery preset)':
                            pass
                '“Can’t they spare a traveler a few moments?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can’t they spare a traveler a few moments?”')
                    $ questionpreset = "monastery1aboutmonastery"
                    menu:
                        'He hesitates. “They see no reason to do so.”
                        '
                        '(monastery1aboutmonastery preset)':
                            pass

        label aeli_about_leader01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could I speak with your prelate?”')
            $ custom1 = "they were"
            jump aeli_about_leader01after

    label aeli_about_theirfaith01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about your faith.”')
        $ aeli_about_theirfaith = 1
        $ aeli_about_monastery += 1
        menu:
            'He takes a deep breath, puts on the hood, and closes his eyes. His voice, while still hoarse, becomes monotone, like a scribe reading a list of the dead.
            \n\n“The Wright is the greatest of souls, The Wall of Light that protects humankind, the life after death. Those who follow their teachings will abandon their shells. {i}To follow{/i} means {i}to guard Wright’s tribe and help it grow in strength and peace{/i}. To achieve this goal, one needs to learn and to accept the creation and its nature. This allows us to shape matter, souls, and pneuma without turning them against us. To be {i}a monk{/i} means to find freedom in Wright’s Tablets, to abandon one’s ambitions. I serve Wright’s will, I let it build my salvation, I prepare the tribes for their end.”
            \n\nHe takes off the hood again. For the first time, you see true gentleness in his eyes. “May these words be carried with my blood. So be it.”
            '
            'I follow his prayer. “So be Wright’s will.”' if pc_religion == "ordersoftruth":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow his prayer. “So be Wright’s will.”')
                $ pc_faithpoints_opportunities += 1
                $ pc_faithpoints += 1
                $ monastery_friendship += 2
                jump aeli_about_theirfaith01churchoftruth
            'I follow his prayer. “So be it.”' if pc_religion == "theunitedchurch" or pc_religion == "unknown" or pc_religion == "fellowship":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow his prayer. “So be it.”')
                if pc_religion == "theunitedchurch" or pc_religion == "fellowship" or pc_religion == "ordersoftruth":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints += 1
                $ monastery_friendship += 1
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    'He smiles and adjusts his rope. “Yes... May they be written on my soul.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '(lie) I follow his prayer. “So be it.”' if not pc_religion == "theunitedchurch" and not pc_religion == "ordersoftruth" and not pc_religion == "fellowship":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I follow his prayer. “So be it.”')
                $ pc_lies += 1
                $ monastery_lies_decima += 1
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints -= 2
                $ monastery_friendship += 1
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    'He smiles and adjusts his rope. “Yes... May they be written on my soul.”
                    \n\nYou catch a glimpse of resentment on {color=#f6d6bd}Decima’s{/color} face, but she turns away from your gaze, shaking her black ponytail.
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '“I see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                if pc_religion == "theunitedchurch" or pc_religion == "fellowship" or pc_religion == "ordersoftruth":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints -= 1
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints += 1
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    'He rubs a large liver spot on his bare hand, piercing you with his gaze.
                    '
                    '(monastery1aboutmonastery preset)':
                        pass

    label aeli_about_theirfaith01churchoftruth:
        menu:
            'He grins. “A fellow Seeker! What sort of order has been guiding thee?”
            '
            '“Their scribes earn dragons by copying codices, but when they can, they study pneuma. They have quite a library of spells that remove curses and move objects from a distance.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Their scribes earn dragons by copying codices, but when they can, they study pneuma. They have quite a library of spells that remove curses and move objects from a distance.”')
                menu:
                    'He snorts. “Magic studies! Such pride it takes to think you can find hope in the power and will of humans. Just as their shells are going to forget the strength of limbs, the swings of swords, their pneuma will be nothing more than the last breath.”
                    \n\nHe peeks at {color=#f6d6bd}Decima{/color}, who responds to his words by kicking the ground, releasing a small cloud of dust from beneath her robe. He raises his eyebrow, then looks at you again, raising his chin.
                    \n\n“But how unlike codices. The stories and teachings will last. Ten copies may be stolen, hundreds may burn, but all it takes is one of them for its wisdom to outlast generations. At least ya, {i}thy{/i} monks try to write. That’s what the monasteries are {i}for{/i}.”
                    '
                    '“You may be right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right.”')
                        $ monastery_friendship += 1
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He rests his hand on his bag. “I may. And I am.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '(lie) “You may be right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “You may be right.”')
                        $ monastery_friendship += 1
                        $ pc_lies += 1
                        $ monastery_lies_decima += 1
                        $ pc_faithpoints -= 1
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He rests his hand on his bag. “I may. And I am.”
                            \n\nYou catch a glimpse of resentment on {color=#f6d6bd}Decima’s{/color} face, but she turns away from your gaze, shaking her black ponytail.
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '“They know what they’re doing.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They know what they’re doing.”')
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            '“If thou say so,” he says with a smirk.
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
            '“They look for ways to make bronze without tin and work on devices that replace human muscles.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They look for ways to make bronze without tin and work on devices that replace human muscles.”')
                menu:
                    'He frowns. “Without tin, thou sayest? Is that what the cityfolk really need? More blades and helmets?”
                    '
                    '“Yeah, I know. I don’t like it either.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah, I know. I don’t like it either.”')
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He looks at his bandaged hand. “I guess it can’t be avoided. Even the deaths of the war weren’t enough to make cityfolk seek strength in another place.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '“It’s not my place to question their intentions.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s not my place to question their intentions.”')
                        $ monastery_friendship += 1
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He looks at {color=#f6d6bd}Decima{/color}, who looks at you with a wide grin. “Good, very well. Prelates do need followers.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '“They think it’s a good call. I trust their wits.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They think it’s a good call. I trust their wits.”')
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He gives you a long look. “Fair. If ye were in our position, ye, {i}thou{/i} wouldst think about it a lot. When to trust, when to think. Not easy.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
            '“They are a small bunch who live close to nature, looking for a new village every two decades or so. They help the tribes plant and alter their forest gardens.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They are a small bunch who live close to nature, looking for a new village every two decades or so. They help the tribes plant and alter their forest gardens.”')
                menu:
                    'He frowns. “Traveling monks? I thought it was stuff of the past. The Orders of Truth have many enemies, some of which wear the clothes of the Unites.” He rubs the fingers of his bare hand with his thumb. “When a village falls, people fall. When an order falls, centuries fall.”
                    \n\n“Brave,” he concludes, “but stupid.”
                    '
                    '“You’ve no right to judge them.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve no right to judge them.”')
                        $ monastery_friendship += 1
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He smiles and gestures for you to calm down. “Don’t tell me what to say if yer not ready to cut off my fingers.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '“Well, maybe they’ll survive. And change the lives of dozens of people.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, maybe they’ll survive. And change the lives of dozens of people.”')
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He adjusts his robe. “Change always comes. What thou wantest is the {i}right kind{/i} of change.”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
                    '“Yeah, I guess so.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah, I guess so.”')
                        $ monastery_friendship -= 1
                        $ pc_faithpoints -= 1
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            'He makes an ugly grimace, but says nothing.
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
            '“They want to answer the large questions that used to torment sages. There’s only a few of them, but they handle all sort of ceremonies, and pray for everyone.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They try to find the answers for the large questions that have troubled the sages for centuries. There’s only a few of them, but they handle all sort of ceremonies, and pray for everyone.”')
                menu:
                    '“Ah, one of those,” he rubs his bandaged hand. His voice is cold. “I see.”
                    '
                    '“What is it?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What is it?”')
                        menu:
                            'He speaks slowly. “All humans think, all humans pray. But there’s pride in doing it while there are sick and hungry shells around you. One’s hands are Wright’s tools, no less than one’s soul.”
                            '
                            '“You’ve no right to judge them.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve no right to judge them.”')
                                $ monastery_friendship += 1
                                $ questionpreset = "monastery1aboutmonastery"
                                menu:
                                    'He smiles and gestures for you to calm down. “Don’t tell me what to say if yer not ready to cut off my fingers.”
                                    '
                                    '(monastery1aboutmonastery preset)':
                                        pass
                            '“Yeah, I guess so.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah, I guess so.”')
                                $ monastery_friendship -= 1
                                $ pc_faithpoints -= 1
                                $ questionpreset = "monastery1aboutmonastery"
                                menu:
                                    'He makes an ugly grimace, but says nothing.
                                    '
                                    '(monastery1aboutmonastery preset)':
                                        pass
                    'I don’t say anything.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t say anything.')
                        $ questionpreset = "monastery1aboutmonastery"
                        menu:
                            '“And that’s that,” he concludes. “Aught else?”
                            '
                            '(monastery1aboutmonastery preset)':
                                pass
            '“It’s a new congregation, you don’t know it. They live among other folk and save their earnings to raise a new monastery.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a new congregation, you don’t know it. They live among other folk and save their earnings to raise a new monastery.”')
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    'He nods. “May they find the right place. The war has been cruel on builders and hewers, and with the roads as they are, I wish no travels to anyone.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass

    label aeli_about_aeli01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How does one become a monk?”')
        $ aeli_about_aeli = 1
        $ aeli_about_monastery += 1
        menu:
            'He lets out an amused grunt and clasps his hands together. “When one needs to join an order, they find a way. It’s not aught thou wantest, but a stuff that happens to thee.”
            '
            '“Give me an example.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Give me an example.”')
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    '“Oh, I don’t know. Abandonest thy past. Throw thy pet down the cliff and pray.”
                    \n\nYou don’t find even a hint of playfulness in his voice. After a longer pause, he carries on.
                    '
                    '(monastery1aboutmonastery preset)':
                        pass

    label aeli_about_hiddenknowledge:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn some of your knowledge about the peninsula.”')
        $ aeli_about_hiddenknowledge = 1
        $ aeli_about_monastery += 1
        menu:
            '“No,” he sighs. “The order protects what it knows, and we seek no wealth.”
            \n\nYou remind him of your trade and he responds with annoyance. “Knowledge builds and destroys the cities. We,” he points at two monks who are seeking snails among the garden patches, “are responsible for what we bring from our journey. A blacksmith isn’t judged by the deaths of their swords, but they oughtn’t sell them to scoundrels.”
            '
            '“I just try to keep myself safe.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just try to keep myself safe.”')
                $ questionpreset = "monastery1aboutmonastery"
                $ monastery_friendship -= 1
                menu:
                    'He stands with his legs apart, with one reaching forward. “In that case, I don’t think ye’ve chosen the right job. {i}Thou hast{/i}, I mean.” He gestures with frustration.
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '“I use what I learn to protect other people.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I use what I learn to protect other people.”')
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    '“And thou thinkest our books and studies are going to help thee? Just keep thy shell healthy, take care of thy pet, listen to elders.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '“Were you never tempted to do something great with your knowledge?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you never tempted to do something great with your knowledge?”')
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    'His smirk is a bit gentler. “Sowing seeds and harvesting crops is great. Fixing an old roof is great. Raising a child is great. Feeding the weak, clothing the poor... Thou hast the eyes of an adventurer, so thou dost not see it. Long gone are the times of fathers and mothers of tribes, of heroes from Wright’s Tablets, of giants from pagan tales. We’re all but pebbles on the face of a mountain.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '“If you believe that there’s freedom and peace in understanding the world, it seems strange that you wouldn’t share what you know with other people.”' if pc_class == "scholar" or aeli_about_thisplace or aeli_about_theirfaith:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you believe that there’s freedom and peace in understanding the world, it seems strange that you wouldn’t share what you know with other people.”')
                $ questionpreset = "monastery1aboutmonastery"
                $ monastery_friendship += 2
                menu:
                    'He scowls at his young companion, who grins back at him like someone who has just won an argument. He wipes his bare hand on his robe. “Well, maybe, who knows. But it takes more to find peace than just knowing stuff. Wisdom needs order of thoughts, a healthy and humble soul. One can lead to the other, but doesn’t have to. It’s crucial for everyone’s safety that we value our trust.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass
            '“So does the order keep everything it learns to itself?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So does the order keep everything it learns to itself?”')
                $ questionpreset = "monastery1aboutmonastery"
                menu:
                    '“There are some souls we trust. The elders of {color=#f6d6bd}Old Págos{/color}. The Seekers from other monasteries. Such people of faith keep the good of the many above their greed. But even they don’t {i}need{/i} to know all.”
                    \n\nHe glances at your axe and smirks. “And sometimes we {i}may{/i} make an exception for a trustworthy outsider.”
                    '
                    '(monastery1aboutmonastery preset)':
                        pass

label aeli_about_sleeping1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why can’t I spend a night here?”')
    $ aeli_about_sleeping1 = 1
    $ questionpreset = "monastery1"
    menu:
        '“Want us to give thee a chest and a weapon rack, too? Or maybe feed thy mouflons in our gardens, or ask us to bed with thou? It’s not an inn. We respect the hardships of one’s journey, so we don’t scare off the strangers who cross the mountains. But we don’t let them wander about and take our time for granted.”
        \n\nHe looks at his bandaged hand, makes a fist, then opens it and stretches out his fingers. “Maybe with {color=#f6d6bd}Old Págos{/color} locked, our old rules too shall change.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_sleeping2:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The plague is gone. Can I spend a night here?”')
    $ monastery_sleep_unlocked = 1
    $ renpy.notify("New shelter unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'He scowls first at you, then at {color=#f6d6bd}Decima{/color}, who observes the sky carelessly. After a few silent heartbeats, he lets out a grunt. “Maybe in the storehouse. But don’t think that I’m going to look after thy horse, or cook for thee. All thee canst get is a roof for thy head.”
        '
        '“It’s already plenty. I appreciate it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s already plenty. I appreciate it.”')
            $ questionpreset = "monastery1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                '“Just don’t tell the others.”
                '
                '(monastery1 preset)':
                    pass
        '“Fine.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.”')
            jump monasteryafterinteractions01

label aeli_about_plague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there nothing you can do about the plague that has beset {color=#f6d6bd}Old Págos{/color}?”')
    $ aeli_about_plague1 = 1
    $ quest_healingtheplague_description_pre = "{color=#f6d6bd}Aeli{/color} believes that the plague can only be healed by time, or by “a mage more powerful than anyone in the order.”"
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        '“Well.” His cough doesn’t help his hoarse throat. “We don’t understand what makes it grow. We put to use all the ingredients we found, brewed as many potions and balms as we could, and they worked - for one afternoon. Then, people once again fell ill. Who can tell where the sickness dwells? A powerful healer could get rid of it once and for all with a single spell, but no follower of The Wright in the North carries such talents.”
        '
        '“Maybe it’s time for someone to enter the village and look for the source.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe it’s time for someone to enter the village and look for this {i}source{/i}.”')
            $ questionpreset = "monastery1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                '“Thou thinkest?” he smirks. “The well isn’t poisoned, the sea brings fresh air, the crops have their regular color, the ibexes drop healthy feces. The tribe isn’t dumb. No reason to lock you inside.”
                '
                '(monastery1 preset)':
                    pass
        '“I’ll seek a great healer, then.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll seek a great healer, then.”')
            $ questionpreset = "monastery1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'He rubs his hands together, pressing a thumb against his palm and looking at the sky. “Such as? The druids? The necromancers? The golem maker? Dangerous souls with no reason to help us.”
                '
                '(monastery1 preset)':
                    pass
        '“Could it be Wright’s punishment?”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could it be Wright’s punishment?”')
            $ questionpreset = "monastery1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                '{color=#f6d6bd}Decima{/color} observes you with narrowed eyes, then exchanges looks with {color=#f6d6bd}Aeli{/color} and moves her eyes toward your palfrey, fixing the strand of hair on her ear.
                \n\n“All is possible,” the taller monk is far from convinced. “We asked them, of course. But they’re just humans, with lives no worse than many others. Would The Wright crush their village when there are pagans and necromancers just nearby?”
                '
                '(monastery1 preset)':
                    pass
        'I smirk. “Could it be Wright’s punishment?”' if not pc_religion == "theunitedchurch" and not pc_religion == "ordersoftruth" and not pc_religion == "fellowship":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Could it be Wright’s punishment?”')
            $ questionpreset = "monastery1"
            $ monastery_friendship -= 2
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                '{color=#f6d6bd}Decima{/color} scratches the ground with her boot and turns toward you, leaning forward, ready to jump. {color=#f6d6bd}Aeli{/color} gestures for her to stop, then warns you with a few clicks of his tongue.
                '
                '(monastery1 preset)':
                    pass
        '“Let me know if there’s something I can do.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me know if there’s something I can do.”')
            $ questionpreset = "monastery1"
            $ monastery_friendship += 1
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'He nods. “I’ll pass ya, {i}thy{/i} offer to {color=#f6d6bd}the prelate{/color}. Thank thee.”
                '
                '(monastery1 preset)':
                    pass

label aeli_about_bronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color}, the enchantress, wants to place these rods in high points across the peninsula. Can you help me out?”')
    $ aeli_about_bronzerod = 1
    $ renpy.notify("Journal updated: Bronze Rods")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        '“Ye’ve brought her magic here?” He steps back, while {color=#f6d6bd}Decima{/color} turns toward you and reaches behind her back with one hand. {color=#f6d6bd}Aeli’s{/color} voice is close to a shout. “Take it away before ye put all of us in danger!”
        '
        '“Calm down, it’s just a piece of bronze.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Calm down, it’s just a piece of bronze.”')
            $ monastery_friendship -= 1
            $ description_eudocia03 = "{color=#f6d6bd}The monks{/color} distrust her and are convinced she may try to harm their order."
            $ questionpreset = "monastery1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'His pale face starts turning red, the echo adds a thunder to his words. “Yer not asked for ya thoughts! Ye think yaself a judge, after ye put ya trust in that witch?” He points at you with a bandaged finger. “She’s a beast in clothes. Its claws will tear away thy head.”
                '
                '(monastery1 preset)':
                    pass
        '“Fine, let me hide it in my bags again.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, let me hide it in my bags again.”')
            $ description_eudocia03 = "{color=#f6d6bd}The monks{/color} seem to distrust her."
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "monastery1"
            menu:
                'Even after you return, he scowls at you, crossing his arms.
                '
                '(monastery1 preset)':
                    pass

label aeli_about_asterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What can you tell me about {color=#f6d6bd}Asterion{/color}?”')
    $ aeli_about_asterion = 1
    $ description_asterion09 = "According to monk {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Asterion’s{/color} thigh was severely hurt by a hundred-legged worm."
    $ quest_asterion_description09 = "According to monk {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Asterion{/color} was tasked with finding iron and steel for the monastery. It’s possible that he purchased some in either {color=#f6d6bd}Gale Rocks{/color} or {color=#f6d6bd}Creeks{/color}."
    $ elah_about_asterion_friendship += 1
    $ renpy.notify("Journal updated: Find the Roadwarden")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        '“Let me think.” He looks at the sky and clenches his fist around the strap of his bag. “The first time he was here, we asked him to find us some iron in {color=#f6d6bd}Gale Rocks{/color}. The second time, he {i}did{/i} bring us a few scraps, but was wounded. A piece of flesh bitten away from his thigh. Said that a hundred-legged worm had caught him off guard in a meadow. Instead of his pay, we offered him a potion.”
        '
        '“Tell me about {color=#f6d6bd}Gale Rocks{/color}.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Gale Rocks{/color}.”')
            $ description_galerocks01 = "A large fishing village near the northern shore."
            $ description_galerocks06 = "According to {color=#f6d6bd}Aeli{/color}: “They are weak and angry, like a wolf beaten and kicked from a pup. Loud, ready to bite, but all it takes is for someone to raise their hand, then it jumps away, in whimpers.”"
            $ description_galerocks07 = "I heard that they trade more than any other village in the North, paying well for crops, wood, and meat."
            menu:
                'He hesitates, but finally nods. “Just some seaweed eaters. Their soil is barren, but the strongest of them spend their days on the boats, among the sharp rocks. Those who can’t hunt for fish, boil water to make salt. They trade with other villages, more than anyone in the peninsula. For crops, wood, and meat.” He snorts. “But they’re weak folk, weak and angry, like a wolf beaten and kicked from a pup. Loud, ready to bite, but all it takes is for someone to raise their hand, then it jumps away, in whimpers.”
                \n\nHe lets go of his bag. “At least they follow Wright’s teachings.”
                '
                '“Anything note-worthy about the iron he delivered?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything note-worthy about the iron he delivered?”')
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        '“Scavenged from furniture. A few of them were rusty. Who knows where he bought them. We melted them for nails.”
                        '
                        '(monastery1 preset)':
                            pass
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    jump monasteryafterinteractions01
        '“Anything note-worthy about the iron he delivered?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything note-worthy about the iron he delivered?”')
            menu:
                '“Scavenged from furniture. A few of them were rusty. Who knows where he bought them. We melted them for nails.”
                '
                '“Tell me about {color=#f6d6bd}Gale Rocks{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Gale Rocks{/color}.”')
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    $ description_galerocks01 = "A large fishing village near the northern shore."
                    $ description_galerocks06 = "According to {color=#f6d6bd}Aeli{/color}: “They are weak and angry, like a wolf beaten and kicked from a pup. Loud, ready to bite, but all it takes is for someone to raise their hand, then it jumps away, in whimpers.”"
                    $ description_galerocks07 = "I heard that they trade more than any other village in the North, paying well for crops, wood, and meat."
                    menu:
                        'He hesitates, but finally nods. “Just some seaweed eaters. Their soil is barren, but the strongest of them spend their days on the boats, among the sharp rocks. Those who can’t hunt for fish, boil water to make salt. They trade with other villages, more than anyone in the peninsula. For crops, wood, and meat.” He snorts. “But they’re weak folk, weak and angry, like a wolf beaten and kicked from a pup. Loud, ready to bite, but all it takes is for someone to raise their hand, then it jumps away, in whimpers.”
                        \n\nHe lets go of his bag. “At least they follow Wright’s teachings.”
                        '
                        '(monastery1 preset)':
                            pass
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    jump monasteryafterinteractions01
        '“I see.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
            jump monasteryafterinteractions01

label aeli_about_barterALL:
    label aeli_about_barter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would you like to barter?”')
        $ aeli_about_buyingorselling = 1
        $ quest_healingpotion_description00d = "It looks like I won’t be able to get the potion from the monks."
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“Not today, not before the spring. Our order uses every bottle we make to help the sick from {color=#f6d6bd}Old Págos{/color}, as well as to protect ourselves.”
            '
            '“I could bring you dragon bones, or something that doesn’t grow in the mountains.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could bring you dragon bones, or something that doesn’t grow in the mountains.”')
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ description_monastery03 = "The monks may welcome some “delicacies.”"
                menu:
                    'He looks at the steel hourglass hanging from the wall. “Taste, softness, tools of murder. We shall {i}crave{/i} naught. One thing we lack are delicacies we could offer to the sick and weak, but thou wilt not find such a thing in this sad land.”
                    '
                    '(monastery1 preset)':
                        pass

    label aeli_about_barter01_alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was asked to look for a healing potion for this trader, {color=#f6d6bd}Akakios{/color}...”')
        $ aeli_about_buyingorselling_alt = 1
        $ quest_healingpotion_description00d_alt = "{color=#f6d6bd}Aeli{/color} told me to ask {color=#f6d6bd}Foggy{/color} about the dolmen."
        if quest_healingpotion == 1:
            $ renpy.notify("Journal updated: Merchant’s Medicament")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament{/i}')
        $ description_foggy07 = "According to {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Foggy{/color} cares about the northern paths."
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'A brief mention of the dolmen is enough to spark an understanding gleam in the monk’s eyes. “I know of this place, even spent the night there once or twice. But if thou truly thinkest it hides stuff from our eyes, head to someone who... {i}cares{/i} about these paths. Try {color=#f6d6bd}Foggy{/color},” he turns his head around, scratching his ear, “the tavernkeep of the northern crossroads. She might have heard something.”
            '
            '(monastery1 preset)':
                pass

    label aeli_about_barter02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You mentioned you lack {i}delicacies{/i}... How about this roast chicken?”')
        $ aeli_about_buyingorselling_chicken_firsttime = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "monastery1"
        menu:
            'He chuckles. “{i}I{/i} lack no such thing, but we look after a few weak souls.” After sniffing the spiced meat, he gives you an approving nod. “We’ve got a few bones we can spare. I’ll pay you, {i}thee{/i} two coins for such a meal.”
            '
            '(monastery1 preset)':
                pass

    label aeli_about_barter03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take this chicken. For two dragons.”')
        if not aeli_about_buyingorselling_chicken_day:
            $ monastery_friendship += 1
            $ custom1 = ""
        else:
            $ aeli_about_buyingorselling_chicken_friendship_counter += 1
            $ custom1 = ""
        if aeli_about_buyingorselling_chicken_friendship_counter >= 2:
            $ monastery_friendship += 1
            $ aeli_about_buyingorselling_chicken_friendship_counter -= 2
        $ aeli_about_buyingorselling_chicken_day = day
        $ coins += 2
        $ item_chicken -= 1
        show screen notifyimage( "You sold the roast chicken. +2", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the roast chicken. +2 {image=cointest}{/i}')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "monastery1"
        menu:
            'He gestures for {color=#f6d6bd}Decima{/color} to take it to one of the caves, then pulls out the coins from his bag. “I could take another one from thee. Maybe in three, four days.”
            '
            '(monastery1 preset)':
                pass

    label aeli_about_sharpeningpotion:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “With the plague gone... Would you brew something that could help me in my journey?”')
        $ aeli_about_sharpeningpotion = 1
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ item_snakebait_truth = 1
        $ aeli_about_snakebait = 1
        menu:
            '“We need to restore our supplies first,” he glances at the nearby garden. Most of its fruits and leaves are already plucked. “But there’s something I can offer thee. Bring me a cave ear, a mushroom that grows in humid chambers underground, and snake bait - an orange flower from the deep woods, though some smoke it for pleasure. On their own, they’re poisonous. Together, even more so,” he snorts, “but I can turn into a dust that {i}sharpens{/i} one’s senses. Good for combat,” he cracks his knuckles. “In one night, I could prepare three doses or so, but use them with care. Once the pneuma loosens, they’ll weaken your shell.”
            '
            '(monastery1 preset)':
                pass

    label aeli_about_sharpeningpotion_timer:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. The mushroom, and the snake bait.”')
        $ aeli_about_sharpeningpotion_timer = day
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ item_snakebait -= 1
        $ item_cavemushroom -= 1
        $ renpy.notify("You lost the snake bait\nand the cave ear.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the snake bait\nand the cave ear.{/i}')
        $ questionpreset = "monastery1"
        menu:
            'He reaches for them, then blinks and steps away. After a few moments, he brings an empty bucket and tells you to put the ingredients inside. “Fine. The sharpening poison will be ready after sunrise.”
            '
            '(monastery1 preset)':
                pass

    label aeli_about_sharpeningpotion_collected:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m here to pick up the poison.”')
        $ aeli_about_sharpeningpotion_collected = 1
        $ item_sharpeningpotion += 3
        $ renpy.notify("You received three doses of sharpening poison.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received three doses of sharpening poison.{/i}')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "monastery1"
        menu:
            'He nods toward {color=#f6d6bd}Decima{/color} and she steps closer, handing you a small case. “Enjoy,” she lets out a cruel whisper, while {color=#f6d6bd}Aeli{/color} chuckles. “Remember, eat a good spoonful of it at once, rub some into thy gums, but only once a day. The effect will last for a good few hours, but will give thee one sorry mug next time you go to sleep.”
            '
            '(monastery1 preset)':
                pass

label aeli_about_snakebait01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found some snake bait... Is it safe for humans?”')
    $ item_snakebait_truth = 1
    $ aeli_about_snakebait = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "monastery1"
    menu:
        '“It’s very much not,” he gestures for you to keep it away. “Some use it for enjoyment, but not for long. There are a few potions I know of that use it, but it’s poisonous, even after an alchemist clears it.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_brewingscholar01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I also dabble in alchemy a bit. Can I use your tools to brew?”')
    $ aeli_about_alchemytable = 1
    $ questionpreset = "monastery1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ description_foggy03 = "She has her own set of alchemical tools, necessary to brew ciders and distill hard drinks."
    menu:
        '“Curious.” He puts a bandaged finger on his chin. “Back in the day, the order would lend thee its workshop in exchange for thy recipes, but now...” He rubs his skin, observing {color=#f6d6bd}Decima{/color}. She shakes her head gently. “That was before the war. If aught breaks under thy touch, we would struggle to replace it. No amount of coins may buy us a trader with glass phials and bronze or golden tools. Rather, thou must follow the road north. Around the lake, until you reach {color=#f6d6bd}Foggy Lake{/color}, a tavern. {color=#f6d6bd}Foggy{/color} makes hard drinks and ciders, and shall have the simpler tools. There also was that one old druidess in {color=#f6d6bd}Howler’s{/color}, but she’s likely already dead.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_powderedbasalt01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Still, I know a recipe for the blinding powder that requires a basalt rock crushed on the top of a mountain. Can I get to those trees high up, just for a few minutes?”')
    if not quest_monasterysupport_description01 and not quest_monasterysupport_description01lie:
        $ aeli_about_powderedbasalt_gray = 1
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'There’s a new gleam in his eye. “I’d adore learning this {i}recipe{/i}, for we use basalt knives often, but {color=#f6d6bd}our prelate{/color} won’t agree for thy {i}stroll{/i}.” He looks toward the tiny orchard. The pride makes his voice stronger. “We’d need to be sure you, {i}thou{/i} art a friend of the order, not a threat.”
            \n\nA gentle cough. “We can’t let you run into the caves, thou seest.”
            '
            '(monastery1 preset)':
                pass
    else:
        label aeli_about_powderedbasalt02:
            $ questionpreset = 0
            $ aeli_about_powderedbasalt = 1
            if not aeli_about_powderedbasalt_gray:
                $ custom1 = "There’s a new gleam in his eye. “I’d adore learning this {i}recipe{/i}, for we use basalt knives often, and since you’re a friend of our order, I’m sure {color=#f6d6bd}the prelate{/color} will agree to thy wish, and will spare you one of our rocks.” He looks toward the tiny orchard. The pride makes his voice stronger. “I’ll assist you.”"
            else:
                $ custom1 = "His gentle bow carries a mockery. “I’ll assist you.”"
            $ quarters += 1
            menu:
                '[custom1]
                \n\nThe climb is harsh. Your steps are careful, and the narrow trail makes you put your hand on the smooth wall. You can’t resist looking back, making sure {color=#f6d6bd}Decima{/color} is still there, despite her noiseless walk. Her smile gets even more cruel once she notices your heavy breath.
                \n\n{color=#f6d6bd}Aeli{/color} gestures for you to climb up the rope ladder first. It’s attached so firmly it needs no holding.
                '
                'I seek a flat surface and something I can use to powder the rock.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I seek a flat surface and something I can use to powder the rock.')
                    $ quarters += 2
                    $ item_rocktobepowdered = 0
                    $ item_powderedrock = 1
                    $ renpy.notify("You added the powdered rock to your bag of ingredients.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the powdered rock to your bag of ingredients.{/i}')
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    $ quarters += 1
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    menu:
                        'The monotonous task of breaking the basalt into smaller chunks, then grinding them into dust, is relieved by {color=#f6d6bd}Aeli’s{/color} questions. You recite the recipe from memory, giving him time to write it down. Having no wall in the north, the wind here is getting only colder.
                        \n\nOnce you fill up a small sack with the black powder, your hands are tired, and a bit scratched. Finally, you’re ready to climb back down.
                        '
                        '(monastery1 preset)':
                            pass

    label aeli_about_powderedbasalt01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still need to powder a basalt rock. Can you lend me one?”')
        jump aeli_about_powderedbasalt02


label aeli_about_readtheletter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was asked to learn what’s on this tablet...”')
    $ item_letterwhitemarshes_read = 1
    if aeli_about_plague2:
        $ custom1 = "He wipes it with his robe."
    else:
        $ custom1 = "He tells you to wash it in a nearby bucket and put it on the ground. As you step away, he moves closer and picks it up, then wipes it with his robe."
    if aeli_about_plague2:
        $ custom2 = "returns your possession"
    else:
        $ custom2 = "washes your possession again and puts it on the ground, keeping his distance"
    $ minutes += 5
    $ questionpreset = "monastery1"
    menu:
        '[custom1] He glances at the carving of the troll, then keeps the letters close to his face. “Decent signs, consistent. Good depth, too. Nice stylus.” He observes the contents patiently, then [custom2]. “It’s just a short farewell. {color=#f6d6bd}Valens’{/color} husband says he couldn’t spend more time in {i}this nightmarish village{/i}, and that he met another soul during his hunting trip. {i}We will start a new family, goodbye{/i}. That’s about it. Not even a signature.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_asteriontablet01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this wax tablet... Could you read it to me?”')
    $ aeli_about_asteriontablet = 1
    $ item_asteriontablet_read = 1
    $ asterion_highisland_clues += 1
    if aeli_about_plague2:
        $ custom1 = "He wipes it with his robe."
    else:
        $ custom1 = "He tells you to wash it in a nearby bucket and put it on the ground. As you step away, he moves closer and picks it up, then wipes it with his robe."
    if aeli_about_plague2:
        $ custom2 = "returns your possession"
    else:
        $ custom2 = "washes your possession again and puts it on the ground, keeping his distance"
    $ minutes += 5
    $ questionpreset = "monastery1"
    menu:
        '[custom1] He has to keep the letters close to his face. “Sloppy signs, shapes are not consistent. Lacks experience. The stylus was too large.” He observes the contents patiently, then [custom2]. “These are notes on oars, boats, and a volcano, but such babbling would take the original scribe to read them. Someone who understands the code. There’s one name here, {color=#f6d6bd}Navica{/color}. It suits a fisher, or a sailor.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_thaisletter00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider asking him to read {color=#f6d6bd}Thais’{/color} letter to me.')
    menu:
        'You frown. The city officials may not be happy about receiving a broken seal.
        '
        '“Could you read this for me?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you read this for me?”')
            jump aeli_about_thaisletter01alt
        'I’ll keep this letter closed until I reach the city.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep this letter closed until I reach the city.')
            $ custom1 = "{color=#f6d6bd}The monk{/color} gives you a curious look."
            $ item_thaisletter_readingblocked = 1
            jump monasteryafterinteractions01alt
        'I need to think about it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to think about it.')
            $ custom1 = "{color=#f6d6bd}The monk{/color} gives you a curious look."
            jump monasteryafterinteractions01alt

label aeli_about_thaisletter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab {color=#f6d6bd}Thais’{/color} letter. “Could you read this scroll to me?”')
    label aeli_about_thaisletter01alt:
        if not item_thaisletter_opened:
            menu:
                'He gives it a hungry look and rubs his hands together. “I mean, it’s sealed.”
                '
                'I open it with my knife. “Don’t worry about it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open it with my knife. “Don’t worry about it.”')
                    $ item_thaisletter_opened = 1
                    $ item_thaisletter = 0
                    if aeli_about_plague2:
                        $ custom1 = "He unrolls the scroll gently."
                    else:
                        $ custom1 = "He puts on a pair of leather from his bag and tells you to put the scroll on the ground, then picks it up and unrolls it gently. "
                    if aeli_about_plague2:
                        $ custom2 = "returns the scroll to you"
                    else:
                        $ custom2 = "puts the scroll on the ground again, steps away, and takes off his gloves"
                    label aeli_about_thaisletter01a:
                        $ item_thaisletter_read = 1
                        $ aeli_about_thaisletter = 1
                        $ banditshideout_galerocks_tiestobandits = 1
                        $ minutes += 5
                        $ questionpreset = "monastery1"
                        menu:
                            '[custom1] He has to keep the parchment close to his face, overcoming his weak eyes. “An unusual shape of letters, but they’re understandable. Same with initials and pictures. But the lines are even. A bit shabby quill. Good ink.” He observes the contents patiently, then starts to read out loud, though his hoarse voice forces him to make a few pauses.
                            \n\nThe letter is long and filled with boring, “official” salutations. One of the parts directly contradicts what {color=#f6d6bd}Thais{/color} has told you, and even the monk narrows his eyes, repeating the entire section: “The beliefs of our fathers are sacred to us, but depending on the proof of your good will, we will permit your missionaries to stay within our walls. I promise they will be treated with the dignity they deserve.”
                            \n\nOne more part also grabs your attention: “This piece of information is sensitive, but I trust that you will put it to good use. {color=#f6d6bd}Gale Rocks{/color}, a village set near the northern shore, participates in trade with the local bandits, led by their own {color=#f6d6bd}Glaucia{/color}. Their alliance grows in strength, and therefore brings many threats to our potential collaboration.”
                            \n\nOnce he finishes, {color=#f6d6bd}Aeli{/color} [custom2]. “So this is how the stuff are in {color=#f6d6bd}Howler’s{/color}. Interesting, warden.” He adjusts his hood and spares {color=#f6d6bd}Decima{/color} a grateful nod, reaching for the cup of water she offers him. “I don’t look forward to seeing the priests of The United Church, nor their soldiers.”
                            '
                            '(monastery1 preset)':
                                pass
                '“Maybe you’re right, I shouldn’t open it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you’re right, I shouldn’t open it.”')
                    jump monasteryafterinteractions01
        else:
            if aeli_about_plague2:
                $ custom1 = "He unrolls it gently."
            else:
                $ custom1 = "He puts on a pair of leather from his bag and tells you to put the scroll on the ground, then picks it up and unrolls it gently. "
            if aeli_about_plague2:
                $ custom2 = "returns the scroll to you"
            else:
                $ custom2 = "puts the scroll on the ground again, steps away, and takes off his gloves"
            jump aeli_about_thaisletter01a

label aeli_about_quest_orentius_thais_description01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a delicate matter to discuss. It’s about {color=#f6d6bd}Orentius{/color}.”')
    $ questionpreset = "monastery1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ minutes += 5
    if not aeli_about_necromancers_bloodmagic or (monastery_friendship+appearance_charisma) < 6:
        $ quest_orentius_thais_description03a03 = "{color=#f6d6bd}The monks{/color} have refused to share their thoughts on the matter."
        menu:
            '{color=#f6d6bd}Aeli{/color} turns around, gets closer to the rock face, and observes the hourglass, listening to your case.
            \n\n“I already know {color=#f6d6bd}our prelate’s{/color} response,” his tone could be explaining that every autumn is followed by winter. “Thou mayest think there’s a difference between the tribe of druids and the tribe of necromancers, but they’re both lost to their desires. With enough time, they’ll find themselves dwindling. There’s no reason for us to interfere.”
            '
            '(monastery1 preset)':
                pass
    else:
        $ quest_orentius_thais_description03a03 = "While {color=#f6d6bd}the monks{/color} have officially refused to share their thoughts on the matter, {color=#f6d6bd}Aeli{/color} offered me a gift to help me in my pursuit."
        $ item_generichealingpotion += 1
        $ renpy.notify("You received a fresh healing potion.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a fresh healing potion.{/i}')
        if aeli_about_necromancers_bloodmagic:
            $ custom1 = "blood sorcery"
        else:
            $ custom1 = "the necromancer"
        menu:
            '{color=#f6d6bd}Aeli{/color} turns around, gets closer to the rock face, and observes the hourglass, listening to your case.
            \n\n“I already know {color=#f6d6bd}our prelate’s{/color} response,” his tone could be explaining that every autumn is followed by winter. “Thou mayest think there’s a difference between the tribe of druids and the tribe of necromancers, but they’re both lost to their desires. With enough time, they’ll find themselves dwindling. There’s no reason for us to interfere.”
            \n\nHe then looks around and steps closer. “But {i}I{/i} don’t take thy tale of [custom1] lightly. A bottle,” he addresses {color=#f6d6bd}Decima{/color} and while she’s reluctant, she gives you a vessel of noticeable size. “If thou facest difficulties, this will save thee.”
            '
            '(monastery1 preset)':
                pass

label aeli_about_phoibe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask him about {color=#f6d6bd}Phoibe{/color} and the spirit rock.')
    $ questionpreset = "monastery1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ aeli_about_spiritrock += 1
    $ minutes += 10
    menu:
        '“Nah, {i}I{/i} wouldn’t bite into aught touched by that witch,” he hides his bandaged hand behind his back. “Why does the father think it may work?” You portray the situation as accurately as you can. {color=#f6d6bd}Aeli{/color} gets closer to the cliff, observing the river beneath it, and spending a good few minutes considering the situation. Suddenly, he turns toward you with wide-open eyes, making {color=#f6d6bd}his companion{/color} stagger.
        \n\n“He’s lying to thee,” he announces with a great dose of enthusiasm. “He seeks no cure for the lack of pneuma, but rather for the lack of {i}soul{/i} itself. Before Adir’s calling to greatness, the tribes of The Dragonwoods saw the spelless children as empty shells, throwing them to beasts just as often as they did with the crippled and the short-witted. There’s this tale...” He glances at you. “Thou won’t remember it anyway. But the Tablets carry no doubt - tribes shan’t hurt those touched with this condition, as there’s no such stuff as {i}soulless{/i} children.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_shortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know anything interesting about the path leading through the heart of the woods?”')
    $ aeli_about_shortcut = 1
    $ description_quintus03 = "According to {color=#f6d6bd}Aeli{/color}: “He’s a brute and an idiot, can’t understand jokes, can’t stand {i}weaklings{/i}. If thou ever meet him, just smile and let him speak as much as he needs to shut up.”"
    $ questionpreset = "monastery1"
    menu:
        '“I used to, but like all places that belong to beasts, it shifts every year. The only reason why it still has trails at all is that creatures use {i}our{/i} roads as their own game trails. Only a dimwit would try to cross it now.” After you ask him if he knows any such person, he takes a deep breath. “Well, last I’ve heard {color=#f6d6bd}Quintus{/color}, the gatekeeper from {color=#f6d6bd}Old Págos{/color}, is missing, or dead. He’s a brute and an idiot, can’t understand jokes, can’t stand {i}weaklings{/i}. If ye, {i}thou{/i} ever meet him, just smile and let him speak as much as he needs to shut up.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I seek knowledge about {color=#f6d6bd}High Island{/color}.”')
    $ aeli_about_highisland = 1
    $ questionpreset = "monastery1"
    menu:
        '“Then it was wise of thee to visit our Order,” he chuckles, “but I’d rather save such {i}knowledge{/i} for the worthy. I’ve got no reason to just throw it away.”
        '
        '(monastery1 preset)':
            pass

label monasterymissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a few hunters from {color=#f6d6bd}Creeks{/color}. Were they here?”')
    $ aeli_about_missinghunters = 1
    $ questionpreset = "monastery1"
    menu:
        '“{i}Hunters from {color=#f6d6bd}Creeks{/color}{/i}?” He mimics your voice with a hint of mockery. “Not a soul from there has reached this temple in...” He rubs the back of his bandaged hand and looks at a monk who’s carrying buckets of water. “Well, a decade? They’ve got enough hunting grounds. The heart of the woods, the watchtower, the northern hills...”
        '
        '(monastery1 preset)':
            pass

label aeli_about_steephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the ruins in the south?”')
    $ aeli_about_steephouse = 1
    $ questionpreset = "monastery1"
    menu:
        '“Are there still but one ruins there?” He glances at {color=#f6d6bd}Decima{/color}, who moves her head left and right slowly, then clears his throat. “Well. I won’t lie by pretending I know little. I just {i}decide{/i} to let it remain among our many bitter secrets.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_bandits01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the local bandits.”')
    $ aeli_about_bandits = 1
    $ questionpreset = "monastery1"
    menu:
        '“Then ask in the villages,” he looks at the wooden entrance hall behind you. “No group is going to bother us, for they’ve got no understanding of our pneuma and potions.”
        '
        '(monastery1 preset)':
            pass

label aeli_about_necromancersALL:
    label aeli_about_necromancers01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the necromancers in the North?”')
        $ questionpreset = "monastery1aboutnecromancers"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'He rubs the liver spots on his forehead with his bandaged hand, looking with one eye at his short companion. “This and that.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard I can find them in the northwest.”')
        $ aeli_about_necromancers_question01 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        $ description_whitemarshes01 = "A village of foragers and peat gatherers set among the western bogs."
        $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
        $ description_orentius10 = "According to {color=#f6d6bd}Aeli{/color}, he’s the real leader of {color=#f6d6bd}White Marshes{/color}, and it’s possible that he kidnaps people from the woods. He’s responsible for raising the undead."
        menu:
            'He nods. “Head back to the crossroads, then north, then right, into the bogs. There, you’ll find {color=#f6d6bd}White Marshes{/color}. The tribe used to forage and gather peat, but now it follows {color=#f6d6bd}Orentius{/color}, their priest. Who knows, maybe he’s the reason why so many travelers have disappeared on the roads.”
            \n\n{color=#f6d6bd}Decima{/color} scratches the ground with her boot, humming a tune, but {color=#f6d6bd}Aeli{/color} tells her to shut up. He carries on with sudden anger.
            \n\n“The story is as old as the Wright’s Tablets. Tribes look at monsters and ask themselves, {i}how can we use them?{/i} Their pride pushes them into their own fall. They hurt the innocent, then vanish in flames, or awake as empty ones.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think of {color=#f6d6bd}White Marshes{/color}?”')
        $ aeli_about_necromancers_question01 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
        $ description_orentius10 = "According to {color=#f6d6bd}Aeli{/color}, he’s the real leader of {color=#f6d6bd}White Marshes{/color}, and it’s possible that he kidnaps people from the woods. He’s responsible for raising the undead."
        menu:
            '“I don’t think much at all. As the tribe follows {color=#f6d6bd}Orentius{/color}, their priest, they’re no longer our allies. Who knows, maybe he’s the reason why so many travelers have disappeared on the roads.”
            \n\n{color=#f6d6bd}Decima{/color} scratches the ground with her boot, humming a tune, but {color=#f6d6bd}Aeli{/color} tells her to shut up. He carries on with sudden anger.
            \n\n“The story is as old as the Wright’s Tablets. Tribes look at monsters and ask themselves, {i}how can we use them?{/i} Their pride pushes them into their own fall. They hurt the innocent, then vanish in flames, or awake as empty ones.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your stance on necromancy, in general?”')
        $ aeli_about_necromancers_question02 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        menu:
            'He pulls his fingers, gathering his thoughts. “{i}My{/i} stance? I don’t {i}need{/i} one. I {i}trust{/i} The Wright. The dead makers must be weeded out. Their power brings only fogs. One may think the spellcaster is in control of the shells, but once they lose their breath, the dead are freed, searching for blood. Humans will never control the dead.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How does one deal with the undead? Or the necromancers?”')
        $ aeli_about_necromancers_question03 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        menu:
            '“Well, well. Is it a single corpse, a squad, an army? Thou needest to learn how shrewd the enemy is. Can it sense thy presence? Can it use a bow, or spells? As long as thou are, {i}art{/i}, alone, it’s always better to run. The older empty ones, even more so those that weren’t awoken by the fogs, get cunning, human-like, but with cruelty thou hast never seen.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Orentius{/color}?”')
        $ aeli_about_necromancers_question04 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        $ description_orentius05 = "I heard that he never leaves his house."
        menu:
            '“He’s never been here. He’s locked in that hut, a prisoner of his own conscience, speaking to his tribe as to children. Could there be a darker joke? A necromancer who calls himself a prophet?” As he snorts, {color=#f6d6bd}Decima{/color} puts on a wide grin. “What next, an emperor bathing in blood? No follower of The Wright could survive such a fall.”
            '
            '(monastery1aboutnecromancers preset)':
                pass
    label aeli_about_necromancers_question05:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was {color=#f6d6bd}White Marshes{/color} like before the priest’s arrival?”')
        $ aeli_about_necromancers_question05 = 1
        $ aeli_about_necromancers += 1
        $ questionpreset = "monastery1aboutnecromancers"
        $ description_whitemarshes10 = "According to {color=#f6d6bd}Aeli{/color}, the village “has been struggling for years. With food, children, the beasts of the bogs, the traders. They were strangers to us, even in the old days, when they used to join {color=#f6d6bd}Old Págos{/color} in their pagan feasts. But then, the monks arrived, and that bridge went down with flames. When the missionaries reached the bogs during the years of war, there were already some wounds that could never be sealed, not even by a shared prayer.”"
        menu:
            '“Far from lovely,” his smirk softens as his eyes grow worried. “It’s been struggling for years. With food, children, the beasts of the bogs, the traders. They were strangers to us, even in the old days, when they used to join {color=#f6d6bd}Old Págos{/color} in their pagan feasts.” He looks at {color=#f6d6bd}Decima{/color}, who listens to his tale curiously. “But then, the monks arrived, and that bridge went down with flames. When the missionaries reached the bogs during the years of war, there were already some wounds that could never be sealed, not even by a shared prayer.”
            '
            '(monastery1aboutnecromancers preset)':
                pass

label aeli_about_bloodmagic01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw {color=#f6d6bd}Orentius’{/color} ritual. He strengthens his weak spells with blood magic.”')
    $ aeli_about_necromancers_bloodmagic = 1
    $ monastery_friendship += 1
    menu:
        'During your report, {color=#f6d6bd}Aeli{/color} avoids {color=#f6d6bd}Decima’s{/color} piercing gaze. “That would clarify some doubts. His tribe was always weak on pneuma, but from what thou sayeth, he’s not a sorcerer, but a madman,” he finally looks back at {color=#f6d6bd}his companion{/color}, his voice grows stronger, “and we’ll need to take it to {color=#f6d6bd}our prelate{/color}.”
        '
        '(monastery1aboutnecromancers preset OR monastery1 set)':
            pass

label aeli_about_nomoreundeadALL:
    label aeli_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”')
        $ aeli_about_nomoreundead = 1
        $ monastery_friendship += 1
        $ minutes += 5
        $ questionpreset = "monastery1"
        menu:
            '“Thou wert not lying, that’s {i}a lot{/i},” he rubs the liver spots on his face once you end your tale. “{i}I’d{/i} rather see that necromancer gone for good, myself,” he nods politely, “but I’ll put trust in ya, {i}thy{/i} judgment. I’ll let the others know.”
            \n\n{color=#f6d6bd}Decima{/color} stands still with closed eyes, as if she’s napping.
            '
            '(monastery1 set)':
                pass

    label aeli_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”')
        $ aeli_about_nomoreundead = 1
        $ monastery_friendship += 2
        $ minutes += 5
        $ questionpreset = "monastery1"
        menu:
            '“Thou wert not lying, that’s {i}a lot{/i},” once you end your tale, he rubs the liver spots on his face firmly. “Having the necromancer gone for good is the best we could have hoped for,” his smile makes you think of a gargoyle, “ya, {i}thy{/i} judgment was just. I’ll let the others know.”
            \n\n{color=#f6d6bd}Decima{/color} stands still with one closed eye, as if she’s struggling to stay awake.
            '
            '(monastery1 set)':
                pass

    label aeli_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”')
        $ aeli_about_nomoreundead = 1
        $ monastery_friendship += 1
        $ minutes += 5
        $ questionpreset = "monastery1"
        menu:
            '“We’ve seen the smoke,” he rubs the liver spots on his face firmly. “I’d normally be happy to hear of a dead necromancer, but it’s a small comfort when we now have a cursed army to struggle with. What happened, truly?”
            \n\n{color=#f6d6bd}Decima{/color} stares at you without blinking, with a worrisome smile. Whenever you try to omit some details, she lets out a quiet grunt. After a few minutes, {color=#f6d6bd}Aeli{/color} looks at the huge hourglass, pondering.
            '
            '(monastery1 set)':
                pass

label aeli_quest_pens_questionALL:
    label aeli_quest_pens_question:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need any help? I’m looking for a job.”')
        if (monastery_friendship+appearance_charisma) < 4:
            $ questionpreset = "monastery1"
            $ aeli_quest_pens_gray = 1
            menu:
                'He puts his hands together and repeatedly taps his fingers. After a few breaths, he straightens up. “No.”
                '
                '(monastery1 preset)':
                    pass
        else:
            $ aeli_quest_pens = 1
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                'He puts his hands together and repeatedly taps his fingers. After a few breaths, he glances at a wandering monk, then lowers his voice. “Let me see thy horse. How fast is it?”
                \n\nYou lead both him and {color=#f6d6bd}Decima{/color} to the storehouse. While his steps are heavy and fierce, she doesn’t make as much as a sound.
                \n\n{color=#f6d6bd}Aeli{/color} shows no interest in your mount. “There’s this {color=#f6d6bd}enchantress{/color}. She has aught we need you to pick up and bring here,” he glances at the door. “Follow the eastern road until you find the watchtower. Don’t bother with it, it’s either empty, or a lair. Then head east, to the lake.”
                '
                '“What do you want me to bring?”' if not aeli_quest_pens_question:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                    jump aeli_quest_pens_question01
                '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                    jump aeli_quest_pens_question201
                '“What about my reward?”' if not aeli_quest_pens_question_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                    jump aeli_quest_pens_question_reward01
                '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                    jump aeli_quest_pens_question_eudocia01
                '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    jump aeli_quest_pens02

    label aeli_quest_pens_question01:
        $ aeli_quest_pens_question = 1
        menu:
            'He waves his fingers. “A set of quills. We sharpened them, and asked her to make them last. Thy pet won’t even notice.”
            '
            '“What do you want me to bring?”' if not aeli_quest_pens_question:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                jump aeli_quest_pens_question01
            '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                jump aeli_quest_pens_question201
            '“What about my reward?”' if not aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                jump aeli_quest_pens_question_reward01
            '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                jump aeli_quest_pens_question_eudocia01
            '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump aeli_quest_pens02

    label aeli_quest_pens_question201:
        $ aeli_quest_pens_question2 = 1
        menu:
            '“It’s really not. It’s just that they’re a surprise gift. No, I asked you to this room for a different reason.”
            '
            '“What do you want me to bring?”' if not aeli_quest_pens_question:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                jump aeli_quest_pens_question01
            '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                jump aeli_quest_pens_question201
            '“What about my reward?”' if not aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                jump aeli_quest_pens_question_reward01
            '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                jump aeli_quest_pens_question_eudocia01
            '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump aeli_quest_pens02

    label aeli_quest_pens_question_reward01:
        $ aeli_quest_pens_question_reward = 1
        menu:
            '“What do...st thou want?”
            '
            '“Just spread a good word about me in the order.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just spread a good word about me in the order.”')
                $ aeli_quest_pens_reward = "reputation"
                menu:
                    'He rubs his cheek with his thumb. “Interesting.”
                    '
                    '“What do you want me to bring?”' if not aeli_quest_pens_question:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                        jump aeli_quest_pens_question01
                    '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                        jump aeli_quest_pens_question201
                    '“What about my reward?”' if not aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                        jump aeli_quest_pens_question_reward01
                    '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                        jump aeli_quest_pens_question_eudocia01
                    '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        jump aeli_quest_pens02
            '“You ask me for a long and dangerous journey. Five dragons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You ask me for a long and dangerous journey. Five dragons.”')
                $ aeli_quest_pens_reward = "dragons"
                menu:
                    'He narrows his eyes, but finally nods. “Fine. They’re not of much use for us anyway.”
                    '
                    '“What do you want me to bring?”' if not aeli_quest_pens_question:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                        jump aeli_quest_pens_question01
                    '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                        jump aeli_quest_pens_question201
                    '“What about my reward?”' if not aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                        jump aeli_quest_pens_question_reward01
                    '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                        jump aeli_quest_pens_question_eudocia01
                    '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        jump aeli_quest_pens02
            '“I’m sure you can find a healing potion to spare.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure you can find a healing potion to spare.”')
                $ aeli_quest_pens_reward = "healingpotion"
                menu:
                    'He rubs his bandaged hand. “We need what we have, but I can spare thee one of the smaller bottles.”
                    '
                    '“What do you want me to bring?”' if not aeli_quest_pens_question:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                        jump aeli_quest_pens_question01
                    '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                        jump aeli_quest_pens_question201
                    '“What about my reward?”' if not aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                        jump aeli_quest_pens_question_reward01
                    '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                        jump aeli_quest_pens_question_eudocia01
                    '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        jump aeli_quest_pens02
            '“I may need to spend a few nights in the monastery.”' if not monastery_sleep_unlocked and not aeli_about_plague2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may need to spend a few nights in the monastery.”')
                $ aeli_quest_pens_reward = "shelter"
                menu:
                    'He adjusts his hood. “Fine, bring me the quills and thou wilt have the haystack all for thyself.”
                    '
                    '“What do you want me to bring?”' if not aeli_quest_pens_question:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                        jump aeli_quest_pens_question01
                    '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                        jump aeli_quest_pens_question201
                    '“What about my reward?”' if not aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                        jump aeli_quest_pens_question_reward01
                    '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                        jump aeli_quest_pens_question_eudocia01
                    '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        jump aeli_quest_pens02

    label aeli_quest_pens_question_eudocia01:
        $ aeli_quest_pens_question_eudocia = 1
        $ description_eudocia04 = "According to {color=#f6d6bd}Aeli{/color}, “her talent knows no equal, yet she’s a spider queen in the center of the web. She’s the only shell she cares about, and uses those who reach out to her. Keep your guard up.”"
        menu:
            'Despite his casual nods, an angry note distorts his already hoarse voice. “{color=#f6d6bd}Eudocia{/color} lives by herself, surrounding her house with dangerous spells. Her talent knows no equal, yet she’s a spider queen in the center of the web.” He wipes his sweat off {color=#f6d6bd}[horsename]’s{/color} side. “She’s the only shell she cares about, and uses those who reach out to her. Keep your guard up.”
            '
            '“What do you want me to bring?”' if not aeli_quest_pens_question:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to bring?”')
                jump aeli_quest_pens_question01
            '“Why is it such a secret?”' if aeli_quest_pens_question and not aeli_quest_pens_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why is it such a secret?”')
                jump aeli_quest_pens_question201
            '“What about my reward?”' if not aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about my reward?”')
                jump aeli_quest_pens_question_reward01
            '“Tell me about this {color=#f6d6bd}enchantress{/color}.”' if not aeli_quest_pens_question_eudocia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about this {color=#f6d6bd}enchantress{/color}.”')
                jump aeli_quest_pens_question_eudocia01
            '“Deal.”' if aeli_quest_pens_question and aeli_quest_pens_question_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump aeli_quest_pens02

    label aeli_quest_pens02:
        $ quest_pensformonastery = 1
        $ renpy.notify("New entry: Quills for The Monastery")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Quills for The Monastery{/i}')
        menu:
            '“Well, we’ll see how good of a rider thou art.” He glances at the door and lowers his voice. “But there’s some other stuff we need from thee. Stuff that takes subtlety and...” he straightens up, “dedication to our cause.”
            '
            '“What do you want me to do?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to do?”')
                jump aeli_quest_pens02accepting
            '“If it’s something shady, I’m out.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it’s something shady, I’m out.”')
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'With a sigh, he leads you outside. {color=#f6d6bd}Decima{/color} observes your steps carefully.
                    '
                    '(monastery1 preset)':
                        pass
            '“And what cause is that?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what cause is that?”')
                menu:
                    'He rubs his lips with his thumb, gathering his thoughts. “I may not care much about some of the souls on this side of {color=#f6d6bd}Hag Hills{/color}, but the tribes deserve our protection and guidance. Aught dark may come from the east, and soon. I want thee to investigate the threat.”
                    '
                    '“What do you want me to do?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to do?”')
                        jump aeli_quest_pens02accepting
                    '“If it’s something shady, I’m out.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it’s something shady, I’m out.”')
                        $ questionpreset = "monastery1"
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        menu:
                            'With a sigh, he leads you outside. {color=#f6d6bd}Decima{/color} observes your steps carefully.
                            '
                            '(monastery1 preset)':
                                pass

    label aeli_quest_pens02accepting:
        menu:
            '“Swear thou wilt not betray our order.”
            '
            '“And what if? You’re going to cast a curse at me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if? You’re going to cast a curse at me?”')
                menu:
                    '“We’re not dark mages. But we rarely forgive.”
                    '
                    '“I won’t betray you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t betray you.”')
                        $ custom1 = "His smile reveals his yellow teeth. "
                        $ monastery_betrayal_blocked = 1
                        jump aeli_quest_pens03
                    '(lie) “I won’t betray you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I won’t betray you.”')
                        $ pc_lies += 1
                        $ monastery_lies_decima += 1
                        $ monastery_friendship -= 1
                        $ monastery_betrayal_available = 1
                        $ custom1 = "{color=#f6d6bd}Decima{/color} raises her chin and shoulders, and while she’s still covered with shadows, you could swear her fingers are clenched around a dagger. {color=#f6d6bd}Aeli{/color} either doesn’t notice it, or chooses to ignore it - his smile reveals his yellow teeth.\n\n"
                        jump aeli_quest_pens03
                    '“You’re asking for too much.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for too much.”')
                        $ questionpreset = "monastery1"
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        menu:
                            'A long pause. “It’s dark here,” he sighs and leads you outside. {color=#f6d6bd}Decima{/color} observes your steps carefully.
                            '
                            '(monastery1 preset)':
                                pass
            '“I won’t betray you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t betray you.”')
                $ custom1 = "His smile reveals his yellow teeth. "
                $ monastery_betrayal_blocked = 1
                jump aeli_quest_pens03
            '(lie) “I won’t betray you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I won’t betray you.”')
                $ pc_lies += 1
                $ monastery_lies_decima += 1
                $ monastery_friendship -= 1
                $ monastery_betrayal_available = 1
                $ custom1 = "{color=#f6d6bd}Decima{/color} raises her chin and shoulders, and while she’s still covered with shadows, you could swear her fingers are clenched around a dagger. {color=#f6d6bd}Aeli{/color} either doesn’t notice it, or chooses to ignore it - his smile reveals his yellow teeth.\n\n"
                jump aeli_quest_pens03
            '“You’re asking for too much.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for too much.”')
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'A long pause. “It’s dark here,” he sighs and leads you outside. {color=#f6d6bd}Decima{/color} observes your steps carefully.
                    '
                    '(monastery1 preset)':
                        pass

    label aeli_quest_pens03:
        menu:
            '[custom1]“Once thou reacheth the enchantress’ house, thou wilt find golems made of stone. I’ve heard they’re larger than a lumberjack. Could tear thy pet to pieces.”
            \n\nHe looks away, talking to himself. “Can they be defeated? Can they do aught without a direct order from their mistress? We need to prepare ourselves. Learn about them as much as thou canst. Give them a good look, ask her a few {i}subtle{/i} questions.”
            '
            '“And what will I get in return?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what will I get in return?”')
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ quest_studyingthegolems = 1
                $ renpy.notify("New entry: Studying the Golems")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Studying the Golems{/i}')
                menu:
                    '“Aught we don’t share lightly. A secret - of thy choice.”
                    \n\nHe gestures for you to follow him outside. “But bring us as much news about these creatures as thou canst. It’s an all-or-naught deal.” {color=#f6d6bd}Decima{/color} stays close to him, but walks backwards, observing your steps carefully.
                    '
                    '(monastery1 preset)':
                        pass

label aeli_about_quests01preALL:
    label aeli_about_quests01pre:
        $ custom1 = "“Aught else?”"
        jump aeli_about_quests01after
        label aeli_about_quests01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the things you asked me to do...”')
            $ custom1 = "“I’m listening.”"
            jump aeli_about_quests01after
        label aeli_about_quests01after:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                '[custom1]
                '
                '“It seems that I’ve destroyed your quills. My apologies.”' if quest_pensformonastery_description02 and quest_pensformonastery == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It seems that I’ve destroyed your quills. My apologies.”')
                    jump aeli_about_questscompletingthepens01fail
                '(lie) “As I was fighting on the road, your quills were destroyed. I’m sorry.”' if quest_pensformonastery_description02 and quest_pensformonastery == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “As I was fighting on the road, your quills were destroyed. I’m sorry.”')
                    jump aeli_about_questscompletingthepens01lie
                '“Here are your quills.”' if item_magicpens and quest_pensformonastery == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here are your quills.”')
                    jump aeli_about_questscompletingthepens01
                'He asked me to bring him the quills from the enchantress. (disabled)' if quest_pensformonastery == 1 and not quest_pensformonastery_description02 and not item_magicpens:
                    pass
                '“I spoke with {color=#f6d6bd}Eudocia{/color} about her sentinels.”' if quest_studyingthegolems_description01 and quest_studyingthegolems == 1 and not aeli_golems_learned01:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with {color=#f6d6bd}Eudocia{/color} about her sentinels.”')
                    jump aeli_about_questsabouttalkingwitheudocia01
                '“I took a closer look at the golems.”' if quest_studyingthegolems_description03 and quest_studyingthegolems == 1 and not aeli_golems_learned03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I took a closer look at the golems.”')
                    jump aeli_about_questsaboutobservingthegolem01
                '“I learned more about the engravings covering the golems.”' if aeli_golems_learned03 and quest_studyingthegolems_description03b and quest_studyingthegolems == 1 and not aeli_golems_learned03b:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I learned more about the engravings covering the golems.”')
                    jump aeli_about_questsaboutobservingthegolem02
                '“I spoke with an experienced huntress about ways to fight golems.”' if dalit_beastiary_unlocked and quest_studyingthegolems == 1 and not aeli_golems_learned04b:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with an experienced huntress about ways to fight golems.”')
                    jump aeli_about_questsaboutfightingthegolem01
                '“I told you quite a lot about those creatures already.”' if aeli_golems_clues_counter >= 3 and quest_studyingthegolems == 1 and not aeli_golems_clues_three:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I told you quite a lot about those creatures already.”')
                    jump aeli_about_questsfinishedstudyingthegolems01
                'He wants me to learn more about the golems. (disabled)' if aeli_golems_clues_counter == 0 and quest_studyingthegolems == 1:
                    pass
                'I could still learn more about the golems. (disabled)' if aeli_golems_clues_counter > 0 and aeli_golems_clues_counter < 0 and quest_studyingthegolems == 1:
                    pass
                '“I want to collect my reward. A secret.”' if aeli_golems_reward_available == 1 or monastery_promise == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to collect my reward. A secret.”')
                    jump monasteryselectingasecret01
                '“That’s all.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all.”')
                    jump monasteryafterinteractions01

    label aeli_about_questscompletingthepens01fail:
        $ quest_pensformonastery = 3
        $ renpy.notify("Quest completed: Quills for The Monastery")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery{/i}')
        $ quest_pensformonastery_description05 = "I’ve brought the news about the destroyed quills to the monastery."
        $ monastery_friendship -= 4
        $ custom1 = "He spreads his arms in fury. “Apologies! The good tribe of {color=#f6d6bd}Old Págos{/color} already paid for them!”\n\nHe spreads his legs apart and raises a fist, making {color=#f6d6bd}his companion{/color} step back, but once she realizes what’s happening, she smoothly jumps behind you.\n\n{color=#f6d6bd}Aeli{/color}, however, blushes, and dusts off his robe. “Old habits. Don’t hurt the warden, {color=#f6d6bd}Decima{/color}.” While his voice lowers, his eyes betray him."
        jump aeli_about_quests01after
    label aeli_about_questscompletingthepens01lie:
        $ pc_lies += 1
        $ monastery_lies_decima += 1
        $ quest_pensformonastery = 3
        $ renpy.notify("Quest completed: Quills for The Monastery")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery{/i}')
        $ quest_pensformonastery_description03 = "I’ve saved my skin with a lie."
        $ monastery_friendship -= 2
        $ minutes += 3
        menu:
            '“Bloody beasts,” he concludes your brief tale. “At least thou art in one piece. Still, such travels ought to be the one stuff thou art good at. I’m sorely disappointed.”
            \n\n{color=#f6d6bd}Decima{/color} is bending her legs, with fists raised to the level of her waist. The man’s eyes widen.
            \n\n“Looks like the little one here doesn’t bite on thy tale, warden.”
            '
            '“Why would I lie?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would I lie?”')
                $ custom1 = "“No idea. But I better not find someone trying to sell me those damn quills tomorrow.” He crosses his arms."
                jump aeli_about_quests01after
    label aeli_about_questscompletingthepens01:
        $ quest_pensformonastery = 2
        $ quest_pensformonastery_description04 = "I’ve delivered the quills to the monastery and collected my reward."
        $ item_magicpens = 0
        $ monastery_friendship += 1
        $ renpy.notify("Quest completed: Quills for The Monastery.\nYou lost the magic quills.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery. You lost the magic quills.{/i}')
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        if aeli_about_plague2:
            $ custom1 = "He reaches for the case with his bandaged hand and opens it gently."
        else:
            $ custom1 = "He tells you to wash the outside of the case in a bucket, then to put it on the ground. After you move away, he picks it up and opens it gently with his bandaged hand."
        menu:
            '[custom1] He greets them with a wide, yellow smile.
            \n\n“So, our deal was about...”
            '
            '“A good word.”' if aeli_quest_pens_reward == "reputation":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A good word.”')
                $ monastery_friendship += 2
                $ oldpagos_reputation += 1
                $ renpy.notify("Quest completed: Quills for The Monastery")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery{/i}')
                $ custom1 = "“Ah, that’s right, thou hast done it from the goodness of thy heart.” He snorts and points at behind him. “I’ll let {color=#f6d6bd}the prelate{/color} know. And my friends from {color=#f6d6bd}Old Págos{/color}, as well. Well done.”"
                jump aeli_about_quests01after
            '“Five dragons.”' if aeli_quest_pens_reward == "dragons":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Five dragons.”')
                $ coins += 5
                show screen notifyimage( "Quest completed: Quills for The Monastery.\n+5", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery. +5 {image=cointest}{/i}')
                if aeli_about_plague2:
                    $ custom1 = "“Right...” He hesitates as he reaches to his bag and pulls out the reward, then hands it to you with his bare hand. “Fair coin for a fair work.”"
                else:
                    $ custom1 = "“Right...” He hesitates as he reaches to his bag and pulls out the reward, then puts it in a single pile on the ground and takes a few steps back. “Fair coin for a fair work.”"
                jump aeli_about_quests01after
            '“A potion.”' if aeli_quest_pens_reward == "healingpotion":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A potion.”')
                $ item_smallhealingpotion += 1
                $ renpy.notify("You received a small healing potion.\nQuest completed: Quills for The Monastery")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a small healing potion. Quest completed: Quills for The Monastery{/i}')
                if aeli_about_plague2:
                    $ custom1 = "“Right...” He pulls out a small earthenware bottle. “It’s a good one. It won’t fix a severed arm, but shall seal a wound.” He hands it to you with his bare hand. “Well done.”"
                else:
                    $ custom1 = "“Right...” He pulls out a small earthenware bottle. “It’s a good one. It won’t fix a severed arm, but shall seal a wound.” He puts it on the ground and takes a few steps back. “Well done.”"
                jump aeli_about_quests01after
            '“The storehouse.”' if aeli_quest_pens_reward == "shelter" and not monastery_sleep_unlocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The storehouse.”')
                $ monastery_sleep_unlocked = 1
                $ renpy.notify("New shelter unlocked.\nQuest completed: Quills for The Monastery")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked. Quest completed: Quills for The Monastery{/i}')
                $ custom1 = "“Right, a {i}hideout{/i} for thee. We’ll lower the bridge even if thou arrive after dusk. But remember, thou wilt find no pile of furs here. Just the hay.”"
                jump aeli_about_quests01after
            '“The storehouse, though I guess I don’t need it anymore.”' if aeli_quest_pens_reward == "shelter" and monastery_sleep_unlocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The storehouse, though I guess I don’t need it anymore.”')
                menu:
                    '“True. I’m prepared to reward you regardless.”
                    '
                    '“Just spread a good word about me.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just spread a good word about me.”')
                        $ aeli_quest_pens_reward = "reputation"
                        $ monastery_friendship += 2
                        $ oldpagos_reputation += 1
                        $ renpy.notify("Quest completed: Quills for The Monastery")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery{/i}')
                        $ custom1 = "“Ah, that’s right, thou hast done it from the goodness of thy heart.” He snorts and points at behind him. “I’ll let {color=#f6d6bd}the prelate{/color} know. And my friends from {color=#f6d6bd}Old Págos{/color}, as well. Well done.”"
                        jump aeli_about_quests01after
                    '“I’ll take five dragons.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take five dragons.”')
                        $ aeli_quest_pens_reward = "dragons"
                        $ coins += 5
                        show screen notifyimage( "Quest completed: Quills for The Monastery.\n+5", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Quills for The Monastery. +5 {image=cointest}{/i}')
                        if aeli_about_plague2:
                            $ custom1 = "“Right...” He hesitates as he reaches to his bag and pulls out the reward, then hands it to you with his bare hand. “Fair coin for a fair work.”"
                        else:
                            $ custom1 = "“Right...” He hesitates as he reaches to his bag and pulls out the reward, then puts it in a single pile on the ground and takes a few steps back. “Fair coin for a fair work.”"
                        jump aeli_about_quests01after
                    '“Can I take a healing potion?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I take a healing potion?”')
                        $ aeli_quest_pens_reward = "healingpotion"
                        $ item_smallhealingpotion += 1
                        $ renpy.notify("You received a small healing potion.\nQuest completed: Quills for The Monastery")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a small healing potion. Quest completed: Quills for The Monastery{/i}')
                        if aeli_about_plague2:
                            $ custom1 = "“Right...” He pulls out a small earthenware bottle. “It’s a good one. It won’t fix a severed arm, but shall seal a wound.” He hands it to you with his bare hand. “Well done.”"
                        else:
                            $ custom1 = "“Right...” He pulls out a small earthenware bottle. “It’s a good one. It won’t fix a severed arm, but shall seal a wound.” He puts it on the ground and takes a few steps back. “Well done.”"
                        jump aeli_about_quests01after

    label aeli_about_questsabouttalkingwitheudocia01: #“I spoke with {color=#f6d6bd}Eudocia{/color} about her sentinels.”
        $ aeli_golems_learned01 = 1
        $ aeli_golems_clues_counter += 1
        $ monastery_friendship += 1
        $ minutes += 10
        $ custom1 = "Your report takes you a good few minutes, especially since {color=#f6d6bd}Aeli{/color} spares you no questions. After you mention that the golems are meant to be available for purchase, he gives {color=#f6d6bd}Decima{/color} a worried look.\n\n“She’s inviting a dragon,” he says in the end. He walks up and down the path with hands behind his back, like a commander preparing themselves for a battle. “No tribe could stop a squad of these. Most troubling news, awful.”"
        jump aeli_about_quests01after

    label aeli_about_questsaboutobservingthegolem01: #“I took a closer look at the golems.”
        if not aeli_golems_learned04b:
            $ quest_studyingthegolems_description02 = "The monk has advised me to look for guidance about fighting off the golems. Maybe an experienced fighter could share their knowledge with me."
        $ aeli_golems_clues_counter += 1
        $ aeli_golems_learned03 = 1
        $ monastery_friendship += 1
        $ minutes += 5
        $ description_eudocia06 = "Her golems are unusual, as if she’s designed them without relying on any inventions of previous generations."
        $ custom1 = "You describe their looks and mention the unusual engravings you noticed on the larger rocks. {color=#f6d6bd}Aeli{/color} listens carefully, but it takes him a few heartbeats to respond.\n\n“Such signs may be dangerous,” he wipes his lips with his bandaged hand. “I’ve read about the city golems. They’re {i}different{/i}. We may need help from an experienced fighter... But we lack such souls in the order.” He finally lowers his hand, observing a child who hums a simple melody at the edge of the cliff."
        jump aeli_about_quests01after

    label aeli_about_questsaboutobservingthegolem02:
        $ aeli_golems_learned03b = 1
        $ aeli_golems_clues_counter += 1
        $ monastery_friendship += 1
        $ minutes += 2
        $ custom1 = "{color=#f6d6bd}Aeli’s{/color} eyes are wide open. He and {color=#f6d6bd}Decima{/color} exchange telling glances. He rubs his bandaged hand. “If those signs work, who knows what kind of words she can select next.” His voice is tense, but hoarse, forcing him to cough. “{i}Take supplies{/i},” maybe? {i}Hunt humans{/i}?”"
        jump aeli_about_quests01after

    label aeli_about_questsaboutfightingthegolem01: #“I spoke with an experienced huntress about ways to fight golems.”
        $ aeli_golems_learned04b = 1
        $ aeli_golems_clues_counter += 1
        $ monastery_friendship += 1
        $ minutes += 2
        $ custom1 = "You share {color=#f6d6bd}Dalit’s{/color} instructions. {color=#f6d6bd}The monk{/color} rests his hands behind the rope around his waist.\n\n“What thou sayest mirrors what I read. Good job, warden. The knowledge of the codices is worth more than dragon bones, but one learns to doubt it. {color=#f6d6bd}Our prelate{/color} says, {i}the second scribe is the first one to be trusted{/i}.”"
        jump aeli_about_quests01after

    label aeli_about_questsfinishedstudyingthegolems01: #“I told you quite a lot about those creatures already.”
        $ aeli_golems_reward_available = 1
        $ aeli_golems_clues_three = 1
        $ quest_studyingthegolems_description06 = "I can return to the monastery and ask for a {i}secret{/i} whenever I want."
        $ renpy.notify("Journal updated: Studying the Golems")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
        menu:
            'He spares you a kind smile. “You did. I’ll speak with {color=#f6d6bd}the prelate{/color} soon. Let me know when thou art ready to collect thy reward.”
            '
            '“I will.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I will.”')
                jump aeli_about_quests01pre

label monasteryselectingasecretALL:
    label monasteryselectingasecret01:
        $ custom1 = "“What {i}overwhelms{/i} thee?”"
        label monasteryselectingasecret01alt:
            menu:
                '[custom1]
                '
                '“I don’t really need your guidance. Could you, instead, forgive me for losing your quills?”' if quest_pensformonastery_description05 and quest_pensformonastery == 3 and not quest_pensformonastery_forgiven:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t really need your guidance. Could you, instead, forgive me for losing your quills?”')
                    jump monasterysecretsaboutforgiveness01
                '“Where is {color=#f6d6bd}Asterion{/color}?”' if not aeli_about_secret_asterion and not asterion_found and quest_asterion == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where is {color=#f6d6bd}Asterion{/color}?”')
                    jump monasterysecretsaboutasterion01
                '“What is it that you really do in this place?”' if not quest_explorepeninsula_description13 and not aeli_about_secret_cave:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What is it that you really do in this place?”')
                    jump monasterysecretsaboutthecaveitself01
                '“How can I find {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”' if quest_reachthepaganvillage == 1 and not greenmountaintribe_firsttime and not description_greenmountaintribe13:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can I find {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”')
                    jump monasterysecretsaboutgreenmountaintribe01
                '“Is the coast really as difficult to navigate through as people think?”' if not quest_explorepeninsula_description03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is the coast really as difficult to navigate through as people think?”')
                    jump monasterysecretsaboutbeastthecoast01
                '“Tell me about {color=#f6d6bd}High Island{/color}.”' if asterion_highisland_knowsabout and not asterion_found and not aeli_about_secret_highisland:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}High Island{/color}.”')
                    jump monasterysecretsaboutbeasttheisland01
                '“What happened to {color=#f6d6bd}the ruined village{/color} in the south?”' if quest_ruins == 1 and not ruinedvillage_truth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened to {color=#f6d6bd}the ruined village{/color} in the south?”')
                    jump monasterysecretsaboutbeasttheruinedvillage01
                '“Tell me how to find the bandits’ hideout.”' if quest_intelforpeltnorth == 1 and not banditshideout_bandits_pchearedabouthideout:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me how to find the bandits’ hideout.”')
                    jump monasterysecretsaboutthebanditshideout01
                '“Teach me how to awaken the giant statue in the far east.”' if quest_sleepinggiant < 2 and not giantstatue_pray_knows and giantstatue_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Teach me how to awaken the giant statue in the far east.”')
                    jump monasterysecretsaboutsleepinggiant01
                '“I won’t need your {i}secrets{/i}. I can seek answers on my own.”' if not (quest_pensformonastery_description05 and quest_pensformonastery == 3 and not quest_pensformonastery_forgiven) and not (not aeli_about_secret_asterion and not asterion_found and quest_asterion == 1) and not (not quest_explorepeninsula_description13) and not (quest_reachthepaganvillage == 1 and not greenmountaintribe_firsttime) and not (not quest_explorepeninsula_description03) and not (asterion_highisland_knowsabout and not asterion_found and not aeli_about_secret_highisland) and not (quest_ruins == 1 and not ruinedvillage_truth) and not (quest_intelforpeltnorth == 1 and not banditshideout_bandits_pchearedabouthideout) and not (quest_sleepinggiant < 2 and not giantstatue_pray_knows and giantstatue_firsttime):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t need your {i}secrets{/i}. I can seek answers on my own.”')
                    jump monasterysecretsrejected01
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    jump aeli_about_quests01after

    label monasterysecretsrejected01: #“I don’t really need your guidance. Could you, instead, forgive me for losing your quills?”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
            $ monastery_friendship += 2
        if monastery_promise == 1:
            $ monastery_promise = 2
            $ monastery_friendship += 2
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quest_pensformonastery_forgiven = 1
        $ quest_pensformonastery = 2
        menu:
            'He gives you a puzzled look, but then his snort turns into laughter. “Very well, great!”
            '
            '(monastery1 preset)':
                pass

    label monasterysecretsaboutforgiveness01: #“I don’t really need your guidance. Could you, instead, forgive me for losing your quills?”
        $ monastery_friendship += 4
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quest_pensformonastery_forgiven = 1
        $ quest_pensformonastery = 2
        menu:
            'His snort turns into laughter. “Very well, great! All is forgiven.”
            '
            '(monastery1 preset)':
                pass

    label monasterysecretsaboutasterion01: #“Where is {color=#f6d6bd}Asterion{/color}?”
        $ aeli_about_secret_asterion = 1
        menu:
            '“I... Don’t know,” he shrugs. “I can offer thee the last place he asked me about. A place away from our roads.”
            '
            '“If you mean {color=#f6d6bd}The Tribe of The Green Mountain{/color}, I already know about it.”' if quest_reachthepaganvillage_description00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you mean {color=#f6d6bd}The Tribe of The Green Mountain{/color}, I already know about it.”')
                $ custom1 = "“Dost thou, now. It’s a dangerous place. It would be wise to abandon thy search.”"
                jump monasteryselectingasecret01alt
            '“Any clue will help.”' if not quest_reachthepaganvillage_description00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any clue will help.”')
                if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
                    $ quest_studyingthegolems = 2
                    $ aeli_golems_reward_available = 2
                    $ quest_studyingthegolems_description07 = "I collected my reward."
                elif monastery_promise == 1:
                    $ monastery_promise = 2
                if quest_reachthepaganvillage == 1:
                    $ renpy.notify("Journal updated: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
                elif not quest_reachthepaganvillage:
                    $ quest_reachthepaganvillage = 1
                    $ renpy.notify("New entry: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
                $ quest_reachthepaganvillage_description00b = "I’ve heard a rumor that {color=#f6d6bd}Asterion{/color} has kept in touch with them."
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“Look for {color=#f6d6bd}The Tribe of The Green Mountain{/color}. These pagans live in the fogs and shadows of the mountain peaks, without trade, without rumors. That’s were {color=#f6d6bd}Asterion{/color} was heading.”
                    \n\nYou ask him how to reach this tribe, and he smirks. “That’s a very different secret, warden.”
                    '
                    '(monastery1 preset)':
                        pass
            '“In that case, I want to ask about something else.”' if not quest_reachthepaganvillage_description00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In that case, I want to ask about something else.”')
                $ custom1 = "“Then do it.”"
                jump monasteryselectingasecret01alt

    label monasterysecretsaboutthecaveitself01: #“What is it that you really do in this place?”
        $ aeli_about_secret_cave = 1
        menu:
            'He raises his bandaged palm. “We worship, and we work. If there’s aught more to say, our most trusted allies will learn all about it. I refuse to answer.”
            '
            '“Let me change my question, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me change my question, then.”')
                $ custom1 = "He waits with an unpleasant smile."
                jump monasteryselectingasecret01alt

    label monasterysecretsaboutgreenmountaintribe01: # “How can I find {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if not quest_reachthepaganvillage_description01 or quest_reachthepaganvillage_description02:
            $ renpy.notify("Journal updated: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
        $ quest_reachthepaganvillage_description01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
        $ description_greenmountaintribe13 = "According to {color=#f6d6bd}Aeli{/color}, “they will soon become little more than a rumor, then a legend. But not against their will - The Tribe has been torn away from its soul centuries ago, and now aims to be lost to the world.”"
        menu:
            '“They will soon become little more than a rumor, then a legend. But not against their will - {color=#f6d6bd}The Tribe{/color} has been torn away from its soul centuries ago, and now aims to be lost to the world. Not unlike a few monks I’ve met,” he looks around with a shadow of a smile. “Ride east, far east. Find a stone bridge that’s between the watchtower and the tavern.”
            \n\nHis speech becomes slower, seeking the almost forgotten memories. “Moving east from there, upstream, will get thee to their mountains. At their feet is a large statue, then the path uphill. Follow it, and enter the cave mouth at its end, with no fields or gardens. That’s where thou wilt find them.”
            '
            '(monastery1 preset)':
                pass

    label monasterysecretsaboutbeastthecoast01: #“Is the coast really as difficult to navigate through as people think?”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quest_explorepeninsula_description03 = "I heard that some of the locals know ways to safely move through the rocky coasts, so it may be possible to maintain access by the sea after all."
        $ description_galerocks04 = "I heard that the fishers from {color=#f6d6bd}Gale Rocks{/color} know how to move between the coastal rocks."
        menu:
            '“Yes and no. The city ships are too large, too heavy. The coastal rocks are like teeth, but the fishers from {color=#f6d6bd}Gale Rocks{/color} cut some of them down. One needs a vessel small enough to fit through, but it’s {i}possible{/i}, even with heavier cargo. An outsider won’t reach the land from the deep waters, but there are guides who could handle that route.”
            '
            '(monastery1 preset)':
                pass

    label monasterysecretsaboutbeasttheisland01: #“Tell me about {color=#f6d6bd}High Island{/color}.”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        $ aeli_about_secret_highisland = 1
        $ minutes += 10
        $ highisland_howtoreach_pcknows = 1
        if not quest_reachthepaganvillage:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("New entry: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
        elif quest_reachthepaganvillage == 1:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("Journal updated: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
        $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
        $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
        $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
        $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
        $ description_highisland06 = "It’s possible that the island still hides ruins of an old village."
        menu:
            '“Art thou asking me for a history lesson,” he looks you in the eyes, “or is that where thou art heading next?”
            \n\n“A bit of both,” you put simply, and he clears his throat. “Then I’ll not bore myself with the details. Thou canst see the island from the coast, it’s the largest scrap of land that can be reached in a few hours, though it’s easier said than done. The ships can’t cross the waters from here to there, while a boat won’t reach the top of the cliffs that surround it. It sticks out from the ocean like a rock, thou seest, and is as wild as the deepest woods.”
            \n\nHe rubs his hand. “A single tribe used to live there. {color=#f6d6bd}The Tribe of The Green Mountain{/color}. They were thrown away by the army of {color=#f6d6bd}Hovlavan{/color}, crushed. But there used to be days, centuries ago, when they were trading with other Northerners.”
            \n\nHe looks you in the eyes, making sure you’re listening. “Reach the eastern coast, or {i}the wall{/i} of {color=#f6d6bd}High Island{/color}, in the middle of the night, when the water is at its highest. A waterfall there, who knows which one, hides a cave that used to serve as a harbor for fishers. With some rope, you can climb up the rocks.”
            \n\nA long pause. “A few souls tried to reach the volcano in the heart of the island, for some say it hides the treasure of {color=#f6d6bd}The Tribe{/color}. This place is but a grave now, the lair of beasts. Now be wise and never use what I told you.”
            '
            '“I’ll consider it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll consider it.”')
                jump monasteryafterinteractions01
            '“I make no promises.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I make no promises.”')
                jump monasteryafterinteractions01

    label monasterysecretsaboutbeasttheruinedvillage01: #“What happened to {color=#f6d6bd}the ruined village{/color} in the south?”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        menu:
            'He looks at the huge hourglass and rubs his hands together, gathering his thoughts for a good minute. “It happened ten years ago.” His voice is solemn, but entwined with remorse. “At that time, {color=#f6d6bd}Thais{/color} of {color=#f6d6bd}Howler’s Dell{/color} offered the tribes to unite under her command. Taxes for the services of her guards. She can spare a strong bunch of people. Thou wouldst need dozens of armed people, or the wrath of the herds, to break through {color=#f6d6bd}Howler’s{/color} walls anyway.”
            \n\n“The people of {color=#f6d6bd}Steep House{/color} were the first ones to refuse, even though they had been the closest allies of {color=#f6d6bd}Howler’s{/color}. In return, {color=#f6d6bd}Thais’{/color} guards and druids made an example of them. The first raid in recent memory.”
            \n\n“{color=#f6d6bd}Steep House{/color} surrendered without a fight, but {color=#f6d6bd}the mayor{/color} didn’t know when to stop, and almost turned that place into ruins. The locals had to cut all the trees from their garden to fix their broken houses and walls, and turned a clearing into farmlands to have any crops, but nature had already been pushed too much. Before the end of the season, {color=#f6d6bd}Steep House{/color} was attacked again, this time by the beasts. Only a few souls survived.”
            \n\nYou try to ask him for more details, but he coughs in his bandaged hand and gestures for you to step back. “People want to forget those days, warden. Nah, they agree those days {i}ought to{/i} be forgotten. Asking for the truth won’t do thee any favors. Thou knowest what thou must.”
            '
            '“That’s... Quite a tale.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s... Quite a tale.”')
                $ quest_ruins_description_truestory = "{color=#f6d6bd}The monks{/color} blame the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to their story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                $ description_ruinedvillage02 = "{color=#f6d6bd}The monks{/color} blame the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to their story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                $ description_thais06 = "{color=#f6d6bd}The monks{/color} blame her for destroying the southern village."
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                $ ruinedvillage_truth = 1
                $ ruinedvillage_name = "Steep House"
                $ minutes += 10
                jump monasteryafterinteractions01

    label monasterysecretsaboutthebanditshideout01: #“Tell me how to find the bandits’ hideout.”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        $ questionpreset = "monastery1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ banditshideout_bandits_pchearedabouthideout = 1
        if quest_intelforpeltnorth == 1:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ banditshideout_pcknowswhere = 1
        menu:
            '“I’m not sure that I should...” He glances at {color=#f6d6bd}Decima{/color}, but she avoids his eyes. “Fine. Y... {i}thou{/i} needest to look for the camp in the deep woods. Return to the crossroads, then ride east, past the gate. Stay on the road until thou reachest the cairn. Then seek the path north. It will lead thou to the camp.”
            '
            '(monastery1 preset)':
                pass

    label monasterysecretsaboutsleepinggiant01: #“Teach me how to awaken the giant statue in the far east.”
        if quest_studyingthegolems == 1 and aeli_golems_reward_available == 1:
            $ quest_studyingthegolems = 2
            $ aeli_golems_reward_available = 2
            $ renpy.notify("Quest completed: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Studying the Golems{/i}')
            $ quest_studyingthegolems_description07 = "I collected my reward."
        elif monastery_promise == 1:
            $ monastery_promise = 2
        if not quest_sleepinggiant:
            $ quest_sleepinggiant = 1
        $ giantstatue_pray_knows = 1
        $ quarters += 2
        menu:
            '“I...” He looks at {color=#f6d6bd}Decima{/color}, who returns his puzzled stare. “I know what place thou mean...eth, but I’ve got no such knowledge. Let me ask the others.” He leaves you with {color=#f6d6bd}his companion{/color}, who also takes a few steps away, not bothering with idle chats. She stares in the distance, moving her shoulders to the tune played by the cold gale and observing an eagle that preens its feathers.
            \n\nAfter {color=#f6d6bd}Aeli’s{/color} return, his face is a bit paler. “A truth of the pagans thou seekest, but if thou wishest so truly, that’s what I’ll give thee. Here’s what I was told: {i}kneel and lower your head, and pray these words, ten times, if not more.{/i}” He utters a bunch of nonsense, and smirks at your confused look. “It means {i}oh, the spirits and the giantfathers, be with our paths, and not in thunder{/i}. It’s not so simple, but that’s the gist of it. Now, follow my lead.”
            \n\nHe spends a good few minutes teaching you the phrases from the Old Speech until you repeat them without mistakes, though also no comprehension. While your tongue is not used to some of the sounds, the rhythm of the poem helps a lot. “I hope ye, {i}thou{/i} dost not expect the cold rock to move like a golem. It’s all a waste of thy time,” he chuckles, “but yes, that’s the secret.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                $ renpy.notify("Journal updated: The Sleeping Giant")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
                jump monasteryafterinteractions01

label aeli_about_healedplagueALL:
    label aeli_about_healedplague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”')
        $ aeli_about_plague2 = 1
        $ monastery_prelate_invited = 1
        if not aeli_about_leader:
            $ aeli_about_leader = 1
            $ aeli_about_monastery += 1
        $ monastery_friendship += 5
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '{color=#f6d6bd}Aeli{/color} flinches as doubt and distrust replace his look of surprise. “How?”
            '
            '“I helped an elder druid from {color=#f6d6bd}Howler’s Dell{/color} recover his strength. He healed the people of {color=#f6d6bd}Old Págos{/color} and with a bit of luck, the illness won’t return.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I helped an elder druid from {color=#f6d6bd}Howler’s Dell{/color} recover his strength. He healed the people of {color=#f6d6bd}Old Págos{/color} and with a bit of luck, the illness won’t return.”')
                menu:
                    'He looks at {color=#f6d6bd}Decima{/color}, not sure how to react, but her wide-opened eyes don’t help him much.
                    \n\nHe reaches out to you with an open palm of his bandaged hand, his fingers are flinching. “Will ye wait here? I’ll gather our order, we’d be honored to hear the entire story.” For a moment, he sounds exactly like the tribe from {color=#f6d6bd}Old Págos{/color}.
                    '
                    '“Sure. I have time.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I have time.”')
                        $ quarters += 1
                        menu:
                            'He climbs uphill and enters the cave mouth next to the wooden bridge. {color=#f6d6bd}His short companion{/color} follows your movements like an owl would a snake, blocking your path to the storehouse. You feel the weight of your axe. Soon, new hooded figures gather in the yard. “Is it true?,” you hear a couple of times.
                            \n\nWhen {color=#f6d6bd}Aeli{/color} returns, there’s maybe twenty souls around you, sitting on the ground, leaning against the walls, standing upright, or wandering around, keenly observing you. The oldest man, wrinkled, blind, and tiny, is sitting on a stool brought by a boy who can’t be older than ten.
                            \n\nNot all of them wear sandals, or carry bags, or have their hoods on, but all of them wear similar dark robes. Seems like only the children are allowed to keep hair longer than an inch.
                            \n\nIn the city harbor, many would take them for refugees.
                            '
                            'I tell them the entire story.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell them the entire story.')
                                $ monastery_friendship += 1
                                $ quarters += 2
                                menu:
                                    'They keep interrupting you with questions about the druid, his powers, or your motivations, but once you mention the role of the altar, their looks get suspicious. They seem to have a decent understanding of {color=#f6d6bd}Beholder{/color} and the gifts it seeks. The interrogation fades away only after you answer many of their doubts and assure them a good couple of times that the village shows no sign of an overhanging curse.
                                    \n\nFinally, {color=#f6d6bd}Aeli{/color} asks the gathering to return to their duties. He gives you a serious look, rubbing the liver spots on his hands. “There’s aught else we need to discuss.”
                                    '
                                    '“Go ahead.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Go ahead.”')
                                        jump aeli_about_healedplague02
                            'I don’t mention anything outside of the knowledge of the people of {color=#f6d6bd}Old Págos{/color}. Especially when it comes to {color=#f6d6bd}Beholder{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t mention anything outside of the knowledge of the people of {color=#f6d6bd}Old Págos{/color}. Especially when it comes to {color=#f6d6bd}Beholder{/color}.')
                                $ monastery_friendship += 2
                                $ quarters += 1
                                menu:
                                    'They keep interrupting you with questions about the druid, his powers, or your motivations, and while avoiding the pagan altar makes you stumble once or twice, your story goes smoothly. Their doubts turn into warm thanks, despite the few raised eyebrows of the elders. A young boy mentions his sister, but is then reprimanded to “forget about his past.”
                                    \n\nFinally, {color=#f6d6bd}Aeli{/color} asks the gathering to return to their duties. He gives you a serious look, rubbing the liver spots on his hands. “There’s aught else we need to discuss.”
                                    '
                                    '“Go ahead.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Go ahead.”')
                                        jump aeli_about_healedplague02
                    '“You don’t need to hear it from me. Go and meet with the villagers, they’ll tell you all you need to know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t need to hear it from me. Go and meet with the villagers, they’ll tell you all you need to know.”')
                        $ minutes += 5
                        menu:
                            'He scowls at you for a bit, but then sighs and asks you to wait. He climbs uphill and enters the cave mouth next to the wooden bridge.
                            \n\n{color=#f6d6bd}His short companion{/color} follows your movements like an owl would a snake, blocking your path to the storehouse. You feel the weight of your axe.
                            \n\nAfter {color=#f6d6bd}Aeli’s{/color} returns, he’s rubbing the liver spots on his hands. “There’s aught else we need to discuss.”
                            '
                            '“Go ahead.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Go ahead.”')
                                jump aeli_about_healedplague02

    label aeli_about_healedplague02:
        if not quest_monasterysupport:
            $ quest_monasterysupport = 1
            $ renpy.notify("New entry: The Support of Monks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Monks{/i}')
        if (monastery_friendship+appearance_charisma) > 10:
            menu:
                '“{color=#f6d6bd}Our prelate{/color} wants to see you, thou, {i}thee{/i},” he coughs. “They’re old and feeble, but they decided it’s an urgent matter. Follow me into {color=#f6d6bd}the temple{/color}. It won’t take long.”
                \n\nHe heads toward the nearest cave entrance. You look around and meet a few curious eyes, as well as {color=#f6d6bd}Decima’s{/color} grin. She keeps one hand behind her back.
                '
                'I’m happy to follow him anyway.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m happy to follow him anyway.')
                    $ custom1 = ""
                    jump aeli_about_healedplague03
                '...Good thing I’m armed.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...Good thing I’m armed.')
                    $ custom1 = ""
                    jump aeli_about_healedplague03
        else:
            menu:
                '“{color=#f6d6bd}Our prelate{/color} wants to see ye, thou, {i}thee{/i},” he coughs. “But they’re old and feeble, and don’t speak unless they have to. And only with those who can be trusted.” He gives you a telling look. “Thou mayest not be a friend of our order, but we hope to find in thee our ally.”
                '
                '“I’d be honored to meet with them, and I’ll try my best to gain your trust.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d be honored to meet with them, and I’ll try my best to gain your trust.”')
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'He snorts. “Thy deeds will speak for thee.”
                        '
                        '(monastery1 preset)':
                            pass
                '“I make no promises.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I make no promises.”')
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        '“Good. Act, and act wisely.”
                        '
                        '(monastery1 preset)':
                            pass

label aeli_about_copper01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should take it directly to the guild, but... “To prove my good will, I’m ready to tell you about the copper vein I found in the North.”')
    $ foragingground_foraging_vein_sabotaged = 1
    $ aeli_about_copper = 1
    $ monastery_friendship += 3
    $ questionpreset = "monastery1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ minutes += 5
    menu:
        'He stares at you for a few long breaths, then freezes with a raised hand. “Explain.”
        \n\nYou tell him the entire story, and while every now and then he glances at {color=#f6d6bd}Decima{/color}, she seems more interested in the picture of a wagon that she draws on the path with her boot.
        \n\n“That’s quite an offering that thou broughtest,” he admits carefully, but then lets out a weak chuckle. “Very well. Once we’re sure our friends from {color=#f6d6bd}Old Págos{/color} are free of the plague for good, we’ll prepare an expedition. To us, rocks are hardly a challenge.”
        '
        '(monastery1 preset)':
            pass

label monasteryrespondingtoinvitationtomeetprelateALL:
    label monasteryrespondingtoinvitationtomeetprelate01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Will {color=#f6d6bd}the prelate{/color} agree to meet with me?”')
        if (monastery_friendship+appearance_charisma) > 10:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            $ world_known_npcs += 1
            $ custom1 = "He adjusts his hood. “The time is right. Follow me into {color=#f6d6bd}the temple{/color}. It won’t take long.” "
            jump aeli_about_healedplague03
        else:
            $ questionpreset = "monastery1"
            menu:
                '“This isn’t the right time. Or rather - thou mayest not be the right soul.”
                '
                '(monastery1 preset)':
                    pass

    label aeli_about_healedplague03:
        stop nature fadeout 4.0
        menu:
            '[custom1]You join {color=#f6d6bd}Aeli{/color} in front of the entrance. You run your eyes over the harsh, gray floor, sparsely covered by tufts of grass and mushrooms. Only a few steps separate you from the darkness.
            \n\n“Take a wrong step and thou wilt break thy neck,” his quiet voice echoes through the corridor, but there are also other sounds reaching you from the depths - the repetitive hits of a hammer and chisel, as well as of a distant pickaxe.
            \n\nThe man doesn’t look at you. “Hand on my shoulder. Don’t let go.”
            '
            'I grasp his robe firmly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grasp his robe firmly.')
                jump aeli_about_healedplague03b
            'I touch his shoulder gently.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch his shoulder gently.')
                jump aeli_about_healedplague03b

    label aeli_about_healedplague03b:
        show areapicture monasteryinside00 at basicfade
        stop music fadeout 4.0
        play nature "audio/ambient/monastery02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        menu:
            'You leave the light behind and your pace slows down. {color=#f6d6bd}Decima’s{/color} steps are followed by the sweeping sound of her robe. For a few breaths your heels hit the solid rock, then move onto wooden logs. The echo of the occasional creaks is worthy of a wraith. Your gasp as well when you stumble over a rope, but {color=#f6d6bd}Aeli’s{/color} confident hand saves you from falling to the floor.
            \n\nAfter a minute or two, you get used to the scent of soggy beams. The gentle draft makes you think of a stream, and you focus your ears - the hum of water is weak, but, once noticed, unmistakable.
            \n\nCounting your steps leads you to nothing. You don’t make any sharp turns, following the rounded corridor. At one point, {color=#f6d6bd}the monk{/color} grabs your free fingers and makes you touch the smooth wall. “Watch your steps,” you hear the hoarse whisper, then walk down the stairs carefully. Another minute goes by, and it happens again, then again.
            \n\n“Almost there,” {color=#f6d6bd}Aeli{/color} stops in place.
            '
            'All I can do is wait.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- All I can do is wait.')
                $ quarters += 1
                menu:
                    'You recognize the sound of him opening his bag. He turns your hand around, palm up, and covers it with cold, soft balm.
                    \n\n“Put it on your eyelids,” he’s voice is confident. “It will help, but not for long. Don’t walk away.”
                    \n\nYou rub your eyelids, catching the scent of snow and tallow candles.
                    '
                    'I look around.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                        show areapicture monasteryinside01 at slowfade
                        menu:
                            'For a few heartbeats, the brightness is overwhelming, even after you cover your eyes, but the sensation fades away. Everything around you turns gray - the walls, your companions, even your very skin are now monuments made of ash.
                            \n\nThe hollow mountain has the shape of a cone. You step back, away from the edge of the narrow, wooden platform, only to then approach it and look down. The magic balm is strong - it allows you to spot maybe two dozen layers of scaffolding.
                            \n\nYou spot another hooded figure a couple of floors below you. It holds the chisel against the wall, hitting it with the hammer. Their confident hands maintain the tiring rhythm.
                            '
                            'I inspect the engravings behind me.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the engravings behind me.')
                                if pc_class == "scholar":
                                    $ at_unlock_knowledge = 1
                                    $ at = 0
                                menu:
                                    'You can’t tell their age, but the cuts are deep. They’re letters, larger than your hand, and some of them are filled with old, dry paint - although to you, like everything else, it looks gray.
                                    \n\n“Read it out loud,” you hear a voice coming from your left, not much louder than the distant humming of water.
                                    '
                                    'I approach the closest painted letter and start reading from there.' ( condition="at == 'knowledge'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the closest painted letter and start reading from there.')
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        $ monastery_friendship += 2
                                        $ quest_explorepeninsula_description13b = "I’ve read a part of the texts myself, so I’m sure the monks weren’t lying to me."
                                        menu:
                                            '“They heard of Samara’s deeds,” after the echo fills the village-size chamber, you lower your voice, “and believed her, for her soul carried no lies. They followed her north, like The Wright had told her, and built houses of wood in The Land of Three Lakes. The Wright taught Samara new tools and new traps, and her children and grandchildren have never seen hunger, for their land was tamed.”
                                            \n\nThe person in a monk’s robe is sitting on a bench, covering themselves with a headless pelt. They’re short, wrinkled, skinny as if they haven’t eaten in years. They sit still, with their head leaning against the wall, eyes closed, and hands folded.
                                            \n\n“Dost thou know what these words are?” Their voice is like a dying breath.
                                            '
                                            '“Of course. It’s from Wright’s Tablets.”' if pc_religion == "theunitedchurch" or pc_religion == "fellowship" or pc_religion == "ordersoftruth" or pc_religion == "unknown":
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Of course. It’s from Wright’s Tablets.”')
                                                jump aeli_about_healedplague05cpcknows
                                            '“It’s from Wright’s Tablets, I think.”' if pc_religion == "unknown" or pc_religion == "none" or pc_religion == "pagan":
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s from Wright’s Tablets, I think.”')
                                                jump aeli_about_healedplague05cpcknows
                                    'I look toward the one who speaks. “I don’t know how.”' ( condition="at != 'knowledge'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look toward the one who speaks. “I don’t know how.”')
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        menu:
                                            '“Few travelers can,” their voice starts like a dying breath, but then shifts, resembling an oration delivered by a priest. “They heard of Samara’s deeds, and believed her, for her soul carried no lies. They followed her north, like The Wright had told her, and built houses of wood in The Land of Three Lakes. The Wright taught Samara new tools and new traps, and her children and grandchildren have never seen hunger, for their land was tamed.”
                                            \n\nThe person in a monk’s robe is sitting on a bench, covering themselves with a headless pelt. They’re short, wrinkled, skinny as if they haven’t eaten in years. They sit still, with their head leaning against the wall, eyes closed, and hands folded.
                                            \n\n“Dost thou know what these words are?”
                                            '
                                            '“Of course. It’s from Wright’s Tablets.”' if pc_religion == "theunitedchurch" or pc_religion == "fellowship" or pc_religion == "ordersoftruth":
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Of course. It’s from Wright’s Tablets.”')
                                                jump aeli_about_healedplague05cpcknows
                                            '“It’s from Wright’s Tablets, I think.”' if pc_religion == "unknown" or pc_religion == "none":
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s from Wright’s Tablets, I think.”')
                                                label aeli_about_healedplague05cpcknows:
                                                    $ monastery_friendship += 1
                                                    menu:
                                                        'They have the accent of {color=#f6d6bd}Hovlavan{/color} elders, but their lips are struggling to utter any sound. “Well done. We’re on the second floor of the {i}The Tribe of Leaves{/i}. The Tribe started as foragers and fruit pickers, too afraid to hunt, with no faith to guide them outside of their cave. But The Wright inspired them with The Truth of what they were and of what they could become. They helped Adir build one of The Ten Cities, and their blood and memory now remains in each of us.”
                                                        \n\n“I’m exhausted,” their breathing remains silent, but their chest starts to rise and fall, “but I wanted thee to see this place.”
                                                        '
                                                        '“I can see it. But what is it, exactly?”':
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can see it. But what is it, exactly?”')
                                                            jump aeli_about_healedplague06
                                            '“Not really.”' if pc_religion == "unknown" or pc_religion == "none" or pc_religion == "pagan":
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really.”')
                                                menu:
                                                    'They have the accent of {color=#f6d6bd}Hovlavan{/color} elders, but their lips are struggling to utter any sound. “It’s from Wright’s Tablets. They are the source of our knowledge, and what allowed us to build villages taller than trees. We study these stories every day, to shape The Land into what it ought to be.”
                                                    \n\nThey cock their head to the side, their chin is shaking. “I just recited a part of the {i}The Tribe of Leaves{/i}. The Tribe started as foragers and fruit pickers, too afraid to hunt, with no faith to guide them outside of their cave. But The Wright inspired them with The Truth of what they were and of what they could become. They helped Adir build one of The Ten Cities, and their blood and memory now remains in each of us.”
                                                    \n\n“I’m exhausted,” their breathing remains silent, but their chest starts to rise and fall, “but I wanted thee to see this place.”
                                                    '
                                                    '“So I’m seeing it. What is this place, exactly?”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I’m seeing it. What is this place, exactly?”')
                                                        jump aeli_about_healedplague06

    label aeli_about_healedplague06:
        if pc_religion == "pagan":
            $ custom1 = "You flinch. It’s not the first time you hear about Wright’s servants willing to destroy the relics left behind by the ancestors. "
        else:
            $ custom1 = ""
        $ monastery_name = "The Library in Stone"
        if not aeli_about_monasteryname:
            $ aeli_about_monasteryname = 1
            $ aeli_about_monastery += 1
        $ quest_explorepeninsula_description13 = "{color=#f6d6bd}The monastery{/color} hides a tremendous cave with walls covered by copies of Wright’s Tablets. It may be of huge importance to the religious leaders in {color=#f6d6bd}Hovlavan{/color}."
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        menu:
            '“One day, these walls will hold all of Wright’s Tablets. Maybe in five years, maybe in twenty five. These ancient caves used to be covered by painted hands and beasts, but we scraped the walls clean, giving way to The Truth.” [custom1]{color=#f6d6bd}The prelate{/color} raises their hands by an inch, but their voice remains monotonous. “The work went slowly and we abandoned our goal, but then the war tore The Ten Cities to pieces.”
            \n\nThey’re wheezing, fighting for air. “It made us realize how... {i}crucial{/i} our duty is. The parchment will burn, the wood covers will rot, the golden plates will be stolen. But these caves lasted for more generations than we can count. They will outlast every page, every teacher,” they raise their voice. “{color=#f6d6bd}The Library in Stone{/color}, will be here, ready to teach our offspring. The final stronghold of The Truth. As long as there’s one soul who can read the Adir’s tongue, there will be hope.”
            \n\nA long pause. {color=#f6d6bd}Aeli{/color} looks at you expectantly, rubbing his hands together. {color=#f6d6bd}Decima{/color} stares at you like an eagle.
            '
            '“So, why am I here? What do you expect me to do?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, why am I here? What do you expect me to do?”')
                $ renpy.save("combatsave", extra_info='Combat Auto Save')
                menu:
                    '“One of us... came here from the city, five years ago, and told us... many things... about her home. Thy city lacks grain, and wood, and parchment. The Unites... grow poor.” They raise their hand to wipe saliva from their mouth, taking longer and longer pauses.
                    \n\n“Thou art not here to ward the roads... but to prepare it for thy masters. They will bring death and pillage.” They stretch out their hand, palm up. “Tell them about {color=#f6d6bd}The Library{/color}. That it needs their protection. That once we’ll complete it, we’ll give it away, just... Just let {color=#f6d6bd}Old Págos{/color} be in peace.”
                    \n\nTheir hand lands on their stomach, their chin rests on their chest. They are gasping for air. “Protect... this place.”
                    '
                    '“Fine. I’ll pass along your message.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll pass along your message.”')
                        $ custom1 = ""
                        if pc_religion == "pagan":
                            $ pc_faithpoints_opportunities += 1
                            $ pc_faithpoints -= 2
                        $ quest_monasterysupport_description01 = "I spoke with {color=#f6d6bd}the prelate{/color} and promised them to portray the monastery’s goals and zeal in front of the officials."
                        jump aeli_about_healedplague08yes
                    '{image=d6} (lie) “I’ll do everything I can.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} (lie) “I’ll do everything I can.”')
                        jump aeli_about_healedplague08lie
                    '“I don’t care about any of that. Unless you show me your generosity, I refuse.”' if pc_religion != "pagan":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t care about any of that. Unless you show me your generosity, I refuse.”')
                        jump aeli_about_healedplague08no
                    '“You ruined the legacy of the ancient tribes. You deserve no sympathy.”' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You ruined the legacy of the ancient tribes. You deserve no sympathy.”')
                        jump aeli_about_healedplague08nopagan

    label aeli_about_healedplague08lie:
        if (pc_lies+monastery_friendship-monastery_lies_decima) >= 14:
            $ pc_lies += 2
            $ orentius_arguments += 1
            $ custom1 = "You hear {color=#f6d6bd}Decima’s{/color} steps. She stares into your eyes, then moves back with a puzzled frown. "
            $ quest_monasterysupport_description01lie = "I spoke with {color=#f6d6bd}the prelate{/color} and lied to them about portraying the monastery’s goals and zeal in front of the officials."
            jump aeli_about_healedplague08yes
        elif monastery_lies_decima >= 2:
            menu:
                '“Lies,” you hear the girl’s voice, sharp like a dagger. {color=#f6d6bd}The prelate{/color} tries to raise their head. “Are you sure, {color=#f6d6bd}Decima{/color}?”
                \n\n“She’s always sure,” {color=#f6d6bd}Aeli{/color} puts his hand on your shoulder. It’s heavy.
                \n\n“Liar, lied now, lied before, I saw it.” {color=#f6d6bd}The young monk’s{/color} rage almost makes her choke.
                \n\nThe chamber falls quiet until {color=#f6d6bd}the prelate{/color} lets out a single, disappointed command. “Kill.”
                '
                '“Wait...”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wait...”')
                    $ pc_hp = 0
                    show minus5hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                    if pc_religion == "pagan":
                        show areapicture gameover_alt at basicfade
                    else:
                        show areapicture gameover at basicfade
                    menu:
                        'The girl’s dagger gets between your ribs. You reach out for your axe, torn with pain, but the man takes you two steps closer to the edge of the platform, then pushes you with an angry grunt.
                        \n\nYou’re falling down, into the grasp of the cold wind. The letters on the walls blur with each other. You look into the gray abyss, seeking anything you could grasp, or maybe cut with your blade...
                        \n\nWhen you hit the streambed, you don’t feel a thing.
                        \n
                        \n\n[pcname]’s soul has left its shell.
                        '
                        'Let me replay this choice.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this choice.')
                            stop music fadeout 4.0
                            $ renpy.load("combatsave")
        else:
            $ monastery_lies_decima += 2
            $ monastery_friendship -= 5
            $ pc_lies += 1
            $ quest_monasterysupport_description03 = "{color=#f6d6bd}The prelate{/color} has seen through my lies. It’s possible I separated the monastery from the city for good."
            $ quest_monasterysupport = 3
            $ renpy.notify("Quest completed: The Support of Monks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Monks{/i}')
            $ monastery_cave_firsttime = 1
            menu:
                '“Lies,” you hear the girl’s voice, sharp like a dagger. {color=#f6d6bd}The prelate{/color} tries to raise their head. “Are you sure, {color=#f6d6bd}Decima{/color}?”
                \n\n“She’s always sure,” {color=#f6d6bd}Aeli{/color} puts his hand on your shoulder. It’s heavy.
                \n\nThe chamber falls quiet until {color=#f6d6bd}the prelate{/color} lets out a single, disappointed command. “Leave.”
                \n\n{color=#f6d6bd}Aeli{/color} pulls you away, moving dangerously close to the edge of the platform.
                '
                '“Get your hands off me.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Get your hands off me.”')
                    show areapicture monastery01gateopen at basicfade
                    $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                    play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    $ quarters += 1
                    menu:
                        'He pushes you forward as if you’re a prisoner, but says nothing more. You move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                        \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug. He then returns to you.
                        \n\n“It’s time for thee to go.”
                        '
                        'I ride to the village.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride to the village.')
                            $ travel_destination = "oldpagos"
                            jump finaldestinationafterevent
                'I walk in silence.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk in silence.')
                    show areapicture monastery01gateopen at basicfade
                    $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                    play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    $ quarters += 1
                    menu:
                        'He lets go of you after a few steps, nodding at the stairs. You climb up on all fours.
                        \n\nYou move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                        \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug. He then returns to you.
                        \n\n“It’s time for thee to go.”
                        '
                        'I ride to the village.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride to the village.')
                            $ travel_destination = "oldpagos"
                            jump finaldestinationafterevent

    label aeli_about_healedplague08yes:
        $ monastery_friendship += 5
        $ monastery_promise = 1
        $ quest_monasterysupport = 2
        $ renpy.notify("Quest completed: The Support of Monks")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Monks{/i}')
        $ monastery_cave_firsttime = 1
        menu:
            '[custom1]{color=#f6d6bd}The prelate{/color} nods gently, resting. {color=#f6d6bd}Aeli{/color} clears his throat. “I thank thee in their name. Let’s get back while the ointment is still working.” He gestures for you to follow him, but seeing the world only in grays takes getting used to. You place steps carefully, and climb the stairs on all fours.
            \n\n{color=#f6d6bd}The monk{/color} continues. “Thou canst ask me about one of our secrets, as a reward. But dost not share what thou hast learned here with any of the tribes. We ought to keep our duty a secret.”
            '
            '“A secret. Fine.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A secret. Fine.”')
                show areapicture monastery01gateopen at basicfade
                $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                $ questionpreset = "monastery1"
                $ quarters += 1
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if pc_goal == "iwantstatus":
                    $ pc_goal_iwantstatuspoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                menu:
                    'You move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                    \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug.
                    \n\nFinally, he meets your eyes and puts on a gentle smile.
                    '
                    '(monastery1 preset)':
                        pass
            '“I’d prefer some of this ointment.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d prefer some of this ointment.”')
                if pc_goal == "iwantstatus":
                    $ pc_goal_iwantstatuspoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                if not galerocks_fulvia_secret_knowsabout:
                    show areapicture monastery01gateopen at basicfade
                    $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                    play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    $ quarters += 1
                    $ questionpreset = "monastery1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        '“Won’t happen,” he doesn’t let you finish. “Use it a few times and thy eyes will see only in gray, and after twenty years or so thou wilt lose thy sight completely. Just use a lantern.”
                        \n\nYou move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                        \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug.
                        \n\nFinally, he meets your eyes and puts on a gentle smile.
                        '
                        '(monastery1 preset)':
                            pass
                else:
                    menu:
                        '“Won’t happen,” he doesn’t let you finish. “Use it a few times and thy eyes will see only in gray, and after twenty years or so thou wilt lose thy sight completely. Just use a lantern.”
                        '
                        '“Is this what happened to {color=#f6d6bd}Fulvia{/color} from {color=#f6d6bd}Gale Rocks{/color}?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is this what happened to {color=#f6d6bd}Fulvia{/color} from {color=#f6d6bd}Gale Rocks{/color}?”')
                            $ aeli_about_fulvia = 1
                            show areapicture monastery01gateopen at basicfade
                            $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                            play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                            $ quarters += 1
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            $ monastery_friendship += 1
                            menu:
                                'He nods gently, looking at you with new respect.
                                \n\nYou move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                                \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug.
                                \n\nFinally, he meets your eyes and puts on a gentle smile.
                                '
                                '(monastery1 preset)':
                                    pass

    label aeli_about_healedplague08no:
        $ monastery_friendship -= 2
        $ quest_monasterysupport_description02 = "I refused to help the monks, possibly separating them from the city officials for good."
        $ quest_monasterysupport = 3
        $ renpy.notify("Quest completed: The Support of Monks")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Monks{/i}')
        $ monastery_cave_firsttime = 1
        menu:
            '{color=#f6d6bd}The prelate{/color} sits without a word, gasping for air. {color=#f6d6bd}Aeli{/color} coughs. “Come, before the ointment stops working.”
            \n\nSeeing the world only in grays takes getting used to. You place steps carefully, and climb the stairs on all fours. {color=#f6d6bd}The monk{/color} continues. “Dost not share what thou hast learned here with any of the tribes. We ought to keep our duty a secret.”
            '
            '“We’ll see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see.”')
                show areapicture monastery01gateopen at basicfade
                $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                $ questionpreset = "monastery1"
                $ quarters += 1
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} lets you grab his shoulder again.
                    \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug.
                    \n\nYou stand in an awkward silence.
                    '
                    '(monastery1 preset)':
                        pass

    label aeli_about_healedplague08nopagan:
        if pc_religion == "pagan":
            $ pc_faithpoints_opportunities += 1
            $ pc_faithpoints += 2
        $ monastery_friendship -= 5
        $ quest_monasterysupport_description02 = "I refused to help the monks, possibly separating them from the city officials for good, but honoring the memory of my ancestors."
        $ quest_monasterysupport = 3
        $ renpy.notify("Quest completed: The Support of Monks")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Monks{/i}')
        $ monastery_cave_firsttime = 1
        menu:
            '{color=#f6d6bd}The prelate{/color} sits without a word, gasping for air. {color=#f6d6bd}Aeli{/color} coughs. “Come, and now.” Seeing the world only in grays takes getting used to. You place steps carefully, and climb the stairs on all fours.
            \n\n{color=#f6d6bd}The monk{/color} continues. “Dost not share what thou hast learned here with any of the tribes. We ought to keep our duty a secret.”
            '
            '“We’ll see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see.”')
                show areapicture monastery01gateopen at basicfade
                $ renpy.music.play("audio/track_08monastery.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
                play nature "audio/ambient/monastery01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                menu:
                    'You move without a word, leaving behind the sounds of steps, hammers, and the stream. Your eyes lose their sharpness slowly, but also restore their ability to perceive colors. Before you reach the mouth of the cavern, {color=#f6d6bd}Aeli{/color} grabs your shoulder and pushes you toward the exit.
                    \n\nAfter getting outside, you take a couple of deep breaths. {color=#f6d6bd}The monk{/color} absently heads toward the storehouse, waiting for {color=#f6d6bd}Decima{/color} to join him. When asked about {color=#f6d6bd}the prelate’s{/color} sleep, she spares {color=#f6d6bd}her companion{/color} a sad shrug. He then returns to you.
                    \n\n“It’s time for thee to go.”
                    '
                    'I ride to the village.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride to the village.')
                        $ travel_destination = "oldpagos"
                        jump finaldestinationafterevent

label aeli_about_iwantnewlifeALL:
    label aeli_about_iwantnewlife01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Now that I’ve been inside the {i}library{/i}, I give the monastery another look.')
        $ pc_goal_iwantnewlife_monastery_about = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 5
        menu:
            'The butterflies try to collect the last shards of food from the overblown summer flowers, while the herbs and lettuce are getting picked by the younger monks, piled up on a small cart. Telling from their conversation, some of those plants are going to end up as pickles.
            \n\nYou turn around, once again noticing the constant roar of the river, in the valley deep down. You’ve managed to learn how to ignore it, but now, as you’re paying closer attention, you hear the sounds of the Order and their land. The chisels echoing in the caves, the singing of a woman looking after the fruit trees, and the cough of an elder who’s been watching you from the edge of one of the paths, close to the massive, steel hourglass.
            \n\nThere may be no walls around, but no one seems worried, or afraid. Even {color=#f6d6bd}Decima{/color}, like always both vigilant and absent, is focused on the picture of an eagle that she’s been drawing with her small boot.
            '
            'One could find peace here. For the price of freedom.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '{color=#f6d6bd}Aeli{/color} gives you a curious glance, as if he’s been reading your thoughts.
                    '
                    '“Once I’m done with my {i}duty{/i} in the city, I’d like to abandon my old life. Would your order take me?”' if pc_religion != "pagan":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Once I’m done with my {i}duty{/i} in the city, I’d like to abandon my old life. Would your order take me?”')
                        $ pc_goal_iwantnewlife_monastery_about2 = 1
                        menu:
                            'He clasps his hands together and steps toward you, staring in your eyes, then sighs and puts his arm around your shoulders. He smells of humid wood, his grasp is firm.
                            \n\n“Thou hast seen our lives and knowest they’re far from gentle, so I trust thy question is honest. But {i}what {/i} makes thee ask?”
                            '
                            '“I need to hide before my past catches up with me.”' if pc_goal == "iwanttostartanewlife":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to hide before my past catches up with me.”')
                                $ custom1 = "“There are more such souls here,” he responds slowly. “Thou mayest hide from the consequences, but not from guilt, or shame, or responsibility. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I’ve got a sibling who may need to come here with me. Hide from our problems.”' if pc_goal == "ineedmoney":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got a sibling who may need to come here with me. Hide from our problems.”')
                                $ custom1 = "“There are more such souls here,” he responds slowly. “Thou mayest hide from the consequences, but not from guilt, or shame, or responsibility. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I’ve been following coins, but... I’m not sure I’d ever have enough to leave my worries behind.”' if pc_goal == "iwantmoney":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='-“I’ve been following coins, but... I’m not sure I’d ever have enough to leave my worries behind.”')
                                $ custom1 = "“A human would sooner eat their own heart than satisfy their hunger,” he responds with a smirk, “yet monks live the lives of hardship, and have got new duties to fulfill. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I’ve been dreaming of greatness, but this land doesn’t look like it really wants a {i}hero{/i}.”' if pc_goal == "iwanttoberemembered":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been dreaming of greatness, but this land doesn’t look like it really wants a {i}hero{/i}.”')
                                $ custom1 = "He chuckles. “The blank walls and prayer are a better mirror than the calmest pond, but art thee sure thou couldst endure it?”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I wanted to help people, but now I’m feeling sort of... defeated.”' if pc_goal == "iwanttohelp":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wanted to help people, but now I’m feeling sort of... defeated.”')
                                $ custom1 = "“Usually, acolytes run away from guilt and shame, not from craving for good,” he responds slowly. “Thou mayest hide from thy ambition, but not from missed opportunities. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I wanted to become {i}someone{/i} in the city, but I’m not sure I want to deal with the choices and sacrifices such power takes.”' if pc_goal == "iwantstatus":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wanted to become {i}someone{/i} in the city, but I’m not sure I want to deal with the choices and sacrifices such power takes.”')
                                $ custom1 = "“There are more such souls here,” he responds slowly. “Thou mayest hide from the consequences, but not from guilt, or shame, or responsibility. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I lack purpose. I’m lost.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I lack purpose. I’m lost.”')
                                $ custom1 = "He chuckles. “The blank walls and prayer are better at bringing questions, then answers. I can’t promise thee a new destination, but we may be open to give thee a chance.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“I’m done with the troubles of this world. I need to rest.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m done with the troubles of this world. I need to rest.”')
                                $ custom1 = "“Yet monks live the lives of hardship,” his voice is gentle, yet lecturing. “Thou mayest flee from choices and responsibilities, but we’ve got new duties to fulfill. We can leave The Land behind, but our feet still touch it.”\n\n"
                                jump aeli_about_iwantnewlife01a
                            '“The Wright calls me to serve them.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The Wright calls me to serve them.”')
                                $ custom1 = "He grunts. “Prideful words, if honest. Not ones we could verify.” "
                                jump aeli_about_iwantnewlife01a
                    'They would never let a {i}pagan{/i} seek shelter in here. (disabled)' if pc_religion == "pagan":
                        pass
                    'I chuckle. This life isn’t for me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I chuckle. This life isn’t for me.')
                        $ questionpreset = "monastery1"
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        menu:
                            'The silence goes on.
                            '
                            '(monastery1 preset)':
                                pass
            'Maybe the Seekers were not hunting down my ancestors, but they didn’t protect them either.' if pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the Seekers were not hunting down my ancestors, but they didn’t protect them either.')
                $ pc_goal_iwantnewlife_monastery_discarded = 1
                $ pc_faithpoints += 1
                $ pc_faithpoints_opportunities += 1
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You take a deep breath, trying to extinguish the anger growing in you, then notice the piercing look of the young assistant. You force yourself to not frown back at her.
                    '
                    '(monastery1 preset)':
                        pass
            'This is yet another cage.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is yet another cage.')
                $ pc_goal_iwantnewlife_monastery_discarded = 1
                $ questionpreset = "monastery1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'Now that you think about it, all these noises, and especially the wind, start to annoy you.
                    '
                    '(monastery1 preset)':
                        pass

    label aeli_about_iwantnewlife01a:
        menu:
            '[custom1]He turns you around, making you face {color=#f6d6bd}Decima{/color}, who has just been drawing a winged hourglass in the sand with her boot. “We need to judge thy honesty. Let her read you.”
            '
            '“Let her {i}what{/i}?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let her {i}what{/i}?”')
                menu:
                    '“Don’t worry, it doesn’t hurt,” {color=#f6d6bd}the monk{/color} chuckles and shoves you to the ground, making you land on your knees. {color=#f6d6bd}His companion’s{/color} eyes can now meet yours without looking up, and she cups her hands around your ears.
                    \n\nIt doesn’t last long, but it feels as if there’s something crawling beneath your skin.
                    '
                    'I try not to look away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try not to look away.')
                        if pc_religion == "none":
                            $ pc_goal_iwantnewlife_monastery_rejected = 1
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her grimace of disgust grows with every breath, until she pinches your ear and leaps away, letting out a loud snort.
                                \n\n“Not ready?” {color=#f6d6bd}Aeli’s{/color} tone is playful, but he straightens up after {color=#f6d6bd}Decima{/color} shakes her head, waving her ponytail. “Empty, dry.”
                                \n\n“Too bad,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We’ve got no robes for thy shell, warden.”
                                '
                                '(monastery1 preset)':
                                    pass
                        elif pc_religion == "unknown":
                            $ pc_goal_iwantnewlife_monastery_rejected = 1
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her grimace of disgust grows with every breath, until she pinches your ear and leaps away, letting out a loud snort.
                                \n\n“Not ready?” {color=#f6d6bd}Aeli’s{/color} tone is playful, but he straightens up after {color=#f6d6bd}Decima{/color} shakes her head, waving her ponytail. “Empty, on the fence.”
                                \n\n“Too bad,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We’ve got no robes for thy shell, warden.”
                                '
                                '(monastery1 preset)':
                                    pass
                        elif description_druids10 and pc_religion == "theunitedchurch":
                            $ pc_goal_iwantnewlife_monastery_rejected = 1
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her grimace of disgust grows with every breath, until she spits in your face and leaps away, letting out a loud snort.
                                \n\n“What is it?” {color=#f6d6bd}Aeli{/color} straightens up, while {color=#f6d6bd}Decima{/color} shakes her head, waving her ponytail. “Empty, bleeding. Traitor.”
                                \n\n“I see,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We can’t hand a rope to a shell that may turn its back on us, warden.”
                                '
                                '(monastery1 preset)':
                                    pass
                        elif pc_faithpoints_opportunities < 8:
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her stare gets more puzzled with every breath, until she steps away and raises her chin.
                                \n\n“Not ready?” {color=#f6d6bd}Aeli’s{/color} tone is playful, and {color=#f6d6bd}Decima{/color} cocks her head to the side, selecting words carefully. “Not tested. Could go either way.”
                                \n\n“Could be worse,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We only let in souls of great conviction. Come back after you prove in front of thyself that thou art one.”
                                '
                                '(monastery1 preset)':
                                    pass
                        elif pc_faithpoints < (pc_faithpoints_opportunities*0.25):
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her grimace of disgust grows with every breath, until she pinches your ear and leaps away, letting out a loud snort.
                                \n\n“Not ready?” {color=#f6d6bd}Aeli’s{/color} tone is playful, and {color=#f6d6bd}Decima{/color} makes a dignified nod. “Not empty, but still on the fence. Weak.”
                                \n\n“Could be worse,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We only let in souls of great conviction. Come back after you squash your doubt.”
                                '
                                '(monastery1 preset)':
                                    pass
                        elif pc_faithpoints < (pc_faithpoints_opportunities*0.75):
                            $ questionpreset = "monastery1"
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'Her frown gets sharper with every breath, until she steps away and raises her chin.
                                \n\n“Not ready?” {color=#f6d6bd}Aeli’s{/color} tone is playful, and {color=#f6d6bd}Decima{/color} makes a dignified nod. “Not empty, but still on the fence.”
                                \n\n“Could be worse,” {color=#f6d6bd}the monk{/color} invites you to stand up with a gesture. “We only let in souls of great conviction. Come back after you squash your doubt.”
                                '
                                '(monastery1 preset)':
                                    pass
                        else:
                            label aeli_about_iwantnewlife02:
                                $ questionpreset = "monastery1"
                                $ can_leave = 1
                                $ can_rest = 1
                                $ can_items = 1
                                $ pc_goal_iwantnewlife_monastery = 1
                                if pc_goal == "iwanttostartanewlife":
                                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
                                menu:
                                    'A few breaths go by and she leans closer to you. Her stare is relentless, even as your foreheads touch each other. Finally, she steps away, giving {color=#f6d6bd}her companion{/color} a wide grin.
                                    \n\n{color=#f6d6bd}Aeli{/color} sighs with relief. “Good, good. Now, [pcname]. Get back to thy life, but if thou wilt remain sure in your request, there’s a cave for thee. Don’t bring any wealth or keepsakes. Whatever River of Faith thou followest,” he points at the massive hourglass, “here thou wilt learn The Truth.”
                                    '
                                    '(monastery1 preset)':
                                        pass

    label aeli_about_iwantnewlife01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Decima{/color}. “I am of strong faith. Read me.”')
        $ pc_goal_iwantnewlife_monastery_about = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You get on your knees, allowing {color=#f6d6bd}the monk{/color} to cup her hands around your ears.
            '
            'I challenge her with my own gaze.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I challenge her with my own gaze.')
                jump aeli_about_iwantnewlife02
            'I smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile.')
                jump aeli_about_iwantnewlife02

label aeli_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Erastos{/color}?”')
    $ quest_recruitahunter_spokento_aeli = 1
    $ quest_recruitahunter_erastos_points += 1
    if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_erastos_points_notify2:
        $ quest_recruitahunter_erastos_points_notify2 = 1
        $ quest_recruitahunter_erastos_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    elif quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_erastos_points_notify1:
        $ quest_recruitahunter_erastos_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    $ questionpreset = "monastery1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ minutes += 2
    menu:
        '“I can a lot, but should naught. He’s a troubled soul.” You ask a few more questions, unable to shatter his patience, and the monk thinks about his words carefully. “He saw us as alchemists, not Wright’s followers. His heart craves someone it can’t have, and he begged us for a remedy. But there’s no potion that can cut such ties, only time.”
        \n\nWhen you mention {color=#f6d6bd}Erastos{/color} sounds like a determined young man, {color=#f6d6bd}Aeli{/color} scoffs. “More like a child who thinks the day they’re touching is the only one that will ever come.”
        '
        '(monastery1 preset)':
            pass
