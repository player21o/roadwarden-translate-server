###################### Old Págos
default oldpagos_cured = 0
default oldpagos_cured_blocked = 0
default oldpagos_cured_introduction = 0
default oldpagos_plague_known = 0
default oldpagos_plague_warnedplaces = 0

default oldpagos_plague_helpfromgalerocks = 0 # wagon with victuals
default oldpagos_plague_helpfromgalerocks_dayofleaving = 0 # day+1

default oldpagos_firsttime = 0
default oldpagos_firsttime_day = 0
default oldpagos_firsttime_intro = 0
default oldpagos_firsttime_after = 0
default oldpagos_reputation = 0
default oldpagos_fluff = ""
default oldpagos_fluff_old = ""

default oldpagos_about_othervillages = 0
default oldpagos_about_othervillages_gray = 0
default oldpagos_about_quintus = 0
default oldpagos_about_trade = 0
default oldpagos_about_druidsplan = 0
default oldpagos_about_asterion = 0
default oldpagos_about_eudocia_parents = 0
default oldpagos_about_oldpagos_plague_warnedplaces = 0
default oldpagos_about_4villages = 0 # from 4
default oldpagos_about_howlersdell = 0
default oldpagos_about_whitemarshes = 0
default oldpagos_about_nomoreundead = 0
default oldpagos_about_harvest = 0

default oldpagos_about_galerocks = 0
default oldpagos_about_creeks = 0
default oldpagos_about_greenmountaintribe = 0
default oldpagos_about_bogroadcat = 0
default oldpagos_about_bogroadcat_introduction = 0
default oldpagos_about_vaschel = 0
default oldpagos_about_highisland = 0
default oldpagos_about_missinghunters = 0
default oldpagos_about_bandits = 0
default oldpagos_about_steephouse = 0
default oldpagos_about_steephouse_gray = 0
default oldpagos_about_steephouse_reputation = 20
default oldpagos_about_steephouse_eudocia = 0
default oldpagos_about_ibex = 0
default oldpagos_about_keys = 0
default oldpagos_about_watchtower_directions = 0
default oldpagos_about_matchmaking = 0

label oldpagos01:
    nvl clear
    $ pc_area = "oldpagos"
    label fluffloppoldpagos:
        if not oldpagos_cured:
            $ oldpagos_fluff = renpy.random.choice(['There are no sounds of work, just the songs of insects and birds. You knock on the gate, and {color=#f6d6bd}Tertia{/color} opens the peephole after a minute or so.', 'You spot feathers, bloodstains, and fresh prints of a large cat. You knock on the gate, and {color=#f6d6bd}Tertia{/color} opens the peephole after a minute or so.', 'You spot a trail left by a massive beast that trampled through the crops. {color=#f6d6bd}Tertia{/color} opens the peephole even before you reach the gate.', 'A large ant is exploring the fields, but flees at your sight. You knock on the gate and {color=#f6d6bd}Tertia{/color} opens the peephole right away.', 'A column of fire comes from the settlement. As you reach the gate, you hear weeping. You knock on the gate a few times, but for a minute or two no one comes. Finally, {color=#f6d6bd}Tertia{/color} opens the peephole.', 'As you’re approaching the gate, you hear muffled shouts and insults. After you knock at the gate, {color=#f6d6bd}Tertia{/color} opens the peephole angrily.'])
        else:
            $ oldpagos_fluff = renpy.random.choice(['Through the closed gate, you hear muffled conversations and echoes of stone cutting. You knock, and {color=#f6d6bd}Tertia{/color} soon orders to open it.', 'A few farmers wave to you from a distance, then hide behind the gate. {color=#f6d6bd}Tertia{/color} shows up soon, and greets you cheerfully.', 'There are fresh prints of boots and ibex hooves. You knock on the gate, and {color=#f6d6bd}Tertia{/color} opens the peephole after a minute or so. Soon after, the gate opens.', 'A massive flock of white-and-orange birds is circling above the hill, casting a shadow on the plateau. You knock on the gate a few times, but for a minute or two no one comes. Finally, it opens, with {color=#f6d6bd}Tertia{/color} standing in the center.', 'A red-and-brown ferret looks at you from the middle of the road, holding a mouse in its mouth. It runs away quickly and disappears among the tufts of grass. You approach the open gate, and {color=#f6d6bd}Tertia{/color} shows up soon after.'])
        if oldpagos_fluff == oldpagos_fluff_old:
            jump fluffloppoldpagos
        else:
            $ oldpagos_fluff_old = oldpagos_fluff
    if not oldpagos_firsttime:
        show areapicture oldpagosscrap01 at basicfade
    elif not oldpagos_cured:
        show areapicture oldpagosscrap03 at basicfade
    else:
        show areapicture oldpagosscrap05 at basicfade
    if not oldpagos_firsttime:
        $ world_known_npcs += 2
        $ world_known_areas += 1
        $ oldpagos_firsttime = 1
        $ monastery_unlocked = 1
        $ westerncrossroads_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ oldpagos_firsttime_day = day
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/mountainroad01.ogg":
            play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump oldpagosfirsttime01
    else:
        stop nature fadeout 4.0
        if druidcave_druid_about_plague_travel == 1:
            $ renpy.music.play("audio/track_09healing.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        elif not oldpagos_cured:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/track_06oldpagosloop.ogg":
                play music "<loop 10.0>audio/track_06oldpagosloop.ogg" fadeout 1.0 fadein 1.0
        else:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/bonustrackscottbuckleybloodloop.ogg":
                play music "<loop 10.0>audio/bonustrackscottbuckleybloodloop.ogg" fadeout 1.0 fadein 1.0
        if druidcave_druid_about_plague_travel == 1:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump druidcave_druid_about_plague04
        elif oldpagos_plague_helpfromgalerocks == 1 and quarters >= 40 and quarters <= 60 and oldpagos_plague_helpfromgalerocks_dayofleaving < day:
            if not oldpagos_cured:
                show areapicture oldpagosscrap03 at basicfade
            else:
                show areapicture oldpagosscrap04 at basicfade
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump oldpagos_plague_helpfromgalerocks01
        elif oldpagos_plague_helpfromgalerocks == 2:
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump oldpagosregular01afterfoodwagon
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if not oldpagos_cured:
            jump oldpagosregular01
        elif not oldpagos_cured_introduction:
            jump oldpagosregularhealedfirsttime01
        else:
            jump oldpagosregularhealed01

label workinglabeloldpagosfirsttime01: #regular first time
    label oldpagosfirsttime01:
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'The corridor of pruned trees leads you to a steep ascent. Behind them grows a peaceful meadow, filled with flowers and crickets, and the humming of a waterfall.
            \n\nOn the beaten path you spot no footprints or wheel trails, but there’s smoke on the horizon.
            '
            'I dismount and lead {color=#f6d6bd}[horsename]{/color} on a rope.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and lead {color=#f6d6bd}%s{/color} on a rope.' %horsename)
                show areapicture oldpagosscrap02 at basicfade
                menu:
                    'The pastures and fields are spread over an unnatural plateau. Humans must have been carving in the hill for generations, covering it with soil brought here in buckets and wagons.
                    \n\nAmong the weeds and tall grasses you spot rotting tools and a tunic. The pasture is overgrowing, and so are the fields. Some of the oats are ready for harvest.
                    '
                    'Something is wrong. I prepare my axe.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Something is wrong. Time to prepare my axe.')
                        $ custom1 = "axe"
                        jump oldpagosfirsttime02
                    'I stay calm.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay calm.')
                        $ custom1 = "noaxe"
                        label oldpagosfirsttime02:
                            show areapicture oldpagosscrap03 at basicfade
                            menu:
                                'The locked gate is taller than a troll, and you can’t imagine climbing up the massive wall. For a moment, you follow the path to the edge of the cliff. The roaring ocean is more than a hundred feet below you.
                                \n\nYou spot no one looking at you from the watchtower, no patrols of archers. The wall is occupied by black and blue birds of various types. You return to the gate and focus on the sounds. There are a few screaming ibexes, a young boy is crying.
                                '
                                'I knock on the gate with my fist.' if custom1 == "noaxe":
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knock on the gate with my fist.')
                                    jump oldpagosfirsttime03
                                'I knock on the gate with the handle of my weapon.' if custom1 == "axe":
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knock on the gate with the handle of my weapon.')
                                    jump oldpagosfirsttime03

    label oldpagosfirsttime03:
        $ at_activate = 1
        $ at = 0
        if item_wingedhourglass_worn:
            $ oldpagos_reputation += 1
            $ custom1 = "The holy sign on ya neck won’t protect ye here. "
        else:
            $ custom1 = ""
        if not pc_firstvillage:
            $ pc_firstvillage = "oldpagos"
        if not oldpagos_cured:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/track_06oldpagosloop.ogg":
                play music "<loop 10.0>audio/track_06oldpagosloop.ogg" fadeout 1.0 fadein 1.0
        else:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/bonustrackscottbuckleybloodloop.ogg":
                play music "<loop 10.0>audio/bonustrackscottbuckleybloodloop.ogg" fadeout 1.0 fadein 1.0
        stop nature fadeout 4.0
        menu:
            'The thudding scares away the birds. They caw loudly, starting the cacophony of throats and flapping wings.
            \n\nAfter maybe a minute, you hear a bronze plate scratching against the wood as someone reveals the peephole. The strict female voice stops you from moving closer.
            \n\n“Traveler! [custom1]{color=#f6d6bd}Old Págos{/color} is secluding, for it has been smitten by a deadly plague. Begone, before ye get sick.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            '“Do you need any help? I’m the new roadwarden.”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Do you need any help? I’m the new roadwarden.”')
                $ at_activate = 0
                $ at = 0
                $ quest_explorepeninsula_description12 = "The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ oldpagos_reputation += 1
                menu:
                    '“No one can save us.” You look into the young, brown eyes that match the skin of the black-haired owner. While the woman looks like a Southerner, she has a strong local accent. She follows you cautiously, without blinking, like a fighter awaiting a strike. “North from here, in the monastery, live masters of spells and potions, blessed people guided by The Wright themselves, and even {i}they{/i} are powerless.”
                    \n\nYou hear more footsteps gathering near the entrance. “May them be blessed, for they look after our ill,” a weak voice of an elder chips in.
                    \n\n“We thank ye, warden,” the woman continues. “We can’t know how many of us will see the winter. If ye really want to help us, warn the other tribes. {i}They{/i} wouldn’t move a finger for us, but we ought to protect them.”
                    '
                    '“There must be something I can do.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There must be something I can do.”')
                        menu:
                            'After she blinks, you catch the sadness in her eyes. “I’ve heard such words more times than I can count. We’ve done all that we could. What’s left is to ask The Wright to ease our pain, and wait.”
                            '
                            '“I’ll also keep you in my prayers.”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                                $ pc_faithpoints += 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll also keep you in my prayers.”')
                                if item_wingedhourglass_worn:
                                    $ oldpagos_reputation += 1
                                    menu:
                                        'She glances at the hourglass on your neck, then closes her eyes and tilts her head forward. You hear a voice of a young man: “May The Wright bless you, warden!”
                                        '
                                        '“If it’s alright, I’ve a few questions.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it’s alright, I’ve a few questions.”')
                                            jump oldpagosafterinteraction01
                                else:
                                    menu:
                                        'She nods politely. “May your road be safe.”
                                        '
                                        '“If it’s alright, I’ve a few questions.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it’s alright, I’ve a few questions.”')
                                            jump oldpagosafterinteraction01
                            '“Can I ask you a few questions, while I’m here?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I ask you a few questions, while I’m here?”')
                                jump oldpagosafterinteraction01
                    '“Can I ask you a few questions, while I’m here?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I ask you a few questions, while I’m here?”')
                        jump oldpagosafterinteraction01
            '“Let your roadwarden in! I can handle a sore throat.”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - Let your roadwarden in! I can handle a sore throat.')
                $ at_activate = 0
                $ at = 0
                $ quest_explorepeninsula_description12 = "The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ oldpagos_reputation -= 2
                menu:
                    'The voice rises. “Stay away! We parted with a dozen souls already, others are spending their days sleeping, screaming from nightmares. In Wright’s name, we won’t drown other tribes with us!”
                    \n\nMore people approach the gate, you hear their distrustful whispers. You look into the young, brown eyes that match the skin of the black-haired owner. While the woman looks like a Southerner, she has a strong local accent.
                    \n\n“We’ll fulfill our duty,” she concludes with a strong, confident voice. She follows you cautiously, without blinking, like a fighter awaiting a strike.
                    '
                    '“Before I leave, I need to ask you a few things.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Before I leave, I need to ask you a few things.”')
                        jump oldpagosafterinteraction01
            'I introduce myself.' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I introduce myself.')
                $ at_activate = 0
                $ at = 0
                $ quest_explorepeninsula_description12 = "The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ oldpagos_reputation += 0
                menu:
                    '“We can’t welcome ye with bread, nor meat.” You look into the young, brown eyes that match the skin of the black-haired owner. While the woman looks like a Southerner, she has a strong local accent. She follows you cautiously, without blinking, like a fighter awaiting a strike. “We parted with a dozen souls already. The monks in the north are masters of spells and potions, guided by The Wright themselves, yet even they can’t help us.”
                    \n\nYou hear more footsteps gathering near the entrance, and a weak voice of an elder chips in. “May them be blessed, for they look after our ill.”
                    \n\nThe woman continues. “Ye won’t find shelter here. We ought not drown other tribes with us, such is our duty.” A pause. “Even if {i}they{/i} would {i}not{/i} show us such kindness.”
                    '
                    '“I’ve a few questions.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a few questions.”')
                        jump oldpagosafterinteraction01
            '“Then keep your distance. I’m a roadwarden, I need to stay healthy.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Then keep your distance. I’m a roadwarden, I need to stay healthy.”')
                $ at_activate = 0
                $ at = 0
                $ quest_explorepeninsula_description12 = "The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ oldpagos_reputation += 0
                menu:
                    '“That’s what we aim to do.” You look into the young, brown eyes that match the skin of the black-haired owner. While the woman looks like a Southerner, she has a strong local accent. She follows you cautiously, without blinking, like a fighter awaiting a strike.
                    \n\nYou hear more footsteps gathering near the entrance, and the guard continues. “We ought not drown other tribes with us, such is our duty.” A pause. “Even if {i}they{/i} would {i}not{/i} show us such kindness. But why are ye here in the first place?”
                    '
                    '“To ask you a few questions.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To ask you a few questions.”')
                        jump oldpagosafterinteraction01
            'I nod toward the peephole and step back. From a distance, I introduce myself.' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I nod toward the peephole and step back. From a distance, I introduce myself.')
                $ at_activate = 0
                $ at = 0
                $ quest_explorepeninsula_description12 = "The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
                $ renpy.notify("Journal updated: Explore the Peninsula")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                $ oldpagos_reputation += 0
                menu:
                    'You look into the young, brown eyes that match the skin of the black-haired owner. While the woman looks like a Southerner, she has a strong local accent. She follows you cautiously, without blinking, like a fighter awaiting a strike. “Salutations, warden, and yer right to be afraid. We parted with a dozen souls already, others are spending their days sleeping, screaming from nightmares.” You hear more footsteps gathering near the entrance. “The monks in the north are masters of spells and potions, guided by The Wright themselves, yet even they can’t help us.”
                    \n\n“May them be blessed, for they look after our ill,” a weak voice of an elder chips in.
                    \n\nThe woman continues. “Ye won’t find shelter here. We ought not drown other tribes with us, such is our duty.” A pause. “Even if {i}they{/i} would {i}not{/i} show us such kindness.”
                    '
                    '“Before I go, would you answer a few questions?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Before I go, would you answer a few questions?”')
                        jump oldpagosafterinteraction01

