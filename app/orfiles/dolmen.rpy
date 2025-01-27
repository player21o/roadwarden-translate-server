###################### Dolmen
default dolmen_firsttime = 0
default dolmen_inside_firsttime = 0
default dolmen_underground_firsttime = 0

default dolmen_fluff = ""
default dolmen_fluff_old = ""
default dolmen_horsename_fluff = ""
default dolmen_horsename_fluff_old = ""

default dolmen_inside_burntlog = 0
default dolmen_inside_soot = 0
default dolmen_inside_writing = 0
default dolmen_inside_campfire = 0

default dolmen_inside_trapdoor = 0
default dolmen_inside_trapdoor_0hp = 0

default dolmen_inside_trapdoor_open = 0
default dolmen_inside_trapdoor_open_axe = 0
default dolmen_inside_trapdoor_open_key = 0

default dolmen_underground_chest = 0

default dolmen_hourglass = 0
default dolmen_hourglass_blood = 0
default dolmen_hourglass_scratches = 0

default dolmen_inside_lantern = 0
default dolmen_inside_lighspell = 0
default dolmen_inside_candle1 = 0
default dolmen_inside_candle2 = 0

label dolmen01:
    $ renpy.music.play("audio/track_05dolmen.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    play nature "audio/ambient/dolmen01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if dolmen_hourglass_blood:
        show areapicture dolmenCLOSEDblood at basicfade
    elif dolmen_hourglass_scratches:
        show areapicture dolmenCLOSEDscratches at basicfade
    else:
        show areapicture dolmenCLOSEDclean at basicfade
    label dolmen_fluffloop:
        $ dolmen_fluff = ""
        $ dolmen_fluff = renpy.random.choice(['A couple of small, yellow birds fly off the roof, screeching with frustration.', 'A pleasant aroma of herbs reaches you from the bushes.', 'A small badger runs away from the entrance and disappears in the bushes.', 'A gentle breeze is stirring the leaves loudly, making you seek possible threats that could camouflage their movements.', 'A multitude of bees and butterflies are flying among the bushes, looking for flowers and filling the area with an unsettling buzz.'])
        if dolmen_fluff_old == dolmen_fluff:
            jump dolmen_fluffloop
        else:
            $ dolmen_fluff_old = dolmen_fluff
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not dolmen_firsttime:
        if day <= 5:
            $ dolmenroad_counter = day+5
        else:
            $ dolmenroad_counter = day+3
        $ world_known_areas += 1
        $ fallentree_unlocked = 1
        $ dolmen_firsttime = 1
        jump dolmenfirsttime01
    else:
        jump dolmenregular01

label dolmenfirsttime01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if stonebridge_firsttime:
        $ stonebridge_likedolmen = ", not unlike the bridge you saw in the northeast,"
    menu:
        'A couple of stone slabs[stonebridge_likedolmen] were turned into a hut-like shape, one of the ancient chapels raised by the priests of The United Church in the days of few soldiers and even fewer shelters. The dolmens proved to be especially durable, though the conditions they offered were harsh.
        \n\nThe entrance is barely wide enough to let you walk inside. It was meant to keep larger beasts away, including your palfrey. You can’t spend the night here.
        \n\nYou dismount and look around.
        '
        'There’s nothing else for me to do here. (disabled)' if dolmen_underground_chest and dolmen_hourglass:
            pass
        'I enter the chapel.' if not dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the chapel.')
            jump dolmeninside
        'I approach the hourglass carved into stone.' if not dolmen_hourglass:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the hourglass carved in the outer wall.')
            jump dolmenhourglass01

label dolmenregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[dolmen_fluff]
        '
        'There’s nothing else for me to do here. (disabled)' if dolmen_underground_chest and dolmen_hourglass:
            pass
        'I enter the chapel.' if not dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the chapel.')
            jump dolmeninside
        'I approach the hourglass carved in the outer wall.' if not dolmen_hourglass:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the hourglass carved in the outer wall.')
            jump dolmenhourglass01

label dolmenhourglassALL:
    label dolmenhourglass01:
        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
            $ pc_faithpoints_opportunities += 1
        $ dolmen_hourglass += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'It’s the most common religious sign of the cityfolk, adapted by The United Church, Orders of Truth, and the majority of fellowships. It’s used in temples and during the funeral rites, but also to decorate codices or jewelery.
            \n\nThe winged hourglasses portray the ephemerality of life and the rigidity of time. When possible, they’re made of steel, signifying the strength of humankind’s determination and innovation.
            '
            'As a member of The United Church, it’s my duty to touch the hourglass and pray.' if pc_religion == "theunitedchurch":
                $ pc_faithpoints += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- As a member of The United Church, it’s my duty to touch the hourglass and pray.')
                jump dolmenhourglassunitedchurch
            'No point in praying when not a soul sees me.' if pc_religion == "theunitedchurch":
                $ pc_faithpoints -= 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No point in praying when not a soul sees me.')
                jump dolmenafterinteraction01
            'In the old days, it was a place of faith. I should touch the hourglass and pray.' if pc_religion == "unknown" or pc_religion == "fellowship":
                $ pc_faithpoints += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In the old days, it was a place of faith. I should touch the hourglass and pray.')
                jump dolmenhourglassfreechurch
            'I step away. The real believers don’t need special places to pray.' if pc_religion == "unknown" or pc_religion == "fellowship":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away. The real believers don’t need special places to pray.')
                $ pc_faithpoints_opportunities -= 1
                jump dolmenafterinteraction01
            'As a member of an Order of Truth, I should bow before the hourglass to honor the brave builders of the past.' if pc_religion == "ordersoftruth":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- As a member of an Order of Truth, I should bow before the hourglass to honor the brave builders of the past.')
                $ pc_faithpoints += 1
                jump dolmenhourglasschurchoftruth
            'It’s but a sign trying to {i}protect{/i} an obsolete building. I step away.' if pc_religion == "ordersoftruth":
                $ pc_faithpoints -= 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s but a sign trying to {i}protect{/i} an obsolete building. I step away.')
                jump dolmenafterinteraction01
            'I feel disgusted seeing this cursed symbol. I should defile it.' if pc_religion == "pagan" or pc_religion == "unknown":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I feel disgusted seeing this cursed symbol. I should defile it.')
                jump dolmenhourglasspagan01
            'I don’t want the locals to get upset at me for destroying their sacred signs. I step away.' if pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t want the locals to get upset at me for destroying their sacred signs. I step away.')
                $ pc_faithpoints -= 1
                jump dolmenafterinteraction01
            'I’m not a pious soul. As I’m standing in front of the hourglass, I feel nothing.' if pc_religion == "none" or pc_religion == "unknown":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not a pious soul. As I’m standing in front of the hourglass, I feel nothing.')
                jump dolmenafterinteraction01

    label dolmenhourglassunitedchurch:
        $ quarters += 1
        menu:
            'The stone welcomes your open palm coldly. The hourglass doesn’t start to shine, the birds don’t cease their singing, there’s no incense inviting you into the chapel.
            \n\nYet once you close your eyes, gather your thoughts, and rub the sacred sign with your fingers, your soul is focused and tranquil, as if awakened after a long rest.
            \n\nYour prayer is built from phrases that you’ve heard repeated dozens of times by the priests, but some words come straight from your heart. When you ask for Wright’s guidance, you feel invigorated. “So be it,” you conclude, as tradition has taught you.
            '
            'After my prayer, I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After my prayer, I step away.')
                jump dolmenafterinteraction01

    label dolmenhourglassfreechurch:
        $ quarters += 1
        menu:
            'The stone welcomes your open palm coldly. The hourglass doesn’t start to shine, the birds don’t cease their singing, there’s no incense inviting you into the chapel. Yet once you close your eyes, gather your thoughts, and rub the sacred sign with your fingers, your soul is focused and tranquil, as if awakened after a long rest.
            \n\nIn your silent prayer, nature seems both distant and familiar. It doesn’t shape itself around your thoughts, but you feel like nothing is going to hurt you, not while you’re here. “So be it,” you say at the end of your prayer, as your ancestors have taught you. The birds are singing delightfully.
            '
            'After my prayer, I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After my prayer, I step away.')
                jump dolmenafterinteraction01

    label dolmenhourglasschurchoftruth:
        $ quarters += 1
        menu:
            'You stay in front of the symbol, lowering your head and gathering your thoughts. You try to imagine the struggles of the valiant builders who put their time, sweat, and blood into gathering, shaping, and transporting these huge rocks. They were led by a vision, one that requires artistry, planning, the sense of shared purpose. They did it for the sake of the future generations and even if their names are forgotten, they saved many lives. The Orders teach to be thankful for such sacrifices.
            \n\nIn your silent prayer, nature seems both distant and complimentary. It doesn’t shape itself around your thoughts, but you feel like nothing is going to hurt you, not while you’re here. For a while, you balance between chaos and order. “So be it,” you say at the end of your prayer, as the tradition has taught you. The birds are singing delightfully.
            '
            'After my prayer, I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After my prayer, I step away.')
                jump dolmenafterinteraction01

    label dolmenhourglasspagan01:
        $ can_items = 1
        menu:
            'The sign brings back the torment of your ancestors. The days of death, rejection, and enslavement. It’s not a testimony of verity or piety, but rather of control and ownership. “This is our land,” it tells you. “You do not belong here.”
            \n\nAs you stare at the image, the fire inside you grows.
            '
            'I sacrifice my blood to cast a curse.' ( condition="pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sacrifice my blood to cast a curse')
                $ can_items = 0
                jump dolmenhourglasspagan01a
            'I’m too weak to sacrifice my blood for a curse. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                pass
            'I grab a rock and spend some time to cover the hourglass with scratches.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab a rock and spend some time to cover the hourglass with scratches.')
                $ quarters += 2
                $ can_items = 0
                jump dolmenhourglasspagan01b
            'I take a bite of bread, chew it for a bit, spit it out, and glue it to the symbol. It’s something my ancestors were using as an insult.' ( condition="item_rations > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a bite of bread, chew it for a bit, spit it out, and glue it to the symbol. It’s something my ancestors were using as an insult.')
                $ minutes += 5
                $ can_items = 0
                jump dolmenhourglasspagan01c
            'I don’t have any food left to use as a curse. (disabled)' ( condition="not item_rations" ):
                pass
            'I’m not as pitiful as our oppressors. I ignore the hourglass and step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not as pitiful as our oppressors. I ignore the hourglass and step away.')
                jump dolmenafterinteraction01

    label dolmenhourglasspagan01a:
        $ pc_hp = limit_pc_hp(pc_hp-1)
        show minus1hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
        $ minutes += 5
        $ pc_faithpoints += 2
        $ at = 0
        $ dolmen_hourglass_blood = 1
        show areapicture dolmenCLOSEDblood at basicfade
        menu:
            'You cut the palm of your hand with your knife, and spread the red liquid with your fingers.
            \n\nYou breathe slowly and feel a peaceful cloud filling your head. Will flies lay eggs in your blood? Is rain going to clear the stone in a day or two? Will goblins lick it clean? None of these outcomes matter. A mischievous satisfaction brings a smile to your face.
            '
            'I wash my wound and cover it with a cloth.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my wound and cover it with a cloth.')
                jump dolmenafterinteraction01

    label dolmenhourglasspagan01b:
        show areapicture dolmenCLOSEDscratches at basicfade
        $ dolmen_hourglass_scratches = 1
        $ pc_faithpoints += 1
        menu:
            'Making a decent tool out of a rock would take a couple of hours, but you don’t have to make cuts as deep as the original engraving. You spend maybe half an hour doing your best to profane the hourglass, but the outcome is humble. At least it will be clear to anyone who sees it that it was an intentional effort. You feel as if you’ve fixed something, made it right.
            '
            'I throw the rock away and step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw the rock away and step away.')
                jump dolmenafterinteraction01

    label dolmenhourglasspagan01c:
        menu:
            'It’s something one does to offend another person without words. The chewed scrap of food, theatrically spit out, means {i}I don’t need it, yet you’re not worth it{/i}.
            \n\nYour bread and saliva stick to the sacred symbol. You know it’s going to disappear soon, but the sight is somewhat satisfying.
            '
            'I observe it for just a moment.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe it for just a moment.')
                jump dolmenafterinteraction01

