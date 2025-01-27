############################# GHOUL CAVE
default ghoulcave_firsttime = 0
default ghoulcave_fluff = ""
default ghoulcave_fluff_old = ""

default ghoulcave_wildplants_left = 5
default ghoulcave_wildplants_display = 0
default ghoulcave_horsenamecomfort = 0

default ghoulcave_cave_firsttime = 0
default ghoulcave_cave_explored = 0
default ghoulcave_cave_item = 0

default ghoulcave_ghoul_gone = ""
default ghoulcave_ghoul_timer = 0
default ghoulcave_ghoul_startled = 0
default ghoulcave_ghoul_killed = 0
default ghoulcave_ghoul_lookedat = 0
default ghoulcave_ghoul_blood = 0
default ghoulcave_ghoul_burnt = 0

default ghoulcave_fishtrap = 0
default ghoulcave_fishtrap_working = 0
default ghoulcave_fishtrap_daychecked = 0
default ghoulcave_fishtrap_fishtimer = 0
default ghoulcave_fishtrap_badthingmodifier = 0

label ghoulcave01:
    nvl clear
    $ pc_area = "ghoulcave"
    stop music fadeout 4.0
    show areapicture ghoulcave01 behind deadghoul, fishtrap at basicfade
    if ghoulcave_fishtrap:
        show fishtrap ghoulcave01 at basicfade
    play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if ghoulcave_ghoul_killed and day <= (ghoulcave_ghoul_timer+2):
        show deadghoul 01 at basicfade
    if ghoulcave_ghoul_killed and day > (ghoulcave_ghoul_timer+2) and ghoulcave_ghoul_gone == "":
        $ ghoulcave_ghoul_gone = " All that’s left of the monstrous carcass are the stains of dark blood."
    elif ghoulcave_ghoul_gone == " All that’s left of the monstrous carcass are the stains of dark blood.":
        $ ghoulcave_ghoul_gone = " "
    label ghoulcave_fluffloop:
        $ ghoulcave_fluff = renpy.random.choice(['A few of the bones by the cave entrance were recently chewed on.', 'The rustling trees echo the burbling water.', 'A family of hares flees through the lea in panic.', 'A small, gray lizard is climbing the hill, seeking the next meal with its tongue.', 'A large elk is walking down the path, and exchanges with you a nervous gaze. After it lowers its head and lets out a growl, you lead your mount through the grasses.', 'A large, red saurian is basking on the top of the crag. It observes you, but doesn’t move any closer.'])
        if ghoulcave_fluff_old == ghoulcave_fluff:
            jump ghoulcave_fluffloop
        else:
            $ ghoulcave_fluff_old = ghoulcave_fluff
    if day <= 5 and ghoulcave_wildplants_left:
        $ ghoulcave_wildplants_left = 5
    elif day <= 10 and ghoulcave_wildplants_left:
        $ ghoulcave_wildplants_left = 4
    elif day <= 15 and ghoulcave_wildplants_left:
        $ ghoulcave_wildplants_left = 3
    elif day <= 20 and ghoulcave_wildplants_left:
        $ ghoulcave_wildplants_left = 2
    elif day <= 25 and ghoulcave_wildplants_left:
        $ ghoulcave_wildplants_left = 1
    else:
        $ ghoulcave_wildplants_left = 0
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not ghoulcave_firsttime:
        $ world_known_npcs += 0
        $ world_known_areas += 1
        $ ghoulcave_firsttime = 1
        $ stonebridge_unlocked = 1
        $ giantstatue_unlocked = 1
        jump ghoulcavefirsttime01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        jump ghoulcaveregular01

label ghoulcavefirsttime01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if ghoulcave_wildplants_left == 5:
        $ custom1 = "There’s plenty of fruits and edible leaves in sight, and even some vegetables - though many of them carry marks left by rabbits’ incisors."
    elif ghoulcave_wildplants_left == 4 or ghoulcave_wildplants_left == 3:
        $ custom1 = "There’s a bunch of fruits and edible leaves in sight, though all the vegetables were already dug out by rabbits."
    elif ghoulcave_wildplants_left == 2 or ghoulcave_wildplants_left == 1:
        $ custom1 = "There’s a bunch of edible leaves in sight, though all the vegetables were already dug out by rabbits, and most of the apples have fallen on the ground."
    else:
        $ custom1 = "The vegetables were dug out by rabbits, and the apples on the ground are already rotten."
        $ ghoulcave_wildplants_display = 1
    if persistent.deafmode:
        $ deafcustom1 = "The creek’s tune is as gentle as rain, clean and bedded with countless pebbles, surrounded by the chants of insects. "
    else:
        $ deafcustom1 = ""
    menu:
        'The trail turns into a wider path, and leads you to a rocky hill. [deafcustom1]{color=#f6d6bd}[horsename]{/color} quenches its thirst, so you fill up your waterskin.
        \n\nThe trees by the road still bear signs of past trimming, giving shadow to old herbal patches, now overgrown. [custom1]
        \n\nYou glance at the cave’s entrance, and let out a sigh at the sight of bones. You could hardly squeeze inside. Fortunately, the path forward is clear.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[ghoulcave_fluff][ghoulcave_ghoul_gone]
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    show areapicture ghoulcave01 behind deadghoul, fishtrap at basicfade
    if ghoulcave_fishtrap:
        show fishtrap ghoulcave01 at basicfade
    if ghoulcave_ghoul_killed and day <= (ghoulcave_ghoul_timer+2):
        show deadghoul 01 at basicfade
    if ghoulcave_ghoul_burnt == day:
        show deadghoul 02 at basicfade
    menu:
        '{color=#f6d6bd}[horsename]{/color} is looking around, flicking back and forth with its ears.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveinside01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 1
    hide deadghoul
    show areapicture ghoulcave02 at basicfade
    hide fishtrap
    play nature "audio/ambient/ghoulcaveinside01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if ghoulcave_cave_explored:
        menu:
            'The murmuring of water fill up the chamber.
            '
            'I search the area and look for anything of value.' if not ghoulcave_cave_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area and look for anything of value.')
                jump ghoulcavelookingfortreasure01
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                jump ghoulcaveafterinteraction01
    else:
        $ ghoulcave_cave_explored = 1
        menu:
            'The ceiling is short, but you can stand upright. The corridors lead to deeper parts of the flooded chamber, but unlike the corpse eater, you can’t squeeze through them.
            \n\nYou spot no human skulls or limbs among the bones, even though there are scraps of old, moldering pants and tunics, as well as some odds and ends that belonged to victims. A comb, an old wooden club, a hood, a leather belt. Thankfully, the corpse eater has cleaned up every scrap of flesh, so there’s no stench of rotting meat.
            '
            'I search the area and look for anything of value.' if not ghoulcave_cave_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area and look for anything of value.')
                jump ghoulcavelookingfortreasure01
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                jump ghoulcaveafterinteraction01