label oldpagosregular01:
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if oldpagos_reputation >= 5:
        menu:
            '[oldpagos_fluff] “Salutations! Any good news?”
            '
            '(oldpagos preset)':
                pass
    else:
        if pc_hp >= 2:
            $ custom1 = "Healthy, still? Good."
        else:
            $ custom1 = "Are ye sure yer not sick?"
        menu:
            '[oldpagos_fluff] You approach the gate and knock at it. She gives you a long look. “[custom1]”
            '
            '(oldpagos preset)':
                pass

label oldpagos_plague_helpfromgalerocks01:
    $ oldpagos_plague_helpfromgalerocks = 2
    if pc_goal == "iwanttoberemembered":
        $ pc_goal_iwanttoberememberedpoints += 1
    if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
        $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ galerocks_reputation += 1
    $ oldpagos_reputation += 3
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'You hear loud conversations coming from the gate, in front of which you find large barrels - similar to those you’ve seen in {color=#f6d6bd}Gale Rocks{/color}.
        \n\nA group of travelers, some of whom you recognize as fishers, guards, lumberjacks, or carriers, is standing many feet away from the wall, shouting toward it with a tone that’s somewhere between embarrassment and nostalgia. You hear awkward apologies, shared memories, plans for the future, questions about family members... As if both tribes are hermits who haven’t spoken with anyone in years. The first, and still unsure, step in a long path toward healing.
        \n\nAs this goes on, the perfumed guard you’ve met at the keep - looking as clean and tidy as ever - welcomes you with a smile. “Always patrolling, I see?” Before you answer, he turns back toward the wall.
        '
        'I let them do their talking.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let them do their talking.')
            $ quarters += 4
            $ oldpagos_reputation += 2
            $ oldpagos_plague_helpfromgalerocks = 3
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "oldpagos"
            if not oldpagos_cured:
                menu:
                    'You lead {color=#f6d6bd}[horsename]{/color} to the meadow and rest by the fence. After about an hour, the Northerners prepare for their departure, hoping to get back before nightfall. As they push their empty wagons, they wish you a safe evening.
                    \n\nAfter you reach the peephole, {color=#f6d6bd}Tertia’s{/color} smile makes her whisper, as if she’s not willing to believe what just happened. “It’s ya doing, isn’t it, [pcname]? I know it is. Thank ye.”
                    '
                    '(oldpagos preset)':
                        pass
            else:
                show areapicture oldpagosscrap05 at basicfade
                menu:
                    'You lead {color=#f6d6bd}[horsename]{/color} to the meadow and rest by the fence. After about an hour, the Northerners prepare for their departure, hoping to get back before nightfall. As they push their empty wagons, they wish you a safe evening.
                    \n\nAfter you reach the peephole the gate opens. {color=#f6d6bd}Tertia’s{/color} smile makes her whisper, as if she’s not willing to believe what just happened. “It’s ya doing, isn’t it, [pcname]? I know it is. Thank ye.”
                    '
                    '(oldpagos preset)':
                        pass
        'I’ve no time for this. I turn {color=#f6d6bd}[horsename]{/color} back.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no time for this. I turn {color=#f6d6bd}%s{/color} back.' %horsename)
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'The empty conversations hit your back.
                '
                'I ride away. (disabled)':
                    pass

label oldpagosregular01afterfoodwagon:
    $ oldpagos_plague_helpfromgalerocks = 3
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if not oldpagos_cured:
        menu:
            'A weak male voice coats the village with its song. Long before you reach the gate, {color=#f6d6bd}Tertia{/color} opens the peephole and greets you cheerfully. “[pcname]! Thanks to ye, we can feed our sick with fish, even in winter.”
            '
            '(oldpagos preset)':
                pass
    else:
        menu:
            'A weak male voice coats the village with its song. Long before you reach the open gate, {color=#f6d6bd}Tertia{/color} waves to you cheerfully with her spear. “[pcname]! Thanks to ye, we can feed our sick with fish, even in winter.”
            '
            '(oldpagos preset)':
                pass

label oldpagosregularhealed01:
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[oldpagos_fluff] You see a hint of a smile in her brown eyes. “It’s good to see ye again, [pcname].”
        '
        '(oldpagos preset)':
            pass

label oldpagosregularhealedfirsttimeALL:
    label oldpagosregularhealedfirsttime01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ oldpagos_cured_introduction = 1
        $ renpy.force_autosave(take_screenshot=False, block=True)
        $ oldpagos_fluff = "Through the closed gate, you hear muffled conversations and echoes of stone cutting. You knock, and {color=#f6d6bd}Tertia{/color} soon orders to open it."
        $ oldpagos_fluff_old = oldpagos_fluff
        menu:
            '[oldpagos_fluff] She stands in the middle, in front of dozens of members of her tribe, though you’re still told to keep your distance. The signs of illness are carved in the exhausted faces of the elders and the children, but this is not the day of sadness - you’re greeted with triumphant shouts and applause.
            \n\n{color=#f6d6bd}Tertia{/color} turns out to be tall and skinny, holding a spear that would be too long for most, but suits her size. While her tribesfolk are wearing tunics and robes made of ibex fur or hemp, she has put on an impressive breastplate made of animal shell. She has short, dark hair, and while her skin is dark brown, you can tell there are others in her village who carry the blood of the Southerners.
            \n\nHer voice matches her cheerful brown eyes as she speaks in the name of her people. “We keep ye in our prayers, [pcname]! If we could, we would invite ye to a feast, but we need to keep our distance, at least till the end of winter. We’d like to reward ye, even if there’s naught that would make us even.”
            '
            '“I don’t need anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need anything.”')
                menu:
                    '“I believe ye, but please, let us. It’s our duty to give back to the world at least as much as we’ve received.”
                    '
                    '“In what way?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In what way?”')
                        jump oldpagosregularhealedfirsttime02
            '“Oh?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh?”')
                label oldpagosregularhealedfirsttime02:
                    if oldpagos_about_druidsplan == 2:
                        menu:
                            '“We’ve already given ye the last treasure we owned, but we took the time to gather our savings. It’s not much, eighteen dragons, but not naught!” Her chuckle sounds like it belongs to a different soul, one lost in the past.
                            '
                            '“Thank you. I’ll put it to good use.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you. I’ll put it to good use.”')
                                jump oldpagosregularhealedfirsttime03money
                            '“I’ve a different idea.” It’s time to speak with them about joining the forces with {color=#f6d6bd}Hovlavan{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a different idea.” It’s time to speak with them about joining the forces with {color=#f6d6bd}Hovlavan{/color}.')
                                jump oldpagosregularhealedfirsttime03aboutcity
                    else:
                        menu:
                            '“There’s naught but one treasure we own in this village, a stuff very close to our hearts.” She raises a rod made of iron or steel, a bit longer than a finger span, but thin, finished with a flattened edge for cutting. It occurs to you that it’s a simple chisel.
                            \n\nAn elderly man chips in. “It belonged to my son, the greatest sculptor that has ever lived in {color=#f6d6bd}Old Págos{/color}, to Wright’s glory and our great joy.” His words are sonorous and solemn. “It’s filled with pneuma that makes its holder’s hands so powerful they can carve in granite, so precise they can write in glass!”
                            \n\nA short pause. “And if ye think ye won’t put it to good use,” adds {color=#f6d6bd}Tertia{/color}, “we took the time to gather our savings. It’s not much, eighteen dragons, but not naught!” Her chuckle sounds like it belongs to a different soul, one lost in the past.
                            '
                            '“Thank you, I’m honored.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you, I’m honored.”')
                                $ oldpagos_reputation += 1
                                jump oldpagosregularhealedfirsttime03chisel
                            '“I’ll take the chisel.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take the chisel.”')
                                jump oldpagosregularhealedfirsttime03chisel
                            '“I could use more dragon bones.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use more dragon bones.”')
                                jump oldpagosregularhealedfirsttime03money
                            '“I’ve a different idea.” It’s time to speak with them about joining the forces with {color=#f6d6bd}Hovlavan{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a different idea.” It’s time to speak with them about joining the forces with {color=#f6d6bd}Hovlavan{/color}.')
                                jump oldpagosregularhealedfirsttime03aboutcity

    label oldpagosregularhealedfirsttime03chisel:
        $ item_magicchisel = 1
        $ renpy.notify("You received a magic chisel.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a magic chisel.{/i}')
        if pc_class == "warrior":
            $ custom1 = "you catch it before it lands on the ground"
        else:
            $ custom1 = "it lands next to your boots"
        $ quest_oldpagossupport = 3
        menu:
            'She throws the rod toward you and [custom1]. It’s as warm as your own skin.
            \n\n“Be blessed, warden,” a small girl shouts, “and return to us in spring, so we can show ye our home!”
            \n\nYou hear many more words of gratitude.
            '
            'Awkward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Awkward.')
                jump oldpagosregularhealedfirsttime04
            'I show my respect with a bow.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show my respect with a bow.')
                jump oldpagosregularhealedfirsttime04

    label oldpagosregularhealedfirsttime03money:
        $ coins += 18
        show screen notifyimage( "+18", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+18 {image=cointest}{/i}')
        if pc_class == "warrior":
            $ custom1 = "you catch it before it lands on the ground"
        else:
            $ custom1 = "it lands next to your boots"
        $ quest_oldpagossupport = 3
        menu:
            'She throws the pouch toward you and [custom1]. It pleasantly fills your hand, with dragon bones trying to flee from your grasp.
            \n\n“Be blessed, warden,” a small girl shouts, “and return to us in spring, so we can show ye our home!”
            \n\nYou hear many more words of gratitude.
            '
            'Awkward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Awkward.')
                jump oldpagosregularhealedfirsttime04
            'I show my respect with a bow.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show my respect with a bow.')
                jump oldpagosregularhealedfirsttime04

    label oldpagosregularhealedfirsttime03aboutcity:
        $ quarters += 1
        menu:
            'You tell them about your journey north, about the officials and their plans for the coast, and the guild’s trade route. You explain that your actions were made “in the name of the city,” and that by paying taxes, they could protect themselves from future disasters.
            \n\n“I need you to keep this between us,” you conclude. “I’ll discuss it with other settlements on my own terms.”
            \n\n{color=#f6d6bd}Tertia{/color} is the first one to break the long silence. “We’ll keep ya words in our hearts, but we need to discuss them. We’re not ones to make rash decisions.”
            '
            '“I understand.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I understand.”')
                $ questionpreset = "oldpagos"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if pc_goal == "iwantstatus":
                    $ pc_goal_iwantstatuspoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Quest completed: The Support of Old Págos.\nJournal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Old Págos. Journal updated: %s{/i}' %quest_pc_goal_name)
                else:
                    $ renpy.notify("Quest completed: The Support of Old Págos")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Old Págos{/i}')
                $ quest_oldpagossupport = 2
                menu:
                    'The other villagers walk away without a word, leaving behind only the sounds of their footsteps. The woman’s voice betrays her exhaustion.
                    \n\n“Tell the merchants we’ll listen to what they’ve got to say, but we promise naught. We’re grateful, warden, we are. But first we want to see the spring. It will be a different world, and we need to understand it first.”
                    \n\nAfter a few breaths, she smiles again. “Ya offer has surprised us all, warden, but we will remember ye as our hero.”
                    '
                    '(oldpagos preset)':
                        pass

    label oldpagosregularhealedfirsttime04:
        $ questionpreset = "oldpagos"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ minutes += 5
        menu:
            'After some time, the villagers disperse, and {color=#f6d6bd}Tertia’s{/color} eyes brighten. Her confident stance adds strength to her voice. “Is there aught else ye need, [pcname]?”
            '
            '(oldpagos preset)':
                pass

label oldpagosafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if oldpagos_cured:
        $ custom1 = "“Go ahead, friend.”"
    elif not oldpagos_firsttime_after:
        $ oldpagos_firsttime_after = 1
        $ description_tertia00 = "Whenever I’m there, I speak with {color=#f6d6bd}Tertia{/color}, a fighter who, despite her age, represents the council."
        $ custom1 = "“Ask, but there’s not much we can do for ye. We see no one, we travel nowhere. We were born on this hill, and we’ll die here.” After a few breaths, her eyes get kinder. “I’m {color=#f6d6bd}Tertia{/color}. If ye bring any news, I’ll take them to our council.”"
    else:
        $ custom1 = ""
        $ custom1 = renpy.random.choice(['She observes you closely.', '“Go ahead.”', '“What d’ye need?”', '“Aught else?”', '“Warden.”'])
    $ questionpreset = "oldpagos"
    menu:
        '[custom1]
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_druidplanALL:
    label oldpagos_about_druidplan01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell them about the druid’s plan.')
        $ minutes += 5
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“I may know a way to help you with the plague,” you begin. Even before you end your story, various voices interrupt you with all sorts of queries, which results in a long and chaotic conversation - as their enthusiasm rises, more people approach the gate, chiming in with their doubts or asking for things that have been already explained. Through the hole in the gate, you see a swarm of shifting faces and clothes.
            '
            'It’s understandable that they’re worried. I try to tell them everything I know.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s understandable that they’re worried. I try to tell them everything I know.')
                $ quarters += 1
                menu:
                    'The locals spend most of the time arguing with each other about hope, desperation, doubt, and distrust. You’re even accused of trying to manipulate desperate souls. Reaching the point where you can move on takes you a good few minutes.
                    '
                    '“There isn’t much you can do from here, but as I’ve said, awakening the altar requires pneuma. If you’ve something I could use as a sacrifice, it will be a huge help.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There isn’t much you can do from here, but as I’ve said, awakening the altar requires magic. If you’ve something I could use as a sacrifice, it will be a huge help.”')
                        jump oldpagos_about_druidplan02
            'This is a waste of time. “Let me speak with one soul at a time. You can discuss it later on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is a waste of time. “Let me speak with one soul at a time. You can discuss it later on.”')
                menu:
                    '{color=#f6d6bd}Tertia{/color} once again shows up in the peephole, observing you attentively. “You’re right. Is there aught we can do to help you with awakening the altar?”
                    '
                    '“If you have any items filled with pneuma, I could use them as a sacrifice.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you have any items filled with pneuma, I could use them as a sacrifice.”')
                        jump oldpagos_about_druidplan02

    label oldpagos_about_druidplan02:
        $ minutes += 5
        if (oldpagos_reputation+appearance_charisma) >= 5:
            $ oldpagos_about_druidsplan = 2
            if pc_class == "warrior":
                $ custom1 = "You catch it before it lands on the ground. At first, you’re not sure what you’re looking at."
            else:
                $ custom1 = "It lands next to your boots. You crouch to pick it up, and at first you’re not sure what you’re looking at."
            menu:
                'Yet another long discussion occurs on the other side, though this time it’s more organized, with one soul speaking at a time. When {color=#f6d6bd}Tertia{/color} addresses you, there’s determination in her eyes.
                \n\n“There are no enchanters here, warden, and the magic potions we had were used to fight the plague. But my neighbors are willing to spare the last treasure they own. They trust ye.”
                \n\nAfter a few moments, a small, metal object is thrown toward you through the peephole. [custom1] It’s longer than a finger span, but thin, finished with a flattened edge for cutting. It occurs to you that it’s a simple chisel.
                '
                '“...Right.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Right.”')
                    jump oldpagos_about_awakeningaltar02
                'I say nothing.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                    jump oldpagos_about_awakeningaltar02
        else:
            $ oldpagos_about_druidsplan = 1
            menu:
                'Yet another long discussion occurs on the other side, though this time it’s more organized, with one soul speaking at a time. When {color=#f6d6bd}Tertia{/color} addresses you, there’s sadness in her eyes.
                \n\n“There are no enchanters here, warden. All the magic potions we had were used to fight the plague, and my neighbors don’t want to give away our last treasure to someone they don’t trust. I can’t make this decision for them.”
                '
                '“Fine. I hope you won’t regret it, though.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I hope you won’t regret it, though.”')
                    $ questionpreset = "oldpagos"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'She closes her eyes for a moment. “Me too.”
                        \n\nThe crowd starts to disperse.
                        '
                        '(oldpagos preset)':
                            pass
                '“Are you serious? You’d rather keep some {i}treasure{/i} than save your lives?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you serious? You’d rather keep some {i}treasure{/i} than save your lives?”')
                    $ oldpagos_reputation -= 1
                    $ questionpreset = "oldpagos"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'People on the other side fall silent. {color=#f6d6bd}The woman{/color} observes you with reluctance. “It’s not the way we do stuff. We won’t turn ourselves into mindless beasts.”
                        '
                        '(oldpagos preset)':
                            pass

