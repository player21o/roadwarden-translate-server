###################### Ruined Village
default ruinedvillage_firsttime = 0
default ruinedvillage_truth = 0
default ruinedvillage_confront_can = 0
default ruinedvillage_name = "The Ruins" # Steep House
default ruinedvillage_arrivingdirection = 0

default ruinedvillage_curse_points = 0
default ruinedvillage_curse_block = 0
default ruinedvillage_curse_gone = 0
default ruinedvillage_curse_firsttime = 0

default ruinedvillage_explored = 0
default ruinedvillage_part_bottomentrance = 0
default ruinedvillage_part_bottomleftwing = 0
default ruinedvillage_part_bottomrightwing = 0
default ruinedvillage_part_clearing = 0
default ruinedvillage_part_leftentrance = 0
default ruinedvillage_part_topentranceinside = 0
default ruinedvillage_part_leftfield = 0
default ruinedvillage_part_leftwing = 0
default ruinedvillage_part_rightpasture = 0
default ruinedvillage_part_rightwing = 0
default ruinedvillage_part_river = 0
default ruinedvillage_part_square = 0
default ruinedvillage_part_topentrance = 0

default ruinedvillage_part_topentrance_UNLOCKED = 0
default ruinedvillage_part_topentrance_EXPLORED = 0
default ruinedvillage_part_topentrance_closerlook = 0

default ruinedvillage_part_topentranceinside_UNLOCKED = 0
default ruinedvillage_part_topentranceinside_EXPLORED = 0
default ruinedvillage_part_topentrance_actions = 0
default ruinedvillage_part_topentrance_tree = 0
default ruinedvillage_part_topentrance_well = 0
default ruinedvillage_part_topentrance_gate_open = 0
default ruinedvillage_part_topentrance_gate_quickclose = 0

default ruinedvillage_tools = 0

default ruinedvillage_part_clearing_UNLOCKED = 0
default ruinedvillage_part_clearing_EXPLORED = 0

default ruinedvillage_part_river_UNLOCKED = 0
default ruinedvillage_part_river_EXPLORED = 0

default ruinedvillage_part_leftwing_UNLOCKED = 0
default ruinedvillage_part_leftwing_EXPLORED = 0

default ruinedvillage_part_rightwing_UNLOCKED = 0
default ruinedvillage_part_rightwing_EXPLORED = 0

default ruinedvillage_part_leftentrance_UNLOCKED = 0
default ruinedvillage_part_leftentrance_EXPLORED = 0

default ruinedvillage_part_square_UNLOCKED = 0
default ruinedvillage_part_square_EXPLORED = 0

default ruinedvillage_part_bottomleftwing_UNLOCKED = 0
default ruinedvillage_part_bottomleftwing_EXPLORED = 0
default ruinedvillage_fishtrap_found = 0

default ruinedvillage_part_bottomrightwing_UNLOCKED = 0
default ruinedvillage_part_bottomrightwing_EXPLORED = 0
default ruinedvillage_quarrel = 0

default ruinedvillage_part_leftfield_UNLOCKED = 0
default ruinedvillage_part_leftfield_EXPLORED = 0 # 2 = pc knows about the curse
default ruinedvillage_part_leftfieldtakencursedsoil = 0

default ruinedvillage_part_rightpasture_UNLOCKED = 0
default ruinedvillage_part_rightpasture_EXPLORED = 0

default ruinedvillage_part_bottomentrance_UNLOCKED = 0
default ruinedvillage_part_bottomentrance_EXPLORED = 0
default ruinedvillage_part_bottomentranceactions = 0
default ruinedvillage_part_bottomentrancelookingatbuilding = 0
default ruinedvillage_part_bottomentrancelookingatgate = 0

default ruinedvillage_treasure = 0
default ruinedvillage_treasure_known = 0
default ruinedvillage_treasure_diggingout = 0

default ruinedvillage_clues = 0
default ruinedvillage_goblinlair_EXPLORED = 0
default ruinedvillage_goblinlair_nose = 0
default ruinedvillage_goblinlair_clue = 0

default ruinedvillage_fishtrap = 0
default ruinedvillage_fishtrap_working = 0
default ruinedvillage_fishtrap_daychecked = 0
default ruinedvillage_fishtrap_fishtimer = 0
default ruinedvillage_fishtrap_badthingmodifier = 0

