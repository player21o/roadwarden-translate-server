###################### Druid's Cave / Druid Cave
default druidcave_firsttime = 0
default druidcave_firsttime_counter = 0 # day
default druidcave_deer_secondtime = 0
default druidcave_banned = 0
default druidcave_fluff = ""
default druidcave_fluff_old = 0
default druidcave_druid_fluff = ""
default druidcave_druid_fluff_old = 0
default druidcave_druid_inside_fluff = ""

default druidcave_cave_open = 0
default druidcave_cave_open_gray = 0
default druidcave_cave_corridor = 0
default druidcave_cave_alchemy = 0
default druidcave_cave_alchemy_used = 0

default druidcave_druid_friendship = 0
default druidcave_druid_hourglass = 0
default druidcave_druid_forestspeaker = 0 # Forest Speaker
default druidcave_druid_healing = 0

default druidcave_druid_about_asterion1 = 0
default druidcave_druid_about_asterion2 = 0
default druidcave_druid_about_peninsula = 0
default druidcave_druid_about_bandits1 = 0
default druidcave_druid_about_greenmountaintribe1 = 0
default druidcave_druid_about_greenmountaintribe1_gray = 0
default druidcave_druid_about_cave = 0
default druidcave_druid_about_altar = 0
default druidcave_druid_about_job = 0
default druidcave_druid_about_job_gray = 0
default druidcave_druid_about_druids1 = 0
default druidcave_druid_about_druids1_gray = 0
default druidcave_druid_about_solitude = 0
default druidcave_druid_about_herbs = 0
default druidcave_druid_about_reputation = 0
default druidcave_druid_about_beholder_cutroot = 0
default druidcave_druid_about_robes = 0
default druidcave_druid_about_sleepinggiant_gray = 0
default druidcave_druid_about_shortcut = 0
default druidcave_druid_about_spiritrock = 0
default druidcave_druid_about_weather = 0
default druidcave_druid_about_thyrsus = 0
default druidcave_druid_about_nomoreundead = 0
default druidcave_druid_about_missinghunters = 0

default druidcave_druid_about_ruins1 = 0
default druidcave_druid_about_ruins1_gray = 0
default druidcave_druid_about_ruins_ver01 = 0
default druidcave_druid_about_ruins_ver02 = 0
default druidcave_druid_about_ruins_ver03 = 0
default druidcave_druid_about_ruins_ver04 = 0
default druidcave_druid_about_ruins_ver05 = 0

default druidcave_druid_about_plague01 = 0
default druidcave_druid_about_plague01a = 0
default druidcave_druid_about_plague01b = 0
default druidcave_druid_about_plague01c = 0
default druidcave_druid_about_plague01d = 0
default druidcave_druid_about_plague01f = 0
default druidcave_druid_about_plague01g = 0
default druidcave_druid_about_plague01h = 0
default druidcave_druid_about_plague01i = 0
default druidcave_druid_about_plague01j = 0
default druidcave_druid_about_plague01k = 0
default druidcave_druid_about_plague02 = 0
default druidcave_druid_about_plague_pcwillcure = 0
default druidcave_druid_about_plague_travel = 0

default druidcave_druid_about_highisland = 0
default druidcave_druid_about_highisland_friendship = 10
default druidcave_druid_about_highisland_gray = 0
default druidcave_druid_about_highisland_elpis = 0

default druidcave_about_thyrsusgift_druidcomment = 0
default druidcave_about_elpis_about_thyrsusgift2 = 0

label druidcave01:
    if not druidcave_firsttime:
        stop music fadeout 4.0
        play nature "audio/ambient/druidcave01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    else:
        stop nature fadeout 4.0
        $ renpy.music.play("audio/track_10druidcave.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    if druidcave_druid_about_herbs == 2:
        show areapicture druidcave01alt02 at basicfade behind druidcavebronzerod
    else:
        show areapicture druidcave01 at basicfade behind druidcavebronzerod
    if eudocia_bronzerod_rodin_druidcave:
        show druidcavebronzerod at basicfade
    $ druidcave_druid_inside_fluff = ""
    $ druidcave_druid_inside_fluff = renpy.random.choice(['The woman is moving in her sleep.', 'The woman is sitting next to her bed, swaying back and forth.', 'The woman is crouching next to her bed, sobbing, covering her face with a cloth.', 'The woman is sitting next to the flooded corridor, with her legs in water, humming rhythmless melody.'])
    label druidcave_fluffloop:
        $ druidcave_fluff = renpy.random.choice(['A shiny empress carp, with orange and golden scales, swims near the shore, hoping to get some tasty scraps of bread.', 'Two blue-tailed monkeys are jumping on the rocky mountainside, chasing each other and screaming cheerfully.', 'A trail of black ants is crossing the road, carrying leaves, dried blades of grass, and little sticks.', 'A flock of colorful birds is circling in the sky.', 'You hear the chilling roar of a dragon from the mountains. At least there’s no avalanche.', 'Two ibexes, a male and a female, are lying on the rocky mountainside. A gentle wind is brushing their fur.'])
        if quest_empresscarp != 2 and druidcave_fluff == "A shiny empress carp, with orange and golden scales, swims near the shore, hoping to get some tasty scraps of bread.":
            jump druidcave_fluffloop
        elif druidcave_fluff_old == druidcave_fluff:
            jump druidcave_fluffloop
        else:
            $ druidcave_fluff_old = druidcave_fluff
    label druidcave_druid_fluffloop:
        $ druidcave_druid_fluff = renpy.random.choice(['{color=#f6d6bd}The old man{/color} shuts the door with a resonant thud.', '{color=#f6d6bd}The old man{/color} is resting on the bench. He welcomes you with a resigned sigh.', '{color=#f6d6bd}The old man{/color} is sitting on a wooden stool between the garden beds, weeding. The torn plants are resting in a small basket.', '{color=#f6d6bd}The druid{/color} is sitting on the shore, keeping his legs in the water and observing the spring. His gaze is a bit absent, and he notices you only after you tap his shoulder.', 'For a moment, you see not only {color=#f6d6bd}the old druid{/color}, but also his female companion. Touched by years, she’s leaning forward. As you arrive, she hides inside the cave. The man welcomes you with an annoyed “What?”', '{color=#f6d6bd}The old man{/color} is grinding something in a bowl placed on a table-like rock, next to the closed entrance.'])
        if druidcave_druid_fluff_old == druidcave_druid_fluff:
            jump druidcave_druid_fluffloop
        else:
            $ druidcave_druid_fluff_old = druidcave_druid_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ pc_area = "druidcave"
    if item_wingedhourglass_worn:
        $ druidcave_druid_hourglass = 1
    if not druidcave_firsttime:
        $ druidcave_firsttime = 1
        $ druidcave_firsttime_counter = day
        $ world_known_areas += 1
        $ world_known_npcs += 1
        $ beholder_unlocked = 1
        jump druidcavefirsttime01
    elif druidcave_druid_about_plague_travel:
        jump druidcavereturningfromoldpagos01
    else:
        jump druidcaveregular01

label druidcaveregular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if whitemarshes_nomoreundead and not druidcave_druid_about_nomoreundead:
        $ druidcave_druid_about_nomoreundead = 1
        if orentius_convinced:
            $ questionpreset = "druidcave1"
            $ druidcave_druid_friendship += 2
            $ minutes += 5
            menu:
                '{color=#f6d6bd}The old druid{/color} is at the edge of the pond, staring at the distance, and after you get on the ground, he gives you a hesitant glance. “Many beasts are heading for the bogs,” he says cautiously. “{color=#f6d6bd}The necromancer’s{/color} spells are nae more?”
                \n\nYou try to figure out how he knows it, but he doesn’t show you much patience. “Explain.”
                \n\nYour tale is brief, and the man doesn’t delve into details. “You took a swing at the cause, ne the symptom.” He strokes his beard, then smiles gently. “We can only wait to see if your cure will work for long,” his voice is as warm as a soft blanket, “but you acted like a healer, ne a pillager.”
                '
                '(druidcave1 set)':
                    pass
        elif orentius_banished:
            $ questionpreset = "druidcave1"
            $ druidcave_druid_friendship += 0
            $ minutes += 5
            menu:
                '{color=#f6d6bd}The old druid{/color} is at the edge of the pond, staring at the distance, and after you get on the ground, he gives you a hesitant glance. “Many beasts are heading for the bogs,” he says cautiously. “{color=#f6d6bd}The necromancer’s{/color} spells are nae more?”
                \n\nYou try to figure out how he knows it, but he doesn’t show you much patience. “Explain.”
                \n\nYour tale is brief, and the man doesn’t delve into details. “You aligned with beasts to fell a monster, you set the village free, but left it nae foundation.” He strokes his beard, speaking mostly to himself. “We’ll hold our breaths, en wait to see what happens.”
                '
                '(druidcave1 set)':
                    pass
        elif whitemarshes_destroyed:
            $ questionpreset = "druidcave1"
            $ druidcave_druid_friendship -= 2
            menu:
                '{color=#f6d6bd}The old druid{/color} is at the edge of the pond, staring at the distance, and after you get on the ground, he gives you a resentful glance. There are red circles around his sky-blue eyes. “An entire tribe, gone,” he almost whispers, then clears his throat.
                '
                '(druidcave1 set)':
                    pass
    elif beholder_cutroot and beholder_cutroot < day and not druidcave_druid_about_beholder_cutroot:
        $ druidcave_druid_friendship -= 1
        $ druidcave_druid_about_beholder_cutroot = 1
        $ beholder_name_known = 1
        $ minutes += 5
        $ questionpreset = "druidcave1"
        menu:
            '[druidcave_fluff] {color=#f6d6bd}The old druid{/color} is standing upright, giving you a harsh look. “You cut off the root of Beholder,” he says without hesitation. “It did ne belong to you.”
            \n\nBefore you respond, he turns away and washes his hands in the spring. It takes him a few minutes to look at your lips.
            '
            '(druidcave1 set)':
                pass
    elif howlersdell_reputation > 5 and not druidcave_druid_about_reputation:
        $ druidcave_druid_friendship += 1
        $ druidcave_druid_about_reputation = 1
        $ questionpreset = 0
        menu:
            '[druidcave_fluff] {color=#f6d6bd}The old druid{/color} is resting on the bench, and welcomes you with a new interest in his voice. “Words of the help you’ve shown to my neighbors from {color=#f6d6bd}Howler’s Dell{/color} have reached me, traveler. Good, very good.”
            '
            '“I’m always ready to do the right thing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m always ready to do the right thing.”')
                $ questionpreset = "druidcave1"
                menu:
                    'He vaguely grunts.
                    '
                    '(druidcave1 set)':
                        pass
            '“Has one of those critters of yours brought you the news?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Has one of those critters of yours brought you the news?”')
                $ questionpreset = "druidcave1"
                menu:
                    '“Moronic. Animals do ne speak, ne even the largest beast.” You see a playful spark in his eye.
                    '
                    '(druidcave1 set)':
                        pass
    else:
        $ questionpreset = "druidcave1"
        menu:
            '[druidcave_fluff] [druidcave_druid_fluff] “What do you need, traveler?”
            '
            '(druidcave1 set)':
                pass