label ghoulcavelookingfortreasure01:
    $ quarters += 1
    $ minutes += 5
    if eudocia_about_missinghunters:
        $ custom1 = "You think about your conversation with {color=#f6d6bd}Eudocia{/color}. This could have belonged to {color=#f6d6bd}Admon{/color}, and is likely still worth a coin or two."
    else:
        $ custom1 = "It’s old, but fancy - could be worth a coin or two."
    menu:
        'You return to {color=#f6d6bd}[horsename]{/color} and unpack a candle and your tinderbox, then sit on the ground and prepare the flint and the linen char cloth. Decades ago, before The Southern Invasion, people used fire strikers made of thick steel, but all you have left is a cube-like piece of harsh pyrite. It’s not the best, but enough to make a couple of sparks.
        \n\nYou put on your gloves and look underneath the remains, then into the corners. Your patience is rewarded once you spot a glitter in one of the pools. You pull it closer with a stick and find a knife with a broken blade made of steel - it carries no signs of rust yet. You consider throwing it away, but the handle is made of polished bone that was engraved with shapes of creepers and flowers. [custom1]
        '
        'I take it outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take it outside.')
            $ ghoulcave_cave_item = 1
            if not quest_missinghunters_admonfound:
                $ quest_missinghunters_admonfound = 1
            $ item_brokenknife = 1
            $ renpy.notify("You found a broken knife.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a broken knife.{/i}')
            play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            jump ghoulcaveafterinteraction01

label ghoulcavelookingatdeadghoul01:
    $ ghoulcave_ghoul_lookedat = 1
    menu:
        'The gray, wrinkled skin resembles that of an old human, but it’s hairless and clings tautly to the bones, especially the ribs. The torso is short, rectangular. The large eyes and long limbs resemble no other monster you’ve seen, not even an ape.
        \n\nYou consider cutting the shell further, but you don’t know where to start. You’ve never seen someone owning a ghoul’s {i}trophy{/i}, while putting it into a stew would poison an entire tavern.
        \n\nThe red-stained grass stinks like rotten eggs. You could collect some of the warm fluid - it’s rare, and may be valuable to an... unusual soul.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcave_ghoul_blood01:
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
        $ pc_faithpoints -= 2
    $ minutes += 5
    $ ghoulcave_ghoul_blood = 1
    $ item_ghoulblood += 1
    $ renpy.notify("You collected the corpse eater’s blood.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the corpse eater’s blood.{/i}')
    menu:
        'You put on the gloves, pick up a broad blade of grass, and carefully gather the poison.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveburningthedeadghoul01:
    $ ghoulcave_ghoul_timer = -1
    $ ghoulcave_ghoul_burnt = day
    $ achievement_pyrepoints += 1
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
        $ pc_faithpoints += 1
        $ custom1 = " You’re now a part of the endless battle between Wright’s churches and corpse eaters."
    else:
        $ custom1 = ""
    $ quarters += 2
    show deadghoul 02 at basicfade
    menu:
        'You spend some time gathering dry sticks and grass and throwing them at the carcass from as far as it takes to avoid the stench of blood. You prepare the worst torch you have, set the oil on fire, and add it to the small pile, then head to the stream to wash your blade.[custom1]
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcavecomfortinghorse01:
    $ minutes += 5
    if item_wildplants:
        $ custom1 = " and find an apple, which you cut in half. Your mount eats from your palm and lets out a relaxed snort"
    else:
        $ minutes += 3
        $ custom1 = ", but you find nothing. You spend some more time patting your mount’s side until it lets out a relaxed snort"
    menu:
        'Your palfrey is walking in place and swishes its tail. You approach it slowly, avoiding its panic. You show it the open palms of your hands and speak out some gentle nonsense. After a few minutes, you step close enough to touch its side.
        \n\nYou reach for your sack for the fresh plants[custom1].
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcavefightALL:
    label ghoulcaveinsidefirsttime01:
        $ ghoulcave_cave_firsttime = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 5
        if item_rope:
            $ custom11 = ", the rope"
        else:
            $ custom11 = ""
        menu:
            'You prepare a torch[custom11], your gloves. You can’t get too far away without putting {color=#f6d6bd}[horsename]{/color} in danger, so you don’t take any food.
            '
            'Better to check if I can get inside with my gambeson on.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better to check if I can get inside with my gambeson on.')
                $ renpy.save("combatsave", extra_info='Combat Auto Save')
                if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
                    play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
                stop nature fadeout 2.0
                menu:
                    'You should be able to squeeze in...
                    \n\nA ghastly screech cuts the air. You step back, dropping a part of your equipment. A creature is running at you.
                    '
                    'I grab my axe.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe.')
                        if pc_class == "warrior":
                            $ at_unlock_force = 1
                            $ at = 0
                        menu:
                            'The monster looks like a furless, gray, wrinkled human with stunningly long limbs. You see its bones, as if the skin hardly contains the guts. In the blink of an eye it squeezes through the entrance, bending in ways that seem impossible to you.
                            \n\nYou’ve disturbed the lair of a corpse eater.
                            '
                            'I jump forward and strike without thinking, hurting it as quickly as I can. It will be easy with the sharpening poison in me.' if item_sharpeningpotion_used and item_sharpeningpotion_used == day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump forward and strike without thinking, hurting it as quickly as I can. It will be easy with the sharpening poison in me.')
                                $ at_unlock_force = 0
                                $ at = 0
                                menu:
                                    'The beast also leaps forward, with arms and legs spread out in a lethal hug. Your axe gives you the crucial finger-length of an advantage - the blood bursts from the creature’s chest and it falls on the ground. It crawls away, flailing its arms in dread.
                                    '
                                    'I finish it off.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I finish it off.')
                                        jump ghoulcaveinsidefirsttime04killed
                                    'I take no risks. I let it run away.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take no risks. I let it run away.')
                                        jump ghoulcaveinsidefirsttime04startled
                            'I focus on dodging its charge.' ( condition="at != 'force'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on dodging its charge.')
                                $ at_unlock_force = 0
                                $ at = 0
                                jump ghoulcaveinsidefirsttime03a
                            'I jump away and take a wide swing. I need to cut deeply, doesn’t matter where.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump away and take a wide swing. I need to cut deeply, doesn’t matter where.')
                                $ at_unlock_force = 0
                                $ at = 0
                                jump ghoulcaveinsidefirsttime03a
                            'I’ll finish it off with a single cut. I hold my position and aim at the head.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll finish it off with a single cut. I hold my position and aim at the head.')
                                $ at_unlock_force = 0
                                $ at = 0
                                jump ghoulcaveinsidefirsttime03a
                            'I jump forward and strike without thinking, hurting it as quickly as I can.' if item_sharpeningpotion_used != day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump forward and strike without thinking, hurting it as quickly as I can.')
                                $ at_unlock_force = 0
                                $ at = 0
                                menu:
                                    'The beast also leaps forward, with arms and legs spread out in a lethal hug. Your axe gives you the crucial finger-length of an advantage - the blood bursts from the creature’s chest and it falls on the ground. It crawls away, flailing its arms in dread.
                                    '
                                    'I finish it off.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I finish it off.')
                                        jump ghoulcaveinsidefirsttime04killed
                                    'I take no risks. I let it run away.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take no risks. I let it run away.')
                                        jump ghoulcaveinsidefirsttime04startled
                            'I’ll slow it down by cutting its legs. I crouch slightly.' ( condition="at != 'force'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll slow it down by cutting its legs. I crouch slightly.')
                                $ at_unlock_force = 0
                                $ at = 0
                                jump ghoulcaveinsidefirsttime03a
                            'If it tries to grapple me, I can cut its arm.' ( condition="at != 'force'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it tries to grapple me, I can cut its arm.')
                                $ at_unlock_force = 0
                                $ at = 0
                                jump ghoulcaveinsidefirsttime03a
                            'It’s fast - I can’t give it an opportunity to get close. (disabled)' ( condition="at == 'force'" ):
                                pass

    label ghoulcaveinsidefirsttime03a:
        $ armor = limit_armor(armor-1)
        show minus1armor at armorchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
        menu:
            'The creature jumps at you right away, with arms and legs spread out in a lethal hug, and you’re too slow to react. Its arms cling to your own, pushing them along your sides, the legs clutch at your hips. You barely stand straight as it instantly tears through the gambeson on your back with its claws. The terrible stench doesn’t help you one bit.
            '
            'I run at the rocks to crush its shell.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run at the rocks to crush its shell.')
                jump ghoulcaveinsidefirsttime03ap02
            'I hit it with my blade.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hit it with my blade.')
                $ custom1 = "The monster’s muscles are overwhelming you. The pain starts at your back, then raises to your neck, tearing it apart. You fall down, but don’t remember the hit."
                jump ghoulcavedead
            'I try to get it off me, doing my best not to fall down.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to get it off me, doing my best not to fall down.')
                $ custom1 = "The monster’s muscles are overwhelming you. The pain starts at your back, then raises to your neck, tearing it apart. You fall down, but don’t remember the hit."
                jump ghoulcavedead
            'I let myself fall down and crush the beast’s limbs.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let myself fall down and crush the beast’s limbs.')
                $ custom1 = "Before you hit the ground the creature spreads its arms, resting its hand on the soil, then sinks its teeth in your neck, still holding you with its legs."
                jump ghoulcavedead

    label ghoulcaveinsidefirsttime03ap02:
        menu:
            'You let out a scream and charge at the wall, making the monster’s back hit it first. It lets out a terrified shriek, its grasp weakens, you set yourself free.
            '
            'No more tricks. I take a new stance and raise my blade. I’m ready now.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No more tricks. I take a new stance and raise my blade. I’m ready now.')
                if armor >= 3:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ custom1 = "It pierces through your gambeson, but doesn’t reach your flesh."
                elif armor == 2:
                    $ armor = limit_armor(armor-2)
                    show minus2armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                    $ custom1 = "It pierces through your gambeson, but doesn’t reach your flesh."
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                elif armor == 1:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        $ cleanliness_clothes_blood = 1
                        show minus2appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                    elif not cleanliness_clothes_blood:
                        $ cleanliness_clothes_blood = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    elif not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ custom1 = "It pierces through your gambeson and as it withdraws its hand, you see your blood on its claws."
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_blood:
                        $ cleanliness_clothes_blood = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ custom1 = "It pierces through your worn gambeson and as it withdraws its hand, you see your blood on its fingers."
                menu:
                    'You barely take a breath and the creature is already dashing toward you. You jump aside, taking a swing at its back, but not only it ducks beneath your blade, its claws reach your abdomen. [custom1]
                    \n\nIt gives you enough time to return the blow. You send it into the ground with a deep wound, and it lands with a thud, crying in pain. It crawls away, flailing its arms in dread.
                    '
                    'I finish it off.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I finish it off.')
                        jump ghoulcaveinsidefirsttime04killed
                    'I take no risks. I let it run away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take no risks. I let it run away.')
                        jump ghoulcaveinsidefirsttime04startled
            '{image=d6} I hurt it as quickly as I can.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I hurt it as quickly as I can.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if pc_hp >= 4:
                    $ d100roll -= 10
                if item_golemglove:
                    $ d100roll -= 10
                if item_axe03:
                    $ d100roll -= 20
                elif item_axe02 or item_axe02alt:
                    $ d100roll -= 10
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if d100roll <= 50:
                    menu:
                        'You surprise the creature and hit it in the middle of its jump. You send it into the ground with a deep wound, and it lands with a thud, crying in pain. It crawls away, flailing its arms in dread.
                        '
                        'I finish it off.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I finish it off.')
                            jump ghoulcaveinsidefirsttime04killed
                        'I take no risks. I let it run away.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take no risks. I let it run away.')
                            jump ghoulcaveinsidefirsttime04startled
                else:
                    if armor >= 3:
                        $ armor = limit_armor(armor-2)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                        $ custom1 = "It pierces through your gambeson, but doesn’t reach your flesh."
                        if not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                    elif armor == 2:
                        if pc_hp < 1:
                            $ custom1 = "You fail to surprise the creature - it jumps aside and reaches your abdomen with its claws, tearing through your stomach. Your hit lands, but is shallow - the beast’s scream lasts briefly, replaced by the splash of your guts as they hit the ground."
                            jump ghoulcavedead
                        $ armor = limit_armor(armor-2)
                        show minus2armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            $ cleanliness_clothes_blood = 1
                            show minus2appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                        elif not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        elif not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        $ custom1 = "It pierces through your gambeson and as it withdraws its hand, you see your blood on its claws."
                    elif armor == 1:
                        if pc_hp < 2:
                            $ custom1 = "You fail to surprise the creature - it jumps aside and reaches your abdomen with its claws, tearing through your stomach. Your hit lands, but is shallow - the beast’s scream lasts briefly, replaced by the splash of your guts as they hit the ground."
                            jump ghoulcavedead
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ pc_hp = limit_pc_hp(pc_hp-2)
                        show minus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                        if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            $ cleanliness_clothes_blood = 1
                            show minus2appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                        elif not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        elif not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        $ custom1 = "It pierces through your gambeson and as it withdraws its hand, you see your blood on its claws."
                    else:
                        if pc_hp < 3:
                            $ custom1 = "You fail to surprise the creature - it jumps aside and reaches your abdomen with its claws, tearing through your stomach. Your hit lands, but is shallow - the beast’s scream lasts briefly, replaced by the splash of your guts as they hit the ground."
                            jump ghoulcavedead
                        $ pc_hp = limit_pc_hp(pc_hp-3)
                        show minus3hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                        if not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        $ custom1 = "It pierces through your worn gambeson and as it withdraws its hand, you see your blood on its fingers."
                    menu:
                        'You fail to surprise the creature - it jumps aside and reaches your abdomen with its claws. Still, it gives you enough time to return the blow. You send it into the ground with a shallow wound, and it lands on its knee, crying in pain. You exchange a quick glance, then it dashes away.
                        '
                        'I won’t be able to catch up with it.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I won’t be able to catch up with it.')
                            jump ghoulcaveinsidefirsttime04startledalt