label dolmeninside:
    if dolmen_hourglass_blood:
        show areapicture dolmenOPENblood behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    elif dolmen_hourglass_scratches:
        show areapicture dolmenOPENscratches behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    else:
        show areapicture dolmenOPENclean behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    if dolmen_inside_trapdoor_open:
        show dolmentrapdoor 02 at basicfade
    elif dolmen_inside_trapdoor:
        show dolmentrapdoor 01 at basicfade
    if dolmen_inside_burntlog and not dolmen_inside_trapdoor:
        show dolmenburntlog at basicfade
    if dolmen_inside_campfire and not dolmen_inside_trapdoor:
        show dolmencampfire at basicfade
    if dolmen_inside_soot:
        show dolmensoot behind dolmentrapdoor at basicfade
    if dolmen_inside_writing:
        show dolmenwriting behind dolmentrapdoor at basicfade
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if not dolmen_inside_firsttime:
        if quest_easternpath == 1:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description10 = "I took a look at the dolmen in the south. It’s safe."
        $ dolmen_inside_firsttime = 1
        $ custom1 = "The beams of light get through the gaps between the rocks, but you can hardly see anything. A torch would fill the place with smoke, but a candle will suffice.\n\nYou wonder how many travelers have sat on the cold rock, observing the entrance and fighting with their heavy eyelids."
    else:
        $ custom1 = "The chapel is empty of life."
    label dolmeninside_after_candle1:
        if (pc_class == "mage" and not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and not dolmen_inside_burntlog) or (pc_class == "mage" and not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and not dolmen_inside_soot):
            $ at_unlock_spell = 1
            $ manacost = 1
        else:
            $ at_unlock_spell = 0
        menu:
            '[custom1]
            '
            'I look around.' if not dolmen_inside_trapdoor:
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("What are you looking for, or paying attention to? (example: door)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                $ tutorial_input = 2
                $ at_unlock_spell = 0
                jump searchdolmen
            'I prepare my wooden lantern.' if (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and item_lantern and not dolmen_inside_burntlog) or (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and item_lantern and not dolmen_inside_soot):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my wooden lantern.')
                $ dolmen_inside_lantern = 1
                $ dolmen_inside_burntlog = 1
                show dolmenburntlog at basicfade
                $ dolmen_inside_soot = 1
                show dolmensoot behind dolmentrapdoor at basicfade
                $ at_unlock_spell = 0
                $ minutes += 5
                menu:
                    'The strong light lets you take a quick look inside. Even though a part of the ground is covered with a single, massive slab, there are sections free of any flooring. You see soil, small rocks, sand. In one spot you find the remains of charred wood.
                    \n\nAlso, you notice sticky soot on the walls. Parts of it cover black marks and pictures, possibly letters.
                    '
                    'I look around.' if not dolmen_inside_trapdoor:
                        if not tutorial_input:
                            $ tutorial_input = 1
                        python:
                            search = renpy.input("What are you looking for, or paying attention to? (example: door)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        $ tutorial_input = 2
                        jump searchdolmen
                    'I approach the trapdoor.' if dolmen_inside_trapdoor: # ropehook
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the trapdoor.')
                        jump dolmentrapdoor
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump dolmenafterinteraction01
            'I use my pearl amulet to look around the room. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my pearl amulet to look around the room.')
                $ dolmen_inside_lighspell = 1
                $ dolmen_inside_burntlog = 1
                show dolmenburntlog at basicfade
                $ dolmen_inside_soot = 1
                show dolmensoot behind dolmentrapdoor at basicfade
                $ at_unlock_spell = 0
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ minutes += 5
                menu:
                    'After a few deep breaths, you raise it to your forehead, coating the ancient structure with pneuma. Even though a part of the ground is covered with a single, massive slab, there are sections free of any flooring. You see soil, small rocks, sand. In one spot you find the remains of charred wood.
                    \n\nAlso, you notice sticky soot on the walls. Parts of it cover black marks and pictures, possibly letters.
                    '
                    'I look around.' if not dolmen_inside_trapdoor:
                        if not tutorial_input:
                            $ tutorial_input = 1
                        python:
                            search = renpy.input("What are you looking for, or paying attention to? (example: door)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        $ tutorial_input = 2
                        jump searchdolmen
                    'I approach the trapdoor.' if dolmen_inside_trapdoor: # ropehook
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the trapdoor.')
                        jump dolmentrapdoor
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump dolmenafterinteraction01
            'I lack pneuma to use my wooden spheres. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana" ):
                pass
            'I light up a candle.' if (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and not dolmen_inside_candle1 and not dolmen_inside_burntlog) or (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and not dolmen_inside_candle1 and not dolmen_inside_soot):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my wooden lantern.')
                $ dolmen_inside_candle1 = 1
                $ at_unlock_spell = 0
                $ minutes += 5
                $ custom1 = "You unpack the tinderbox from your saddles, then place the flint and the linen char cloth on the narrow slab sticking out to the right of the entrance. Decades ago, before The Southern Invasion, people used fire strikers made of thick steel, but all you have left is a cube-like piece of harsh pyrite. It’s not the best, but enough to make a couple of sparks.\n\nSadly, the weak light is hardly enough to let you examine the chamber."
                jump dolmeninside_after_candle1
            '{image=d6} The candle light may be weak, but I’m patient. I look for clues carefully.' if (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and not dolmen_inside_candle2 and dolmen_inside_candle1 and not dolmen_inside_burntlog) or (not dolmen_inside_trapdoor and not dolmen_inside_lantern and not dolmen_inside_lighspell and dolmen_inside_candle1 and not dolmen_inside_candle2 and not dolmen_inside_soot):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} The candle may be weak, but I’m patient. I look for clues carefully.')
                $ dolmen_inside_candle2 = 1
                $ dolmen_inside_burntlog = 1
                show dolmenburntlog at basicfade
                $ dolmen_inside_soot = 1
                show dolmensoot behind dolmentrapdoor at basicfade
                $ at_unlock_spell = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 3)
                $ quarters += (1+d100roll)
                menu:
                    'You touch your surroundings, bringing the candle closer whenever something catches your attention. Even though a part of the ground is covered with a single, massive slab, there are sections free of any flooring. You see soil, small rocks, sand. In one spot you find the remains of charred wood.
                    \n\nAlso, you notice sticky soot on the walls. Parts of it cover black marks and pictures, possibly letters.
                    '
                    'I look around.' if not dolmen_inside_trapdoor:
                        if not tutorial_input:
                            $ tutorial_input = 1
                        python:
                            search = renpy.input("What are you looking for, or paying attention to? (example: door)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        $ tutorial_input = 2
                        jump searchdolmen
                    'I approach the trapdoor.' if dolmen_inside_trapdoor: # ropehook
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the trapdoor.')
                        jump dolmentrapdoor
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump dolmenafterinteraction01
            'I approach the trapdoor.' if dolmen_inside_trapdoor: # ropehook
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the trapdoor.')
                $ at_unlock_spell = 0
                jump dolmentrapdoor
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                $ at_unlock_spell = 0
                jump dolmenafterinteraction01

label dolmenafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    hide dolmenburntlog
    hide dolmencampfire
    hide dolmensoot
    hide dolmenwriting
    hide dolmentrapdoor
    if dolmen_hourglass_blood:
        show areapicture dolmenCLOSEDblood at basicfade
    elif dolmen_hourglass_scratches:
        show areapicture dolmenCLOSEDscratches at basicfade
    else:
        show areapicture dolmenCLOSEDclean at basicfade
    label dolmen_horsename_fluffloop:
        $ dolmen_horsename_fluff = ""
        $ dolmen_horsename_fluff = renpy.random.choice(['is playfully poking the nearby bushes with its nose, ready for the further journey.', 'is looking for the next clump of grass to graze upon.', 'is leaning against the wall, napping.', 'is observing the area.', 'is listening to the leaves carefully.'])
        if dolmen_horsename_fluff_old == dolmen_horsename_fluff:
            jump dolmen_horsename_fluffloop
        else:
            $ dolmen_horsename_fluff_old = dolmen_horsename_fluff
    menu:
        '{color=#f6d6bd}[horsename]{/color} [dolmen_horsename_fluff]
        '
        'There’s nothing else for me to do here. (disabled)' if dolmen_underground_chest and dolmen_hourglass:
            pass
        'I enter the chapel.' if not dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the chapel.')
            jump dolmeninside
        'I approach the hourglass carved in the outer wall.' if not dolmen_hourglass:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the hourglass carved in the outer wall.')
            jump dolmenhourglass01

#################SEARCH
label searchdolmen:
    #EASTER EGGS
    if search == "nothing" or search == "none" or search == "something" or search == "anything" or search == "whatever" or search == " " or search == "":
        menu:
            'And you find nothing.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "love" or search == "meaning" or search == "meaningoflife" or search == "purpose" or search == "happiness" or search == "god" or search == "girlfriend" or search == "boyfriend" or search == "bhaalspawn":
        menu:
            'Not the right place to look for it.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "fuck" or search == "sex" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag":
        menu:
            'Grow up.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "pokemon":
        menu:
            '...no.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "panda" or search == "pandas":
        menu:
            'I wish. Maybe in another life.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    #IMPORTANT SEARCHES THAT DO NOTHING
    elif search == "light" or search == "sun" or search == "sunlight":
        menu:
            'The beams of light get through the gaps between the rocks, but you can hardly see anything.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "air" or search == "wind" or search == "draft":
        menu:
            'The walls protect you from the wind and you don’t notice any unusual drafts. The air is a bit humid and after taking a couple of deep breaths, the faint scent of urine wafts closer.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "smell" or search == "scent" or search == "urine":
        menu:
            'You notice the faint scent of urine and animal fur.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "button" or search == "buttons":
        menu:
            'There are no obvious buttons around.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "hole" or search == "holes":
        menu:
            'You try to make a hole somewhere in the ground, but with no luck.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "dirt":
        menu:
            'It’s in every corner.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "wall" or search == "walls":
        menu:
            'They are all around you.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "prints" or search == "track" or search == "tracks" or search == "footprint" or search == "bootprint" or search == "footprints" or search == "bootprints" or search == "shoeprint" or search == "shoeprints" or search == "feetprint" or search == "boot" or search == "foot" or search == "print" or search == "trail" or search == "trace" or search == "paws" or search == "paw" or search == "pawprints" or search == "pawmarks":
        menu:
            'There are sparse marks left by raccoons and birds, but you recognize no unusual pattern in them.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "hiddendoor" or search == "hiddencorridor":
        menu:
            'If it’s here, it’s hidden.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "underfloor":
        menu:
            'You need to be more specific.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "window" or search == "windows":
        menu:
            'The light enters the chamber through the main entrance, as well as through the gaps between the slabs, but other than that, there are no windows.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "roof" or search == "ceiling":
        menu:
            'You see a couple of spiderwebs. One of the spots on the ceiling is covered by soot.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "spiderwebs" or search == "spiderweb" or search == "spider" or search == "cobweb" or search == "cobwebs" or search == "fly" or search == "spiders" or search == "spider" or search == "web" or search == "webs":
        menu:
            'You see a couple of cobwebs, but they hold only the corpses of spiders and flies.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "lever" or search == "levers":
        menu:
            'There are no visible levers around.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "treasure" or search == "money" or search == "chest" or search == "gold" or search == "jewelry" or search == "diamonds" or search == "diamond" or search == "cash" or search == "gem" or search == "gems" or search == "secrettreasure" or search == "secret":
        menu:
            'If it’s nearby, you need to figure out how to get to it.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "hiddenpassage" or search == "hiddentreasure" or search == "hiddenroom" or search == "secretdoor" or search == "secretpassage":
        menu:
            'If it’s here, it’s hidden.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "undergroundtunnel" or search == "tunnel" or search == "underground" or search == "down":
        menu:
            'You stomp in a couple of spots and don’t hear any direct response. If there’s anything below this chapel, it must be under a thick layer of soil and rocks.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "door" or search == "doors":
        menu:
            'There are no doors in the walls and considering the size of this dolmen, it has only one chamber.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "entrance" or search == "entrances":
        menu:
            'You only see the main entrance. It doesn’t let enough light in to make your search easier.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "ladder" or search == "rope" or search == "stairs":
        menu:
            'You don’t see any.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "ambush":
        menu:
            'Watch out!... Nah, you’re safe. Or are you?
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "trap" or search == "danger":
        menu:
            'If there is one, you haven’t found it, nor activated it. Yet.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    #IMPORTANT SEARCHES THAT DO SOMETHING
    elif search == "soil" or search == "ground" or search == "rocks" or search == "rock" or search == "stone" or search == "slab" or search == "floor":
        $ dolmen_inside_burntlog = 1
        show dolmenburntlog at basicfade
        menu:
            'Even though a part of the ground is covered with a single, massive slab, there are sections free of any flooring. You see soil, small rocks, sand. In one spot you find the remains of charred wood.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "soot":
        $ dolmen_inside_soot = 1
        show dolmensoot behind dolmentrapdoor at basicfade
        menu:
            'You notice sticky soot on the walls. Parts of it cover black marks and pictures, possibly letters.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "smoke":
        $ dolmen_inside_soot = 1
        show dolmensoot behind dolmentrapdoor at basicfade
        menu:
            'You don’t see, nor smell, any smoke, but you notice sticky soot on the walls. Parts of it cover black marks and pictures, possibly letters.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "campfire" or search == "fire" or search == "dust" or search == "wood" or search == "charcoal" or search == "coal" or search == "bones" or search == "bonfire" or search == "hearth" or search == "ash" or search == "ashes" or search == "log" or search == "woodenlog" or search == "firewood" or search == "charredwood":
        $ dolmen_inside_campfire = 1
        $ dolmen_inside_burntlog = 1
        show dolmenburntlog at basicfade
        show dolmencampfire at basicfade
        menu:
            'A part of the floor is littered with the remains of an old campfire, not more than a couple of months old. You see dust, burnt bones, and wood. The wall above this spot is covered with soot.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "signs" or search == "sign" or search == "solution":
        menu:
            'You need to be more specific.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01
    elif search == "marks" or search == "inscription" or search == "lettering" or search == "symbols" or search == "symbol" or search == "arrow" or search == "image" or search == "images" or search == "picture" or search == "pictures" or search == "engraving" or search == "engravings" or search == "writing" or search == "writings" or search == "letters" or search == "letter" or search == "text" or search == "markings" or search == "marking":
        $ at = 0
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
        $ dolmen_inside_writing = 1
        show dolmenwriting behind dolmentrapdoor at basicfade
        menu:
            'A large part of the wall is covered with engravings. It’s difficult to figure out what they are meant to portray, but one picture is obvious to you. A long arrow pointing down.
            \n\nParts of the writing, as well as the nearby wall, is covered with soot.
            '
            'I understand what’s written here.' (condition="at == 'knowledge'"):
                $ at_unlock_knowledge = 0
                $ at = 0
                menu:
                    'The images and letters are a combination of two separate texts. The first one is written with Words of Adir and belongs to an era as old as the dolmen itself. It’s almost impossible to decipher it, but you can make sense of it by connecting some words and the general structure. It was a prayer, or a spell, asking for a safe road.
                    \n\nThe other messages are maybe a couple years old. While they use the same alphabet, they tried to express the modern City Tongue. It’s a list of wares, sometimes portrayed by images, and their value in dragon bones. Some of the pictures are used as obscene insults. You see, for example, the head of a griffon, or a sketch of a wolf. Someone was not happy with the prices they saw.
                    \n\nOne passage is especially interesting: “trapdoor payment.”
                    '
                    'I look for something else.':
                        python:
                            search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump searchdolmen
                    'I go outside.':
                        jump dolmenafterinteraction01
            'I look for something else.':
                $ at_unlock_knowledge = 0
                $ at = 0
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                $ at = 0
                $ at_unlock_knowledge = 0
                jump dolmenafterinteraction01
    elif search == "trapdoor" or search == "hatch" or search == "accesshatch" or search == "underthecampfire" or search == "undercampfire" or search == "underthefire" or search == "underfire" or search == "doorinfloor" or search == "doorunderfloor" or search == "doorinsidefloor" or search == "underfirewood" or search == "underwood" or search == "belowthecampfire" or search == "belowcampfire" or search == "belowthefire" or search == "belowfire" or search == "doorbelowfloor" or search == "doorinsidefloor" or search == "belowfirewood" or search == "belowwood" or search == "beneaththecampfire" or search == "beneathcampfire" or search == "beneaththefire" or search == "beneathfire" or search == "doorbeneathfloor" or search == "doorinsidefloor" or search == "beneathfirewood" or search == "beneathwood" or search == "underarrow" or search == "beneatharrow" or search == "beneathsoot" or search == "undersoot" or search == "floordoor" or search == "doorfloor" or search == "doorfloor" or search == "belowarrow" or search == "downarrow" or search == "belowfire" or search == "underfire":
        $ dolmen_inside_trapdoor = 1
        $ quarters += 1
        show dolmentrapdoor 01 at basicfade
        hide dolmenburntlog
        hide dolmencampfire
        menu:
            'You make a couple of small holes in various spots, but the most interesting area turns out to be hidden beneath the remains of an old campfire. You move all the ash and pieces of wood, until you find a well-preserved plank. You dig around, finding a solid trapdoor locked with a steel padlock.
            '
            'I open the trapdoor with a key.' if item_trapdoorkeydolmen and not dolmen_inside_trapdoor_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the trapdoor with a key.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_key = 1
                jump dolmenopentrapdoorkey
            'I break the trapdoor with my axe.' if not dolmen_inside_trapdoor_open and not dolmen_inside_trapdoor_0hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                if pc_hp > 0:
                    $ dolmen_inside_trapdoor_open = 1
                    show dolmentrapdoor 02 at basicfade
                    $ dolmen_inside_trapdoor_open_axe = 1
                    $ quarters += 1
                    jump dolmenopentrapdooraxe
                else:
                    $ dolmen_inside_trapdoor_0hp = 1
                    jump dolmenopentrapdoorfail
            'I break the trapdoor with my axe.' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                $ quarters += 1
                jump dolmenopentrapdooraxe
            'I’m too weak to open the trapdoor with brute strength. (Required vitality: 1) (disabled)' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and not pc_hp" ):
                pass
            'I break the lock with The Tool of Destruction.' if item_magicchisel == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the lock with The Tool of Destruction.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                jump dolmenopentrapdoorchisel
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump dolmenafterinteraction01
    elif search == "dig":
        menu:
            'You look at the ground. You {i}could{/i} grab your knife, some light, and dig through a few inches of soil and sand, step by step, finding... Probably just rocks. But you doubt it’s going to go smoothly.
            '
            '{image=d6} Let’s get to it.':
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 4)
                $ quarters += (4+d100roll)
                $ dolmen_inside_trapdoor = 1
                $ quarters += 1
                show dolmentrapdoor 01 at basicfade
                hide dolmenburntlog
                hide dolmencampfire
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You start where you stand, pushing aside the layers of dirt and disturbing a few colonies of worms, and the most interesting area turns out to be hidden beneath the remains of an old campfire. You move all the ash and pieces of wood, until you find a well-preserved plank. You dig around, finding a solid trapdoor locked with a steel padlock.
                    '
                    'I open the trapdoor with a key.' if item_trapdoorkeydolmen and not dolmen_inside_trapdoor_open:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the trapdoor with a key.')
                        $ dolmen_inside_trapdoor_open = 1
                        show dolmentrapdoor 02 at basicfade
                        $ dolmen_inside_trapdoor_open_key = 1
                        jump dolmenopentrapdoorkey
                    'I break the trapdoor with my axe.' if not dolmen_inside_trapdoor_open and not dolmen_inside_trapdoor_0hp:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                        if pc_hp > 0:
                            $ dolmen_inside_trapdoor_open = 1
                            show dolmentrapdoor 02 at basicfade
                            $ dolmen_inside_trapdoor_open_axe = 1
                            $ quarters += 1
                            jump dolmenopentrapdooraxe
                        else:
                            $ dolmen_inside_trapdoor_0hp = 1
                            jump dolmenopentrapdoorfail
                    'I break the trapdoor with my axe.' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and pc_hp > 0" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                        $ dolmen_inside_trapdoor_open = 1
                        show dolmentrapdoor 02 at basicfade
                        $ dolmen_inside_trapdoor_open_axe = 1
                        $ quarters += 1
                        jump dolmenopentrapdooraxe
                    'I’m too weak to open the trapdoor with brute strength. (Required vitality: 1) (disabled)' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and not pc_hp" ):
                        pass
                    'I break the lock with The Tool of Destruction.' if item_magicchisel == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the lock with The Tool of Destruction.')
                        $ dolmen_inside_trapdoor_open = 1
                        show dolmentrapdoor 02 at basicfade
                        $ dolmen_inside_trapdoor_open_axe = 1
                        jump dolmenopentrapdoorchisel
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump dolmenafterinteraction01
            'I could examine one spot in particular, or at least look for a specific object.':
                $ at_unlock_knowledge = 0
                $ at = 0
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump dolmenafterinteraction01
    else:
        menu:
            'You either don’t find it, or I can’t understand you.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchdolmen
            'I go outside.':
                jump dolmenafterinteraction01