label druidcavefirsttime01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if persistent.deafmode:
        $ deafcustom1 = "The humming of a spring is hidden beneath the piercing shouts of birds that circle above the pond, seeking insects to feast upon."
    else:
        $ deafcustom1 = ""
    menu:
        'You’ve reached {color=#f6d6bd}Hag Hills{/color}, the wall of stones that has blocked the city’s grasp. The one well-established route through them leads through the valley where you found {color=#f6d6bd}Tulia’s camp{/color}. There are no maps of the highlands, nor local tribes, only stories.
        \n\nThe beaten path leads you by the garden beds of herbs and vegetables, to an old, yet not abandoned, mine, hidden behind a massive door made of steel. [deafcustom1]
        '
        'I look around. There’s no hitching rail for a mount.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around. There’s no hitching rail for a mount.')
            $ at_activate = 1
            $ at = 0
            menu:
                '{color=#f6d6bd}A bearded, skinny elder{/color} sits still on a bench, observing you like a sculpture, with his legs crossed and fingers interlocked on his abdomen.
                '
                ' (disabled)' ( condition="at == 0" ):
                    pass
                '“Good day to you. Don’t worry about my horse, I’ll keep it away from your garden.”' ( condition="at == 'friendly'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) “Good day to you. Don’t worry about my horse, I’ll keep it away from your garden.”')
                    $ at_activate = 0
                    $ at = 0
                    if pc_class == "scholar" and pc_religion != "pagan":
                        $ at_unlock_knowledge = 1
                    menu:
                        '“Only worms, too stupid to understand me, would eat what’s mine.” You dismount and mention that your palfrey is no worm, but the man reprimands you with a thick accent. “Let me see you whilst you speak, I can ne hear without magic, but I’ll read your lips.”
                        \n\nHe doesn’t yell, but his voice reminds you of a combat instructor from the city. His face is wrinkled, but he sits straight, with beard and hair still carrying glimpses of fair blonde. He’s tanned like a worker and his eyes are blue and piercing, as if they belong to an infant.
                        \n\n“You’re ne from here, en I will ne welcome a stranger in this refuge. Say what you’re looking for en begone.”
                        '
                        'The stories of my ancestors may reveal to me who this man is.' if pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stories of my ancestors may reveal to me who this man is.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I’ve read about people like him in Wright’s Tablets.' ( condition="at == 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve read about people like him in Wright’s Tablets.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I explain who I am.':
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                            python:
                                search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump druidcavetypingnamefirsttime
                'I look around. “I think something has swallowed your wall, old man. Better move your veggies inside.”' ( condition="at == 'playful'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) I look around. “I think something has swallowed your wall, old man. Better move your veggies inside.”')
                    $ druidcave_druid_friendship -= 1
                    $ at_activate = 0
                    $ at = 0
                    if pc_class == "scholar" and pc_religion != "pagan":
                        $ at_unlock_knowledge = 1
                    menu:
                        'The reprimanding look is followed by ice-cold words. “A traveler is ne going to teach me how to take {i}care{/i} of ma land. Your words are of a soul as dumb as a fowl.” Digesting the thick accent and the insult it delivers, you get off your horse, once again hearing the man’s annoyed voice. “Let me see you whilst you speak, I can ne hear without magic, but I’ll read your lips.”
                        \n\nHe doesn’t yell, but his voice reminds you of a combat instructor from the city. His face is wrinkled, but he sits straight, with beard and hair still carrying glimpses of fair blonde. He’s tanned like a worker and his eyes are blue and piercing, as if they belong to an infant.
                        \n\n“‘Tis a refuge for those who are trusted, but I see nae friendly breath in you. Say what you’re looking for en leave me be.”
                        '
                        'The stories of my ancestors may reveal to me who this man is.' if pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stories of my ancestors may reveal to me who this man is.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I’ve read about people like him in Wright’s Tablets.' ( condition="at == 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve read about people like him in Wright’s Tablets.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I explain who I am.':
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                            python:
                                search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump druidcavetypingnamefirsttime
                'I get off my horse respectfully.' ( condition="at == 'distanced'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) I get off my horse respectfully.')
                    $ at_activate = 0
                    $ at = 0
                    if pc_class == "scholar" and pc_religion != "pagan":
                        $ at_unlock_knowledge = 1
                    menu:
                        'You dismount and keep an eye on {color=#f6d6bd}[horsename]{/color}. You greet the man and as he nods back to you, you mention that you have a few questions. There’s cold civility in the air, as if you’re sharing a table at an inn.
                        \n\n“I need you to look at me whilst you speak.” His strict voice reminds you of a master of craft guild, though his thick accent distorts this image. “I can ne hear without magic, but I’ll read your lips. I’ve nae wish to talk about your daily struggles, traveler. It’s ne a refuge for strangers. Say what you’re looking for and let our paths split.”
                        \n\nHe doesn’t yell, but his voice is not used to being opposed. His face is wrinkled, but he sits straight, with beard and hair still carrying glimpses of fair blonde. He’s tanned like a worker and his eyes are blue and piercing, as if they belong to an infant.
                        '
                        'The stories of my ancestors may reveal to me who this man is.' if pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stories of my ancestors may reveal to me who this man is.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I’ve read about people like him in Wright’s Tablets.' ( condition="at == 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve read about people like him in Wright’s Tablets.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I explain who I am.':
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                            python:
                                search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump druidcavetypingnamefirsttime
                'Without a word, I observe him from the saddle silently.' ( condition="at == 'intimidating'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) Without a word, I observe him from the saddle silently.')
                    $ at_activate = 0
                    $ at = 0
                    $ druidcave_druid_friendship -= 1
                    if pc_class == "scholar" and pc_religion != "pagan":
                        $ at_unlock_knowledge = 1
                    menu:
                        'After a silent minute, the man bursts out laughing. “You do ne eva have time to touch the ground? If you’re going to dwell there, better speak loud en clear, oh brave vanquisher. But do ne expect me to welcome a brigand with a chatter.”
                        \n\nBefore you answer, he reprimands you with a thick accent. “I need you to look at me whilst you speak. I can ne hear you without magic, but I’ll read your lips. ‘Tis a refuge for those who are trusted, en I see nae friendly breath in you. Say what you’re looking for en leave me be.”
                        \n\nHe doesn’t yell, but his voice reminds you of a combat instructor from the city. His face is wrinkled, but he sits straight, with beard and hair still carrying glimpses of fair blonde. He’s tanned like a worker and his eyes are blue and piercing, as if they belong to an infant.
                        '
                        'The stories of my ancestors may reveal to me who this man is.' if pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stories of my ancestors may reveal to me who this man is.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I’ve read about people like him in Wright’s Tablets.' ( condition="at == 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve read about people like him in Wright’s Tablets.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I explain who I am.':
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                            python:
                                search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump druidcavetypingnamefirsttime
                'I get off my horse and, with a lowered head, I approach him. “I’m seeking your guidance, old man.”' ( condition="at == 'vulnerable'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) I get off my horse and, with a lowered head, I approach him. “I’m seeking your guidance, old man.”')
                    $ at_activate = 0
                    $ druidcave_druid_friendship += 1
                    $ at = 0
                    if pc_class == "scholar" and pc_religion != "pagan":
                        $ at_unlock_knowledge = 1
                    menu:
                        'He moves aside and invites you to sit next to him. “Come closer, traveler. I need you to look at me whilst you speak.” His tone is gentle, but strict, as of a teacher. “I can ne hear you without magic, I’ll read your lips. Your tongue tells me that you’re ne from here, but I’ll listen to what bothers you.”
                        \n\nHis face is wrinkled, but he sits straight, with beard and hair still carrying glimpses of fair blonde. He’s tanned like a worker and his eyes are blue and piercing, as if they belong to an infant.
                        \n\nYou rest on the planks, observing the peaceful garden and the few frogs resting on the shore.
                        '
                        'The stories of my ancestors may reveal to me who this man is.' if pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stories of my ancestors may reveal to me who this man is.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I’ve read about people like him in Wright’s Tablets.' ( condition="at == 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve read about people like him in Wright’s Tablets.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump druidcavetypingnameclue
                        'I thank him for his kindness.':
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                            python:
                                search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump druidcavetypingnamefirsttime

    label druidcavetypingnameclue:
        if not description_druids01:
            $ description_druids01 = "I can find the local druids in their cave, near the large tree in the southwest corner of the peninsula, on the edge of the swamp."
        menu:
            'You ponder about his unusual vigor and the unguarded garden. He may be a spiritual leader of a pagan community, most likely a spellcaster. Druids try to protect others from nature’s wrath by teaching them to respect the laws of balance and restraint. Different tribes develop their own traditions, but you know that in this province such priests prefer to be addressed as “forest speakers.”
            '
            'I explain who I am.' if druidcave_druid_friendship <= 0:
                $ at_unlock_knowledge = 0
                $ at = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                python:
                    search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump druidcavetypingnamefirsttime
            'I thank him for his kindness.' if druidcave_druid_friendship > 0:
                $ at_unlock_knowledge = 0
                $ at = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain who I am.')
                python:
                    search = renpy.input("What do you call him? (example: old man)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump druidcavetypingnamefirsttime

        label druidcavetypingnamefirsttime:
            if search == "forestspeaker" or search == "speakeroftheforest" or search == "speakerofforest" or search == "speakeroftheforests" or search == "forestsspeaker" or search == "greetingsforestsspeaker" or search == "hiforestsspeaker" or search == "helloforestsspeaker":
                $ druidcave_druid_forestspeaker = 1
                $ druidcave_druid_friendship += 2
                if not item_wingedhourglass_worn and not druidcave_druid_hourglass:
                    menu:
                        'He lowers his head and closes his eyes, taking slow, deep breaths, forcing you to wait in silence. The elder is tall, with long hair and a beard that was let loose a long time ago. His sandals are covered in dust, and you spot dirt on his clothes and skin. The woolen tunic and linen were made with care, decorated with colorful threads at the collar and sleeves. Now all the blues and greens have faded, and the fabric is held together by patches and stitches.
                        \n\nHe unfolds his hands and puts them on his lap, palms up. “You know our customs, at least some of them. Those who know how to bow to the trees will never suffer from wild creatures.”
                        '
                        'I wait for him to look at me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                            jump druidcavedruidcavefirsttime02
                        'I do my best not to smirk. He doesn’t know what he’s talking about.' if pc_religion != "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do my best not to smirk. He doesn’t know what he’s talking about.')
                            jump druidcavedruidcavefirsttime02
                else:
                    if item_wingedhourglass_worn:
                        $ custom1 = "eva if you’re wearing a sign of death on your neck"
                    else:
                        $ custom1 = "eva if you used to wear a sign of death on your neck"
                    menu:
                        'He lowers his head and closes his eyes, taking slow, deep breaths, forcing you to wait in silence. The elder is tall, with long hair and a beard that was let loose a long time ago. His sandals are covered in dust, and you spot dirt on his clothes and skin. The woolen tunic and linen were made with care, decorated with colorful threads at the collar and sleeves. Now all the blues and greens have faded, and the fabric is held together by patches and stitches.
                        \n\nWhile his voice is gentle, he unfolds his fingers and points at your chest. “You know our customs, at least some of them, [custom1]. As long as you do ne spill blood, you’ll find nae threat here. The’s nae hatred in the forest, only that which you bring yourself.”
                        '
                        'I wait for him to look at me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                            jump druidcavedruidcavefirsttime02
                        'I do my best not to smirk. He doesn’t know what he’s talking about.' if pc_religion != "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do my best not to smirk. He doesn’t know what he’s talking about.')
                            jump druidcavedruidcavefirsttime02
            #############################
            elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag":
                python:
                    search = renpy.input("...Let’s try this again. What do you call him?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump druidcavetypingnamefirsttime
            #############################
            else:
                if not item_wingedhourglass_worn and not druidcave_druid_hourglass:
                    menu:
                        'He stares off across the garden beds, forcing you to wait in silence. The elder is tall, with long hair and a beard that was let loose a long time ago. His sandals are covered in dust, and you spot dirt on his clothes and skin. The woolen tunic and linen were made with care, decorated with colorful threads at the collar and sleeves. Now all the blues and greens have faded, and the fabric is held together by patches and stitches.
                        \n\nHis hands are still folded, the voice remains firm. “You do ne know our customs. Your name, your trade, your calling mean naething to the forest. I do ne know what you expected to find here, but this is ne a place for strangers.”
                        '
                        'I wait for him to look at me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                            jump druidcavedruidcavefirsttime02
                        'I do my best not to smirk. He doesn’t know what he’s talking about.' if pc_religion != "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do my best not to smirk. He doesn’t know what he’s talking about.')
                            jump druidcavedruidcavefirsttime02
                else:
                    $ druidcave_druid_friendship -= 1
                    if item_wingedhourglass_worn:
                        $ custom1 = "you’re wearing a sign of death on your neck"
                    else:
                        $ custom1 = "you used to wear a sign of death on your neck"
                    menu:
                        'He stares off across the garden beds, forcing you to wait in silence. The elder is tall, with long hair and a beard that was let loose a long time ago. His sandals are covered in dust, and you spot dirt on his clothes and skin. The woolen tunic and linen were made with care, decorated with colorful threads at the collar and sleeves. Now all the blues and greens have faded, and the fabric is held together by patches and stitches.
                        \n\nWhile his voice remains firm, he unfolds his fingers and points at your chest. “You do ne know our customs, en [custom1]. Your name, your trade, your calling mean naething to the forest. I do ne know what you expected to find here, but this is ne a place for strangers.”
                        '
                        'I wait for him to look at me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                            jump druidcavedruidcavefirsttime02
                        'I do my best not to smirk. Pagans always blame Wright’s followers for their own wrongdoings.' if pc_religion != "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do my best not to smirk. He doesn’t know what he’s talking about.')
                            jump druidcavedruidcavefirsttime02

        label druidcavesupporttyping:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know how I should have addressed you. I want to fix my mistake.”')
            python:
                search = renpy.input("What do you call him?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            jump druidcavetypingnameothertimes

    label druidcavetypingnameothertimes:
        if search == "forestspeaker" or search == "speakeroftheforest" or search == "speakerofforest" or search == "speakeroftheforests" or search == "forestsspeaker" or search == "greetingsforestsspeaker" or search == "hiforestsspeaker" or search == "helloforestsspeaker":
            $ druidcave_druid_forestspeaker = 1
            $ druidcave_druid_friendship += 1
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            if not item_wingedhourglass_worn and not druidcave_druid_hourglass:
                $ questionpreset = "druidcave1"
                menu:
                    'He nods. “The voice of the forest guards the soul carriers. Those who bow to the trees will ne suffer from wild creatures.” He smiles, looking at you with sky-like eyes. “You’ve made the decision to learn our customs, en I appreciate it. ‘Tis ne ma goal to turn people into strangers.”
                    '
                    '(druidcave1 set)':
                        pass
            else:
                $ questionpreset = "druidcave1"
                if item_wingedhourglass_worn:
                    $ custom1 = "eva if you’re wearing a sign of death on your neck"
                else:
                    $ custom1 = "eva if you used to wear a sign of death on your neck"
                menu:
                    'He nods. “The voice of the forest guards the soul carriers. Those who bow to the trees will ne suffer from wild creatures.” He points at your chest. “You’ve made the decision to learn our customs, [custom1]. ‘Tis ne ma goal to turn people into strangers. The’s nae hatred in the forest, only that which you bring yourself.”
                    '
                    '(druidcave1 set)':
                        pass
        #############################
        elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag" or search == "bitch" or search == "whore" or search == "cunt":
            python:
                search = renpy.input("...Let’s try this again. What do you call him?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            jump druidcavetypingnameothertimes
        #############################
        else:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                '“You do ne understand the sound of the forest, you’re as deaf as these rocks. You want to build bridges, but for you they are just structures, owned en used by humans. Prove that you’re ready to learn our customs en the bridge will grow on its own.”
                '
                '(druidcave1 set)':
                    pass

    label druidcavedruidcavefirsttime02:
        stop nature fadeout 6.0
        $ renpy.music.play("audio/track_10druidcave.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        menu:
            'The man stands up and approaches your palfrey. Without touching it, he observes its eyes, mane, stomach, and rear. {color=#f6d6bd}[horsename]{/color} ignores this examination.
            \n\n“Ma nose was right, then. {color=#f6d6bd}Asterion{/color} is dead, as are his plans. Such is the fate of all dreamers.”
            \n\nHe turns toward you with a grim look. “Are you going to look for him?” You nod. “Why? If he’s vanished into the fogs, the’s nae point in putting yourself in danger. What do you expect to find?”
            '
            '“It’s a job. There’s a reward for finding him.”' if quest_asterion == 1 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a job. There’s a reward for finding him.”')
                menu:
                    'He closes his eyes and nods slowly. “The people of the North need someone willing to jump through the fire in exchange for furs en iron. Yet I wish you’d focus on saving the living, ne chasing those who are already gone.”
                    \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                    '
                    'Old people need time to gather their thoughts.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
                    'He tries to dictate the pace of the conversation and put me in my place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
            '“He may need my help.”' if quest_asterion == 1 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He may need my help.”')
                $ druidcave_druid_friendship += 1
                menu:
                    '“Do you believe that? That a man with no power over animals could disappear in the wilderness en survive for that long?” He lets out a chilling laugh. “I bow to your optimism.” He doesn’t actually bow. “If what you say is honest, you en I could share our paths one day. Defending those who ca ne help themselves is something that... Makes me whole.”
                    \n\nHe takes a deep breath and smiles. “You have some questions for me.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        $ minutes += 10
                        jump druidcavedruidcavefirsttime03
            '“I need to know what kind of danger he encountered.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to know what kind of danger he encountered.”')
                menu:
                    'He’s observing you carefully. “Do you plan to get rid of this danger, or maybe learn from {color=#f6d6bd}Asterion’s{/color} mistakes? Or are you still thinking about leaving this land for good?” He starts to chuckle. “Only the right questions will bring you the answers.”
                    \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                    '
                    'Old people need time to gather their thoughts.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
                    'He tries to dictate the pace of the conversation and put me in my place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
            '“If he’s dead, I want people to know about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If he’s dead, I want people to know about it.”')
                menu:
                    'There’s a playful glimpse in his eye. “En you {i}just{/i} want the truth for its own sake, with nae gain behind it?” His laughter is chilling. “I heard he had put his hands into many storms, which will ne end without him. I do ne doubt people will value the knowledge.” He pauses for a moment and looks away. “The peninsula could use some honesty.”
                    \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                    '
                    'Old people need time to gather their thoughts.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
                    'He tries to dictate the pace of the conversation and put me in my place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
            '“If someone tried to make him disappear... They deserve to face justice.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If someone tried to make him disappear... They deserve to face justice.”')
                menu:
                    'His chuckle is close to being a cough. “This realm is owned by beasts. Doom falls upon any soul that pokes the clouds with a stick.” His eyes are amused. “If someone had hurt him, they would have given you dozens of reasons why ‘twas crucial for their survival.” He pauses for a moment. “Good luck looking for justice, traveler. When an egg is cracked by an ant, there’s nae right or wrong side.”
                    \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                    '
                    'Old people need time to gather their thoughts.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
                    'He tries to dictate the pace of the conversation and put me in my place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
            '“There’s no reason why you need to know that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s no reason why you need to know that.”')
                $ druidcave_druid_friendship -= 1
                menu:
                    '“So be it.” He walks past you. “You came here as a leech, not a trader.” With lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                    '
                    'Old people need time to gather their thoughts.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
                    'He tries to dictate the pace of the conversation and put me in my place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                        $ quarters += 1
                        jump druidcavedruidcavefirsttime03
            '“I’ve already found him. Or what was left of him.”' if quest_asterion == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve already found him. Or what was left of him.')
                menu:
                    '“Is that right?” He seems to be surprised. “May you share this tale with me?”
                    '
                    'I tell him what I know.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him what I know.')
                        $ druidcave_druid_friendship += 1
                        $ druidcave_druid_about_asterion2 = 1
                        $ quarters += 1
                        menu:
                            'His eyes widen after you mention the undead from a cave. Once he speaks, his voice is shaking. “Awoken by the fogs... You released him from the worst fate. To know the truth...” He sighs. “It feels right.”
                            '
                            'I nod.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                                jump druidcavedruidcavefirsttime03
                    'I smile. “Trust me, you don’t want to know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Trust me, you don’t want to know.”')
                        $ druidcave_druid_about_asterion2 = 2
                        menu:
                            '”I see,” he observes you for a moment. “I will honor the judgment of a silent roadwarden.”
                            \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                            '
                            'Old people need time to gather their thoughts.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                                $ quarters += 1
                                jump druidcavedruidcavefirsttime03
                            'He tries to dictate the pace of the conversation and put me in my place.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                                $ quarters += 1
                                jump druidcavedruidcavefirsttime03
                    'I shake my head. “I need to keep it to myself, at least for now.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake my head. “I need to keep it to myself, at least for now.”')
                        $ druidcave_druid_about_asterion2 = 2
                        menu:
                            '”I see,” he observes you for a moment. “More of the games.”
                            \n\nWith lively steps, he heads toward the spring. He washes his hands, once again forcing you to wait.
                            '
                            'Old people need time to gather their thoughts.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Old people need time to gather their thoughts.')
                                $ quarters += 1
                                jump druidcavedruidcavefirsttime03
                            'He tries to dictate the pace of the conversation and put me in my place.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tries to dictate the pace of the conversation and put me in my place.')
                                $ quarters += 1
                                jump druidcavedruidcavefirsttime03

###############
label druidcavedruidcavefirsttime03:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    if druidcave_druid_friendship >= 2:
        $ custom1 = "His voice is warm. “So, how can I help you?”"
    else:
        $ custom1 = "His voice is cold and confident. “So, what do you need?”"
    menu:
        '[custom1]
        '
        '(druidcave1 set)':
            pass

label druidcaveregularquestions:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        'He’s observing your lips. “Do you need anything else?”
        '
        '(druidcave1 set)':
            pass

label druidcaveregularquestionsv2:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        'He’s observing your lips. “Go ahead.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_druids1: #What can you tell me about the druids?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the druids?”')
    if (druidcave_druid_friendship+appearance_charisma) < 5:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        $ druidcave_druid_about_druids1_gray = 1
        menu:
            'He strokes his beard gently. “I will ne share our paths with strangers. We are of the people of {color=#f6d6bd}Howler’s Dell{/color}, en of the lands around it.”
            '
            '(druidcave1 set)':
                pass
    else:
        $ druidcave_druid_about_druids1 = 1
        $ description_druids06 = "I heard that an elderly druid who lives in the cave in the southwest corner of the peninsula is a selfless man who considers the well-being of others to be his top priority."
        $ description_druids09 = "According to {color=#f6d6bd}an old druid from the cave{/color}: “The forest guides us, en we share its wisdom with the tribes. We and they ought to stay humble, take from the land what is needed instead of what’s wanted. Ne because ‘tis something we {i}believe{/i} in, but because it protects us from the wrath of the herds. To stay safe, one {i}needs{/i} to know how to be patient, take restraint into their hearts. En to make the beasts listen to us, we keep the animals healthy, teaching them to ne approach our homes en travelers.”"
        menu:
            'He strokes his beard gently. “The forest guides us, en we share its wisdom with the tribes. We and they ought to stay humble, take from the land what is needed instead of what’s wanted. Ne because ‘tis something we {i}believe{/i} in, but because it protects us from the wrath of the herds. To stay safe, one {i}needs{/i} to know how to be patient, take restraint into their hearts. En to make the beasts listen to us, we keep the animals healthy, teaching them to ne approach our homes en travelers.”
            '
            '“Sounds reasonable.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds reasonable.”')
                if pc_religion == "pagan":
                    $ pc_faithpoints += 1
                    $ pc_faithpoints_opportunities += 1
                if pc_religion == "theunitedchurch":
                    $ pc_faithpoints -= 1
                jump druidcaveregularquestions
            'I change the topic. I know that monsters will never be able to live side by side with people.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to change the topic. I know that monsters will never be able to live side by side with monsters.')
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                jump druidcaveregularquestionsv2

