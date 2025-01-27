###################### Fishing Hamlet
default fishinghamlet_firsttime = 0
default fishinghamlet_fluff = ""
default fishinghamlet_fluff_old = ""
default fishinghamlet_aegidia_fluff = ""
default fishinghamlet_aegidia_fluff_old = ""
default fishinghamlet_areas_seen = 1 #out of 7
default fishinghamlet_areas_seen_01 = 1
default fishinghamlet_areas_seen_02 = 0
default fishinghamlet_areas_seen_03 = 0
default fishinghamlet_areas_seen_04 = 0
default fishinghamlet_areas_seen_05 = 0
default fishinghamlet_areas_seen_06 = 0
default fishinghamlet_areas_seen_06b = 0
default fishinghamlet_areas_seen_07 = 0

default fishinghamlet_driftwood = 0

label fishinghamlet01:
    if highisland_mode and not asterion_found:
        jump highisland_journey_fishinghamlet00
    nvl clear
    $ pc_area = "fishinghamlet"
    stop music fadeout 4.0
    if aegidia_firsttime:
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
    else:
        play nature "audio/ambient/fishinghamlet01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show howlersdelldarkbackground at basicfade
    if fishinghamlet_areas_seen_01:
        show fishinghamletscrap01 at basicfade
    if fishinghamlet_areas_seen_02:
        show fishinghamletscrap02 at basicfade
    if fishinghamlet_areas_seen_03:
        show fishinghamletscrap03 at basicfade
    if fishinghamlet_areas_seen_04:
        show fishinghamletscrap04 at basicfade
    if fishinghamlet_areas_seen_05:
        show fishinghamletscrap05 at basicfade
    if fishinghamlet_areas_seen_06:
        show fishinghamletscrap06 at basicfade
    if fishinghamlet_areas_seen_07:
        show fishinghamletscrap07 at basicfade
    label fishinghamlet_fluffloop:
        $ fishinghamlet_fluff = renpy.random.choice(['The white and purple seagulls are crowding the sky, preparing themselves for the next battle.', 'You hear a thunderous roar coming from a sea monster, even though you see none on the horizon.', 'A green-and-red tortoise is resting in the grass, but flees to the water as soon as it hears your mount.', 'The waves are getting higher. Hit by the chilling wind, you adjust your cloak.', 'For a few moments, you think that some of the tall rocks are moving, but as you stare at them, you find only the seagulls.', 'an ibex is drinking from the brook, but runs away when it notices your gaze.', 'A small monkey is sitting on one of the roofs, feasting on a fish larger than its arm.'])
        if fishinghamlet_fluff_old == fishinghamlet_fluff:
            jump fishinghamlet_fluffloop
        else:
            $ fishinghamlet_fluff_old = fishinghamlet_fluff
    label fishinghamlet_aegidia_fluffloop:
        $ fishinghamlet_aegidia_fluff = renpy.random.choice(['{color=#f6d6bd}Aegidia{/color} is in the main yard of the hamlet, training with her bow.', '{color=#f6d6bd}Aegidia{/color} is by the brook, fishing with a spear. When she sees you, she gets out of the water and wipes herself with a cloth.', '{color=#f6d6bd}Aegidia{/color} is sitting near the entrance, carving a bowl from a piece of driftwood.', '{color=#f6d6bd}Aegidia{/color} is standing on the shore, staring at the horizon.', 'You catch a whiff of a roasted fish and see smoke coming from the hamlet’s yard.', 'You catch a whiff of a roasted bird and see smoke coming from the largest building.'])
        if fishinghamlet_aegidia_fluff_old == fishinghamlet_aegidia_fluff:
            jump fishinghamlet_aegidia_fluffloop
        else:
            $ fishinghamlet_aegidia_fluff_old = fishinghamlet_aegidia_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not fishinghamlet_firsttime:
        $ world_known_npcs += 1
        $ world_known_areas += 1
        $ fishinghamlet_firsttime = 1
        $ world_known_areas += 1
        $ rockslide_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        jump fishinghamletfirsttime01
    else:
        jump fishinghamletregular01