label ghoulcaveinsidefirsttime04killed:
    stop music fadeout 4.0
    play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ ghoulcave_ghoul_killed = 1
    $ pc_battlecounter += 1
    $ ghoulcave_ghoul_timer = day
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
        $ pc_faithpoints_opportunities += 1
    if ghoulcave_ghoul_killed and day <= (ghoulcave_ghoul_timer+2):
        show deadghoul 01 at basicfade
    menu:
        'You catch up with it as it turns on its back. You sink the blade in its torso, once, twice, more - until it stops moving. Its raised arms stay still for a moment, then rest on grass. The dark nails, longer than the rest of its hands, lie still.
        \n\nYour breath slows down. The carcass smells of unwashed sweat and rotting flesh.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveinsidefirsttime04startled:
    stop music fadeout 4.0
    play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ ghoulcave_ghoul_startled = 1
    $ achievement_animalssavedpoints += 1
    $ pc_battlecounter += 1
    menu:
        'It gets back on its feet and flees up the road, then climbs up the crag, as swiftly as an ibex. You could swear its arms have two elbows each, and that it could catch up with {color=#f6d6bd}[horsename]{/color} at a short distance.
        \n\nYour breath slows down. The blood on you axe smells of unwashed sweat and rotting flesh. You wash it at the stream.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcaveinsidefirsttime04startledalt:
    stop music fadeout 4.0
    play nature "audio/ambient/ghoulcave01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ ghoulcave_ghoul_startled = 1
    $ achievement_animalssavedpoints += 1
    $ pc_battlecounter += 1
    menu:
        'It runs up the road, then climbs up the crag, as swiftly as an ibex. You could swear its arms have two elbows each, and that it could catch up with {color=#f6d6bd}[horsename]{/color} at a short distance.
        \n\nYour breath slows down. The blood on you axe smells of unwashed sweat and rotting flesh. You wash it at the stream.
        '
        'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
            jump ghoulcaveburningthedeadghoul01
        'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
            jump ghoulcavelookingatdeadghoul01
        'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
            jump ghoulcave_ghoul_blood01
        'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
            jump ghoulcaveburningthedeadghoul01
        'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
            jump ghoulcaveinsidefirsttime01
        '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
            $ ghoulcave_horsenamecomfort = 1
            jump ghoulcavecomfortinghorse01
        'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
            jump ghoulcaveinside01
        'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
            jump ghoulcaveforaging01
        'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
            jump ghoulcaveforaging01
        'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
            jump ghoulcaveforaging01
        'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
            jump ghoulcaveforaging01
        'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
            jump ghoulcaveforaging01
        'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
            pass
        ######################################
        'I consider cleaning myself in the stream.':
            jump ghoulcavestream01
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
            jump ghoulcave_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
            jump ghoulcave_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
            jump ghoulcave_fishtrap03
        'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
            jump ghoulcave_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
            pass

