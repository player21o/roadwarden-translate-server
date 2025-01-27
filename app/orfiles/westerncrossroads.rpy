###################### Western Crossroads
default westerncrossroads_firsttime = 0
default westerncrossroads_fluff = ""
default westerncrossroads_fluff_old = ""

default westerncrossroads_sn = ""
default westerncrossroads_ss = ""
default westerncrossroads_sw = ""
default westerncrossroads_se = ""

default westerncrossroads_knownpaths = 0
default westerncrossroads_searched = 0
default westerncrossroads_missingsign = 0

label westerncrossroads01:
    nvl clear
    $ pc_area = "westerncrossroads"
    stop music fadeout 4.0
    play nature "audio/ambient/southerncrossroads01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture westerncrossroads01 at basicfade
    label westerncrossroads_fluffloop:
        $ westerncrossroads_fluff = renpy.random.choice(['Two squirrels, one red and one blue, are standing on the top of two opposite signposts, screaming and throwing pebbles at each other. When you get closer, they climb down swiftly, then run toward a nearby tree.', 'There’s some sort of skirmish happening in the nearby bushes, but the dense leaves block your view. You hear a painful whine, and the plants stop shaking.', 'A terrible roaring comes from the east. You can’t even guess what sort of creature would be capable of making such a noise.', 'You reach a pleasant smell of moist soil and the constant cacophony of buzzing insects.', 'A massive eagle is cutting through the skies above you, either unaware of your presence, or unperturbed by you.'])
        if westerncrossroads_fluff_old == westerncrossroads_fluff:
            jump westerncrossroads_fluffloop
        else:
            $ westerncrossroads_fluff_old = westerncrossroads_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not westerncrossroads_firsttime:
        $ world_known_npcs += 0
        $ world_known_areas += 1
        $ westerncrossroads_firsttime = 1
        $ world_known_areas += 1
        $ howlersdell_unlocked = 1
        $ westgate_unlocked = 1
        $ oldpagos_unlocked = 1
        $ ford_unlocked = 1
        jump westerncrossroadsfirsttime01
    else:
        jump westerncrossroadsregular01

label westerncrossroadsfirsttime01:
    if not westgate_firsttime:
        $ custom1 = "The road east leads toward the hills, behind which there are unusually tall, dark trees. "
    else:
        $ custom1 = ""
        $ westerncrossroads_knownpaths += 1
    if not howlersdell_firsttime:
        $ custom3 = "The trail south is curvy, surrounded by hills. You don’t see many plants on the horizon. "
    else:
        $ custom3 = ""
        $ westerncrossroads_knownpaths += 1
    if not ford_firsttime:
        $ custom2 = "There’s a dense forest in the north, from which you hear the croaking of toads. "
    else:
         $ custom2 = ""
         $ westerncrossroads_knownpaths += 1
    if westerncrossroads_knownpaths == 1:
        $ westerncrossroads_knownpaths = "The last path is already known to you."
    else:
        $ westerncrossroads_knownpaths = "The other paths are already known to you."
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '{color=#f6d6bd}[horsename]’s{/color} hooves thump loudly on the beaten track. The green bushes, shrubs, and trees prove that the soil here is fertile, yet the plants don’t overgrow the road. These crossroads must be busy at times, maybe even patrolled.
        \n\nIn the distant west, you see the mountain peaks dividing the lowlands from the ocean. [custom1][custom2][custom3][westerncrossroads_knownpaths]
        \n\nYou’re surrounded by four signposts, all of which seem to be made from the same type of wood, now covered in moss and fungi, yet the pictures and letters that cover the nailed boards are nothing alike.
        '
        'I approach the western signpost.' if not westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
            jump westerncrossroads_swest01
        'I approach the eastern signpost.' if not westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
            jump westerncrossroads_seast01
        'I approach the northern signpost.' if not westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
            jump westerncrossroads_snorth01
        'I approach the southern signpost.' if not westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
            jump westerncrossroads_ssouth01
        'I return to the western signpost.' if westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
            jump westerncrossroads_swest01
        'I return to the eastern signpost.' if westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
            jump westerncrossroads_seast01
        'I return to the northern signpost.' if westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
            jump westerncrossroads_snorth01
        'I return to the southern signpost.' if westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
            jump westerncrossroads_ssouth01
        'I search the area.' if not westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
            jump westerncrossroads_ssearch01
        'I search the area some more.' if westerncrossroads_searched == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
            jump westerncrossroads_ssearch02
        'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
            jump westerncrossroads_ssearch03
        'I take another look at the destroyed sign.' if westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
            jump westerncrossroads_ssearch04

label westerncrossroadsregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[westerncrossroads_fluff]
        '
        'I approach the western signpost.' if not westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
            jump westerncrossroads_swest01
        'I approach the eastern signpost.' if not westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
            jump westerncrossroads_seast01
        'I approach the northern signpost.' if not westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
            jump westerncrossroads_snorth01
        'I approach the southern signpost.' if not westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
            jump westerncrossroads_ssouth01
        'I return to the western signpost.' if westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
            jump westerncrossroads_swest01
        'I return to the eastern signpost.' if westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
            jump westerncrossroads_seast01
        'I return to the northern signpost.' if westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
            jump westerncrossroads_snorth01
        'I return to the southern signpost.' if westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
            jump westerncrossroads_ssouth01
        'I search the area.' if not westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
            jump westerncrossroads_ssearch01
        'I search the area some more.' if westerncrossroads_searched == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
            jump westerncrossroads_ssearch02
        'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
            jump westerncrossroads_ssearch03
        'I take another look at the destroyed sign.' if westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
            jump westerncrossroads_ssearch04

label westerncrossroads_swest01:
    $ westerncrossroads_sw = 1
    if pc_class != "scholar":
        menu:
            'It has two planks attached to a single post, both of them nailed with rusty steel.
            \n\nThe lower sign is divided in two halves. The left edge is engraved with four simple shapes - squares with roof-like lines hanging above them. The other edge bears two engraved “piles” - one of them made of horizontal rectangles, the other of inexact circles. You don’t recognize the letters between those two piles.
            \n\nThe upper plank is covered with two short words drawn in white paint and, right below them, an engraved, vertical rectangle with an hourglass inside it.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
    else:
        menu:
            'It has two planks attached to a single post, both of them nailed with rusty steel.
            \n\nThe lower sign is divided in two halves. The left edge is engraved with four simple shapes - squares with roof-like lines hanging above them. The other edge bears two engraved “piles” - one of them made of horizontal rectangles, the other of inexact circles. The letters between these two piles say {i}STONE{/i}.
            \n\nThe upper plank is covered with a white word {i}MONA-STERY{/i}, though it’s divided in half. Right below it is an engraved, vertical rectangle with an hourglass inside it.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04

label westerncrossroads_seast01:
    $ westerncrossroads_se = 1
    menu:
        'The long plank, attached with rusted iron nails, is almost empty. It bears no words, only a single picture, painted with great care. It portrays a city-like gate, with a watchtower to its left and right, and a couple of small conifers growing beside and partially behind the towers.
        '
        'I approach the western signpost.' if not westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
            jump westerncrossroads_swest01
        'I approach the eastern signpost.' if not westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
            jump westerncrossroads_seast01
        'I approach the northern signpost.' if not westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
            jump westerncrossroads_snorth01
        'I approach the southern signpost.' if not westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
            jump westerncrossroads_ssouth01
        'I return to the western signpost.' if westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
            jump westerncrossroads_swest01
        'I return to the eastern signpost.' if westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
            jump westerncrossroads_seast01
        'I return to the northern signpost.' if westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
            jump westerncrossroads_snorth01
        'I return to the southern signpost.' if westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
            jump westerncrossroads_ssouth01
        'I search the area.' if not westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
            jump westerncrossroads_ssearch01
        'I search the area some more.' if westerncrossroads_searched == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
            jump westerncrossroads_ssearch02
        'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
            jump westerncrossroads_ssearch03
        'I take another look at the destroyed sign.' if westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
            jump westerncrossroads_ssearch04