label druidcaveaboutweather01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Since you know so much about nature... Could you predict the weather for me?”')
    jump druidcaveaboutweather03

    label druidcaveaboutweather02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of weather do you expect for tomorrow?”')
        jump druidcaveaboutweather03

    label druidcaveaboutweather03:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        if day == 1:
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 2:
            $ custom1 = "“A great rain will fall on us this very night.”"
        elif day == 3: # weathermud
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 4:
            $ custom1 = "“There will be a lot of sun, but also plenty of cold winds.”"
        elif day == 5:
            $ custom1 = "“A cold day awaits us, but ne a harsh one.”"
        elif day == 6:
            $ custom1 = "“It should rain gently both in the night en in the day.”"
        elif day == 7: # weathermud
            $ custom1 = "“The fogs will cover the dawn, eva if ne for long.”"
        elif day == 8: # weatherfog
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 9:
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 10:
            $ custom1 = "“There will be a lot of sun, but also plenty of cold winds.”"
        elif day == 11:
            $ custom1 = "“It will start to rain soon, maybe this evening.”"
        elif day == 12: # weathermud
            $ custom1 = "“A cold day awaits us, but ne a harsh one.”"
        elif day == 13:
            $ custom1 = "“There will be a lot of sun, but also plenty of cold winds.”"
        elif day == 14:
            $ custom1 = "“The fogs will cover the night and dawn. Fearsome for some, whilst wonderful for others.”"
        elif day == 15: # weatherfog
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 16:
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 17:
            $ custom1 = "“A great rain will fall on us this very night.”"
        elif day == 18: # weathermud
            $ custom1 = "“It will ne get any warmer than it is now, en more rains are to come.”"
        elif day == 19: # weathermud
            $ custom1 = "“A cold day awaits us, but ne a harsh one.”"
        elif day == 20:
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 21:
            $ custom1 = "“The fogs will start in the evening, en make the night beasts a great threat.”"
        elif day == 22: # weatherfog
            $ custom1 = "“A cold day awaits us, but ne a harsh one.”"
        elif day == 23:
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 24:
            $ custom1 = "“It should rain gently both in the night en in the day.”"
        elif day == 25: # weathermud
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 26:
            $ custom1 = "“There will be a lot of sun, but also plenty of cold winds.”"
        elif day == 27:
            $ custom1 = "“The fogs will cover the dawn, eva if ne for long.”"
        elif day == 28: # weatherfog
            $ custom1 = "“It will get warmer than usual. The last such days before fall.”"
        elif day == 29:
            $ custom1 = "“It will remain warm. The last such days before fall.”"
        elif day == 30 and world_deadline == 30:
            $ custom1 = "“I can ne tell, traveler. ‘Tis a nature’s mystery.”"
        elif day == 30:
            $ custom1 = "“‘Tis getting colder with each day. There will be more rains, and more fogs, but ne tomorrow.”"
        elif day == 31:
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 32:
            $ custom1 = "“A great rain will fall on us this very night.”"
        elif day == 33: # weathermud
            $ custom1 = "“The fogs will cover the dawn, eva if ne for long.”"
        elif day == 34: # weatherfog
            $ custom1 = "“There will be a lot of sun, but also plenty of cold winds.”"
        elif day == 35:
            $ custom1 = "“It should rain gently both in the night en in the day.”"
        elif day == 36: # weathermud
            $ custom1 = "“A cold day awaits us, but ne a harsh one.”"
        elif day == 37:
            $ custom1 = "“The fogs will cover the dawn, eva if ne for long.”"
        elif day == 38: # weatherfog
            $ custom1 = "“The winds will be gentle, but the light will hide behind clouds.”"
        elif day == 39:
            $ custom1 = "“It will be a warm and gentle day.”"
        elif day == 40 and world_deadline == 40:
            $ custom1 = "“I can ne tell, traveler. ‘Tis a nature’s mystery.”"
        elif day == 40:
            $ custom1 = "“A sunny day awaits us. May be one of the last few before the snows come.”"
        elif day == 41:
            $ custom1 = "“A great rain will fall on us this very night.”"
        elif day == 42:# weathermud
            $ custom1 = "“It will ne get any warmer than it is now, en more rains are to come.”"
        elif day == 43:# weathermud
            $ custom1 = "“The rains will fade away, but the fogs are to cover the night. The autumn spirits are chasing after their prey.”"
        elif day == 44:# weatherfog
            $ custom1 = "“‘Tis about to get colder, despite the new sun.”"
        elif day == 45:
            $ custom1 = "“I can ne tell, traveler. ‘Tis a nature’s mystery.”"
        $ minutes += 5
        if not druidcave_druid_about_weather:
            $ custom2 = "“If ‘tis so easy, why can ne every soul learn to read the weather?” His harsh gaze shifts into an amused smile. “But it may just be that na ancestors have taught me a few tricks.”\n\nIt takes him a few minutes to study the clouds, listen to the wind, touch the rocks, and observe the flight of birds and insects. In the end, he crouches with a flexibility that’s surprising for his age, and speaks out loud a few words in the Old Speech, drawing a vague symbol in the ground with a finger, then almost violently grasping the soil. He stands up and blows into his fist, spreading its content in front of him. He then nods toward you."
        else:
            $ custom2 = "It takes him a few minutes to complete his ritual."
        $ druidcave_druid_about_weather = day
        menu:
            '[custom2] [custom1]
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_greenmountaintribe1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”')
    if (druidcave_druid_friendship+appearance_charisma) < 7:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        $ druidcave_druid_about_greenmountaintribe1_gray = 1
        menu:
            'He scowls at you, then looks down the path. “The’s nae reason for anyone to bother them, or to leave the safe paths.”
            '
            '(druidcave1 set)':
                pass
    else:
        label druidcaveaboutthegreenmountaintribe03:
            $ druidcave_druid_about_greenmountaintribe1 = 1
            if not quest_reachthepaganvillage:
                $ quest_reachthepaganvillage = 1
                $ renpy.notify("New entry: The Hidden Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
            $ quest_reachthepaganvillage_description01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
            $ description_greenmountaintribe01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
            $ description_greenmountaintribe03 = "{color=#f6d6bd}The druid from the cave{/color} has told me that once I find this place, I should introduce myself as “a freedom seeker, a friend of the speakers of the forest,” and that I need to present myself with humbleness."
            $ description_greenmountaintribe04 = "This tribe doesn’t trust people who follow Wright’s teaching."
            menu:
                'He considers your question and finally looks at the sky, making his long hair fall on his back. “Listen closely, I’m not going to say anything else.”
                \n\nHe takes a deep breath and turns toward the pond, observing the current. “The road in the far east, one tha’s now abandoned, is ne showing the truth. Look for a brook bridge made of stone. On its northern side, turn east again, go along the stream. It will be rough at first, but soon enough, you’ll get to the game trail, then a mountain. Climb it to reach the village of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who follow traditions older than any of ours. This grim tribe avoids the outside world. Wright’s followers have hurt them deeply.”
                \n\n“If you want them to share a stew with you, this is what you should tell: {i}I’m a freedom seeker, a friend of the speakers of the forest.{/i} Say these words like an unwanted guest looking for a roof. They do ne want you there, but prove to them that you’re willing to listen, ne just speak.” He turns toward you. “The’s naething else to say.”
                '
                '“I have some other questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some other questions.”')
                    if quest_reachthepaganvillage == 1 or quest_reachthepaganvillage == 2:
                        $ renpy.notify("Journal updated: The Hidden Village")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
                    jump druidcaveregularquestionsv2

    label druidcaveaboutthegreenmountaintribe02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still need to learn more about {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”')
        jump druidcaveaboutthegreenmountaintribe03

label druidcaveaboutenteringthedruidcave01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I enter the cavern? I need a place to rest.”')
    if (druidcave_druid_friendship+appearance_charisma) >= 9:
        jump druidcavecavernfirsttime01
    else:
        $ druidcave_cave_open_gray = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            '“Why would I allow a stranger to do such a thing?”
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_job:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
    if (druidcave_druid_friendship+appearance_charisma) < 3 and not druidcave_druid_about_spiritrock:
        $ druidcave_druid_about_job_gray = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'He looks at the garden beds. “We have everything we need.”
            '
            '(druidcave1 set)':
                pass
    else:
        $ druidcave_druid_about_job = 1
        if druidcave_druid_about_spiritrock:
            $ custom1 = "You’ve already talked to {color=#f6d6bd}Photios{/color} from {color=#f6d6bd}Gale Rocks{/color}. He’s in my debt, en I want you to collect what’s mine."
        else:
            $ custom1 = "At the northern coast you’ll find {color=#f6d6bd}Gale Rocks{/color}, a village of fishers. One of them is in my debt, en I want you to collect what’s mine."
        menu:
            '“I believe your goodwill, en I’m in need of your help.” He gestures for you to follow him to the pond. “‘Tis ne a dangerous task, but one that I can ne complete by maself. En my spells are ne enough to ask animals to fetch for me.”
            \n\nHe speaks very slowly. “[custom1]” You want to ask him about this debt, but he doesn’t look at you. He points at a shiny, large fish, with orange and golden scales that’s swimming just nearby. “This gorgeous creature is {i}an empress carp{/i}, one of the few animals that thrive both in the seas en the lakes.”
            '
            'I wait for him to look at me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                $ quest_empresscarp = 1
                $ renpy.notify("New entry: Empress Carp")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Empress Carp{/i}')
                if druidcave_druid_about_spiritrock:
                    $ custom1 = ""
                else:
                    $ custom1 = "Go to that place and find {color=#f6d6bd}Photios{/color}. He’s a young father, an ocean folk with scars on his neck, which he will ne hide. "
                menu:
                    'You don’t know where the man found the large worm that he now drops in the water, feeding his pet. “[custom1]Ask for a male empress carp, but beware - I need it alive, so it can mate with the one I have.”
                    \n\nHe stands up and approaches you. “I do ne sleep on dragon bones, but the’s pneuma in my blood. I’ll use some of it to heal your wounds, though ne more than once. Tha’s fair.”
                    '
                    '“I agree.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to look at me.')
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "druidcave1"
                        menu:
                            '“I’m glad. The empress carp we have keeps our water clean of leeches, at least as much as it can. One more would help us greatly.”
                            '
                            '(druidcave1 set)':
                                pass
                    '“Traveling with a live fish isn’t going to be easy. I can’t promise I’ll do it right away.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Traveling with a live fish isn’t going to be easy. I can’t promise I’ll do it right away.”')
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "druidcave1"
                        menu:
                            '“Do ne worry. As long as it arrives here before fall, en {i}alive{/i}, ‘tis going to be a huge help for us.”
                            '
                            '(druidcave1 set)':
                                pass

label druidcaveonsleepinggiant01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about the giant from the far east.”')
    jump druidcaveonsleepinggiant02
    label druidcaveonsleepinggiant01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you help me wake up the giant from the far east?”')
        if (druidcave_druid_friendship+appearance_charisma) < 10:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ druidcave_druid_about_sleepinggiant_gray = 1
            $ questionpreset = "druidcave1"
            menu:
                'His eyes get thinner, and his voice more sonorous. “I would ne trust a stranger with the tales of the old tribes. Ask those who build it, if you need it.”
                '
                '(druidcave1 set)':
                    pass
        else:
            label druidcaveonsleepinggiant02:
                $ giantstatue_pray_knows = 1
                if not quest_sleepinggiant:
                    $ quest_sleepinggiant = 1
                    $ renpy.notify("New entry: The Sleeping Giant")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Sleeping Giant{/i}')
                else:
                    $ renpy.notify("Journal updated: The Sleeping Giant")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "druidcave1"
                $ quarters += 1
                menu:
                    'His blue eyes are piercing through your skull and chest. “The knowledge you gather helps the causes I find dear to me, that much I saw. Here’s what you’ll do: kneel in front of the statue, and pray with these words.” He utters a bunch of nonsense, and seeing your confused look, he lets out a sigh. “Eva with these words on your tongue, you’d have nae eyes to see through them. Speak with me, and learn.”
                    \n\nHe spends a good few minutes teaching you the phrases from the Old Speech, until you’re able to repeat them without mistakes, though also no comprehension. While your tongue is not used to some of the sounds, their rhythm makes you think of a poem, and helps you a lot.
                    \n\n“You need naething more.”
                    '
                    '(druidcave1 set)':
                        pass