label ghoulcavedead:
    $ pc_hp = 0
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    menu:
        '[custom1]
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        'Let me replay this combat.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this combat.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")

######################################

label ghoulcaveforaging01:
    $ ghoulcave_wildplants_display = 1
    if ghoulcave_wildplants_left == 5:
        $ item_wildplants += 5
        $ achievement_wildplants += 5
        $ renpy.notify("You picked 5 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 5 bunches of wild plants.{/i}')
        $ quarters += 6
        $ custom1 = "You pick apples and plums, as well as overripe sorb fruits - for a moment you think about a sweet pie they could serve in. The wild strawberries are tiny, but delicious.\n\nWhen it comes to vegetables, there’s more of them than you could use. A home dweller would turn them into a stew, but as a traveler you limit yourself to those you can eat raw: cabbages, lettuce, and a few types of sorrel, from purple to pink. You leave the onions behind."
    elif ghoulcave_wildplants_left == 4:
        $ item_wildplants += 4
        $ achievement_wildplants += 4
        $ renpy.notify("You picked 4 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 4 bunches of wild plants.{/i}')
        $ quarters += 4
        $ custom1 = "You pick apples and plums, and a few overripe sorb fruits, but leave many more to rot further in the grass. The wild strawberries are tiny, but delicious.\n\nWhen it comes to vegetables, there’s more of them than you could use. A home dweller would turn them into a stew, but as a traveler you limit yourself to those you can eat raw: cabbages, lettuce, and a few types of sorrel, from purple to pink. You leave the onions behind."
    elif ghoulcave_wildplants_left == 3:
        $ item_wildplants += 3
        $ achievement_wildplants += 3
        $ renpy.notify("You picked 3 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 3 bunches of wild plants.{/i}')
        $ quarters += 3
        $ custom1 = "You pick apples and plums, but have to spend some time throwing away those that give home to worms and ants. The wild strawberries are tiny, but delicious. The sorb fruits are already rotting among the grasses.\n\nWhen it comes to vegetables, there’s still plenty of them. A home dweller would turn them into a stew, but as a traveler you limit yourself to those you can eat raw: cabbages, lettuce, and a few types of sorrel, from purple to pink. You leave the onions behind."
    elif ghoulcave_wildplants_left == 2:
        $ item_wildplants += 2
        $ achievement_wildplants += 2
        $ renpy.notify("You picked 2 bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 2 bunches of wild plants.{/i}')
        $ quarters += 2
        $ custom1 = "The sorb fruits are already rotting among the grasses, while the wild strawberries are overrun by ants. You find a few apples and plums, but half of them give shelter to worms.\n\nYou find more luck with vegetables. A home dweller would turn them into a stew, but as a traveler you limit yourself to those you can eat raw: lettuce, a single cabbage, and a few types of sorrel, from purple to pink. Raw onions won’t be tasty, but you don’t have a better option."
    else:
        $ item_wildplants += 1
        $ achievement_wildplants += 1
        $ renpy.notify("You picked a bunch of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a bunch of wild plants.{/i}')
        $ quarters += 2
        $ custom1 = "The sorb fruits are already rotting among the grasses, while the wild strawberries are overrun by ants. Since most of the remaining fruits give shelter to worms, you pick only a few apples and plums. The lettuce and cabbages are gone - all that’s left is purple sorrel and raw onions."
    $ ghoulcave_wildplants_left = 0
    menu:
        '[custom1]
        '
        'I wash everything in the stream and spread the plants among my bundles.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash everything in the stream and spread the plants among my bundles.')
            jump ghoulcaveafterinteraction01

label ghoulcave_fishtrapALL:
    label ghoulcave_fishtrap01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend some time setting up a fish trap at the bank.')
        show fishtrap ghoulcave01 at basicfade
        $ quarters += 2
        $ item_fishtrap -= 1
        $ ghoulcave_fishtrap = 1
        $ ghoulcave_fishtrap_daychecked = day
        $ ghoulcave_fishtrap_working = day
        $ ghoulcave_fishtrap_fishtimer = renpy.random.randint(1, 3)
        $ ghoulcave_fishtrap_fishtimer = (ghoulcave_fishtrap_fishtimer+day)
        menu:
            'You place the basket on the ground, then grab a bowl and start digging, looking for a few larger worms. You bait the stick and push it inside the basket, locking it between the sides, then cover the entrance with the lid - tying it together takes you a few good moments, but will be easier later on. You lock the entire trap between the rocks, moving it around to make sure it stays in place.
            \n\nWho knows how long it will take before something large enough swims inside. Still, it would be better to not wait for too long - otherwise, the prey may die of hunger.
            '
            'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                jump ghoulcaveburningthedeadghoul01
            'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                jump ghoulcavelookingatdeadghoul01
            'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                jump ghoulcaveburningthedeadghoul01
            'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                jump ghoulcaveinsidefirsttime01
            '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                $ ghoulcave_horsenamecomfort = 1
                jump ghoulcavecomfortinghorse01
            'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                jump ghoulcaveinside01
            'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                jump ghoulcaveforaging01
            'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                jump ghoulcaveforaging01
            'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                jump ghoulcaveforaging01
            'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                jump ghoulcaveforaging01
            'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                jump ghoulcaveforaging01
            'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                pass
            ######################################
            'I consider cleaning myself in the stream.':
                jump ghoulcavestream01
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                jump ghoulcave_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                jump ghoulcave_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                jump ghoulcave_fishtrap03
            'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                jump ghoulcave_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                pass

    label ghoulcave_fishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the fish trap had any luck.')
        if ghoulcave_fishtrap_fishtimer > day:
            $ ghoulcave_fishtrap_daychecked = day
            $ minutes += 5
            menu:
                'Unfortunately, it’s still empty.
                '
                'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                    jump ghoulcaveburningthedeadghoul01
                'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                    jump ghoulcavelookingatdeadghoul01
                'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                    jump ghoulcave_ghoul_blood01
                'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                    jump ghoulcave_ghoul_blood01
                'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                    jump ghoulcaveburningthedeadghoul01
                'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                    jump ghoulcaveinsidefirsttime01
                '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                    $ ghoulcave_horsenamecomfort = 1
                    jump ghoulcavecomfortinghorse01
                'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                    jump ghoulcaveinside01
                'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                    jump ghoulcaveforaging01
                'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                    jump ghoulcaveforaging01
                'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                    jump ghoulcaveforaging01
                'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                    jump ghoulcaveforaging01
                'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                    jump ghoulcaveforaging01
                'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                    pass
                ######################################
                'I consider cleaning myself in the stream.':
                    jump ghoulcavestream01
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                    jump ghoulcave_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                    jump ghoulcave_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                    jump ghoulcave_fishtrap03
                'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                    jump ghoulcave_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                    pass
        elif ghoulcave_fishtrap_fishtimer+3 > day:
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            $ d100roll += ghoulcave_fishtrap_badthingmodifier
            $ minutes += 5
            if not ghoulcave_ghoul_killed and not ghoulcave_ghoul_startled: # harsh fail
                $ ghoulcave_fishtrap_badthingmodifier = 0
                $ ghoulcave_fishtrap_working = 0
                # $ ghoulcave_fishtrap = 0
                $ ghoulcave_fishtrap_fishtimer = 0
                $ ghoulcave_fishtrap_daychecked = 0
                menu:
                    'Sadly, it’s unsealed and empty. A human, or an unusually dextrous, creature was able to steal your catch.
                    '
                    'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                        jump ghoulcaveburningthedeadghoul01
                    'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                        jump ghoulcavelookingatdeadghoul01
                    'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                        jump ghoulcave_ghoul_blood01
                    'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                        jump ghoulcave_ghoul_blood01
                    'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                        jump ghoulcaveburningthedeadghoul01
                    'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                        jump ghoulcaveinsidefirsttime01
                    '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                        $ ghoulcave_horsenamecomfort = 1
                        jump ghoulcavecomfortinghorse01
                    'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                        jump ghoulcaveinside01
                    'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                        jump ghoulcaveforaging01
                    'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                        jump ghoulcaveforaging01
                    'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                        jump ghoulcaveforaging01
                    'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                        jump ghoulcaveforaging01
                    'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                        jump ghoulcaveforaging01
                    'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                        pass
                    ######################################
                    'I consider cleaning myself in the stream.':
                        jump ghoulcavestream01
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                        jump ghoulcave_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                        jump ghoulcave_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                        jump ghoulcave_fishtrap03
                    'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                        jump ghoulcave_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                        pass
            else: # success
                $ ghoulcave_fishtrap_fishtimer = 0
                $ quarters += 1
                if ghoulcave_fishtrap_badthingmodifier:
                    $ ghoulcave_fishtrap_badthingmodifier += 10
                $ ghoulcave_fishtrap_working = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if d100roll > 50:
                    $ item_rawfishtotalnumber += 1
                    $ achievement_fish += 1
                    $ item_rawfish_gaining = 1
                    $ renpy.notify("You caught a fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught a fish.{/i}')
                    $ custom1 = "you lift the trap and see a flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animal with two careful blows in the top of its head, then finish it off with a knife, cutting it underneath the gill plate. You spend another minute or two bleeding out the fish in the creek, then cover it with a waxed linen sheet.\n\nYou should eat it soon, before it spoils."
                else:
                    $ item_rawfishtotalnumber += 2
                    $ achievement_fish += 2
                    $ item_rawfish_gaining = 2
                    $ renpy.notify("You caught 2 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 2 fish.{/i}')
                    $ custom1 = "you lift the trap and see two flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the creek, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                menu:
                    '[custom1]
                    '
                    'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                        jump ghoulcaveburningthedeadghoul01
                    'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                        jump ghoulcavelookingatdeadghoul01
                    'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                        jump ghoulcave_ghoul_blood01
                    'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                        jump ghoulcave_ghoul_blood01
                    'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                        jump ghoulcaveburningthedeadghoul01
                    'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                        jump ghoulcaveinsidefirsttime01
                    '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                        $ ghoulcave_horsenamecomfort = 1
                        jump ghoulcavecomfortinghorse01
                    'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                        jump ghoulcaveinside01
                    'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                        jump ghoulcaveforaging01
                    'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                        jump ghoulcaveforaging01
                    'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                        jump ghoulcaveforaging01
                    'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                        jump ghoulcaveforaging01
                    'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                        jump ghoulcaveforaging01
                    'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                        pass
                    ######################################
                    'I consider cleaning myself in the stream.':
                        jump ghoulcavestream01
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                        jump ghoulcave_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                        jump ghoulcave_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                        jump ghoulcave_fishtrap03
                    'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                        jump ghoulcave_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                        pass
        else:
            $ ghoulcave_fishtrap_working = 0
            $ ghoulcave_fishtrap_fishtimer = 0
            $ minutes += 5
            menu:
                'Sadly, you’re too late. Your catch has already starved to death, and is now eaten by dozens of little creatures. You open the lid and pour out the contents into the creek.
                '
                'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                    jump ghoulcaveburningthedeadghoul01
                'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                    jump ghoulcavelookingatdeadghoul01
                'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                    jump ghoulcave_ghoul_blood01
                'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                    jump ghoulcave_ghoul_blood01
                'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                    jump ghoulcaveburningthedeadghoul01
                'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                    jump ghoulcaveinsidefirsttime01
                '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                    $ ghoulcave_horsenamecomfort = 1
                    jump ghoulcavecomfortinghorse01
                'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                    jump ghoulcaveinside01
                'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                    jump ghoulcaveforaging01
                'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                    jump ghoulcaveforaging01
                'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                    jump ghoulcaveforaging01
                'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                    jump ghoulcaveforaging01
                'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                    jump ghoulcaveforaging01
                'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                    pass
                ######################################
                'I consider cleaning myself in the stream.':
                    jump ghoulcavestream01
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                    jump ghoulcave_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                    jump ghoulcave_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                    jump ghoulcave_fishtrap03
                'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                    jump ghoulcave_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                    pass

    label ghoulcave_fishtrap03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I set the fish trap again.')
        $ ghoulcave_fishtrap_working = day
        $ minutes += 5
        $ ghoulcave_fishtrap = 1
        show fishtrap ghoulcave01 at basicfade
        $ ghoulcave_fishtrap_daychecked = day
        $ ghoulcave_fishtrap_fishtimer = renpy.random.randint(1, 4)
        $ ghoulcave_fishtrap_fishtimer = (ghoulcave_fishtrap_fishtimer+day)
        menu:
            'You need to look for worms again, but at least sealing the lid takes only a moment.
            '
            'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                jump ghoulcaveburningthedeadghoul01
            'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                jump ghoulcavelookingatdeadghoul01
            'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                jump ghoulcaveburningthedeadghoul01
            'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                jump ghoulcaveinsidefirsttime01
            '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                $ ghoulcave_horsenamecomfort = 1
                jump ghoulcavecomfortinghorse01
            'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                jump ghoulcaveinside01
            'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                jump ghoulcaveforaging01
            'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                jump ghoulcaveforaging01
            'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                jump ghoulcaveforaging01
            'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                jump ghoulcaveforaging01
            'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                jump ghoulcaveforaging01
            'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                pass
            ######################################
            'I consider cleaning myself in the stream.':
                jump ghoulcavestream01
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                jump ghoulcave_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                jump ghoulcave_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                jump ghoulcave_fishtrap03
            'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                jump ghoulcave_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                pass

    label ghoulcave_fishtrap04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the trap back')
        $ minutes += 5
        $ item_fishtrap += 1
        $ renpy.notify("You dismantled the trap.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You dismantled the trap.{/i}')
        $ ghoulcave_fishtrap = 0
        hide fishtrap
        $ ghoulcave_fishtrap_daychecked = 0
        $ ghoulcave_fishtrap_working = 0
        $ ghoulcave_fishtrap_fishtimer = 0
        menu:
            'You shake the basket, expecting it will get drier during your ride, then attach it to your saddle.
            '
            'My faith teaches that I should burn this monster “without delay.”' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_blood and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My faith teaches that I should burn this monster “without delay.”')
                jump ghoulcaveburningthedeadghoul01
            'I take a closer look at the dead corpse eater.' if ghoulcave_ghoul_killed and not ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the dead corpse eater.')
                jump ghoulcavelookingatdeadghoul01
            'It may be sinful, but I fill up a phial with the creature’s blood.' if (pc_religion == "theunitedchurch" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be sinful, but I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I fill up a phial with the creature’s blood.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and ghoulcave_ghoul_lookedat and not ghoulcave_ghoul_blood and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill up a phial with the creature’s blood.')
                jump ghoulcave_ghoul_blood01
            'I better burn this monster.' if (pc_religion == "unknown" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "pagan" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "none" and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "theunitedchurch" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "ordersoftruth" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)) or (pc_religion == "fellowship" and ghoulcave_ghoul_blood and ghoulcave_ghoul_killed and not ghoulcave_ghoul_burnt and day <= (ghoulcave_ghoul_timer+2)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better burn this monster.')
                jump ghoulcaveburningthedeadghoul01
            'I tether {color=#f6d6bd}[horsename]{/color} to a withered shrub. I take my axe and approach the cave.' if not ghoulcave_cave_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to a withered shrub. I take my axe and approach the cave.' %horsename)
                jump ghoulcaveinsidefirsttime01
            '{color=#f6d6bd}[horsename]{/color} is afraid. I should calm it down.' if (ghoulcave_ghoul_killed and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)) or (ghoulcave_ghoul_startled and pc_likeshorsename and not ghoulcave_horsenamecomfort and not day > (ghoulcave_ghoul_timer)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}%s{/color} is afraid. I should calm it down.' %horsename)
                $ ghoulcave_horsenamecomfort = 1
                jump ghoulcavecomfortinghorse01
            'I return to the cave.' if ghoulcave_cave_firsttime and not ghoulcave_cave_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the cave.')
                jump ghoulcaveinside01
            'I forage for plants for even more than an hour.' if ghoulcave_wildplants_left == 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can find a lot of food here. I’m ready to spend even more than an hour on that.')
                jump ghoulcaveforaging01
            'I forage for plants for an hour or so.' if ghoulcave_wildplants_left == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for an hour or so.')
                jump ghoulcaveforaging01
            'I forage for plants for about an hour.' if ghoulcave_wildplants_left == 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for plants for about an hour.')
                jump ghoulcaveforaging01
            'I forage for the remaining plants for half an hour or so.' if ghoulcave_wildplants_left == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I forage for the remaining plants for half an hour or so.')
                jump ghoulcaveforaging01
            'For half an hour or so I forage for the plants the animals left behind.' if ghoulcave_wildplants_left == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- For half an hour or so I forage for the plants the animals left behind.')
                jump ghoulcaveforaging01
            'The wild animals have managed to take care of the edible plants before me. (disabled)' if ghoulcave_wildplants_left == 0 and not ghoulcave_wildplants_display:
                pass
            ######################################
            'I consider cleaning myself in the stream.':
                jump ghoulcavestream01
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not ghoulcave_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters <= (world_daylength-8)" ):
                jump ghoulcave_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not ghoulcave_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked != day:
                jump ghoulcave_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if ghoulcave_fishtrap and ghoulcave_fishtrap_working and ghoulcave_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working:
                jump ghoulcave_fishtrap03
            'I take the fish trap back.' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and not item_fishtrap:
                jump ghoulcave_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if ghoulcave_fishtrap and not ghoulcave_fishtrap_working and item_fishtrap:
                pass

label ghoulcavestreamALL:
    label ghoulcavestream01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider cleaning myself in the stream.')
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
            'You can sit down in the creek and wash yourself like in a bathtub.
            \n\n[custom1][custom2]
            '
            'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump ghoulcavestreamwashing01
            'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump ghoulcavestreamwashing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.')
                jump ghoulcavestreamlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ghoulcaveafterinteraction01

    label ghoulcavestreamwashing01:
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
            'You take a moment to relax in the gentle, clean water.
            '
            'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump ghoulcavestreamwashing01
            'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump ghoulcavestreamwashing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.')
                jump ghoulcavestreamlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ghoulcaveafterinteraction01

    label ghoulcavestreamlaundry01:
        $ cleanliness_clothes_blood = 0
        $ quarters += 2
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'You soak and rub the fabric in the crystal clear water and, when necessary, you pound them on the flat rocks. It takes you hardly any time.
            '
            'I wash my shell.' if cleanliness < 2 and cleanliness_equipment < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump ghoulcavestreamwashing01
            'I wash my shell carefully.' if cleanliness < 3 and cleanliness_equipment >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump ghoulcavestreamwashing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a great spot to remove blood stains from my clothes. It will take me half an hour or so.')
                jump ghoulcavestreamlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump ghoulcaveafterinteraction01