label westerncrossroads_snorth01:
    $ westerncrossroads_sn = 1
    if pc_class != "scholar":
        menu:
            'It’s attached with nails made of pointy, carved bones, and divided into three sections covered with small engravings.
            \n\nThe part on the left has three large squares with roof-like lines hanging above them. No other pictures or words.
            \n\nThe one in the middle has only one square, but also a simple, horizontal symbol of a fish and a short word beneath it, which you don’t recognize.
            \n\nThe image on the right has two roofed squares, but also two other images, which you recognize easily. A deer and a standing barrel.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
    else:
        menu:
            'It’s attached with nails made of pointy, carved bones, and divided into three sections covered with small engravings.
            \n\nThe part on the left has three large squares with roof-like lines hanging above them. No other pictures or words.
            \n\nThe one in the middle has only one square, but also a simple, horizontal symbol of a fish and a short word beneath. It spells {i}SALT{/i}.
            \n\nThe image on the right has two roofed squares, but also two other images, which you recognize easily. A deer and a standing barrel.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04

label westerncrossroads_ssouth01:
    $ westerncrossroads_ss = 1
    if pc_class != "scholar":
        menu:
            'It’s covered with green, blue, and white paint that portray simple squares with roof-like lines hanging above them. Each square has a large letter inside it, though you don’t recognize them. Nevertheless, the pictures are not too old.
            \n\nThere are no other words or marks. The plank was attached with a set of wooden wedges.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
    else:
        menu:
            'It’s covered with green, blue, and white paint that portray simple squares with roof-like lines hanging above them. Each square has a large letter inside it, and together they spell {i}HOWLERSDELL{/i}. Both the pictures and letters are not too old.
            \n\nThere are no other words or marks. The plank was attached with a set of wooden wedges.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04

label westerncrossroads_ssearch01:
    $ westerncrossroads_searched = 1
    $ quarters += 1
    if pc_class != "scholar":
        menu:
            'The thicket doesn’t help. You notice the remains of berries and pears, but most of them are already rotting, spread close to the wooden stools at the side of the road. The nearby creek is not impressively deep, but the beaver dam, for some reason taller than you are, makes it wide, and waters the surrounding soil.
            \n\nA few steps away from the southern signpost you find something sticking out of a shrub. It’s a moist plank, covered by fungi. You try to move it with a stick and a gloved hand.
            \n\nAfter a minute or so, you confirm it’s an abandoned sign, covered with green letters and colorful pictures of flowers and trees.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
    else:
        menu:
            'The thicket doesn’t help. You notice the remains of berries and pears, but most of them are already rotting, spread close to the wooden stools at the side of the road. The nearby creek is not impressively deep, but the beaver dam, for some reason taller than you are, makes it wide, and waters the surrounding soil.
            \n\nA few steps away from the southern signpost you find something sticking out of a shrub. It’s a moist plank, covered by fungi. You try to move it with a stick and a gloved hand.
            \n\nAfter a minute or so, you confirm it’s an abandoned sign, covered with green letters and colorful pictures of flowers and trees. {i}STEEPHOUSE{/i}, you read with difficulty.
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04