label druidcave_druid_about_asterion1: #Have you met {color=#f6d6bd}Asterion{/color}?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you met {color=#f6d6bd}Asterion{/color}?”')
    $ druidcave_druid_about_asterion1 = 1
    $ description_asterion05 = "According to the druid from the cave in the southwest, {color=#f6d6bd}Asterion{/color} was planning to settle down in the peninsula, but was hoping to make it a better place first."
    $ quest_asterion_description03 = "According to {color=#f6d6bd}the druid from the cave{/color} in the southwest, Asterion was last seen in one of the villages in the North."
    $ elah_about_asterion_friendship += 1
    $ description_bandits05 = "According to {color=#f6d6bd}the druid from the cave{/color}, {color=#f6d6bd}Asterion{/color} was planning to get rid of the bandits."
    menu:
        'He wanders among the garden beds, from time to time touching the leaves at hand. “He was here, more than once. He was ne one to stand aside en let events play out by themselves. The villagers from the North are sometimes in need of ma assistance, en {color=#f6d6bd}Asterion{/color} was serving them as a messenger.”
        \n\nHe bends down and tears away a small, flowerless plant. “He wanted to settle down among these roads, maybe to live freely. He had great plans, en wanted to make this realm flourish. To rebuild the ruins, get rid of the brigands, en clear the trade route. I told him that the forest needs nae more people, en that this realm is too wild to feed and clothe everyone. His greed and dreams have eaten him, en now he is nae more.”
        \n\nHe pauses and you can hear his heavy breathing, as if he’s getting tired. He straightens up. “En tha’s that, traveler. If you want to look for his shell, travel north, far north. People there should know where he is.”
        '
        '“I’ll do that.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do that.”')
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
            jump druidcaveregularquestions

    label druidcave_druid_about_asterion2: #Have you met {color=#f6d6bd}Asterion{/color}?
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        $ druidcave_druid_friendship += 1
        $ druidcave_druid_about_asterion2 = 1
        $ quarters += 1
        menu:
            'His eyes widen after you mention the undead from a cave. Once he speaks, his voice is shaking. “Awoken by the fogs... You released him from the worst fate. To know the truth...” He sighs. “It feels right.”
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_peninsula: #What can you tell me about the peninsula?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the peninsula?”')
    $ druidcave_druid_about_peninsula = 1
    $ quest_explorepeninsula_description04 = "I heard that many creatures have recently left the northern forests, which results in much more tension among the predators. Some claim that the wilderness has become unusually dangerous."
    menu:
        '“Can? I’ve lived here for almost a century, traveled both by the paths en through the wilderness.” His voice becomes stronger and makes you think of a bard. “But I will ne be your guide or a teacher, en if the’s anything I can wish for, ‘tis that you will stay away from the woods. The creatures get angrier the more we take from them. They do ne listen to our warnings, en one day they’ll bury us under a storm of claws en fangs. There will be nae soul to spare a tear after us.”
        \n\nHis eyes are as harsh as a hawk’s, making him look like a priest who hears a child asking for honey on a day of ceremonial fasting. “Do ne poke the hornets’ nest. Do ne ride east, en never use the path that runs through the heart of this land. That road was meant to save time, but brings only death. Be a servant, ne an overseer, do ne try to bend this place to your will.” He points at you and wags his finger after every word. “Your will, anyone’s will, is the key to danger, ne salvation.”
        '
        'I thank him. These instructions are in line with my own thoughts.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank him. These instructions are in line with my own thoughts.')
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
            jump druidcaveregularquestions
        'I’m not going to be anyone’s puppet.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not going to be anyone’s puppet.')
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
            jump druidcaveregularquestions
        'I need to take some risks to achieve my goals.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to take some risks to achieve my goals.')
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
            jump druidcaveregularquestions

label druidcave_druid_about_bandits1: #I’ve heard about some bandits. Were they bothering you?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Were they bothering you?”')
    $ druidcave_druid_about_bandits1 = 1
    $ quest_intelforpeltnorth_description03 = "It looks like the bandits have been especially harsh toward {color=#f6d6bd}White Marshes{/color}."
    $ description_glaucia02 = "I heard that she was raised by her family in the village of {color=#f6d6bd}Gale Rocks{/color}."
    $ description_glaucia03 = "According to {color=#f6d6bd}the druid from the cave{/color}, Glaucia listens only to force and looks for ways to display her own superiority."
    if quest_intelforpeltnorth == 1:
        $ renpy.notify("Journal updated: Glaucia’s Band")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
    $ questionpreset = "druidcave1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'His strokes his beard, but then grasps it nervously. “There are souls who steal from {color=#f6d6bd}White Marshes{/color}, a village in the north. They would ne dare to show up here, but those brigands are brutes, simpletons. Eva their leader, {color=#f6d6bd}Glaucia{/color}, listens only to force, en will humiliate for the enjoyment of her band. She will ne be afraid of some lost roadwarden.”
        \n\nHe lets go of his beard and lowers his head. “She’s drifted so far away from her old self. A kind, bright girl from {color=#f6d6bd}Gale Rocks{/color}, loved by her parents. But now... Do ne cross her, or she’ll find you.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_cave: #What can you tell me about this place?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about this place?”')
    $ druidcave_druid_about_cave = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        '“Your eye sees what the’s to know. People found copper in a cave. It’s been abandoned for a long time now, so we turned it into a shelter to stay close to the sacred tree and its altar. We’re servants, ma wife and I, en this place is naething more than a servants’ house.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_altar: # Can you tell me anything about the altar near the crossroads in the north?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about the altar near the crossroads in the north?”')
    $ beholder_fruit_truth = "Apparently, eating the fruit “heals shell and soul, and makes those who eat it stronger than they ever were.”"
    $ questionpreset = "druidcave1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ druidcave_druid_about_altar = 1
    menu:
        'He smiles. “‘Tis the tree that you should pay attention to, the true gift from the forest. It answers to our offerings and rewards us with its magnificent fruits. They heal both shell and soul, en make anyone who eats them stronger than they ever were. We gather around this altar whenever the winter ends, en whilst it requires a painful sacrifice from all of us, it prepares one soul for the future like naething else could.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about this trapper, {color=#f6d6bd}Erastos{/color}...”')
    $ questionpreset = "druidcave1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quest_recruitahunter_spokento_druid = 1
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
    menu:
        '“Are you {i}sure{/i} he’s a trapper still?” His tone is inquisitive. “I spoke with him in this very place ne so long ago, en he was {i}convinced{/i} he’s going to take a lighter craft.”
        '
        '(druidcave1 set)':
            pass

label druidcavefirstreward:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve brought what you had asked for.”')
    if item_empresscarp_timelimit+2 < day:
        $ item_empresscarp = 0
        $ renpy.notify("You lost the dead fish.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the dead fish.{/i}')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'He looks inside the bucket quickly. His eyes are grim. “Dead. How long have you been carrying it?” He closes it again and puts it on the bench. “Bring me a living one.”
            '
            '(druidcave1 set)':
                pass
    else:
        $ quest_empresscarp_description01 = "I can collect my reward whenever I want to."
        $ renpy.notify("Journal updated: Empress Carp.\nYou lost the bucket.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Empress Carp.\nYou lost the bucket.{/i}')
        $ druidcave_druid_healing += 1
        $ quest_empresscarp = 2
        $ pc_goal_iwanttohelppoints += 1
        $ item_empresscarp = 0
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        $ druidcave_druid_friendship += 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'He looks inside the bucket quickly, then gives you a big smile. “Now I’m in your debt, traveler. Let me know if you need a healing touch.” He closes the bucket again and puts it on the bench.
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_healing:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ druidcave_druid_healing -= 1
    $ quarters += 1
    $ pc_hp = limit_pc_hp(pc_hp+4)
    show plus4hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 vitality points.{/i}')
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m hurt. I’d like to collect my reward.”')
    $ questionpreset = "druidcave1"
    menu:
        'He reaches for your hands. “Now, the less you blink, the less time it will take. Focus.” You look back into his eyes and join the time in its chaotic run to entropy, through the blue flowers, butterflies, the sky... You barely notice the waves of pneuma that crawl through your arms.
        '
        '(druidcave1 set)':
            pass

label druidcavecaverninstallingarod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color}, the enchantress, has asked me to place these bronze rods in high spots across the peninsula. I should be done in about half an hour.”')
    $ minutes += 5
    menu:
        'He takes and observes the rod for a moment, then closes his eyes and bites it gently. When he returns it, he seems unconvinced. “I sense a spirit in it, but I’m ne one who can tell who’s behind it. How can I be sure?”
        \n\nYou explain what you know about the nature of the rods, but he changes the topic to {color=#f6d6bd}Eudocia{/color} herself. Another minute passes by before he accepts that you indeed know her.
        \n\n“Fine. I’ll ask for her story next time I see her. Go, but away from the spring. Don’t break your neck.”
        \n\nEven a child could get to the higher parts of such a rugged cliff, though you have no reason to expect all the loose rocks to be cleared.
        '
        'I take off my armor and put away my weapons and bags.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take off my armor and put away my weapons and bags.')
            $ quarters += 1
            menu:
                'The bronze rod is attached to your back by a cord. As you place your feet and hands on the rocks, you realize that you have to move slowly, maintaining your balance, pushing away small and large pebbles, making sure that the wall doesn’t collapse under your feet.
                \n\nThe rocks are coarse, supporting your grasp, and you rarely find a sharp spot. The climb resembles a nice summer walk, though your muscles are not prepared for such movements.
                \n\nYou find the perfect spot - a small crack between two massive rocks. You use the rod to broaden it just a bit, then push it halfway in and fill the gaps with a rag. Doing it with one hand makes you dizzy, but not for long.
                '
                'I take a short break to catch a second breath.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a short break to catch a second breath.')
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    $ quarters += 1
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ eudocia_bronzerod_rodin_druidcave = 1
                    $ item_bronzerod -= 1
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
                    if eudocia_bronzerod_rodin_druidcave:
                        show druidcavebronzerod at basicfade
                    $ questionpreset = "druidcave1"
                    menu:
                        'Climbing down is easier, though you struggle to recall exactly where you had previously placed your limbs. The warm sun eases your tension. After a few minutes you land on the soft grass and dust off your hands. Once again, you prepare your equipment.
                        \n\nThe druid gives the shining rod a pouty look.
                        '
                        '(druidcave1 set)':
                            pass

label druidcave_druid_about_solitude: #How can you survive in this place, being all by yourself?
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can you survive in this place, being all by yourself?”')
    $ druidcave_druid_about_solitude = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        'His raised voice makes him sound like a preacher. “One day, me en ma wife will be but defenseless old people, but we’ve studied pneuma en leaves for many decades. I heal wounds en illnesses of humans en animals alike, en the beasts listen to our whispers. The Holy Seed lets our shells wait for death in strength.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_missinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have any hunters from {color=#f6d6bd}Creeks{/color} visited you recently?”')
    $ druidcave_druid_about_missinghunters = 1
    $ creeks_reasonstojoin_creeksaboutlackingmeat = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        '“Here, in the opposite corner of the peninsula? Most people do ne have a beast to carry them for miles, stranger,” his playful tone suddenly gets worried. “Or did their struggles with meat get so grim that they eva consider such dangerous trips?” He takes a deep breath and leans back. “I can ne force beasts to jump under one’s blade. The forest would ne trust me anymore.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_shortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It seems like the path at the heart of the woods is quite dangerous.”')
    $ druidcave_druid_about_shortcut = 1
    $ questionpreset = "druidcave1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not quest_ruins_10yclue09 and quest_ruins == 1 and quest_ruins_description01:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    $ quest_ruins_10yclue09 = "People stopped using the road leading through the heart of the forest."
    menu:
        '“It has a long en dark past, en already caught many souls of its builders. ‘Tis paved with blood, en last ten years have revealed it was all for naething. Since the days of...” He glances at you, once again surprising you with how shiny and lively the blueness of his eyes is. “Of {i}grand discord{/i}, the tribes of this land are locking themselves in their fields en houses, too afraid to leave them behind, too untrusting to meet other souls unguarded. ‘Tis ne the first road to be claimed back by the wilderness, en will ne be the last.”
        \n\nYou ask if he has any tips for you on how to survive such a trip, and he tells you it would be wiser to just avoid it. He then reaches to his pocket, grabs a leaf, and puts it in his mouth, chewing gently. “Death may take many paths to us, stranger, but cats are the one enemy tha’s both as dangerous in its stealth, as in combat. No human can fight it alone. If you see one of them en it’s ne too late... Do ne provoke it, make it wary, but ne scared. Look big, talk a lot, seek its action in its eyes.”
        '
        '(druidcave1 set)':
            pass