label oldpagos_about_awakeningaltarALL:
    label oldpagos_about_awakeningaltar01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still need help with awakening the altar.”')
        $ oldpagos_about_druidsplan = 2
        if pc_class == "warrior":
            $ custom1 = "You catch it before it lands on the ground. At first, you’re not sure what you’re looking at."
        else:
            $ custom1 = "It lands next to your boots. You crouch to pick it up, and at first you’re not sure what you’re looking at."
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'There’s determination in her eyes. “And my neighbors are willing to give away the last treasure they own. They trust ye, warden.”
            \n\nAfter a few moments, a small, metal object is thrown toward you through the peephole. [custom1] It’s longer than a finger span, but thin, finished with a flattened edge for cutting. It occurs to you that it’s a simple chisel.
            '
            '“...Right.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Right.”')
                jump oldpagos_about_awakeningaltar02
            'I say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                jump oldpagos_about_awakeningaltar02

    label oldpagos_about_awakeningaltar02:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You hear an elderly man. “It belonged to my son, the greatest sculptor that has ever lived in {color=#f6d6bd}Old Págos{/color}, to Wright’s glory and our great joy.” His words are sonorous and solemn. “It’s filled with pneuma that makes its holder’s hands so powerful they can carve in granite, so precise they can write in glass!”
            \n\nThe tool is as warm as your own skin.
            '
            '“It’s better than nothing. Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s better than nothing. Thanks.”')
                $ oldpagos_reputation -= 1
                $ item_magicchisel = 1
                $ renpy.notify("You received a magic chisel.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a magic chisel.{/i}')
                $ questionpreset = "oldpagos"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You hear the resentful gasps as the crowd disperses. {color=#f6d6bd}Tertia{/color} returns to the peephole, giving you a harsh look.
                    '
                    '(oldpagos preset)':
                        pass
            '“I’ll honor your son’s memory by putting it to good use. You won’t regret this.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll honor your son’s memory by putting it to good use. You won’t regret this.”')
                $ oldpagos_reputation += 1
                $ item_magicchisel = 1
                $ renpy.notify("You received a magic chisel.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a magic chisel.{/i}')
                $ questionpreset = "oldpagos"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“Be blessed by The Good Architect,” the old man goes on, “as you ride through paths too dangerous for human shells. You’ve got our trust and gratitude, [pcname]!”
                    \n\nThe crowd disperses slowly. {color=#f6d6bd}Tertia{/color} returns to the peephole and gives you a curious, though kind look.
                    '
                    '(oldpagos preset)':
                        pass

label oldpagos_about_plague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about this illness. What does it do to you?”')
    $ oldpagos_plague_known = 1
    if quest_foggy1oldpagos == 1:
        $ renpy.notify("Journal updated: Check on Old Págos")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Old Págos{/i}')
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'She glances at someone or something that stands to her right. “It lasts a long time, even those who seem to avoid death remain weak for days. There are fevers, headaches, red faces, red eyes, and rash. Those whom we had to burn were sleeping and raving, unable to understand us, and got too weak to move, or even drink.”
        \n\nShe looks down. “Children and elderly suffer the most.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_harvest01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why don’t you harvest your crops?”')
    $ oldpagos_about_harvest = 1
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'Even though her cold gaze doesn’t break, her voice betrays her pain. “Some of our youth refuse to stay behind the walls. They say they need to leave before they fall sick. If we were to let them outside... One of them could refuse to come back.”
        \n\nYou frown. No, it wasn’t {i}pain{/i} what you’ve heard. It’s {i}shame{/i}.
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_asterionALL:
    label oldpagos_about_asterion01:
        $ oldpagos_about_asterion = 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not oldpagos_cured:
            $ custom11 = "eyes"
        else:
            $ custom11 = "look"
        menu:
            'You can’t tell anything from her [custom11]. “Isn’t he dead?”
            '
            '“What makes you think that?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What makes you think that?”')
                menu:
                    '“I’d say that about any traveler who {i}disappeared{/i} in the wilds. Wardens may know their roads, but they’re not above humans. Don’t you know the saying? {i}Wait two days for the lost, ten for the wounded, twenty for the ill and mad.{/i} Ye don’t wait for more.”
                    '
                    '“So you were waiting for him?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you were waiting for him?”')
                        jump oldpagos_about_asterion02
            '“I want to know for sure.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to know for sure.”')
                menu:
                    '“If he’s not, what else? Souls perish on the roads every day. We don’t wait for him anymore. The best ye can hope for is that he rode South.”
                    '
                    '“What is it that you {i}were{/i} waiting for?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So what is it that you {i}were{/i} waiting for?”')
                        jump oldpagos_about_asterion02

    label oldpagos_about_asterion02:
        $ quest_asterion_description08 = "In {color=#f6d6bd}Old Págos{/color} I heard that he was planning to restore the watchtower that stands at the eastern crossroads."
        $ renpy.notify("Journal updated: Find the Roadwarden")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        menu:
            '“That’s not much of a secret,” she looks to her right, then at you again. “Head far east, to the crossroads. Ye’ll find a watchtower, an old building made of our stone,” you notice the pride in her voice, “but hardly used since the war. Ya friend wanted to turn it into a shelter. Hire guards, patrol the roads... He took our key and rode away. He was meant to meet with us again, trade for materials and tools. Never happened.”
            '
            '“Any idea who else could have such a key?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who else could have such a key?”')
                jump oldpagos_about_asterion03
            '“He’s not my friend.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s not my friend.”')
                menu:
                    'She takes a step back. “So why would ye look for him?”
                    '
                    '“I’ll get paid for uncovering the truth.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll get paid for uncovering the truth.”')
                        menu:
                            'She narrows her eyes.
                            '
                            '“Any idea who else could have a key to that watchtower?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who else could have a key to that watchtower?”')
                                jump oldpagos_about_asterion03
                    '“If someone hurt him, I ought to bring the perpetrator to justice.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If someone hurt him, I ought to bring the perpetrator to justice.”')
                        $ oldpagos_reputation += 1
                        menu:
                            'She observes you closely. “It very much may be the case. There are many pagans in the North, bandits, even. Finding out what’s true, who’s to be trusted... It can wear out even the brightest souls.”
                            '
                            '“Any idea who else could have a key to that watchtower?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who else could have a key to that watchtower?”')
                                jump oldpagos_about_asterion03
                    '“I don’t like the idea of living in a corner of The Land where roadwardens just {i}disappear{/i}.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like the idea of living in a corner of The Land where roadwardens just {i}disappear{/i}.”')
                        menu:
                            'She nods. “And neither do I. I hope you’ll do better than he did.”
                            '
                            '“Any idea who else could have a key to that watchtower?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who else could have a key to that watchtower?”')
                                jump oldpagos_about_asterion03
                    '“It’s my duty as a roadwarden. He may be in need, and if so, I should help him.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s my duty as a roadwarden. He may be in need, and if so, I should help him.”')
                        $ oldpagos_reputation += 1
                        if not oldpagos_cured:
                            $ custom11 = "Her eyes and voice smile at you."
                        else:
                            $ custom11 = "She gives you a kind smile."
                        menu:
                            '[custom11] “An honorable cause. Who knows, maybe in a different world our paths would not just cross, but aim in the same direction.”
                            '
                            '“Any idea who else could have a key to that watchtower?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who else could have a key to that watchtower?”')
                                jump oldpagos_about_asterion03

    label oldpagos_about_asterion03:
        $ questionpreset = "oldpagos"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ galerocks_watchtowerkey_knows = 1
        menu:
            '“Before it was completed, the builders were spending the rainy days in the coastal village in the far north. {color=#f6d6bd}Gale Rocks{/color}, it’s called. Ask there.”
            '
            '(oldpagos preset)':
                pass