label westerncrossroads_ssearch02:
    $ westerncrossroads_searched = 2
    $ quarters += 1
    menu:
        'After another few minutes of disturbing the local fauna, you’re sure there’s nothing more here to be found.
        '
        'I approach the western signpost.' if not westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
            jump westerncrossroads_swest01
        'I approach the eastern signpost.' if not westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
            jump westerncrossroads_seast01
        'I approach the northern signpost.' if not westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
            jump westerncrossroads_snorth01
        'I approach the southern signpost.' if not westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
            jump westerncrossroads_ssouth01
        'I return to the western signpost.' if westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
            jump westerncrossroads_swest01
        'I return to the eastern signpost.' if westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
            jump westerncrossroads_seast01
        'I return to the northern signpost.' if westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
            jump westerncrossroads_snorth01
        'I return to the southern signpost.' if westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
            jump westerncrossroads_ssouth01
        'I search the area.' if not westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
            jump westerncrossroads_ssearch01
        'I search the area some more.' if westerncrossroads_searched == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
            jump westerncrossroads_ssearch02
        'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
            jump westerncrossroads_ssearch03
        'I take another look at the destroyed sign.' if westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
            jump westerncrossroads_ssearch04

label westerncrossroads_ssearch03:
    $ westerncrossroads_missingsign = 1
    $ minutes += 5
    menu:
        'The southern post is the only one with holes left by nails.
        '
        'I approach the western signpost.' if not westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
            jump westerncrossroads_swest01
        'I approach the eastern signpost.' if not westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
            jump westerncrossroads_seast01
        'I approach the northern signpost.' if not westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
            jump westerncrossroads_snorth01
        'I approach the southern signpost.' if not westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
            jump westerncrossroads_ssouth01
        'I return to the western signpost.' if westerncrossroads_sw:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
            jump westerncrossroads_swest01
        'I return to the eastern signpost.' if westerncrossroads_se:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
            jump westerncrossroads_seast01
        'I return to the northern signpost.' if westerncrossroads_sn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
            jump westerncrossroads_snorth01
        'I return to the southern signpost.' if westerncrossroads_ss:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
            jump westerncrossroads_ssouth01
        'I search the area.' if not westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
            jump westerncrossroads_ssearch01
        'I search the area some more.' if westerncrossroads_searched == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
            jump westerncrossroads_ssearch02
        'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
            jump westerncrossroads_ssearch03
        'I take another look at the destroyed sign.' if westerncrossroads_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
            jump westerncrossroads_ssearch04

label westerncrossroads_ssearch04:
    if westerncrossroads_missingsign:
        $ custom1 = " As far as you can tell, it used to be attached to the southern post."
    else:
        $ custom1 = ""
    if pc_class != "scholar":
        menu:
            'It’s covered with green letters and colorful pictures of flowers and trees, now blending in with mold.[custom1]
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
    else:
        menu:
            'It’s covered with green letters that spell {i}STEEPHOUSE{/i} and colorful pictures of flowers and trees, now blending in with mold.[custom1]
            '
            'I approach the western signpost.' if not westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the western signpost.')
                jump westerncrossroads_swest01
            'I approach the eastern signpost.' if not westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the eastern signpost.')
                jump westerncrossroads_seast01
            'I approach the northern signpost.' if not westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the northern signpost.')
                jump westerncrossroads_snorth01
            'I approach the southern signpost.' if not westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern signpost.')
                jump westerncrossroads_ssouth01
            'I return to the western signpost.' if westerncrossroads_sw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the western signpost.')
                jump westerncrossroads_swest01
            'I return to the eastern signpost.' if westerncrossroads_se:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the eastern signpost.')
                jump westerncrossroads_seast01
            'I return to the northern signpost.' if westerncrossroads_sn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern signpost.')
                jump westerncrossroads_snorth01
            'I return to the southern signpost.' if westerncrossroads_ss:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern signpost.')
                jump westerncrossroads_ssouth01
            'I search the area.' if not westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area.')
                jump westerncrossroads_ssearch01
            'I search the area some more.' if westerncrossroads_searched == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area some more.')
                jump westerncrossroads_ssearch02
            'I try to find out where did the old sign used to be attached.' if westerncrossroads_searched and not westerncrossroads_missingsign:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find out where did the old sign used to be attached.')
                jump westerncrossroads_ssearch03
            'I take another look at the destroyed sign.' if westerncrossroads_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the destroyed sign.')
                jump westerncrossroads_ssearch04