label dolmentrapdoor:
    if not dolmen_inside_trapdoor_open:
        menu:
            'It’s locked.
            '
            'I open the trapdoor with a key.' if item_trapdoorkeydolmen:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the trapdoor with a key.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_key = 1
                jump dolmenopentrapdoorkey
            'I break the trapdoor with my axe.' if not dolmen_inside_trapdoor_open and not dolmen_inside_trapdoor_0hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                if pc_hp > 0:
                    $ dolmen_inside_trapdoor_open = 1
                    show dolmentrapdoor 02 at basicfade
                    $ dolmen_inside_trapdoor_open_axe = 1
                    $ quarters += 1
                    jump dolmenopentrapdooraxe
                else:
                    $ dolmen_inside_trapdoor_0hp = 1
                    jump dolmenopentrapdoorfail
            'I break the trapdoor with my axe.' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                $ quarters += 1
                jump dolmenopentrapdooraxe
            'I’m too weak to open the trapdoor with brute strength. (Required vitality: 1) (disabled)' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and not pc_hp" ):
                pass
            'I break the lock with The Tool of Destruction.' if item_magicchisel == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the lock with The Tool of Destruction.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                jump dolmenopentrapdoorchisel
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump dolmenafterinteraction01
    else:
        menu:
            'There are vertical {i}stairs{/i} leading to the room below.
            '
            'I climb down.' ( condition="pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down.')
                if dolmen_underground_firsttime:
                    jump dolmenunderground
                else:
                    jump dolmenundergroundfirsttime
            'I’m too exhausted to climb down. (Required vitality: 1) (disabled)' ( condition="not pc_hp" ):
                pass
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump dolmenafterinteraction01

    label dolmenopentrapdoorfail:
        menu:
            'You make a couple of strikes, but your head starts to spin. You don’t have enough strength to get through such a durable obstacle.
            '
            'I open the trapdoor with a key.' if item_trapdoorkeydolmen:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the trapdoor with a key.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_key = 1
                jump dolmenopentrapdoorkey
            'I break the trapdoor with my axe.' if not dolmen_inside_trapdoor_open and not dolmen_inside_trapdoor_0hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                if pc_hp > 0:
                    $ dolmen_inside_trapdoor_open = 1
                    show dolmentrapdoor 02 at basicfade
                    $ dolmen_inside_trapdoor_open_axe = 1
                    $ quarters += 1
                    jump dolmenopentrapdooraxe
                else:
                    $ dolmen_inside_trapdoor_0hp = 1
                    jump dolmenopentrapdoorfail
            'I break the trapdoor with my axe.' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the trapdoor with my axe.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                $ quarters += 1
                jump dolmenopentrapdooraxe
            'I’m too weak to open the trapdoor with brute strength. (Required vitality: 1) (disabled)' ( condition="not dolmen_inside_trapdoor_open and dolmen_inside_trapdoor_0hp and not pc_hp" ):
                pass
            'I break the lock with The Tool of Destruction.' if item_magicchisel == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the lock with The Tool of Destruction.')
                $ dolmen_inside_trapdoor_open = 1
                show dolmentrapdoor 02 at basicfade
                $ dolmen_inside_trapdoor_open_axe = 1
                jump dolmenopentrapdoorchisel
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump dolmenafterinteraction01

    label dolmenopentrapdoorkey:
        menu:
            'You insert the key and after a bit of wiggling, something clicks. The padlock is cold, dirty, and rusty, but you easily get to the iron latch, which moves away smoothly. You have no problem unlocking the trapdoor.
            '
            'I look inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look inside.')
                jump dolmentrapdoorfirstopened

    label dolmenopentrapdooraxe:
        $ achievement_breakingstuff_points += 1
        menu:
            'You take your axe, but realize that the padlock may be much easier to break through. The wooden planks, even if a bit moist, are in great shape.
            \n\nYou look for the right angle and make three strong swings. After an encouraging clang, the padlock falls off.
            '
            'I look inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look inside.')
                jump dolmentrapdoorfirstopened

    label dolmenopentrapdoorchisel:
        $ achievement_breakingstuff_points += 1
        menu:
            'You grab the chisel and a large rock that you found outside. You appose it to the padlock and make one strong swing. After an encouraging clang, the padlock falls off, broken in half.
            '
            'I look inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look inside.')
                jump dolmentrapdoorfirstopened

    label dolmentrapdoorfirstopened: # ropehook
        menu:
            'You lift the hatch and the heavy, humid air suggests an abandoned farm cellar. Your candle allows you to estimate that the tunnel is roughly fifteen feet deep, but there’s no ladder that you can use.
            \n\nYou think about lowering the rope, but you realize that one of the brick walls is covered with large holes, meant to be used as a sort of vertical “stairs.”
            \n\nYou hear no sound coming from the tunnel, but the moldy walls and old cobwebs are not very welcoming.
            '
            'I climb down.' ( condition="pc_hp > 0" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down.')
                if dolmen_underground_firsttime:
                    jump dolmenunderground
                else:
                    jump dolmenundergroundfirsttime
            'I’m too exhausted to climb down. (Required vitality: 1) (disabled)' ( condition="not pc_hp" ):
                pass
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump dolmenafterinteraction01

label dolmenundergroundfirsttime:
    $ dolmen_underground_firsttime += 1
    hide dolmenburntlog
    hide dolmencampfire
    hide dolmensoot
    hide dolmenwriting
    hide dolmentrapdoor
    show areapicture dolmenundergroundpart at basicfade
    stop nature fadeout 2.0
    menu:
        'You have to move slowly, learning the new route. You hug the cold, moist wall, seeking the support for your boots. It doesn’t take long before you feel comfortable enough to jump down, then light up another candle.
        \n\nBoth the walls and the floor are made of stone slabs. You see no movement, no other sources of light. The short tunnel leads you to a small room.
        '
        'I walk inside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk inside.')
            jump dolmenunderground