label oldpagos_about_watchtower_directions01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Which way would you take if you were to travel to the watchtower?”')
    $ oldpagos_about_watchtower_directions = 1
    if not description_quintus01:
        $ description_quintus01 = "According to {color=#f6d6bd}Tertia{/color}, he used to take care of the western gate that leads to the heart of the forest."
    $ description_quintus06 = "According to {color=#f6d6bd}Tertia{/color}, “he may be not of the sharpest wits, but he’s loyal to his duty and returns kindness with kindness, like we all should.”"
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ shortcut_pcknowsabout = 1
    if oldpagos_about_quintus:
        $ custom1 = "the one guarded by {color=#f6d6bd}Quintus{/color}. It’s the most dangerous path, but ya palfrey may be just fast enough to get ye through.”\n\nYou ask her what are her thoughts on {color=#f6d6bd}the gatekeeper{/color}, and she gives you a warm look. “He may be not of the sharpest wits, but he’s loyal to his duty and returns kindness with kindness, like we all should.”"
    else:
        $ custom1 = "though opening it on ya own may not be easy. It used to be that our guards were keeping it open for the travelers, but the last one that we sent away, {color=#f6d6bd}Quintus{/color}, is either dead, or seeking refuge in another village. Still, behind the gate ye’ll find the shortcut. It’s a dangerous path, but ya palfrey may be just fast enough to get ye to the other end.”\n\nYou ask her what can she tell you about this {color=#f6d6bd}gatekeeper{/color}, and she gives you a warm look. “He may be not of the sharpest wits, but he’s loyal to his duty and returns kindness with kindness, like we all should.”"
    menu:
        '“The northern route, most likely. There’s more tribes there. But the eastern road is dangerous, no matter from which way yer going to enter it. But if ye care about time,” she hesitates, “ye could check on the {i}gate{/i}, [custom1]
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_eudocia_parents01:
    $ oldpagos_about_eudocia_parents = 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color}, the enchantress from the East, wants to know if {color=#f6d6bd}Eulalia{/color} and {color=#f6d6bd}Ireneus{/color} have avoided the sickness.”')
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'A long, uncomfortable silence. “She’s too late. They were asking for their daughter in their nightmares, before the illness took away their tongues. We burned both of them on the same day, if it means aught to her.”
        \n\nShe looks down. “Tell her I’m... sorry for her loss. I hope she found the peace she was looking for.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_recruitahunter01:
    $ quest_recruitahunter_spokento_tertia = 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Erastos{/color}?”')
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'She speaks slowly. “Remind me who that is?” After your brief description, she still needs to ask someone for advice. “I believe he was here, yes, but soon left to ask {color=#f6d6bd}the monks{/color} for their guidance. Rather unusual,” her voice gets cold, “for a {i}pagan{/i}.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_trade01:
    $ oldpagos_about_trade = 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have anything for sale? Maybe some food rations?”')
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        '“We hardly have enough for ourselves. We used to get supplies for rocks and sculptures, but the monks advised us against it. Our wares may carry the illness.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_quintus01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met {color=#f6d6bd}Quintus{/color}, the gatekeeper. He’s doing... fine.”')
    $ oldpagos_about_quintus = 1
    $ oldpagos_reputation += 1
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quintus_friendswithdalit += 1
    menu:
        '“So he’s still with us!” Her voice rings with enthusiasm. She asks about his well-being, reacting to your story with a mixture of worry and joy.
        \n\n“I’m sorry to hear about his nose. I hope he knows what he’s doing, in his position I would just look for work in {color=#f6d6bd}Howler’s Dell{/color}, or ask for help from his friends at {color=#f6d6bd}Pelt{/color}.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_warningothervillages01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to many settlements, warning the locals about the plague. You don’t have to worry about their safety.”')
    jump oldpagos_about_warningothervillages02
    label oldpagos_about_warningothervillages01lie:
        $ pc_lies += 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’ve been to many settlements, warning the locals about the plague. You don’t have to worry about their safety.”')
        jump oldpagos_about_warningothervillages02
    label oldpagos_about_warningothervillages02:
        $ oldpagos_about_oldpagos_plague_warnedplaces = 1
        $ oldpagos_reputation += 2
        $ questionpreset = "oldpagos"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if not oldpagos_cured:
            $ custom11 = "she bows her head"
        else:
            $ custom11 = "she bows gently"
        menu:
            '“Thank ye, warden,” [custom11]. “I’ll ask the council to rethink our isolation - with the gates and doors of our neighbors closed, we could start seeking food after all, maybe even send outside a few hunting trips.”
            '
            '(oldpagos preset)':
                pass

label oldpagos_about_ibex01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found an ibex marked with a red knot. Was it any of yours?”')
    $ oldpagos_reputation += 1
    $ questionpreset = "oldpagos"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_ibex = 1
    if not oldpagos_cured:
        $ custom11 = "Her brown eyes widen"
    else:
        $ custom11 = "She cocks her head to the left as her brown eyes widen"
    menu:
        '[custom11]. “Ye found it? Is it safe?” After you mention the kobolds, she nods. “We had no hopes of seeing it again. Creatures who are used to living with humans won’t survive on their own. I’ll let the others know. Thank ye.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_quest_orentius_thais_description01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a delicate matter to discuss. It’s about the necromancers of {color=#f6d6bd}White Marshes{/color}.”')
    $ questionpreset = "oldpagos"
    $ minutes += 5
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quest_orentius_thais_description03a02 = "{color=#f6d6bd}Old Págos{/color} doesn’t trust {color=#f6d6bd}Thais’{/color} judgment, but also won’t support the people of {color=#f6d6bd}White Marshes{/color}."
    $ renpy.notify("Journal updated: Orentius, the Necromancer")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
    if not oldpagos_cured:
        $ custom11 = "returns to the peephole, giving you a vigilant look. “Be careful around the people of {color=#f6d6bd}Howler’s{/color},” her voice is hesitant, but she looks straight into your eyes."
    else:
        $ custom11 = "returns to the gate, giving you a vigilant look as she adjusts her armor. “Be careful around the people of {color=#f6d6bd}Howler’s{/color},” her voice is hesitant, but she looks straight into your eyes."
    menu:
        'You don’t go far with your explanations before {color=#f6d6bd}Tertia{/color} chips in. “Yer talking about a raid? Such decisions belong to the entire tribe. Wait here.”
        \n\nAfter a few minutes, a small crowd gathers beneath the gate and an old man encourages you to start from the beginning. You try, but the locals are eager to argue with each other, often interrupting you. Because of their heavy accents, you struggle with following their debate, but you catch the tribe’s anger, fear, and shame.
        \n\nFinally, a vote takes place - with raised hands, in silence. An older woman clears her throat, addressing you without approaching the peephole.
        \n\n“Shadows fill those who awaken the dead, no matter their reasons, yet there’s no wickedness greater than the intrigues of {color=#f6d6bd}Thais{/color}, the traitor. We don’t trust the other tribes, and we’ve got to endure our own isolation. We won’t help ye, warden, but we will also not stop ye.”
        \n\n{color=#f6d6bd}The brown-eyed woman{/color} [custom11] “There are venom fangs behind their mask.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_nomoreundeadALL:
    label oldpagos_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead of {color=#f6d6bd}White Marshes{/color} are gone. I hope you’ll have an opportunity to trade with the tribe in spring.”')
        $ oldpagos_about_nomoreundead = 1
        $ oldpagos_reputation += 2
        $ minutes += 10
        $ questionpreset = "oldpagos"
        menu:
            'She observes you for a good few heartbeats, then turns around and shouts cheerfully. “The empty ones are gone!”
            \n\nThe locals start a commotion, gathering around the gate to hear your tale. They start an avalanche of questions, but after you satisfy their curiosity, {color=#f6d6bd}Tertia’s{/color} eyes are relieved. “To think ye {i}convinced{/i} them,” she blinks. “May The Wright bring a rapid end upon {color=#f6d6bd}the necromancer{/color}.”
            '
            '(oldpagos set)':
                pass

    label oldpagos_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead of {color=#f6d6bd}White Marshes{/color} are gone, but I wouldn’t expect the tribe to be open to trade in the near future.”')
        $ oldpagos_about_nomoreundead = 2
        $ oldpagos_reputation += 3
        $ minutes += 10
        $ questionpreset = "oldpagos"
        menu:
            'She observes you for a good few heartbeats, then turns around and shouts cheerfully. “The empty ones are gone!”
            \n\nThe locals start a commotion, gathering around the gate to hear your tale. They start an avalanche of questions, but after you satisfy their curiosity, {color=#f6d6bd}Tertia’s{/color} eyes are relieved. “To think ye brought {color=#f6d6bd}the necromancer{/color} to justice,” she blinks. “May The Wright guide you further!”
            '
            '(oldpagos set)':
                pass

    label oldpagos_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Since you’re placed closely to {color=#f6d6bd}White Marshes{/color}, you must double your guards. The village is overtaken by undead.”')
        $ oldpagos_about_nomoreundead = 3
        $ oldpagos_reputation += 1
        $ minutes += 10
        $ questionpreset = "oldpagos"
        if not oldpagos_cured:
            menu:
                'You hear the murmuring of the crowd. {color=#f6d6bd}Tertia{/color} freezes, then looks at the ground. “What happened to the tribe?”
                \n\nThe locals start a commotion, gathering around the gate to hear your tale. Their questions are sorrowful, but after you satisfy their curiosity, you hear a few words of encouragement. {color=#f6d6bd}The brown-eyed woman{/color} maintains her strong voice. “A high price for clearing The Land of necromancers, but such was your duty,” she pauses. “I just wish our old wounds could have healed first. Yet, it was their decision, not ours, not yours.”
                '
                '(oldpagos set)':
                    pass
        else:
            menu:
                'The crowd murmurs. {color=#f6d6bd}Tertia{/color} lowers her spear, then looks at the ground. “What happened to the tribe?”
                \n\nThe locals start a commotion, gathering around the gate to hear your tale. Their questions are sorrowful, but after you satisfy their curiosity, you hear a few words of encouragement. {color=#f6d6bd}The brown-eyed woman{/color} maintains her strong voice. “A high price for clearing The Land of necromancers, but such was your duty,” she pauses. “I just wish our old wounds could have healed first. Yet, it was their decision, not ours, not yours.”
                '
                '(oldpagos set)':
                    pass

label oldpagosreturningkey01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I happened to recover the key you gave {color=#f6d6bd}Asterion{/color}. I’m ready to return it.”')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ oldpagos_about_keys = 1
    $ oldpagos_reputation += 2
    if not oldpagos_cured:
        $ custom11 = "voice"
    else:
        $ custom11 = "look"
    menu:
        '“Truly?” {color=#f6d6bd}Tertia’s{/color} [custom11] gets warmer. “Place it on the ground, I’ll pick it up later on. I appreciate your trouble.”
        '
        'I put it on the ground. “It’s not going to be that useful, though. The door is already broken.”' if watchtower_open == "axe":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put it on the ground. “It’s not going to be that useful, though. The door is already broken.”')
            $ oldpagos_reputation -= 2
            $ renpy.notify("You lost the Asterion’s key.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the Asterion’s key.{/i}')
            $ item_asterionkey = 0
            $ questionpreset = "oldpagos"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'She speaks with a mixture of amusement and reprimand. “Then I’m even more surprised that ye decided to bother with it. Well, we can still melt it.”
                '
                '(oldpagos preset)':
                    pass
        '(lie) “May it serve you well.”' if watchtower_open == "axe":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “May it serve you well.”')
            $ pc_lies += 1
            $ renpy.notify("You lost the Asterion’s key.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the Asterion’s key.{/i}')
            $ item_asterionkey = 0
            jump oldpagosafterinteraction01
        'I do as she says. “Very well.”' if watchtower_open != "axe":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do as she says. “Very well.”')
            $ renpy.notify("You lost the Asterion’s key.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the Asterion’s key.{/i}')
            $ item_asterionkey = 0
            jump oldpagosafterinteraction01

label oldpagos_about_bogroadmonster01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That weird creature from the bogs you told me about... I’ve quite a story for you.”')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ oldpagos_reputation += 1
    $ minutes += 8
    if not oldpagos_cured:
        $ custom11 = "you’ve never heard before"
    else:
        $ custom11 = "you don’t recognize"
    menu:
        '{color=#f6d6bd}Tertia{/color} reacts to your story with a wholehearted laughter, and as a group of the villagers gathers at the gate, you’re asked to repeat the whole thing. Raising your voice, you tell about the dark cat and its gray companion, not forgetting about your desperate attempt to save a lost soul.
        \n\n“But what happened then,” asks a boy [custom11]. “D’ye kill the cat, warden?”
        '
        '(lie) “But of course. I didn’t have much of a choice.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “But of course. I didn’t have much of a choice.”')
            $ oldpagos_reputation += 1
            $ pc_lies += 1
            $ questionpreset = "oldpagos"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ oldpagos_about_bogroadcat = 1
            menu:
                '“Poor thing,” says the kid, but is then reprimanded by an old woman. “Nah, hush! Such is our duty against the monsters from the shadows!”
                \n\n“So say Wright’s Tablets,” adds another elder. “A beast of such sage schemes is naught but a threat to all of us, more a catfolk, than a cat. For this is how one recons if a beastfolk is a hungry savage, or a mug that can be reasoned with: they run on all fours to hunt, but on two to listen.”
                \n\nThe mumbling of the other villagers suggests not all of them agree with these words. As they argue, {color=#f6d6bd}the brown-eyed woman{/color} returns her glance to you.
                '
                '(oldpagos preset)':
                    pass
        '“No... But it’s very much dead.” I tell them about the saurian.' if bogroad_cathp <= 0:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No... But it’s very much dead.” I tell them about the saurian.')
            $ oldpagos_reputation += 1
            $ questionpreset = "oldpagos"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ oldpagos_about_bogroadcat = 1
            menu:
                '“Poor thing,” says the kid, but is then reprimanded by an old woman. “Nah, hush! A good thing happens when the monsters from the shadows kill each other!”
                \n\n“And we ought to be grateful for it,” adds another elder. “A beast of such sage schemes is naught but a threat to all of us, more a catfolk, than a cat. For this is how one recons if a beastfolk is a hungry savage, or a mug that can be reasoned with: they run on all fours to hunt, but on two to listen.”
                \n\nThe mumbling of the other villagers suggests not all of them agree with these words. As they argue, {color=#f6d6bd}the brown-eyed woman{/color} returns her glance to you.
                '
                '(oldpagos preset)':
                    pass
        '(lie) “It ran away. I’m sure it’s fine.”' if bogroad_cathp <= 0:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “It ran away. I’m sure it’s fine.”')
            $ pc_lies += 1
            label oldpagos_about_bogroadmonster01a:
                $ questionpreset = "oldpagos"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ oldpagos_about_bogroadcat = 1
                menu:
                    '“Oh, I see!” The kid responds enthusiastically, but is then reprimanded by an old woman. “Nah, hush! Who knows whom it will try to murder next time! We ought to wish doom upon the monsters from the shadows!”
                    \n\n“So say Wright’s Tablets,” adds another elder. “A beast of such sage schemes is naught but a threat to all of us, more a catfolk, than a cat. For this is how one recons if a beastfolk is a hungry savage, or a mug that can be reasoned with: they run on all fours to hunt, but on two to listen.”
                    \n\nThe mumbling of the other villagers suggests not all of them agree with these words. As they argue, {color=#f6d6bd}the brown-eyed woman{/color} returns her glance to you.
                    '
                    '(oldpagos preset)':
                        pass
        '“It ran away. I’m sure it’s fine.”' if bogroad_cathp > 0:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It ran away. I’m sure it’s fine.”')
            jump oldpagos_about_bogroadmonster01a

label oldpagos_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}High Island{/color}.”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_highisland = 1
    $ questionpreset = "oldpagos"
    if not oldpagos_cured:
        menu:
            '“Give me a moment,” she steps away from the peephole and asks a few people about something you can’t fully hear. Once she’s back, there’s no joy in her eyes. “The illness already has taken whom ye wanted to speak with. The old sailors from {color=#f6d6bd}Howler’s Dell{/color}, husband and wife, who found the true word of The Wright. Now gone,” her voice is at the brink of cracking.
            \n\nShe closes her brown eyes and regains her composure with a few breaths. “Ye may learn more in the monastery, but the monks rarely share their secrets.”
            '
            '(oldpagos preset)':
                pass
    else:
        menu:
            '“Give me a moment,” she walks deeper into the village and asks a few people about something you can’t fully hear. Once she’s back, there’s no joy in her eyes. “The illness already has taken whom ye wanted to speak with. The old sailors from {color=#f6d6bd}Howler’s Dell{/color}, husband and wife, who found the true word of The Wright. Now gone,” her voice is at the brink of cracking.
            \n\nShe closes her brown eyes and regains her composure with a few breaths. “Ye may learn more in the monastery, but the monks rarely share their secrets.”
            '
            '(oldpagos preset)':
                pass

label oldpagos_about_missinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are there any hunters from {color=#f6d6bd}Creeks{/color} locked in there with you?”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_missinghunters = 1
    $ questionpreset = "oldpagos"
    menu:
        'She frowns. “You’re the first soul who came here in a very long time.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_bandits01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you bothered by any bandits in recent seasons?”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_bandits = 1
    $ questionpreset = "oldpagos"
    menu:
        '“Not in years, warden. They did attack us on the road once before, but their little pack won’t come here.” At first her tone is gentle, but after she blinks twice, it turns solemn. “Or they would face our anger. Our walls fear only dragons, our blades are made of steel.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_matchmaking01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- People from the other tribes are looking for spouses.”')
    $ renpy.notify("Journal updated: Matchmaking")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_matchmaking = 1
    if oldpagos_cured:
        $ custom1 = "She flinches, as if the question reached her from another realm. “Ye gave us hope for the next season, but we still don’t know if the winter will spare us. I can’t offer ye any promises for the tribes, and we ought to reconsider,” pause, “who our friends are.”"
    else:
        $ custom1 = "She blinks, as if the question reached her from another realm. “We can’t be sure of the next spring, even less so that our gates will ever open. I can’t offer ye any promises for the tribes.”"
    $ questionpreset = "oldpagos"
    menu:
        '[custom1]
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_steephouse_eudocia01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color} has a message for you. {i}The warden ought to know about {color=#f6d6bd}Steep House{/color}, {color=#f6d6bd}Little Otter{/color}{/i}.”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ oldpagos_about_steephouse_eudocia = 1
    $ oldpagos_about_steephouse_reputation -= 2
    $ questionpreset = "oldpagos"
    if not oldpagos_cured:
        $ custom11 = "Her eyes are wide-open"
    else:
        $ custom11 = "She squeezes her spear tightly"
    menu:
        '[custom11]. “{color=#f6d6bd}Raccoon{/color} isn’t one of us anymore,” she starts with confidence, then pauses. “But... I’ll consider her words.”
        '
        '(oldpagos preset)':
            pass

label oldpagos_about_steephouseALL:
    label oldpagos_about_steephouse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You told me that {color=#f6d6bd}Thais{/color} had grand plans ten years ago. Is this related to the ruins in the south?”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ oldpagos_about_steephouse_gray = 1
        $ questionpreset = "oldpagos"
        menu:
            'Her breaths get heavy. “Warden. Studying the past is a part of ya duties, I realize that,” she closes her eyes, “but ye’ll find naught of worth in that place, and naught that can be fixed. {i}My{/i} duty is to keep everyone safe, and I can do so only through silence.”
            '
            '(oldpagos preset)':
                pass

    label oldpagos_about_steephouse02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the hourglass on my neck and show it to her. “For Wright’s truth, tell me what happened to the village in the south. These people deserve justice!”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She observes the sacred symbol with dread. “Ye... Yer right, [pcname],” she glances at her tribesfolk, then back at you. “The village of {color=#f6d6bd}Howler’s Dell{/color} murdered the people of {color=#f6d6bd}Steep House{/color}. {color=#f6d6bd}Thais{/color} gave them an order, and they said {i}yes.{/i}”
            '
            '“...Go on.”':
                jump oldpagos_about_steephouse03

    label oldpagos_about_steephouse02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Please, {color=#f6d6bd}Tertia{/color}. I need to learn the truth about the village in the south. These people deserve justice.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“The dead need no justice, [pcname],” she starts, but as you spot echoes of pain in her voice, you pressure her further. She glances at her tribesfolk, then back at you. “The village of {color=#f6d6bd}Howler’s Dell{/color} murdered the people of {color=#f6d6bd}Steep House{/color}. {color=#f6d6bd}Thais{/color} gave them an order, and they said {i}yes.{/i}”
            '
            '“...Go on.”':
                label oldpagos_about_steephouse03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Go on.”')
                    $ oldpagos_about_steephouse = 1
                    if not oldpagos_cured:
                        $ custom11 = "She lowers her eyes"
                    else:
                        $ custom11 = "She lowers her eyes and spear"
                    menu:
                        'With every breath, her words get stronger. “{color=#f6d6bd}Thais{/color} offered the tribes to follow her. In exchange for taxes, her soldiers and druids would assist our walls, secure the roads for {i}our{/i} sake, she claimed. Her people are strong, and well guarded. She can send away twenty, thirty souls, and would still be stronger than us, even than {color=#f6d6bd}Gale Rocks{/color}.”
                        \n\nShe observes you keenly, drawing your eyes. “{color=#f6d6bd}Steep House{/color} used to be close with {color=#f6d6bd}Howler’s{/color}, a smaller part of the same tribe. But they were first to see that {color=#f6d6bd}Thais’{/color} soul was one of constant hunger and fear. They had refused, and their older sibling raided them, like in the days before emperors. They were crushed.”
                        \n\nHer voice is close to a shout. “{color=#f6d6bd}Steep House{/color} has surrendered, but the raiders pushed them further, burned their homes, took their food. They {i}had to{/i} cut down their forest garden to restore their walls and supplies, but the beasts didn’t forgive them. The wave of monsters followed, and only a few souls survived.”
                        \n\n[custom11]. “We had no time to bring them even one loaf of bread. And they were gone. {color=#f6d6bd}Thais’{/color} stopped sending us messengers, I don’t know why. But it’s good she did,” her brown eyes return to you, “or we would kill them.”
                        '
                        '“Thank you for telling me this.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for telling me this.”')
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            $ quest_ruins_description_truestory = "{color=#f6d6bd}Tertia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                            $ description_ruinedvillage02 = "{color=#f6d6bd}Tertia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                            $ description_thais06 = "{color=#f6d6bd}Tertia{/color} blames her for destroying the southern village."
                            $ renpy.notify("Journal updated: The Ruined Village")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                            $ ruinedvillage_truth = 1
                            $ ruinedvillage_name = "Steep House"
                            $ questionpreset = "oldpagos"
                            menu:
                                'Her eyes sink in melancholy. “We can’t reach {color=#f6d6bd}Thais{/color}, and we won’t start a war with her people. But they’re murderers.”
                                '
                                '(oldpagos preset)':
                                    pass
                        '“So you didn’t try to stop her?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you didn’t try to stop her?”')
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            $ oldpagos_reputation -= 2
                            $ quest_ruins_description_truestory = "{color=#f6d6bd}Tertia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                            $ description_ruinedvillage02 = "{color=#f6d6bd}Tertia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
                            $ description_thais06 = "{color=#f6d6bd}Tertia{/color} blames her for destroying the southern village."
                            $ renpy.notify("Journal updated: The Ruined Village")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                            $ ruinedvillage_truth = 1
                            $ ruinedvillage_name = "Steep House"
                            $ questionpreset = "oldpagos"
                            menu:
                                'There’s an angry spark in her eye. “{i}We{/i} didn’t know her plans. And {i}I{/i} was but a child.”
                                '
                                '(oldpagos preset)':
                                    pass

label oldpagos_about_othervillagesALL:
    label oldpagos_about_othervillages01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you want me to ask the other villages for help?”')
        jump oldpagos_about_othervillages01after
        label oldpagos_about_othervillages01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why didn’t you want me to ask the other villages for help?”')
            jump oldpagos_about_othervillages01after
        label oldpagos_about_othervillages01after:
            $ oldpagos_about_othervillages = 1
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            if oldpagos_about_nomoreundead == 3:
                $ custom1 = "were"
            else:
                $ custom1 = "are"
            menu:
                '“There’s no love between us and them. We don’t share drinks, stories, or dances. If it weren’t for marriages, our children would never see each other, and if it wasn’t for trade, we could just as well live on a mountain peak. They need our stone, we need fishes and salt from {color=#f6d6bd}Gale Rocks{/color}, game meat from {color=#f6d6bd}Creeks{/color}, and grain from {color=#f6d6bd}Howler’s Dell{/color}. But all of them are harpies, led by greed and lust, the same ills that wounded our grandparents.”
                \n\nShe hesitates and looks to her left. “Still... The wicked souls of {color=#f6d6bd}White Marshes{/color} [custom1] even more burrowed in shadows.”
                '
                '“Sounds like you hold a grudge against them.”' if oldpagos_about_nomoreundead != 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds like you hold a grudge against them.”')
                    jump oldpagos_about_othervillages01afterpart2
                '“Sounds like you have a lot to say about the tribes.”' if oldpagos_about_nomoreundead == 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds like you have a lot to say about the tribes.”')
                    label oldpagos_about_othervillages01afterpart2:
                        if (oldpagos_reputation+appearance_charisma) < 4:
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            $ questionpreset = "oldpagos"
                            $ oldpagos_about_othervillages_gray = 1
                            menu:
                                'She takes a deep breath. “Yet I won’t spread any rumors. As much as it saddens me, they need us to survive, and we need them. And yer even stranger to us than they are.”
                                '
                                '(oldpagos preset)':
                                    pass
                        else:
                            menu:
                                '“I shouldn’t gossip... But I can try to share with ye the truth. Yer a warden, after all.”
                                '
                                '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                                    jump oldpagos_about_4villages02howlers
                                '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                                    jump oldpagos_about_4villages02marshes
                                '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                                    jump oldpagos_about_4villages02galerocks
                                '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                                    jump oldpagos_about_4villages02creeks
                                '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                                    jump oldpagos_about_4villages02greenmountain
                                '“I’ve no more questions.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                                    jump oldpagosafterinteraction01

    label oldpagos_about_4villages01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to hear what you have to say about the other villages.”')
        if (oldpagos_reputation+appearance_charisma) < 4:
            $ questionpreset = "oldpagos"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ oldpagos_about_othervillages_gray = 1
            menu:
                '“I won’t spread any rumors. As much as it saddens me, they need us to survive, and we need them. And yer even stranger to us than they are.”
                '
                '(oldpagos preset)':
                    pass
        else:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                '“Which ones?”
                '
                '“Howler’s Dell.”' if not oldpagos_about_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Howler’s Dell.”')
                    jump oldpagos_about_4villages02howlers
                '“White Marshes.”' if not oldpagos_about_whitemarshes:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “White Marshes.”')
                    jump oldpagos_about_4villages02marshes
                '“Gale Rocks.”' if not oldpagos_about_galerocks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gale Rocks.”')
                    jump oldpagos_about_4villages02galerocks
                '“Creeks.”' if not oldpagos_about_creeks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Creeks.”')
                    jump oldpagos_about_4villages02creeks
                '“The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The Tribe of The Green Mountain.”')
                    jump oldpagos_about_4villages02greenmountain
                '“I’ve no more questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                    jump oldpagosafterinteraction01

    label oldpagos_about_4villages02howlers:
        $ oldpagos_about_4villages += 1
        $ oldpagos_about_howlersdell += 1
        $ minutes += 3
        $ description_thais05 = "I heard that ten years ago she tried to start a pact that was meant to unite the villages of the North, but was unable to make her neighbors a tempting enough offer."
        if quest_ruins == 1 and quest_ruins_description01 and not quest_ruins_10yclue01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue01 = "I heard that {color=#f6d6bd}Thais{/color} tried to start a pact that was meant to unite the local tribes, but it turned out to be a failure."
        $ description_howlersdell05 = "The locals are following the teachings of a group of druids."
        $ description_thais11 = "According to {color=#f6d6bd}Tertia{/color}, “her laughter is as hollow as her soul.”"
        $ description_howlersdell03 = "According to {color=#f6d6bd}Tertia{/color}, “they have food, riches, mead, and pretty houses. But all of those carry poison, and this poison is what leads them.”"
        menu:
            '“They’re the closest village, ye can get there riding south from the crossroads with the four signposts. But {i}don’t{/i} trust them,” she gives you a piercing gaze. “They have an order of druids who bow to animals and dead spirits, and their mayor, {color=#f6d6bd}Thais{/color}, has too many grand ideas in her head and a tongue dancing to lies. Ten years ago, she tried to tie the tribes in the North with a pact, yet wanted to grasp all the wealth, telling us we should pay {i}her{/i} for protection,” her voice rises. “Her laughter is as hollow as her soul.”
            \n\nLong pause “Don’t let them cloud ya eyes. They have food, riches, mead, and pretty houses. But all of those carry poison, and this poison is what leads them.”
            '
            '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                jump oldpagos_about_4villages02howlers
            '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                jump oldpagos_about_4villages02marshes
            '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                jump oldpagos_about_4villages02galerocks
            '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                jump oldpagos_about_4villages02creeks
            '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                jump oldpagos_about_4villages02greenmountain
            '“I’ve no more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                jump oldpagosafterinteraction01

    label oldpagos_about_4villages02marshes:
        $ oldpagos_about_4villages += 1
        $ oldpagos_about_whitemarshes += 1
        if oldpagos_about_nomoreundead == 1 or oldpagos_about_nomoreundead == 2:
            $ minutes += 3
            menu:
                '“Ye know that rotten place better than any one of us. Such a deceiving name!” There’s fury in her eyes, her voice raises. “We refused to trade with them even before that priest called himself a {i}prophet{/i}. They swim in death, and will soon drown.”
                \n\nYou ask her a few questions, but most of her words are little more than an ardent condemnation.
                '
                '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                    jump oldpagos_about_4villages02howlers
                '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                    jump oldpagos_about_4villages02marshes
                '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                    jump oldpagos_about_4villages02galerocks
                '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                    jump oldpagos_about_4villages02creeks
                '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                    jump oldpagos_about_4villages02greenmountain
                '“I’ve no more questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                    jump oldpagosafterinteraction01
        elif oldpagos_about_nomoreundead == 3:
            menu:
                'Her voice turns grim. “Don’t ask me to badmouth the dead, or they’ll hear us.”
                '
                '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                    jump oldpagos_about_4villages02howlers
                '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                    jump oldpagos_about_4villages02marshes
                '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                    jump oldpagos_about_4villages02galerocks
                '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                    jump oldpagos_about_4villages02creeks
                '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                    jump oldpagos_about_4villages02greenmountain
                '“I’ve no more questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                    jump oldpagosafterinteraction01
        else:
            $ description_orentius04 = "According to {color=#f6d6bd}Tertia{/color}, he’s {i}a pagan blinded by his wicked wits, rotten to the core{/i}."
            $ description_whitemarshes02 = "The locals use the awoken undead to do their bidding."
            $ minutes += 3
            $ oldpagos_about_bogroadcat_introduction = 1
            menu:
                '“Such a deceiving name for that dark place, rotten to the core, led by a pagan blinded by his wicked wits. His followers are closer to evil spirits than humans, for they use the empty ones as their tools.” There’s fury in her eyes, her voice raises. “We refused to trade with them even before that priest called himself a {i}prophet{/i}. They swim in death, and will soon drown.”
                \n\nYou ask her a few questions, but most of her words are little more than an ardent condemnation. One part in particular draws your attention:
                \n\n“The road through the bogs is dangerous, spiked with weird beasts. Some of them yell with human-like voices, luring travelers away from the main path. When ya knees are in water, they, these beasts, jump from a tree on ya back, biting ya skin off. Even {color=#f6d6bd}White Marshes{/color} are little more than a trap set in the woods.”
                '
                '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                    jump oldpagos_about_4villages02howlers
                '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                    jump oldpagos_about_4villages02marshes
                '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                    jump oldpagos_about_4villages02galerocks
                '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                    jump oldpagos_about_4villages02creeks
                '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                    jump oldpagos_about_4villages02greenmountain
                '“I’ve no more questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                    jump oldpagosafterinteraction01

    label oldpagos_about_4villages02galerocks:
        $ oldpagos_about_4villages += 1
        $ oldpagos_about_galerocks += 1
        $ banditshideout_bandits_pchearedabout = 1
        $ banditshideout_galerocks_tiestobandits = 1
        $ description_galerocks14 = "According to {color=#f6d6bd}Tertia{/color}, “they follow Wright’s teachings, work hard and live humbly. We used to trade with them and take our clothes to {color=#f6d6bd}Rufina{/color} for fixing, but they betrayed our trust and if it weren’t for the plague, we’d be sharpening our blades.”"
        $ minutes += 3
        if not oldpagos_cured:
            $ custom11 = "You ask her to share with you the entire story, which instead is told by the voice of a young man. He claims that his group was transporting a statue ordered to the tribe of {color=#f6d6bd}Creeks{/color}, yet during their stay in the tavern at the northern road, it “mysteriously” disappeared."
        else:
            $ custom11 = "You ask her to share with you the entire story, which instead is told by a young man. He claims that his group was transporting a statue ordered to the tribe of {color=#f6d6bd}Creeks{/color}, yet during their stay in the tavern at the northern road, it “mysteriously” disappeared."
        menu:
            '“It’s in the North, just on the coast. They follow Wright’s teachings, work hard and live humbly. We used to trade with them and take our clothes to {color=#f6d6bd}Rufina{/color} for fixing, but they betrayed our trust and if it weren’t for the plague, we’d be sharpening our blades.”
            \n\n[custom11]
            \n\n“It must be the bandits’ doing,” adds {color=#f6d6bd}Tertia{/color}. “They keep spreading their arms wider, but we won’t allow them to stay untouched, with or without {color=#f6d6bd}Gale Rocks’{/color} help.”
            '
            '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                jump oldpagos_about_4villages02howlers
            '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                jump oldpagos_about_4villages02marshes
            '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                jump oldpagos_about_4villages02galerocks
            '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                jump oldpagos_about_4villages02creeks
            '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                jump oldpagos_about_4villages02greenmountain
            '“I’ve no more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                jump oldpagosafterinteraction01

    label oldpagos_about_4villages02creeks:
        $ oldpagos_about_4villages += 1
        $ oldpagos_about_creeks += 1
        $ creeks_reasonstojoin_creeksaboutlackingwall += 1
        $ description_creeks10 = "According to {color=#f6d6bd}Tertia{/color}, “they wouldn’t be great neighbors or friends. They drink a lot, hunt for sport, die often and give birth to many children. I wouldn’t rely on them.”"
        $ minutes += 3
        menu:
            '“I don’t know much about them. It’s a small village in the far east, younger than me. They came here as refugees from the war, and now hunt for wild meat and pelts, but have got almost no dragon bones to spare. When they tried to get our bricks, we had to refuse.”
            \n\nYou ask her a few more questions, but she cocks her head and gives you a bored look. “We’ve got little reason to travel so far. And they wouldn’t be great neighbors or friends. They drink a lot, hunt for sport, die often and give birth to many children. I wouldn’t rely on them.”
            '
            '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                jump oldpagos_about_4villages02howlers
            '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                jump oldpagos_about_4villages02marshes
            '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                jump oldpagos_about_4villages02galerocks
            '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                jump oldpagos_about_4villages02creeks
            '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                jump oldpagos_about_4villages02greenmountain
            '“I’ve no more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                jump oldpagosafterinteraction01

    label oldpagos_about_4villages02greenmountain:
        $ description_greenmountaintribe04 = "This tribe doesn’t trust people who follow Wright’s teachings."
        $ oldpagos_about_4villages += 1
        $ oldpagos_about_greenmountaintribe += 1
        $ minutes += 1
        menu:
            'She sizes you up. “I don’t know what ye’ve heard, but they never bothered us, and neither offered us their friendship. The Tribe keeps its distance from those who follow Wright’s Tablets. Ask other pagans, or their elders.”
            '
            '“Tell me about Howler’s Dell.”' if not oldpagos_about_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Howler’s Dell.”')
                jump oldpagos_about_4villages02howlers
            '“Tell me about White Marshes.”' if not oldpagos_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about White Marshes.”')
                jump oldpagos_about_4villages02marshes
            '“Tell me about Gale Rocks.”' if not oldpagos_about_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Gale Rocks.”')
                jump oldpagos_about_4villages02galerocks
            '“Tell me about Creeks.”' if not oldpagos_about_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about Creeks.”')
                jump oldpagos_about_4villages02creeks
            '“Tell me about The Tribe of The Green Mountain.”' if quest_reachthepaganvillage and not oldpagos_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about The Tribe of The Green Mountain.”')
                jump oldpagos_about_4villages02greenmountain
            '“I’ve no more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                jump oldpagosafterinteraction01