label ruinedvillage01:
    $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout= 1.0, fadein= 1.0, if_changed=True)
    stop nature fadeout 4.0
    nvl clear
    label pyrrhos_ruinedvillage_fluffloop:
        if description_pyrrhos01:
            $ pyrrhos_ruinedvillage_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is detaching a scrap of metal from an old cask. Without stopping his work, he asks what you need.', '{color=#f6d6bd}Pyrrhos{/color} is looking for something inside his tent. He crawls out quickly. “Greetings, roadster. Almost didn’t hear ye.”', '{color=#f6d6bd}Pyrrhos{/color} is scratching a stain off his shirt. “Ah, are we leaving?”', '{color=#f6d6bd}Pyrrhos{/color} is lying inside his tent, and crawls out after you clear your throat. “Roadster! What do ye need?”'])
        else:
            $ pyrrhos_ruinedvillage_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is detaching a scrap of metal from an old cask. Without stopping his work, he asks what you need.', '{color=#f6d6bd}The scavenger{/color} is looking for something inside his tent. He crawls out quickly. “Greetings, roadster. Almost didn’t hear ye.”', '{color=#f6d6bd}The scavenger{/color} is scratching a stain off his shirt. “Ah, are we leaving?”', '{color=#f6d6bd}The scavenger{/color} is lying inside his tent, and crawls out after you clear your throat. “Roadster! What do ye need?”'])
        if pyrrhos_ruinedvillage_fluff_old == pyrrhos_ruinedvillage_fluff:
            jump pyrrhos_ruinedvillage_fluffloop
        else:
            $ pyrrhos_ruinedvillage_fluff_old = pyrrhos_ruinedvillage_fluff
    ######
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_topentranceinside == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentranceinside 02 at basicfade
        else:
            show ruinedvillage_part_topentranceinside 01 at basicfade
    if ruinedvillage_part_clearing == 1:
        show ruinedvillage_part_clearing 01 at basicfade
    if ruinedvillage_part_river == 1:
        show ruinedvillage_part_river 01 behind fishtrap at basicfade
    if ruinedvillage_part_leftentrance == 1:
        show ruinedvillage_part_leftentrance 01 at basicfade
    if ruinedvillage_part_leftwing == 1:
        show ruinedvillage_part_leftwing 01 at basicfade
    if ruinedvillage_part_rightwing == 1:
        show ruinedvillage_part_rightwing 01 at basicfade
    if ruinedvillage_part_square == 1:
        show ruinedvillage_part_square 01 at basicfade
    if ruinedvillage_part_bottomleftwing == 1:
        show ruinedvillage_part_bottomleftwing 01 at basicfade
    if ruinedvillage_part_bottomrightwing == 1:
        show ruinedvillage_part_bottomrightwing 01 at basicfade
    if ruinedvillage_part_leftfield == 1:
        show ruinedvillage_part_leftfield 01 at basicfade
    if ruinedvillage_part_rightpasture == 1:
        show ruinedvillage_part_rightpasture 01 at basicfade
    if ruinedvillage_part_bottomentrance == 1:
        show ruinedvillage_part_bottomentrance 01 at basicfade
    if ruinedvillage_fishtrap:
        show fishtrap ruinedvillage01 at basicfade
    ######
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not ruinedvillage_firsttime:
        $ ruinedvillage_firsttime = 1
        $ world_known_areas += 1
        if ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
            $ pyrrhos_quest_tohowlersdell = 1
        if ruinedvillage_arrivingdirection == "north":
            jump ruinedvillage01topentrancefirsttime
        else:
            jump ruinedvillage01bottomentrancefirsttime
    if ruinedvillage_arrivingdirection == "north":
        jump ruinedvillage01topentrancearrival
    else:
        jump ruinedvillage01bottomentrancearrival

label ruinedvillage01topentrancefirsttime:
    $ ruinedvillage_part_topentrance = 1
    $ ruinedvillage_part_topentrance_EXPLORED = 1
    $ ruinedvillage_part_topentrance_UNLOCKED = 1
    $ ruinedvillage_part_clearing_UNLOCKED = 1
    $ ruinedvillage_part_river_UNLOCKED = 1
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    $ quest_ruins = 1
    $ renpy.notify("New entry: The Ruined Village")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Ruined Village{/i}')
    $ quest_explorepeninsula_description09 = "The abandoned village in the South may be a useful spot for future settlers. I should figure out why it was ruined."
    if not ruinedvillage_part_river_EXPLORED:
        $ custom1 = "\n\nYou hear a river in the east, separated by the lush meadow, filled with crickets and rodents."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_clearing_EXPLORED:
        $ custom2 = "\n\nThere are many tree stumps around you, especially in the west, covered with moss and fungi."
    else:
        $ custom2 = ""
    menu:
        'Standing in front of the gate, you hear no voices, no tools at work, no steps. Dozens of birds live among the collapsed roofs. Their fluttering, singing, and squawking is free of worries.
        \n\nIf you want to travel any further, you need to ride around the palisade. Searching the ruins may take a lot of time.[custom1][custom2]
        '
        'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_topentrance_closerlook = 1
            jump ruinedvillage01topentrance02
        'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
            jump ruinedvillage01topentrance03
        'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
            pass
        'I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

    label ruinedvillage01topentrance02:
        menu:
            'Pushed or pulled, it doesn’t move an inch. Someone has spread dirt and rocks both underneath it and around it, seemingly to keep the planks stuck in the ground.
            '
            'I want to open it.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open it.')
                jump ruinedvillage01topentrance03
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03:
        if not ruinedvillage_part_topentrance_EXPLORED or not ruinedvillage_part_topentranceinside_EXPLORED:
            jump ruinedvillage01topentrance03cant
        if ruinedvillage_tools:
            jump ruinedvillage01topentrance03b
        menu:
            'It may take a couple of hours, especially without proper tools to help you remove all the ground and rocks.
            '
            'I do it anyway.' ( condition="pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do it anyway.')
                $ quarters += 10
                jump ruinedvillage01topentrancegateopeningwithoutools
            'I’m too tired to take care of it now. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03cant:
        menu:
            'You should take a look at the other side to be sure it’s even possible, especially since it may take a couple of hours without proper tools.
            '
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03b:
        menu:
            'It may take quite a bit of time, but with the wooden and bone tools you found in one of the buildings you’ll speed up your endeavor.
            '
            'I collect the tools and get to work.' ( condition="pc_hp" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect the tools and get to work.')
                $ quarters += 2
                jump ruinedvillage01topentrancegateopeningwithtools
            'I’m too tired to take care of it now. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

label ruinedvillage01topentrancegateopeningwithoutools:
    $ ruinedvillage_part_topentrance_gate_open = 1
    $ ruinedvillage_part_topentrance_actions += 1
    $ ruinedvillage_part_topentrance_EXPLORED = 2
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 2
    show ruinedvillage_part_topentrance 02 at basicfade
    show ruinedvillage_part_topentranceinside 02 at basicfade
    $ cleanliness = limit_cleanliness(cleanliness-2)
    show minus2appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
    menu:
        'You take off your cloak and put away your bags and satchels, while {color=#f6d6bd}[horsename]{/color} grazes gladly in the meadow. After looking at the pile of dirt, you let out a sigh.
        \n\nYou start with the larger rocks, removing the ground around them and pushing them into a single pile. Then you do the same on the other side. The real problem is the soil - you keep kneeling and bending forward to move away the larger clods. It goes on for a long time, and once you’re done, your back hurts a bit.
        \n\nFrom now on, passing through this place will take you less time.
        '
        'I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

label ruinedvillage01topentrancegateopeningwithtools:
    $ ruinedvillage_part_topentrance_gate_open = 1
    $ ruinedvillage_part_topentrance_EXPLORED = 2
    $ ruinedvillage_part_topentrance_actions += 1
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    show ruinedvillage_part_topentrance 02 at basicfade
    show ruinedvillage_part_topentranceinside 02 at basicfade
    $ cleanliness = limit_cleanliness(cleanliness-1)
    show minus1appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
    menu:
        'You take off your cloak and put away your bags and satchels, while {color=#f6d6bd}[horsename]{/color} grazes gladly in the meadow. After looking at the pile of dirt, you let out a sigh.
        \n\nYou start with the larger rocks, removing the ground around them and pushing them into a single pile. Then you do the same on the other side. The simple shovel and pitchfork help you a lot and once you get used to them, the work goes smoothly. You’re done before you get too tired.
        \n\nFrom now on, passing through this place will take you less time.
        '
        'I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

label ruinedvillage01topentrancearrival:
    if not ruinedvillage_part_topentrance_EXPLORED:
        jump ruinedvillage01topentrance01
    $ ruinedvillage_part_topentrance = 1
    if ruinedvillage_part_topentrance_EXPLORED < 2:
        $ ruinedvillage_part_topentrance_EXPLORED = 1
    $ ruinedvillage_part_topentrance_UNLOCKED = 1
    $ ruinedvillage_part_clearing_UNLOCKED = 1
    $ ruinedvillage_part_river_UNLOCKED = 1
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    $ ruinedvillage_part_topentrance = 1
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    if ruinedvillage_part_bottomentrance_EXPLORED and ruinedvillage_part_bottomleftwing_EXPLORED == 2 and ruinedvillage_part_bottomrightwing_EXPLORED == 2 and ruinedvillage_part_clearing_EXPLORED == 2 and ruinedvillage_part_leftentrance_EXPLORED == 2 and ruinedvillage_part_topentranceinside_EXPLORED and ruinedvillage_part_leftfield_EXPLORED and ruinedvillage_part_leftwing_EXPLORED == 2 and ruinedvillage_part_rightpasture_EXPLORED == 2 and ruinedvillage_part_rightwing_EXPLORED == 2 and ruinedvillage_part_river_EXPLORED == 2 and ruinedvillage_part_square_EXPLORED == 2 and ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_explored:
        $ ruinedvillage_explored = 1
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if pc_class == "scholar" and ruinedvillage_part_leftfield_EXPLORED == 2 and not ruinedvillage_part_leftfieldtakencursedsoil and not item_cursedsoil:
        $ at_unlock_knowledge = 1
        $ at = 0
    else:
        $ at_unlock_knowledge = 0
        $ at = 0
    if ruinedvillage_part_river_EXPLORED and ruinedvillage_part_clearing_EXPLORED:
        menu:
            'The village remains dead.
            '
            'I consider washing myself in the river.' if ruinedvillage_part_river_EXPLORED:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillagebath01
            'I pick up the fish trap from the ruined building.' if not item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the fish trap from the ruined building.')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ ruinedvillage_fishtrap_found = 1
                $ item_fishtrap += 1
                $ renpy.notify("You picked up a fish trap.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up a fish trap{/i}')
                jump ruinedvillageselectarea
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters <= (world_daylength-8) and ruinedvillage_part_river" ):
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap01
            'It’s already dark. Setting up a fish trap in the river right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters > (world_daylength-8) and ruinedvillage_part_river" ):
                pass
            'Let’s see if the fish trap had any luck.' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked != day and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked == day and ruinedvillage_part_river:
                pass
            'I set the fish trap again.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap03
            'I take the fish trap back.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and not item_fishtrap and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and item_fishtrap and ruinedvillage_part_river:
                pass
            ################
            'I enter the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and not ruinedvillage_goblinlair_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair01
            'I return to the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and ruinedvillage_goblinlair_EXPLORED and not ruinedvillage_goblinlair_clue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair02
            ################
            'I return to the scavenger’s camp.' if (ruinedvillage_curse_gone and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the scavenger’s camp.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01scavengerscamp01
            ################
            'I go to the road leading north from the village.' if ruinedvillage_part_topentrance_UNLOCKED == 1 and not ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the road leading north from the village.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentrance01
            ################
            'I want to look around the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the northern gate.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01
            'I return to the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01explored
            ################
            'I inspect the clearing in the west.' if ruinedvillage_part_clearing_UNLOCKED == 1 and not ruinedvillage_part_clearing_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the clearing in the west')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftclearing01
            ################
            'I head to the river.' if ruinedvillage_part_river_UNLOCKED == 1 and not ruinedvillage_part_river_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the river.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01river01
            ################
            'I inspect the palisade in the west.' if ruinedvillage_part_leftentrance_UNLOCKED == 1 and not ruinedvillage_part_leftentrance_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the palisade in the west.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftentrance01
            ################
            'I explore the northwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftwing01
            ################
            'I explore the northeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED):
                $ minutes += 7
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northeast part of the village.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightwing01
            ################
            'I go to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED):
                $ minutes += 5
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01
            'I return to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01explored
            ################
            'I explore the southwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomleftwing01
            ################
            'I explore the southeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southeast part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomrightwing01
            ################
            'I inspect the fields in the southwest.' if ruinedvillage_part_leftfield_UNLOCKED == 1 and not ruinedvillage_part_leftfield_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the fields in the southwest.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01
            'I return to the barren fields in the southwest.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the barren fields in the southwest.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01explored
            'I shove some of the cursed soil into a jar. It’s a valuable ingredient.' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shove some of the cursed soil into a jar. It’s a valuable ingredient.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01takingthecursedsoil
            ################
            'I inspect the pasture in the southeast.' if ruinedvillage_part_rightpasture_UNLOCKED == 1 and not ruinedvillage_part_rightpasture_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the pasture in the southeast.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightpasture01
            ###############
            'I want to look around the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and not ruinedvillage_part_bottomentrance_EXPLORED:
                $ minutes += 6
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01
            'I return to the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and ruinedvillage_part_bottomentrance_EXPLORED == 1:
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01explored
            ################
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            'I need to see what’s on the other side of the northern gate if I want to open it. (disabled)' if (ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            ###############
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_leftfield_EXPLORED < 2) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_clue) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_EXPLORED < 2):
                pass
            ###############
            'I saw a fish trap in the ruined building, but I won’t be able to fit another one in the saddle. (disabled)' if item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                pass
            'The river would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ruinedvillage_fishtrap and ruinedvillage_part_river:
                pass
    else:
        if not ruinedvillage_part_river_EXPLORED:
            $ custom1 = "\n\nYou hear a river in the east, separated by the lush meadow, filled with crickets and rodents."
        else:
            $ custom1 = ""
        if not ruinedvillage_part_clearing_EXPLORED:
            $ custom2 = "\n\nThere are many tree stumps around you, especially in the west, covered with moss and fungi."
        else:
            $ custom2 = ""
        menu:
            'The village remains dead. [custom1][custom2]
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

label ruinedvillage01topentrance01:
    $ ruinedvillage_part_topentrance = 1
    $ ruinedvillage_part_topentrance_EXPLORED = 1
    $ ruinedvillage_part_topentrance_UNLOCKED = 1
    $ ruinedvillage_part_clearing_UNLOCKED = 1
    $ ruinedvillage_part_river_UNLOCKED = 1
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    if not ruinedvillage_part_river_EXPLORED:
        $ custom1 = "\n\nYou hear a river in the east, separated by the lush meadow, filled with crickets and rodents."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_clearing_EXPLORED:
        $ custom2 = "\n\nThere are many tree stumps around you, especially in the west, covered with moss and fungi."
    else:
        $ custom2 = ""
    menu:
        'You’re at the closed, northern gate. The neglected road is partially overgrown.[custom1][custom2]
        '
        'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_topentrance_closerlook = 1
            jump ruinedvillage01topentrance02
        'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
            jump ruinedvillage01topentrance03
        'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
            pass
        'I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

label ruinedvillage01topentrance01explored:
    if not ruinedvillage_part_river_EXPLORED:
        $ custom1 = "\n\nYou hear a river in the east, separated by the lush meadow, filled with crickets and rodents."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_clearing_EXPLORED:
        $ custom2 = "\n\nThere are many tree stumps around you, especially in the west, covered with moss and fungi."
    else:
        $ custom2 = ""
    menu:
        'You’re at the northern gate. [custom1][custom2]
        '
        'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_topentrance_closerlook = 1
            jump ruinedvillage01topentrance02
        'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
            jump ruinedvillage01topentrance03
        'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
            pass
        'I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

############################################################

label ruinedvillage01topentranceinsideALL:
    label ruinedvillage01topentranceinside01:
        $ ruinedvillage_part_topentranceinside = 1
        $ ruinedvillage_part_topentranceinside_EXPLORED = 1
        $ ruinedvillage_part_leftwing_UNLOCKED = 1
        $ ruinedvillage_part_rightwing_UNLOCKED = 1
        if ruinedvillage_part_topentranceinside == 1:
            if ruinedvillage_part_topentrance_gate_open:
                show ruinedvillage_part_topentranceinside 02 at basicfade
            else:
                show ruinedvillage_part_topentranceinside 01 at basicfade
        if not ruinedvillage_part_square_EXPLORED:
            $ custom1 = ", while the path south leads to the main square"
        else:
            $ custom1 = ""
        menu:
            'The paths here have almost been reclaimed by grasses.
            \n\nTo your east and west you see shadowy alleys behind damaged buildings[custom1].
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03inside
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentranceinside02: #tree
        $ ruinedvillage_clues += 1
        $ quest_ruins_insideclues08 = "I found a quince tree that was partially burnt by a torch."
        if quest_ruins == 1:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            'You don’t find anything worth picking. The half-dead quinces have maggots crawling under their skins. You wonder which part of this meal is more tempting for the dark-winged birds sitting among the branches - the flesh of the fruits, or of the worms.
            \n\nQuinces are rarely eaten without having a chance to blet. You can safely guess that they were meant to be dried, or to add taste to cookies or hard drinks.
            \n\nAfter a few moments, you realize that the bottom part of the tree, just above the ground, is partially charred. Someone must have apposed a torch here, but the wet wood didn’t burst into flames.
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03inside
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentranceinside03: #well
        menu:
            'It’s filled up with soil, and you find nothing interesting about the area around it.
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03inside
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance02inside:
        menu:
            'Pushed or pulled, it doesn’t move an inch. Someone has spread dirt and rocks both underneath it and around it, seemingly to keep the planks stuck in the ground.
            '
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03inside
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentranceinside01explored:
        menu:
            'You approach the northern gate. It’s currently closed.
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03inside
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03inside:
        if not ruinedvillage_part_topentrance_EXPLORED or not ruinedvillage_part_topentranceinside_EXPLORED:
            jump ruinedvillage01topentrance03cantinside
        if ruinedvillage_tools:
            jump ruinedvillage01topentrance03binside
        menu:
            'It may take a couple of hours, especially without proper tools to help you remove all the ground and rocks.
            '
            'I do it anyway.' ( condition="pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do it anyway.')
                $ quarters += 10
                jump ruinedvillage01topentrancegateopeningwithoutools
            'I’m too tired to take care of it now. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                pass
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03cantinside:
        menu:
            'You should take a look at the other side to be sure it’s even possible, especially since it may take a couple of hours without proper tools.
            '
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

    label ruinedvillage01topentrance03binside:
        menu:
            'It may take quite a bit of time, but with the wooden and bone tools you found in one of the buildings you’ll speed up your endeavor.
            '
            'I collect the tools and get to work.' ( condition="pc_hp" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect the tools and get to work.')
                $ quarters += 2
                jump ruinedvillage01topentrancegateopeningwithtools
            'I’m too tired to take care of it now. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                pass
            'I take a closer look at the gate.' if not ruinedvillage_part_topentrance_closerlook and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_topentrance_closerlook = 1
                jump ruinedvillage01topentrance02inside
            'I approach the nearby tree.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_tree) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_tree):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nearby tree.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_tree = 1
                jump ruinedvillage01topentranceinside02
            'I look into the well.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_well) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_well):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the well.')
                $ ruinedvillage_part_topentrance_actions += 1
                if ruinedvillage_part_topentrance_actions >= 2:
                    $ ruinedvillage_part_topentranceinside_EXPLORED = 2
                    if not ruinedvillage_curse_gone:
                        $ ruinedvillage_curse_points += 1
                $ ruinedvillage_part_topentrance_well = 1
                jump ruinedvillage01topentranceinside03
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if not ruinedvillage_curse_gone and ruinedvillage_curse_block:
                pass
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

####################################

label ruinedvillage01leftclearing01:
    $ ruinedvillage_part_clearing = 1
    $ ruinedvillage_part_clearing_EXPLORED = 2
    $ ruinedvillage_part_topentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftentrance_UNLOCKED = 1
    show ruinedvillage_part_clearing 01 at basicfade
    $ ruinedvillage_clues += 1
    $ quest_ruins_insideclues02 = "The nearby clearing was massive, large enough to provoke the wrath of the herds."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    if not ruinedvillage_part_leftentrance_EXPLORED:
        $ custom1 = "In the south, you see a path leading around the palisade."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_topentrance_EXPLORED:
        $ custom2 = "In the east, you see a road leading north."
    else:
        $ custom2 = ""
    menu:
        'The meadow is lush and colorful, and so dense it’s unsafe for a rider. For a couple of minutes you lead {color=#f6d6bd}[horsename]{/color} with a rope, avoiding the potential disaster in case of a hoof falling into an animal den. Being forced to travel around the palisade every time you get here is going to be a pain.
        \n\nMost of the tree trunks look similar and have a comparable size. They were most likely planted with the sole purpose of being cut down and used by the locals, though cutting so many trees at once... That alone could provoke the wrath of the herds. Such a process should be spread across a couple of seasons, and you can’t be sure that was the case.
        \n\nIn the west and north the clearing turns into a wild forest. [custom1][custom2]
        '
        'I leave the clearing.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the clearing.')
            jump ruinedvillageselectarea

label ruinedvillage01river01:
    $ ruinedvillage_part_river = 1
    $ ruinedvillage_part_river_EXPLORED = 2
    show ruinedvillage_part_river 01 behind fishtrap at basicfade
    $ ruinedvillage_clues += 1
    $ quest_ruins_insideclues07 = "A wooden wagon and a set of tools were thrown into a river, all right next to each other."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    menu:
        'You see a quenching family of boars, some of them brown, some black. You consider turning back, but they pay you little attention. After a couple of grunts, they run north.
        \n\nThe river is not too wide, yet unusually deep, with banks altered by the locals for decades, if not centuries. The water is cold and clean, yet filled with long plants growing from the bottom. You would rather avoid jumping inside or drinking from it, but you’re tempted to at least wash your face, neck, and hands. Dozens, if not hundreds of small fish are looking for tasty leaves, but also try to avoid their predators. A dance of life, completely unaware of your presence.
        \n\nYou suddenly realize there’s something else buried among the kelp. A rusty sickle sticking out of the ground, a couple of stone axes and hoes. The wooden handles and a large wagon are covered with moss, but you recognize their shapes. Why would someone drop them here?
        \n\nOn the opposite bank, the meadow turns into a thick forest, impenetrable for a rider.
        '
        'I turn back.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back.')
            jump ruinedvillageselectarea

label ruinedvillage01leftentrance01:
    $ ruinedvillage_part_leftentrance = 1
    $ ruinedvillage_part_leftentrance_EXPLORED = 2
    $ ruinedvillage_part_clearing_UNLOCKED = 1
    $ ruinedvillage_part_leftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_square_UNLOCKED = 1
    $ ruinedvillage_part_leftfield_UNLOCKED = 1
    show ruinedvillage_part_leftentrance 01 at basicfade
    if not ruinedvillage_part_clearing_EXPLORED:
        $ custom1 = "The grasses in the north surround dozens of tree stumps, already covered with moss and fungi."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_leftfield_EXPLORED:
        $ custom2 = ""
    else:
        $ custom2 = "\n\nGoing south, you’ll reach a large field, though you don’t see any crops."
    menu:
        'The tracks of human footwear and many, many more ape footprints cover the path formed around the palisade’s breach. As far as you can tell, the freshest footprints lead to the village.
        \n\nThe wooden stakes spread on the ground are rotten, covered in mushrooms, small flowers, insects, and worms. A good source of animal or goblin food, though you’d expect them to also hunt for the birds and eggs.
        \n\nThe meadow in the west turns into a forest quickly. [custom1][custom2]
        '
        'I shouldn’t enter the forest, especially not in this area. It’s unpredictable.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            jump ruinedvillageselectarea

label ruinedvillage01leftwing01:
    $ ruinedvillage_part_leftwing = 1
    $ ruinedvillage_part_leftwing_EXPLORED = 2
    $ ruinedvillage_part_topentranceinside_UNLOCKED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_square_UNLOCKED = 1
    show ruinedvillage_part_leftwing 01 at basicfade
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    menu:
        'The colorful grass covers the entire fenced pasture. The large stone placed in the middle suggests it could be a playground for ibexes, or maybe it’s just an old garden.
        \n\nYou see a couple of small sheds, a latrine, and a single building to the south, completely burnt down. All of these places were cleaned out by scavengers.
        \n\n{color=#f6d6bd}[horsename]{/color} doesn’t want to approach the large ruins in the north. The terrible stench of feces and rotting food scares you off as well. The paths are covered with goblin footprints.
        \n\nIt’s daytime, so the pack should be asleep. If the beasts were active, they would try to scare you off, or to hunt down your mount. This is their territory, and once they wake up, you will face a furious enemy.
        '
        'I go somewhere else. Quietly.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else. Quietly.')
            jump ruinedvillageselectarea

label ruinedvillage01rightwing01:
    $ ruinedvillage_part_rightwing = 1
    $ ruinedvillage_part_rightwing_EXPLORED = 2
    $ ruinedvillage_part_topentranceinside_UNLOCKED = 1
    $ ruinedvillage_part_bottomrightwing_UNLOCKED = 1
    $ ruinedvillage_part_square_UNLOCKED = 1
    $ ruinedvillage_tools = 1
    show ruinedvillage_part_rightwing 01 at basicfade
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    menu:
        'The debris was partially moved outside of the destroyed houses, but you find nothing of value. The table, cupboards, shelves, and bits and pieces were carefully ransacked. The wildly growing vegetables and herbs are the only remnants of the abandoned gardens.
        \n\nYou spot fresh human footprints at the entrance to the latrine, most of which lead to and from the center of the village.
        \n\nYou notice a set of simple tools leaned against a pile of rubble. A wooden spade and a shovel, a pointed stick, a hoe with a bone head, a stone axe... All of them are too old and too awkward to bother with transporting them around, but you’ll know where to find them if you need them in the future.
        '
        'Good to know.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Good to know.')
            jump ruinedvillageselectarea

label ruinedvillage01square01:
    $ ruinedvillage_clues += 1
    $ ruinedvillage_part_square = 1
    $ ruinedvillage_part_square_EXPLORED = 1
    $ ruinedvillage_part_topentranceinside_UNLOCKED = 1
    $ ruinedvillage_part_leftwing_UNLOCKED = 1
    $ ruinedvillage_part_rightwing_UNLOCKED = 1
    $ ruinedvillagepartlefentrance_UNLOCKED = 1
    $ ruinedvillage_part_bottomrightwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    show ruinedvillage_part_square 01 at basicfade
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    if ruinedvillage_curse_gone:
        $ custom1 = ""
    elif not ruinedvillage_curse_points:
        $ custom1 = ""
    elif ruinedvillage_curse_points == 1:
        $ custom1 = "You feel a slight aching in your stomach."
    elif ruinedvillage_curse_points == 2:
        $ custom1 = "Your stomach makes you let out a painful groan."
    # elif ruinedvillage_curse_points == 3:
    #     $ custom1 = "You stop and touch your aching stomach."
    elif ruinedvillage_curse_points == 3:
        $ custom1 = "You stop and touch your aching stomach."#"The closer you are to the village, the more you want to vomit."
    else:
        $ custom1 = "The pain in your stomach slows you down."
    $ quest_ruins_insideclues05 = "While the village used to be small, it was also unusually wealthy."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    if day <= pyrrhos_deathcounter_unmet:
        menu:
            'In every village, the main square is the fanciest area, meant to charm the travelers. Yet this is way more than you expected - the houses are as big as in {color=#f6d6bd}Hovlavan{/color}, and the paved ground took a lot of work and materials. The walls, now charred and riddled with holes, are made of an expensive, coated wattle. The tiles for the roofs also had to be brought here from a different settlement.
            \n\nYou peek inside the three smaller buildings, the rotting remains of their former splendor. The birds living in dozens of nests respond to your arrival with quite a commotion. You don’t find even a single dragon bone, nor a tool or a piece of furniture left unbroken, or unrotten. You’re surrounded by bad smells, dirt, animal droppings, and garbage.
            \n\nThe well also stinks. It has no bucket, but you’d be afraid to use it anyway. Who knows how many birds have relieved themselves inside, or how many old rats have found their death while climbing up the walls?
            \n\nSuddenly, you hear some sounds coming from the largest building. [custom1]
            '
            'I should check it out. I prepare my axe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should check it out. I prepare my axe.')
                $ ruinedvillage_part_square_EXPLORED = 2
                $ ruinedvillage_camp_UNLOCKED = 1
                jump ruinedvillage01scavengerscamp01firsttime
            'I should walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should walk away.')
                jump ruinedvillageselectarea
    else:
        menu:
            'In every village, the main square is the fanciest area, meant to charm the travelers. Yet this is way more than you expected - the houses are as big as in {color=#f6d6bd}Hovlavan{/color}, and the paved ground took a lot of work and materials. The walls, now charred and riddled with holes, are made of an expensive, coated wattle. The tiles for the roofs also had to be brought here from a different settlement.
            \n\nYou peek inside the three smaller buildings, the rotting remains of their former splendor. The birds living in dozens of nests respond to your arrival with quite a commotion. You don’t find even a single dragon bone, nor a tool or a piece of furniture left unbroken, or unrotten. You’re surrounded by bad smells, dirt, animal droppings, and garbage.
            \n\nThe well also stinks. It has no bucket, but you’d be afraid to use it anyway. Who knows how many birds have relieved themselves inside, or how many old rats have found their death while climbing up the walls?
            \n\nSuddenly, you notice the stains of blood at the entrance to the largest building. [custom1]
            '
            'I should check it out. I prepare my axe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should check it out. I prepare my axe.')
                $ ruinedvillage_part_square_EXPLORED = 2
                $ ruinedvillage_camp_UNLOCKED = 1
                jump ruinedvillage01scavengerscamp01firsttimedead
            'I should walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should walk away.')
                jump ruinedvillageselectarea

