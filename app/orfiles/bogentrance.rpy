# ###################### BOG ENTRANCE
default bogentrance_firsttime = 0
default bogentrance_fluff = ""
default bogentrance_fluff_old = ""

default bogentrance_wildplants_left = 0
default bogentrance_wildplants_howmanytimes = 0
default bogentrance_wildplants_taken = 0
default bogentrance_wildplants_threshold1 = 0
default bogentrance_wildplants_threshold2 = 0
default bogentrance_wildplants_threshold3 = 0
default bogentrance_wildplants_threshold4 = 0
default bogentrance_wildplants_threshold5 = 0

default bogentrance_dialogue_maxquestions = 0 # how many can be asked by player
default bogentrance_dialogue_askedquestions = 0 # how many were asked
default bogentrance_dialogue_friendship = 0 # whitemarshes_reputation

default bogentrance_dialogue_guesses = 0
default bogentrance_dialogue_about_themselves = 0
default bogentrance_dialogue_about_findingwhitemarshes = 0
default bogentrance_dialogue_about_whitemarshes = 0
default bogentrance_dialogue_about_cart = 0
default bogentrance_dialogue_about_trade = 0
default bogentrance_dialogue_about_asterion = 0
default bogentrance_dialogue_about_area = 0
default bogentrance_dialogue_about_undead = 0
default bogentrance_dialogue_about_hoodedperson = 0
default bogentrance_dialogue_about_missinghunters = 0

default bogentrance_whitemarshes_destroyed = 0

label bogentrance01:
    nvl clear
    $ pc_area = "bogentrance"
    show areapicture bogentrance01 at basicfade
    label bogentrance_fluffloop:
        $ bogentrance_fluff = ""
        $ bogentrance_fluff = renpy.random.choice(['The sparse trees and shrubs grow strong, but there are no fruits left, only bird nests among the branches, and leftovers spread in the short grass.', 'A small group of roe notices your arrival. The largest one sounds a bark-like warning. At once, all of them hurry away, heading west.', 'A falcon rests on the broken signpost, but soars into the sky before you get closer. For a few minutes, it flies above you, maybe waiting for you to leave.', 'A fresh mold covers the abandoned cart, and as you get closer to it, a small mouse springs out of one of the boxes, disappearing between the blades of grass.'])
        if bogentrance_fluff_old == bogentrance_fluff:
            jump bogentrance_fluffloop
        else:
            $ bogentrance_fluff_old = bogentrance_fluff
    if day >= 25:
        if not bogentrance_wildplants_threshold1:
            $ bogentrance_wildplants_threshold1 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold2:
            $ bogentrance_wildplants_threshold2 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold3:
            $ bogentrance_wildplants_threshold3 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold4:
            $ bogentrance_wildplants_threshold4 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold5:
            $ bogentrance_wildplants_threshold5 = 1
            $ bogentrance_wildplants_left += 1
    elif day >= 20:
        if not bogentrance_wildplants_threshold1:
            $ bogentrance_wildplants_threshold1 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold2:
            $ bogentrance_wildplants_threshold2 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold3:
            $ bogentrance_wildplants_threshold3 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold4:
            $ bogentrance_wildplants_threshold4 = 1
            $ bogentrance_wildplants_left += 1
    elif day >= 15:
        if not bogentrance_wildplants_threshold1:
            $ bogentrance_wildplants_threshold1 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold2:
            $ bogentrance_wildplants_threshold2 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold3:
            $ bogentrance_wildplants_threshold3 = 1
            $ bogentrance_wildplants_left += 1
    elif day >= 10:
        if not bogentrance_wildplants_threshold1:
            $ bogentrance_wildplants_threshold1 = 1
            $ bogentrance_wildplants_left += 1
        if not bogentrance_wildplants_threshold2:
            $ bogentrance_wildplants_threshold2 = 1
            $ bogentrance_wildplants_left += 1
    elif day >= 5:
        if not bogentrance_wildplants_threshold1:
            $ bogentrance_wildplants_threshold1 = 1
            $ bogentrance_wildplants_left += 1
    if not bogentrance_firsttime:
        $ world_known_areas += 1
        $ bogentrance_firsttime = 1
        $ bogcrossroads_unlocked = 1
        $ ford_unlocked = 1
        $ ruinedshelter_unlocked = 1
        $ tutorial_bogdaylength = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        stop music fadeout 4.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump bogentrancefirsttime01
    elif bogentrance_whitemarshes_destroyed == 1:
        $ bogentrance_whitemarshes_destroyed = 2
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        stop music fadeout 4.0
        play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        jump bogentrance_whitemarshes_destroyed01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        stop music fadeout 4.0
        play nature "audio/ambient/bogentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump bogentranceregular01

label bogentranceregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if bogentrance_wildplants_left >= 5:
        $ custom1 = "There’s plenty of ripe fruits in sight, as well as berries and vegetables."
    elif bogentrance_wildplants_left == 4:
        $ custom1 = "There are many ripe fruits in sight, as well as berries and vegetables."
    elif bogentrance_wildplants_left == 3:
        $ custom1 = "There are quite a few ripe fruits in sight, as well as berries."
    elif bogentrance_wildplants_left == 2:
        $ custom1 = "There are quite a few ripe fruits in sight."
    elif bogentrance_wildplants_left == 1:
        $ custom1 = "There are some ripe fruits in sight."
    else:
        $ custom1 = "While there’s many edible plants in sight, they aren’t ready yet for picking."
    menu:
        '[bogentrance_fluff] [custom1]
        '
        'I could spend a few minutes foraging for wild plants.' if bogentrance_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend a few minutes foraging for wild plants.')
            jump bogentranceforaging01
        'I could spend half an hour foraging for wild plants.' if bogentrance_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend half an hour foraging for wild plants.')
            jump bogentranceforaging01
        'I could spend more than half an hour foraging for wild plants.' if bogentrance_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than half an hour foraging for wild plants.')
            jump bogentranceforaging01
        'I could spend an hour or so foraging for wild plants.' if bogentrance_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend an hour or so foraging for wild plants.')
            jump bogentranceforaging01
        'I could spend more than an hour foraging for wild plants.' if bogentrance_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than an hour foraging for wild plants.')
            jump bogentranceforaging01
        'After a few more days there may be fruits and other plants to pick here. (disabled)' if bogentrance_wildplants_left == 0:
            pass

label bogentrancefirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if not renpy.music.get_playing(channel='nature') == "audio/ambient/bogentrance01.ogg":
        play nature "audio/ambient/bogentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if quarters > (world_daylength-26):
        $ custom1 = ", carry lit lanterns"
    else:
        $ custom1 = ""
    menu:
        'The trees and bushes are sparse here, growing from the barren grassland. Some of them bear late-summer fruits.
        \n\nA group of wayfarers is spread around the broken signpost and the abandoned cart. They’re skinny, but healthy, and are standing upright. They’re wearing humble, dim gambesons on top of their hemp tunics and pants, all of them worn, in some cases undyed, while others are dark green or brown. Four of these individuals wear cloaks[custom1], and are armed with spears, bows, and stone maces. On their necks, wrists, and belts you spot small talismans - fangs, bones, wooden beads, leather straps.
        \n\nThere’s also the fifth figure, standing a bit in the back, with lowered shoulders. Unlike the others, they’re hooded, and in such a manner that you doubt they can see anything other than their boots. Their clothes are shabby, torn, but your eyes mostly run to their “club” - a bough as long as its owner is tall and as thick as a leg, resting with one end on the ground. You get closer, and the person raises the weapon with just one arm, but another traveler gestures for them to stop - and they do so right away, freezing in place.
        '
        'I stay in the saddle, just in case.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay in the saddle, just in case.')
            if quarters <= 40:
                $ custom1 = "Safe travels, stranger. T’may be early, ba bogs aren’t safe. Betta keep moving, you’ll find’a inn."
            elif quarters < (world_daylength-20):
                $ custom1 = "Safe travels, stranger. T’may still be time before the evenfall, ba bogs aren’t safe. Betta keep moving, you’ll find’a inn."
            else: # late
                $ custom1 = "Bogs aren’t safe for us, ba even less’a stranger. T’s evenfall, an’ far from roofs. Betta keep moving, you’ll find’a inn soon."
            if quarters > (world_daylength-26):
                $ custom2 = ", holding his lantern high in the air"
            else:
                $ custom2 = ""
            $ tutorial_bogdaylength = 2
            $ at_activate = 1
            $ at = 0
            menu:
                'The man behind the gesture doesn’t approach you, just nods. “[custom1]”
                \n\nYou try to digest his thick accent. He’s broad-shouldered, with a large belly, but the scars on his face sculpt an image of someone who’s earned their share of food with many skirmishes. He doesn’t reach for his weapon, and pushes one of his companions closer to the cart. She kneels by an empty box and looks inside it.
                \n\nThe man observes you with little curiosity[custom2].
                '
                ' (disabled)' ( condition="at == 0" ):
                    pass
                'I nod at their cart. “Need any help?”' ( condition="at == 'friendly'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I nod at their cart. “Need any help?”')
                    $ at_activate = 0
                    $ at = 0
                    jump bogentrancefirsttime02friendly
                '“Nice place for a camp. The air is a bit smelly, though.”' ( condition="at == 'playful'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Nice place for a camp. The air is a bit smelly, though.”')
                    $ at_activate = 0
                    $ at = 0
                    jump bogentrancefirsttime02playful
                '“Greetings.”' ( condition="at == 'distanced'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “Greetings.”')
                    $ at_activate = 0
                    $ at = 0
                    jump bogentrancefirsttime02distanced
                'I look at the gigantic club. “Hold your weapons close, if it makes you feel safer.” I show them my own blade. “I don’t mind.”' ( condition="at == 'intimidating'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I look at the gigantic club. “Hold your weapons close, if it makes you feel safer.” I show them my own blade. “I don’t mind.”')
                    $ at_activate = 0
                    $ at = 0
                    jump bogentrancefirsttime02intimidating
                'I sigh. “I’m just glad you’re not highwaymen.”' ( condition="at == 'vulnerable'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I sigh. “I’m just glad you’re not highwaymen.”')
                    $ at_activate = 0
                    $ at = 0
                    jump bogentrancefirsttime02vulnerable
    label bogentrancefirsttime02friendly: # I nod at their cart. “Need any help?”
        $ bogentrance_dialogue_maxquestions = 4
        $ questionpreset = "bogentrance"
        menu:
            'He makes an annoyed grimace. “Not really. T’s timber’s sickening, moldy an’ wet. We’re checking on the place, ba seems t’s’a bad year for it.”
            \n\nHe looks at his companions, who simply shrug and spread to take a look at the cart - all but the one with the bough, who doesn’t move an inch. “I canna say I’ve time to loaf. You’ve questions, ask, ba be quick. Don’t put us to sleep.”
            '
            '(bogentrance preset)':
                pass
    label bogentrancefirsttime02playful: # “Nice place to make a camp. The air is a bit smelly, though.”
        $ bogentrance_dialogue_maxquestions = 3
        $ bogentrance_dialogue_friendship -= 1
        $ questionpreset = "bogentrance"
        menu:
            'He gives you a piercing look. “Stupid talk, no soul makes a fire here. An’ t’s not so bad, the air. Means the woods breathe, grow. Wad be a bad year without the smells.”
            \n\nHe looks at his companions, who simply shrug and spread to take a look at the cart - all but the one with the bough, who doesn’t move an inch. “I’ve no time to loaf, an’ no patience to bother. You need something, be quick.”
            '
            '(bogentrance preset)':
                pass
    label bogentrancefirsttime02distanced: # “Greetings.”
        $ bogentrance_dialogue_maxquestions = 4
        $ questionpreset = "bogentrance"
        menu:
            'He gives you a slightly deeper nod this time, then looks at his companions, who simply shrug and spread to take a look at the cart - all but the one with the bough, who doesn’t move an inch. “I canna say I’ve time to loaf. You’ve questions, ask, ba be quick. Don’t put us to sleep.”
            '
            '(bogentrance preset)':
                pass
    label bogentrancefirsttime02intimidating: #I look at the gigantic club. “Hold your weapons close, if it makes you feel safer.” I show them my own blade. “I don’t c.”
        $ bogentrance_dialogue_friendship += 1
        $ bogentrance_dialogue_maxquestions = 5
        $ questionpreset = "bogentrance"
        menu:
            'He lets out a timid chuckle, then a light bow. “I cherish your goodwill.” He looks at his companions, who observe you with gentle smiles, and commands them to take a look at the cart. They spread, all but the one with the bough, who doesn’t move an inch.
            \n\nThe man takes two steps closer, but stops after {color=#f6d6bd}[horsename]’s{/color} snort. “Don’t worry, big one,” he reassures your mount, then looks at you again. “I canna say I’ve time to loaf, ba you’ve questions, ask, just be quick.”
            '
            '(bogentrance preset)':
                pass
    label bogentrancefirsttime02vulnerable: # I sigh. “I’m just glad you’re not highwaymen.”
        $ bogentrance_dialogue_friendship -= 1
        $ bogentrance_dialogue_maxquestions = 2
        $ questionpreset = "bogentrance"
        menu:
            'He scoffs. “You’re breathing, so t’s obvious. The’re robbers on this land, ba you think the’re going to talk on the weather? If you canna handle them alone, then stay with’a group.”
            \n\nHe looks at his companions, who smirk back at him, then spread to take a look at the cart - all but the one with the bough, who doesn’t move an inch. “I’ve no time to loaf, an’ no patience to bother. You need something, be quick.”
            '
            '(bogentrance preset)':
                pass

label bogentrancefirsttimequestions:
    label bogentrance_dialogue_about_themselves01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you from around here?”')
        $ bogentrance_dialogue_about_themselves = 1
        menu:
            '“Very much so! An’ you’re new to these roads? You know our home?”
            '
            '“Maybe...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe...”')
                $ bogentrance_dialogue_guesses += 1
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                $ tutorial_input = 2
                jump bogentrance_dialogue_about_themselves02
            '“No clue.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears of strangers, specially these days.”"
                jump bogentranceafterquestion01
    label bogentrance_dialogue_about_themselves02:
        if search == "whitemarshes" or search == "hwitemarshes" or search == "thewhitemarshes":
            $ bogentrance_dialogue_friendship += 1
            $ custom1 = "He straightens up. “True! T’s there,” he looks at the crossroad leading east. “I thought t’s already forgotten, ba you’ve a clean ear.”"
            jump bogentranceafterquestion01
        elif search == "whitemarsh" or search == "hwitemarsh" or search == "thewhitemarsh" or search == "whitebogs" or search == "hwitebogs" or search == "thewhitebogs" or search == "whiteswamps" or search == "hwiteswamps" or search == "thewhiteswamps":
            $ bogentrance_dialogue_friendship += 1
            $ custom1 = "“Almost,” laughs one of his companions. He also smiles. “{color=#f6d6bd}White Marshes{/color}, more like. T’s there,” he looks at the crossroad leading east. “I thought t’s already forgotten, ba you’ve a clean ear.”"
            jump bogentranceafterquestion01
        #############################
        elif search == "creeks" or search == "thecreeks" or search == "galerocks" or search == "thegalerocks" or search == "peltnorth" or search == "thepeltnorth" or search == "foggylake" or search == "thefoggylake":
            if bogentrance_dialogue_guesses >= 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "A woman searching through the boxes giggles. “Thankfully not, an’ not even close,” she mutters. The scarred man nods in agreement. “They’re far - we used to trade, ba no longer.”\n\n“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    'A woman searching through the boxes giggles. “Thankfully not, an’ not even close,” she mutters. The scarred man nods in agreement. “They’re far - we used to trade, ba no longer.”
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears f’strangers, specially these days.”"
                        jump bogentranceafterquestion01
        elif search == "oldpagos" or search == "theoldpagos" or search == "monastery" or search == "themonastery":
            if bogentrance_dialogue_guesses >= 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "“They’re close, ba no,” says the oldest person of the entire group, a wrinkled, skinny man that’s looking beneath the cart. “We used to be in touch with them,” adds the scarred man, “times’re dif’rent.”\n\n“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    '“They’re close, ba no,” says the oldest person of the entire group, a wrinkled, skinny man that’s looking beneath the cart. “We used to be in touch with them,” adds the scarred man, “times’re dif’rent.”
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears of strangers, specially these days.”"
                        jump bogentranceafterquestion01
        elif search == "howlersdell" or search == "thehowlersdell" or search == "howlers" or search == "howlerdell" or search == "thehowlerdell":
            if bogentrance_dialogue_guesses >= 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "Another man, who’s leaning on the cart, sighs. “I’d rather die,” he states, then drinks from a waterskin and grimaces with disgust. His boss smiles, but doesn’t add anything.\n\n“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    'Another man, who’s leaning on the cart, sighs. “I’d rather die,” he states, then drinks from a waterskin and grimaces with disgust. His boss smiles, but doesn’t add anything.
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears of strangers, specially these days.”"
                        jump bogentranceafterquestion01
        elif search == "thetribeofthegreenmountain" or search == "tribeofthegreenmountain" or search == "thetribeofgreenmountain" or search == "tribeofgreenmountain" or search == "tribeofgreenmountain" or search == "tribegreenmountain" or search == "thegreenmountaintribe" or search == "greenmountaintribe" or search == "greenmountainpeople":
            $ description_greenmountaintribe07 = "Apparently they try to stay away from the cityfolk, afraid of persecution at the hands of The United Church."
            if not quest_reachthepaganvillage:
                $ quest_reachthepaganvillage = 1
                $ renpy.notify("New entry: The Hidden Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
            if bogentrance_dialogue_guesses >= 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "“What a weird guess,” says the man, while his companions look at each other suspiciously. “We’re almost as’far’s we can be from them. Betta don’t look for them too hard,” he adds after a short pause. “They don’t love the cityfolk.”\n\n“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    '“What a weird guess,” says the man, while his companions look at each other suspiciously. “We’re almost as’far’s we can be from them. Betta don’t look for them too hard,” he adds after a short pause. “They don’t love the cityfolk.”
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears f’strangers, specially these days.”"
                        jump bogentranceafterquestion01
        elif search == "steephouse" or search == "thesteephouse":
            $ ruinedvillage_name = "Steep House"
            if bogentrance_dialogue_guesses >= 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "The entire group freezes, observing you with tension. “Sad to be the one to tell you,” says the man after a few breaths, “ba that place is no more. You’ll find it far away, in the south.”\n\n“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    'The entire group freezes, observing you with tension. “Sad to be the one to tell you,” says the man after a few breaths, “ba that place is no more. You’ll find it far away, in the south.”
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears of strangers, specially these days.”"
                        jump bogentranceafterquestion01
        #############################
        elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag" or search == "bitch" or search == "whore" or search == "cunt":
            $ bogentrance_dialogue_guesses += 1
            python:
                search = renpy.input("...Let’s try this again. Name of the village?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            jump druidcavetypingnameothertimes
        #############################
        else:
            if bogentrance_dialogue_guesses > 2:
                $ bogentrance_dialogue_askedquestions += 1
                $ custom1 = "“Well, you tried,” he raises his spear and puts it on his shoulders, holding it with both hands. “{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, ba they don’t reach the ears f’strangers.”"
                jump bogentranceafterquestion01
            else:
                $ bogentrance_dialogue_guesses += 1
                menu:
                    '“...What?”
                    '
                    '“Let me think...”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think...”')
                        python:
                            search = renpy.input("What do you think the name of their village is?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump bogentrance_dialogue_about_themselves02
                    '“No clue.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No clue.”')
                        $ bogentrance_dialogue_askedquestions += 1
                        $ custom1 = "“{color=#f6d6bd}White Marshes{/color}, t’s there,” he looks at the crossroad leading east. “An old place, plenty f’stories there, but they rarely reach the ears f’strangers, specially these days.”"
                        jump bogentranceafterquestion01

    label bogentrance_dialogue_about_trade01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to trade.”')
        $ bogentrance_dialogue_about_trade = 1
        menu:
            '“We don’t welcome many travelers, nor hope to see more of them, specially adventurers. An’ we need all the lumber we cut,” he frowns. “We’ve herbs, I guess. What can you bring?”
            '
            '“Just the dragon bones, most likely.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just the dragon bones, most likely.”')
                $ custom1 = "He pretends to yawn. “Not too helpful, merchants come to us maybe once a year, at least since...” He thinks for a moment, then sighs. “We’ve most f’what we need, other than iron, steel, bronze. Bring those, we’ll welcome you.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
                jump bogentranceafterquestion01
            '“Are you in need of food?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you in need of food?”')
                $ custom1 = "He pretends to yawn. “We’re doing fine, used to counting on ourselves, at least since...” He thinks for a moment, then sighs. “We’ve most f’what we need, other than iron, steel, bronze. Bring those, we’ll welcome you.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
                jump bogentranceafterquestion01
            '“How about some animal trophies? Furs, tusks?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about some animal trophies? Furs, tusks?”')
                $ custom1 = "“You think we’ve nothing to catch in the bogs?” He scoffs. “We’ve most f’what we need, other than iron, steel, bronze. Bring those, we’ll welcome you.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
                jump bogentranceafterquestion01
            '“Iron, maybe some copper. Weapons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Iron, maybe some copper.”')
                $ custom1 = "He takes a big, relieved breath. “T’s what I want to hear. We’ve some bones we’ve little use for. Bring what you can, we’ll share aplenty.”"
                $ bogentrance_dialogue_friendship += 1
                $ whitemarshes_reputation += 1
                $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
                jump bogentranceafterquestion01
            '“Odds and ends. Trinkets, herbs, you know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Odds and ends. Trinkets, herbs, you know.”')
                $ custom1 = "He pretends to yawn. “We pick and make what we need when the nights get long, have no need for peddlers, at least since...” He thinks for a moment, then sighs. “We only lack iron, steel, bronze. Bring those, we’ll welcome you.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ description_whitemarshes06 = "The locals are especially interested in purchasing iron."
                jump bogentranceafterquestion01

    label bogentrance_dialogue_about_findingwhitemarshes01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can I reach {color=#f6d6bd}White Marshes{/color}?”')
        $ bogentrance_dialogue_about_findingwhitemarshes = 1
        $ bogentrance_dialogue_askedquestions += 1
        menu:
            '“T’s not so hard, if you have bones or food with you. Ride down the road, turn left, an’ take a gift to {color=#f6d6bd}Thyrsus{/color}, the warden of our peat fields. He’ll open the creepers for you.” Seeing your look, he carries on. “They’re on the right path, one that’ll take you to the village.”
            '
            '“Anything dangerous between here and there?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything dangerous between here and there?”')
                $ custom1 = "“Water hides saurians, don’t let your horse drink. Just stay on the road, all the time.” One of the women chips in. “An’ don’t follow voices, or lights. Weird beasts lure humans into death. An’ don’t touch the creepers.”"
                $ bogentrance_dialogue_askedquestions += 1
                jump bogentranceafterquestion01
            '“What are you using peat for?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are you using peat for?”')
                $ custom1 = "“What else? Fuel, bricks. We used to sell it, some plants need it in soil.”"
                $ bogentrance_dialogue_askedquestions += 1
                jump bogentranceafterquestion01
            '“Sounds easy enough.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds easy enough.”')
                $ custom1 = "He shrugs. “It used to be, ba the roads sink more an’ more. Mayhap for the betta.”"
                jump bogentranceafterquestion01

    label bogentrance_dialogue_about_area01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about this area?”')
        $ bogentrance_dialogue_askedquestions += 1
        $ bogentrance_dialogue_about_area = 1
        $ description_oldpagos09 = "According to the wayfarers I met, the locals “are a warm bunch”."
        menu:
            'He scratches his head with the tip of his spear, then looks around. “Well, the’re wetlands in the east. Right now, we’re on the main road. North, it leads through the hills, to the inn, an’ the villages behind it. Ba the’re also villages the other way... Hard to say,” he smiles apologetically. “I don’t travel much. You may find news in {color=#f6d6bd}Old Págos{/color}, they’re a warm bunch. Just ride south, to the crossroads, then west. Not east,” he shakes the spear like a wagging finger. “That way leads to the heart of the woods, a forsaken place.”
            '
            '“And what about this very place? Is this a forest garden?”' if not whitemarshes_forestgardenabandoned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what about this very place? Is this a forest garden?”')
                $ custom1 = "He nods with approval. “Pretty much. My great grandparents started it to harvest various fruits an’ sap from birches. Ba those were other days, an’ other roads. The’s nothing f’value left, an’ no time or strong folks to take care of the land.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ whitemarshes_forestgardenabandoned = 1
                jump bogentranceafterquestion01
            '“What happened to the signpost?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened to the signpost?”')
                $ custom1 = "He shrugs. “It used to invite strangers to come by. Ba now, we don’t need them.”"
                $ bogentrance_dialogue_askedquestions += 1
                jump bogentranceafterquestion01
            '“Actually, {color=#f6d6bd}Old Págos{/color} is struggling with the plague.”' if not helvius_about_plague1 and oldpagos_plague_known:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, {color=#f6d6bd}Old Págos{/color} is struggling with the plague.”')
                $ custom1 = "As you describe the situation, the rest of the group straightens up, caught by surprise. “Was thinking why the’re more beasts on the road these days.” The man rubs his scarred cheek, lost in his thoughts, but the others don’t spare you questions about the village and the illness itself. After another minute, the air gets even grimmer."
                $ helvius_about_plague1 += 1
                $ bogentrance_dialogue_askedquestions -= 1
                $ whitemarshes_reputation += 1
                $ bogentrance_dialogue_friendship += 1
                $ oldpagos_plague_warnedplaces += 1
                jump bogentranceafterquestion01
            '“I see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                $ custom1 = "“No soul uses these cursed roads anyway,” adds another man. “bat’s more peaceful, that way.”"
                jump bogentranceafterquestion01

    label bogentrance_dialogue_about_whitemarshes01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about your village.”')
        $ bogentrance_dialogue_about_whitemarshes = 1
        menu:
            '“T’s home,” he starts to play with his spear. “As much a home’s the bogs can be. Beasts’re smaller than in the woods, ba water’s the real threat.”
            '
            '“Is it rough, living in the wetlands?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it rough, living in the wetlands?”')
                $ custom1 = "“Not as rough’s living with robbers one side an’ that fake, smiling rat that leads {color=#f6d6bd}Howler’s{/color} on the other,” he says to the delight of his group. You look at him, but he says nothing more."
                $ description_thais07 = "I met people in the west who called her a “fake, smiling rat.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ bogentrance_dialogue_friendship += 1
                jump bogentranceafterquestion01
            '“Why {i}Marshes{/i}, when it’s set at the bogs?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {i}Marshes{/i}, when it’s set at the bogs?”')
                $ custom1 = "“Swamps, quagmires, sloughs... Who cares? As long’s the’s peat under the grass an’ saurians in the ponds, t’s our land.”"
                jump bogentranceafterquestion01
            '“Will I find {color=#f6d6bd}Asterion{/color} there?”' if quest_asterion == 1 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Will I find {color=#f6d6bd}Asterion{/color} there?”')
                $ custom1 = "His eyes lose a part of their shine. “So he’s not around, an’ you’re {i}looking{/i} for him?” Because of the scars, his grimace is hard to read. “No, he’sn’t at our home. Talk about it with {color=#f6d6bd}Thyrsus{/color} on the peat fields, if you must.”"
                $ quest_asterion_description11a = "I heard that {color=#f6d6bd}Thyrsus{/color} from {color=#f6d6bd}peat fields{/color} may know something about him."
                $ renpy.notify("Journal updated: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                jump bogentranceafterquestion01
            '“I heard some... Rumors about the dark magic used by your people.”' if description_whitemarshes02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard some... Rumors about the dark magic used by your people.”')
                $ quest_explorepeninsula_description02prec = "The few travellers I met at the edge of the bog got upset upset when I mentioned the undead."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ bogentrance_dialogue_askedquestions += 30
                $ bogentrance_dialogue_about_undead = 1
                $ bogentrance_dialogue_friendship -= 2
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'He stays silent for a moment, then raises his voice and addresses his companions. “We wasted too much time on t’s froth. Time to get back.” As he walks away, he speaks again, without turning back. “Stay safe, stranger. Bogs’re a dangerous place.”
                    \n\nThe others, giving you harsh looks, join their guide. The one with the bough stays still, until a gentle gesture commands them to follow. They keep up with the rest of the group, dragging the club behind themselves with remarkable strength.
                    '
                    'I could spend a few minutes foraging for wild plants.' if bogentrance_wildplants_left == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend a few minutes foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend half an hour foraging for wild plants.' if bogentrance_wildplants_left == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend half an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend more than half an hour foraging for wild plants.' if bogentrance_wildplants_left == 3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than half an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend an hour or so foraging for wild plants.' if bogentrance_wildplants_left == 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend an hour or so foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend more than an hour foraging for wild plants.' if bogentrance_wildplants_left == 5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'After a few more days there may be fruits and other plants to pick here. (disabled)' if bogentrance_wildplants_left == 0:
                        pass
                    'We prepare for the journey. (disabled)' if pc_likeshorsename:
                        pass
                    'I prepare for the journey. (disabled)' if not pc_likeshorsename:
                        pass

    label bogentrance_dialogue_about_cart01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is this your cart?”')
        $ bogentrance_dialogue_askedquestions += 1
        $ bogentrance_dialogue_about_cart = 1
        menu:
            '“In a way. My neighbor’s.” You then hear one of the women proudly claiming that it belongs to her uncle, but the man doesn’t allow you to dig into this topic. “{i}We{/i} used to carry wood an’ plants from here to the village, ba eventually there was not a thing {i}to{/i} carry, an’ t’was left for another day. T’s trash, now.”
            '
            '“I saw an abandoned wagon on the opposite side of the peninsula. I thought it may be connected.”' if fallentree_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw an abandoned wagon on the opposite side of the peninsula. I thought it may be connected.”')
                $ custom1 = "After your short tale, the man moves his sealed lips left and right. Finally, the same woman interrupts. “Must be the robbers.” The man nods. “True. What she said.”"
                $ description_bandits02 = "When I mentioned the abandoned wagon to a group of travelers, they said the bandits are the most likely culprits."
                $ quest_fallentree_description03 = "When I mentioned the abandoned wagon to a group of travelers, they said the bandits are the most likely culprits."
                $ bogentrance_dialogue_askedquestions += 1
                $ banditshideout_bandits_pchearedabout = 1
                $ bogentrance_dialogue_friendship += 1
                if quest_fallentree == 1:
                    $ renpy.notify("Journal updated: Fallen Tree")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Fallen Tree{/i}')
                jump bogentranceafterquestion01
            '“What makes this place so special?”' if not whitemarshes_forestgardenabandoned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What makes this place so special?”')
                $ custom1 = "He sighs. “It used to be a forest garden. My great grandparents started it to harvest various fruits an’ sap from birches. Ba those were other days, an’ other roads. The’s nothing f’value left, an’ no time or strong folks to take care of the land.”"
                $ bogentrance_dialogue_askedquestions += 1
                $ whitemarshes_forestgardenabandoned = 1
                jump bogentranceafterquestion01
            '“Are you going to leave it here, as it is?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you going to leave it here, as it is?”')
                $ custom1 = "He raises his eyebrow, then scoffs. “F’course. For termites an’ mushrooms, then we’ll eat them when we get hungry. Nothing goes to waste.”"
                jump bogentranceafterquestion01

    label bogentrance_dialogue_about_hoodedperson01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the hooded person. “What’s up with this one?”')
        $ bogentrance_dialogue_about_hoodedperson = 1
        menu:
            'He smiles, but you notice that the others keenly observe you. “Nothing is {i}up{/i}. They’re keeping us safe.”
            '
            '“They must feel hot, under so many clothes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They must feel hot, under so many clothes.”')
                $ custom1 = "“Don’t worry about it. See, they don’t.”"
                $ bogentrance_dialogue_askedquestions += 1
                jump bogentranceafterquestion01
            '“That’s an impressive... {i}club{/i}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an impressive... {i}club{/i}.”')
                $ custom1 = "One of the men, now turning over a moldy plank with his boot, giggles. “T’s one way to put it. Their pneuma’s strong.”"
                $ bogentrance_dialogue_askedquestions += 1
                jump bogentranceafterquestion01
            '“I heard some... Rumors about the dark magic used by your people.”' if description_whitemarshes02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard some... Rumors about the dark magic used by your people.”')
                $ quest_explorepeninsula_description02prec = "The few travellers I met at the edge of the bog got upset when I mentioned the undead."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ bogentrance_dialogue_askedquestions += 30
                $ bogentrance_dialogue_about_undead = 1
                $ bogentrance_dialogue_friendship -= 2
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'He stays silent for a moment, then raises his voice and addresses his companions. “We wasted too much time on t’s froth. Time to get back.” As he walks away, he speaks again, without turning back. “Stay safe, stranger. Bogs’re a dangerous place.”
                    \n\nThe others, giving you harsh looks, join their guide. The one with the bough stays still, until a gentle gesture commands them to follow. They keep up with the rest of the group, dragging the club behind themselves with remarkable strength.
                    '
                    'I could spend a few minutes foraging for wild plants.' if bogentrance_wildplants_left == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend a few minutes foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend half an hour foraging for wild plants.' if bogentrance_wildplants_left == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend half an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend more than half an hour foraging for wild plants.' if bogentrance_wildplants_left == 3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than half an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend an hour or so foraging for wild plants.' if bogentrance_wildplants_left == 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend an hour or so foraging for wild plants.')
                        jump bogentranceforaging01
                    'I could spend more than an hour foraging for wild plants.' if bogentrance_wildplants_left == 5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than an hour foraging for wild plants.')
                        jump bogentranceforaging01
                    'After a few more days there may be fruits and other plants to pick here. (disabled)' if bogentrance_wildplants_left == 0:
                        pass
                    'We prepare for the journey. (disabled)' if pc_likeshorsename:
                        pass
                    'I prepare for the journey. (disabled)' if not pc_likeshorsename:
                        pass

    label bogentrance_dialogue_about_missinghunters01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I seek a few missing hunters from {color=#f6d6bd}Creeks{/color}. Have you seen any of them?”')
        $ bogentrance_dialogue_about_missinghunters = 1
        $ quest_missinghunters_daliaknown = 1
        if item_rawhide:
            $ custom1 = " He then points at the rawhide hanging from your bundles. “T’s her, isn’t it?”"
            $ northernroad_rawhide_owner = 1
        else:
            $ custom1 = ""
        # $ bogentrance_dialogue_askedquestions += 1
        $ questionpreset = "bogentrance"
        menu:
            '“Ah, a beast seeker on’a dumb bet? She was at our home days back, Dela?” He looks at one of the women. “T’was {color=#f6d6bd}Dalia{/color},” she corrects him and he nods gratefully. “Hear that, stranger? She asked us on howlers, spent one night at our hut, said she’ll go north.”[custom1]
            '
            '(bogentrance preset)':
                pass

label bogentranceafterquestion01:
    if bogentrance_dialogue_askedquestions < bogentrance_dialogue_maxquestions:
        $ questionpreset = "bogentrance"
        menu:
            '[custom1]
            '
            '(bogentrance preset)':
                pass
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            \n\nHe then stretches out and gets closer to the signpost, using his spear as a walking stick. “Well, stay safe, stranger.” He raises his voice and addresses his companions. “We wasted too much time on t’s froth, time to get back.”
            \n\nThe others prepare their own weapons and join their guide. The one with the bough stays silent, until a gentle gesture commands them to follow. They keep up with the rest of the group, dragging the club behind themselves with remarkable strength.
            '
            'I could spend a few minutes foraging for wild plants.' if bogentrance_wildplants_left == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend a few minutes foraging for wild plants.')
                jump bogentranceforaging01
            'I could spend half an hour foraging for wild plants.' if bogentrance_wildplants_left == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend half an hour foraging for wild plants.')
                jump bogentranceforaging01
            'I could spend more than half an hour foraging for wild plants.' if bogentrance_wildplants_left == 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than half an hour foraging for wild plants.')
                jump bogentranceforaging01
            'I could spend an hour or so foraging for wild plants.' if bogentrance_wildplants_left == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend an hour or so foraging for wild plants.')
                jump bogentranceforaging01
            'I could spend more than an hour foraging for wild plants.' if bogentrance_wildplants_left == 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend more than an hour foraging for wild plants.')
                jump bogentranceforaging01
            'After a few more days there may be fruits and other plants to pick here. (disabled)' if bogentrance_wildplants_left == 0:
                pass
            'We prepare for the journey. (disabled)' if pc_likeshorsename:
                pass
            'I prepare for the journey. (disabled)' if not pc_likeshorsename:
                pass

    label bogentranceleavingfriendly01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, better to carry on. Good luck with the forest.”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ description_thyrsus01 = "According to the patrol I encountered at the old forest garden, I shouldn’t “bother him long. He’s f’a cold soul.”"
        menu:
            '“Yeah, the days’re getting short. When you see {color=#f6d6bd}Thyrsus{/color}, don’t bother him long. He’s f’a cold soul.” He smiles. “An’ safe travels.”
            \n\nHis companions nod to you as well. The one with the bough remains silent and still, like a statue.
            '
            'We ride past them. (disabled)' if pc_likeshorsename:
                pass
            'I ride past them. (disabled)' if not pc_likeshorsename:
                pass
    label bogentranceleavingneutral01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to them. “Farewell, then.”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He nods. “Farewell, stranger.”
            \n\nHis companions carry on with their work. The one with the bough remains silent and still, like a statue.
            '
            'We ride past them. (disabled)' if pc_likeshorsename:
                pass
            'I ride past them. (disabled)' if not pc_likeshorsename:
                pass
    label bogentranceleavingangry01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gesture for them to clear the way. “I’m leaving.”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He steps aside, his companions are giving you harsh looks. The one with the bough remains silent and still, like a statue.
            '
            'We ride past them. (disabled)' if pc_likeshorsename:
                pass
            'I ride past them. (disabled)' if not pc_likeshorsename:
                pass

label bogentranceforaging01:
    $ bogentrance_wildplants_howmanytimes += 1
    if bogentrance_wildplants_left == 1:
        $ item_wildplants += 1
        $ achievement_wildplants += 1
        $ bogentrance_wildplants_taken += 1
        $ bogentrance_wildplants_left -= 1
        $ quarters += 1
        $ renpy.notify("You picked a bunch of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a bunch of wild plants.{/i}')
        if bogentrance_wildplants_howmanytimes == 1:
            $ custom1 = "Most of what you find are large apples, not as sour as the wild ones, and some wild strawberries."
            $ custom2 = "Picking them takes little effort - the short meadow hides nothing more dangerous than rats, rabbits, mice, and grasshoppers, and with the help of your mount you can reach the higher branches."
        elif bogentrance_wildplants_howmanytimes == 2:
            $ custom1 = "Most of what you find are sour apples and juicy plums."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 3:
            $ custom1 = "Most of what you find are sweat pears and overripe sorb fruits."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 4:
            $ custom1 = "Most of what you find are sweat pears and overripe sorb fruits."
            $ custom2 = ""
        else:
            $ custom1 = "Most of what you find are small plums and purple carrots."
            $ custom2 = ""
    if bogentrance_wildplants_left == 2:
        $ item_wildplants += 2
        $ achievement_wildplants += 2
        $ bogentrance_wildplants_taken += 2
        $ bogentrance_wildplants_left -= 2
        $ renpy.notify("You picked 2 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 2 bunches of wild plants.{/i}')
        if bogentrance_wildplants_howmanytimes == 1:
            $ custom1 = "Most of what you find are large apples, not as sour as the wild ones, wild strawberries, and a few clumps of sorrel."
            $ custom2 = "Picking them takes little effort - the short meadow hides nothing more dangerous than rats, rabbits, mice, and grasshoppers, and with the help of your mount you can reach the higher branches."
        elif bogentrance_wildplants_howmanytimes == 2:
            $ custom1 = "Most of what you find are sour apples, juicy plums, and a few clumps of sorrel."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 3:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, and a few clumps of sorrel."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 4:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, and a few clumps of sorrel."
            $ custom2 = ""
        else:
            $ custom1 = "Most of what you find are small plums, purple carrots, and a few clumps of sorrel."
            $ custom2 = ""
    if bogentrance_wildplants_left == 3:
        $ item_wildplants += 3
        $ achievement_wildplants += 3
        $ bogentrance_wildplants_taken += 3
        $ bogentrance_wildplants_left -= 3
        $ renpy.notify("You picked 3 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 3 bunches of wild plants.{/i}')
        if bogentrance_wildplants_howmanytimes == 1:
            $ custom1 = "Most of what you find are large apples, not as sour as the wild ones, wild strawberries, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = "Picking them takes little effort - the short meadow hides nothing more dangerous than rats, rabbits, mice, and grasshoppers, and with the help of your mount you can reach the higher branches."
        elif bogentrance_wildplants_howmanytimes == 2:
            $ custom1 = "Most of what you find are sour apples, juicy plums, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 3:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 4:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        else:
            $ custom1 = "Most of what you find are small plums, purple carrots, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
    if bogentrance_wildplants_left == 4:
        $ item_wildplants += 4
        $ achievement_wildplants += 4
        $ bogentrance_wildplants_taken += 4
        $ bogentrance_wildplants_left -= 4
        $ renpy.notify("You picked 4 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 4 bunches of wild plants.{/i}')
        if bogentrance_wildplants_howmanytimes == 1:
            $ custom1 = "Most of what you find are large apples, not as sour as the wild ones, wild strawberries, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = "Picking them takes little effort - the short meadow hides nothing more dangerous than rats, rabbits, mice, and grasshoppers, and with the help of your mount you can reach the higher branches."
        elif bogentrance_wildplants_howmanytimes == 2:
            $ custom1 = "Most of what you find are sour apples, juicy plums, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 3:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 4:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        else:
            $ custom1 = "Most of what you find are small plums, purple carrots, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
    if bogentrance_wildplants_left == 5:
        $ item_wildplants += 5
        $ achievement_wildplants += 5
        $ bogentrance_wildplants_taken += 5
        $ bogentrance_wildplants_left -= 5
        $ renpy.notify("You picked 5 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 5 bunches of wild plants.{/i}')
        if bogentrance_wildplants_howmanytimes == 1:
            $ custom1 = "Most of what you find are large apples, not as sour as the wild ones, wild strawberries, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = "Picking them takes little effort - the short meadow hides nothing more dangerous than rats, rabbits, mice, and grasshoppers, and with the help of your mount you can reach the higher branches."
        elif bogentrance_wildplants_howmanytimes == 2:
            $ custom1 = "Most of what you find are sour apples, juicy plums, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 3:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        elif bogentrance_wildplants_howmanytimes == 4:
            $ custom1 = "Most of what you find are sweat pears, overripe sorb fruits, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
        else:
            $ custom1 = "Most of what you find are small plums, purple carrots, a few clumps of sorrel, and a bit of lettuce, somehow spared by the wild critters."
            $ custom2 = ""
    menu:
        '[custom1] [custom2]
        '
        'I pack them into nets and bags. (disabled)':
            pass