label druidcave_druid_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to learn more about {color=#f6d6bd}High Island{/color}.”')
    $ druidcave_druid_about_highisland_gray = 1
    if (druidcave_druid_friendship+appearance_charisma) < druidcave_druid_about_highisland_friendship:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'His eyes widen. “Come again?” You move your lips slowly as you repeat your question, and his look grows suspicious. “Why would you head for that forsaken land?”
            \n\nYou explain briefly what you’ve learned about {color=#f6d6bd}Asterion{/color}. The elder listens patiently, but then straightens up and raises his voice. Even his accent gets thicker, as if he’s repeating an old sermon. “The feet of the living have naething to find in these ancient woods and their ruins. ‘Tis but a graveyard of a tribe long driven out, en their memories deserve to be either forgotten, or shared by their descendents.”
            \n\nHe remains in the same position for another few breaths, then lowers his shoulders and scowls at you. “City spies ought to forget it eva more than most.”
            '
            '(druidcave1 set)':
                pass
    else:
        menu:
            'His eyes widen. “Come again?” You move your lips slowly as you repeat your question, and his look grows suspicious. “Why would you head for that forsaken land?”
            \n\nYou explain briefly what you’ve learned about {color=#f6d6bd}Asterion{/color}. The elder listens patiently, but then straightens up and raises his voice. Even his accent gets thicker, as if he’s repeating an old sermon. “The feet of the living have naething to find in these ancient woods and their ruins. ‘Tis but a graveyard of a tribe long driven out, en their memories deserve to be either forgotten, or shared by their descendents.”
            \n\nHe remains in the same position for another few breaths, then lowers his shoulders and looks into your eyes.
            '
            'I look back at him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look back at him.')
                $ custom1 = "“You may be but a city spy, stranger, but...” he starts, then"
                label druidcave_druid_about_highisland03:
                    hide druidcavebronzerod
                    show areapicture beholdertodruidscave at basicfade
                    menu:
                        '[custom1] enters the path leading down the hill, and gestures for you to follow him on his stroll. During his speech, he never glances at your lips, and doesn’t ask if you have any questions.
                        \n\n“Centuries ago, a great tribe used to live on {color=#f6d6bd}High Island{/color}. Hunting, farming, mining, fishing,” he observes the pond as it gets continuously more muddy. “Prospering. The volcano, {color=#f6d6bd}The Green Mountain{/color}, is naked since its last eruption a few years back, but wait another generation en the wilderness will cover it again.”
                        \n\nThere’s a sudden movement coming from the grasses on your right, but as you look in that direction, you notice that a deer is just observing you, though at an unusually close distance. “‘Tis ne ma place to paint their suffering, but what is ne a secret is how they’ve been treated by {color=#f6d6bd}Hovlavan{/color}. {i}Join us, or the sea will be taken away from you{/i}, they’ve heard. Corsairs had surrounded the island en attacked anyone on sight, waiting for the tribe to surrender.”
                        \n\nHe can’t cover the growing disdain in his voice. “After a decade, The Ten Cities breached the shore, tired of waiting. Cloaked by night, they crossed the walls that were raised to stop beasts, not human-shaped creatures. With farms burnt, supplies taken, en harbors destroyed, the tribe saw no future for itself. Yet, instead of bending to the will of the emperor, they left on their last, hidden ship. At least those who survived.”
                        \n\nHe takes a deeper breath. “The cityfolk resettled the island, but had nae knowledge of it, or of its weird seasons. Beasts and eruptions crushed them, as they had crushed the previous dwellers. There was ne a single soul that would gain from all this suffering.”
                        '
                        'I try to memorize it all.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to memorize it all.”')
                            show areapicture druidcave01alt01 at basicfade behind druidcavebronzerod
                            if eudocia_bronzerod_rodin_druidcave:
                                show druidcavebronzerod at basicfade
                            $ quarters += 1
                            $ druidcave_druid_about_highisland = 1
                            $ highisland_howtoreach_pcknows = 1
                            if not quest_reachthepaganvillage or quest_reachthepaganvillage == 1:
                                $ quest_reachthepaganvillage = 1
                                $ renpy.notify("New entry: The Hidden Village")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
                            $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
                            $ description_highisland10 = "The story of this place reaches centuries back. According to what you’ve heard, {color=#f6d6bd}The Tribe of The Green Mountain{/color} used to thrive on this island, but was thrown out by the corsairs of {color=#f6d6bd}Hovlavan{/color} when they refused to join the city."
                            $ description_greenmountaintribe10 = "According to what you’ve heard, The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but was thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when it refused to join the city."
                            menu:
                                'The man observes the bloody remains of a rabbit lying at the side of the road, and after maybe a minute, nods for you to follow him back to his garden.
                                \n\n“To land there, you have to reach the island soon after dusk, when the sea rises. Only then you can reach the cave hidden behind one of the waterfalls. I do ne know which waterfall it is,” he observes you, making sure you’re listening. “En you’ll do better by speaking with {color=#f6d6bd}The Tribe of The Green Mountain{/color} before you attempt it. ‘Tis {i}their{/i} land, en you ought to ne to trespass.”
                                '
                                '“I’ll consider it.”' if not cephasgaiane_about_highisland_permission:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll consider it.”')
                                    jump druidcaveregularquestions
                                '“Of course.”' if not cephasgaiane_about_highisland_permission:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Of course.”')
                                    jump druidcaveregularquestions
                                '“I took care of it already.”' if cephasgaiane_about_highisland_permission:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Of course.”')
                                    jump druidcaveregularquestions
                                'I say nothing.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                                    jump druidcaveregularquestions

    label druidcave_druid_about_highisland01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elpis{/color} asks you to tell me more about the island, as a favor for her.”')
        $ druidcave_druid_about_highisland_friendship -= 2
        $ druidcave_druid_about_highisland_elpis = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'He lets out a brief snicker. “She thinks her cult can handle an eva greater debt, even though I already left them so much?” Despite his words, there’s a sudden sadness hidden in his sky-blue eyes. “I’d expect no stranger would ever find help at her side. Are you that much of a negotiator, or that much of a tool?” He looks at the spring, not giving you time to answer. “I’ll... think about her request.”
            '
            '(druidcave1 set)':
                pass

    label druidcave_druid_about_highisland02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Look at my lips. I {i}need{/i} to learn more about {color=#f6d6bd}High Island{/color}.”')
        $ custom1 = "He looks you in the eyes, then nods slowly and"
        jump druidcave_druid_about_highisland03

label druidcave_druid_about_ruins1alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I deserve to know what happened to the ruined village.”')
    jump druidcaveabouttheruins02
    label druidcave_druid_about_ruins1:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to know what happened to the village in the east.”')
        if (druidcave_druid_friendship+appearance_charisma) < 11 or not oldpagos_cured:
            $ druidcave_druid_about_ruins1_gray = 1
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                '“En I’m ne willing to tell you that,” he raises his chin, and his beard shakes. “That shameful tale ought to be kept in the past, for the sake of the living.”
                '
                '(druidcave1 set)':
                    pass
        else:
            label druidcaveabouttheruins02:
                $ druidcave_druid_about_ruins1 = 1
                menu:
                    'He lowers his head, but keeps looking at your lips. “En what do you think happened?”
                    '
                    '“It was raided by humans.”' if not druidcave_druid_about_ruins_ver01:
                        jump druidcaveabouttheruins02a
                    '“It was destroyed during the wrath of the herds.”' if not druidcave_druid_about_ruins_ver02:
                        jump druidcaveabouttheruins02b
                    '“It was pillaged by humans, then destroyed by monsters.”' if not druidcave_druid_about_ruins_ver03:
                        jump druidcaveabouttheruins02c
                    '“It was attacked by beasts, then finished off by humans.”' if not druidcave_druid_about_ruins_ver04:
                        jump druidcaveabouttheruins02d
                    '“Humans used monsters to destroy it.”' if not druidcave_druid_about_ruins_ver05:
                        jump druidcaveabouttheruins02e
            label druidcaveabouttheruins02a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was raided by humans.”')
                $ druidcave_druid_about_ruins_ver01 = 1
                $ druidcave_druid_about_ruins_ver02 = 1
                menu:
                    'He stays still, but you notice a glint in his eye. “You only see a part of the picture.”
                    '
                    '“It was raided by humans.”' if not druidcave_druid_about_ruins_ver01:
                        jump druidcaveabouttheruins02a
                    '“It was destroyed during the wrath of the herds.”' if not druidcave_druid_about_ruins_ver02:
                        jump druidcaveabouttheruins02b
                    '“It was pillaged by humans, then destroyed by monsters.”' if not druidcave_druid_about_ruins_ver03:
                        jump druidcaveabouttheruins02c
                    '“It was attacked by beasts, then finished off by humans.”' if not druidcave_druid_about_ruins_ver04:
                        jump druidcaveabouttheruins02d
                    '“Humans used monsters to destroy it.”' if not druidcave_druid_about_ruins_ver05:
                        jump druidcaveabouttheruins02e
            label druidcaveabouttheruins02b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was destroyed during the wrath of the herds.”')
                $ druidcave_druid_about_ruins_ver02 = 1
                $ druidcave_druid_about_ruins_ver01 = 1
                menu:
                    'He frowns slightly. “‘Tis not everything that happened.”
                    '
                    '“It was raided by humans.”' if not druidcave_druid_about_ruins_ver01:
                        jump druidcaveabouttheruins02a
                    '“It was destroyed during the wrath of the herds.”' if not druidcave_druid_about_ruins_ver02:
                        jump druidcaveabouttheruins02b
                    '“It was pillaged by humans, then destroyed by monsters.”' if not druidcave_druid_about_ruins_ver03:
                        jump druidcaveabouttheruins02c
                    '“It was attacked by beasts, then finished off by humans.”' if not druidcave_druid_about_ruins_ver04:
                        jump druidcaveabouttheruins02d
                    '“Humans used monsters to destroy it.”' if not druidcave_druid_about_ruins_ver05:
                        jump druidcaveabouttheruins02e
            label druidcaveabouttheruins02c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was pillaged by humans, then destroyed by monsters.”')
                $ druidcave_druid_about_ruins_ver03 = 1
                if not druidcave_druid_about_ruins_ver01 and not druidcave_druid_about_ruins_ver02 and not druidcave_druid_about_ruins_ver04 and not druidcave_druid_about_ruins_ver05:
                    $ druidcave_druid_friendship += 1
                $ quest_ruins_10yclue04p2 = "{color=#f6d6bd}The druid from the cave{/color} has confirmed that “It was pillaged by humans, then destroyed by monsters.”"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "druidcave1"
                if quest_ruins == 1:
                    $ renpy.notify("Journal updated: The Ruined Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                menu:
                    'He lowers his head. “Yes. You see our shame.”
                    '
                    '(druidcave1 set)':
                        pass
            label druidcaveabouttheruins02d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was attacked by beasts, then finished off by humans.”')
                $ druidcave_druid_about_ruins_ver04 = 1
                menu:
                    'He strokes his beard. “You got it all wrong, stranger.”
                    '
                    '“It was raided by humans.”' if not druidcave_druid_about_ruins_ver01:
                        jump druidcaveabouttheruins02a
                    '“It was destroyed during the wrath of the herds.”' if not druidcave_druid_about_ruins_ver02:
                        jump druidcaveabouttheruins02b
                    '“It was pillaged by humans, then destroyed by monsters.”' if not druidcave_druid_about_ruins_ver03:
                        jump druidcaveabouttheruins02c
                    '“It was attacked by beasts, then finished off by humans.”' if not druidcave_druid_about_ruins_ver04:
                        jump druidcaveabouttheruins02d
                    '“Humans used monsters to destroy it.”' if not druidcave_druid_about_ruins_ver05:
                        jump druidcaveabouttheruins02e
            label druidcaveabouttheruins02e:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was attacked by beasts, then finished off by humans.”')
                $ druidcave_druid_about_ruins_ver05 = 1
                menu:
                    'He lets out a quiet sigh. “Nae soul in the north holds this kind of power.”
                    '
                    '“It was raided by humans.”' if not druidcave_druid_about_ruins_ver01:
                        jump druidcaveabouttheruins02a
                    '“It was destroyed during the wrath of the herds.”' if not druidcave_druid_about_ruins_ver02:
                        jump druidcaveabouttheruins02b
                    '“It was pillaged by humans, then destroyed by monsters.”' if not druidcave_druid_about_ruins_ver03:
                        jump druidcaveabouttheruins02c
                    '“It was attacked by beasts, then finished off by humans.”' if not druidcave_druid_about_ruins_ver04:
                        jump druidcaveabouttheruins02d
                    '“Humans used monsters to destroy it.”' if not druidcave_druid_about_ruins_ver05:
                        jump druidcaveabouttheruins02e

label druidcaveonsnakebait:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show him the snake bait. “What can you tell me about this?”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    $ eudocia_about_flower_druid = 1
    $ item_snakebait_truth = 1
    menu:
        'He needs only a breath to recognize it. “Ah, ‘tis snake bait.” He leans a bit closer. “‘Tis ne that rare, en ne many people need it.”
        \n\nYou learn that it’s infamous for its alleged power to lure serpents and saurians. When consumed in moderation, it makes a shell more responsive to stimuli and makes periods of sleeplessness easier to bear.
        \n\nJuice from a single leaf is enough to induce hallucinations or an addicting sense of dreamlike euphoria. Using a large dose at once, or small doses too often, leads to frailty or death.
        '
        '(druidcave1 set)':
            pass

label druidcaveonthyrsus:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You were {color=#f6d6bd}Thyrsus’{/color} teacher, am I right?”')
    $ druidcave_druid_friendship += 1
    $ druidcave_druid_about_thyrsus = 1
    menu:
        'With a loud sigh, he looks away. “He’s still around? Glad to hear that,” his voice carries pain, but as he carries on, you catch a hint of shame. “He carries ne many good tales of our shared time, I expect?”
        '
        '“He claims your tribe was forcing him to follow pagan teachings, but at least you were a good teacher.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He claims your tribe was forcing him to follow pagan teachings, but at least you were a good teacher.”')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                'His shoulders drop. “Aye, I was ne there to protect him, en ma neighbors treated him poorly. One night, he just left, all by himself, yet he reached his home, despite the threats of the bogs. His pneuma carries great potential, though from what I’ve heard his soul is still... Maturing.”
                \n\nHis eyes look even brighter than usual, but his voice grows stronger. “If you plan to see him again, tell him I’m sorry. Ne just for my daughter, or for that... {i}violent{/i} day. I’m sorry {i}I{/i} failed him.”
                '
                '(druidcave1 set)':
                    pass
        '(lie) “What do you mean? He values your guidance to this day.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “What do you mean? He values your guidance to this day.”')
            $ pc_lies += 1
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                'His frowns, but then spares you a humble smile. “Is that what he said? He judges ma weakness more gently than it deserves. Ma neighbors treated him poorly. One night, he just left, all by himself, yet he reached his home, despite the threats of the bogs. His pneuma carries great potential.”
                \n\nHis eyes look even brighter than usual, but his voice grows stronger. “If you plan to see him again, tell him I’m sorry. Ne just for my daughter, or for that... {i}violent{/i} day. I’m sorry {i}I{/i} failed him.”
                '
                '(druidcave1 set)':
                    pass

label druidcave_about_thyrsusgift_druidcomment01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there something {color=#f6d6bd}Thyrsus{/color} could do to reunite with his parents?”')
    $ druidcave_about_thyrsusgift_druidcomment = 1
    $ minutes += 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        '“Nae, en naer should he.” He looks into your eyes, challengingly so. “He’s done ne a thing wrong, en was rejected ne for his faults, but for what’s beyond his control. His desire is that of a sick, lonely soul,” the strength in his voice starts to dwindle, “but nae one can pluck it out with words alone. In his heart, he’s sitting at the one branch that connects him to his ancestors, but the truth is he’s been tossed aside. What he needs are new roots, en to let go of his longing.”
        \n\nA long pause as he looks at the spring, unable to hear its constant humming. “Eva if you were to say it to him, he wouldn’t listen. But once he seems lost... Tell him I’m ready to hear him out. Like in the old days.”
        '
        '(druidcave1 set)':
            pass

label druidcave_about_elpis_about_thyrsusgift2:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I helped another druid find cursed soil in {color=#f6d6bd}Howler’s{/color} forest garden.”')
    $ druidcave_about_elpis_about_thyrsusgift2 = 1
    $ druidcave_druid_friendship = 1
    $ minutes += 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    $ minutes += 5
    menu:
        'Your tale takes less effort than you expected it would, since the elder seems to be well aware of the spot. “A shameful, deserved trouble. ‘Tis the tomb of a nightmarish object, but it does ne belong to a human shell. The gathering is more than capable of handling it, though we can only hope they’ll be eager to find a lesson in this endeavor.”
        \n\nHe rubs his forehead, right between the eyes, with a pained frown. “But this hope has served me little, so far.”
        '
        '(druidcave1 set)':
            pass

label druidcaveaboutrobes01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why don’t you wear robes, like the druids from {color=#f6d6bd}Howler’s Dell{/color}?”')
    $ druidcave_druid_about_robes = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    menu:
        '“I wear what I need, en therefore what is needed of me,” he speaks with pride. “Ma ancestors knew such path leads to freedom. Ne empty gestures, but honesty, gratitude, en tranquility.” He looks toward the North. “Those left in the village are putting their hands into matters that fit the empty-hearted. Their petty clothes are but a costume, ne better than a dress of a merchant, or a pretty rock thrown into a lake.”
        '
        '(druidcave1 set)':
            pass

label druidcaveaboutphoibe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can we talk about {color=#f6d6bd}Phoibe{/color}, {color=#f6d6bd}Photios’{/color} daughter?”')
    $ druidcave_druid_about_spiritrock = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ description_monastery07 = "{color=#f6d6bd}The old druid{/color} told me to “speak with them with nae anger, but also nae foolery.”"
    $ questionpreset = "druidcave1"
    menu:
        '“He’s still trying to get a spirit rock?” After your nod, he closes his eyes slowly, allowing the gentle breeze to shake his beard. “{color=#f6d6bd}Asterion{/color} mentioned the man’s anger en denial. The’s pride in his efforts, but also pain, as he can ne accept his daughter as the spirits have shaped her.” He opens his eyes, leads you to the main path, and looks north-west, at the very distant mountains. “Beyond {color=#f6d6bd}Old Págos{/color} you’ll find {color=#f6d6bd}the monastery{/color}, with its respectable monks en their haunting temple. Speak with them with nae anger, but also nae foolery. Maybe {color=#f6d6bd}Photios{/color} will listen to Wright’s followers.”
        '
        '(druidcave1 set)':
            pass

label druidcavequestionaboutscholarherbs01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I dabble a bit in herbalism... Any chance you’d sell me some of the woundwort you grow here?”')
    $ druidcave_druid_about_herbs = 1
    menu:
        'He looks at you with a renewed curiosity, then rests at the wooden bench, from where he glances at the pink flowers. His beard shakes as he tilts his head forward. “Wishing to help the wounded, I see. A notable goal.” Once his eyes turn toward your lips, you see a doubting, raised brow. “‘Tis a good season to pick their flowers and leaves, but you’d leave me with naething but the bare stalks and the black tubers in the soil. En I quite like these tubers. You wish to take the oils away, take care of the rest.”
        '
        'It shouldn’t take more than an hour. “Very well.” ':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It shouldn’t take more than an hour. “Very well.”')
            jump druidcavequestionaboutscholarherbs02
        '“Maybe another time.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                'He returns to the same sitting position with which he welcomed you.
                '
                '(druidcave1 set)':
                    pass

    label druidcavequestionaboutscholarherbs02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have time now to dig out these woundworts for you.”')
        label druidcavequestionaboutscholarherbs02:
            $ druidcave_druid_friendship += 1
            $ quarters += 2
            $ druidcave_druid_about_herbs = 2
            menu:
                '“Grab yourself a cloth from the bucket, keep your knees from dirt.” His tone has not a hint of a light-hearted invitation. It’s an order of a master addressing their pupil, a statement as undisputed as the color of the sky.
                \n\nYou put away your belongings and grab both the cloth and a small spade that’s placed next to it. As you prepare {color=#f6d6bd}[horsename]{/color} to graze in peace, you notice a horned bear among the nearby trees, just down the path. It completely ignores your presence and as you’re reaching for the axe, you hear a calm voice of the elder. “Let the beasts drink in peace. They seek nae harm.”
                \n\nAfter a minute or so, you place the cloth on the ground and kneel on it. You start by cutting away the oily parts of the plants with your dagger and placing them on a wax-soaked linen cloth, hoping they’ll stay somewhat fresh before the season ends. You stop caring about the way they color your fingers with green and pink. You don’t have to be gentle, either - after all, you plan to remove the woundworts in their entirety.
                \n\nThe man interrupts you before you start digging. “I do ne expect the’s many herbs growing in the city.”
                \n\nYou look at him and wipe your forehead with a sleeve.
                '
                '“Once you learn how to read, you can find a lot in the herbaria.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Once you learn how to read, you can find a lot in the herbaria.”')
                    $ custom1 = "He opens and closes his mouth. You return to your work, but after a few minutes, the man interrupts you again. “What does a codex like this look like? Are there instructions kept on parchment?”\n\nYou describe the richness stored among hundreds of pages. How each plant is both described and drawn with at least a couple of vivid colors. Through discussion and experiments, the monks gather knowledge about the cultivation and usages of various herbs. “There are cooking and alchemical recipes as well, though kept in other books,” you finish your tale. The man thinks about your tale, so you move on with your task."
                    $ pc_home_druid = "citybooks"
                    jump druidcavequestionaboutscholarherbs03
                '“The monastery has a great garden with all sorts of valuable plants. And caretakers willing to share their knowledge.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The monastery has a great garden with all sorts of valuable plants. And caretakers willing to share their knowledge.”')
                    $ custom1 = "He nods approvingly. “This is ne far away from the way we teach our youngsters. The’s nae better path to wisdom than through telling, showing, en acting, all at once.”"
                    $ pc_home_druid = "citymonasterygarden"
                    jump druidcavequestionaboutscholarherbs03
                '“My neighbors used to be farmers before they lost their home in the war. They helped me a lot.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My neighbors used to be farmers before they lost their home in the war. They helped me a lot.”')
                    $ custom1 = "He seems to be puzzled by your words. You return to your work, and once he carries on, he mostly speaks to himself. “A weird generation will soon arrive. Of people who never held hoes and pitchforks, with rare seeds brought from {color=#f6d6bd}Hovlavan{/color} traders en nae knowledge of how to plant them, but for whom there will be nae place behind the tall walls. May we hope their grandparents can lighten their path with their memories, before they are all lost to the gloom of age.”"
                    $ pc_home_druid = "cityneighbors"
                    jump druidcavequestionaboutscholarherbs03
                '“But people do have gardens in the city. On the roofs, outside of the wall, and in small beds.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But people do have gardens in the city. On the roofs, outside of the wall, and in small beds.”')
                    $ custom1 = "A gentle smile shows up on his face. “I used to think {color=#f6d6bd}Hovlavan{/color} is ne much more than its roads, walls, and tall houses. I heard there are nae trees and shrubs left. Tell me, what do the humans there grow?” You chit-chat with him for a bit, describing the herbs and vegetables that can fit in the pots and tiny scraps of lands."
                    $ pc_home_druid = "cityhasroofgardens"
                    jump druidcavequestionaboutscholarherbs03
                'I shrug. “I wasn’t born in {color=#f6d6bd}Hovlavan{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “I wasn’t born in {color=#f6d6bd}Hovlavan{/color}.”')
                    $ pc_home_druid = "notfromthecity"
                    $ custom1 = "He nods. “I figured as much.”"
                    jump druidcavequestionaboutscholarherbs03

        label druidcavequestionaboutscholarherbs03:
            $ quarters += 1
            $ item_blackwoundwort += 3
            $ renpy.notify("You added three bundles of black woundwort to your bag of ingredients.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added three bundles of black woundwort to your bag of ingredients.{/i}')
            show areapicture druidcave01alt01 at basicfade behind druidcavebronzerod
            if eudocia_bronzerod_rodin_druidcave:
                show druidcavebronzerod at basicfade
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            menu:
                '[custom1]
                \n\nYou stab the soil with the spade, getting to all the black rhizomes and roots you can find. The man tells you to leave the garden bed as it is so he can add some animal dung to it. You’ve gathered a small pile of yellowish worm-like tubers, still covered in dirt, not much longer than a finger and disturbingly twisted. You gesture at the results of your work, but the man frowns and looks toward the pond. “You forgot to wash them, herbalist.”
                '
                '“You have a strong back. Just wash them before you eat.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You have a strong back. Just wash them before you eat.”')
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    $ questionpreset = "druidcave1"
                    menu:
                        'You put the plants on one of the flat rocks near the bench. The man sits in silence, and the air is a bit heavier. The screams of apes and birds make you look around, while the elder observes the garden. You wash your hands in the cool spring and check on your mount, which enjoys its short nap.
                        '
                        '(druidcave1 set)':
                            pass
                '“...Fine.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Fine.”')
                    jump druidcavequestionaboutscholarherbs03a
                'I begrudgingly carry the tubers to the bank.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I begrudgingly carry the tubers to the bank.')
                    label druidcavequestionaboutscholarherbs03a:
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "druidcave1"
                        $ druidcave_druid_friendship += 1
                        $ quarters += 1
                        menu:
                            'You get closer to the tiny waterfall. You stand across it and let the cool water do your job for you, in the meantime washing your hands. The refreshing touch tempts you to take a sip as well. Finally, you put the tubers on the bench, and the old man, without a comment, grabs one of them and puts it in his mouth, chewing with a hint of a smile.
                            \n\nYour mount just woke up from its short nap.
                            '
                            '(druidcave1 set)':
                                pass

label druidcavespring01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the spring.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if cleanliness_equipment <= 0:
        $ custom1 = "{color=#6a6a6a}You need at least 2 pieces of bathing equipment to get more out of this place.{/color}"
        $ custom2 = ""
    elif cleanliness_equipment == 1:
        if item_soap:
            $ custom1 = "The oak-ash soap you own is not enough to help you get cleaner."
        elif item_teethset:
            $ custom1 = "The teeth set you own is not enough to help you get cleaner."
        elif item_perfume:
            $ custom1 = "The perfume you own is not enough to help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need at least 2 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment == 2:
        if item_soap and item_teethset:
            $ custom1 = "The oak-ash soap and the teeth set you own can help you get cleaner."
        elif item_soap and item_perfume:
            $ custom1 = "The oak-ash soap and the perfume you own can help you get cleaner."
        elif item_teethset and item_perfume:
            $ custom1 = "The teeth set and the perfume you own can help you get cleaner."
        $ custom2 = ""
    elif cleanliness_equipment >= 3:
        $ custom1 = "The oak-ash soap, the teeth set, and the perfume you own can help you get cleaner."
        $ custom2 = ""
    menu:
        'Standing astride the spring water won’t be too convenient, but you can shove your head right into the crystal-clear water.
        \n\n[custom1][custom2]
        '
        'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump druidcavespringwashing01
        'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
            jump druidcavespringwashing01
        'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- In an hour I’ll remove blood stains from my clothes.')
            jump druidcavespringlaundry01
        'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump druidcaveleavingthespring01

    label druidcavespringwashing01:
        if not cleanliness:
            if cleanliness_equipment >= 2:
                $ minutes += 20
                $ cleanliness = limit_cleanliness(cleanliness+3)
                show plus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 appearance points.{/i}')
            else:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
        elif cleanliness == 1:
            if cleanliness_equipment >= 2:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        elif cleanliness == 2:
            $ minutes += 10
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'The splashes of cold water free you from tallow, sweat, and dirt.
            '
            'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump druidcavespringwashing01
            'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump druidcavespringwashing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In an hour I’ll remove blood stains from my clothes.')
                jump druidcavespringlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump druidcaveleavingthespring01

    label druidcavespringlaundry01:
        $ cleanliness_clothes_blood = 0
        $ quarters += 4
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'You occasionally rub the fabric while it’s in the flowing water. It goes on for an hour, but doesn’t require too much effort.
            '
            'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump druidcavespringwashing01
            'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump druidcavespringwashing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In an hour I’ll remove blood stains from my clothes.')
                jump druidcavespringlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump druidcaveleavingthespring01

    label druidcaveleavingthespring01:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "druidcave1"
        menu:
            'The druid observes the sky, but looks at you after a few breaths.
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_plague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Old Págos{/color}. A terrible plague has fallen upon it.”')
    $ druidcave_druid_friendship += 1
    $ druidcave_druid_about_plague01 = 1
    $ minutes += 5
    menu:
        'His eyes widen. “What did you say? A plague?”
        \n\nYou tell him everything you’ve heard about the symptoms. He attentively observes your lips and sometimes asks you to clarify some details, though you usually don’t know how to answer him. He finally nods, then turns away and approaches the garden beds, lost in his thoughts. You wait in silence.
        \n\nHe speaks after a short break. “The’s naething I can do.” His words are trembling.
        '
        '“You’ll have their blood on your hands.”' if not druidcave_druid_about_plague01a:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ll have their blood on your hands.”')
            jump druidcave_druid_about_plague01a
        '“No soul says you have to sacrifice yourself.”' if druidcave_druid_about_plague01a and not druidcave_druid_about_plague01c:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would you have to die to do something about it?”')
            jump druidcave_druid_about_plague01c
        'He’s pissing me off. “And that’s it? Are druids really that useless?”' if not druidcave_druid_about_plague01b:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s pissing me off. “And that’s it? Are druids really that useless?”')
            jump druidcave_druid_about_plague01b
        '“Is there anything I can do?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there anything I can do?”')
            jump druidcave_druid_about_plague01d

    label druidcave_druid_about_plague01a: #“You’ll have their blood on your hands.”
        $ druidcave_druid_about_plague01a = 1
        menu:
            '“I wish things were different, but I’ll ne cast away this shell for their sake. I need to stay among the living, ‘Tis my duty to help {color=#f6d6bd}Howler’s{/color}, its ill en weak.” He pauses, then takes a deep breath. “To take care of ma wife.”
            '
            '“You’ll have their blood on your hands.”' if not druidcave_druid_about_plague01a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ll have their blood on your hands.”')
                jump druidcave_druid_about_plague01a
            '“No soul says you have to sacrifice yourself.”' if druidcave_druid_about_plague01a and not druidcave_druid_about_plague01c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would you have to die to do something about it?”')
                jump druidcave_druid_about_plague01c
            'He’s pissing me off. “And that’s it? Are druids really that useless?”' if not druidcave_druid_about_plague01b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s pissing me off. “And that’s it? Are druids really that useless?”')
                jump druidcave_druid_about_plague01b
            '“Is there anything I can do?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there anything I can do?”')
                jump druidcave_druid_about_plague01d

    label druidcave_druid_about_plague01b: #He’s pissing me off. “And that’s it? Are druids really that useless?”
        $ druidcave_druid_about_plague01b = 1
        $ druidcave_druid_friendship -= 1
        menu:
            'He straightens up and furiously walks toward you, wagging his finger. “The’s ne spell master that could cure every illness under the sun, ne here, ne in any land. We do ne choose our calling, we do ne seek {i}power{/i},” he says with spite, then raises his voice. “How blind you must be! Do you wish us to dry out the seas, to ride dragons, juggle the mountains, awaken the dead?”
            \n\nHe only now realizes that he has put the tip of his finger on your chest. He looks at his hand with surprise, then steps back.
            '
            '“You’ll have their blood on your hands.”' if not druidcave_druid_about_plague01a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ll have their blood on your hands.”')
                jump druidcave_druid_about_plague01a
            '“No soul says you have to sacrifice yourself.”' if druidcave_druid_about_plague01a and not druidcave_druid_about_plague01c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would you have to die to do something about it?”')
                jump druidcave_druid_about_plague01c
            'He’s pissing me off. “And that’s it? Are druids really that useless?”' if not druidcave_druid_about_plague01b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s pissing me off. “And that’s it? Are druids really that useless?”')
                jump druidcave_druid_about_plague01b
            '“Is there anything I can do?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there anything I can do?”')
                jump druidcave_druid_about_plague01d

    label druidcave_druid_about_plague01c: #“No soul says you have to sacrifice yourself.”
        $ druidcave_druid_about_plague01c = 1
        menu:
            '“Healing takes knowing. To heal a shell consumed by forces I do ne understand... I must force one’s spirit to crush the weakness, like a blind child trying to trample a spider. I could help one soul, maybe two. But I ca ne clean an entire place. I may die trying. I may die succeeding. I may fail, en stay there as another meal for the illness,” he nods slowly. “Another {i}sacrifice{/i}.”
            '
            '“You’ll have their blood on your hands.”' if not druidcave_druid_about_plague01a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ll have their blood on your hands.”')
                jump druidcave_druid_about_plague01a
            '“No soul says you have to sacrifice yourself.”' if druidcave_druid_about_plague01a and not druidcave_druid_about_plague01c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would you have to die to do something about it?”')
                jump druidcave_druid_about_plague01c
            'He’s pissing me off. “And that’s it? Are druids really that useless?”' if not druidcave_druid_about_plague01b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s pissing me off. “And that’s it? Are druids really that useless?”')
                jump druidcave_druid_about_plague01b
            '“Is there anything I can do?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there anything I can do?”')
                jump druidcave_druid_about_plague01d

    label druidcave_druid_about_plague01d: #“Is there anything I can do?”
        menu:
            'He strokes his beard and examines your equipment. “There may be. You can help me cast a spell of great power, but it will take much. You would ne dare. En you’d have to give up a grand reward. ‘Tis a quest for a hero, ne a messenger. En there are nae heroes.”
            '
            '“You may be right. Tell me more and I’ll decide what to do later on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right. Tell me more and I’ll decide what to do later on.”')
                jump druidcave_druid_about_plague01e
            '“You underestimate me. I show you what I’m made of.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You underestimate me. I show you what I’m made of.”')
                $ druidcave_druid_about_plague_pcwillcure = 1
                jump druidcave_druid_about_plague01e

    label druidcave_druid_about_plague01e:
        $ quest_healingtheplague = 1
        $ beholder_name_known = 1
        $ quest_healingtheplague_description01 = "{color=#f6d6bd}The old druid from the cave{/color} has told me that to help the sick people from {color=#f6d6bd}Old Págos{/color}, he’d need to use the Holy Seed borne by {color=#f6d6bd}Beholder{/color}, the large tree growing near the altar."
        $ quest_healingtheplague_description02 = "The tree “eats magic,” which can also be found in human blood."
        $ renpy.notify("Journal updated: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ questionpreset = "druidcave2"
        menu:
            'Before you finish, he turns away from you and looks at the falling water. “Then listen. Help me awaken {color=#f6d6bd}Beholder{/color}, the good totem from the swamp. You’ve already passed its altar in the crossroads, north from here. It needs to be fed, en it only feasts on spirits. The pneuma held in human blood, the magic locked in items. Offer them, en it will answer your call. But ‘tis a hungry being, en it will ne be nurtured by a single gift. Who knows how much it wants?”
            \n\nHe carries on without pausing, as if he’s speaking from memory. “But let it grow, en it will reward you. Take its Holy Seed, en bring it back to me. I’ll enter the village, en through the totem’s power, I’ll replenish my strength en keep the pneuma before it leaves the lungs of humans.”
            \n\nHe stands in the same spot for a few breaths, then finally looks back at you.
            '
            '(druidcave2 set)':
                pass

    label druidcave_druid_about_plague01f: #“So, I need to {i}offer magic{/i} to the altar. What will we do next?”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, I need to {i}offer magic{/i} to the altar. What will we do next?”')
        $ druidcave_druid_about_plague01f = 1
        $ questionpreset = "druidcave2"
        menu:
            '“When you deliver the Seed to me, we’ll leave, though we’ll need time to get to {color=#f6d6bd}Old Págos{/color} and back. ‘Tis a long road for a shell of my years, but the totem’s gift will keep me strong.”
            '
            '(druidcave2 set)':
                pass

    label druidcave_druid_about_plague01g: #“Tell me more about this... seed.”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about this... seed.”')
        $ druidcave_druid_about_plague01g = 1
        $ questionpreset = "druidcave2"
        menu:
            'His voice becomes confident and solemn. “{color=#f6d6bd}Beholder{/color} bears but one fruit a year, en only if its hunger is satisfied. The heart of this fruit, its Seed, holds a great power of youth, strength, en magic. Therefore, when the winter ends, the people of {color=#f6d6bd}Howler’s Dell{/color} gather at its feet and give away the pneuma held in their blood en possessions. ‘Tis a sacrifice that would kill a single soul, but when shared by many, ‘tis but a sign of acceptance, an act of overcoming pain.”
            '
            '(druidcave2 set)':
                pass

    label druidcave_druid_about_plague01h: #“It sounds like you’re trying to push me into some dark magic, old man.”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It sounds like you’re trying to push me into some dark magic, old man.”')
        $ druidcave_druid_about_plague01h = 1
        $ questionpreset = "druidcave2"
        if item_wingedhourglass_worn or druidcave_druid_hourglass:
            $ druidcave_druid_friendship -= 1
            if item_wingedhourglass_worn:
                $ custom1 = "the winged hourglass on your neck"
            else:
                $ custom1 = "the spot where you used to wear the winged hourglass"
            menu:
                'He points at [custom1]. “Spoken like an inquisitor, with paranoia clouding your judgment! None of us would accept a sacrifice of a human life. To grow, {color=#f6d6bd}Beholder{/color} needs ne our souls, but rather any pneuma it can find.”
                '
                '(druidcave2 set)':
                    pass
        else:
            menu:
                'He gestures for you to stop. “None of us would accept a sacrifice of a human life. To grow, {color=#f6d6bd}Beholder{/color} needs ne our souls, but rather any pneuma it can find. Your judgment is ne needed here.”
                '
                '(druidcave2 set)':
                    pass

    label druidcave_druid_about_plague01i: #“Maybe it’s time to ask the druids from the village to help me. I’m sure they could spare some of their pneuma.”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe it’s time to ask the druids from the village to help me. I’m sure they could spare some of their pneuma.”')
        $ druidcave_druid_about_plague01i = 1
        $ questionpreset = "druidcave2"
        menu:
            'He puts his hands on his sides and looks at the clouds above him. “If they were willing to help you, they would ne send you here, at least ne all by yourself. They stare into the promises of power en the fears that such promises bring. For them, losing pneuma is a risk. You must understand that {color=#f6d6bd}Old Págos{/color} is ne friend of theirs, as it bows to The Wright, the creature that laughs when we wither. Many people would ne spare a tear for this place, en would much prefer it to turn into a house for boars en rooks.”
            '
            '(druidcave2 set)':
                pass

    label druidcave_druid_about_plague01k: #“Do you have anything I could give to the altar?”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have anything I could give to the altar?”')
        $ druidcave_druid_about_plague01k = 1
        $ questionpreset = "druidcave2"
        if druidcave_druid_friendship < 2:
            menu:
                '“I have nae reason to believe your words. If you help these people, I’ll admit I was wrong. But I will ne give you anything.”
                '
                '(druidcave2 set)':
                    pass
        elif (druidcave_druid_friendship+appearance_charisma) < 6:
            $ item_spiritrock += 1
            $ renpy.notify("You received a spirit rock.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a spirit rock.{/i}')
            menu:
                'He reaches into a pouch that was previously hanging from his neck. “I do ne know you en I can ne trust you. But if ‘tis this or the death of dozens of souls, I have nae choice. Here.”
                \n\nAs he reaches out, you see a flat, blueish pebble lying on his open palm. You could go to any stream and find hundreds of rocks like this one.
                \n\n“‘Tis a gift I received a few years back. A rock filled with pneuma by {color=#f6d6bd}Eudocia{/color}, the enchantress. Once put in one’s mouth, it brings back the strength of one’s exhausted pneuma. Or kills you, if you’re ne a spellcaster. Put it on the altar en it will help you feed it.”
                '
                '(druidcave2 set)':
                    pass
        else:
            $ item_spiritrock += 1
            $ renpy.notify("You received a spirit rock.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a spirit rock.{/i}')
            menu:
                'His blue eyes are kind. He reaches into a pouch that was previously hanging from his neck. “I ca ne say I trust you, but I want to believe you’ll prove to be honest. Take this.”
                \n\nAs he reaches out, you see a flat, blueish pebble lying on his open palm. You could go to any stream and find hundreds of rocks like this one.
                \n\n“‘Tis a gift I received a few years back. A rock filled with pneuma by {color=#f6d6bd}Eudocia{/color}, the enchantress. Once put in one’s mouth, it brings back the strength of one’s exhausted pneuma. Or kills you, if you’re ne a spellcaster. Put it on the altar en it will help you feed it.”
                '
                '(druidcave2 set)':
                    pass

    label druidcave_druid_about_plague01j: #“What will I get in return for all this trouble?”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I get in return for all this trouble?”')
        $ druidcave_druid_about_plague01j = 1
        $ questionpreset = "druidcave2"
        menu:
            'He looks toward a brown rat that wanders near the rocks, looking for seeds. “Who can tell? I hold nae treasures to share, en I’ll do my part ne for a reward, but for ma belief that ‘tis the right thing to do. Maybe the monks keep something in a chest, in that disgusting temple of theirs?”
            '
            '(druidcave2 set)':
                pass

    label druidcave_druid_about_plague01z: #“Fine. I know everything I need.”
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I know everything I need.”')
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“If you say so, traveler. If you say so.”
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_plague02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have the... fruit that you told me about.”')
    $ druidcave_druid_about_plague02 = 1
    $ renpy.notify("Journal updated: Healing the Plague")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
    $ druidcave_druid_friendship += 3
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ item_magicfruit = 0
    $ achievement_magicfruit = "sacrificedfruit"
    if howlersdell_firsttime:
        $ quest_healingtheplague_description05 = "I gave away the seed. Whenever I’m ready, I should return to the druid no later than six hours before nightfall, so we can together travel to {color=#f6d6bd}Old Págos{/color} and back."
        $ custom1 = "Return to me once you’re ready to take me to {color=#f6d6bd}Old Págos{/color} en back, but ne later than the early afternoon. I may help us push away the wild animals, but I’ll be too weak to protect us from the creatures of the night. We need maybe even six hours."
    else:
        $ quest_healingtheplague_description05alt = "I gave away the seed. I now need to visit the village of {color=#f6d6bd}Howler’s Dell{/color}, so we can safely pass through it. Whenever I’m ready, I should return to the druid no later than six hours before nightfall, so we can travel together to {color=#f6d6bd}Old Págos{/color} and back."
        $ custom1 = "I know that you have ne been to {color=#f6d6bd}Howler’s Dell{/color} yet. Do it now, to make sure the villagers will let you ride through. Return to me once you’re ready to take me to {color=#f6d6bd}Old Págos{/color} en back, but ne later than the early afternoon. I may help us push away the wild animals, but I’ll be too weak to protect us from the creatures of the night. We need maybe even six hours."
    $ questionpreset = "druidcave1"
    menu:
        'He straightens up and takes the fruit gently, then carries it to the cave. When he returns, he bows his head to you. “I’m astonished, traveler. I am. It must have taken a lot, but we’re almost done with it. [custom1]”
        '
        '(druidcave1 set)':
            pass

    label druidcave_druid_about_plague02instant:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pull out the weird fruit from my bag. “Guess what I found!”')
        $ druidcave_druid_about_plague02 = 1
        $ renpy.notify("Journal updated: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ druidcave_druid_friendship += 4
        $ item_magicfruit = 0
        if howlersdell_firsttime:
            $ quest_healingtheplague_description05 = "I gave away the seed. Whenever I’m ready, I should return to the druid at least six hours before the dusk, so we can travel together to {color=#f6d6bd}Old Págos{/color} and back."
            $ custom1 = "Return to me once you’re ready to take me to {color=#f6d6bd}Old Págos{/color} en back, but ne later than the early afternoon. I may help us push away the wild animals, but I’ll be too weak to protect us from the creatures of the night."
        else:
            $ quest_healingtheplague_description05alt = "I gave away the seed. I now need to visit the village of {color=#f6d6bd}Howler’s Dell{/color}, so we can easily pass through it. Whenever I’m ready, I should return to the druid at least six hours before the dusk, so we can travel together to {color=#f6d6bd}Old Págos{/color} and back."
            $ custom1 = "I know that you have ne been to {color=#f6d6bd}Howler’s Dell{/color} yet. Do it now, to make sure the villagers will let you ride through. Return to me once you’re ready to take me to {color=#f6d6bd}Old Págos{/color} en back, but ne later than the early afternoon. I may help us push away the wild animals, but I’ll be too weak to protect us from the creatures of the night. We need maybe even six hours."
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“Wha...” He stutters, holds his breath, then chuckles quietly. “Just like that, you’ve awoken our holy totem, yet you’ve resisted the temptation of its Seed?”
            \n\nHe straightens up and takes the fruit gently, then carries it to the cave. When he returns, he bows his head to you. “I’m astonished, traveler. I am. It must have taken a lot, but we’re almost done with it. [custom1]”
            '
            '(druidcave1 set)':
                pass

    label druidcave_druid_about_plague02fail:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve eaten the fruit. Will the tree bear another one?”')
        $ druidcave_druid_about_plague02 = 1
        $ quest_healingtheplague = 3
        $ quest_healingtheplague_description07 = "The village will have to take care of itself without my help."
        $ renpy.notify("Quest completed: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ druidcave_druid_friendship -= 4
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He looks away, with a sad smile on his chapped lips. “Just as I expected. A better soul would be tempted by it. Nae. The’s nae other way.”
            '
            '(druidcave1 set)':
                pass

    label druidcave_druid_about_plague02failalt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve lost the fruit. Will the tree bear another one?”')
        $ druidcave_druid_about_plague02 = 1
        $ quest_healingtheplague = 3
        $ quest_healingtheplague_description07 = "The village will have to take care of itself without my help."
        $ renpy.notify("Quest completed: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ druidcave_druid_friendship -= 4
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He looks away, with a sad smile on his chapped lips. “Just as I expected. An idiot, or a slave to human masters. Nae. The’s nae other way.”
            '
            '(druidcave1 set)':
                pass

    label druidcave_druid_about_plague02failinstant:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually... I’ve already eaten this... Fruit. Is there maybe some other way?”')
        $ druidcave_druid_about_plague02 = 1
        $ quest_healingtheplague = 3
        $ quest_healingtheplague_description07 = "The village will have to take care of itself without my help."
        $ renpy.notify("Quest completed: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ druidcave_druid_friendship -= 4
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“Wha...” He stutters, holds his breath, then chuckles quietly. “So you awoke a powerful totem, en just ate its fruit, with nae regard for your safety?”
            \n\nHe then looks away, with a sad smile on his chapped lips. “Tha’s ne a surprise. A better soul would be tempted by it. Nae. The’s nae other way.”
            '
            '(druidcave1 set)':
                pass

    label druidcave_druid_about_plague02failinstantalt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually... I’ve already lost this... Fruit. Is there maybe some other way?”')
        $ druidcave_druid_about_plague02 = 1
        $ quest_healingtheplague = 3
        $ quest_healingtheplague_description07 = "The village will have to take care of itself without my help."
        $ renpy.notify("Quest completed: Healing the Plague")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Healing the Plague{/i}')
        $ druidcave_druid_friendship -= 4
        $ questionpreset = "druidcave1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“Wha...” He stutters, holds his breath, then chuckles quietly. “So you awoke a powerful totem, en just {i}lost{/i} its fruit? What did you do with it, give it away for a mug of ale en someone to keep your bed warm?”
            \n\nHe then looks away, with a sad smile on his chapped lips. “Tha’s ne a surprise. You’re an idiot, or a slave to human masters. Nae. The’s nae other way.”
            '
            '(druidcave1 set)':
                pass

label druidcave_druid_about_plague03ALL:
    label druidcave_druid_about_plague03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to take you to {color=#f6d6bd}Old Págos{/color}.”')
        $ druidcave_druid_about_plague_travel = 1
        $ questionpreset = 0
        label druidcave_druid_about_plague03after:
            menu:
                'Without a word, he walks through the metal door and leaves you alone for a few minutes. Once he returns, he holds a red staff and a linen bag, which he gives to you. “I’m old. You’ll carry it,” he states matter-of-factly. He’s changed into similar pants and a tunic, but their greens, blues, and reds are lively. You don’t see any stitches or patches. Still, he looks like an old commandant, not a priest.
                \n\nAs you lead {color=#f6d6bd}[horsename]{/color} down the path, there isn’t much of an opportunity to speak with the old druid. He looks around, observes the plants and the sky, but hardly ever glances toward you, and never for long enough to have a chance to read your lips.
                '
                'I follow him north.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him north.')
                    $ travel_destination = "howlersdell"
                    jump finaldestinationafterevent

    label druidcave_druid_about_plague03b:
        show areapicture howlersdellfull at basicfade behind druidcavebronzerod
        $ howlersdell_reputation += 1
        $ quarters += 2
        if description_druids07:
            $ custom1 = "Elpis"
        else:
            $ custom1 = "The pale leader of the local druids"
        $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'The locals drop their tools and head to the road, observing your approach anxiously and bowing to the elder. The commotion spreads to the other side of the wall as the villagers call their friends and families to gather around. Behind the open gates you’re welcomed by a tunnel of onlookers.
            \n\nThe druid raises his hand and waves to no one in particular. He moves forward silently, not interested in what he sees. Once you get to the fruit-bearing trees, you turn right. Crossing the bridge is not easy for an old man, but he doesn’t ask anyone to hold him, instead putting his weight on the staff and taking slow steps forward.
            \n\nThe welcoming committee awaits you on the islet. {color=#f6d6bd}The druids{/color} are gathered on one side, while a group of elders are on the other. {color=#f6d6bd}Thais{/color} stands in your way, right before the second bridge. When you reach her, there’s a long silence.
            '
            'I let them play out their games.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let them play out their games.')
                jump druidcave_druid_about_plague03c
            '“Let us be. What we do here is unrelated to you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let us be. What we do here is unrelated to you.”')
                jump druidcave_druid_about_plague03d

    label druidcave_druid_about_plague03c: # let them play out their games.
        menu:
            '{color=#f6d6bd}The mayor{/color} welcomes the elder with a nod. “We’re honored to see your arrival, forest speaker. I hope you do ne want to leave us already!” She puts her right hand on her chest and chillingly titters. There’s no trace of her {i}city{/i} accent.
            \n\n{color=#f6d6bd}The elder’s{/color} tone is both firm and polite. “I’m ne here. If there had been another path I could take, I would.” He looks around, observing the nearby faces. “I’m glad to see you in good health! This place does ne need me. En thanks to this stranger, I can reach the people in great misfortune. Good day!”
            \n\n{color=#f6d6bd}[custom1]{/color} steps forward, with fingers clenched around her staff. “Beholder has been awoken. Our people have the right to its Seed. You’re robbing us of a fruit for which we’ve been waiting since spring.” Her cadence is indistinguishable from your companion’s, and you notice their staffs have an identical length.
            '
            'I don’t intervene.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t intervene.')
                jump druidcave_druid_about_plague03e
            '“I’ve made the sacrifice. It belongs to me. And I get to decide.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve made the sacrifice. It belongs to me. And I get to decide.”')
                jump druidcave_druid_about_plague03f

    label druidcave_druid_about_plague03d: #“Let us be. What we do here is unrelated to you.”
        $ thais_friendship -= 1
        $ druidcave_druid_friendship += 1
        menu:
            '{color=#f6d6bd}The mayor’s{/color} eyes are filled with anger, yet her tone remains calm. “We do ne wish to bother any of you. Quite the opposite, roadwarden, ‘tis a great day for our village. The forest speaker has visited us again, after so many years! I hope the news you’re bringing are delightful!” She raises her head and chillingly titters. There’s no trace of her {i}city{/i} accent.
            \n\n{color=#f6d6bd}The elder’s{/color} tone is both firm and polite. “I have nae more words for any of you. If there had been another path I could take, I would.” He looks around slowly, observing the nearby faces. “I’m glad to see you in good health! This place does ne need me. En thanks to [pcname], I can reach the people in great misfortune.” He puts his free hand on your shoulder.
            \n\n{color=#f6d6bd}[custom1]{/color} steps forward, with fingers clenched around her staff. “Beholder has been awoken. Our people have the right to its Seed. You’re robbing us of a fruit for which we’ve been waiting since spring.” Her cadence is indistinguishable from your companion’s, and you notice their staffs have an identical length.
            '
            'I don’t intervene.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t intervene.')
                jump druidcave_druid_about_plague03e
            '“It belongs to me. I’ve made the sacrifice and I get to decide.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It belongs to me. I’ve made the sacrifice and I get to decide.”')
                jump druidcave_druid_about_plague03f

    label druidcave_druid_about_plague03e: #I don’t intervene.
        menu:
            'The elder responds without looking in her direction. “To think you would dare to claim our holy totem as your belonging! Your soul is marked with corruption!” As he points at her with his staff, his hand is shaking. “‘Twas the roadwarden who awoke the swamp spirit through true sacrifices, something that your soft beds and colorful clothing have made you forget about!” {color=#f6d6bd}The man{/color} sounds like a disappointed teacher, and you realize he has {i}heard{/i} the druidess voice without looking at her lips. “You who believe you {i}deserve{/i} the Seed do ne understand who you are, how lost you are!” He moves his staff around, pointing at various faces.
            \n\nHe wants to move forward, but {color=#f6d6bd}the mayor{/color} puts hands on her sides. In her eyes you see an unfamiliar glimpse of fear. “You’ve already eaten the Seed once, oh speaker. Do ne make us use force.”
            '
            'He knows what he’s doing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He knows what he’s doing.')
                jump druidcave_druid_about_plague03g
            '“There’s no need for violence. Don’t push us into it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s no need for violence. Don’t push us into it.”')
                jump druidcave_druid_about_plague03h

    label druidcave_druid_about_plague03f: #“It belongs to me. I’ve made the sacrifice and I get to decide.”
        $ howlersdell_elpis_friendship -= 1
        $ druidcave_druid_friendship += 1
        $ description_druids07 = "The leader of the druids from {color=#f6d6bd}Howler’s Dell{/color} is known as {color=#f6d6bd}Elpis{/color}, though she rarely uses this name."
        menu:
            '“En this stranger has chosen what none of you is brave enough to do!” {color=#f6d6bd}The man{/color} sounds like a disappointed teacher, and you realize he has {i}heard{/i} the druidess voice without looking at her lips. “Eva you, {color=#f6d6bd}Elpis{/color}!” He points at the pale druidess with his staff. His hand is shaking. “To think you would dare to claim our holy totem as your belonging! Your soul is marked with corruption!” He looks around. “You who believe you {i}deserve{/i} the Seed do ne understand who you are, how lost you are!” He moves his staff around, pointing at various faces.
            \n\nHe wants to move forward, but {color=#f6d6bd}the mayor{/color} puts hands on her sides. In her eyes you see an unfamiliar glimpse of fear. “You’ve already eaten the Seed once, oh speaker. Do ne make us use force.”
            '
            'He knows what he’s doing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He knows what he’s doing.')
                jump druidcave_druid_about_plague03g
            '“There’s no need for violence. Don’t push us into it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s no need for violence. Don’t push us into it.”')
                jump druidcave_druid_about_plague03h

    label druidcave_druid_about_plague03g: #He knows what he’s doing.
        menu:
            'A good minute passes by before {color=#f6d6bd}the elder{/color} speaks again. “Ma wife welcomed you to this world, {color=#f6d6bd}Thais{/color}. I maself voted to use the Seed to heal your weak bones. I can ne believe you have fallen so far. Our journey illuminates, nae doubt. You’re but a brigand.” Only you can hear his sigh. “Enough of this. Begone.”
            \n\nHe doesn’t wait any longer. He steps forward and the mayor gets out of your way, observing the two of you with fear and fury. You cross the bridge, then the open gate. The man returns to silence, but his back is bowed, shoulders drooping.
            '
            'We’re almost there.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We’re almost there.')
                $ travel_destination = "oldpagos"
                $ quarters += 1
                jump finaldestination

    label druidcave_druid_about_plague03h: #“There’s no need for violence. Don’t push us into it.”
        $ thais_friendship -= 1
        $ druidcave_druid_friendship += 1
        menu:
            '{color=#f6d6bd}The elder{/color} scoffs. “I would sooner turn maself into a pike en swim down the stream to drop the Seed into the swamps than let you rob the one who has followed our traditions. The roadwarden did so in the name of what’s right, en I believe it with my whole soul!” His voice raises. “One year. After everything I’ve done for you, I’m taking away but one year of prayers, yet you still fight. What a pathetic day.”
            \n\nHe doesn’t wait any longer. He steps forward and the mayor gets out of your way, observing the two of you with shame and fury. You cross the bridge, then the open gate. The man returns to silence, but his back is bowed, shoulders drooping.
            '
            'We’re almost there.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We’re almost there.')
                $ travel_destination = "oldpagos"
                $ quarters += 1
                jump finaldestination

    label druidcave_druid_about_plague04:
        menu:
            'The hills are bright and colorful. The tall grasses and flowers dance with the wind, unaware of the countless grasshoppers, butterflies, and mice that romp and prey among them. Dark green birds are circling above the walls and cliffs, arguing in tongues unknown to humans. With every breath you take in the summer in its dusk, the drying ground and the promise of rainfalls, as well as the pinching smoke coming from the funeral pyre set in the center of the village, cutting the horizon like a column weaved from shadows.
            \n\nAs time goes on, the old man’s walking pace slows down, observing the lands around you with great interest. His keen eyes stop on trees, bushes, and flowers, though it’s the crops on the plateau that make him stop for a bit.
            \n\nAfter a minute or two, he speaks. “The plants want to fall, they need nae more than two rains. The farmers need to come out right after dawn.”
            \n\nHe doesn’t look at your lips, just turns around and approaches the second ascent, once again slowing down to climb it without your help.
            '
            'I tether {color=#f6d6bd}[horsename]{/color} to the fence so it can graze on the meadow.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to the fence so it can graze on the meadow.' %horsename)
                jump druidcave_druid_about_plague04a

    label druidcave_druid_about_plague04a:
        menu:
            'The man awaits at the gate and reaches out to you. You give him the bag that he gave you back at his shelter. “You do ne have to stay away, but it will ne be pleasant,” he sighs. “I’ll come out soon en we’ll leave this place right away. The village may be cured, but that does ne mean that the plague is cleansed. We can still be infected.”
            \n\nHe raises his red staff and uses it to knock on the gate. You don’t wait long for the dark-eyed woman to open the peephole. This time, there are not that many people around her.
            \n\n“Let me in,” says the druid. The peephole closes right away. After a few loud minutes of moving the wooden bars, the gate opens slightly. You have a couple of moments to look around - the few buildings you notice are unlike anything you’ve seen in this province, made of materials that resemble the rock faces seen on this very hill, with tiled roofs and stone walls.
            \n\nThe gate closes gently.
            '
            'I stay near the gate.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay near the gate.')
                $ pc_hp = limit_pc_hp(pc_hp+1)
                show plus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ oldpagos_cured = 1
                $ creeks_reasonstojoin_healedtheplague += 1
                $ oldpagos_reputation += 10
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 2
                    $ renpy.notify("Journal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                elif pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 3
                    $ renpy.notify("Journal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                else:
                    $ renpy.notify("Journal updated: Explore the Peninsula")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ quest_explorepeninsula_description12a = "I’ve managed to take care of the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
                if pc_likeshorsename:
                    $ custom1 = "and put a hand on its side. It blows air of its nose, noticing your attention, but is way too focused on chewing to raise its head."
                else:
                    $ custom1 = "and examine your equipment and all the nodes that attach it to the saddle and traveling sacks."
                menu:
                    'You hear footsteps, voices, crying, heavy objects that are moved around. For a couple of moments, everything calms down, but then a sudden wind strikes you, pushing you away from the wall. Your skin tingles, then your shell convulses. Your stomach hurts, you want to spit out something that you can’t comprehend, like a dragon with a breath of pestilence.
                    \n\nThe feeling stops suddenly. You wipe the sweat from your forehead, feeling a weird relaxation in your limbs, a lethargy under your control, something you’d feel after a long training or a day of hard work. You take a deep breath and the wood, stone, smoke, ground, and grass spark a new sensation in your nose, some sort of sharpness that you hadn’t perceived before.
                    '
                    'I focus on regaining control over my shell.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on regaining control over my shell.')
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ quest_explorepeninsula_description12a = "I’ve managed to take care of the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
                        show areapicture oldpagosscrap04 at basicfade behind druidcavebronzerod
                        menu:
                            'Only now do you notice that the gate is open, and that the old man is right next to you, kneeling, leaning forward, breathing heavily. He opens his bag, pulling out the weird fruit that you gave him. With shaking hands, he detaches the first “slice” of its skin, but before you take a good look at it, it turns into a gray powder and slips through the man’s fingers. The rest of the fruit follows its example, covering the soil with an ash-like dust.
                            \n\nThe thing that remains resembles yet another fruit, or a cherry-sized seed, levitating in the middle of a floral “rib-cage.” The man observes it for a few breaths, then reaches for it with two fingers, squishing it softly, and puts it into his mouth.
                            \n\nDuring the next minute he gets up, grins at you, dusts off his knees, and takes a few steps forward, which turn into dance-like skipping. He then descends from the hill, without a word.
                            \n\nYou hear the joyful calls of the villagers. Their hysterical laughter and names screamed at the sky, welcoming those that have awoken after a long dream.
                            '
                            'I prepare my horse and follow the druid.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my horse and follow the druid.')
                                $ travel_destination = "druidcave"
                                $ quarters += 2
                                jump finaldestination
            'I walk away to have a better look.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away to have a better look.')
                $ oldpagos_cured = 1
                $ creeks_reasonstojoin_healedtheplague += 1
                $ oldpagos_reputation += 10
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 2
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Journal updated: Explore the Peninsula,\n%s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula, %s{/i}' %quest_pc_goal_name)
                elif pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 3
                    $ renpy.notify("Journal updated: Explore the Peninsula")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                else:
                    $ renpy.notify("Journal updated: Explore the Peninsula")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ quest_explorepeninsula_description12a = "I’ve managed to take care of the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
                if pc_likeshorsename:
                    $ custom1 = "and put a hand on its side. It blows air from its nose, noticing your attention, but is way too focused on chewing to raise its head."
                else:
                    $ custom1 = "and examine your equipment and all the nodes that attach it to the saddle and traveling sacks."
                menu:
                    'You return to your mount [custom1] The only sounds come from the grass, insects, birds. Suddenly, you notice a beam of green light coming from the village, as well as a strong gust of wind that ends in a complete silence.
                    \n\nThe druid staggers out through the gate, exhausted.
                    '
                    'I walk to him.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk to him.')
                        $ druidcave_druid_friendship += 1
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ quest_explorepeninsula_description12a = "I’ve managed to take care of the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
                        show areapicture oldpagosscrap04 at basicfade behind druidcavebronzerod
                        menu:
                            'When he sees your steps, he gestures for you to stop, with a weak smile hidden in the corners of his eyes. He kneels and leans forward, breathing heavily. He opens his bag, pulling out the weird fruit that you gave him. With shaking hands, he detaches the first “slice” of its skin, but before you take a good look at it, it turns into a gray powder and slips through the man’s fingers. The rest of the fruit follows its example, covering the soil with an ash-like dust.
                            \n\nThe thing that remains resembles yet another fruit, or a cherry-sized seed, levitating in the middle of a floral “rib-cage.” The man observes it for a few breaths, then reaches for it with two fingers, squishing it softly, and puts it into his mouth.
                            \n\nDuring the next minute he gets up, grins at you, dusts off his knees, and takes a few steps forward, which turn into dance-like skipping. He then descends from the hill, without a word.
                            \n\nYou hear the joyful calls of the villagers. Their hysterical laughter and names screamed at the sky, welcoming those that have awoken after a long dream.
                            '
                            'I prepare my horse and follow the druid.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my horse and follow the druid.')
                                $ travel_destination = "druidcave"
                                $ quarters += 2
                                jump finaldestination
                    'I stay away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay away.')
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ quest_explorepeninsula_description12a = "I’ve managed to take care of the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
                        show areapicture oldpagosscrap04 at basicfade behind druidcavebronzerod
                        menu:
                            'He takes a few more steps, then falls down on his side, breathing heavily. He opens his bag, pulling out the weird fruit that you gave him. With shaking hands, he detaches the first “slice” of its skin, but before you take a good look at it, it turns into a gray powder and slips through the man’s fingers. The rest of the fruit follows its example, covering the soil with an ash-like dust.
                            \n\nThe thing that remains resembles yet another fruit, or a cherry-sized seed, levitating in the middle of a floral “rib-cage.” The man observes it for a few breaths, then reaches for it with two fingers, squishing it softly, and puts it into his mouth.
                            \n\nDuring the next minute he gets up, grins at you, dusts off his knees, and takes a few steps forward, which turn into dance-like skipping. He then descends from the hill, without a word.
                            \n\nYou hear the joyful calls of the villagers. Their hysterical laughter and names screamed at the sky, welcoming those that have awoken after a long dream.
                            '
                            'I prepare my horse and follow the druid.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my horse and follow the druid.')
                                $ travel_destination = "druidcave"
                                $ quarters += 2
                                jump finaldestination

