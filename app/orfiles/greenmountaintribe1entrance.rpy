###################### THE TRIBE OF THE GREEN MOUNTAIN
default greenmountaintribe_firsttime = 0
default greenmountaintribe_firsttime_achievement = 0
default greenmountaintribe_fluff = ""
default greenmountaintribe_fluff_old = ""
default greenmountaintribe_cave_fluff = ""
default greenmountaintribe_cave_fluff_old = ""

default greenmountaintribe_reputation = 0
default greenmountaintribe_banned = 0

default greenmountaintribe_firstattitude = 0
default greenmountaintribe_secondattitude = 0

default greenmountaintribe_sleep = 0
default greenmountaintribe_about_cephasgaiane1 = 0
default greenmountaintribe_about_cephasgaiane2 = 0
default greenmountaintribe_about_wanteditems = 0
default greenmountaintribe_about_missinghunters = 0
default greenmountaintribe_about_asterion = 0

label greenmountaintribe01:
    nvl clear
    $ pc_area = "greenmountaintribe"
    label greenmountaintribe_fluffloop:
        $ greenmountaintribe_fluff = renpy.random.choice(['The villagers are busy with their work, sometimes glancing at you from a distance, but not paying much attention to you. A few of them grab spears and tools and approach the entrance, previously unguarded. {color=#f6d6bd}The saurian rider{/color} shows up soon after.', 'A few armed villagers, {color=#f6d6bd}the saurian rider{/color} included, are gathered at the entrance, engaged in a loud discussion. Once you dismount, they fall silent, giving each other angry scowls, then welcome you with cold nods.', 'The gatekeepers welcome you by blowing a horn. For a few breaths, there’s no one in sight, then {color=#f6d6bd}the saurian rider{/color} runs out of the cave mouth, welcoming you with a handwave.', 'A few villagers are sitting on the terrace walls and the roof of the shed, enjoying their meals as they gossip and laugh at each other’s jokes. Once you get closer, they welcome you in the Old Speech, then one of them announces loudly that the “radarden” is back. {color=#f6d6bd}The saurian rider{/color} shows up soon after, walking down the stairs.', 'You notice the saurian even before you reach the village. {color=#f6d6bd}The rider{/color} waves to you, then returns to the village, ready to greet you at the cave mouth.'])
        if greenmountaintribe_fluff_old == greenmountaintribe_fluff:
            jump greenmountaintribe_fluffloop
        else:
            $ greenmountaintribe_fluff_old = greenmountaintribe_fluff
    label greenmountaintribe_cave_fluffloop:
        $ greenmountaintribe_cave_fluff = renpy.random.choice(['{color=#f6d6bd}The chief and the shaman{/color} are already in the chamber, chatting with each other. They welcome you with polite nods.', 'While {color=#f6d6bd}Cephas{/color} is already waiting for you, he asks you to wait for a few minutes. When {color=#f6d6bd}Gaiane{/color} shows up, she coughs a bit, but welcomes you with a warm smile and sits down on the trunk, letting out a loud, relaxed sigh. She spreads her stones on the fabric, moving them with great care.', 'While {color=#f6d6bd}Gaiane{/color} is already waiting for you, teaching a young boy how to grind herbs, she asks you to wait for a bit. When {color=#f6d6bd}Cephas{/color} gets back, he’s gasping for air, holding his sword. Before he sits down, he shouts a few orders down the tunnel in the Old Speech.', 'Just before you enter the chamber, you’re told to wait for a bit. You hear the quiet, grim voices of {color=#f6d6bd}Cephas{/color} and {color=#f6d6bd}Gaiane{/color}, and after you’re invited to join them, their eyes are absent. It takes a few moments before {color=#f6d6bd}the shaman{/color} asks you to speak.'])
        if greenmountaintribe_cave_fluff_old == greenmountaintribe_cave_fluff:
            jump greenmountaintribe_cave_fluffloop
        else:
            $ greenmountaintribe_cave_fluff_old = greenmountaintribe_cave_fluff
    $ shop = "greenmountaintribeentrance"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not greenmountaintribe_firsttime:
        $ world_known_npcs += 2
        $ world_known_areas += 1
        $ greenmountaintribe_firsttime = 1
        $ mountainroad_unlocked = 1
        jump greenmountaintribefirsttime01
    else:
        if asterion_found and not cephasgaiane_about_highisland_permission:
            stop nature fadeout 4.0
            show areapicture mountainroadtogreenmountaintribe3 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump greenmountaintriberegular01BAN
        else:
            stop nature fadeout 4.0
            show areapicture greenmountaintribeentrance01 at basicfade
            $ renpy.music.play("audio/blackyenwhitebirch_greenmountaintribe_loop.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump greenmountaintriberegular01

label greenmountaintribefirsttime01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ renpy.force_autosave(take_screenshot=True, block=True)
    show areapicture mountainroadtogreenmountaintribe1 at basicfade
    play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    menu:
        'The winds, cold sweat, and altitude make you want to simultaneously take off your cloak and put on some heavier clothes. At least {color=#f6d6bd}[horsename]{/color} doesn’t seem to care.
        \n\nYou take deeper breaths. The path ahead seems gentler - there are no more trees, and you’re surrounded by grasses, pebbles, sporadic bushes. You look down at the herds gathering around the stream, the rustling leaves, and the birds, large and small, flying above the forests of the peninsula. From here, everything seems calm.
        '
        'Too bad most people will never catch such a view.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Too bad most people will never catch such a view.')
            jump greenmountaintribefirsttime01a
        'It’s just an illusion. These trees hide blood, blades, and claws. There’s nothing peaceful about them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s just an illusion. These trees hide blood, blades, and claws. There’s nothing peaceful about them.')
            jump greenmountaintribefirsttime01a
        'I wish I could see all of this from the peak of the mountain.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish I could see all of this from the peak of the mountain.')
            jump greenmountaintribefirsttime01a
        'At least getting down won’t be as difficult.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least getting down won’t be as difficult.')
            jump greenmountaintribefirsttime01a

    label greenmountaintribefirsttime01a:
        if asterion_found and not cephasgaiane_about_highisland_permission:
            stop nature fadeout 4.0
            show areapicture mountainroadtogreenmountaintribe2 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
            jump greenmountaintribefirsttime01BAN
        else:
            if pc_religion == "pagan":
                $ custom1 = "that at first confuses you, but you manage to figure out a few of the words. She’s using the Old Speech, the almost forgotten tongue of your ancestors, though in a dialect so distant that you doubt you could speak freely with her. You think she’s saying something similar to “{i}Greetings, traveler. Are you lost?{/i}”"
            else:
                $ custom1 = "that you’ve only heard used among the elders raised in distant villages. The Old Speech is almost forgotten outside of the most remote pagan tribes."
            menu:
                'A loud screech reaches you from up the path, where at the top of a crag you see a massive saurian standing on four limbs. It’s displaying proudly its dark-green skin with a bit brighter stomach, and orange stripes on its legs and eyebrows, as well as the tail, which is swinging left and right.
                \n\nThe size of the monster makes you stop, but before you turn around, you realize there’s {color=#f6d6bd}a short woman{/color} sitting on its back - dressed in a red gambeson and an iron helmet, with green pants that blend in with her mount. You can’t see the details of her hair, but she’s not attacking you just yet, resting the blunt edge of her spear on the ground. Her other hand holds the reins, attached to a “bridle” put on the monster’s head, cramping its wide mouth.
                \n\nShe raises her weapon in a greeting, and speaks in a language [custom1]
                '
                'I greet her back, using the remains of the Old Speech I heard as a kid. “I seek the village at the end of this path!”' if pc_religion == "pagan":
                    $ galerocks_reputation += 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I greet her back, using the remains of the Old Speech I heard as a kid. “I seek the village at the end of this path!”')
                    $ custom1 = "This time it’s her who pauses, then repeats: “{i}The village?{/i}” She pronounces it so differently from you that it makes you smile, but you confirm her guess. During the following minutes, you both try to get used to each other’s speech. Whenever she uses the City Tongue, she does so with sounds she’s clearly not used to saying out loud. But as you combine it with gestures and the few words you know from the Old Speech, it’s enough to move the conversation forward rather smoothly.\n\nFinally, she asks if you have a message for {color=#f6d6bd}the chief{/color} or {color=#f6d6bd}the shaman{/color}. “{i}Tell me, I’ll pass it to them.{/i}”"
                    jump greenmountaintribefirsttime01b
                'All I have left is the City Tongue. “I can’t understand you!”' if pc_religion != "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- All I have left is the City Tongue. “I can’t understand you!”')
                    $ custom1 = "She stays still for a few breaths, then uses sounds that she’s clearly not used to saying out loud. “You lost?” During the following minutes, you both try to get used to each other’s speech, though sometimes you can’t find any common ground, depending on the combination of the City Tongue and gestures.\n\nYou explain that you’re heading to the village at the end of this path, and she asks if you have a message for {color=#f6d6bd}the chief{/color} or {color=#f6d6bd}the shaman{/color}. “Say it to me.”"
                    label greenmountaintribefirsttime01b:
                        menu:
                            '[custom1]
                            '
                            '“I need to speak with them myself. I’m the local roadwarden.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to speak with them myself. I’m the local roadwarden.”')
                                $ at_activate = 1
                                $ at = 0
                                $ minutes += 5
                                if item_wingedhourglass_worn:
                                    $ greenmountaintribe_reputation -= 1
                                    $ pc_faithpoints += 1
                                    $ custom1 = "She points at your neck. “And like cityfolks, you carry dread.” You glance at your winged hourglass, trying to not think about the green beast observing you from just a few feet away. “What do {i}radardens{/i} do?”"
                                else:
                                    $ custom1 = "“What do radardens do, really?”"
                                menu:
                                    'Even though she doesn’t give any clear command to her mount, it takes a few steps forward, moving without needing to speed up quickly. After a confident leap, the beast lands on the crag right above you, allowing the warrior to look at you closely. “Radarden,” she says in the City Tongue. “Like {color=#f6d6bd}Asterion{/color}, t’ cityfolk.” You nod. [custom1]
                                    '
                                    ' (disabled)' ( condition="at == 0" ):
                                        pass
                                    '“I protect travelers and help settlements stay in touch with each other.”' ( condition="at == 'friendly'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “I protect travelers and help settlements stay in touch with each other.”')
                                        $ at = 0
                                        $ at_activate = 0
                                        $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is strict. “You’ll find no ‘ting for you here, as we seek no travels, no {i}intouch{/i}.”"
                                        $ greenmountaintribe_firstattitude = "friendly"
                                        jump greenmountaintribefirsttime02
                                    '“Looking back at my last few days, I think I’m meant to do pretty much {i}everything{/i}.”' ( condition="at == 'playful'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Looking back at my last few days, I think I’m meant to do pretty much {i}everything{/i}.”')
                                        $ at = 0
                                        $ at_activate = 0
                                        if pc_religion == "pagan":
                                            $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is strict. “{i}I’m not sure what you mean. {color=#f6d6bd}Asterion{/color} was also speaking in riddles.{/i}”"
                                        else:
                                            $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is strict. “Your riddle tells me little, {color=#f6d6bd}Asterion{/color} was the same way.”"
                                        $ greenmountaintribe_firstattitude = "playful"
                                        jump greenmountaintribefirsttime02
                                    '“The city of {color=#f6d6bd}Hovlavan{/color} pays me for making the roads safer.”' ( condition="at == 'distanced'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “The city of {color=#f6d6bd}Hovlavan{/color} pays me for making the roads safer.”')
                                        $ at = 0
                                        $ at_activate = 0
                                        $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is harsh. “Not’ing good comes from t’ city,” she says without hesitance, “not’ing and no one.”"
                                        $ greenmountaintribe_firstattitude = "distanced"
                                        $ greenmountaintribe_reputation -= 1
                                        jump greenmountaintribefirsttime02
                                    'I show her my blade. “I’m meant to patrol {i}my{/i} roads, but that involves a lot of bloodshed.”' ( condition="at == 'intimidating'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I show her my blade. “I’m meant to patrol {i}my{/i} roads, but that involves a lot of bloodshed.”')
                                        $ at = 0
                                        $ at_activate = 0
                                        $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is strict. “You claim as yours what’s no one’s. Roads are of souls and beasts alike.”"
                                        $ greenmountaintribe_firstattitude = "intimidating"
                                        jump greenmountaintribefirsttime02
                                    '“It’s just a fancy way of calling a rider for hire. Like a messenger and an adventurer in one.”' ( condition="at == 'vulnerable'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “It’s just a fancy way of calling a rider for hire. Like a messenger and an adventurer in one.”')
                                        $ at = 0
                                        $ at_activate = 0
                                        if pc_religion == "pagan":
                                            $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is gentler. “{i}That’s what we call souls of your trade. Riders. After years of fighting on foot, I’ve got this beast now, and since spring. Maybe I’ll become a rider too, one day.{/i}”"
                                        else:
                                            $ custom2 = "You hear a monstrous roar coming from the mountains. The woman looks around, with a raised spear, and when her eyes return to you again, her voice is gentler. “‘At’s what we call souls like you. {i}Riders{/i}. I’ve this beast since spring. May be a rider too, one day.”"
                                        $ greenmountaintribe_firstattitude = "vulnerable"
                                        # $ greenmountaintribe_reputation += 1
                                        jump greenmountaintribefirsttime02

    label greenmountaintribefirsttime02:
        if pc_religion == "pagan":
            $ custom1 = "She pulls the reins and makes the saurian turn around, then leaps away, up the path, staying on top of the crags. “{i}Something’s happening not far away from here,{/i}” she shouts from a distance. “{i}Let’s not risk staying around, we’ll speak in the village.{/i}”"
        else:
            $ custom1 = "She pulls the reins and makes the saurian turn around, then leaps away, up the path, staying on top of the crags. “Some’ing’s happening ‘tere,” she shouts from a distance. “Road’s not safe, come. We’ll speak in t’ village.”"
        menu:
            '[custom2]
            \n\n[custom1]
            '
            'I tell {color=#f6d6bd}[horsename]{/color} to keep up with the beast.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell {color=#f6d6bd}%s{/color} to keep up with the beast.' %horsename)
                stop nature fadeout 4.0
                show areapicture mountainroadtogreenmountaintribe2 at basicfade
                $ renpy.music.play("audio/blackyenwhitebirch_greenmountaintribe_loop.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                menu:
                    'You ride through the corridor of rock faces, led by the jumping saurian. {color=#f6d6bd}The woman{/color} in a helmet blows a large horn, longer and thinner than a ram’s, with enough power to cause an avalanche, and once you reach the massive, wooden gate blocking the path, it’s already open. The few people you’ve seen so far are well-equipped, wearing heavy jackets, shields, and steel weapons, though some of them seem a bit old.
                    \n\nYour surroundings get more spacious, with small garden patches and stone sheds spread on both sides of the path. Riding by the onlookers, you enter a trot, then a walk. The locals pay as much attention to you as to your mount, commenting on your appearance in the Old Speech.
                    \n\nUnlike the guards, the workers are carrying rather simple tools, many of them made of bones or rocks. Their woolen, undyed outfits are appropriate for hard labor, worn and patched up, but also heavy, protecting their owners from the cold mountain winds. The one thing that differentiates them from one another is their headgear - every person you see is wearing something on their head, mostly ear-covering kerchiefs, vividly dyed, with embroidered patterns of leaves, flowers, and gems.
                    \n\nThey are seafolk, no doubt about it - they have long limbs, hardly any beards, and the few children you see have uncovered hair, wavy and dense. Yet their paleness is unusual, as if they spend little time outside.
                    \n\n{color=#f6d6bd}Your guide{/color} is nowhere in sight, but so far no one has tried to stop you.
                    '
                    'I don’t want to trample anyone. I dismount and look for {color=#f6d6bd}the saurian rider{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t want to trample anyone. I dismount and look for {color=#f6d6bd}the saurian rider{/color}.')
                        show areapicture greenmountaintribeentrance01 at basicfade
                        if pc_religion == "pagan":
                            $ custom1 = "“{i}You’re safe here, but not welcome,{/i}” you hear from {color=#f6d6bd}your guide{/color} in the Old Speech. She’s not the only guard in sight - the spears, slings, and clubs are getting a bit too numerous for your taste. “{i}We need not a rock from you, rider, you weren’t invited by us. Unless you have a gift worthy of {color=#f6d6bd}our chief’s{/color} and {color=#f6d6bd}shaman’s{/color} time, we see your visit as needless.{/i}”"
                        else:
                            $ custom1 = "“A safe place, but don’t be here for long,” you hear from {color=#f6d6bd}your guide{/color} in her lacking City Tongue, though still much better than your Old Speech. She’s not the only guard in sight - the spears, slings, and clubs are getting a bit too numerous for your tastes. “We need you not!” She looks around, but only a few people nod in agreement - most of them are giving you puzzled looks. “What’s your gift for {color=#f6d6bd}t’ chief{/color} and {color=#f6d6bd}t’ shaman{/color}?”"
                        $ greenmountaintribe_firsttime_achievement = 1
                        if not pc_firstvillage:
                            $ pc_firstvillage = "greenmountaintribe"
                        menu:
                            'She awaits you at the cave mouth, where the “teeth” and “tongue” are so distinct you doubt they were shaped so without the villagers’ interference. The crisp air carries the scent of late-summer meadows. Aside from the discussions of farmers and guards, you hear the roaming wind and the gloating ibexes, but the terraces and crops around you are quiet, making you realize it’s the first village you’ve seen in quite a while where there’s no constant noise of humming water, or of heavy labor.
                            \n\n[custom1]
                            \n\nYou realize she’s more than forty, and even if she has a small stature, no one seems eager to replace her as a negotiator, or to question her authority. The accent of those who chat in the distance is so dense you can’t catch a single word.
                            '
                            '“I need to bring your tribe a gift so I can see your leaders?”':
                                $ can_leave = 1
                                $ can_rest = 1
                                $ can_items = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to bring your tribe a gift so I can see your leaders?”')
                                $ quest_reachthepaganvillage_description08 = "If I want to see the leaders of the tribe, I need to bring them a worthy gift."
                                $ renpy.notify("Journal updated: The Hidden Village")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
                                if pc_religion == "pagan":
                                    $ custom1 = "She lets out a dishonest laugh. “{i}Or why would they want to see you? Your problems are but a pebble in a stream, and we seek no change of the current.{/i}”"
                                else:
                                    $ custom1 = "She lets out a dishonest laugh. “Why would ‘ey want to see you?” She tries to say something you can’t understand, and after a few attempts, she picks up a small rock. “Your problems,” she keeps in front of her chest, then points at the mountains above you. “Our lives.”"
                                menu:
                                    '[custom1]
                                    '
                                    'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
                                        jump greenmountaintribeentrancebarter01
                                    '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
                                        jump greenmountaintribe_about_cephasgaiane101
                                    '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
                                        jump greenmountaintribe_about_cephasgaiane201
                                    '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
                                        jump greenmountaintribeentrancaboutasterion01
                                    '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
                                        jump greenmountaintribeentrancaboutmissinghunters01
                                    'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
                                        jump greenmountaintribe_sleep01
                                    'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
                                        jump greenmountaintribeentrancegrindingrock01
                                    'I enter the cave.' if cephasgaiane_available:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
                                        jump greenmountaintribechiefregular01

label greenmountaintriberegular01:
    $ questionpreset = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[greenmountaintribe_fluff]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

    label greenmountaintribeleavingthecave01:
        $ shop = "greenmountaintribeentrance"
        $ questionpreset = 0
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        show areapicture greenmountaintribeentrance01 at basicfade
        menu:
            '{color=#f6d6bd}The saurian rider{/color} helps you leave the caves. The sunlight and the crisp air are a welcome change.
            '
            'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
                jump greenmountaintribeentrancebarter01
            '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
                jump greenmountaintribe_about_cephasgaiane101
            '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
                jump greenmountaintribe_about_cephasgaiane201
            '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
                jump greenmountaintribeentrancaboutasterion01
            '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
                jump greenmountaintribeentrancaboutmissinghunters01
            'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
                jump greenmountaintribe_sleep01
            'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
                jump greenmountaintribeentrancegrindingrock01
            'I enter the cave.' if cephasgaiane_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
                jump greenmountaintribechiefregular01

    label greenmountaintribeentranceafterinteraction01:
        hide screen selling
        $ shop = "greenmountaintribeentrance"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            '
            'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
                jump greenmountaintribeentrancebarter01
            '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
                jump greenmountaintribe_about_cephasgaiane101
            '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
                jump greenmountaintribe_about_cephasgaiane201
            '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
                jump greenmountaintribeentrancaboutasterion01
            '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
                jump greenmountaintribeentrancaboutmissinghunters01
            'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
                jump greenmountaintribe_sleep01
            'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
                jump greenmountaintribeentrancegrindingrock01
            'I enter the cave.' if cephasgaiane_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
                jump greenmountaintribechiefregular01

    label greenmountaintribeentranceafterinteraction02:
        hide screen selling
        $ shop = "greenmountaintribeentrance"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ greenmountaintribe_about_wanteditems = 1
        if pc_religion == "pagan":
            $ custom1 = "“{i}Haven’t you heard tales of the old times, when the chiefs welcomed each other with the best things they had to offer?{/i}” There’s a playful hint in her voice. “{i}Something of great value, and what’s difficult to find. A sharp blade. A cask full of golden liquid. Spices from another land.{/i}”"
            $ quest_reachthepaganvillage_description09 = "According to the guard, it could be “something of great value, and what’s difficult to find. A sharp blade. A cask full of golden liquid. Spices from another land.”"
        else:
            $ custom1 = "With a playful voice, she tries to tell you something complex, even asking her companions to help them translate it, but finally gives up. “‘Ting rare to us. A good blade. Good drink. Spices.”"
            $ quest_reachthepaganvillage_description09 = "According to the guard, it could be “‘ting rare to us. A good blade. Good drink. Spices.”"
        $ renpy.notify("Journal updated: The Hidden Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
        menu:
            '[custom1]
            '
            'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
                jump greenmountaintribeentrancebarter01
            '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
                jump greenmountaintribe_about_cephasgaiane101
            '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
                jump greenmountaintribe_about_cephasgaiane201
            '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
                jump greenmountaintribeentrancaboutasterion01
            '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
                jump greenmountaintribeentrancaboutmissinghunters01
            'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
                jump greenmountaintribe_sleep01
            'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
                jump greenmountaintribeentrancegrindingrock01
            'I enter the cave.' if cephasgaiane_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
                jump greenmountaintribechiefregular01

    label greenmountaintribeaftersleep:
        nvl clear
        $ shop = "greenmountaintribeentrance"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        stop nature fadeout 4.0
        show areapicture greenmountaintribeentrance01 at basicfade
        hide screen selling
        $ renpy.music.play("audio/blackyenwhitebirch_greenmountaintribe_loop.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
            $ renpy.notify("The days are getting shorter.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
        menu:
            'You gladly leave the shed, making sure that {color=#f6d6bd}[horsename]{/color} is safe and rested, then prepare your equipment. There’s but a few souls around, mostly the guards replacing the night shift. {color=#f6d6bd}The saurian rider{/color} is yawning. Without the helmet, she reveals her short, chestnut curls. She’s already keeping an eye on you from the cave mouth.
            '
            'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
                jump greenmountaintribeentrancebarter01
            '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
                jump greenmountaintribe_about_cephasgaiane101
            '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
                jump greenmountaintribe_about_cephasgaiane201
            '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
                jump greenmountaintribeentrancaboutasterion01
            '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
                jump greenmountaintribeentrancaboutmissinghunters01
            'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
                jump greenmountaintribe_sleep01
            'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
                jump greenmountaintribeentrancegrindingrock01
            'I enter the cave.' if cephasgaiane_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
                jump greenmountaintribechiefregular01

label greenmountaintribe_about_cephasgaiane101:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there something I could do for you instead?”')
    if pc_religion == "pagan":
        $ custom1 = "“{i}Our mountains will kill any stranger, we spend years mastering their trails and traps. Whatever comes from the woodlands will bring us nothing of value. Don’t you dare suggest we were waiting for a cityfolk to help with our troubles.{/i}”"
    else:
        $ custom1 = "“Mountains will kill you, you need years to learn ‘em. T’ ‘tings of woodlands are of no wort’ to us. Don’t dare to say {i}we{/i} need help of cityfolk.”"
    $ greenmountaintribe_about_cephasgaiane1 = 1
    menu:
        '“No,” she scoffs, but seeing your expression, continues with a serious look of her own. [custom1]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

label greenmountaintribe_about_cephasgaiane201:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news of great importance, matters of life and death.”')
    $ greenmountaintribe_about_cephasgaiane2 = 1
    if pc_religion == "pagan":
        $ custom1 = "She looks at the faces that surround you. “{i}Important to who? To a rider from a city? What does it matter to the farmers, builders, smiths, and fighters of {color=#f6d6bd}The Tribe of The Green Mountain{/color}? If we need help, we go to the lowlands on our own legs.{/i}”"
    else:
        $ custom1 = "Hesitant, she answers slowly. “Important... To a {i}radarden{/i} of cityfolk. But not to t’ souls of,” she says a few words in the Old Speech, and after your frown, tries to translate them, though with a displeased frown. “Of {color=#f6d6bd}T’ Tribe of T’ Green Mountain{/color}.”"
    menu:
        '[custom1]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

label greenmountaintribe_sleep01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point at the sky. “I’ll need to hide. Sleep.”')
    $ greenmountaintribe_sleep = 1
    $ renpy.notify("New shelter unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
    if pc_religion == "pagan":
        $ custom1 = "She looks away and speaks with her neighbors. You recognize words such as {i}shelter{/i} or {i}stranger{/i}, but when she’s not doing her best to speak slowly and clearly, it’s as if she’s using yet another language. She then gestures for you to follow her to the shed just a few steps behind you, and draws aside the curtain covering the entrance. The room is filled with sacks, old barrels, and bone-made tools. “{i}We’ll prepare you a sleeping spot, and your beast can stay outside. The village is heavily guarded at night, don’t be afraid.{/i}”\n\nSoon after, a few of the farmers bring a pile of furs, placing them in the corner. “{i}Move them to the center when you’re ready.{/i}”"
    else:
        $ custom1 = "She looks away and speaks with her neighbors, making you wait in silence. She then gestures for you to follow her to the shed just a few steps behind you, and draws aside the curtain covering the entrance. The room is filled with sacks, old barrels, and bone-made tools. “You’ll have a sleeping spot here, leave t’ beast ‘tere,” she points at the main path. “We guard t’ village, it will be safe.”\n\nSoon after, a few of the farmers bring a pile of furs, placing them in the corner. “Move ‘em ‘tere when you go to sleep,” {color=#f6d6bd}your guide{/color} points at the center of the room."
    menu:
        '[custom1]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

label greenmountaintribeentrancaboutasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find {color=#f6d6bd}Asterion{/color}.”')
    $ greenmountaintribe_about_asterion = 1
    if pc_religion == "pagan":
        $ custom1 = "She gives you a grim look. “{i}So is {color=#f6d6bd}our shaman{/color}. She had some big plans with him, but I shouldn’t talk about it with cityfolk.{/i}”"
    else:
        $ custom1 = "She gives you a grim look. “{color=#f6d6bd}Our shaman{/color} too, but I can’t talk about it.”"
    menu:
        '[custom1]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

label greenmountaintribeentrancaboutmissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”')
    $ greenmountaintribe_about_missinghunters = 1
    if pc_religion == "pagan":
        $ custom1 = "She exchanges looks with the other armored villagers to her left and right, but they shake their heads, and she meets your eyes again with a confident nod. “{i}We haven’t seen anyone from that tribe in many years.{/i}”"
    else:
        $ custom1 = "She repeats your question, then translates it to the armored villagers to her left and right. After they shake their heads, she meets your eyes again with a confident nod. “Not in years.”"
    menu:
        '[custom1]
        '
        'I show her my possessions. “Do any of these interest you?”' if not cephasgaiane_available:
            jump greenmountaintribeentrancebarter01
        '“Is there something I could do for you instead?”' if not cephasgaiane_available and not greenmountaintribe_about_cephasgaiane1:
            jump greenmountaintribe_about_cephasgaiane101
        '“I bring news of great importance, matters of life and death.”' if not cephasgaiane_available and greenmountaintribe_about_cephasgaiane1 and not greenmountaintribe_about_cephasgaiane2:
            jump greenmountaintribe_about_cephasgaiane201
        '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1 and not greenmountaintribe_about_asterion:
            jump greenmountaintribeentrancaboutasterion01
        '“I’m trying to find a few hunters from the village of {color=#f6d6bd}Creeks{/color}. Were they around?”' if quest_missinghunters == 1 and not greenmountaintribe_about_missinghunters:
            jump greenmountaintribeentrancaboutmissinghunters01
        'I point at the sky. “I’ll need to hide. Sleep.”' ( condition="not greenmountaintribe_sleep" ):
            jump greenmountaintribe_sleep01
        'I get back to {color=#f6d6bd}[horsename]{/color}. I won’t get any higher - I should powder the basalt rock here.' if not item_powderedrock and not item_blindingpowder and item_rocktobepowdered:
            jump greenmountaintribeentrancegrindingrock01
        'I enter the cave.' if cephasgaiane_available:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cave.')
            jump greenmountaintribechiefregular01

label greenmountaintribeentrancegrindingrock01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}. I won’t get any higher - I should powder the basalt rock here.' %horsename)
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if appearance_charisma < 0:
        $ quarters += 4
        menu:
            'You nod to the {color=#f6d6bd}saurian rider{/color} and step away. You follow the unclear steps of the ritual, preparing the new ingredient without fully understanding how the steps you take make any difference. While some alchemical rituals are essential, you are never sure which ones can be omitted, or altered. Will Companion, the air-like shell that carries pneuma, “see” your efforts as sufficient? You can only hope.
            \n\nYou place the piece of basalt on a larger rock, not getting in anyone’s way, then spend over an hour breaking it loudly into smaller chunks and grinding them into dust. At the beginning of the process, a few of the locals, mostly children, observe you, but they get bored quickly, leaving you to your eccentricities. Once you fill up a small sack with the black powder, your hands are tired, and a bit scratched.
            '
            'I put it with the rest of my bundles, then get back to the cave mouth.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put it with the rest of my bundles, then get back to the cave mouth.')
                $ item_rocktobepowdered = 0
                $ item_powderedrock = 1
                $ renpy.notify("You added the powdered rock to your bag of ingredients.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the powdered rock to your bag of ingredients.{/i}')
                $ custom1 = "“{i}Magic?{/i}” Says {color=#f6d6bd}your guide{/color} calmly, using one of the few words that sound almost identical in both languages, and after seeing your nod, she simply points at the bucket, letting you wash your hands."
                jump greenmountaintribeentranceafterinteraction01
    else:
        $ quarters += 1
        menu:
            'You nod to the {color=#f6d6bd}saurian rider{/color} and step away. You follow the unclear steps of the ritual, preparing the new ingredient without fully understanding how the steps you take make any difference. While some alchemical rituals are essential, you are never sure which ones can be omitted, or altered. Will Companion, the air-like shell that carries pneuma, “see” your efforts as sufficient? You can only hope.
            \n\nYou place the piece of basalt on a larger rock, not getting in anyone’s way, then spend a few minutes breaking it loudly into smaller chunks and grinding them into dust. At the beginning of the process, a few of the locals, mostly children, observe you, but after seeing your slow progress, they start to whisper, then chuckle. One of the boys gets closer, takes a grinding rock from you, and starts to show you how to use it, speaking too quickly in the Old Speech for you to recognize any of the instructions. Then the other children also find a few rocks and join these efforts, and help you finish the task.
            \n\nOnce you fill up a small sack with the black powder, your hands are tired, and a bit scratched. The children smile at each other, raising their skinny arms in a way that’s meant to show everyone how strong they are.
            '
            'I put it with the rest of my bundles, then get back to the cave mouth.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put it with the rest of my bundles, then get back to the cave mouth.')
                $ item_rocktobepowdered = 0
                $ item_powderedrock = 1
                $ renpy.notify("You added the powdered rock to your bag of ingredients.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the powdered rock to your bag of ingredients.{/i}')
                $ custom1 = "“{i}Magic?{/i}” Says {color=#f6d6bd}your guide{/color} calmly, using one of the few words that sound almost identical in both languages, and after seeing your nod, she simply points at the bucket, letting you wash your hands."
                jump greenmountaintribeentranceafterinteraction01

label greenmountaintribeentrancebarter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her my possessions. “Do any of these interest you?”')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ thingstosell = 0
    if item_axe02alt or item_axehead or item_axeset:
        $ thingstosell += 1
    if item_axe03:
        $ thingstosell += 1
    if item_cidercask:
        $ thingstosell += 1
    if item_ironingot:
        $ thingstosell += 1
    if item_sealskin:
        $ thingstosell += 1
    if item_cidercask:
        $ thingstosell += 1
    if item_beholderroot:
        $ thingstosell += 1
    if item_spices:
        $ thingstosell += 1
    if not tutorial_selling:
        $ tutorial_selling = 1
    if thingstosell:
        if not tutorial_selling2:
            $ tutorial_selling2 = 1
    if thingstosell:
        $ shop = "greenmountaintribeentrance"
        show screen selling()
        if thingstosell == 1:
            $ custom1 = "She points at the only thing that her tribe could use."
        else:
            $ custom1 = "She finds a few things that her tribe could use, and puts them on an unfolded blanket."
        menu:
            '[custom1] Her neighbors gather around, light-heartedly commenting on the things you carried onto the mountain.
            '
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She shrugs and lets you pack your bundles."
                jump greenmountaintribeentranceafterinteraction01
    else:
        menu:
            'You pull out some items, but she spares them nothing more than a shrug.
            '
            '“What would you want, then?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you want, then?”')
                jump greenmountaintribeentranceafterinteraction02
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01
            '“Fine.”' if greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.”')
                $ custom1 = "She waits for you to pack your bundles."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingsealskin:
        if pc_religion == "pagan":
            $ custom1 = "Her voice gets nostalgic when she lifts the hide. “{i}In our tales, almost no one wears the pelt of an elk, or a bear, or a wolf. Seals were easier to catch, and outside of the woods’ shadows. We would be grateful to hang it on a wall.{/i}”"
        else:
            $ custom1 = "Her voice gets nostalgic when she lifts the hide, talking with her excited neighbors. “We used to wear sealskin, not elks or wolves. We can hang it on a wall.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the sealskin.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the sealskin.{/i}')
                $ item_sealskin = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingbeholderroot:
        if pc_religion == "pagan":
            $ custom1 = "The mysterious jar sparks great interest among the locals, especially once the root you take out twitches on its own. “{i}From {color=#f6d6bd}Howler’s{/color},{/i}” states one of them, and {color=#f6d6bd}the saurian rider{/color} nods. “{i}It may hold dark powers, but maybe {color=#f6d6bd}our shaman{/color} will understand how to protect ourselves from them.{/i}”"
        else:
            $ custom1 = "The mysterious jar sparks great interest among the locals, especially once the root you take out twitches on its own. You recognize that one of them mentions {color=#f6d6bd}Howler’s{/color}, but after the long conversation, all {color=#f6d6bd}the saurian rider{/color} has to say is “for {color=#f6d6bd}our shaman{/color}.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the weird root.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the weird root.{/i}')
                $ item_beholderroot = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingaxe02:
        if pc_religion == "pagan":
            $ custom1 = "The saurian rider doesn’t pay much attention to the bronze blade, but one of the other guards is insistent she should accept it. “{i}I guess it will last centuries,{/i}” she admits carefully. “{i}Very well. We can accept it.{/i}”"
        else:
            $ custom1 = "The saurian rider doesn’t pay much attention to the bronze blade, but one of the other guards keeps arguing with her, until she caves in. “He wants it a lot,” she explains, “and it may last... It’s enough.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the bronze axe.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the bronze axe.{/i}')
                $ item_axe02alt = 0
                $ item_axehead = 0
                $ item_axeset = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingaxe03:
        if pc_religion == "pagan":
            $ custom1 = "The saurian rider takes a closer look at the fine blade you bought in {color=#f6d6bd}Howler’s Dell{/color}, and gives it a good swing. A few of her companions argue she should accept it, and she caves in quickly. “{i}A treasure of a blade,{/i}” she admits. “{i}We can accept it.{/i}”"
        else:
            $ custom1 = "The saurian rider takes a closer look at the fine blade you bought in {color=#f6d6bd}Howler’s Dell{/color}, and gives it a good swing. A few of her companions argue with her about something, and when she speaks, you hear jealousy. “Great blade,” she admits. “We’ll take it.”"
        menu:
            '[custom1]
            '
            '“Very well.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                $ renpy.notify("You gave away the battle axe.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the battle axe.{/i}')
                $ item_axe03 = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingcidercask:
        if pc_religion == "pagan":
            $ custom1 = "You explain what the cask’s contents are, warning it won’t stay fresh for long, though you don’t know how to say {i}cider{/i} in the Old Speech, so you instead call it a {i}sweet apple beer{/i}, pointing at the tree behind you. A few of the locals are greatly interested in taking a whiff, but you explain it’s not possible. “{i}We rarely make hard drinks in the mountains,{/i}” admits {color=#f6d6bd}the saurian rider{/color}. “{i}We can agree to such a gift.{/i}”"
        else:
            $ custom1 = "You try to explain what the cask’s contents are, but since the word {i}cider{/i} seems to mean nothing to the locals, you call it a {i}sweet apple beer{/i}, pointing at the tree behind you. A few of the locals are greatly interested in taking a whiff, but you try to explain that it’s not possible, since it may spoil soon. After a short debate, {color=#f6d6bd}the saurian rider{/color} admits that “we drink water and milk, not beers. ‘Tis gift is fine.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the cider cask.")
                if quest_foggy3whitemarshes == 1:
                    $ quest_foggy3whitemarshes_description07 = "I sold the cask outside of {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Foggy{/color} won’t learn about it."
                    $ renpy.notify("Journal updated: Cask of Cider\nYou gave away the cask of cider.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider. You gave away the cask of cider.{/i}')
                else:
                    $ renpy.notify("You gave away the cask of cider.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the cask of cider.{/i}')
                $ item_cidercask = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingironingot:
        if pc_religion == "pagan":
            $ custom1 = "Seeing how the locals have more bronze and steel weapons and helmets than people in most villages, it’s not surprising that they pay little attention to the crude iron. Still, a few of them try to convince {color=#f6d6bd}the saurian rider{/color} that even such a small supply would be useful for the upcoming winter, and finally she nods to you.”"
        else:
            $ custom1 = "Seeing how the locals have more bronze and steel weapons and helmets than people in most villages, it’s not surprising that they pay little attention to the crude iron. Still, a few of them start to talk at length with {color=#f6d6bd}the saurian rider{/color}, and finally she nods to you.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the iron ingot.")
                $ item_ironingot = 0
                $ item_ironingot_sold_greenmountain = 1
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingspices:
        if pc_religion == "pagan":
            $ custom1 = "The locals pick up the sacks and smell their contents. An enthusiastic whisper runs among them, and {color=#f6d6bd}the saurian rider{/color} speaks with a smile, affectionately patting the bag. “{i}We have plenty of herbs, but only a few of their type grow in our mountains. Having unique spices to grind would be a great gift for us.{/i}”"
        else:
            $ custom1 = "The locals pick up the sacks and smell their contents. An enthusiastic whisper runs among them, and {color=#f6d6bd}the saurian rider{/color} speaks with a smile, affectionately patting the bag. “Our herbs are boring, even if ‘tere are plenty. A great gift for our tribe.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away the sacks of spices.")
                $ item_spices = 0
                $ greenmountaintribe_reputation += 2
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

    label greenmountaintribeentrancesellingasterionscloak:
        if pc_religion == "pagan":
            $ custom1 = "Met with disbelief, you describe the cloak’s powers, and after {color=#f6d6bd}the saurian rider{/color} covers wraps herself up in it, there’s a gleam in her eyes. “{i}We’ll give it to our elders to embrace them during the nights, our night watch on the walls, our climbers to protect them from the cave winds.{/i}”"
        else:
            $ custom1 = "Describing the way the cloak works turns out to be difficult, so you let {color=#f6d6bd}the saurian rider{/color} try it, even encouraging her to lie down on the ground. She gives you a surprised look, the word {i}pneuma{/i} is repeated by her tribesfolk. There’s a gleam in her eyes. “Good for elders, for climbers. A great gift.”"
        menu:
            '[custom1]
            '
            '“Very well, take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well, take it.”')
                $ renpy.notify("You gave away Asterion’s cloak.")
                $ item_asterioncloak = 0
                $ greenmountaintribe_reputation += 2
                jump greenmountaintribeentrancebarter02
            '“What else would interest you?”' if not greenmountaintribe_about_wanteditems:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else would interest you?”')
                jump greenmountaintribeentranceafterinteraction02
            '“I can’t agree to that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t agree to that.”')
                $ custom1 = "She walks back to the entrance."
                jump greenmountaintribeentranceafterinteraction01

label greenmountaintribeentrancebarter02:
    hide screen selling
    $ cephasgaiane_available = 1
    if pc_religion == "pagan":
        $ custom1 = "She gives you a few minutes to pack up your belongings. “{i}Your beast will be safe here,{/i}” she says confidently. “{i}We have enough meat, hides, and muscles, we won’t rob you. Let it graze.{/i}”"
    else:
        $ custom1 = "She gives you a few minutes to pack up your belongings. “Let your beast stay on t’ grass,” she pats its side. “It’s safe here.”"
    menu:
        '[custom1]
        \n\nAfter you tether {color=#f6d6bd}[horsename]{/color} to a tree, keeping it away from most garden patches, you head to the cave mouth. The corridor goes down, getting darker after only a few steps, but seeing how often the locals go through it without any source of light, you doubt there’s going to be many treacherous steps ahead of you.
        \n\nStill, {color=#f6d6bd}your guide{/color} leaves the shed with a lantern made of old brass, with windows engraved with winged dragons circling around an erupting volcano.
        '
        'I grab my own crude lantern.' if item_lantern:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own crude lantern.')
            jump greenmountaintribeentrancebarter02a
        'I stay close to her, depending on her source of light.' if not item_lantern:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay close to her, depending on her source of light.')
            label greenmountaintribeentrancebarter02a:
                $ quarters += 1
                show areapicture monasteryinside00 at basicfade
                menu:
                    'The “tongue” sticking out of the entrance doesn’t go on for long. For some time, you descend gently, then encounter a set of spiral stairs. Once you reach the bottom, you find yourself in a labyrinth of tunnels and chambers, some of them sunk in darkness, others lit by campfires, with smoke leaving through holes in the ceilings. Spread among them are dozens of children and elders, but also workbenches and other spots worked by adults, some of them too busy to even spare you a look. There are woodworkers, water carriers, potters, flour millers, cooks - you hardly notice how stuffy the air is down here.
                    \n\nSeeing the consistently spacious corridors, conveniently wide enough for even an obese shell to squeeze through them, you can’t tell how many, if any, of these passages were not made by human hands. The entire walk takes you only a few minutes, but the sheer amount of rooms you walk by makes you lose your way many times before you reach a short path leading to a bright, warm chamber, to which {color=#f6d6bd}the saurian rider{/color} invites you with a gesture.
                    \n\nYou smell smoke and humidity, and as you listen, the humming of a stream reaches you from below. Much louder are the cries of an infant, amplified by an echo.
                    '
                    'I put away my lantern and enter the chamber.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put away my lantern and enter the chamber.')
                        jump greenmountaintribechieffirsttime01

label greenmountaintribefirsttime01BAN:
    $ greenmountaintribe_banned = 1
    if quest_reachthepaganvillage == 1:
        if quest_sleepinggiant == 1:
            $ quest_sleepinggiant = 3
            $ renpy.notify("Quests completed: The Hidden Village,\nThe Sleeping Giant")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Hidden Village, The Sleeping Giant{/i}')
        else:
            $ renpy.notify("Quest completed: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Hidden Village{/i}')
    elif quest_sleepinggiant == 1:
        $ quest_sleepinggiant = 3
        $ renpy.notify("Quests completed: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Sleeping Giant{/i}')
    $ quest_reachthepaganvillage = 3
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 0
    menu:
        'You hear a loud sound of a horn, and as you look ahead, you see a massive saurian standing on four limbs on the top of a crag. It’s displaying proudly its dark-green skin, with a bit brighter stomach, and orange stripes on its legs and eyebrows, as well as the tail, which is swinging left and right.
        \n\nThe size of the monster makes you stop, and you’re lucky to do so - maybe two short breaths later, it lands on the path before you, and only then do you realize there’s {color=#f6d6bd}a short woman{/color} sitting on its back, dressed in a red gambeson and an iron helmet, with green pants that blend in with her mount. With one hand, she holds the reins, attached to a “bridle” put on the monster’s head, while the other holds a raised spear, ready to strike.
        \n\n“‘Tis not a place for your dirty soul,” she solemnly announces, scowling at you. “Our friends warned us you broke our laws, pillaged our homeland.” After a pause, she shouts. “Get out, or die.”
        \n\nSeeing your hesitation, she makes the green saurian steps forward, towering over you.
        '
        'I need to get out of this mountain. (disabled)':
            pass

label greenmountaintriberegular01BAN:
    $ greenmountaintribe_banned = 1
    if quest_reachthepaganvillage == 1:
        if quest_sleepinggiant == 1:
            $ quest_sleepinggiant = 3
            $ renpy.notify("Quests completed: The Hidden Village,\nThe Sleeping Giant")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Hidden Village, The Sleeping Giant{/i}')
        else:
            $ renpy.notify("Quest completed: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Hidden Village{/i}')
    elif quest_sleepinggiant == 1:
        $ quest_sleepinggiant = 3
        $ renpy.notify("Quests completed: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Sleeping Giant{/i}')
    $ quest_reachthepaganvillage = 3
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 0
    if pc_religion == "pagan":
        $ custom1 = "She uses the City Tongue, as if you’re unworthy of the bond that the Old Speech opened to you before. "
    else:
        $ custom1 = ""
    menu:
        'Before you reach the gates of the village, you hear the sound of a horn, a bit different from the one you’d heard upon your first arrival. Soon after, the fully equipped {color=#f6d6bd}saurian rider{/color} lands in the middle of the road, making {color=#f6d6bd}[horsename]{/color} stop.
        \n\n“‘Tis not a place for your dirty soul,” she solemnly announces, scowling at you. [custom1]“Our friends warned ‘at you pillaged our homeland.” After a pause, she shouts. “Get out, or die.”
        \n\nSeeing your hesitation, she makes the green saurian leap forward, and raises her spear. Your mount tries to make a turn.
        '
        'I need to get out of this mountain. (disabled)':
            pass