label dolmenunderground:
    if not dolmen_underground_chest:
        show areapicture dolmenundergroundfull at basicfade
        $ custom1 = "The one thing that seems to be uniquely fresh and durable is a small, wooden box, held together by a few fiber cords."
    else:
        show areapicture dolmenundergroundfullnobox at basicfade
        $ custom1 = "You find nothing of value."
    stop nature fadeout 2.0
    hide dolmenburntlog
    hide dolmencampfire
    hide dolmensoot
    hide dolmenwriting
    hide dolmentrapdoor
    menu:
        'The room smells of rotten wood and fungi. Abandoned junk is scattered on the ground and shelves: earthenware jars, rotting scraps of linen or leather, wooden plates, bones for carving, and rusty, iron tools.
        \n\nWhile these odds and ends may be years or decades old, the basement could be just as ancient as the main floor of the chapel.
        \n\n[custom1]
        '
        'I take the box.' if not dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the box.')
            $ dolmen_underground_chest += 1
            jump dolmenpctakesthebox
        'I leave the box behind and climb outside.' if not dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the box behind and climb outside.')
            jump dolmenleavingtheunderground
        'I climb outside.' if dolmen_underground_chest:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb outside.')
            jump dolmenleavingtheunderground

label dolmenleavingtheunderground:
    if dolmen_hourglass_blood:
        show areapicture dolmenOPENblood behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    elif dolmen_hourglass_scratches:
        show areapicture dolmenOPENscratches behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    else:
        show areapicture dolmenOPENclean behind dolmenburntlog, dolmencampfire, dolmensoot, dolmenwriting, dolmentrapdoor at basicfade
    $ quarters += 1
    if dolmen_inside_trapdoor_open:
        show dolmentrapdoor 02 at basicfade
    elif dolmen_inside_trapdoor:
        show dolmentrapdoor 01 at basicfade
    if dolmen_inside_burntlog and not dolmen_inside_trapdoor:
        show dolmenburntlog at basicfade
    if dolmen_inside_campfire and not dolmen_inside_trapdoor:
        show dolmencampfire at basicfade
    if dolmen_inside_soot:
        show dolmensoot behind dolmentrapdoor at basicfade
    if dolmen_inside_writing:
        show dolmenwriting behind dolmentrapdoor at basicfade
    play nature "audio/ambient/dolmen01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    menu:
        'Using the light of your candle, you memorize the holes. You climb up quickly.
        '
        'I climb down.' ( condition="pc_hp > 0" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down.')
            if dolmen_underground_firsttime:
                jump dolmenunderground
            else:
                jump dolmenundergroundfirsttime
        'I’m too exhausted to climb down. (Required vitality: 1) (disabled)' ( condition="not pc_hp" ):
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump dolmenafterinteraction01

label dolmenpctakestheboxALL:
    label dolmenpctakesthebox:
        $ quest_healingpotion_description01 = "I found the box."
        if quest_healingpotion == 1:
            $ renpy.notify("Journal updated: Merchant’s Medicament")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament{/i}')
        show areapicture dolmenundergroundfullnobox at basicfade
        hide dolmenburntlog
        hide dolmencampfire
        hide dolmensoot
        hide dolmenwriting
        hide dolmentrapdoor
        menu:
            'It doesn’t feel empty, but it’s light. You shake it for a bit, trying to guess what’s inside. You can’t open the box without cutting the cords.
            '
            'I cut the cords with my knife and open the box.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut the cords with my knife and open the box.')
                jump dolmenpcopensthebox
            'This box belongs to someone. For now, I’m going to keep it in one piece.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This box belongs to someone. For now, I’m going to keep it in one piece.')
                $ item_boxfromdolmen += 1
                $ renpy.notify("You found a locked box.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a locked box.{/i}')
                jump dolmenleavingtheunderground

    label dolmenpcopensthebox:
        $ quest_healingpotion_description02 = "It turns out that the box contained a bottle, probably a magical potion."
        if quest_healingpotion == 1:
            $ renpy.notify("Journal updated: Merchant’s Medicament")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament{/i}')
            $ custom1 = "Probably the one that you were meant to find for {color=#f6d6bd}Akakios{/color}, the merchant."
        else:
            $ custom1 = ""
        menu:
            'The box turns out to be filled with rags, covering a fragile bottle. It’s small and closed with a tall wax seal, inside of which you see a thin stick. It should be easy to instantly open it, if needed.
            \n\nYou can’t look inside and if you open it, you may not be able to seal it again. Nevertheless, you recognize a magical potion when you see one. [custom1]
            '
            'I open the bottle and drink from it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the bottle and drink from it.')
                $ item_potiondolmen_known = 1
                jump dolmenpcdrinkspotion
            'I open the bottle and smell its contents.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the bottle and smell its contents.')
                $ item_potiondolmen_known = 1
                jump dolmenpcsmellsspotion
            'I attach it to my belt - it may be useful later on. I prepare to leave.':
                $ item_potiondolmen = 1
                $ renpy.notify("You found a bottle.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a bottle.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I attach it to my belt - it may be useful later on. I prepare to leave.')
                jump dolmenleavingtheunderground

    label dolmenpcdrinkspotion:
        $ pc_hp = limit_pc_hp(pc_hp+4)
        show plus4hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 vitality points.{/i}')
        $ quest_healingpotion_description04 = "I’ve lost the potion. I should speak with the merchant."
        if quest_healingpotion == 1:
            $ renpy.notify("Journal updated: Merchant’s Medicament")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament{/i}')
        menu:
            'It tastes like honey, raspberries, and wormwood. Initially, it’s awful, but you forget about your senses quickly. Your shell feels refreshed, strong, ready to act. Even the scratches are instantly healed.
            \n\nThe ecstatic warmth fills your limbs, and you can’t help but smile and giggle for a few breaths.
            '
            'I try to focus on where I am and prepare for the rest of the journey.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to focus on where I am and prepare for the rest of the journey.')
                jump dolmenleavingtheunderground

    label dolmenpcsmellsspotion:
        menu:
            'It smells tasty, like fruits cooked in honey syrup. You don’t sense any hard drinks. Probably a healing potion. If so, it must be valuable.
            \n\nYou know that you can safely seal the bottle again. The potion shouldn’t spoil anytime soon.
            '
            'I drink the potion.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drink the potion.')
                jump dolmenpcdrinkspotion
            'I close the bottle with its wax seal and attach it to my belt.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I close the bottle with its wax seal and attach it to my belt.')
                $ item_potiondolmen = 1
                $ renpy.notify("You found a potion.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a potion.{/i}')
                jump dolmenleavingtheunderground