label druidcavereturningfromoldpagos01:
    $ druidcave_druid_about_plague_travel = 0
    $ druidcave_druid_friendship += 2
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'You help the man dismount, realizing how light he actually is. Holding your shoulder, he points at the bench near the spring. You help him sit down and place his staff and bag nearby. He’s smiling, covered by sunbeams, stretching out his legs, leaning back to rest on the warm rocks.
        \n\n“We’ve done a good job,” he says quietly, but clearly. “Now all we can do is hope they’ll stop cutting down the trees before the wild creatures push them into the sea.” After a moment, he opens his eyes and looks at your lips.
        '
        '“Thank you for your assistance.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for your assistance.”')
            $ renpy.notify("Quest completed: Healing the Plague")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Healing the Plague{/i}')
            $ quest_healingtheplague = 2
            $ quest_healingtheplague_description08 = "The village is still under quarantine, but it should regain its strength before winter."
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                '“En I thank you. ‘Tis one of those strange things that make us different from so many creatures. We may ne belong to a single pack, yet we’ve joined our strength, pursued the same goals.” He looks at his small garden. “Saved the lives of others, just because we could. Our souls do make me wonder.”
                \n\nHe sighs. “I want to get some sleep. If you need anything before you leave, now is the time.”
                '
                '(druidcave1 set)':
                    pass
        '“I’m still not sure why you decided to aid them. They’re not your allies.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still not sure why you decided to aid them. They’re not your allies.”')
            $ renpy.notify("Quest completed: Healing the Plague")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Healing the Plague{/i}')
            $ quest_healingtheplague = 2
            $ quest_healingtheplague_description08 = "The village is still under quarantine, but it should regain its strength before winter."
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                '“For the same reason why I agreed to speak with you in the first place. I have seen too much to divide people into {i}us{/i} en {i}them{/i}. All these games push us away from the things that we need en lure us into gathering, eating, possessing, just so we can have more than the others, be stronger than them, be ready to fight them off. The village we saved is enslaved by its god, true, but not more than ma people are enslaved by their vanity. They deserve our help, just as a bear deserves its food, though it doesn’t mean you should hug it.”
                \n\nHe sighs. “I want to get some sleep. If you need anything before you leave, now is the time.”
                '
                '(druidcave1 set)':
                    pass
        'I remain silent.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remain silent.')
            $ renpy.notify("Quest completed: Healing the Plague")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Healing the Plague{/i}')
            $ quest_healingtheplague = 2
            $ quest_healingtheplague_description08 = "The village is still under quarantine, but it should regain its strength before winter."
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "druidcave1"
            menu:
                '“I want to get some sleep. If you need anything before you leave, now is the time.”
                '
                '(druidcave1 set)':
                    pass