label fishinghamletfirsttime01:
    if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
        $ can_leave = 1
        $ can_rest = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
    $ can_items = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'The coast is a mixture of green and gray, with sands already covered by the water. The waves hit the land fiercely, but can’t put an end to the screeching of seagulls.
        \n\nThe signs of human presence are fading away - the grasses overgrow the path, the palisade and building are already collapsing. The lonely tree, still bearing signs of human pruning, is unkempt and wild. You see no smoke or lights.
        '
        'I keep {color=#f6d6bd}[horsename]{/color} close. There may be something hidden behind a rock.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep %s close. There may be something hidden behind a rock.' %horsename)
            $ at = 0
            $ can_items = 1
            if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
                $ can_leave = 1
                $ can_rest = 1
            else:
                $ can_leave = 0
                $ can_rest = 0
            if pc_class == "scholar" and fishinghamlet_areas_seen_05 and not fishinghamlet_driftwood and not item_driftwood and not beach_driftwoodtaken:
                $ at_unlock_knowledge = 1
                $ at = 0
            menu:
                'In the north, you find tall rocks sticking out of the land, like fingers of a buried troll.
                \n\nThe southern brook hides even more grasses and shrubs, which end with yet another rockface.
                \n\nThere are no obvious obstacles that would block you from entering the village, but there’s also enough space to look around the wall.
                '
                'I should prepare my crossbow.' if not aegidia_crossbow and item_crossbow and item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should prepare my crossbow.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump aegidia_crossbow01
                'I don’t have any quarrels for my crossbow. (disabled)' if not aegidia_crossbow and item_crossbow and not item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
                    pass
                'I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamlet_driftwood01
                'I return to {color=#f6d6bd}Aegidia{/color}.' if aegidia_firsttime and aegidia_name:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Aegidia{/color}.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletaegidiaregular01
                'I return to {color=#f6d6bd}the archeress{/color}.' if aegidia_firsttime and not aegidia_name:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the archeress{/color}.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletaegidiaregular01
                'I cross the brook.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross the brook.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap02
                'I approach the southern shore.' if fishinghamlet_areas_seen_02 and not fishinghamlet_areas_seen_03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern shore.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap03
                'I walk along the palisade, near the southern building.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_04:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk along the palisade, near the southern building.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap04
                'I go north, to the shore.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_05:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go north, to the shore.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap05
                'I enter the hamlet.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_06:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap06
                'I go to the harbor.' if fishinghamlet_areas_seen_06 and not fishinghamlet_areas_seen_07:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the harbor.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump fishinghamletdiscoveringscrap07
                'I wash myself in the ocean.' if cleanliness <= 0 and fishinghamlet_areas_seen_07:
                    jump fishinghamlettakingabath01
                'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0 and fishinghamlet_areas_seen_07:
                    pass
                'I’ve already explored the entire hamlet. (disabled)' if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_02 and fishinghamlet_areas_seen_03 and fishinghamlet_areas_seen_04 and fishinghamlet_areas_seen_05 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
                    pass

