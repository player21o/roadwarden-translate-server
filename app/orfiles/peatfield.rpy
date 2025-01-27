###################### PEAT FIELD
# description_thyrsus01 = 0 #"According to the patrol I encountered at the old forest garden, I shouldn’t “bother him long. He’s of a cold soul.”"
# description_thyrsus02 = 0 #"According to the people of {color=#f6d6bd}Gale Rocks{/color}: “He just listens to what we need, tells his price, and makes us go, he does.”"
# description_thyrsus03 = 0 #"According to {color=#f6d6bd}Glaucia{/color}, he has “a soul as firm as a shield. No threat nor begging will move him an inch.”"

# Thyrsus: “Yep.” he speaks very briefly, weirdly, acts as if he’s constantly high. He plays with various amulets, and sometimes moves the creepers surrounding his arms. He moves his toes nervously, yawns. Immature brat.

default peatfield_firsttime = 0
default peatfield_firsttime_destroyed = 0
default peatfield_fluff = ""
default peatfield_fluff_old = ""

default thyrsus_greeting = ""
default thyrsus_shop = 0
default thyrsus_shop_alchemytable_asked = 0

default thyrsus_shop_witheringdust = 0
default thyrsus_shop_witheringdust_price = 0
default thyrsus_shop_bonehook = 0
default thyrsus_shop_stingointment = 0
default thyrsus_shop_bugrepellent = 0
default thyrsus_shop_bugrepellent_price = 3

default thyrsus_shop_venom = 0
default thyrsus_shop_venom_price = 4
default thyrsus_shop_ghoulblood = 0
default thyrsus_shop_ghoulblood_price = 8
default thyrsus_shop_powderedrock = 0
default thyrsus_shop_powderedrock_price = 10

default thyrsus_shop_blackwoundwort = 0
default thyrsus_shop_blackwoundwort_timer = 0
default thyrsus_shop_marshbules = 0
default thyrsus_shop_marshbules_timer = 0

default thyrsus_friendship = 0
default thyrsus_orentius_canhelp = 0
default thyrsus_orentius_helped = 0
default thyrsus_orentius_nomoreundead_react = 0
default thyrsus_orentius_debt_option = 0
default thyrsus_orentius_debt_achieved = 0

default thyrsus_about_highisland_recruitment = 0
default thyrsus_about_highisland_recruitment_done = 0
default thyrsus_highisland_joined = 0

default thyrsus_whitemarshes_entrance = 0
default thyrsus_whitemarshes_entrance_counter = 0

default thyrsus_about_himself1 = 0
default thyrsus_about_himself2 = 0
default thyrsus_about_himself3 = 0
default thyrsus_about_peat = 0
default thyrsus_about_returninghome = 0
default thyrsus_about_cursedsoil = 0

default thyrsus_about_druids1 = 0
default thyrsus_about_druids2 = 0
default thyrsus_about_readtheletter = 0

default thyrsus_about_asterion1 = 0
default thyrsus_about_asterion2 = 0
default thyrsus_about_asterion_question1 = 0
default thyrsus_about_asterion_question2 = 0
default thyrsus_about_asterion_question3 = 0
default thyrsus_about_asterion_question4 = 0
default thyrsus_about_asterion_question5 = 0

default thyrsus_about_spiritrock = 0
default thyrsus_about_cidercask = 0
default thyrsus_about_cidercask_delivered = 0

default thyrsus_about_dissent1 = 0
default thyrsus_about_dissent2 = 0
default thyrsus_about_dissent3 = 0
default thyrsus_about_dissent_question1 = 0
default thyrsus_about_dissent_question2 = 0
default thyrsus_about_dissent_question3 = 0
default thyrsus_about_dissent_question4 = 0
default thyrsus_about_dissent_question5 = 0
default thyrsus_about_treant = 0
default thyrsus_about_magicchisel1 = 0
default thyrsus_about_magicchisel2 = 0
default thyrsus_about_riskofthais = 0
default thyrsus_about_snakebait = 0

default thyrsus_about_thyrsusgift = 0
default thyrsus_about_thyrsusgift_mainquestion_1 = 0
default thyrsus_about_thyrsusgift_mainquestion_2 = 0
default thyrsus_about_thyrsusgift_bonusquestion_1 = 0
default thyrsus_about_thyrsusgift_bonusquestion_2 = 0
default thyrsus_about_thyrsusgift_bonusquestion_3 = 0
default thyrsus_about_thyrsusgift_bonusquestion_4 = 0
default thyrsus_about_thyrsusgift_bonusquestion_5 = 0
default thyrsus_about_thyrsusgift_bonusquestion_6 = 0

default thyrsus_about_thyrsusgift_druidcomment = 0
default thyrsus_about_thyrsusgift_parentscomment = 0
# default quest_thyrsusgift_dayofsuccess = 0

default thyrsus_assistance_threshold = 5
default thyrsus_assistance_gray = 0

label peatfield01:
    nvl clear
    $ pc_area = "peatfield"
    if not peatfield_firsttime:
        show areapicture bogroadtopeatfield at basicfade
    elif not whitemarshes_destroyed:
        show areapicture peatfield01 at basicfade behind peatfield
        if quest_thyrsusgift == 2:
            show peatfield shirt at basicfade
    else:
        show areapicture peatfield02 at basicfade behind peatfield
        if quest_thyrsusgift == 2:
            show peatfield shirt at basicfade
    label peatfield_fluffloop:
        $ peatfield_fluff = renpy.random.choice(['Frogs fill the bogs with their songs, and hide among the puddles as you ride down the path.', 'The gentle breeze is soothing, but spoiled by the “sour” scent of rotting soil. You avoid deeper breaths.', 'A tiny vole, as brown as the short grasses, is washing its fur at the edge of a puddle, but jumps into it once it notices your arrival.', 'An outraged shout of birds fills the bogs - suddenly, more than twenty brown birds take off from the grasses, scared off by the sound of hooves.', 'A white-and-brown hawk is sitting in the middle of the path, tearing away flesh off its furry prey. Once it realizes you’re riding straight at it, it takes to the air, leaving with its meal, not even sparing you a glance.'])
        if peatfield_fluff_old == peatfield_fluff:
            jump peatfield_fluffloop
        else:
            $ peatfield_fluff_old = peatfield_fluff
    if thyrsus_friendship >= 8:
        $ thyrsus_greeting = "{color=#f6d6bd}Thyrsus{/color} is at the edge of the scarp, spreading his arms and creepers. “Welcome back!”"
    elif thyrsus_friendship >= 4:
        $ thyrsus_greeting = "{color=#f6d6bd}Thyrsus{/color} is at the edge of the scarp, greeting you with a polite nod. The creepers idly hang from his arms, resting on the ground."
    elif thyrsus_friendship >= 1:
        $ thyrsus_greeting = "{color=#f6d6bd}Thyrsus{/color} is sitting on the bench, observing your arrival as he grinds something in a mortar, but once you greet him, he leaves his tools behind and moves to the edge of the scarp. The creepers idly hang from his arms, resting on the ground."
    elif thyrsus_friendship >= -1:
        $ thyrsus_greeting = "{color=#f6d6bd}Thyrsus{/color} is sitting on the bench, observing your arrival as he’s grinding something in a mortar. You greet him, but he asks you to wait a minute, and only after he’s satisfied with his work does he leave his tools behind and move to the edge of the scarp. The creepers on his arms are slightly raised."
    else:
        $ thyrsus_greeting = "{color=#f6d6bd}Thyrsus{/color} is standing among the peat bricks, observing something in the distance. He ignores your arrival. Once you greet him, he moves to the edge of the scarp, thinning his lips. The creepers on his arms are in front of him, slightly raised."

    $ shop = "thyrsuswares"
    if not peatfield_firsttime:
        $ world_known_npcs += 1
        $ world_known_areas += 1
        $ peatfield_firsttime = 1
        $ bogroad_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        stop music fadeout 4.0
        play nature "audio/ambient/peatfield01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump thyrsusfirsttime01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if not whitemarshes_destroyed:
            if not renpy.music.get_playing(channel='music') == "audio/weloveindies_searchingfortrails_peatfieldloop.ogg":
                play music "audio/weloveindies_searchingfortrails_peatfieldloop.ogg" fadeout 1.0 fadein 1.0
            stop nature fadeout 4.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump thyrsusregular01
        else:
            stop music fadeout 4.0
            play nature "audio/ambient/peatfield01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump thyrsusregular02

label thyrsusfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if not weathermud:
        $ custom1 = ""
    else:
        $ custom1 = "Your palfrey takes slow steps forward, fighting with the dense mud left by the recent rain. "
    if bogroad_clotheswet == day:
        $ custom2 = "and dragonflies, along with the splashes of your soaked clothes slapping against your mount."
    else:
        $ custom2 = "and dragonflies."
    menu:
        'You ride along shallow waters on one side, and flooded trees on the other. You reach what seems like the end of the road - the turn south is already overgrown, most likely abandoned after it was devoured by the bog.
        \n\nBut as you look north, you see a wide clearing that, with time, has become a meadow, and a lonely hut at the end of an often-traveled path. At first, you ride down slightly, following the twisted trail. [custom1]There’s plenty of puddles around, as well as brown, gray, and purple grasses, but all of them are too short for any lurking predators, and the few foxes you see far away don’t pay you any attention.
        \n\nYou pass by the fresh tracks of heavy, hooved beasts, but spot no wild game in sight. Your ears can’t free themselves from the birds, rodents, [custom2]
        '
        'We need to ride carefully. If {color=#f6d6bd}[horsename]’s{/color} leg sinks into the mud, it may get broken.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- We need to ride carefully. If {color=#f6d6bd}%s’s{/color} leg sinks into the mud, it may get broken.' %horsename)
            show areapicture peatfield01 at basicfade
            if not renpy.music.get_playing(channel='music') == "audio/weloveindies_searchingfortrails_peatfieldloop.ogg":
                play music "audio/weloveindies_searchingfortrails_peatfieldloop.ogg" fadeout 1.0 fadein 1.0
            stop nature fadeout 6.0
            menu:
                'The farther north you ride, the shorter the grass gets. These vast peat fields, broader than two or three villages placed side by side, are many years old. The turf bricks surrounding the solitary hut are still fresh, drying in the late summer light.
                \n\nThe scent of this area is like that of no bog you’ve ever encountered - instead of a sublime aroma of healthy soil, it’s intense, sulfury, leaving an almost sour taste on your tongue. The short scarp is dripping with water, like a running sore of the earth, carved with spade and muscle.
                \n\nThe house, made of birch wood, dried turf, and a blanket of soil, is a structure you’re not too familiar with, but you imagine its interiors are much smaller than they appear to be. The walls are a few feet thick to keep in the warmth, and such roofs tend to get soggy, until they collapse after a decade or so.
                \n\nThe only soul in sight is sitting on the bench, stuffing his mouth with fistfuls of green leaves that he takes out of a small basket placed on his knees.
                '
                'I introduce myself, and for now stay in the saddle.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself, and for now stay in the saddle.')
                    if bogroad_clotheswet == day:
                        $ custom2 = "Bathing in the bogs, I see,” he mocks your wet clothes. “"
                    else:
                        $ custom2 = ""
                    menu:
                        'Still chewing, he mutters something in response, then shakes his hairy head, swallows, and puts the basket away. He stands up and takes a single step forward, approaching the edge of the scarp.
                        \n\nHis arms are entangled by green creepers, longer than he is tall. They rub against the ground after each step, and judging by the way they occasionally twitch, they’re very much alive, even though you can’t see where they originate from.
                        \n\n“[pcname], the {i}roadwarden{/i},” he repeats, this time clearly. He moves his sealed lips left and right, as if he’s tasting your name, still not sure if he should swallow it, or spit it out. “[custom2]Your face’s familiar, ba not {i}this{/i},” he points at your mount, staring at it for a good minute.
                        \n\nHis voice is quiet and young, not older than thirty. If you were standing next to each other, he would be almost a head shorter than you, but for now, he towers over you. He has sunken cheeks and sloped shoulders, and while his gray, woolen robe was never pretty, it’s now close to being a rag, and his sandals reveal long toenails.
                        '
                        'I observe him more closely.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe him more closely.')
                            $ at_activate = 1
                            $ at = 0
                            menu:
                                'His eyes are as brown and dark as the grasses of this very bog. His left earring is made of a tusk and a feather, while the right one is an hourglass made of silver, though a broken wing makes it at all times tilted under its own weight. The leather strips on his wrists and ankles hold beads, pieces of amber, old game dice, and tiny skulls of birds and critters.
                                \n\nEven more cords are hanging from his neck, some of them so long they reach his stomach. They carry countless amulets, some of them torn, dried, shabby, or fragmented, and you spot among them small boxes made of wood and bone, as well as leather pouches, which hide even more secrets.
                                \n\n“Were you here before? Mayhap I dreamt you in my sleep,” his voice and look are absent. “If so, I’m {color=#f6d6bd}Thyrsus{/color}, the {i}turfwarden{/i}.”
                                '
                                ' (disabled)' ( condition="at == 0" ):
                                    pass
                                '“Is warding turf difficult?”' ( condition="at == 'friendly'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Is warding turf difficult?”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ thyrsus_friendship -= 0
                                    $ custom1 = "“Yep,” he looks at you in silence, then yawns loudly. His teeth are yellow, but don’t seem to be neglected, at least from this far. “T’s hard, for t’s {i}boring{/i} like a toad’song.” He sighs. “You’re off the main road, stranger. What for?”"
                                    jump thyrsusfirsttime02
                                'I run my eyes over the wet scarp. “Shouldn’t you {i}ward{/i} your home out of here? The earth beneath it is going to collapse.”' ( condition="at == 'playful'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I run my eyes over the wet scarp. “Shouldn’t you {i}ward{/i} your home out of here? The earth beneath it is going to collapse.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ thyrsus_friendship -= 1
                                    $ custom1 = "He huffs so loudly that the wall of amulets on his chest jangles and rattles, and even more so after he shrugs. The pause he makes between both of these gestures is unnerving. “We move these bricks north every spring. Don’t teach a peat farmer about bogs, {i}buildwarden{/i}.”\n\nWithout another word, he stares in the distance. Just to be sure, you look around. There’s no other soul around you."
                                    jump thyrsusfirsttime02
                                '“{i}Dreamt{/i}?”' ( condition="at == 'distanced'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “{i}Dreamt{/i}?”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ thyrsus_about_asterion1 = 1
                                    $ thyrsus_friendship += 1
                                    $ custom1 = "He observes you keenly, letting out an approving grunt. “No, t’sn’t your shell I saw, ba your wandering eyes, hands used to touch beasts more than humans, ass burning from’a saddle, an’ cold sweat f’nights. T’was’a man before you here, {color=#f6d6bd}Asterion{/color}, an’ was as lost’s you are. Lost,” he makes a dramatic pause, then smiles. “Ba not unwelcome.”"
                                    jump thyrsusfirsttime02
                                '“Wake up while {i}I’m{/i} here, {color=#f6d6bd}Thyrsus{/color}. We have things to discuss.”' ( condition="at == 'intimidating'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Wake up while {i}I’m{/i} here, {color=#f6d6bd}Thyrsus{/color}. We have things to discuss.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ thyrsus_friendship -= 1
                                    $ custom1 = "He sighs, looks at the clouds - the wall of amulets rattle - and speaks even more slowly. “S’prise me.”"
                                    jump thyrsusfirsttime02
                                'I keep looking at the creepers dangling from his sides. “I hope I’m not bothering you, {i}warden{/i}. I need some guidance through these bogs.”' ( condition="at == 'vulnerable'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I keep looking at the creepers dangling from his sides. “I hope I’m not bothering you, {i}warden{/i}. I need some guidance through these bogs.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ thyrsus_friendship += 0
                                    $ custom1 = "“You do? The’sn’t a thing behind me, nor east f’here. All you can do’s turn back,” he looks at you in silence, then yawns loudly. His teeth are yellow, but don’t seem to be neglected, at least from this far. “You’re off the main road, stranger. What for?”"
                                    jump thyrsusfirsttime02

    label thyrsusfirsttime02:
        $ questionpreset = "thyrsus1"
        menu:
            '[custom1]
            '
            '(thyrsus1 set)':
                pass

label thyrsusregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "thyrsus1"
    if not weathermud:
        $ custom1 = ""
    else:
        $ custom1 = "Your palfrey takes slow steps forward, fighting with the dense mud left by the recent rain. "
    if thyrsus_orentius_helped and orentius_spared and not thyrsus_orentius_nomoreundead_react:
        $ thyrsus_orentius_nomoreundead_react = 1
        $ thyrsus_friendship -= 4
        menu:
            '[custom1][peatfield_fluff]
            \n\n{color=#f6d6bd}Thyrsus{/color} scowls at you, holding his amulets in a clenched fist, and shaking them up and down. Their rattle carries a cold promise.
            \n\n“We’ll not speak f’your failure,” he growls. “Tell me what you want an’ be on your way, {i}warden{/i}.”
            '
            '(thyrsus1 set)':
                pass
    elif thyrsus_orentius_helped and whitemarshes_nomoreundead and not thyrsus_orentius_nomoreundead_react:
        $ thyrsus_orentius_nomoreundead_react = 1
        $ thyrsus_friendship += 3
        $ minutes += 5
        menu:
            '[custom1][peatfield_fluff]
            \n\n{color=#f6d6bd}Thyrsus{/color} welcomes you by widely spreading his arms and creepers. “I still smell the pyres! {color=#f6d6bd}Orentius{/color}, {i}know-all-thing-priest{/i}, has washed his ears for you!” His laughter makes his amulets rattle. “I must say, I expected much worse things from a cityfolk after all the stories I’ve heard! What did you tell him, warden?”
            \n\nYou answer a few of his questions, enough for him to grow bored of this exchange, but even then he keeps wandering along the scarp.
            '
            '(thyrsus1 set)':
                pass
    elif not thyrsus_orentius_helped and whitemarshes_nomoreundead and not whitemarshes_attacked and not thyrsus_orentius_nomoreundead_react:
        $ thyrsus_orentius_nomoreundead_react = 1
        $ thyrsus_friendship += 2
        $ minutes += 5
        menu:
            '[custom1][peatfield_fluff]
            \n\n{color=#f6d6bd}Thyrsus{/color} welcomes you by widely spreading his arms and creepers. “I don’t know what you did,” he shouts long before you reach his house, “ba the messenger was here. {color=#f6d6bd}Orentius{/color}, {i}know-all-thing-priest{/i}, has washed his ears?” His laughter makes his amulets rattle. “What happened, warden?”
            \n\nYou answer a few of his questions, enough for him to grow bored of this exchange, but even then he keeps wandering along the scarp.
            '
            '(thyrsus1 set)':
                pass
    elif not thyrsus_orentius_helped and whitemarshes_nomoreundead and whitemarshes_attacked and not thyrsus_orentius_nomoreundead_react:
        $ thyrsus_orentius_nomoreundead_react = 1
        $ thyrsus_friendship -= 1
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        $ quest_explorepeninsula_description17a = "In spring, {color=#f6d6bd}White Marshes{/color} will most likely completely separate itself from the rest of the peninsula."
        menu:
            '[custom1][peatfield_fluff]
            \n\n{color=#f6d6bd}Thyrsus{/color} scowls at you, holding his amulets in a clenched fist and shaking them up and down. “To think {i}a warden{/i} wad lead a strike against my home,” his voice is weak, “yet... One’s eyes wad see it as {i}a right cause{/i}.”
            \n\nHis creepers are between the two of you, a living, green shield. “If I open the gate for you, I’ll lose my life. You must understand. We can barter, if we’ve got to, ba you’d do betta not returning to the bogs. In spring, the paths through the waters will be sunk for good, so that no one may cross it again.”
            '
            '(thyrsus1 set)':
                pass
    else:
        menu:
            '[custom1][peatfield_fluff]
            \n\n[thyrsus_greeting]
            '
            '(thyrsus1 set)':
                pass

label thyrsusafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "thyrsus1"
    $ custom1 = renpy.random.choice(['He yawns loudly.', '“What else?”', 'He stares in the distance, rubbing his amulets with his fingers.', 'He adjusts his bracelets, giving you a bored look.', 'He stretches, yawning subtly.'])
    menu:
        '[custom1]
        '
        '(thyrsus1 set)':
            pass

label thyrsusenteringwhitemarshes01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is this the way to {color=#f6d6bd}White Marshes{/color}?”')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ description_thyrsus00a = " A capable mage specialized in controlling plants."
    $ thyrsus_whitemarshes_entrance = 1
    menu:
        '“Both the opposite an’ quite so. You took the left turn, {i}away from{/i} the village, ba you wadn’t reach it anyway. The path’s sealed, an’ {i}I{/i} keep it that way.”
        \n\nYou ask him to explain and he raises his hands, waggling his fingers as if he’s casting a curse. “My green pets keep the troublemakers away. Ba I {i}cad{/i} make an exception for a warden, one willing to prove they bring {i}gifts{/i}, not troubles.”
        '
        '“...What’s the toll?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...What’s the toll?”')
            $ custom1 = "He reaches for his basket and places it on the lower edge of the scarp, crouching right behind it. You look inside - indeed, it’s filled with wild leaves, flowers, and berries. “Give me nuff for a day or so, an’ I’ll bend the vines for a day. Or so.”"
            jump thyrsusenteringwhitemarshes01a

    label thyrsusenteringwhitemarshes01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some plants are blocking the way to {color=#f6d6bd}White Marshes{/color}. How about the road south from here?”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ description_thyrsus00a = " A capable mage specialized in controlling plants."
        $ thyrsus_whitemarshes_entrance = 1
        menu:
            '“With’a horse, an’ no guide? You’d get swallowed in no time. By monsters. An’ the mud.” He raises his hands, waggling his fingers as if he’s casting a curse. “My green pets keep the troublemakers away. Ba I {i}cad{/i} make an exception for a warden, one willing to prove they bring {i}gifts{/i}, not troubles.”
            '
            '“...What’s the toll?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...What’s the toll?”')
                $ custom1 = "He reaches for his basket and places it on the lower edge of the scarp, crouching right behind it. You look inside - indeed, it’s filled with wild leaves, flowers, and berries. “Give me nuff for a day or so, an’ I’ll bend the vines for a day. Or so.”"
                jump thyrsusenteringwhitemarshes01a

    label thyrsusenteringwhitemarshes02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need you to open the path to {color=#f6d6bd}White Marshes{/color}.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ custom1 = "“Then you know what I need {i}you{/i} to do,” he smiles and reaches for his basket."
        jump thyrsusenteringwhitemarshes01a

    label thyrsusenteringwhitemarshes01a:
        $ description_whitemarshes00 = "To enter it, I need to pay a toll to {color=#f6d6bd}Thyrsus{/color}, the mage living among the peat fields."
        menu:
            '[custom1]
            '
            '“...I set your village free, {color=#f6d6bd}Thyrsus{/color}.”' if whitemarshes_nomoreundead and not whitemarshes_attacked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...I set your village free, {color=#f6d6bd}Thyrsus{/color}.”')
                $ vines_perma_open = 1
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    'He straightens up and sighs. “In a way, sure. I guess.” He snaps his fingers. “The vines know your hooves anyway,” {color=#f6d6bd}[horsename]{/color} interrupts him with a snort, as if he’s listening to every word. “They’ll remember to stay away from you.”
                    '
                    '(thyrsus1 set)':
                        pass
            '“...Aren’t we allies, {color=#f6d6bd}Thyrsus{/color}?”' if thyrsus_about_dissent2 and not whitemarshes_nomoreundead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Aren’t we allies, {color=#f6d6bd}Thyrsus{/color}?”')
                $ vines_perma_open = 1
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    'He straightens up and sighs. “In a way, sure. I guess.” He snaps his fingers. “The vines know your hooves anyway,” {color=#f6d6bd}[horsename]{/color} interrupts him with a snort, as if he’s listening to every word. “They’ll remember to stay away from you.”
                    '
                    '(thyrsus1 set)':
                        pass
            '“Will a food ration be fine?”' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Will a food ration be fine?”')
                $ vines_open_day = day
                $ thyrsus_whitemarshes_entrance_counter += 1
                if thyrsus_whitemarshes_entrance_counter >= 3:
                    $ thyrsus_whitemarshes_entrance_counter -= 3
                    $ thyrsus_friendship += 1
                $ item_rations -= 1
                $ renpy.notify("You lost a food ration.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    '“{i}Very{/i} fine,” he licks his lips, and once he spots a piece of jerky among your gifts, he reaches for it right away. With a full mouth, he snaps his fingers, and mutters something with satisfaction.
                    '
                    '(thyrsus1 set)':
                        pass
            '“These wild fruits and leaves are not much, but I can give you {i}a lot{/i} of them.”' if item_wildplants >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These wild fruits and leaves are not much, but I can give you {i}a lot{/i} of them.”')
                $ vines_open_day = day
                $ thyrsus_whitemarshes_entrance_counter += 0
                if thyrsus_whitemarshes_entrance_counter >= 3:
                    $ thyrsus_whitemarshes_entrance_counter -= 3
                    $ thyrsus_friendship += 1
                $ item_wildplants -= 2
                $ renpy.notify("You lost two bunches of wild plants.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost two bunches of wild plants.{/i}')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    'He purses his lips, his toes flinching nervously. “You think I canna find those by myself? Fine, go ahead,” he mutters with resignation, and you throw in enough fruits and leaves to fill up his basket. He snaps his fingers. “Done.”
                    '
                    '(thyrsus1 set)':
                        pass
            'I have some wild plants to spare, but it won’t be enough. (disabled)' if item_wildplants == 1:
                pass
            '“This chicken roast smells really good.”' if item_chicken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This chicken roast smells really good.”')
                $ vines_open_day = day
                $ thyrsus_whitemarshes_entrance_counter += 2
                if thyrsus_whitemarshes_entrance_counter >= 3:
                    $ thyrsus_whitemarshes_entrance_counter -= 3
                    $ thyrsus_friendship += 1
                $ item_chicken -= 1
                $ renpy.notify("You lost a chicken.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a chicken.{/i}')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    '“Yep,” his eyes widen. You drop the cold piece of meat into his basket and he tears away one of its legs. He suddenly scowls at you, as if you just showed up in front of him out of thin air. “What else? Canna see I’m eating?” He snaps his fingers with an annoyed grunt.
                    '
                    '(thyrsus1 set)':
                        pass
            '“Maybe a roasted fish?”' if item_cookedfish:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe a roasted fish?”')
                $ vines_open_day = day
                $ thyrsus_whitemarshes_entrance_counter += 1
                if thyrsus_whitemarshes_entrance_counter >= 3:
                    $ thyrsus_whitemarshes_entrance_counter -= 3
                    $ thyrsus_friendship += 1
                $ item_cookedfish -= 1
                $ renpy.notify("You lost a cooked fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a cooked fish.{/i}')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    '“Betta than what I’ve got,” he smiles with his yellow teeth and waits for you to throw the fish into his basket. He puts it back on the bench, then snaps his fingers. “Done.”
                    '
                    '(thyrsus1 set)':
                        pass
            'I have no food to spare. (disabled)' if item_wildplants == 0 and item_cookedfish == 0 and item_chicken == 0 and item_rations == 0:
                pass
            '“Can you just take a dragon bone?”' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you just take a dragon bone?”')
                $ vines_open_day = day
                $ thyrsus_whitemarshes_entrance_counter += 1
                if thyrsus_whitemarshes_entrance_counter >= 3:
                    $ thyrsus_whitemarshes_entrance_counter -= 3
                    $ thyrsus_friendship += 1
                show screen notifyimage( "-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                $ coins -= 1
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    '“An’ what’d I do with it? Chew it like an auroch?” While you’re not sure what he means by that, he finally lets out a sigh, and you throw the tiny disc onto his humble supplies. He snaps his fingers. “Done.”
                    '
                    '(thyrsus1 set)':
                        pass
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "thyrsus1"
                menu:
                    '“Betta do so on your own,” he straightens up, reaches into the basket, and for the next minute or so he munches on the greens.
                    '
                    '(thyrsus1 set)':
                        pass

label thyrsus_about_himself101ALL:
    label thyrsus_about_himself101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you live here all by yourself?”')
        $ thyrsus_about_himself1 = 1
        $ description_thyrsus00 = "A warlock and the caretaker of the peat fields."
        $ questionpreset = "thyrsus1"
        menu:
            '“Yep. Warlocking. Peddling. Guarding turf. My tribe dug out what they can this summer, I just keep dragons away from squashing the bricks.” Your eyes turn west, following the man’s raised finger, and you indeed notice a distant trail of massive three-fingered footprints, now turned into small puddles. They’re as long as your torso, with pointy claws, one of which appears to be broken at its tip.
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_about_himself201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But how do you avoid wild beasts?”')
        $ thyrsus_about_himself2 = 1
        $ questionpreset = "thyrsus1"
        menu:
            '“T’s them who avoid this place. They’re afraid f’spears, {i}my{/i} plants, an’ poisons.” Seeing your frown, he raises his creepers quickly, waving them like a dancer would scarves, yet his arms remain still. “They’re stronger than muscles,” he simply explains. “Ba still, I’m not much f’a wanderer.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_about_himself301:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my chin. “Did you {i}choose{/i} to move to this field, or were you forced to do so?”')
        $ thyrsus_about_himself3 = 1
        $ questionpreset = "thyrsus1"
        menu:
            'He reaches toward his chest, rubbing a small tusk nervously. “One f’us surely likes to ask questions, while the other’s got work to do.” His voice is colder than soil.
            '
            '(thyrsus1 set)':
                pass

label thyrsus_shop01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have anything to sell... {i}warlock{/i}?”')
    $ description_thyrsus00b = " A herbalist willing to sell useful balms and powders."
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ thyrsus_shop = 1
    $ renpy.notify("New trader unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
    if pc_class == "scholar":
        $ custom1 = "\n\nYou pause. You’re quite sure that you’re more than capable of making all the balms and powders he just mentioned on your own, if you had an alchemy table at hand. You mention it, and he huffs loudly, already standing in the threshold. “You’re not touching {i}my{/i} tools, warden. Ba I may’ve some woundwort or marshbules f’you, an’ the’re mushrooms in the bogs.”"
    else:
        $ custom1 = ""
    menu:
        'He eagerly smiles and steps away, reaching to the doorknob with his right creeper. “Odds an’ ends. Want to buy a hook? ‘Venturers love those, an’ I’ve got it for cheap.” He doesn’t give you time to respond. “On most days, I brew an’ mix stuff f’poisons an’ medicine, if one’s desperate nuff to cross the bogs for it. I’ve one that withers plants, an’ one that kills worms an’ bugs, an’ one that keeps flies away, for betta health.”[custom1]
        '
        '“Let me take a look.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me take a look.”')
            $ minutes += 10
            show screen shopscreen with dissolve
            jump thyrsusafterinteraction01

    label thyrsus_shop02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you sell me?”')
        $ shop = "thyrsuswares"
        show screen shopscreen with dissolve
        $ questionpreset = "thyrsus1"
        menu:
            'He describes what he can spare loudly.
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_shop03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you got any ingredients I could use?”')
        $ thyrsus_shop = 2
        label thyrsus_shop05:
            $ shop = "thyrsusingredients"
            show screen shopscreen with dissolve
            $ questionpreset = "thyrsus1"
            menu:
                'He pulls out a few jars from his hut.
                '
                '(thyrsus1 set)':
                    pass
        label thyrsus_shop04:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Show me your alchemical ingredients.”')
            jump thyrsus_shop05

label thyrsus_alchemytable01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I use your alchemy table?”')
    $ thyrsus_shop_alchemytable_asked = 1
    $ minutes += 1
    $ description_foggy03 = "She has her own set of alchemical tools, necessary to brew ciders and distill hard drinks."
    $ questionpreset = "thyrsus1"
    menu:
        '“F’course not,” he spares you an incredulous glance. “What wad I do without it? If you’ve bones to spare, take them to {color=#f6d6bd}Foggy{/color}, by the northern road. She brews hard drinks, may let you play.”
        '
        '(thyrsus1 set)':
            pass

label thyrsusaboutspiritrock01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a man living in {color=#f6d6bd}Gale Rocks{/color} who is trying to{i}heal{/i} his spell-less daughter...”')
    $ thyrsus_about_spiritrock = 1
    $ minutes += 5
    $ questionpreset = "thyrsus1"
    $ description_thyrsus04 = "He was taught his unusual magic by the druids of {color=#f6d6bd}Howler’s Dell{/color}."
    $ description_druids02 = "I can find the local druids in the village of {color=#f6d6bd}Howler’s Dell{/color}, at the western road."
    menu:
        'The warlock cuts in right after you mention {color=#f6d6bd}Eudocia’s{/color} rock. “Whatever it is, the’s no way anyone other than a {i}real{/i} prophet wad help that girl. Pneuma’s weak in my tribe, you know. Myself, I’m gifted, yep, ba had no teachers here,” he shrugs his arms, making the creepers bend upward. “Took the pagan priests from {color=#f6d6bd}Howler’s Dell{/color} to help me twist more than a twig. If there {i}was{/i} a way to put pneuma in shells, for good, people wad {i}kill{/i} to find it.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_highisland_recruitment01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m heading for {color=#f6d6bd}High Island{/color}. I want to take you with me, just for a single night.”')
    $ thyrsus_about_highisland_recruitment = 1
    $ thyrsus_about_highisland_recruitment_done = 1
    $ questionpreset = "thyrsus1"
    menu:
        '“Good!” His amulets rattle. “I {i}hate{/i} having vague debts to pay. Come once you need me, an’ let’s be done with this quickly.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_druids101:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You were training with the druids?”')
    $ thyrsus_about_druids1 = 1
    if not quest_ruins_10yclue12 and quest_ruins == 1 and quest_ruins_description01:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    $ quest_ruins_10yclue12 = "{color=#f6d6bd}Thyrsus{/color} left his teachers at {color=#f6d6bd}Howler’s Dell{/color}."
    $ questionpreset = "thyrsus1"
    menu:
        '“{i}The forest speakers{/i},” his mocking voice makes him sound like a brat. “I left when I was a teen, ten years ago, if not more. When everything went to shit,” he suddenly pauses, then waves it off.
        \n\nAfter a few more questions, he speaks slowly, observing your eyes. “Don’t get me wrong, I did learn a lot, specially from that one old man, ba his daughter kept making me meditate, an’ I’m not one to sit still,” his amulets rattle from his flinch. “We {i}paid{/i} them for teaching me, ba they broke their word, kept telling me f’spirits, lumber, an’ {i}f’Wright’s poison{/i},” after his annoyed scoff, he bites his tongue, and taps his toes nervously.
        \n\nYou ask about the “old man,” but {color=#f6d6bd}Thyrsus{/color} runs out of patience. “I don’t know, the one with the {i}real{/i} gift. He guided all the ceremonies, yet was arguing with others, all the time. I don’t care. He was good for nothing, like all f’them.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_druids201:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring a message from your old teacher.”')
    $ thyrsus_about_druids2 = 1
    $ thyrsus_friendship += 1
    $ description_orentius07 ="According to {color=#f6d6bd}Thyrsus{/color}, he used to eagerly oppose pagan magic, seeing it as disgusting in Wright’s eyes."
    $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
    $ questionpreset = "thyrsus1"
    menu:
        'He listens to it without a word, then reaches for one of his bracelets, playing with the wooden beads. He grunts a few times, and his eyes grow absent. “I was happy when I got there, you know? I’m not a loafer, was ready to learn all their ways. Back then, {color=#f6d6bd}priest Orentius{/color} saw any spells coming from pagans as {i}disgusting in Wright’s eyes{/i}.” His tone swings between mocking and begrudging. “Ba I didn’t let go, an’ the others outvoted him. Those were... very dif’rent days.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_readtheletter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him about {color=#f6d6bd}Valens’{/color} situation.')
    $ thyrsus_about_readtheletter = 1
    # $ thyrsus_friendship += 1
    $ renpy.notify("Journal updated: Read the Letter")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Read the Letter{/i}')
    $ quest_readtheletter_description00b = "According to {color=#f6d6bd}Thyrsus{/color}, it’d be better to spare {color=#f6d6bd}Valens{/color} unnecessary suffering."
    $ questionpreset = "thyrsus1"
    menu:
        'He stares in the distance, toward the village. “Poor thing, a fair soul with too much patience. Ba the’s nothing I can do.” After you ask him for advice, he spits on the ground. “Lie, I guess. {color=#f6d6bd}Orentius{/color} already did, won’t be happy with you causing pain to his people. An’ {color=#f6d6bd}Helvius{/color} neither. Unless the hunter was lying, too.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_peat01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is peat really worth constant overseeing?”')
    $ thyrsus_about_peat = 1
    if not quest_explorepeninsula_description17:
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        $ quest_explorepeninsula_description17 = "The western bogs are a good spot for peat harvesting - as long as the locals are friendly to the outsiders, they may be willing to trade for it."
    $ questionpreset = "thyrsus1"
    menu:
        'He looks at the nearby bricks and frowns, as if he’s seeing them for the first time. “Sure, kind of. I think.” You ask him to tell you about them, but he admits it’s “the others” who harvest it. “I’m meant to pile it all up into rickles,” he points at a small dolmen-shaped structure, “ba I’m always {i}so{/i} busy.” He grins.
        \n\nYou ask him what turf is good for, and he starts to tap his toes. “You can build with it. You can burn it. Add it to the soil. An’s great f’smoking meat. We used to dig it slowly an’ barter for stone an’ timber, ba we changed our ways.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_cursedsoil01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found a scrap of land that I think may be cursed, though I’m not sure how to examine it.”')
    $ thyrsus_about_cursedsoil = 1
    $ questionpreset = "thyrsus1"
    menu:
        '“An’ you’re saying the rest f’the North {i}isn’t{/i} cursed?” He lets out a chuckle, but seeing how you still wait for his advice, he raises one of his creepers and, looking in the distance, scratches it. “I’ve no cure for that, ba ask {color=#f6d6bd}Eudocia{/color}, the witch from the other side f’the woods, far east. Mayhaps she has a wand, or something.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_snakebait01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about snake bait?”')
    $ thyrsus_about_snakebait = 1
    $ item_snakebait_truth = 1
    $ questionpreset = "thyrsus1"
    menu:
        '“I can tell you to stay away from it, it stains your fingers, an’ thoughts.” A long pause, cut once you clear your throat. “What do you want me to say? T’s a weird herb, poisoned pleasure. It grows by the meadows, but wanderers pluck it, so it keeps to the darker parts of the woods.”
        '
        '(thyrsus1 set)':
            pass

label thyrsus_about_cidercaskALL:
    label thyrsus_about_cidercask01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was meant to deliver this cask of cider to {color=#f6d6bd}Helvius{/color}, but he’s afraid to accept it. Any advice?”')
        $ thyrsus_about_cidercask = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“Right, the {i}new laws{/i},” his tone carries disdain. “Ba I’m not paying for rotten apples.”
            \n\nYou explain that it was already paid for, and the man asks you to show him how large it is. You tap the barrel loudly, then flinch when the man’s left creeper glides toward it. Surprised by your reaction, he clears his throat and mutters an apology quickly.
            \n\n“{color=#f6d6bd}Helvius{/color} follows {color=#f6d6bd}Orentius{/color} like a duckling wad t’s mother,” he steps away. “Ba he gets bored, comes here from time to time for {i}a special{/i} balm,” he giggles. “I cad keep it for him. He’ll appreciate it.”
            '
            '“Very well. Take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. Take it.”')
                jump thyrsus_about_cidercask02after
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                jump thyrsusafterinteraction01
    label thyrsus_about_cidercask02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can take the cider, if you want.”')
        jump thyrsus_about_cidercask02after
    label thyrsus_about_cidercask02after:
        $ thyrsus_about_cidercask_delivered = day
        $ thyrsus_friendship += 1
        $ renpy.notify("Journal updated: Cask of Cider")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider{/i}')
        $ quest_foggy3whitemarshes_description02 = "I convinced {color=#f6d6bd}Thyrsus{/color} to take and hide the cask."
        $ item_cidercask -= 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "thyrsus1"
        menu:
            'The creepers reach for the cask’s lids, like the limbs of a sea monster, and wait for you to undo the buckles and knots. Without taking as much as a step, he moves the cider behind him swiftly, dropping it into his basket. The squashed food lets out a sad moan, making the man turn around, but it’s already too late. He waves at it and nods to you. “I’ll give it to him in some days, if that matters.”
            '
            '(thyrsus1 set)':
                pass

label thyrsus_about_asterionALL:
    label thyrsus_about_asterion201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know anything about {color=#f6d6bd}Asterion’s{/color} whereabouts?”')
        $ thyrsus_about_asterion2 = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 1
        menu:
            '“Hm,” he raises his chin, “know what? I {i}may{/i},” his amulets rattle after his triumphant announcement, but he then looks at the clouds in the distance. You wait for him to carry on, to no avail.
            '
            'I sigh. “So? What do you want?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “So? What do you want?”')
                $ custom1 = "He flinches. “Huh? Nah, not a thing,” he shifts from foot to foot. “Was just thinking, t’s all.”"
                jump thyrsus_about_asterion203
            'I wait patiently.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait patiently.')
                $ minutes += 1
                $ custom1 = "He nods to himself. “Didn’t notice t’s been so long. Fall’s almost here.”"
                jump thyrsus_about_asterion203

    label thyrsus_about_asterion202:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about {color=#f6d6bd}Asterion{/color}.”')
        $ custom1 = "He shifts from foot to foot and rubs one of his bracelets."
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        jump thyrsus_about_asterion203

    label thyrsus_about_asterion203:
        menu:
            '[custom1]
            '
            '“Where is he, then?”' if not thyrsus_about_asterion_question1 and not asterion_highisland_knowsabout:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where is he, then?”')
                $ thyrsus_about_asterion_question1 = 1
                $ custom1 = "“Well, not at my place, t’s for sure.” To prove his point, he raises one of his creepers and opens the door, though from where you’re sitting you see mostly the cold fireplace and the darkness behind it."
                jump thyrsus_about_asterion203
            '“But you {i}do{/i} have an idea where I can look for him.”' if thyrsus_about_asterion_question1 and not asterion_highisland_knowsabout and not thyrsus_about_asterion_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But you do have an idea where I can look for him.”')
                $ thyrsus_about_asterion_question4 = 1
                $ at_activate = 1
                $ at = 0
                menu:
                    '“Yep. At a monster’s lair, most likely.”
                    \n\nYou meet his eyes.
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“Are you alright?”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Are you alright?”')
                        $ at_activate = 0
                        $ at = 0
                        $ thyrsus_friendship += 0
                        $ quest_asterion_description16 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a journey{/i}.”"
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ asterion_highisland_clues += 1
                        $ custom1 = "He huffs and looks away, straightening up. “Mayhap these questions bore me to sleep, thought f’that? I {i}too’ve{/i} things to do.”\n\nBefore you explain that you simply got worried, he waves it off. “{color=#f6d6bd}Asterion{/color} asked me for help with various creatures, was heading for {i}a journey{/i}, he said. Needed bogey balms to scare animals away, even some weird ones, the harpies an’ sea monsters, ba I’ve no such things. I canna {i}poison{/i} the sea.”\n\nAs you think what to make of all of it, he starts to tap his toes, taking a deep breath. “The’s a huntress living in {color=#f6d6bd}Pelt f’the North{/color}, this inn at the southern road. {color=#f6d6bd}Dalit{/color}. {color=#f6d6bd}Asterion{/color} said she knows wild beasts like no other soul, so he was prepared for them, anyway.”"
                        $ dalit_name = "Dalit"
                        $ description_dalit05 = "According to {color=#f6d6bd}Thyrsus{/color}, she’s an expert when it comes to fighting dangerous beasts."
                        jump thyrsus_about_asterion203
                    '“Great, you’re {i}very{/i} helpful.”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Great, you’re {i}very{/i} helpful.”')
                        $ at_activate = 0
                        $ at = 0
                        $ thyrsus_friendship += 0
                        $ quest_asterion_description16 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a journey{/i}.”"
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ asterion_highisland_clues += 1
                        $ custom1 = "He huffs and looks away, straightening up. “And are you any more? I {i}too’ve{/i} things to do, ba I don’t stop strangers to talk with them.”\n\nBefore you mention that you doubt he’s all that busy, he waves it off. “{color=#f6d6bd}Asterion{/color} asked me for help with various creatures, was heading for {i}a journey{/i}, he said. Needed bogey balms to scare animals away, even some weird ones, the harpies an’ sea monsters, ba I’ve no such things. I canna {i}poison{/i} the sea.”\n\nAs you think what to make of all of it, he starts to tap his toes, taking a deep breath. “The’s a huntress living in {color=#f6d6bd}Pelt f’the North{/color}, this inn at the southern road. {color=#f6d6bd}Dalit{/color}. {color=#f6d6bd}Asterion{/color} said she knows wild beasts like no other soul, so he was prepared for them, anyway.”"
                        $ dalit_name = "Dalit"
                        $ description_dalit05 = "According to {color=#f6d6bd}Thyrsus{/color}, she’s an expert when it comes to fighting dangerous beasts."
                        jump thyrsus_about_asterion203
                    'I nod. “Any monster in particular?”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I nod. “Any monster in particular?”')
                        $ at_activate = 0
                        $ at = 0
                        $ thyrsus_friendship += 1
                        $ quest_asterion_description16 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a journey{/i}.”"
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ asterion_highisland_clues += 1
                        $ custom1 = "He looks away, and reaches for one of his bracelets. “He asked me for help with many, was heading for {i}a journey{/i}, he said. Needed bogey balms to scare animals away.” You push him a bit, but he doesn’t have to think long, as if these questions’ve been bothering him for the entire season. “Weirdest ones were f’ the harpies, an’ he wanted ones for sea monsters, ba I’ve no such things. I canna {i}poison{/i} the sea.”\n\nAs you think what to make of all of it, he starts to tap his toes, taking a deep breath. “The’s a huntress living in {color=#f6d6bd}Pelt f’the North{/color}, this inn at the southern road. {color=#f6d6bd}Dalit{/color}. {color=#f6d6bd}Asterion{/color} said she knows wild beasts like no other soul, so he was prepared for them, anyway.”"
                        $ dalit_name = "Dalit"
                        $ description_dalit05 = "According to {color=#f6d6bd}Thyrsus{/color}, she’s an expert when it comes to fighting dangerous beasts."
                        jump thyrsus_about_asterion203
                    '“Stop treating me like I’m an idiot. Tell me what you know.”' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Stop treating me like I’m an idiot. Tell me what you know.”')
                        $ at_activate = 0
                        $ at = 0
                        $ thyrsus_friendship -= 1
                        $ quest_asterion_description16 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a journey{/i}.”"
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ asterion_highisland_clues += 1
                        $ custom1 = "He straightens up, without looking away. “I cad ask an {i}idiot{/i} for betta prices, you’re more of a fly that keeps buzzing by my ear. I {i}too’ve{/i} things to do.”\n\nBefore you mention that you doubt he’s all that busy, he waves it off. “{color=#f6d6bd}Asterion{/color} asked me for help with various creatures, was heading for {i}a journey{/i}, he said. Needed bogey balms to scare animals away, even some weird ones, the harpies an’ sea monsters, ba I’ve no such things. I canna {i}poison{/i} the sea.”"
                        jump thyrsus_about_asterion203
                    '“Please, {color=#f6d6bd}Thyrsus{/color}. I need your help.”' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Please, {color=#f6d6bd}Thyrsus{/color}. I need your help.”')
                        $ at_activate = 0
                        $ at = 0
                        $ thyrsus_friendship -= 1
                        $ quest_asterion_description16 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a journey{/i}.”"
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ asterion_highisland_clues += 1
                        $ custom1 = "He waves it off, both with a hand and a creeper. “Help with chasing long-gone ghosts? I {i}too’ve{/i} things to do. Food to find, peat to move. Yet I ask you for not a thing.”\n\nBefore you mention that you doubt he’s all that busy, he carries on. “{color=#f6d6bd}Asterion{/color} asked me for help with various creatures, was heading for {i}a journey{/i}, he said. Needed bogey balms to scare animals away, even some weird ones, the harpies an’ sea monsters, ba I’ve no such things. I canna {i}poison{/i} the sea.”"
                        jump thyrsus_about_asterion203
            '“What do you think of him?”' if not thyrsus_about_asterion_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think of him?”')
                $ thyrsus_about_asterion_question3 = 1
                $ custom1 = "He stands with an open mouth, as if he’s not sure what you mean by that. “I... Don’t? Left me with’a heavier pouch, ba asked nosy questions, like {i}someone else{/i} I know.” He gives you a telling look."
                jump thyrsus_about_asterion203
            '“Is he your client, or do you share a goal?”' if not thyrsus_about_asterion_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is he your client, or do you share a goal?”')
                $ thyrsus_about_asterion_question2 = 1
                $ custom1 = "He crosses his arms, making the creepers hit his amulets. “Never had a witch or a warlock at home? T’s wrong f’me to speak for others. I’ll take on my pyre a lot f’shame an’ doubt, an’ I need to be trusted.”"
                jump thyrsus_about_asterion203
            'I can’t tell if he’s hiding anything useful from me or not. (disabled)' if thyrsus_about_asterion_question2 and not description_asterion02b and thyrsus_friendship < 5 and not thyrsus_about_asterion_question5:
                pass
            '“I understand these questions annoy you, but you know I wouldn’t ask them without a good reason. You had more in common with him than you admit.”' if thyrsus_about_asterion_question2 and thyrsus_friendship >= 5 and not thyrsus_about_asterion_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I understand these questions annoy you, but you know I wouldn’t ask them without a good reason. You had more in common with him than you admit.”')
                jump thyrsus_about_asterion204
            '“People claim that he and your tribe were planning something big. Do you deny that?”' if thyrsus_about_asterion_question2 and description_asterion02b and not thyrsus_about_asterion_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “People claim that he and your tribe were planning something big. Do you deny that?”')
                $ minutes += 5
                label thyrsus_about_asterion204:
                    $ thyrsus_about_asterion_question3 = 1
                    $ thyrsus_about_asterion_question5 = 1
                    $ quest_intelforpeltnorth_description04a = "{color=#f6d6bd}White Marshes{/color} suffered from bandit attacks quite severely."
                    $ banditshideout_villagesasked_aboutattacks += 1
                    if quest_intelforpeltnorth == 1:
                        $ renpy.notify("Journal updated: Find the Roadwarden,\nGlaucia’s Band")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden, Glaucia’s Band{/i}')
                    else:
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                    $ quest_asterion_description15 = "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} promised him to “take care of” the conflict between {color=#f6d6bd}White Marshes{/color} and {color=#f6d6bd}Glaucia{/color}, the bandit, as well as of the undead kept by his own tribe."
                    $ quest_intelforpeltnorth_description03 = "It looks like the bandits have been especially harsh toward {color=#f6d6bd}White Marshes{/color}."
                    $ description_bandits07 = "According to {color=#f6d6bd}Thyrsus{/color}, they don’t bother his hut, but in recent years pillaged {color=#f6d6bd}White Marshes{/color} a few times."
                    $ description_glaucia21 = "According to {color=#f6d6bd}Thyrsus{/color}, she’s a bandit leader who puts obedience above all else."
                    if not banditshideout_bandits_pchearedabout:
                        $ banditshideout_bandits_pchearedabout = 1
                    $ whitemarshes_opposition = 1
                    $ custom1 = "He rolls his eyes, shrugging his arms and showing his empty palms, yet the nervous twitches of the creepers add little to his “innocent” demeanor. “He an’ I traded a few times, ba I didn’t bed with him or offer him mint an’ stew. He said he may’ve {i}a job{/i} for me in the woods, an’ I told him I don’t need his bones anymore.”\n\nWhen asked what he {i}did{/i} need, {color=#f6d6bd}Thyrsus{/color} purses his lips. “I want things to {i}change{/i}, t’s’all. I wake up to awoken shells in the fogs an’ {color=#f6d6bd}Glaucia’s{/color} robbers threatening my family. All I want’s for this cursed land to be {i}normal{/i}.” His yawn comes out of nowhere, but you then notice his dropped shoulders and heavy eyelids. “An’ yep. That warden told me he’s going to take care f’it.”"
                    jump thyrsus_about_asterion203
            '“...That’s all.”' if not thyrsus_about_asterion_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...That’s all.”')
                jump thyrsusafterinteraction01
            '“Thanks.”' if thyrsus_about_asterion_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump thyrsusafterinteraction01

label thyrsusfavorALL:
    label thyrsusabouttravelingwithpc01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say {i}I{/i} were to help your people with the bandits and get rid of the undead. Would you return the favor?”')
        $ thyrsus_orentius_debt_option = 1
        $ thyrsus_friendship += 1
        $ questionpreset = "thyrsus1"
        menu:
            'He spares you a yellow grin. “T’s all, you say? Yep-yep, save the North, or the scrap f’it I care about, an’ I’ll follow you into a fog.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsusabouttravelingwithpc01alt1:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve already weakened {color=#f6d6bd}Glaucia{/color} quite a bit. Let’s say I were to get rid of the undead. Would you return the favor?”')
        $ thyrsus_orentius_debt_option = 1
        $ thyrsus_friendship += 1
        $ minutes += 5
        $ questionpreset = "thyrsus1"
        menu:
            'You tell him about your meeting with {color=#f6d6bd}Gale Rocks’{/color} council and he gives you a serious look. “You did all that? Yep-yep, help my tribe save its souls an’ I’ll follow you into a fog.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsusabouttravelingwithpc01alt2:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I already helped you with the undead. Let’s say I were to help your people with the bandits - would you return the favor?”')
        $ thyrsus_orentius_debt_option = 1
        $ thyrsus_friendship += 1
        $ questionpreset = "thyrsus1"
        menu:
            'He gives you a serious look. “After what you already did, I trust t’s possible. Find a way to weaken {color=#f6d6bd}Glaucia{/color} an’ I’ll follow you into a fog.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsusabouttravelingwithpc02alt1:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve already weakened {color=#f6d6bd}Glaucia{/color} quite a bit, and there are no more undead. Will you return the favor?”')
        $ thyrsus_orentius_debt_option = 1
        $ thyrsus_friendship += 2
        $ thyrsus_orentius_debt_achieved = 1
        $ questionpreset = "thyrsus1"
        menu:
            'You tell him about your meeting with {color=#f6d6bd}Gale Rocks’{/color} council and he spares you a yellow grin. “You did all that? We had no deal, warden, ba you saved the North, or the scrap f’it I care about. Come here once you need me to follow you into a fog.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsusabouttravelingwithpc02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You owe me.”')
        $ thyrsus_friendship += 1
        $ minutes += 5
        $ thyrsus_orentius_debt_achieved = 1
        $ questionpreset = "thyrsus1"
        menu:
            'You discuss the recent events and while the man lets out a grim sigh, he then crouches, shortening the distance between your eyes. “You had my word. I’ll await your call.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsusabouttravelingwithpc02alt3:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I helped you with the undead and I brought you your possessions. This should be enough to earn your help.”')
        $ thyrsus_friendship += 1
        $ minutes += 5
        $ thyrsus_orentius_debt_achieved = 1
        $ questionpreset = "thyrsus1"
        menu:
            'You discuss the recent events and while the man lets out a grim sigh, he then crouches, shortening the distance between your eyes. “T’wasn’t the deal, b’I want you to keep on breathing. I’ll await your call.”
            '
            '(thyrsus1 set)':
                pass

label thyrsusaboutdissentALL:
    label thyrsus_about_dissent101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I stare at him. “Something needs to be done about the undead.”')
        $ custom1 = "He returns your gaze and sits down on the bench. “Yep. Ba t’s not a task for a warlock an’ a cityfolk. You’d need a band, an’ I’ll tear off your head sooner than I’d bring a threat to my tribe.”\n\nYou reach toward your blade, but the creepers remain idle. “You’re stepping into a treant’s branch.” Seeing your frown, he explains. “Their grasp gets tighter the more you move, you see? Forget it,” he waves it off. “Why do you care about any f’that? Let my people choose their path.”"
        jump thyrsus_about_dissent102

    label thyrsus_about_dissent101alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you telling me you’re {i}wardening{/i} the bogs because you wanted to do so? You refused to accept the new order of things, these necromantic practices.”')
        $ custom1 = "He sits down on the bench. “Do I care who {i}made me{/i} leave the walls? {color=#f6d6bd}Orentius{/color} didn’t want me there, ba I didn’t want to stay. To stop him now, you’d need a band, an’ I’ll tear off your head sooner than I’d bring a threat to my tribe.”\n\nYou reach toward your blade, but the creepers remain idle. “You’re stepping into a treant’s branch.” Seeing your frown, he continues. “Their grasp gets tighter the more you move, you see? Forget it,” he waves it off. “Why do you care about any f’that? Let my people choose their path.”"
        jump thyrsus_about_dissent102

    label thyrsus_about_dissent102:
        $ thyrsus_about_dissent1 = 1
        $ thyrsus_about_treant = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“The dead shells deserve to rest. They’re being enslaved.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The dead shells deserve to rest. They’re being enslaved.”')
                $ thyrsus_friendship += 0
                $ custom1 = "“You speak like yet another priest, I cadn’t care less. All I want’s my tribe’s safety, ba this means not a thing to {color=#f6d6bd}Orentius{/color}.” He reaches for the broken hourglass in his ear. “What’s your plan once you get to him?”"
                jump thyrsus_about_dissent102a
            '“The undead will turn dangerous, we just don’t know when.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead will turn dangerous, we just don’t know when.”')
                $ thyrsus_friendship += 1
                $ custom1 = "He nods. “T’s what I told him, ba {color=#f6d6bd}Orentius’{/color} sure he’s a prophet. He doesn’t listen.” He leans forward, paying close attention to your eyes. “What’s your plan once you get to him?”"
                jump thyrsus_about_dissent102a
            '“Your tribe’s becoming an outcast. Soon, no merchants will want to trade with necromancers.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your tribe’s becoming an outcast. Soon, no merchants will want to trade with necromancers.”')
                $ thyrsus_friendship += 0
                $ custom1 = "“You speak as if t’s’a matter f’the future, ba my tribe accepts the risk. I cadn’t care less. All I want’s my tribe’s safety, ba this means not a thing to {color=#f6d6bd}Orentius{/color}.” He reaches for the broken hourglass in his ear. “What’s your plan once you get to him?”"
                jump thyrsus_about_dissent102a
            'I sigh. “Come on, {color=#f6d6bd}Thyrsus{/color}. You know just as well as I do that this is {i}wrong{/i}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “Come on, {color=#f6d6bd}Thyrsus{/color}. You know just as well as I do that this is {i}wrong{/i}.”')
                $ thyrsus_friendship -= 1
                $ custom1 = "He huffs. “I’ve had nuff f’people who do what they feel like doing. Are your wits that shallow? What I want’s my tribe’s safety, an’ the undead’re dangerous. T’s why I argued with {color=#f6d6bd}Orentius{/color}, ba this means not a thing to him.” He scowls at you. “What’s your plan once you get to him?”"
                jump thyrsus_about_dissent102a

    label thyrsus_about_dissent102a:
        menu:
            '[custom1]
            '
            'I think for a moment before I speak. “Whatever’s necessary to make him stop.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think for a moment before I speak. “Whatever’s necessary to make him stop.”')
                $ thyrsus_friendship -= 1
                $ custom1 = "He springs back to his feet. “You canna! Having him dead wad break his spells, set the undead free!” He starts to stride along the scarp. “You’d bring doom on us all. You’ve to {i}talk{/i} with him, if anything. All {i}I{/i} can do’s find a way to let you into his house, an’ you’ll’ve ba one chance. {i}If{/i} you can convince me you’re to be trusted.” He shakes his head, raising one of the turf bricks with his creeper and breaking it in half. He steps away and looks at it in silence, as if he’s not sure how it happened. “Yep, well. He may not be as easy to persuade as you think, you know.”"
                jump thyrsus_about_dissent103
            '“I’ll talk to him, help him realize he’s wrong.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll talk to him, help him realize he’s wrong.”')
                $ thyrsus_friendship += 0
                $ custom1 = "He looks down. “So the same thing I tried. Mayhap you’re betta at speaking with people, seeing how much you {i}like to{/i} talk,” with a scoff, he stands up. “All {i}I{/i} can do’s find a way to let you into his house, an’ you’ll’ve ba one chance. {i}If{/i} you can convince me you’re to be trusted.” His toes tap on his sandals. “He may not be as easy to persuade as you think, you know.”"
                jump thyrsus_about_dissent103
            '“I want to learn what pushes him to do all this. He must have his reasons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn what pushes him to do all this. He must have his reasons.”')
                $ thyrsus_friendship += 1
                $ custom1 = "He freezes, as if he barely understands what you mean. “Huh, this may be a good first step. Ba then he needs some persuading, an’ it won’t be as easy’s you think,” he gives you a warm look, then stands up slowly and looks at the clouds. “All {i}I{/i} can do’s find a way to let you into his house, an’ you’ll’ve ba one chance. {i}If{/i} you can convince me you’re to be trusted.”"
                jump thyrsus_about_dissent103
            '“I’ll improvise.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll improvise.”')
                $ thyrsus_friendship -= 1
                $ custom1 = "“Can you not?” He lets out a sigh and gets back on his feet, wandering along the scarp. “I’d rather see you being serious about this. All {i}I{/i} can do’s find a way to let you into his house, an’ you’ll’ve ba one chance. {i}If{/i} you can convince me you’re to be trusted.” He shakes his head, raising one of the turf bricks with his creeper and breaking it in half. He steps away and looks at it in silence, as if he’s not sure how it happened. “Yep, well. He may not be as easy to persuade as you think, you know.”"
                jump thyrsus_about_dissent103

    label thyrsus_about_dissent103:
        if not quest_orentius:
            $ quest_orentius = 1
            $ renpy.notify("New entry: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Orentius, the Necromancer{/i}')
        else:
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        $ quest_orentius_thyrsus_description01 = "{color=#f6d6bd}Thyrsus{/color} will help me meet with {color=#f6d6bd}Orentius{/color} if I make it worth his time and trust."
        $ minutes += 5
        menu:
            '[custom1]
            '
            '“You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”' if (thyrsus_friendship+appearance_charisma) >= 7:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”')
                $ custom1 = "He raises his hands and rubs his arms, hesitating for another minute. Finally, he sighs. “You’re right. Who else, if not you? Let’s do it.”"
                jump thyrsusselling02
            'He doesn’t trust me enough to help me. (disabled)' if (thyrsus_friendship+appearance_charisma) < 7:
                pass
            'I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”' if not thyrsus_about_riskofthais and quest_orentius_thais_description00 and not thais_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”')
                jump thyrsusaboutdissentriskofthais01
            'I pat my bundles. “Do I have anything that could convince you?”' if not thyrsus_assistance_gray or (thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < 7 and (thyrsus_friendship+appearance_charisma) >= thyrsus_assistance_threshold):
                jump thyrsusselling01
            'I need his trust before I offer him a bribe. (disabled)' if thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < thyrsus_assistance_threshold:
                pass
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump thyrsusafterinteraction01

    label thyrsus_about_dissent201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to meet with {color=#f6d6bd}Orentius{/color}.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“An’ {i}I{/i} need to be sure you won’t make me regret helping you.”
            '
            '“You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”' if (thyrsus_friendship+appearance_charisma) >= 7:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”')
                $ custom1 = "He raises his hands and rubs his arms, hesitating for another minute. Finally, he sighs. “You’re right. Who else, if not you? Let’s do it.”"
                jump thyrsusselling02
            'He doesn’t trust me enough to help me. (disabled)' if (thyrsus_friendship+appearance_charisma) < 7:
                pass
            'I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”' if not thyrsus_about_riskofthais and quest_orentius_thais_description00 and not thais_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”')
                jump thyrsusaboutdissentriskofthais01
            'I pat my bundles. “Do I have anything that could convince you?”' if not thyrsus_assistance_gray or (thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < 7 and (thyrsus_friendship+appearance_charisma) >= thyrsus_assistance_threshold):
                jump thyrsusselling01
            'I need his trust before I offer him a bribe. (disabled)' if thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < thyrsus_assistance_threshold:
                pass
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump thyrsusafterinteraction01

    label thyrsusaboutdissentriskofthais01:
        $ thyrsus_about_riskofthais = 1
        $ thyrsus_friendship += 1
        menu:
            'His eyes fill up with dread. His dropped shoulders and anxious toes confirm that your message was clear.
            '
            '“You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”' if (thyrsus_friendship+appearance_charisma) >= 7:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”')
                $ custom1 = "He raises his hands and rubs his arms, hesitating for another minute. Finally, he sighs. “You’re right. Who else, if not you? Let’s do it.”"
                jump thyrsusselling02
            'He doesn’t trust me enough to help me. (disabled)' if (thyrsus_friendship+appearance_charisma) < 7:
                pass
            'I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”' if not thyrsus_about_riskofthais and quest_orentius_thais_description00 and not thais_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”')
                jump thyrsusaboutdissentriskofthais01
            'I pat my bundles. “Do I have anything that could convince you?”' if not thyrsus_assistance_gray or (thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < 7 and (thyrsus_friendship+appearance_charisma) >= thyrsus_assistance_threshold):
                jump thyrsusselling01
            'I need his trust before I offer him a bribe. (disabled)' if thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < thyrsus_assistance_threshold:
                pass
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump thyrsusafterinteraction01

    label thyrsusselling01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pat my bundles. “Do I have anything that could convince you?”')
        $ thyrsus_assistance_gray = 1
        if (thyrsus_friendship+appearance_charisma) < thyrsus_assistance_threshold:
            menu:
                'He licks his lips, but then looks away. “I’d rather not look.”
                '
                '“You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”' if (thyrsus_friendship+appearance_charisma) >= 7:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know you can trust me, {color=#f6d6bd}Thyrsus{/color}. Help me help you.”')
                    $ custom1 = "He raises his hands and rubs his arms, hesitating for another minute. Finally, he sighs. “You’re right. Who else, if not you? Let’s do it.”"
                    jump thyrsusselling02
                'He doesn’t trust me enough to help me. (disabled)' if (thyrsus_friendship+appearance_charisma) < 7:
                    pass
                'I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”' if not thyrsus_about_riskofthais and quest_orentius_thais_description00 and not thais_defeated:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow an ominous pause. “If we don’t act, {color=#f6d6bd}Thais{/color} will.”')
                    jump thyrsusaboutdissentriskofthais01
                'I pat my bundles. “Do I have anything that could convince you?”' if not thyrsus_assistance_gray or (thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < 7 and (thyrsus_friendship+appearance_charisma) >= thyrsus_assistance_threshold):
                    jump thyrsusselling01
                'I need his trust before I offer him a bribe. (disabled)' if thyrsus_assistance_gray and (thyrsus_friendship+appearance_charisma) < thyrsus_assistance_threshold:
                    pass
                '“We’ll return to this later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                    jump thyrsusafterinteraction01
        $ shop = "thyrsuswares"
        $ peltnorth_selling = 1
        $ thingstosell = 0
        if item_asterioncloak:
            $ thingstosell += 1
        if item_ghoulblood:
            $ thingstosell += 1
        if item_magicchisel == 1 and not thyrsus_about_magicchisel1:
            $ thingstosell += 1
        if item_magicchisel == 2:
            $ thingstosell += 1
        # if item_trollurine:
        #     $ thingstosell += 1
        if not tutorial_selling:
            $ tutorial_selling = 1
        if thingstosell:
            if not tutorial_selling2:
                $ tutorial_selling2 = 1
        if thingstosell:
            show screen selling()
            menu:
                'He takes a deep breath, then reaches for one of his bracelets. “You may.”
                '
                '“We’ll return to this later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                    hide screen selling
                    jump thyrsusafterinteraction01
        else:
            menu:
                'You pull out some items, but {color=#f6d6bd}the warlock{/color} taps his toes to cut you off. “I don’t need things to sell. You want me to use my tribe’s trust against them, bring me something f’strong pneuma that I cad use. Or a rare blood f’a monster, for my poisons.”
                '
                '“We’ll return to this later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                    hide screen selling
                    jump thyrsusafterinteraction01

    label peatfieldsellingasterioncloak:
        menu:
            '“I need to see if it {i}really{/i} works,” he smacks his lips. “Ba I {i}cad{/i} use a warm blanket for fall nights.”
            '
            '“Take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it.”')
                $ renpy.notify("You gave away Asterion’s cloak.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s cloak.{/i}')
                $ item_asterioncloak -= 1
                $ thyrsus_friendship += 1
                $ custom1 = "He reaches for it with a creeper, then throws it on his shoulders and wraps himself up. After a minute or two of growing coziness, he flashes a yellow grin. “We’ve a deal, warden.”"
                $ minutes += 5
                hide screen selling
                jump thyrsusselling02
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                hide screen selling
                jump thyrsusafterinteraction01

    label peatfieldsellingghoulblood:
        menu:
            'He spares the phial no more than a glance, but after you describe where you got it, his eyes widen. “The color’s right,” even though he crouches, you hardly hear his whisper. “I know how to use it.”
            '
            '“Take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it.”')
                $ renpy.notify("You gave away the corpse eater’s blood.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the corpse eater’s blood.{/i}')
                $ item_ghoulblood -= 1
                $ thyrsus_friendship += 2
                $ custom1 = "You place the bottle into his soft, open palm, and he locks it in a wooden box hanging among his amulets. He stands up, and lets out a relieved sigh."
                hide screen selling
                jump thyrsusselling02
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                hide screen selling
                jump thyrsusafterinteraction01

    label peatfieldsellingmagicchisel1:
        $ thyrsus_about_magicchisel1 = 1
        menu:
            '“Do I look like I carve in rocks? I’d rather take something that breaks them.”
            '
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                hide screen selling
                jump thyrsusafterinteraction01

    label peatfieldsellingmagicchisel2:
        if not thyrsus_about_magicchisel2:
            $ thyrsus_about_magicchisel2 = 1
            $ minutes += 5
            $ custom1 = "Seeing his doubting look, you tell him to test the Tool’s capabilities on some rock. “Turf bricks are too gentle,” you add, and the man walks behind his hut. After maybe a minute, you hear a sound like thunder, then the man’s burst of laughter. “Brilliant!” He returns with tears in his eyes. “Will be a great help for the workers in the fields.”"
        else:
            $ custom1 = "“Yep, t’s nuff.”"
        menu:
            '[custom1]
            '
            '“Take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it.”')
                $ renpy.notify("You gave away The Tool of Destruction.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away The Tool of Destruction.{/i}')
                $ item_magicchisel = 0
                $ thyrsus_friendship += 1
                $ custom1 = "He flashes a yellow grin and shoves the chisel into a sack hanging from his belt. “We’ve a deal, warden.”"
                hide screen selling
                jump thyrsusselling02
            '“We’ll return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                hide screen selling
                jump thyrsusafterinteraction01

    label thyrsusselling02:
        $ thyrsus_about_dissent2 = 1
        $ renpy.notify("Journal updated: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        $ quest_orentius_thyrsus_description02 = "{color=#f6d6bd}Thyrsus{/color} can wait until I spend the night in {color=#f6d6bd}White Marshes{/color}. I should return to him only once I’m ready to speak with {color=#f6d6bd}Orentius{/color} - it’s the only chance I’ll get."
        menu:
            '[custom1]
            \n\n“Here’s how t’s going to work. Tell me once you’re ready to talk with {color=#f6d6bd}Orentius{/color}, then get to {color=#f6d6bd}White Marshes{/color} an’ spend the night there. In the middle f’the night, I’ll show up with’a’few {i}friends{/i}, an’ will clear the way for you. Ba remember - t’s your only chance.”
            '
            '“Tell me about {color=#f6d6bd}Orentius{/color}.”' if not thyrsus_about_dissent_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Orentius{/color}.”')
                $ thyrsus_about_dissent_question1 = 1
                $ description_orentius08 = "According to {color=#f6d6bd}Thyrsus{/color}: “I was never close with him. When I left the village to learn spells, many years ago, he was ba a priest f’ours. Once I returned, he came forward like a prophet, shouting with zeal, warning the tribe needs to {i}prepare{/i} itself, for whatever. When his followers brought the first dead shells to the village, they were still in the minority, ba were ready to fight for him. We cad either throw them all outside f’our walls, or... Empty disputes, empty threats. You can tell how it all ended.”"
                $ custom1 = "“I was never close with him. When I left the village to learn spells, many years ago, he was ba a priest f’ours. Once I returned, he came forward like a prophet, shouting with zeal, warning the tribe needs to {i}prepare{/i} itself, for whatever. When his followers brought the first dead shells to the village, they were still in the minority, ba were ready to fight for him. We cad either throw them all outside f’our walls, or...” He waves it off. “Empty disputes, empty threats. You can tell how it all ended.”"
                jump thyrsus_about_dissent205
            '“Any ideas how to convince him?”' if not thyrsus_about_dissent_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any ideas how to convince him?”')
                $ thyrsus_about_dissent_question2 = 1
                $ description_orentius09 = "According to {color=#f6d6bd}Thyrsus{/color}, he may be more eager to listen to me if I have {color=#f6d6bd}Helvius’{/color} trust on my side."
                $ custom1 = "“Why wad I know? He didn’t listen to me,” he taps his toes. “Be prepared. He quotes Wright’s Tablets, talks about what’s just, right, an’ whatnots... Ba he also knows a lot about the tribe. If {color=#f6d6bd}Helvius{/color} speaks f’you kindly, {color=#f6d6bd}Orentius{/color} will know it.”"
                jump thyrsus_about_dissent205
            '“Who could help me get a better understanding of necromancy?”' if not thyrsus_about_dissent_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who could help me get a better understanding of necromancy?”')
                $ thyrsus_about_dissent_question3 = 1
                $ custom1 = "He blows out his cheeks, moving his lips left and right. “Well, not the druids...” He speaks slowly. “Mayhap {color=#f6d6bd}the monks{/color} in the mountains to the west, beyond {color=#f6d6bd}Old Págos{/color}? Only they’ve time to learn about things they don’t need to survive.”"
                $ description_monastery06 = "I’ve heard they may be able to give me a better understanding of necromancy."
                jump thyrsus_about_dissent205
            '“Should I be afraid of him? Will I need a weapon?”' if not thyrsus_about_dissent_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I be afraid of him? Will I need a weapon?”')
                $ thyrsus_about_dissent_question4 = 1
                $ custom1 = "“He’s an old, weak man, he wadn’t hurt a rat. Ba the only way I’m going to convince anyone to help us is if t’s clear you’re just as harmless. You’ll leave your axe by your bags,” he says it like it’s an order, but you doubt he noticed the dagger in your boot."
                jump thyrsus_about_dissent205
            '“Are you {i}sure{/i} you can get me in?”' if not thyrsus_about_dissent_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you {i}sure{/i} you can get me in?”')
                $ thyrsus_about_dissent_question5 = 1
                $ custom1 = "He giggles. “You underestimate how many secrets a warlock knows, an’ how many favors he carries.” He grabs and shakes the amulets on his chest, as if they’re meant to explain it further."
                jump thyrsus_about_dissent205
            '“I’m ready to meet with him.”' if not thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to meet with him.”')
                $ thyrsus_orentius_canhelp = 1
                $ custom1 = "A long pause. “We’ll see. Go to the village an’ spend the night there. I’ll wake you up."
                $ renpy.notify("Journal updated: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
                $ quest_orentius_thyrsus_description02 = "{color=#f6d6bd}Thyrsus{/color} will wait for me to fall asleep in {color=#f6d6bd}White Marshes{/color}. He’ll then take me to {color=#f6d6bd}Orentius{/color}."
                jump thyrsus_about_dissent205
            '“Fine. I’ll come here once I’m ready.”' if not thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll come here once I’m ready.”')
                jump thyrsusafterinteraction01
            '“See you in {color=#f6d6bd}White Marshes{/color}.”' if thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “See you in {color=#f6d6bd}White Marshes{/color}.”')
                jump thyrsusafterinteraction01

    label thyrsus_about_dissent204:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about {color=#f6d6bd}Orentius{/color}.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ custom1 = "He sighs. “Of course.”"
        jump thyrsus_about_dissent205

    label thyrsus_about_dissent205:
        menu:
            '[custom1]
            '
            '“Tell me about {color=#f6d6bd}Orentius{/color}.”' if not thyrsus_about_dissent_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Orentius{/color}.”')
                $ thyrsus_about_dissent_question1 = 1
                $ description_orentius08 = "According to {color=#f6d6bd}Thyrsus{/color}: “I was never close with him. When I left the village to learn spells, many years ago, he was ba a priest f’ours. Once I returned, he came forward like a prophet, shouting with zeal, warning the tribe needs to {i}prepare{/i} itself, for whatever. When his followers brought the first dead shells to the village, they were still in the minority, ba were ready to fight for him. We cad either throw them all outside f’our walls, or... Empty disputes, empty threats. You can tell how it all ended.”"
                $ custom1 = "“I was never close with him. When I left the village to learn spells, many years ago, he was ba a priest f’ours. Once I returned, he came forward like a prophet, shouting with zeal, warning the tribe needs to {i}prepare{/i} itself, for whatever. When his followers brought the first dead shells to the village, they were still in the minority, ba were ready to fight for him. We cad either throw them all outside f’our walls, or...” He waves it off. “Empty disputes, empty threats. You can tell how it all ended.”"
                jump thyrsus_about_dissent205
            '“Any ideas how to convince him?”' if not thyrsus_about_dissent_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any ideas how to convince him?”')
                $ thyrsus_about_dissent_question2 = 1
                $ description_orentius09 = "According to {color=#f6d6bd}Thyrsus{/color}, he may be more eager to listen to me if I have {color=#f6d6bd}Helvius’{/color} trust on my side."
                $ custom1 = "“Why wad I know? He didn’t listen to me,” he taps his toes. “Be prepared. He quotes Wright’s Tablets, talks about what’s just, right, an’ whatnots... Ba he also knows a lot about the tribe. If {color=#f6d6bd}Helvius{/color} speaks f’you kindly, {color=#f6d6bd}Orentius{/color} will know it.”"
                jump thyrsus_about_dissent205
            '“Who could help me get a better understanding of necromancy?”' if not thyrsus_about_dissent_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who could help me get a better understanding of necromancy?”')
                $ thyrsus_about_dissent_question3 = 1
                $ custom1 = "He blows out his cheeks, moving his lips left and right. “Well, not the druids...” He speaks slowly. “Mayhap {color=#f6d6bd}the monks{/color} in the mountains to the west, beyond {color=#f6d6bd}Old Págos{/color}? Only they’ve time to learn about things they don’t need to survive.”"
                $ description_monastery06 = "I’ve heard they may be able to give me a better understanding of necromancy."
                jump thyrsus_about_dissent205
            '“Should I be afraid of him? Will I need a weapon?”' if not thyrsus_about_dissent_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I be afraid of him? Will I need a weapon?”')
                $ thyrsus_about_dissent_question4 = 1
                $ custom1 = "“He’s an old, weak man, he wadn’t hurt a rat. Ba the only way I’m going to convince anyone to help us is if t’s clear you’re just as harmless. You’ll leave your axe by your bags,” he says it like it’s an order, but you doubt he noticed the dagger in your boot."
                jump thyrsus_about_dissent205
            '“Are you {i}sure{/i} you can get me in?”' if not thyrsus_about_dissent_question5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you {i}sure{/i} you can get me in?”')
                $ thyrsus_about_dissent_question5 = 1
                $ custom1 = "He giggles. “You underestimate how many secrets a warlock knows, an’ how many favors he carries.” He grabs and shakes the amulets on his chest, as if they’re meant to explain it further."
                jump thyrsus_about_dissent205
            '“I’m ready to meet with him.”' if not thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to meet with him.”')
                $ thyrsus_orentius_canhelp = 1
                $ custom1 = "A long pause. “We’ll see. Go to the village an’ spend the night there. I’ll wake you up."
                $ renpy.notify("Journal updated: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
                $ quest_orentius_thyrsus_description02 = "{color=#f6d6bd}Thyrsus{/color} will wait for me to fall asleep in {color=#f6d6bd}White Marshes{/color}. He’ll then take me to {color=#f6d6bd}Orentius{/color}."
                jump thyrsus_about_dissent205
            '“Fine. I’ll come here once I’m ready.”' if not thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll come here once I’m ready.”')
                jump thyrsusafterinteraction01
            '“See you in {color=#f6d6bd}White Marshes{/color}.”' if thyrsus_orentius_canhelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “See you in {color=#f6d6bd}White Marshes{/color}.”')
                jump thyrsusafterinteraction01

label thyrsus_about_returninghome01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Now that your tribe has been shaken by the recent events, why don’t you return to the village?”')
    $ thyrsus_about_returninghome = 1
    $ thyrsus_friendship += 1
    $ questionpreset = "thyrsus1"
    menu:
        '“I’ll try it in winter! This place,” he hits the front wall with his creeper, and you’re sure the punched brick moved a little bit, “{i}is{/i} my home. For years now I’ve stood away from digging fields an’ cutting rocks. As long’s monsters know the smell f’my poisons, I’m safe. We’ll see how {i}awkward{/i} the gossip will get now that I had a part in the {i}prophet’s{/i} fall!” He laughs brightly.
        '
        '(thyrsus1 set)':
            pass

label thyrsusregular02:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ peatfield_firsttime_destroyed = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if quest_thyrsusgift == 1:
        $ elpis_about_thyrsusgift1 = 0
        $ howlersdell_mundanework_type = "hunters"
        $ quest_thyrsusgift = 3
        $ renpy.notify("Quest completed: Thyrsus’ Wand")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Thyrsus’ Wand{/i}')
        $ quest_thyrsusgift_description_faildescription = "{color=#f6d6bd}Thyrsus{/color} no longer needs my assistance."
    menu:
        'You’re surrounded by silence, as if all the birds and frogs are hiding behind rocks and branches. Even from afar you notice the bloodstains on the door, and as you stand up in the saddle, you see scraps of fabric, broken vessels, and fallen furniture. The brutal encounter wasn’t fast, and there are no dead shells to burn.
        '
        'He tried to help his tribe, and didn’t reach shelter in time.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He tried to help his tribe, and didn’t reach shelter in time.')
            jump thyrsusregular02a
        'Without the village, the wilderness is thrown off-balance. Beasts grow bolder.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without the village, the wilderness is thrown off-balance. Beasts grow bolder.')
            jump thyrsusregular02a
        'Even a dim undead could open this door. And they’re not afraid of poisons.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Even a dim undead could open this door. And they’re not afraid of poisons.')
            jump thyrsusregular02a
        'He got what he deserved. He ought to have done {i}something{/i} long before I got here.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He got what he deserved. He ought to have done {i}something{/i} long before I got here.')
            jump thyrsusregular02a
        '...It’s my fault.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...It’s my fault.')
            $ pc_faithpoints += 1
            jump thyrsusregular02a

    label thyrsusregular02a:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        $ quest_explorepeninsula_description17a = "There’s no soul left to harvest the peat of {color=#f6d6bd}White Marshes{/color}."
        if pc_likeshorsename:
            $ custom1 = "It won’t like the stench of blood."
        else:
            $ custom1 = "The “culprit” may be close."
        menu:
            'You turn {color=#f6d6bd}[horsename]{/color} around. [custom1]
            '
            'I ride away. (disabled)':
                pass

label thyrsus_about_thyrsusgiftALL:
    label thyrsus_about_thyrsusgift101:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you have a message for the druids, I {i}could{/i} do you a favor.”')
        $ thyrsus_about_thyrsusgift = 1
        $ minutes += 2
        menu:
            '“Such’a waste f‘thoughts, this bunch,” his angry look is at odds with his hesitancy. “I’d rather talk to the rats f’the bogs, or even...” 
            \n\nHis eyes leave you, staring at the smoke coming from his home on the horizon. After a longer moment, his creepers rise up tensely. 
            \n\n“No, I’ve got no words for {i}the forest speakers{/i}. But they do have my stuff. I’d pay you for bringing it back.” 
            '
            '“What stuff?”' if not thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What stuff?”')
                $ thyrsus_about_thyrsusgift_mainquestion_1 = 1
                $ minutes += 1
                $ custom1 = "“Things I left behind when I snuck out f’that monkey house. For reasons. I’d like all f’them back, ba one more than the others. Just some polished twig.” A pause marks the moment when he realizes the stupidity of his lie. “My old wand.”"
                jump thyrsus_about_thyrsusgift102
            '“You don’t seem to be using a wand right now.”' if not thyrsus_about_thyrsusgift_bonusquestion_6 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t seem to be using a wand right now.”')
                $ thyrsus_about_thyrsusgift_bonusquestion_6 = 1
                $ minutes += 1
                $ custom1 = "“No need for it.” The creepers point in your direction, swiftly tracking the movement of your shoulders, as if they have their own eyes. “I need no teachers. No masters. No {i}breathing exercise{/i},” a fake chuckle."
                jump thyrsus_about_thyrsusgift102
            '“Pay me with what?”' if not thyrsus_about_thyrsusgift_mainquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pay me with what?”')
                $ thyrsus_about_thyrsusgift_mainquestion_2 = 1
                $ minutes += 1
                $ custom1 = "“Aren’t people {i}like you{/i}” he says with little kindness “in need f’healing potions, at all times? I cad brew you a small one. Or I cad spare you a few coins instead. Let’s say... One for riding to {color=#f6d6bd}Howler’s{/color}. One for talking with the druids. One for bringing my stuff back.” He raises three fingers."
                jump thyrsus_about_thyrsusgift102
            '“Why would they keep your stuff for this long?”' if not thyrsus_about_thyrsusgift_bonusquestion_3 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would they keep your stuff for this long?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_3 = 1
                $ minutes += 1
                $ custom1 = "“Beats me. Ba a year ago a caravan from there stopped by, looking for the mushrooms from our bogs. Before they took their noisy boots out f’here, one f’the guards cried that he’d break my {i}baby wand{/i}, make me pay for the time I cracked his nose with’a branch.” He plays with his amulets as his eyes avoid yours. “T’was a mistake, I was still learning.”"
                jump thyrsus_about_thyrsusgift102
            '“What do you even need this stuff for?”' if not thyrsus_about_thyrsusgift_bonusquestion_1 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you even need this stuff for?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_1 = 1
                $ minutes += 1
                $ custom1 = "He rubs the ground with his heel, observing his dirty toes. “It’s mine,” his voice gets quieter. “I deserve it.”"
                jump thyrsus_about_thyrsusgift102
            '“How was it? In {color=#f6d6bd}Howler’s Dell{/color}?”' if not thyrsus_about_thyrsusgift_bonusquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How was it? In {color=#f6d6bd}Howler’s Dell{/color}?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_2 = 1
                $ minutes += 1
                $ custom1 = "He blinks. “I left, didn’t I? Or rather ran away. Cadn’t handle their looks. Their tone. They think they’re betta than us here. An’didn’t let me forget it.”"
                $ description_thyrsus04a = "He left the village when he realized that he was seen by everyone as an outsider."
                $ description_howlersdell09 = "According to {color=#f6d6bd}Thyrsus{/color}: “Cadn’t handle their looks. Their tone. They think they’re betta than us here. An’ didn’t let me forget it.”"
                jump thyrsus_about_thyrsusgift102
            '“Any tips on how to talk with the druids?”' if not thyrsus_about_thyrsusgift_bonusquestion_5 and thyrsus_about_thyrsusgift_bonusquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips on how to talk with the druids?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_5 = 1
                $ minutes += 1
                $ custom1 = "“Can tell you how {i}not{/i} to talk with them. Don’t laugh. Don’t look at them. Don’t tell the truth. Just bow down an’ repeat how {i}honored{/i} you are they’re sparing you as much’s a glance.”"
                $ description_druids11 = "According to {color=#f6d6bd}Thyrsus{/color}: “Can tell you how {i}not{/i} to talk with them. Don’t laugh. Don’t look at them. Don’t tell the truth. Just bow down an’ repeat how {i}honored{/i} you are they’re sparing you as much’s a glance.”"
                jump thyrsus_about_thyrsusgift102
            '“Is that why you were sent to the druids? You couldn’t control pneuma?”' if not thyrsus_about_thyrsusgift_bonusquestion_4 and thyrsus_about_thyrsusgift_bonusquestion_3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is that why you were sent to the druids? You couldn’t control pneuma?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_4 = 1
                $ minutes += 1
                $ custom1 = "“Not much talent for spells in our blood at {color=#f6d6bd}White Marshes{/color},” he says nonchalantly. “With no one there to guide me, I hurt a few kids before I figured things out.”\n\nSeeing your raised eyebrow, he continues, but cautiously. “Some tribes are just like that. Young ones, specially. Give us two, three generations more, an’ a mage or two from the outside. Art needs to grow.”"
                $ description_whitemarshes15 = "According to {color=#f6d6bd}Thyrsus{/color}, the locals are weak in pneuma."
                jump thyrsus_about_thyrsusgift102
            '“I know everything I need to.”' if thyrsus_about_thyrsusgift_mainquestion_1 and thyrsus_about_thyrsusgift_mainquestion_2 and not quest_thyrsusgift:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know everything I need to.”')
                jump thyrsus_about_thyrsusgift1_after
            '“That’s about it.”' if thyrsus_about_thyrsusgift_mainquestion_1 and thyrsus_about_thyrsusgift_mainquestion_2 and quest_thyrsusgift:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s about it.”')
                jump thyrsus_about_thyrsusgift101bonus_after

    label thyrsus_about_thyrsusgift101bonus:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a few more questions about the old wand.”')
        $ custom1 = "“Just an old twig. What’s there to say?”"
        jump thyrsus_about_thyrsusgift102

    label thyrsus_about_thyrsusgift102:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“What stuff?”' if not thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What stuff?”')
                $ thyrsus_about_thyrsusgift_mainquestion_1 = 1
                $ minutes += 1
                $ custom1 = "“Thing I left behind when I snuck out f’that monkey house. For reasons. I’d like all f’them back, ba one more than the others. Just some polished twig.” A pause marks the moment when he realizes the stupidity of his lie. “My old wand.”"
                jump thyrsus_about_thyrsusgift102
            '“You don’t seem to be using a wand right now.”' if not thyrsus_about_thyrsusgift_bonusquestion_6 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t seem to be using a wand right now.”')
                $ thyrsus_about_thyrsusgift_bonusquestion_6 = 1
                $ minutes += 1
                $ custom1 = "“No need for it.” The creepers point in your direction, swiftly tracking the movement of your shoulders, as if they have their own eyes. “I need no teachers. No masters. No {i}breathing exercise{/i},” a fake chuckle."
                jump thyrsus_about_thyrsusgift102
            '“Pay me with what?”' if not thyrsus_about_thyrsusgift_mainquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pay me with what?”')
                $ thyrsus_about_thyrsusgift_mainquestion_2 = 1
                $ minutes += 1
                $ custom1 = "“Aren’t people {i}like you{/i}” he says with little kindness “in need f’healing potions, at all times? I cad brew you a small one. Or I cad spare you a few coins instead. Let’s say... One for riding to {color=#f6d6bd}Howler’s{/color}. One for talking with the druids. One for bringing my stuff back.” He raises three fingers."
                jump thyrsus_about_thyrsusgift102
            '“Why would they keep your stuff for this long?”' if not thyrsus_about_thyrsusgift_bonusquestion_3 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would they keep your stuff for this long?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_3 = 1
                $ minutes += 1
                $ custom1 = "“Beats me. Ba a year ago a caravan from there stopped by, looking for the mushrooms from our bogs. Before they took their noisy boots out f’here, one f’the guards cried that he’d break my {i}baby wand{/i}, make me pay for the time I cracked his nose with’a branch.” He plays with his amulets as his eyes avoid yours. “T’was a mistake, I was still learning.”"
                jump thyrsus_about_thyrsusgift102
            '“What do you even need this stuff for?”' if not thyrsus_about_thyrsusgift_bonusquestion_1 and thyrsus_about_thyrsusgift_mainquestion_1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you even need this stuff for?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_1 = 1
                $ minutes += 1
                $ custom1 = "He rubs the ground with his heel, observing his dirty toes. “It’s mine,” his voice gets quieter. “I deserve it.”"
                jump thyrsus_about_thyrsusgift102
            '“How was it? In {color=#f6d6bd}Howler’s Dell{/color}?”' if not thyrsus_about_thyrsusgift_bonusquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How was it? In {color=#f6d6bd}Howler’s Dell{/color}?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_2 = 1
                $ minutes += 1
                $ custom1 = "He blinks. “I left, didn’t I? Or rather ran away. Cadn’t handle their looks. Their tone. They think they’re betta than us here. An’didn’t let me forget that.”"
                $ description_thyrsus04a = "He left the village when he realized that he was seen by everyone as an outsider."
                $ description_howlersdell09 = "According to {color=#f6d6bd}Thyrsus{/color}: “Cadn’t handle their looks. Their tone. They think they’re betta than us here. An’ didn’t let me forget that.”"
                jump thyrsus_about_thyrsusgift102
            '“Any tips on how to talk with the druids?”' if not thyrsus_about_thyrsusgift_bonusquestion_5 and thyrsus_about_thyrsusgift_bonusquestion_2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips on how to talk with the druids?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_5 = 1
                $ minutes += 1
                $ custom1 = "“Can tell you how {i}not{/i} to talk with them. Don’t laugh. Don’t look at them. Don’t tell the truth. Just bow down an’ repeat how {i}honored{/i} you are they’re sparing you as much’s a glance.”"
                $ description_druids11 = "According to {color=#f6d6bd}Thyrsus{/color}: “Can tell you how {i}not{/i} to talk with them. Don’t laugh. Don’t look at them. Don’t tell the truth. Just bow down an’ repeat how {i}honored{/i} you are they’re sparing you as much’s a glance.”"
                jump thyrsus_about_thyrsusgift102
            '“Is that why you were sent to the druids? You couldn’t control pneuma?”' if not thyrsus_about_thyrsusgift_bonusquestion_4 and thyrsus_about_thyrsusgift_bonusquestion_3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is that why you were sent to the druids? You couldn’t control pneuma?”')
                $ thyrsus_about_thyrsusgift_bonusquestion_4 = 1
                $ minutes += 1
                $ custom1 = "“Not much talent for spells in our blood at {color=#f6d6bd}White Marshes{/color},” he says nonchalantly. “With no one there to guide me, I hurt a few kids before I figured things out.”\n\nSeeing your raised eyebrow, he continues, but cautiously. “Some tribes are just like that. Young ones, specially. Give us two, three generations more, an’ a mage or two from the outside. Art needs to grow.”"
                $ description_whitemarshes15 = "According to {color=#f6d6bd}Thyrsus{/color}, the locals are weak in pneuma."
                jump thyrsus_about_thyrsusgift102
            '“I know everything I need to.”' if thyrsus_about_thyrsusgift_mainquestion_1 and thyrsus_about_thyrsusgift_mainquestion_2 and not quest_thyrsusgift:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know everything I need to.”')
                jump thyrsus_about_thyrsusgift1_after
            '“That’s about it.”' if thyrsus_about_thyrsusgift_mainquestion_1 and thyrsus_about_thyrsusgift_mainquestion_2 and quest_thyrsusgift:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s about it.”')
                jump thyrsus_about_thyrsusgift101bonus_after

    label thyrsus_about_thyrsusgift1_after:
        $ quest_thyrsusgift = 1
        $ renpy.notify("New entry: Thyrsus’ Wand")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Thyrsus’ Wand{/i}')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ minutes += 1
        $ questionpreset = "thyrsus1"
        menu:
            'His amulets rattle with joy. “Good.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_about_thyrsusgift101bonus_after:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "thyrsus1"
        menu:
            '“What now?”
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_about_thyrsusgift103:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I brought you your {i}prized possessions{/i}.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ quest_thyrsusgift_dayofsuccess = day
        $ item_thyrsusgift = 0
        $ renpy.notify("You lost the bundle.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the bundle.{/i}')
        $ thyrsus_friendship += 1
        show peatfield shirt at basicfade
        $ minutes += 5
        menu:
            'He grabs the package and unwraps it rapidly. At the sight of the broken twig he lets out a sigh, but finds some comfort in stroking the buckle, and even smiles at the rotten doll, holding it with a creeper. He takes a whiff of his old tunic, but then throws it away, into the mud.
            \n\nThe silence lingers.
            '
            '“Is my potion ready?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is my potion ready?”')
                $ custom1 = "“Very much so.” He enters the hut, searches through a pile of clay bottles - some of them land on the floor - and brings you one that’s especially small. Judging by the seal, it may be seasons old.\n\n"
                $ item_smallhealingpotion += 1
                $ renpy.notify("You received a small healing potion.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a small healing potion.{/i}')
                jump thyrsus_about_thyrsusgift103_a
            '“Three coins, wasn’t it?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Three coins, wasn’t it?”')
                $ custom1 = "“It was.” His fingers flinch nervously as he reaches for a small pouch buried among many others. Before he gives you the coins, he needs to shake some dried basil off them.\n\n"
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the bundle.{/i}')
                show screen notifyimage( "+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
                $ coins += 3
                label thyrsus_about_thyrsusgift103_a:
                    menu:
                        '[custom1]“Cheers for wardening this stuff for me.”
                        '
                        '“Just doing my job.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just doing my job.”')
                            $ thyrsus_friendship += 1
                            $ custom1 = "He spares you a slow nod, followed by a kind smile."
                            jump thyrsus_about_thyrsusgift102_b
                        '“You’ve paid quite a bit for a sentimental trip.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve paid quite a bit for a sentimental trip.”')
                            $ custom1 = "He shrugs your words aside. “T’was nothing f’the sort. T’s meant to be a gift.”"
                            label thyrsus_about_thyrsusgift102_b:
                                $ quest_thyrsusgift = 2
                                $ renpy.notify("Quest completed: Thyrsus’ Wand")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Thyrsus’ Wand{/i}')
                                $ can_leave = 1
                                $ can_rest = 1
                                $ can_items = 1
                                $ questionpreset = "thyrsus1"
                                menu:
                                    '[custom1]
                                    '
                                    '(thyrsus1 set)':
                                        pass

    label thyrsus_about_thyrsusgift_parentscomment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How did it go? With your parents?”')
        $ thyrsus_about_thyrsusgift_parentscomment = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "thyrsus1"
        menu:
            'He steps away, raising his eyes, but can’t mask the pain in his voice. “It didn’t. They didn’t take it. Told me to take it with me, into my pyre.”
            '
            '(thyrsus1 set)':
                pass

    label thyrsus_about_thyrsusgift_druidcomment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may want to have a chat with the old druid.”')
        $ thyrsus_about_thyrsusgift_druidcomment = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "thyrsus1"
        $ thyrsus_friendship += 1
        menu:
            'You try to repeat the hermit’s words, but coming from your lips they sound awkward, preachy, and they bounce off the warlock without leaving any visible dent. 
            \n\n“Mayhap. T’s far away. Will think about it.”
            '
            '(thyrsus1 set)':
                pass