label ruinedvillage01square01explored:
    menu:
        'You’ve returned to the village, welcomed by the annoyed squawks of the nearby birds. You’re almost sure something hides inside the largest building.
        '
        'I should check it out. I prepare my axe.' if day <= pyrrhos_deathcounter_unmet:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should check it out. I prepare my axe.')
            $ ruinedvillage_part_square_EXPLORED = 2
            $ ruinedvillage_camp_UNLOCKED = 1
            jump ruinedvillage01scavengerscamp01firsttime
        'I should check it out. I prepare my axe.' if day > pyrrhos_deathcounter_unmet:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should check it out. I prepare my axe.')
            $ ruinedvillage_part_square_EXPLORED = 2
            $ ruinedvillage_camp_UNLOCKED = 1
            jump ruinedvillage01scavengerscamp01firsttimedead
        'I should go away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should go away.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomleftwing01:
    $ ruinedvillage_part_bottomleftwing = 1
    $ ruinedvillage_part_bottomleftwing_EXPLORED = 2
    $ ruinedvillage_part_leftentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomrightwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_square_UNLOCKED = 1
    $ ruinedvillage_clues += 1
    $ quest_ruins_insideclues03 = "I found many marks left by large animal claws on various building entrances."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    show ruinedvillage_part_bottomleftwing 01 at basicfade
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    menu:
        'The buildings, some of which have collapsed, are made of wood, now charred and rotten. You spot claw marks on the walls, especially close to the doors and window frames. They could belong to a dragonling, or a large wolf, larger than the gray ones. Or a corpse eater... Too many options to make a guess.
        '
        'Yet no beast remains in sight.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yet no beast remains in sight.')
            menu:
                'You find the remains of clothes, furniture, odds and ends. Only one object seems to be of use - a basket-like fish trap made of vines and willow branches. If a large fish swims into it, it won’t be able to get out on its own.
                '
                'It’s quite large, but I can fit it on my saddle.' if not item_fishtrap:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s quite large, but I can fit it on my saddle.')
                    $ ruinedvillage_fishtrap_found = 1
                    $ item_fishtrap += 1
                    $ renpy.notify("You picked up a fish trap.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up a fish trap{/i}')
                    jump ruinedvillageselectarea
                'I won’t be able to fit another trap in the saddle. I’ll leave it for later.' if item_fishtrap:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I won’t be able to fit another trap in the saddle. I’ll leave it for later.')
                    jump ruinedvillageselectarea

label ruinedvillage01bottomrightwing01:
    $ ruinedvillage_part_bottomrightwing = 1
    $ ruinedvillage_part_bottomrightwing_EXPLORED = 2
    $ ruinedvillage_part_rightwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_square_UNLOCKED = 1
    show ruinedvillage_part_bottomrightwing 01 at basicfade
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    menu:
        'You find a small backyard. The ground is beaten, the grass grows only right next to the buildings. It would have been a fair spot for training dancers and fighters.
        \n\nThe stakes of the palisade are covered with playful carvings, left by children who were portraying monsters, weapons, and humans.
        \n\nThe rubble has been pushed into the corners of the houses. The furniture is broken, but you find something of use in one of the piles - a slightly rusty piece of steel. Once you pull it out, you realize it’s a quarrel for a crossbow. Still usable.
        '
        'It won’t be difficult to find a use for it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It won’t be difficult to find a use for it.')
            $ ruinedvillage_quarrel = 1
            $ item_crossbowquarrels += 1
            $ renpy.notify("You picked up a quarrel.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up a quarrel.{/i}')
            jump ruinedvillageselectarea

label ruinedvillage01leftfield01:
    $ ruinedvillage_part_leftfield = 1
    $ ruinedvillage_part_leftfield_EXPLORED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftentrance_UNLOCKED = 1
    show ruinedvillage_part_leftfield 01 at basicfade
    $ at = 0
    if pc_class == "mage":
        $ at_unlock_spell = 1
        $ manacost = 1
        $ custom1 = ""
    else:
        $ custom1 = "You’d need a mage to either confirm, or dismiss this idea."
    if not ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points += 1
    if not ruinedvillage_part_leftentrance_EXPLORED:
        $ custom1 = "\n\nIn the north, you see a path leading around the palisade."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_bottomentrance_EXPLORED:
        $ custom2 = "\n\nEast from here there’s an abandoned building and a road leading south."
    else:
        $ custom2 = ""
    menu:
        'You’re surrounded by what looks like a field plowed in late autumn, disturbed by hundreds of rains and snow falls. There’s a few clumps of grass and wheat, but a place like this one, abandoned for years, should already have turned itself into a green lea.
        \n\nA barren field? Maybe it was overused, but you would still expect the weeds to sprout. A curse?
        \n\nThe path leading west from here ends at the edge of the field, shifting into a meadow, then a forest. [custom1][custom2]
        '
        'I use my amulets to sense if there’s pneuma buried in this place. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my amulets to sense if there’s a pneuma buried in this place.')
            $ ruinedvillage_part_leftfield_EXPLORED = 2
            $ at_unlock_spell = 0
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            if not ruinedvillage_curse_gone:
                $ ruinedvillage_curse_points += 1
            jump ruinedvillage01leftfield02
        'I use the weird sapling to sense if there’s pneuma buried in this place.' if item_magicalsapling:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the weird sapling to sense if there’s a pneuma buried in this place.')
            $ ruinedvillage_part_leftfield_EXPLORED = 2
            $ at_unlock_spell = 0
            if not ruinedvillage_curse_gone:
                $ ruinedvillage_curse_points += 1
            jump ruinedvillage01leftfield03
        'I lack pneuma to detect magic in the ground. [[Cost: [manacost]] (disabled)' ( condition= "at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I don’t have time to investigate.' ( condition="ruinedvillage_part_leftfield_EXPLORED < 2 and at == 'spell' or item_magicalsapling == 1"):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to investigate')
            $ at_unlock_spell = 0
            jump ruinedvillageselectarea
        'I don’t have a way to investigate.' ( condition="ruinedvillage_part_leftfield_EXPLORED < 2 and at != 'spell' and not item_magicalsapling"):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have a way to investigate.')
            $ at_unlock_spell = 0
            jump ruinedvillageselectarea
        'I go somewhere else.' ( condition="ruinedvillage_part_leftfield_EXPLORED > 1"):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
            $ at_unlock_spell = 0
            jump ruinedvillageselectarea

    label ruinedvillage01leftfield01explored:
        $ at = 0
        if pc_class == "mage":
            $ at_unlock_spell = 1
            $ manacost = 1
        if not ruinedvillage_part_leftentrance_EXPLORED:
            $ custom1 = "\n\nIn the north, you see a path leading around the palisade."
        else:
            $ custom1 = ""
        if not ruinedvillage_part_bottomentrance_EXPLORED:
            $ custom2 = "\n\nEast from here there’s an abandoned building and a road leading south."
        else:
            $ custom2 = ""
        menu:
            'You’re surrounded by barren fields. The path leading west from here ends together with the field, shifting into a meadow, then a forest. In the north, you see a passable path around the palisade. East from here you see a road leading south and an abandoned building. [custom1][custom2]
            '
            'I use my amulets to sense if there’s pneuma buried in this place. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my amulets to sense if there’s a pneuma buried in this place.')
                $ ruinedvillage_part_leftfield_EXPLORED = 2
                $ at_unlock_spell = 0
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                if not ruinedvillage_curse_gone:
                    $ ruinedvillage_curse_points += 1
                jump ruinedvillage01leftfield02
            'I use the weird sapling to sense if there’s pneuma buried in this place.' if item_magicalsapling:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the weird sapling to sense if there’s a pneuma buried in this place.')
                $ ruinedvillage_part_leftfield_EXPLORED = 2
                $ at_unlock_spell = 0
                if not ruinedvillage_curse_gone:
                    $ ruinedvillage_curse_points += 1
                jump ruinedvillage01leftfield03
            'I lack pneuma to detect magic in the ground. [[Cost: [manacost]] (disabled)' ( condition= "at_unlock_spell == 1 and mana < manacost" ):
                pass
            'I don’t have time to investigate.' ( condition="ruinedvillage_part_leftfield_EXPLORED < 2 and at == 'spell' or item_magicalsapling == 1"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to investigate')
                $ at_unlock_spell = 0
                jump ruinedvillageselectarea
            'I don’t have a way to investigate.' ( condition="ruinedvillage_part_leftfield_EXPLORED < 2 and at != 'spell' and not item_magicalsapling"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have a way to investigate.')
                $ at_unlock_spell = 0
                jump ruinedvillageselectarea
            'I go somewhere else.' ( condition="ruinedvillage_part_leftfield_EXPLORED > 1"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                $ at_unlock_spell = 0
                jump ruinedvillageselectarea

    label ruinedvillage01leftfield02:
        $ quarters += 2
        $ ruinedvillage_clues += 2
        $ quest_ruins_insideclues06 = "I’ve proven that the local fields have been turned barren by a curse."
        if quest_ruins == 1:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            'You unpack the wooden spheres, pleasantly smooth and light. The entire set fits in the palm of your hand. You place them in various spots, marking their positions by sticking a branch in the soil. All you can do now is wait, so you brush {color=#f6d6bd}[horsename]{/color} for a bit and make sure the saddle doesn’t bother it.
            \n\nWhen you return to gather your amulets, all of them are much warmer than your skin. The entire field is corrupted, though seeing how there are already some plants growing from it, the spell is fading away. The curse is most likely as old as the last harvest.
            '
            'I walk away. I need these amulets to cool off.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away. I need these amulets to cool off.')
                $ at_unlock_spell = 0
                jump ruinedvillageselectarea

    label ruinedvillage01leftfield03:
        $ quarters += 2
        $ ruinedvillage_clues += 2
        $ item_magicalsapling -= 1
        if quest_ruins == 1:
            $ renpy.notify("Journal updated: The Ruined Village.\nYou lost the sapling.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village. You lost the sapling.{/i}')
        else:
            $ renpy.notify("You lost the sapling.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the sapling.{/i}')
        $ quest_ruins_insideclues06 = "I’ve proven that the local fields have been turned barren by a curse."
        if pc_class == "scholar" and ruinedvillage_part_leftfield_EXPLORED == 2 and not ruinedvillage_part_leftfieldtakencursedsoil and not item_cursedsoil:
            $ at_unlock_knowledge = 1
            $ at = 0
        else:
            $ at_unlock_knowledge = 0
            $ at = 0
        menu:
            'You remove the linen sack and shake off the soil from the roots, then dig a hole and plant the sapling in the middle of the field. Just to be sure, you don’t water it. All you can do now is wait, so you brush {color=#f6d6bd}[horsename]{/color} for a bit and make sure the saddle doesn’t bother it.
            \n\nWhen you return, the plant is dark from sickness, dried up, withered. The field must have been corrupted, though seeing how there are already some plants growing from it, the spell is fading away. The curse is most likely as old as the last harvest.
            '
            'I shove some of the cursed soil into a jar. It’s a valuable ingredient.' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shove some of the cursed soil into a jar. It’s a valuable ingredient.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01takingthecursedsoil
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                $ at_unlock_spell = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillageselectarea

    label ruinedvillage01leftfield01takingthecursedsoil:
        $ at_unlock_knowledge = 0
        $ at = 0
        $ minutes += 5
        $ ruinedvillage_clues += 2
        $ ruinedvillage_part_leftfieldtakencursedsoil += 1
        $ item_cursedsoil += 1
        $ renpy.notify("You added the cursed soil to your bag of ingredients.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the cursed soil to your bag of ingredients.{/i}')
        menu:
            'You look for a proper, clean container, then crouch down and fill it with some of the soil, removing any rocks and remains of the plants. During these few minutes, you only find one worm.
            '
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                $ at_unlock_spell = 0
                jump ruinedvillageselectarea

label ruinedvillage01rightpasture01:
    $ ruinedvillage_part_rightpasture = 1
    $ ruinedvillage_part_rightpasture_EXPLORED = 2
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_clues += 1
    show ruinedvillage_part_rightpasture 01 at basicfade
    $ quest_ruins_insideclues09 = "Some humans chopped through the fence that surrounds the large pasture. Maybe to save a herd, maybe to steal it."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    menu:
        'You don’t find a single sign of the livestock that lived here in the past. Any bones, horns, antlers, or dung have already been devoured by the wilderness.
        \n\nThe pasture ends at the river. On the opposite bank, the meadow turns into a thick forest, impenetrable for a rider. What are the chances that a herd of defenseless animals could get there and survive?
        \n\nThe breach in the southern fence wasn’t made by some brute force - you find axe cuts in the spots that were ultimately broken away. After all these years, there are no tracks that you could follow.
        '
        'I return to the main road.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main road.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrancefirsttime:
    $ ruinedvillage_part_bottomentrance = 1
    show ruinedvillage_part_bottomentrance 01 at basicfade
    $ ruinedvillage_part_bottomentrance_EXPLORED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftfield_UNLOCKED = 1
    $ ruinedvillage_part_rightpasture_UNLOCKED = 1
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    $ quest_ruins = 1
    $ renpy.notify("New entry: The Ruined Village")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Ruined Village{/i}')
    $ quest_explorepeninsula_description09 = "The abandoned village in the South may be a useful spot for future settlers. I should figure out why it was ruined."
    if not ruinedvillage_part_bottomleftwing_EXPLORED:
        $ custom1 = "\n\nThe broken gate in the north will lead you to the village."
    else:
        $ custom1 = ""
    if not ruinedvillage_part_rightpasture_EXPLORED:
        $ custom2 = "\n\nThe sound of a gentle river reaches you from the east, where you see a saggy fence surrounding an overgrown pasture."
    else:
        $ custom2 = ""
    if not ruinedvillage_part_leftfield_EXPLORED:
        $ custom3 = "\n\nBehind the burnt building in the east, you see an oddly barren field. "
    else:
        $ custom3 = ""
    menu:
        'Standing in front of the gate, you hear no voices, no tools at work, no steps. Dozens of birds live among the collapsed roofs. Their fluttering, singing, and squawking is free of worries.
        \n\nIf you want to travel any further, you need to ride around the palisade. Searching the ruins may take a lot of time.[custom1][custom2][custom3]
        '
        'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance02
        'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatgate = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance03
        'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_treasure_diggingout = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance04
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrance02: #building-storage
    menu:
        'The broken logs and planks are charred, while the wooden walls are rotten and covered in moss. You see no ashes or dust, proving that the fire happened long ago.
        \n\nThe smell is awful, and there are no reasons to stay for long. You see no furniture, just some broken shelves. It was just a storage room. The valuable odds and ends were already taken by the scavengers.
        '
        'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatgate = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance03
        'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_treasure_diggingout = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance04
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrance03: #gate
    $ ruinedvillage_clues += 1
    $ quest_ruins_insideclues01 = "The southern gate was destroyed by a massive force, most likely a troll or a powerful mage."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    menu:
        'The palisade is in good shape and the entrance wasn’t even touched by the fire. It was torn away, possibly thrown. The amount of used force  must have been huge, but you’d expect that it would push the gate into the village, not away from it.
        \n\nYou don’t see any marks of a dragon bite. A troll could toss such planks, but after so many years, you see no paw prints. A mage? You can’t really tell.
        '
        'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance02
        'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_treasure_diggingout = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance04
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrance04: #treasure
    menu:
        'I’m sorry, this option shouldn’t be available to you.
        '
        'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance02
        'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatgate = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance03
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrancearrival:
    if not ruinedvillage_part_bottomentrance_EXPLORED:
        jump ruinedvillage01bottomentrance01
    $ ruinedvillage_part_bottomentrance = 1
    if ruinedvillage_part_bottomentrance_EXPLORED < 2:
        $ ruinedvillage_part_bottomentrance_EXPLORED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftfield_UNLOCKED = 1
    $ ruinedvillage_part_rightpasture_UNLOCKED = 1
    show ruinedvillage_part_bottomentrance 01 at basicfade
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    if ruinedvillage_part_bottomentrance_EXPLORED and ruinedvillage_part_bottomleftwing_EXPLORED == 2 and ruinedvillage_part_bottomrightwing_EXPLORED == 2 and ruinedvillage_part_clearing_EXPLORED == 2 and ruinedvillage_part_leftentrance_EXPLORED == 2 and ruinedvillage_part_topentranceinside_EXPLORED and ruinedvillage_part_leftfield_EXPLORED and ruinedvillage_part_leftwing_EXPLORED == 2 and ruinedvillage_part_rightpasture_EXPLORED == 2 and ruinedvillage_part_rightwing_EXPLORED == 2 and ruinedvillage_part_river_EXPLORED == 2 and ruinedvillage_part_square_EXPLORED == 2 and ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_explored:
        $ ruinedvillage_explored = 1
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if pc_class == "scholar" and ruinedvillage_part_leftfield_EXPLORED == 2 and not ruinedvillage_part_leftfieldtakencursedsoil and not item_cursedsoil:
        $ at_unlock_knowledge = 1
        $ at = 0
    else:
        $ at_unlock_knowledge = 0
        $ at = 0
    if ruinedvillage_part_bottomleftwing_EXPLORED and ruinedvillage_part_rightpasture_EXPLORED and ruinedvillage_part_leftfield_EXPLORED:
        menu:
            'The village remains dead.
            '
            'I consider washing myself in the river.' if ruinedvillage_part_river_EXPLORED:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillagebath01
            'I pick up the fish trap from the ruined building.' if not item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the fish trap from the ruined building.')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ ruinedvillage_fishtrap_found = 1
                $ item_fishtrap += 1
                $ renpy.notify("You picked up a fish trap.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up a fish trap{/i}')
                jump ruinedvillageselectarea
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters <= (world_daylength-8) and ruinedvillage_part_river" ):
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap01
            'It’s already dark. Setting up a fish trap in the river right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters > (world_daylength-8) and ruinedvillage_part_river" ):
                pass
            'Let’s see if the fish trap had any luck.' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked != day and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked == day and ruinedvillage_part_river:
                pass
            'I set the fish trap again.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap03
            'I take the fish trap back.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and not item_fishtrap and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and item_fishtrap and ruinedvillage_part_river:
                pass
            ################
            'I enter the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and not ruinedvillage_goblinlair_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair01
            'I return to the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and ruinedvillage_goblinlair_EXPLORED and not ruinedvillage_goblinlair_clue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair02
            ################
            'I return to the scavenger’s camp.' if (ruinedvillage_curse_gone and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the scavenger’s camp.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01scavengerscamp01
            ################
            'I go to the road leading north from the village.' if ruinedvillage_part_topentrance_UNLOCKED == 1 and not ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the road leading north from the village.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentrance01
            ################
            'I want to look around the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the northern gate.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01
            'I return to the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01explored
            ################
            'I inspect the clearing in the west.' if ruinedvillage_part_clearing_UNLOCKED == 1 and not ruinedvillage_part_clearing_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the clearing in the west')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftclearing01
            ################
            'I head to the river.' if ruinedvillage_part_river_UNLOCKED == 1 and not ruinedvillage_part_river_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the river.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01river01
            ################
            'I inspect the palisade in the west.' if ruinedvillage_part_leftentrance_UNLOCKED == 1 and not ruinedvillage_part_leftentrance_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the palisade in the west.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftentrance01
            ################
            'I explore the northwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftwing01
            ################
            'I explore the northeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED):
                $ minutes += 7
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northeast part of the village.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightwing01
            ################
            'I go to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED):
                $ minutes += 5
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01
            'I return to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01explored
            ################
            'I explore the southwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomleftwing01
            ################
            'I explore the southeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southeast part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomrightwing01
            ################
            'I inspect the fields in the southwest.' if ruinedvillage_part_leftfield_UNLOCKED == 1 and not ruinedvillage_part_leftfield_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the fields in the southwest.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01
            'I return to the barren fields in the southwest.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the barren fields in the southwest.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01explored
            'I shove some of the cursed soil into a jar. It’s a valuable ingredient.' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shove some of the cursed soil into a jar. It’s a valuable ingredient.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01takingthecursedsoil
            ################
            'I inspect the pasture in the southeast.' if ruinedvillage_part_rightpasture_UNLOCKED == 1 and not ruinedvillage_part_rightpasture_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the pasture in the southeast.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightpasture01
            ###############
            'I want to look around the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and not ruinedvillage_part_bottomentrance_EXPLORED:
                $ minutes += 6
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01
            'I return to the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and ruinedvillage_part_bottomentrance_EXPLORED == 1:
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01explored
            ################
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            'I need to see what’s on the other side of the northern gate if I want to open it. (disabled)' if (ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            ###############
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_leftfield_EXPLORED < 2) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_clue) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_EXPLORED < 2):
                pass
            ###############
            'I saw a fish trap in the ruined building, but I won’t be able to fit another one in the saddle. (disabled)' if item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                pass
            'The river would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ruinedvillage_fishtrap and ruinedvillage_part_river:
                pass
    else:
        if not ruinedvillage_part_bottomleftwing_EXPLORED:
            $ custom1 = "\n\nThe broken gate in the north will lead you to the village."
        else:
            $ custom1 = ""
        if not ruinedvillage_part_rightpasture_EXPLORED:
            $ custom2 = "\n\nThe sound of a gentle river reaches you from the east, where you see a saggy fence surrounding an overgrown pasture."
        else:
            $ custom2 = ""
        if not ruinedvillage_part_leftfield_EXPLORED:
            $ custom3 = "\n\nBehind the burnt building in the east, you see an oddly barren field. "
        else:
            $ custom3 = ""
        menu:
            'The village remains dead.[custom1][custom2][custom3]
            '
            'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
                $ ruinedvillage_part_bottomentranceactions += 1
                $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
                if ruinedvillage_part_bottomentranceactions >= 2:
                    $ ruinedvillage_part_bottomentrance_EXPLORED = 2
                jump ruinedvillage01bottomentrance02
            'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
                $ ruinedvillage_part_bottomentranceactions += 1
                $ ruinedvillage_part_bottomentrancelookingatgate = 1
                if ruinedvillage_part_bottomentranceactions >= 2:
                    $ ruinedvillage_part_bottomentrance_EXPLORED = 2
                jump ruinedvillage01bottomentrance03
            'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
                $ ruinedvillage_part_bottomentranceactions += 1
                $ ruinedvillage_treasure_diggingout = 1
                if ruinedvillage_part_bottomentranceactions >= 2:
                    $ ruinedvillage_part_bottomentrance_EXPLORED = 2
                jump ruinedvillage01bottomentrance04
            'I go somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go somewhere else.')
                jump ruinedvillageselectarea

label ruinedvillage01bottomentrance01:
    $ ruinedvillage_part_bottomentrance = 1
    $ ruinedvillage_part_bottomentrance_EXPLORED = 1
    $ ruinedvillage_part_bottomleftwing_UNLOCKED = 1
    $ ruinedvillage_part_bottomentrance_UNLOCKED = 1
    $ ruinedvillage_part_leftfield_UNLOCKED = 1
    $ ruinedvillage_part_rightpasture_UNLOCKED = 1
    show ruinedvillage_part_bottomentrance 01 at basicfade
    if ruinedvillage_part_bottomentrance and ruinedvillage_part_topentrance:
        $ beholder_unlocked = 1
    if not ruinedvillage_part_rightpasture_EXPLORED:
        $ custom2 = "\n\nThe sound of a gentle river reaches you from the east, where you see a saggy fence surrounding an overgrown pasture."
    else:
        $ custom2 = ""
    if not ruinedvillage_part_leftfield_EXPLORED:
        $ custom3 = "\n\nBehind the burnt building in the east, you see an oddly barren field. "
    else:
        $ custom3 = ""
    menu:
        'The gate leading to the village is completely destroyed. The building is almost burnt to the ground.[custom2][custom3]
        '
        'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance02
        'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatgate = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance03
        'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_treasure_diggingout = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance04
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

label ruinedvillage01bottomentrance01explored:
    if not ruinedvillage_part_bottomleftwing_EXPLORED:
        $ custom1 = "The broken gate in the north will lead you to the village."
    else:
        $ custom1 = "Not much has changed at the broken gate."
    if not ruinedvillage_part_rightpasture_EXPLORED:
        $ custom2 = "\n\nThe sound of a gentle river reaches you from the east, where you see a saggy fence surrounding an overgrown pasture."
    else:
        $ custom2 = ""
    if not ruinedvillage_part_leftfield_EXPLORED:
        $ custom3 = "\n\nBehind the burnt building in the east, you see an oddly barren field. "
    else:
        $ custom3 = ""
    menu:
        '[custom1][custom2][custom3]
        '
        'I approach the building near the field.' if not ruinedvillage_part_bottomentrancelookingatbuilding:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the building near the field.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatbuilding = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance02
        'I take a closer look at the gate.' if not ruinedvillage_part_bottomentrancelookingatgate:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the gate.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_part_bottomentrancelookingatgate = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance03
        'I’m looking for a treasure near the dead tree.' if not ruinedvillage_treasure_diggingout and ruinedvillage_treasure_known and not ruinedvillage_treasure:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for a treasure near the dead tree.')
            $ ruinedvillage_part_bottomentranceactions += 1
            $ ruinedvillage_treasure_diggingout = 1
            if ruinedvillage_part_bottomentranceactions >= 2:
                $ ruinedvillage_part_bottomentrance_EXPLORED = 2
            jump ruinedvillage01bottomentrance04
        'I move forward.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
            jump ruinedvillageselectarea

    label ruinedvillage01investigation02:
        if quest_ruins == 1:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            'You don’t have enough evidence to prove it, but you may use these conclusions in your further investigation.
            '
            'Let’s move to a different spot.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s move to a different spot.')
                jump ruinedvillageselectarea

label ruinedvillage01goblinlair01:
    $ ruinedvillage_goblinlair_EXPLORED = 1
    if pc_goal == "iwanttohelp":
        $ pc_goal_iwanttohelppoints += 1
    menu:
        'You return to the northwest corner of the village. The goblins may have been killed or chased off, but their smell is still around, so {color=#f6d6bd}[horsename]{/color} is just as alert as it was the last time you were here. You tether it in the animal pen, the one with a single boulder, allowing it to graze on the struggling, dry grass.
        \n\nJust in case, you take your blade with you, but also the other pieces of equipment. You don’t expect the creatures to move back, but who knows when the next scavenger will move in to feed on the remains of the pack.
        \n\nYou stand in front of the entrance. The dried-out blood now covers the older layers of dirt and rubbish.
        '
        'I plug my nose with some scraps of fabric. And maybe cover it as well.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I plug my nose with some scraps of fabric. And maybe cover it as well.')
            $ ruinedvillage_goblinlair_nose = 1
            $ custom1 = "It helps, but not as much as you’d like. When you find yourself surrounded by the chopped-off shell parts, trash, bodily fluids, and feces, your imagination fills in the blanks of the vague sensations. Not looking directly at the place of carnage helps, so you raise your eyes and move forward."
            jump ruinedvillage01goblinlair01a
        'No matter how disgusting this place is, I can endure it. I need all of my senses.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No matter how disgusting this place is, I can endure it. I need all of my senses.')
            $ custom1 = "When you find yourself surrounded by the chopped-off shell parts, trash, bodily fluids, and feces, your head is filled with so many sensations that your legs get weaker. You try to look away, move forward without looking at what’s at your feet, but you can’t help but be as present as possible."
            jump ruinedvillage01goblinlair01a

    label ruinedvillage01goblinlair01a:
        #show areapicture goblinlair01 at basicfade
        menu:
            '[custom1]
            \n\nThe building has two floors, with the upper one used to store straw and supplies. Since the roof’s collapse, half of this place is covered with broken furniture, beams, bricks, planks, already overgrown by moss and fungi. The greenish pile makes you think of a side of a hill, though it’s riddled with so many gaps that the light and rain can squeeze in between the debris. You try to avoid the puddles.
            '
            'Let’s see what I can find.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s see what I can find.')
                menu:
                    'The lair is as crude as a rat’s nest, yet escapes your words and senses. The sleeping spots are made of straw, scraps of clothes, feathers, and moss, but are so old and clumped together that you doubt they are any softer than the rotting planks beneath them. The corners are filled with feces, and you don’t think it would make any difference for the creatures to relieve themselves in the middle of the room. You see broken furniture and all sorts of rubbish with no specific shape, nor a purpose you can identify, and a stack of bones and sharpened sticks, taller than you are.
                    \n\nIt’s nothing like the humble shelters that the families of apes build among the tree crowns. It’s tamed chaos, an attempt at maintaining order in a place that ceased to be a human structure, yet is still not a part of the wilderness.
                    \n\nJust a few days ago dozens of beasts were living here, but you can’t imagine how anything could survive in such conditions. The walls are covered with black and green molds. The floor is very much alive, with countless worms, insects, small lizards, and rodents running among the dirt and the fresh shells of furry goblins. The blood, guts, and flesh are covering way more spots than you’d hope for. Something is happening in your stomach.
                    '
                    '{image=d6} Time to look for anything of value. I’m ready to spend even more than an hour in this place.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Time to look for anything of value. I’m ready to spend even more than an hour in this place.')
                        jump ruinedvillage01goblinlair03
                    '...Maybe I’ll come back later.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...Maybe I’ll come back later.')
                        jump ruinedvillageselectarea

    label ruinedvillage01goblinlair02:
        #show areapicture goblinlair01 at basicfade
        menu:
            'You’ve returned to the stinking building. The rotting corpses will need weeks, if not more, before they turn to bone, but the worms and other animals are having a feast.
            '
            '{image=d6} Time to look for anything of value. I’m ready to spend even more than an hour in this place.' if not ruinedvillage_goblinlair_clue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Time to look for anything of value. I’m ready to spend even more than an hour in this place.')
                jump ruinedvillage01goblinlair03
            'I leave the building.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                jump ruinedvillageselectarea

    label ruinedvillage01goblinlair03:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 3)
        $ d100roll += 1
        $ quarters += d100roll
        if d100roll == 2:
            $ custom1 = "half an hour"
        if d100roll == 3:
            $ custom1 = "almost an hour"
        if d100roll == 4:
            $ custom1 = "an hour"
        $ ruinedvillage_goblinlair_clue = 1
        if not ruinedvillage_curse_gone:
            $ ruinedvillage_curse_points += 1
        if quest_escortpyrrhos == 3 and not pyrrhos_gave_ironingot:
            if galerocks_pastrobbery:
                $ custom2 = " Then you find an unusually heavy brick, which, after being treated with some water, turns out to be a dark ingot of crude iron. Could it be the same as the one stolen from {color=#f6d6bd}Gale Rocks{/color}?"
            else:
                $ custom2 = " Then you find an unusually heavy brick, which, after being treated with some water, turns out to be a dark ingot of crude iron. Not as valuable as steel, but something that will surely be worth a good sack of dragon bones."
            $ item_ironingot = 1
            $ renpy.notify("You found an iron ingot.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found an iron ingot.{/i}')
        else:
            $ custom2 = ""
        $ cleanliness = limit_cleanliness(cleanliness-2)
        show minus2appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        menu:
            'The painful search takes you [custom1]. You move the carcasses around, look into the stacks of garbage, examine the sleeping spots. By accident, you make one of the piles of furniture collapse, covering the floor with yet another layer of chaos. With every minute you get more upset about the state of your boots and gloves, knowing that some tiresome cleaning is ahead of you.
            \n\nYour disappointment grows. There are many stories of goblins storing unusual treasures in their lairs, but you find not even a single dragon. Could the hunters have been so sharp-eyed in their search that they’ve left nothing behind? Or were the goblins simply never interested in gathering things for which they found no purpose?[custom2]
            \n\nYou move a larger plank, an ex-shelf leaning against one of the moldy walls, and you reveal something curious. A group of signs made with red paint.
            '
            'I look at the marks closely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the marks closely.')
                $ quest_ruins_treepicture = 1
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                if item_howlersdelltoken:
                    $ custom1 = "It’s very similar to the picture on the {i}Token of Gratitude{/i} that you received in {color=#f6d6bd}Howler’s Dell{/color}."
                elif howlersdell_firsttime:
                    $ custom1 = "You saw a similar plant in the main square of {color=#f6d6bd}Howler’s Dell{/color}. "
                else:
                    $ custom1 = "You’re not sure what exactly it could be."
                if pc_class == "scholar":
                    $ custom2 = "Above the tree you see a single, large word. {i}TRAITORS.{/i}"
                else:
                    $ custom2 = "Above the tree you see a single, large word, though you can’t read it."
                menu:
                    'The paint is old, placed with noteworthy artistry. It portrays a large tree without leaves, just a bunch of branches. [custom1] Its roots grow out of a human skull, penetrating its eye sockets and the open mouth, and a couple of red drops were allowed to run down the wall.
                    \n\n[custom2]
                    '
                    'I go outside. I need the fresh air and some water from the river.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside. I need the fresh air and some water from the river.')
                        $ quarters += 1
                        jump ruinedvillageselectarea