label fishinghamletregular01:
    $ at = 0
    if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
        $ can_leave = 1
        $ can_rest = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
    if pc_class == "scholar" and fishinghamlet_areas_seen_05 and not fishinghamlet_driftwood and not item_driftwood and not beach_driftwoodtaken:
        $ at_unlock_knowledge = 1
        $ at = 0
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'The hamlet is peaceful, silent like a dead tree. [fishinghamlet_fluff] [fishinghamlet_aegidia_fluff]
        '
        'I should prepare my crossbow.' if not aegidia_crossbow and item_crossbow and item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should prepare my crossbow.')
            jump aegidia_crossbow01
        'I don’t have any quarrels for my crossbow. (disabled)' if not aegidia_crossbow and item_crossbow and not item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
            pass
        'I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamlet_driftwood01
        'I return to {color=#f6d6bd}Aegidia{/color}.' if aegidia_firsttime and aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Aegidia{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I return to {color=#f6d6bd}the archeress{/color}.' if aegidia_firsttime and not aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the archeress{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I cross the brook.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross the brook.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap02
        'I approach the southern shore.' if fishinghamlet_areas_seen_02 and not fishinghamlet_areas_seen_03:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap03
        'I walk along the palisade, near the southern building.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_04:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk along the palisade, near the southern building.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap04
        'I go north, to the shore.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_05:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go north, to the shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap05
        'I enter the hamlet.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_06:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap06
        'I go to the harbor.' if fishinghamlet_areas_seen_06 and not fishinghamlet_areas_seen_07:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the harbor.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap07
        'I wash myself in the ocean.' if cleanliness <= 0 and fishinghamlet_areas_seen_07:
            jump fishinghamlettakingabath01
        'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0 and fishinghamlet_areas_seen_07:
            pass
        'I’ve already explored the entire hamlet. (disabled)' if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_02 and fishinghamlet_areas_seen_03 and fishinghamlet_areas_seen_04 and fishinghamlet_areas_seen_05 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
            pass

label fishinghamletselectwheretogo:
    $ at = 0
    $ can_items = 1
    if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
        $ can_leave = 1
        $ can_rest = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
    if pc_class == "scholar" and fishinghamlet_areas_seen_05 and not fishinghamlet_driftwood and not item_driftwood and not beach_driftwoodtaken:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'Where would you like to go?
        '
        'Actually, it’s a good moment to load my crossbow.' if not aegidia_crossbow and item_crossbow and item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, it’s a good moment to load my crossbow.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump aegidia_crossbow01
        'I don’t have any quarrels for my crossbow. (disabled)' if not aegidia_crossbow and item_crossbow and not item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
            pass
        'I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamlet_driftwood01
        'I return to {color=#f6d6bd}Aegidia{/color}.' if aegidia_firsttime and aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Aegidia{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I return to {color=#f6d6bd}the archeress{/color}.' if aegidia_firsttime and not aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the archeress{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I cross the brook.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross the brook.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap02
        'I approach the southern shore.' if fishinghamlet_areas_seen_02 and not fishinghamlet_areas_seen_03:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap03
        'I walk along the palisade, near the southern building.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_04:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk along the palisade, near the southern building.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap04
        'I go north, to the shore.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_05:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go north, to the shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap05
        'I enter the hamlet.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_06:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap06
        'I go to the harbor.' if fishinghamlet_areas_seen_06 and not fishinghamlet_areas_seen_07:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the harbor.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap07
        'I wash myself in the ocean.' if cleanliness <= 0 and fishinghamlet_areas_seen_07:
            jump fishinghamlettakingabath01
        'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0 and fishinghamlet_areas_seen_07:
            pass
        'I’ve already explored the entire hamlet. (disabled)' if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_02 and fishinghamlet_areas_seen_03 and fishinghamlet_areas_seen_04 and fishinghamlet_areas_seen_05 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
            pass

label fishinghamletselectwheretogover02:
    $ at = 0
    $ can_items = 1
    if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
        $ can_leave = 1
        $ can_rest = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
    if pc_class == "scholar" and fishinghamlet_areas_seen_05 and not fishinghamlet_driftwood and not item_driftwood and not beach_driftwoodtaken:
        $ at_unlock_knowledge = 1
        $ at = 0
    if aegidia_friendship <= 1:
        $ custom1 = "Still holding her bow, she keenly looks at you."
    if aegidia_friendship <= 4:
        $ custom1 = "She nods slowly, still holding her bow, and observes your mount."
    else:
        $ custom1 = "“Safe travels,” she says with a smile and pats your palfrey’s neck."
    menu:
        '[custom1] You leave the hamlet.
        '
        'Actually, it’s a good moment to load my crossbow.' if not aegidia_crossbow and item_crossbow and item_crossbowquarrels and aegidia_alive and not aegidia_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, it’s a good moment to load my crossbow.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump aegidia_crossbow01
        'I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend some time looking through the pieces of driftwood at the northern shore. They could be useful at an alchemy table.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamlet_driftwood01
        'I return to {color=#f6d6bd}Aegidia{/color}.' if aegidia_firsttime and aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Aegidia{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I return to {color=#f6d6bd}the archeress{/color}.' if aegidia_firsttime and not aegidia_name:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the archeress{/color}.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletaegidiaregular01
        'I cross the brook.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross the brook.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap02
        'I approach the southern shore.' if fishinghamlet_areas_seen_02 and not fishinghamlet_areas_seen_03:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the southern shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap03
        'I walk along the palisade, near the southern building.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_04:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk along the palisade, near the southern building.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap04
        'I go north, to the shore.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_05:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go north, to the shore.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap05
        'I enter the hamlet.' if fishinghamlet_areas_seen_01 and not fishinghamlet_areas_seen_06:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap06
        'I go to the harbor.' if fishinghamlet_areas_seen_06 and not fishinghamlet_areas_seen_07:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the harbor.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump fishinghamletdiscoveringscrap07
        'I wash myself in the ocean.' if cleanliness <= 0 and fishinghamlet_areas_seen_07:
            jump fishinghamlettakingabath01
        'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0 and fishinghamlet_areas_seen_07:
            pass
        'I’ve already explored the entire hamlet. (disabled)' if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_02 and fishinghamlet_areas_seen_03 and fishinghamlet_areas_seen_04 and fishinghamlet_areas_seen_05 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
            pass

label fishinghamletdiscoveringscrap02:
    show fishinghamletscrap02 at basicfade
    $ fishinghamlet_areas_seen_02 = 1
    $ fishinghamlet_areas_seen += 1
    $ minutes += 5
    menu:
        'The area is surrounded by cliffs, like an antechamber in a palace. The meadow here is modest, but still lengthy enough for {color=#f6d6bd}[horsename]{/color} to enjoy it.
        \n\nYou count the tree stumps and boughs, then realize that this lea is but a dead shell of a lush copse, a clearing left behind by the settlers. A single shrub is still alive, too weak to withstand the sun and winds all by itself. You think of the roots spreading beneath your boots, now dead and rotting.
        '
        'I go to the shore in the west.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the shore.')
            jump fishinghamletdiscoveringscrap03
        'I turn back.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back.')
            jump fishinghamletselectwheretogo

label fishinghamletdiscoveringscrap03:
    show fishinghamletscrap03 at basicfade
    $ fishinghamlet_areas_seen_03 = 1
    $ fishinghamlet_areas_seen += 1
    $ minutes += 5
    $ item_oceannecklace = 1
    $ renpy.notify("You found an ocean necklace.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found an ocean necklace.{/i}')
    if not fishinghamlet_areas_seen_04:
        $ custom1 = " Being by the bank of the brook, you look north, but find no human beings."
    else:
        $ custom1 = ""
    menu:
        'The stones here are almost as huge as a building, both on land and in the water. You can only guess how much space they occupy beneath the surface.
        \n\nYou inspect the dead tree growing by the brook and find an old necklace among its roots. It’s made from a leather strip, now covered in mold, a long, cream-colored seashell, and a few thin, round flakes, most likely made of a sea monster’s tooth.
        \n\nYou try to wash it, but to no avail.
        '
        'I shove it into a sack.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shove it into a sack.')
            jump fishinghamletselectwheretogo

label fishinghamletdiscoveringscrap04:
    show fishinghamletscrap04 at basicfade
    $ fishinghamlet_areas_seen_04 = 1
    $ fishinghamlet_areas_seen += 1
    $ minutes += 2
    if not fishinghamlet_areas_seen_03:
        $ custom1 = "\n\nBeing by the bank of the brook, you look south, but find no human beings."
    else:
        $ custom1 = ""
    menu:
        'You tell {color=#f6d6bd}[horsename]{/color} to drink from the brook, and enter the narrow path. The building, which has a door leading outside of the palisade, is closed, and its roof has collapsed. On the ground, you find a wooden bowl, a mug, a spoon, and a fishing rod. All of them are rotten, broken, or swollen by rains and hoarfrosts.[custom1]
        '
        'I return to my horse.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my horse.')
            jump fishinghamletselectwheretogo

label fishinghamletdiscoveringscrap05:
    show fishinghamletscrap05 at basicfade
    $ fishinghamlet_areas_seen_05 = 1
    $ fishinghamlet_areas_seen += 1
    $ minutes += 5
    menu:
        'The farther north you go, the more the grass gets replaced by sand. You walk by dozens of rocks, many of which are much larger than you, or even two or three people standing on top of each other.
        \n\nThe land reaching from this point to the distant, steep cliff is desolate. One could bring here a treasure, bury it under any of those silent sentinels, then never find it again.
        '
        'I return to the gate.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the gate.')
            jump fishinghamletselectwheretogo

label fishinghamletdiscoveringscrap07:
    show fishinghamletscrap07 at basicfade
    $ fishinghamlet_areas_seen_07 = 1
    $ fishinghamlet_areas_seen += 1
    $ minutes += 5
    if fishinghamlet_areas_seen_01 and fishinghamlet_areas_seen_06 and fishinghamlet_areas_seen_07:
        $ quest_fisherhamlet_description05 = "I’ve been to the hamlet. I should return to {color=#f6d6bd}Thais{/color}."
        $ renpy.notify("Journal updated: The Old Hamlet")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
    if pc_sea_fluff:
        menu:
            'You walk by the small garden that carries a few bean plants and not many weeds. You leave {color=#f6d6bd}[horsename]{/color} behind and take a walk on the wooden logs of the massive bridge. They’re in much better shape than the other structures here, and the boat is almost new, still shining proudly from varnish.
            \n\nYou look back at the nearby building. While restoring all of the structures to their former functionality will be rough, there’s a lot to work with. {color=#f6d6bd}Thais{/color} would be pleased.
            '
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump fishinghamletselectwheretogo
    else:
        $ pc_sea_fluff = 1
        menu:
            'The sea here is not like the one from {color=#f6d6bd}Hovlavan’s{/color} port. The harbor and waters most people see during their busy days are full of life - ships, warehouses, traders, dockers. And of course, there’s Sickle, the barrier island that provides the city with its lagoon, but also serves as a home to dozens of species of birds, monkeys, and rodents. For most people, the sea is never silent.
            \n\nBut if one travels to Sickle and looks west, or embarks on a boat and sails away, there’s yet another view, a very different one. The never-ending blue, the emptiness, the humming waves, the monsters swimming to the surface just to take a breath, not even interested in the wooden vessels. Many say that if one jumps off a ship with a heavy stone, they will drown before they touch the seabed.
            \n\nHere, however, the water can’t be separated from the rocks that cut through it, like a swarm of mushrooms in a dark forest. Their shapes and sizes vary, but it’s their number that makes them unusual. If you were to name each one, you’d have to make up at least half of the names.
            '
            'I approach the harbor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the harbor.')
                menu:
                    'You walk by the small garden that carries a few bean plants and not many weeds. You leave {color=#f6d6bd}[horsename]{/color} behind and take a walk on the wooden logs of the massive bridge. They’re in much better shape than the other structures here, and the boat is almost new, still shining proudly from varnish.
                    \n\nYou look back at the nearby building. While restoring all of the structures to their former functionality will be rough, there’s a lot to work with. {color=#f6d6bd}Thais{/color} would be pleased.
                    '
                    'I go somewhere else.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                        jump fishinghamletselectwheretogo

label fishinghamlettakingabath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash myself in the ocean.')
    $ at_unlock_knowledge = 0
    $ minutes += 10
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    show plus1appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
    $ cleanliness = limit_cleanliness(1)
    menu:
        'You submerge yourself in the freezing water, floating above the sharp rocks and opposing the waves. The unpleasant touch of salt covering your skin will travel with you.
        '
        'I pack my things.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
            jump fishinghamletselectwheretogo

label fishinghamlet_driftwood01:
    $ at_unlock_knowledge = 0
    $ at = 0
    $ quarters += 1
    $ fishinghamlet_driftwood = 1
    $ item_driftwood += 1
    $ renpy.notify("You added the driftwood to your bag of ingredients.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the driftwood to your bag of ingredients.{/i}')
    menu:
        'You stay close to your mount, observing the disorder of rocks, dead plants, and animal remains that are coating the grasses. The pieces of wood, with their forgotten stories of foreign lands and sunk ships, are gathered in short stacks. You approach the largest pile, and push all the sticks, boughs, and branches aside, sparking displeased shouts of worms, crabs, and other beings that used to live among them.
        \n\nYou find the piece you were looking for, which is unlike the others. Not too thick, nor too long, and with a few little chunks of wood coming out of only one end, like a bunch of fingers. You nod with approval, reciting in your head a part of the withering dust recipe: {i}fuel with an ocean wood in the shape of a flower{/i}.
        '
        'I go to a different spot.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to a different spot.')
            jump fishinghamletselectwheretogo

label aegidia_crossbow01:
    $ aegidia_crossbow = 1
    $ minutes += 2
    menu:
        'You take off the linen sack that protects your weapon and prepare it for a shot. Then raise it to your eye, getting used to aiming. As you lower it, you feel confident.
        \n\nIf anything shows up, you’ll have the first shot.
        '
        'I go to a different spot.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to a different spot.')
            jump fishinghamletselectwheretogo