label ruinedvillageselectarea:
    if ruinedvillage_part_bottomentranceactions >= 2:
        $ ruinedvillage_part_bottomentrance_EXPLORED = 2
    $ at_unlock_knowledge = 0
    $ at = 0
    hide areapicture
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_topentranceinside == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentranceinside 02 at basicfade
        else:
            show ruinedvillage_part_topentranceinside 01 at basicfade
    if ruinedvillage_part_clearing == 1:
        show ruinedvillage_part_clearing 01 at basicfade
    if ruinedvillage_part_river == 1:
        show ruinedvillage_part_river 01 behind fishtrap at basicfade
    if ruinedvillage_part_leftentrance == 1:
        show ruinedvillage_part_leftentrance 01 at basicfade
    if ruinedvillage_part_leftwing == 1:
        show ruinedvillage_part_leftwing 01 at basicfade
    if ruinedvillage_part_rightwing == 1:
        show ruinedvillage_part_rightwing 01 at basicfade
    if ruinedvillage_part_square == 1:
        show ruinedvillage_part_square 01 at basicfade
    if ruinedvillage_part_bottomleftwing == 1:
        show ruinedvillage_part_bottomleftwing 01 at basicfade
    if ruinedvillage_part_bottomrightwing == 1:
        show ruinedvillage_part_bottomrightwing 01 at basicfade
    if ruinedvillage_part_leftfield == 1:
        show ruinedvillage_part_leftfield 01 at basicfade
    if ruinedvillage_part_rightpasture == 1:
        show ruinedvillage_part_rightpasture 01 at basicfade
    if ruinedvillage_part_bottomentrance == 1:
        show ruinedvillage_part_bottomentrance 01 at basicfade
    if ruinedvillage_fishtrap:
        show fishtrap ruinedvillage01 at basicfade
    #################################
    if ruinedvillage_part_bottomentrance_EXPLORED and ruinedvillage_part_bottomleftwing_EXPLORED == 2 and ruinedvillage_part_bottomrightwing_EXPLORED == 2 and ruinedvillage_part_clearing_EXPLORED == 2 and ruinedvillage_part_leftentrance_EXPLORED == 2 and ruinedvillage_part_topentranceinside_EXPLORED and ruinedvillage_part_leftfield_EXPLORED and ruinedvillage_part_leftwing_EXPLORED == 2 and ruinedvillage_part_rightpasture_EXPLORED == 2 and ruinedvillage_part_rightwing_EXPLORED == 2 and ruinedvillage_part_river_EXPLORED == 2 and ruinedvillage_part_square_EXPLORED == 2 and ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_explored:
        $ ruinedvillage_explored = 1
    if ruinedvillage_curse_gone:
        $ ruinedvillage_curse_points = 0
    if ruinedvillage_curse_points >= 3 and not ruinedvillage_curse_block:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
        $ ruinedvillage_curse_firsttime += 1
        menu:
            'The closer you are to the village, and the longer you stay around, the sicker you feel. The taste of gastric juices hits your mouth, your forehead hurts, you start to stumble. {color=#f6d6bd}[horsename]{/color}, worried by the sight, pokes your head with its nose.
            '
            'I walk far away from the walls.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk far away from the walls.')
                $ ruinedvillage_curse_block = 1
                $ quarters += 1
                menu:
                    'Leaning on your mount, you go outside, keeping your mouth shut. After a few minutes, your eyes get clearer.
                    '
                    'It may be better to leave, or at least to stay away from the village for the rest of the day.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be better to leave, or at least to stay away from the village for the rest of the day.')
                        jump ruinedvillageselectarea
            'I can’t push through the sickness through sheer will. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                pass
            'I have to remain strong. I push through the illness.' ( condition="pc_hp >= 2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have to remain strong. I push through the illness.')
                $ ruinedvillage_curse_points -= 3
                $ minutes += 5
                if pc_food >= 3:
                    $ custom1 = "return your last meal"
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    $ custom1 = "return whatever was left in your stomach, going through a lot of pain"
                $ pc_food = limit_pc_food(pc_food-4)
                show minus4food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 nourishment points.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'After another few steps, you [custom1]. You spend a minute or so leaned forward, gathering your breath, then wipe your mouth. You feel better.
                    '
                    'I straighten up.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I straighten up.')
                        jump ruinedvillageselectarea
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if pc_class == "scholar" and ruinedvillage_part_leftfield_EXPLORED == 2 and not ruinedvillage_part_leftfieldtakencursedsoil and not item_cursedsoil:
            $ at_unlock_knowledge = 1
            $ at = 0
        else:
            $ at_unlock_knowledge = 0
            $ at = 0
        if ruinedvillage_curse_gone:
            $ custom1 = "With the curse lifted, your stomach doesn’t bother you anymore.\n\n"
        elif not ruinedvillage_curse_points:
            $ custom1 = ""
        elif ruinedvillage_curse_points == 1:
            $ custom1 = "You feel a slight aching in your stomach.\n\n"
        elif ruinedvillage_curse_points == 2:
            $ custom1 = "Your stomach makes you let out a painful groan.\n\n"
        # elif ruinedvillage_curse_points == 3:
        #     $ custom1 = "You stop and touch your aching stomach."
        elif ruinedvillage_curse_points == 3:
            $ custom1 = "You stop and touch your aching stomach.\n\n"#"The closer you are to the village, the more you want to vomit."
        else:
            $ custom1 = "The pain in your stomach slows you down.\n\n"
        menu:
            '[custom1]Where do you want to go?
            '
            'I consider washing myself in the river.' if ruinedvillage_part_river_EXPLORED:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillagebath01
            'I pick up the fish trap from the ruined building.' if not item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the fish trap from the ruined building.')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ ruinedvillage_fishtrap_found = 1
                $ item_fishtrap += 1
                $ renpy.notify("You picked up a fish trap.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up a fish trap{/i}')
                jump ruinedvillageselectarea
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters <= (world_daylength-8) and ruinedvillage_part_river" ):
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap01
            'It’s already dark. Setting up a fish trap in the river right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ruinedvillage_fishtrap and quarters > (world_daylength-8) and ruinedvillage_part_river" ):
                pass
            'Let’s see if the fish trap had any luck.' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked != day and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ruinedvillage_fishtrap and ruinedvillage_fishtrap_working and ruinedvillage_fishtrap_daychecked == day and ruinedvillage_part_river:
                pass
            'I set the fish trap again.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap03
            'I take the fish trap back.' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and not item_fishtrap and ruinedvillage_part_river:
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ruinedvillage_fishtrap and not ruinedvillage_fishtrap_working and item_fishtrap and ruinedvillage_part_river:
                pass
            ################
            'I enter the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and not ruinedvillage_goblinlair_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair01
            'I return to the goblins’ lair.' if dalit_about_goblins_timer and dalit_about_goblins_timer < day and ruinedvillage_goblinlair_EXPLORED and not ruinedvillage_goblinlair_clue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the goblins’ lair.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01goblinlair02
            ################
            'I return to the scavenger’s camp.' if (ruinedvillage_curse_gone and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_camp_UNLOCKED == 1 and quest_escortpyrrhos < 2 and not pyrrhos_peltnorth and not pyrrhos_howlersdell and not pyrrhos_dead):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the scavenger’s camp.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01scavengerscamp01
            ################
            'I go to the road leading north from the village.' if ruinedvillage_part_topentrance_UNLOCKED == 1 and not ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentrance_gate_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the road leading north from the village.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentrance01
            ################
            'I want to look around the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and not ruinedvillage_part_topentranceinside_EXPLORED and not ruinedvillage_part_topentrance_gate_open):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the northern gate.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01
            'I return to the northern gate.' if (ruinedvillage_curse_gone and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_UNLOCKED == 1 and ruinedvillage_part_topentranceinside_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the northern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01topentranceinside01explored
            ################
            'I inspect the clearing in the west.' if ruinedvillage_part_clearing_UNLOCKED == 1 and not ruinedvillage_part_clearing_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the clearing in the west')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftclearing01
            ################
            'I head to the river.' if ruinedvillage_part_river_UNLOCKED == 1 and not ruinedvillage_part_river_EXPLORED:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the river.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01river01
            ################
            'I inspect the palisade in the west.' if ruinedvillage_part_leftentrance_UNLOCKED == 1 and not ruinedvillage_part_leftentrance_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the palisade in the west.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftentrance01
            ################
            'I explore the northwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftwing_UNLOCKED == 1 and not ruinedvillage_part_leftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftwing01
            ################
            'I explore the northeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_rightwing_UNLOCKED == 1 and not ruinedvillage_part_rightwing_EXPLORED):
                $ minutes += 7
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the northeast part of the village.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightwing01
            ################
            'I go to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and not ruinedvillage_part_square_EXPLORED):
                $ minutes += 5
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01
            'I return to the main square.' if (ruinedvillage_curse_gone and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_square_UNLOCKED == 1 and ruinedvillage_part_square_EXPLORED == 1):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main square.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01square01explored
            ################
            'I explore the southwest part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomleftwing_UNLOCKED == 1 and not ruinedvillage_part_bottomleftwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southwest part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomleftwing01
            ################
            'I explore the southeast part of the village.' if (ruinedvillage_curse_gone and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_bottomrightwing_UNLOCKED == 1 and not ruinedvillage_part_bottomrightwing_EXPLORED):
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explore the southeast part of the village.')
                $ minutes += 7
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomrightwing01
            ################
            'I inspect the fields in the southwest.' if ruinedvillage_part_leftfield_UNLOCKED == 1 and not ruinedvillage_part_leftfield_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the fields in the southwest.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01
            'I return to the barren fields in the southwest.' if (ruinedvillage_curse_gone and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and ruinedvillage_part_leftfield_UNLOCKED == 1 and ruinedvillage_part_leftfield_EXPLORED == 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the barren fields in the southwest.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01explored
            'I shove some of the cursed soil into a jar. It’s a valuable ingredient.' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shove some of the cursed soil into a jar. It’s a valuable ingredient.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01leftfield01takingthecursedsoil
            ################
            'I inspect the pasture in the southeast.' if ruinedvillage_part_rightpasture_UNLOCKED == 1 and not ruinedvillage_part_rightpasture_EXPLORED:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I inspect the pasture in the southeast.')
                $ minutes += 5
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01rightpasture01
            ###############
            'I want to look around the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and not ruinedvillage_part_bottomentrance_EXPLORED:
                $ minutes += 6
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01
            'I return to the southern gate.' if ruinedvillage_part_bottomentrance_UNLOCKED == 1 and ruinedvillage_part_bottomentrance_EXPLORED == 1:
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the southern gate.')
                $ at_unlock_knowledge = 0
                $ at = 0
                jump ruinedvillage01bottomentrance01explored
            ################
            'I want to open the gate.' if (ruinedvillage_curse_gone and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_curse_gone and not ruinedvillage_curse_block and not ruinedvillage_part_topentrance_gate_open and not ruinedvillage_part_topentrance_gate_quickclose and ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            'I need to see what’s on the other side of the northern gate if I want to open it. (disabled)' if (ruinedvillage_part_topentrance_EXPLORED and not ruinedvillage_part_topentranceinside_EXPLORED) or (not ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_topentranceinside_EXPLORED):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to open the gate.')
                jump ruinedvillage01topentrance03
            ###############
            'I feel like every step into the village weakens me more. I should return another day. (disabled)' if (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_leftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_rightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_square_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomleftwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_part_bottomrightwing_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_leftfield_EXPLORED < 2) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_EXPLORED) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and not ruinedvillage_goblinlair_clue) or (not ruinedvillage_curse_gone and ruinedvillage_curse_block and ruinedvillage_part_topentranceinside_EXPLORED < 2):
                pass
            ###############
            'I saw a fish trap in the ruined building, but I won’t be able to fit another one in the saddle. (disabled)' if item_fishtrap and ruinedvillage_part_bottomleftwing_EXPLORED and not ruinedvillage_fishtrap_found:
                pass
            'The river would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ruinedvillage_fishtrap and ruinedvillage_part_river:
                pass

##################################################

label ruinedvillage_fishtrapALL:
    label ruinedvillage_fishtrap01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend some time setting up a fish trap at the bank.')
        show fishtrap ruinedvillage01 at basicfade
        $ quarters += 2
        $ item_fishtrap -= 1
        $ ruinedvillage_fishtrap = 1
        $ ruinedvillage_fishtrap_daychecked = day
        $ ruinedvillage_fishtrap_working = day
        $ ruinedvillage_fishtrap_fishtimer = renpy.random.randint(1, 3)
        $ ruinedvillage_fishtrap_fishtimer = (ruinedvillage_fishtrap_fishtimer+day)
        menu:
            'You place the basket on the ground, then grab a bowl and start digging, looking for a few larger worms. You bait the stick and push it inside the basket, locking it between the sides, then cover the entrance with the lid - tying it together takes you a few good moments, but will be easier later on. You attach the entire trap to a bush and push it into the stream, far enough that it sinks entirely.
            \n\nWho knows how long it will take before something large enough swims inside. Still, it would be better to not wait for too long - otherwise, the prey may die of hunger.
            '
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ruinedvillageselectarea

    label ruinedvillage_fishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the fish trap had any luck.')
        if ruinedvillage_fishtrap_fishtimer > day:
            $ ruinedvillage_fishtrap_daychecked = day
            $ minutes += 5
            menu:
                'Unfortunately, it’s still empty.
                '
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump ruinedvillageselectarea
        elif ruinedvillage_fishtrap_fishtimer+3 > day:
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            $ d100roll += ruinedvillage_fishtrap_badthingmodifier
            $ minutes += 5
            if d100roll > 100: # harsh fail
                $ ruinedvillage_fishtrap_badthingmodifier = 0
                $ ruinedvillage_fishtrap_working = 0
                # $ ruinedvillage_fishtrap = 0
                $ ruinedvillage_fishtrap_fishtimer = 0
                $ ruinedvillage_fishtrap_daychecked = 0
                menu:
                    'Sadly, it’s not only empty, the bait is already gone. Whatever had squeezed into the trap, was small enough to catch the worms and swim outside.
                    '
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump ruinedvillageselectarea
            else: # success
                $ ruinedvillage_fishtrap_fishtimer = 0
                $ quarters += 1
                if ruinedvillage_fishtrap_badthingmodifier:
                    $ ruinedvillage_fishtrap_badthingmodifier += 10
                $ ruinedvillage_fishtrap_working = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if d100roll > 40:
                    $ item_rawfishtotalnumber += 2
                    $ item_rawfish_gaining = 2
                    $ achievement_fish += 2
                    $ renpy.notify("You caught 2 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 2 fish.{/i}')
                    $ custom1 = "You pull the rope and see two flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the stream, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                else:
                    $ item_rawfishtotalnumber += 3
                    $ item_rawfish_gaining = 3
                    $ achievement_fish += 3
                    $ renpy.notify("You caught 3 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 3 fish.{/i}')
                    $ custom1 = "You pull the rope and see three flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the stream, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                menu:
                    '[custom1]
                    '
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump ruinedvillageselectarea
        else:
            $ ruinedvillage_fishtrap_working = 0
            $ ruinedvillage_fishtrap_fishtimer = 0
            $ minutes += 5
            menu:
                'Sadly, you’re too late. Your catch has already starved to death, and is now eaten by dozens of little creatures. You open the lid and pour out the contents into the river.
                '
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump ruinedvillageselectarea

    label ruinedvillage_fishtrap03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I set the fish trap again.')
        $ ruinedvillage_fishtrap_working = day
        $ minutes += 5
        $ ruinedvillage_fishtrap = 1
        show fishtrap ruinedvillage01 at basicfade
        $ ruinedvillage_fishtrap_daychecked = day
        $ ruinedvillage_fishtrap_fishtimer = renpy.random.randint(1, 3)
        $ ruinedvillage_fishtrap_fishtimer = (ruinedvillage_fishtrap_fishtimer+day)
        menu:
            'You need to look for worms again, but at least sealing the lid takes only a moment.
            '
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ruinedvillageselectarea

    label ruinedvillage_fishtrap04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the trap back')
        $ minutes += 5
        $ item_fishtrap += 1
        $ renpy.notify("You dismantled the trap.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You dismantled the trap.{/i}')
        $ ruinedvillage_fishtrap = 0
        hide fishtrap
        $ ruinedvillage_fishtrap_daychecked = 0
        $ ruinedvillage_fishtrap_working = 0
        $ ruinedvillage_fishtrap_fishtimer = 0
        menu:
            'You shake the basket, expecting it will get drier during your ride, then attach it to your saddle.
            '
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ruinedvillageselectarea

label ruinedvillagebath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider washing myself in the river.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ custom1 = ""
    $ custom2 = ""
    if cleanliness_equipment <= 0:
        $ custom1 = "{color=#6a6a6a}You need at least 1 piece of bathing equipment to get more out of this place.{/color}"
        $ custom2 = ""
    elif cleanliness_equipment == 1:
        if item_soap:
            $ custom1 = "The oak-ash soap you own can help you get cleaner."
        elif item_teethset:
            $ custom1 = "The teeth set you own can help you get cleaner."
        elif item_perfume:
            $ custom1 = "The perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need 3 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment == 2:
        if item_soap and item_teethset:
            $ custom1 = "The oak-ash soap and the teeth set you own can help you get cleaner."
        elif item_soap and item_perfume:
            $ custom1 = "The oak-ash soap and the perfume you own can help you get cleaner."
        elif item_teethset and item_perfume:
            $ custom1 = "The teeth set and the perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need 3 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment >= 3:
        $ custom1 = "The oak-ash soap, the teeth set, and the perfume you own can help you get cleaner."
        $ custom2 = ""
    menu:
        'The living stream, filled with fish and plants, won’t help you much.
        \n\n[custom1][custom2]
        '
        'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
            jump ruinedvillagebath02
        'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump ruinedvillagebath02
        'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
            jump ruinedvillagebath02
        'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump ruinedvillageselectarea

    label ruinedvillagebath02:
        if not cleanliness:
            if cleanliness_equipment >= 3:
                $ minutes += 20
                $ cleanliness = limit_cleanliness(cleanliness+3)
                show plus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 appearance points.{/i}')
            if cleanliness_equipment >= 1:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance points.{/i}')
        elif cleanliness == 1:
            if cleanliness_equipment >= 3:
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
            'The kelp forest reaches to the water surface. Surrounded by little creatures and the smell of river plants, you crouch by the bank and draw handfuls of water.
            '
            'I put on my clothes.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ruinedvillageselectarea
