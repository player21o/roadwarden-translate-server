###################### ruinedshelter
default ruinedshelter_name = "An Abandoned Place" # The Ruined Shelter, The Dusk Foxes’ Shelter
default ruinedshelter_firsttime = 0
default ruinedshelter_firsttime00b = 0
default ruinedshelter_firsttime00c = 0
default ruinedshelter_firsttime00d = 0
default ruinedshelter_fluff = ""
default ruinedshelter_fluff_old = ""
default ruinedshelter_horsename_fluff = ""
default ruinedshelter_horsename_fluff_old = ""

default ruinedshelter_mushrooms = 0
default ruinedshelter_lefttobeasts = 0
default ruinedshelter_ruin_cleared = 0
default ruinedshelter_bushes = 0 # 1 - interacted with, 2 - removed
default ruinedshelter_bushes_cut = 0

default ruinedshelter_duskfoxes_axe = 0
default ruinedshelter_duskfoxes_axe_prepared = 0
default ruinedshelter_duskfoxes_defeated = 0
default ruinedshelter_duskfoxes_hp = 3
default ruinedshelter_duskfoxes_wounded = 0
default ruinedshelter_duskfoxes_dayofgettinghurt = 0
default ruinedshelter_duskfoxes_lookedat = 0
default ruinedshelter_duskfoxes_item = 0 # wand, shield, blindingpowder
default ruinedshelter_duskfoxes_item_wandused = 0
default ruinedshelter_duskfoxes_item_blindingpowderused = 0
default ruinedshelter_duskfoxes_dmgtopc = 0
default ruinedshelter_duskfoxes_scared = 0 # day
default ruinedshelter_duskfoxes_scarring = 0

label ruinedshelter01:
    nvl clear
    $ pc_area = "ruinedshelter"
    if (not ruinedshelter_firsttime) or (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated) or (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_hp <= 0) or (ruinedshelter_duskfoxes_hp <= 0 and ruinedshelter_duskfoxes_dayofgettinghurt and ruinedshelter_duskfoxes_dayofgettinghurt != day):
        stop music fadeout 4.0
        play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    else:
        stop nature fadeout 2.0
        if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
            play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    if ruinedshelter_ruin_cleared:
        show areapicture ruinedshelter02 at basicfade behind ruinedshelteraxe
    elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
        show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
    elif ruinedshelter_firsttime00b:
        if ruinedshelter_firsttime00c:
            show areapicture ruinedshelter00c at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00d:
            show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00b at basicfade behind ruinedshelteraxe
    else:
        show areapicture ruinedshelter00a at basicfade behind ruinedshelteraxe
    if ruinedshelter_duskfoxes_axe:
        show ruinedshelteraxe 02 at basicfade
    elif ruinedshelter_bushes_cut:
        show ruinedshelteraxe 01 at basicfade
    label ruinedshelter_fluffloop:
        $ ruinedshelter_fluff = renpy.random.choice(['The shelter hasn’t changed much since your last visit. New leaves are crowding the ground, the grass climbs up the walls slowly.', 'Through the open gate, you spot two brown rats, observing you from behind a mushroom. They flee from your gaze into the tall grasses.', 'A small family of gray ibexes is climbing up the rock face, with confidence only matched by their dexterity.', 'You notice new nut shells and fruit chunks spread around in the grass. A squirrel observes you curiously from the top of the nearby tree.', 'When you get closer to the gate, a flock of red and gray birds takes-off from the walls and the wooden beams of the ruin.'])
        if ruinedshelter_fluff_old == ruinedshelter_fluff:
            jump ruinedshelter_fluffloop
        else:
            $ ruinedshelter_fluff_old = ruinedshelter_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")

    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ manacost = 2
    if not ruinedshelter_firsttime:
        $ world_known_areas += 1
        $ ruinedshelter_firsttime = 1
        $ bogentrance_unlocked = 1
        $ northernroad_unlocked = 1
        jump ruinedshelterfirsttime01
    elif ruinedshelter_duskfoxes_hp <= 0 and not ruinedshelter_duskfoxes_defeated:
        $ ruinedshelter_duskfoxes_defeated = 1
        jump ruinedshelterregular01defeatfirsttime
    elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated:
        jump ruinedshelterregular01
    elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c:
        jump ruinedshelterbeforecombat01
    else:
        jump ruinedshelterfirsttime02

label ruinedshelterfirsttime01all:
    label ruinedshelterfirsttime01:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if persistent.deafmode:
            $ deafcustom1 = "\n\nThe air is fresh, and the wind shakes the tree crowns gently. Birds are feasting, singing, and crowing above you, not afraid of any threats. You don’t notice any worrisome sounds."
        else:
            $ deafcustom1 = " The air is fresh, and the wind shakes the tree crowns gently."
        menu:
            'At the top of the hill you reach a stone wall, a quiet place with no smoke coming from behind it. You look inside and see the glimpse of a peaceful ruin. While the main road is beaten and easy for hooves to trod, the destroyed gate and the remains of the front yard have almost been reclaimed by the short grasses.
            \n\nYou seek any suspicious movement, but the place seems to be free of inhabitants larger than a falcon.[deafcustom1]
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f

    label ruinedshelterfirsttime02: # player wasn't in ruinedshelter_firsttime00c yet, maybe even not in ruinedshelter_firsttime00b
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'The place hasn’t changed much since your last visit, though you notice some fresh paw prints in the yard.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f

    label ruinedshelterbeforecombat01: # player was in ruinedshelter_firsttime00c but not ruinedshelter_duskfoxes_defeated
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if ruinedshelter_duskfoxes_hp > 0 or not ruinedshelter_duskfoxes_dayofgettinghurt or ruinedshelter_duskfoxes_dayofgettinghurt == day:
            menu:
                'Soon after your arrival, the largest of the dusk foxes jumps on the building’s wall, growling. It stretches out its shell, ready to jump at you any moment now. You hear the whine of another pack member, followed by the rest of the creatures, the youngest of which seem more scared than threatening.
                '
                'I enter the yard.' if not ruinedshelter_firsttime00b:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                    jump ruinedshelterfirsttime01b
                'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                    jump ruinedshelterfirsttime01c
                'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                    jump ruinedshelterfirsttime01d
                'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                    jump ruinedshelterfirsttimepreparingaxe01d2
                'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                    pass
                'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                    pass
                'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                    jump ruinedshelterfirsttime01e
                'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                    jump ruinedshelterfirsttime01scaringaway
                'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                    pass
                'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                    pass
                'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                    jump ruinedshelterfirsttime01f
        else:
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            menu:
                'You look around and listen carefully to any signs of dusk foxes’ presence, but you notice no such thing. There are, however, bloodstains on the beaten path, surrounded with fresh paw marks. They’re leading into the southern forest.
                \n\nMaybe their wounds scared the creatures away from this place.
                '
                'I want to look around.' if not ruinedshelter_bushes or not ruinedshelter_mushrooms:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                    if not tutorial_input:
                        $ tutorial_input = 1
                    python:
                        search = renpy.input("What are you looking for, or paying attention to? (example: gate)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    $ tutorial_input = 2
                    jump searchruinedshelter
                'There isn’t much left for me to do here. (disabled)' if ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared and ruinedshelter_mushrooms:
                    pass
                'I approach the bushes growing next to the rock face.' if ruinedshelter_bushes == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the bushes growing next to the rock face.')
                    jump ruinedshelter_bushes01
                'I enter the ruined building.' if not ruinedshelter_ruin_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the ruined building.')
                    jump ruinedshelterinteractingwithhouse01

    label ruinedshelterfirsttime01b: # I enter the yard.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ ruinedshelter_firsttime00b = 1
        show areapicture ruinedshelter00b at basicfade behind ruinedshelteraxe
        menu:
            'The hamlet could be a hunter’s shelter, a military outpost, or a storehouse for traders, but you spot no fresh human trails. The damaged door and gate are years old, soggy and moldy, and judging by the squirrels, birds, and the animal feces you see in the grass, this place is but a part of the wilderness.
            \n\nThe roof collapsed only a few years back, turning into food for mushrooms. The outer wall looks generations old, but it used to be maintained. Some of its materials came from different times and areas.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f
            'I get back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                jump ruinedshelterfirsttime01g

    label ruinedshelterfirsttime01d: # I enter the building.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ ruinedshelter_firsttime00d = 1
        $ ruinedshelter_name = "The Ruined Shelter"
        if ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
            show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
        menu:
            'It’s a simple chamber with no furniture that would explain its purpose. The fireplace is buried beneath the roof. You inspect the walls, made of hundreds of small rocks dressed with a chisel.
            \n\nThe trash is heavy from the moisture. You push it with your boot, what starts a commotion among gray, disoriented bugs. Removing the rubble would take some effort, but for now it doesn’t look like there’s anything of value left behind. With enough wood, a group of builders could restore this hamlet in just a few days.
            \n\nYou hear a rustle coming from the backyard. You look through the crumbling wall and notice the movement of a reddish fur. Not a tall creature.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f
            'I get back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                jump ruinedshelterfirsttime01g

    label ruinedshelterfirsttimepreparingaxe01d2: #I prepare my axe.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ ruinedshelter_duskfoxes_axe_prepared = 1
        menu:
            'Its touch calms you down. The sounds of animal steps are careful and light.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f
            'I get back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                jump ruinedshelterfirsttime01g

    label ruinedshelterfirsttime01f: # This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'Are you sure you want to leave this place to its fate?
            '
            'Actually...':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually...')
                jump ruinedshelterfirsttime01g
            'That’s right. I get in the saddle and ride away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- That’s right. I get in the saddle and ride away.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ ruinedshelter_name = "Dusk Foxes’ Shelter"
                $ ruinedshelter_lefttobeasts = 1
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03alt = "I don’t think humans should disturb the dusk foxes at the shelter in the west."
                $ achievement_animalssavedpoints += 2
                stop music fadeout 4.0
                play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                menu:
                    'The dusk foxes observe you as you climb up the saddle. They’re growling and walking in circles. One of the pups knocks down their sibling, starting a playful fight.
                    '
                    'There’s no reason to bother them. (disabled)':
                        pass

    label ruinedshelterfirsttime01g: # I get back to {color=#f6d6bd}[horsename]{/color}.
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'You’re ready for the further journey.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f

    label ruinedshelterfirsttime01c: # I go behind the building.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ ruinedshelter_firsttime00c = 1
        stop nature fadeout 2.0
        if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
            play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
        $ ruinedshelter_duskfoxes_scared = day
        if ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
            show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00c at basicfade behind ruinedshelteraxe
        if pc_class == "warrior":
            $ at_unlock_force = 1
            $ at = 0
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'The chaos sparks right after you approach the tree stump. The dusk foxes’ growls sound like a mix of an obnoxious bird and an infant. One of the animals, standing only a few feet away from you, is jumping and showcasing its tiny, sharp teeth and a raccoon-like black mask on its little head. The animal, with its thick, brownish-gray fur, seems more stout than any red fox.
            \n\nThe second loud creature jumps onto a table made of a halved trunk. Unlike the first one, it has a brighter, golden fur. It bends one of its forelegs, observing you with its dark eyes, not furious, nor scared, rather sad and protective. Its growl turns into a miserable whine.
            \n\nThe beasts are not even waist-high, but their number may be an issue. There’s yet another sound coming from behind you, and even more from the bushes nearby.
            '
            '{image=d6} No time to wait. I kick one of them as quickly as I can.' ( condition="at != 'knowledge' and at != 'force' and not ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I kick one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} No time to wait. I cut one of them as quickly as I can.' ( condition="at != 'knowledge' and at != 'force' and ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I cut one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.' ( condition="at != 'knowledge' and at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.')
                jump ruinedshelterfirsttime01cblock
            'I step away and try to count them.' ( condition="at != 'knowledge' and at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away and try to count them.')
                jump ruinedshelterfirsttime01ccountfail
            'I have enough time to judge the situation clearly.' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have enough time to judge the situation clearly.')
                jump ruinedshelterfirsttime01ccountscholar
            'It shouldn’t be too hard to dodge their attack. I’ll keep myself safe and take a better look at the situation.' ( condition="at == 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It shouldn’t be too hard to dodge their attack. I’ll keep myself safe and take a better look at the situation.')
                jump ruinedshelterfirsttime01ccountwarrior

    label ruinedshelterfirsttime01ccountscholar:
        $ at_unlock_force = 0
        $ at_unlock_knowledge = 0
        $ at = 0
        $ ruinedshelter_duskfoxes_lookedat = 1
        menu:
            'You take a quick glance and memorize your surroundings. There’s three large creatures in your proximity - the third one is right behind you, and while loud, it’s lumbering on its paws. The noises from the bushes belong to little pups, most likely harmless, though they are doing their best to imitate their guardians.
            \n\nYour sharp senses allow you to react right away.
            '
            '{image=d6} No time to wait. I kick one of them as quickly as I can.' ( condition="not ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I kick one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} No time to wait. I cut one of them as quickly as I can.' ( condition="ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I cut one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.')
                jump ruinedshelterfirsttime01cblock
            'Since the one behind me is weaker than the others, I run for it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the one behind me is weaker than the others, I run for it.')
                jump ruinedshelterrunningawayfromduskfoxes01

    label ruinedshelterfirsttime01ccountwarrior:
        $ at_unlock_force = 0
        $ at_unlock_knowledge = 0
        $ at = 0
        $ ruinedshelter_duskfoxes_lookedat = 1
        menu:
            'You take a quick glance and evade the creature in front of you as it tries to bite your leg, then you take a wide swing to scare away the third large creature - it was standing right behind you, and while loud, it’s lumbering on its paws. The noises from the bushes belong to little pups, most likely harmless, though they are doing their best to imitate their guardians.
            '
            '{image=d6} No time to wait. I kick one of them as quickly as I can.' ( condition="not ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I kick one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} No time to wait. I cut one of them as quickly as I can.' ( condition="ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I cut one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.')
                jump ruinedshelterfirsttime01cblock
            'Since the one behind me has already moved back, I run for it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the one behind me has already moved back, I run for it.')
                jump ruinedshelterrunningawayfromduskfoxes01

    label ruinedshelterfirsttime01ccountfail:
        $ at_unlock_force = 0
        $ at_unlock_knowledge = 0
        $ at = 0
        $ ruinedshelter_duskfoxes_lookedat = 1
        if pc_hp:
            $ ruinedshelter_duskfoxes_dmgtopc = 1
        $ pc_hp = limit_pc_hp(pc_hp-1)
        show minus1hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
        menu:
            'You take a quick glance and evade the creature in front of you as it tries to bite your leg, but you then feel the bite on your calf. The third fox was standing right behind you. While it’s loud, it’s also lumbering about, not trying to hold you in place. The noises from the bushes belong to little pups, most likely harmless, though they are doing their best to imitate their guardians.
            \n\nYou take a step back.
            '
            '{image=d6} No time to wait. I kick one of them as quickly as I can.' ( condition="not ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I kick one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} No time to wait. I cut one of them as quickly as I can.' ( condition="ruinedshelter_duskfoxes_axe_prepared" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} No time to wait. I cut one of them as quickly as I can.')
                jump ruinedshelterfirsttime01ccharge
            '{image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to block their charge. I raise my hands and prepare myself to strike back.')
                jump ruinedshelterfirsttime01cblock
            'Since the one behind me already moved away, I run for it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the one behind me already moved away, I run for it.')
                jump ruinedshelterrunningawayfromduskfoxes01

    label ruinedshelterfirsttime01ccharge:
        $ at_unlock_force = 0
        $ at_unlock_knowledge = 0
        $ at = 0
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if ruinedshelter_duskfoxes_axe_prepared:
            $ d100roll -= 15
        if ruinedshelter_duskfoxes_lookedat:
            $ d100roll -= 15
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter)
        else:
            $ d100roll -= (pc_battlecounter/2)
        if d100roll > 60: # fail
            if pc_hp:
                $ ruinedshelter_duskfoxes_dmgtopc = 1
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if ruinedshelter_duskfoxes_axe_prepared:
                $ custom1 = "with a swing of your axe"
            elif ruinedshelter_duskfoxes_lookedat:
                $ custom1 = "with your boot"
            else:
                $ custom1 = "with your fists"
            if ruinedshelter_duskfoxes_lookedat:
                $ custom2 = ""
                $ custom3 = "It hurts, but since the animal was already weakened, you manage to free yourself with a single kick."
                $ custom4 = "The two pups keep their distance, piercing your ears with their yelps."
            else:
                $ custom2 = "- one that was sneaking behind you - "
                $ custom3 = "It hurts, but the animal is weakened, lumbering on its paws. You manage to free yourself with a single kick."
                $ custom4 = "There are two small pups hidden behind a tree stumps, keeping their distance, piercing your ears with their yelps."
            menu:
                'You dash forward, but not as quickly as the fox jumps away, using as a shelter the large, brown mushroom. You try to reach it [custom1], but then feel the teeth tearing the armor on your forearm,. The golden creature’s weight makes you lose focus, giving enough time to the third opponent [custom2]to bite your leg. [custom3]
                \n\nThe dusk foxes spread. [custom4] Their protectors growl at you, warning you to withdraw.
                '
                'I run for it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run for it.')
                    jump ruinedshelterrunningawayfromduskfoxes01
                '{image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.')
                    jump ruinedsheltercombat01
        elif d100roll > 30: # semi success
            if ruinedshelter_duskfoxes_axe_prepared:
                $ custom1 = "with your axe"
            elif ruinedshelter_duskfoxes_lookedat:
                $ custom1 = "with your boot"
            else:
                $ custom1 = "with your fists"
            if ruinedshelter_duskfoxes_lookedat:
                $ custom2 = ""
                $ custom3 = "The animal moves away in panic."
                $ custom4 = "The two pups keep their distance, piercing your ears with their yelps."
            else:
                $ custom2 = "- one that was sneaking behind you - "
                $ custom3 = "The animal moves away in panic, and you realize it was already weakened, lumbering on its paws."
                $ custom4 = "There are two small pups hidden behind a tree stumps, keeping their distance, piercing your ears with their yelps."
            menu:
                'You dash forward, but not as quickly as the fox jumps away, using as a shelter the large, brown mushroom. You try to reach it [custom1], but then the golden creature catches your forearm with its teeth, unable to pierce through it. Its weight makes you lose focus, giving enough time to the third opponent [custom2]to reach you. Still, you do manage to avoid its bite, scaring it away as you swing your leg. [custom3]
                \n\nThe dusk foxes spread. [custom4] Their protectors triumphantly growl at you, warning you to withdraw.
                '
                'I run for it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run for it.')
                    jump ruinedshelterrunningawayfromduskfoxes01
                '{image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.')
                    jump ruinedsheltercombat01
        else: # success
            $ ruinedshelter_duskfoxes_hp -= 1
            $ ruinedshelter_duskfoxes_dayofgettinghurt = day
            $ ruinedshelter_duskfoxes_wounded = 1
            if ruinedshelter_duskfoxes_axe_prepared:
                $ ruinedshelter_duskfoxes_wounded = 2
                if item_golemglove:
                    $ ruinedshelter_duskfoxes_hp -= 1
                if item_axe03:
                    $ ruinedshelter_duskfoxes_hp -= 2
                elif item_axe02:
                    $ ruinedshelter_duskfoxes_hp -= 1
                $ custom1 = "You reach it with your axe, sending its blood in the air. It whines in pain and tries to run, sliding on the ground, looking for shelter behind the large, brown mushroom"
            elif ruinedshelter_duskfoxes_lookedat:
                $ custom1 = "Once your boot hits its skull, it catches the creature in the middle of its jump. It flies away and hits the large tree stump, then slides down, gasping for air, yet still landing on all fours. As it looks at you with widely opened eyes, you see in them shock rather than pain"
            else:
                $ custom1 = "After a few swift punches land on its tiny head, it whines in pain and makes a few short jumps away from you, looking for shelter behind the large, brown mushroom. As it looks at you with widely opened eyes, you see in them shock rather than pain"
            if ruinedshelter_duskfoxes_lookedat:
                $ custom2 = ""
                $ custom3 = ""
                $ custom4 = "The two pups keep their distance, piercing your ears with their yelps."
            else:
                $ custom2 = "- one that was sneaking behind you - "
                $ custom3 = "You realize it was already weakened as it’s now lumbering on its paws."
                $ custom4 = "There are two small pups hidden behind a tree stumps, keeping their distance, piercing your ears with their yelps."
            menu:
                'You dash forward, surprising the fox with your speed. [custom1].
                \n\nYou then feel the blunt hit on your back. The golden beast from the table tried to get to your arm, but missed. It lands on the ground, then gets away with just two jumps, looking for a better opportunity. It’s then when you notice the third opponent [custom2]trying to reach you, but you scare it away by just raising your arm. [custom3]
                \n\nThe dusk foxes spread. [custom4] Their protectors growl at you, but quieter now. The hamlet fills with the smell of fear.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}. I need to gather my thoughts.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}. I need to gather my thoughts.' %horsename)
                    jump ruinedshelterrunningawayfromduskfoxes01
                '{image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.')
                    jump ruinedsheltercombat01

    label ruinedshelterfirsttime01cblock:
        $ at_unlock_force = 0
        $ at_unlock_knowledge = 0
        $ at = 0
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if ruinedshelter_duskfoxes_lookedat:
            $ d100roll -= 20
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter)
        else:
            $ d100roll -= (pc_battlecounter/2)
        if d100roll > 50: # fail
            if pc_hp:
                $ ruinedshelter_duskfoxes_dmgtopc = 1
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if ruinedshelter_duskfoxes_axe_prepared:
                $ custom1 = "You hit it with the blunt side of your axe, sending it into the air. It lands on all fours."
            elif ruinedshelter_duskfoxes_lookedat:
                $ custom1 = "You hit it with a precise kick, sending it into the air. It lands on all fours."
            else:
                $ custom1 = "You punch it with your fist, crushing it into the ground."
            if ruinedshelter_duskfoxes_lookedat:
                $ custom2 = ""
                $ custom3 = "It hurts, but since the animal was already weakened, you manage to free yourself with a single kick."
                $ custom4 = "The two pups keep their distance, piercing your ears with their yelps."
            else:
                $ custom2 = "- one that was sneaking behind you - "
                $ custom3 = "It hurts, but the animal is weakened, lumbering on its paws. You manage to free yourself with a single kick."
                $ custom4 = "There are two small pups hidden behind a tree stumps, keeping their distance, piercing your ears with their yelps."
            menu:
                'You step back as the fox in front of you jumps at your chest. [custom1]
                \n\nBefore you decide to run after it, the golden creature catches your forearm with its teeth, unable to pierce through it. Its weight makes you lose focus, giving enough time to the third opponent [custom2]to bite your leg. [custom3]
                \n\nThe dusk foxes spread. [custom4] Their protectors growl at you, warning you to stay away.
                '
                'I run for it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run for it.')
                    jump ruinedshelterrunningawayfromduskfoxes01
                '{image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.')
                    jump ruinedsheltercombat01
        else: # success
            if ruinedshelter_duskfoxes_axe_prepared:
                $ custom1 = "You hit it with the blunt side of your axe, sending it into the air. It lands on all fours."
            elif ruinedshelter_duskfoxes_lookedat:
                $ custom1 = "You hit it with a precise kick, sending it into the air. It lands on all fours."
            else:
                $ custom1 = "You punch it with your fist, sending it into the ground."
            if ruinedshelter_duskfoxes_lookedat:
                $ custom2 = ""
                $ custom3 = "The animal moves away in panic."
                $ custom4 = "The two pups keep their distance, piercing your ears with their yelps."
            else:
                $ custom2 = "- one that was sneaking behind you - "
                $ custom3 = "The animal moves away in panic, and you realize it was already weakened, lumbering on its paws."
                $ custom4 = "There are two small pups hidden behind a tree stumps, keeping their distance, piercing your ears with their yelps."
            menu:
                'You step back as the fox in front of you jumps at your chest. [custom1]
                \n\nBefore you decide to run after it, the golden creature catches your forearm with its teeth, unable to pierce through it. Its weight makes you lose focus, giving enough time to the third opponent [custom2]to reach you. Still, you do manage to avoid its bite, scaring it away as you swing your leg. [custom3]
                \n\nThe dusk foxes spread. [custom4] Their protectors triumphantly growl at you, warning you to withdraw.
                '
                'I run for it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run for it.')
                    jump ruinedshelterrunningawayfromduskfoxes01
                '{image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I fight them off, ready to get hurt if this is what it takes to get rid of them.')
                    jump ruinedsheltercombat01

    label ruinedshelterrunningawayfromduskfoxes01:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'You pass the weaker fox and run toward your belongings, encouraging the beasts to chase you all the way to the gate as they growl with determination. For now, they stay in the shelter, filled with pride.
            \n\nYou and {color=#f6d6bd}[horsename]{/color} take a few steps away.
            '
            'I enter the yard.' if not ruinedshelter_firsttime00b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump ruinedshelterfirsttime01b
            'I go behind the building.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go behind the building.')
                jump ruinedshelterfirsttime01c
            'I enter the building.' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d) or (ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and not ruinedshelter_firsttime00d):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                jump ruinedshelterfirsttime01d
            'I prepare my axe.' if ruinedshelter_firsttime00b and not ruinedshelter_firsttime00c and ruinedshelter_firsttime00d and not ruinedshelter_duskfoxes_axe_prepared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedshelterfirsttimepreparingaxe01d2
            'The creatures won’t let me get close to the building. (disabled)' if (ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and not ruinedshelter_firsttime00d):
                pass
            'I’m too exhausted to face the dusk foxes. (Required vitality: 1) (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp <= 0:
                pass
            'I need to get rid of these creatures.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get rid of these creatures.')
                jump ruinedshelterfirsttime01e
            'I let the foxes see me, then wear them down with shouts.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared != day and pc_hp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the foxes see me, then wear them down with shouts.')
                jump ruinedshelterfirsttime01scaringaway
            'I already bothered them today. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and ruinedshelter_duskfoxes_scarring:
                pass
            'I could return here another day, try to scare them off. (disabled)' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated and ruinedshelter_duskfoxes_scared == day and not ruinedshelter_duskfoxes_scarring:
                pass
            'This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.' if ruinedshelter_firsttime00c and not ruinedshelter_duskfoxes_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place was already abandoned, so I’ll let the dusk foxes stay. They aren’t threatening anyone.')
                jump ruinedshelterfirsttime01f

    label ruinedshelterfirsttime01scaringaway: # I let the foxes see me, then wear them down with shouts.
        $ ruinedshelter_duskfoxes_scarring = 1
        $ ruinedshelter_duskfoxes_scared = day
        $ ruinedshelter_duskfoxes_hp -= 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if ruinedshelter_duskfoxes_hp <= 0:
            $ custom1 = "You run away as the beasts get closer, but they don’t really chase after you. The older ones stay silent, while the pups keep yelping, hidden somewhere behind the building."
        elif ruinedshelter_duskfoxes_hp == 1:
            $ custom1 = "You run away as the beasts are chasing you all the way to the gate, but as they growl at you, they keep their distance."
        else:
            $ custom1 = "You run away as the beasts are chasing you all the way to the gate, growling with determination. For now, they stay in the shelter."
        menu:
            'You burst into the hamlet, yelling, running, swinging your axe, hitting the rocks loudly with the side of the blade. The confused dusk foxes observe you from afar, jumping from one corner to another, showing their teeth. After half a minute or so, they regain their senses, trying to surround you.
            \n\n[custom1]
            '
            'I can try again tomorrow. (disabled)':
                pass

    label ruinedshelterfirsttime01e: # I need to get rid of these creatures.
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ ruinedshelter_duskfoxes_axe_prepared = 1
        if item_golemglove:
            $ custom1 = " and put on The Golem Glove"
        else:
            $ custom1 = ""
        menu:
            'You search your bundles[custom1].
            '
            'I take my amulets.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my amulets.')
                $ ruinedshelter_duskfoxes_item = "wand"
                jump ruinedsheltercombat02
            'I won’t be able to use magic with such a weak pneuma. (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'A shield could help me push the foxes away.' if item_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A shield could help me push the foxes away.')
                $ ruinedshelter_duskfoxes_item = "shield"
                jump ruinedsheltercombat02
            'A fistful of blinding powder should be enough.' if item_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A fistful of blinding powder shoud be enough.')
                $ ruinedshelter_duskfoxes_item = "blindingpowder"
                jump ruinedsheltercombat02
            'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'My axe is enough.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My axe is enough.')
                $ ruinedshelter_duskfoxes_item = 0
                jump ruinedsheltercombat02
            'I have second thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have second thoughts.')
                $ ruinedshelter_duskfoxes_item = 0
                jump ruinedshelterfirsttime01g

    label ruinedsheltercombat01: # if the player fights right away
        if ruinedshelter_duskfoxes_axe_prepared:
            $ custom1 = "With the axe in your hand, you’re observing the beasts as they move to new positions, looking for their weaknesses."
        else:
            $ custom1 = "You reach for your axe as the beasts move to their new positions."
        if ruinedshelter_duskfoxes_wounded == 2:
            $ custom2 = "is already bleeding, and its movements are a bit chaotic, as if it tries to move around quickly, but isn’t able to"
        elif ruinedshelter_duskfoxes_wounded == 1:
            $ custom2 = "remains in constant movement, pretending to attack you, then moving back, but you notice that one of its paws is already limping"
        else:
            $ custom2 = "remains in constant movement, pretending to attack you, then moving back"
        menu:
            '[custom1] The pups stay far behind, relying on their protectors. The weakest dusk fox is near the bare tree, hoping to repeat its previous attack. The golden one remains in the corner, but is now jumping from seat to seat, as well as onto the tree stump, and keeps growling at you. The last one, which seems to be the bravest, [custom2].
            '
            '{image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.' :
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.')
                jump ruinedsheltercombat02aggressive
            '{image=d6} I need to use all of my strength. I’ll let them get close, ready to cut only a few times, but for good.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} They’re not really that strong. I’ll let them get close, ready to cut only a few times, but for good.')
                jump ruinedsheltercombat02strength
            '{image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.')
                jump ruinedsheltercombat02deffensive

    label ruinedsheltercombat02: # if the player fights later on
        $ at = 0
        if pc_class == "mage" and ruinedshelter_duskfoxes_item == "wand":
            $ at_unlock_spell = 1
            $ manacost = 2
        if ruinedshelter_duskfoxes_item == "shield":
            $ custom1 = "With the axe in one hand and the shield in the other, you enter the hamlet. The dusk foxes react right away, seeking new positions as they try to keep you in the front yard."
        elif ruinedshelter_duskfoxes_item == "blindingpowder":
            $ custom1 = "With the axe in one hand and the dust in the other, you enter the hamlet. The dusk foxes react right away, seeking new positions as they try to keep you in the front yard."
        elif ruinedshelter_duskfoxes_item == "wand":
            $ custom1 = "With the axe in one hand and the wand in the other, you enter the hamlet. The dusk foxes react right away, seeking new positions as they try to keep you in the front yard."
        else:
            $ custom1 = "With the axe in hand, you enter the hamlet. The dusk foxes react right away, seeking new positions as they try to keep you in the front yard."
        if ruinedshelter_duskfoxes_wounded == 2:
            $ custom2 = "is already bleeding, and its movements are a bit chaotic, as if it tries to move around quickly, but isn’t able to"
        elif ruinedshelter_duskfoxes_wounded == 1:
            $ custom2 = "remains in constant movement, pretending to attack you, then moving back, but you notice that one of its paws is already limping"
        else:
            $ custom2 = "remains in constant movement, pretending to attack you, then moving back"
        menu:
            '[custom1]
            \n\nThe lumbering beast is running to your right, clinging to the wall, hoping to repeat its attack from behind. The golden one jumps on the tree stump, growling at you as it lowers its head. The last one, which seems to be the bravest, [custom2].
            \n\nThe pups stay far behind, relying on their protectors.
            '
            '{i}Dusk{/i} foxes should be susceptible to light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Dusk{/i} foxes should be susceptible to light.')
                $ at_unlock_spell = 0
                $ at = 0
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ ruinedshelter_duskfoxes_item_wandused = 1
                menu:
                    'You grab one of your oldest amulets, a pendant made of leather and a single dim pearl. The little sphere is covered by cryptic engravings, but if there’s any special meaning behind them, you were never able to find out what it could be.
                    \n\nHolding the pearl between your fingers makes you feel the pleasant, familiar warmth. After a deep, single breath, you shut your eyes and start spinning the pendant above your head. The pneuma leaves your shell.
                    \n\nYou hear the whimpers, then you cease your spell and look around. The foxes are shaking their heads and moving back. You have an advantage, though only for a few heartbeats.
                    '
                    '{image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.' ( condition="at != 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.')
                        $ at_unlock_spell = 0
                        jump ruinedsheltercombat02aggressive
                    '{image=d6} I need to use all of my strength. I’ll let them get close, ready to cut only a few times, but for good.' ( condition="at != 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} They’re not really that strong. I’ll let them get close, ready to cut only a few times, but for good.')
                        $ at_unlock_spell = 0
                        jump ruinedsheltercombat02strength
                    '{image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.' ( condition="at != 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.')
                        $ at_unlock_spell = 0
                        jump ruinedsheltercombat02deffensive
            'Time to throw the dust at the brave one.' ( condition="at != 'spell' and ruinedshelter_duskfoxes_item == 'blindingpowder'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to throw the dust at the brave one.')
                $ at_unlock_spell = 0
                $ ruinedshelter_duskfoxes_item_blindingpowderused = 1
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp = 0
                $ ruinedshelter_duskfoxes_defeated = 1
                if ruinedshelter_firsttime00d:
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
                $ pc_battlecounter += 1
                menu:
                    'You take a few confident steps forward, then throw the dust in front of you, simultaneously turning your head away and jumping back to the gate. The other two foxes instantly leap toward you, but they stop once they notice the painful yelps of their companion. It whines in shock, unable to see, and spends a few moments trying to wash its face in the dust of the beaten path, not knowing yet the only thing that can save its vision is time, if anything at all. With every painful breath it cries louder, maybe begging for help, maybe cursing humankind.
                    \n\nAs the golden fox looks at you, you raise your axe, and the beast doesn’t wait anymore. It runs away, followed by the lumbering one. They grab their pups by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. Then, growling at you, they approach the hurt pack member, and with gentle bites and pushes direct it to the exit.
                    \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                    '
                    'Seems like I’m done here.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’m done here.')
                        stop music fadeout 4.0
                        play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        jump ruinedshelterafterinteraction01
            '{image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.' ( condition="at != 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I have to be faster than they are and trust my blade. I take the initiative, keep moving, cut whenever I have a chance.')
                $ at_unlock_spell = 0
                jump ruinedsheltercombat02aggressive
            '{image=d6} I need to use all of my strength. I’ll let them get close, ready to cut only a few times, but for good.' ( condition="at != 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to use all of my strength. I’ll let them get close, ready to cut only a few times, but for good.')
                $ at_unlock_spell = 0
                jump ruinedsheltercombat02strength
            '{image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.' ( condition="at != 'spell'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to rely on my gambeson, focus on protecting my legs and hands. With a few lucky hits, I can scare them off.')
                $ at_unlock_spell = 0
                jump ruinedsheltercombat02deffensive

    label ruinedsheltercombat02aggressive:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        if item_golemglove:
            $ d100roll -= 5
        if item_axe03:
            $ d100roll -= 15
        elif item_axe02:
            $ d100roll -= 10
        if ruinedshelter_duskfoxes_item == "shield":
            $ d100roll -= 5
        if ruinedshelter_duskfoxes_item_wandused:
            $ d100roll -= 20
        if ruinedshelter_duskfoxes_hp:
            $ d100roll += (10*ruinedshelter_duskfoxes_hp)
        if not ruinedshelter_duskfoxes_item_wandused and d100roll > 60:
            if pc_hp < 2: # complete failure with harsh punishment
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    $ cleanliness_clothes_blood = 1
                    $ cleanliness = limit_cleanliness(cleanliness-2)
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
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp -= 1
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    'The brave fox doesn’t wait for you to land a hit. As it nimbly dodges your charge, luring you deeper into the yard, you stumble over a branch. Before you regain your balance, teeth are already sinking into your leg. You shake the creature off, only to get hit by the golden one, now clinging to your [custom1] with its claws and reaching for your neck. You manage to grab it and throw it away, but you’re already hardly standing straight.
                    \n\nSomething bites your hand, but you don’t even look at it. With a scream, you run to the gate, where {color=#f6d6bd}[horsename]{/color} is already warming up, snorting at you with fear.
                    '
                    'I get in the saddle and flee. (disabled)':
                        pass
            else: # success with harsh punishment
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                show minus1appearance at appearancechange onlayer myoverlay
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp = 0
                $ ruinedshelter_duskfoxes_defeated = 1
                if ruinedshelter_firsttime00d:
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    'The brave fox doesn’t wait for you to land a hit. As it nimbly dodges your charge, luring you deeper into the yard, you stumble over a branch. Before you regain your balance, teeth are already sinking into your leg. You shake the creature off, only to get hit by the golden one, now clinging to your [custom1] with its claws and reaching for your neck. Thankfully, you’re strong enough to grab it and throw it away, making it hit the wall with an unpleasant thud.
                    \n\nSomething bites your hand, and without even looking at the beast you cut it with an axe. You’re heavily wounded, but also furious, and your anger makes the suffering beasts back away. They see your raised blade and wait no more. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree, then get through it with confident jumps.
                    \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                    '
                    'I get back to {color=#f6d6bd}[horsename]{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                        stop music fadeout 4.0
                        play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        jump ruinedshelterafterinteraction01
        elif d100roll > 40: # complete success with soft punishment
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom1 = "The stunned fox tries to jump away as it hears your steps, but not quickly enough - you land a hit, and the whining beast moves away, leaving a trail of blood behind it."
            else:
                $ custom1 = "You and the brave fox are equally fast. It doesn’t wait for you to land a hit and nimbly dodges your charge, but you manage to reach it with the side of the axe before the foxes regroup."
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom2 = "shield"
            else:
                $ custom2 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom1] The weakest fox approaches your leg, while the golden one clings to your [custom2] with its claws, trying to get to your neck. You’re strong enough to grab it and throw it away, making it hit the wall with an unpleasant thud, though your hand also gets scratched pretty badly.
                \n\nYour blood remains cold. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01
        else: # complete success with no punishment
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom1 = "The stunned fox tries to jump away as it hears your steps, but not quickly enough - you land a hit, and the whining beast moves away, leaving a trail of blood behind it."
            else:
                $ custom1 = "You and the brave fox are equally fast. It doesn’t wait for you to land a hit and nimbly dodges your charge, but you manage to reach it with the side of the axe before the foxes regroup."
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom2 = "shield"
            else:
                $ custom2 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom1] The weakest fox approaches your leg, while the golden one clings to your [custom2] with its claws, trying to get to your neck. You’re strong enough to grab it and throw it away, making it hit the wall with an unpleasant thud.
                \n\nYour blood remains cold. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01

    label ruinedsheltercombat02strength:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        if item_golemglove:
            $ d100roll -= 10
        if item_axe03:
            $ d100roll -= 5
        if pc_hp:
            $ d100roll -= (6*pc_hp)
        if ruinedshelter_duskfoxes_item == "shield":
            $ d100roll -= 10
        if ruinedshelter_duskfoxes_item_wandused:
            $ d100roll -= 10
        if ruinedshelter_duskfoxes_hp:
            $ d100roll += (10*ruinedshelter_duskfoxes_hp)
        if d100roll > 60:
            if pc_hp < 2: # complete failure with harsh punishment
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    $ cleanliness_clothes_blood = 1
                    $ cleanliness = limit_cleanliness(cleanliness-2)
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
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp -= 1
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item_wandused:
                    $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
                else:
                    $ custom3 = "The brave fox"
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    '[custom3] is quick and nimble, so your precise, powerful swing misses, almost hitting your own leg. The beast grabs your armor and pulls, making you stumble, and before you regain your balance, teeth are already sinking into your leg. You shake the creature off, only to get hit by the golden critter, clinging to your [custom1] with its claws and reaching for your neck. You manage to grab it and throw it away, but you’re already hardly standing straight.
                    \n\nSomething bites your hand, but you don’t even look at it. With a scream, you run to the gate, where {color=#f6d6bd}[horsename]{/color} is already warming up, snorting at you with fear.
                    '
                    'I get in the saddle and flee. (disabled)':
                        pass
            else: # success with harsh punishment
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp = 0
                $ ruinedshelter_duskfoxes_defeated = 1
                if ruinedshelter_firsttime00d:
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item_wandused:
                    $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
                else:
                    $ custom3 = "The brave fox"
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    '[custom3] is quick and nimble, so your precise, powerful swing misses, almost hitting your own leg. The beast grabs your armor and pulls, making you stumble, and before you regain your balance, teeth are already sinking into your leg. You shake the creature off, only to get hit by the golden critter, clinging to your [custom1] with its claws and reaching for your neck. You manage to grab it and throw it away, but you’re already hardly standing straight.
                    \n\nSomething bites your hand, and without even looking at the beast you kick it so harshly that it doesn’t get up for a good few breaths. You’re heavily wounded, but also furious, and your anger makes the suffering beasts back away. They see your raised blade and wait no more. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                    \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                    '
                    'I get back to {color=#f6d6bd}[horsename]{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                        stop music fadeout 4.0
                        play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        jump ruinedshelterafterinteraction01
        elif d100roll > 40: # complete success with soft punishment
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
            else:
                $ custom3 = "The brave fox"
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom1 = "shield"
            else:
                $ custom1 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom3] is nimble, but your precise, powerful swing is quick enough to land. The whining beast moves away, leaving a trail of blood behind it. The weakest creature approaches your leg while you’re getting hit by the golden critter, clinging to your [custom1] with its claws and reaching for your neck. You’re conscious enough to grab it and throw it away, making it hit the wall with an unpleasant thud, though your hand also gets scratched pretty badly.
                \n\nYour blood remains cold. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01
        else: # complete success with no punishment
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
            else:
                $ custom3 = "The brave fox"
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom1 = "shield"
            else:
                $ custom1 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom3] is nimble, but your precise, powerful swing is quick enough to land. The whining beast moves away, leaving a trail of blood behind it. The weakest creature approaches your leg while you’re getting hit by the golden critter, clinging to your [custom1] with its claws and reaching for your neck. You’re conscious enough to grab it and throw it away, making it hit the wall with an unpleasant thud.
                \n\nYour blood remains cold. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01

    label ruinedsheltercombat02deffensive:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        if pc_hp:
            $ d100roll -= (2*pc_hp)
        if armor >= 3:
            $ d100roll -= 25
        elif armor == 2:
            $ d100roll -= 15
        if ruinedshelter_duskfoxes_item == "shield":
            $ d100roll -= 20
        if ruinedshelter_duskfoxes_item_wandused:
            $ d100roll -= 5
        if ruinedshelter_duskfoxes_hp:
            $ d100roll += (10*ruinedshelter_duskfoxes_hp)
        if d100roll > 60:
            if pc_hp < 2: # complete failure with harsh punishment
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
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp -= 1
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item_wandused:
                    $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
                else:
                    $ custom3 = "The brave fox"
                if armor >= 2:
                    $ custom2 = "Your fine armor is not enough to stop the pain, and as you raise your arm,"
                else:
                    $ custom2 = "Your armor is unable to stop the pain, and as you scream,"
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    '[custom3] is quick and nimble. You try to keep it at a distance, aware that another fox is approaching you from the back slowly, but then you get hit by the golden critter, which is clinging to your [custom1] with its claws and reaching for your neck. [custom2] the fox manages to reach your skin with the edge of its teeth. The blood doesn’t gush, just flows out on your chest, so you’re conscious enough to grab the creature and throw it away. You hardly manage to stand straight - especially as the weakest beast is now also biting your leg.
                    \n\nYou kick and swing your arms, setting yourself free, then run for the gate with a painful shout. Your horse is already starting to warm up, snorting at you with fear.
                    '
                    'I get in the saddle and flee. (disabled)':
                        pass
            else: # success with harsh punishment
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
                if not ruinedshelter_duskfoxes_wounded:
                    $ ruinedshelter_duskfoxes_wounded = 1
                $ ruinedshelter_duskfoxes_hp = 0
                $ ruinedshelter_duskfoxes_defeated = 1
                if ruinedshelter_firsttime00d:
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
                $ pc_battlecounter += 1
                if ruinedshelter_duskfoxes_item_wandused:
                    $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
                else:
                    $ custom3 = "The brave fox"
                if armor >= 2:
                    $ custom2 = "Your fine armor is not enough to stop the pain, and as you raise your arm,"
                else:
                    $ custom2 = "Your armor is unable to stop the pain, and as you scream,"
                if ruinedshelter_duskfoxes_item == "shield":
                    $ custom1 = "shield"
                else:
                    $ custom1 = "armored shoulder"
                $ ruinedshelter_duskfoxes_item = 0
                $ ruinedshelter_duskfoxes_item_wandused = 0
                menu:
                    '[custom3] is quick and nimble. You try to keep it at a distance, aware that another fox is approaching you from the back slowly, but then you get hit by the golden critter, which is clinging to your [custom1] with its claws and reaching for your neck. [custom2] the fox manages to reach your skin with the edge of its teeth. The blood doesn’t gush, just flows out on your chest, so you’re conscious enough to grab the creature and throw it away. You hardly manage to stand straight - especially as the weakest beast is now also biting your leg.
                    \n\nSomething bites your hand, and without even looking at the beast you kick it so harshly that it doesn’t get up for a good few breaths. You’re heavily wounded, but also furious, and your anger makes the suffering beasts back away. They see your raised blade and wait no more. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                    \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                    '
                    'I get back to {color=#f6d6bd}[horsename]{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                        stop music fadeout 4.0
                        play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        jump ruinedshelterafterinteraction01
        elif d100roll > 40: # complete success with soft punishment
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
            else:
                $ custom3 = "The brave fox"
            if armor >= 3:
                $ custom2 = "Your fine armor stops the pain completely, and as you raise your arm,"
            elif armor == 2:
                $ custom2 = "Your fine armor is not enough to stop the pain, and as you raise your arm,"
            else:
                $ custom2 = "Your armor is unable to stop the pain, and as you scream,"
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom1 = "shield"
            else:
                $ custom1 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom3] is quick and nimble. You try to keep it at a distance, aware that another fox is approaching you from the back slowly, but then you get hit by the golden critter, which is clinging to your [custom1] with its claws and reaching for your neck. [custom2] the fox’s jaw is almost at the edge of its teeth, but you’re conscious enough to grab it and throw it away, making it hit the wall with an unpleasant thud, though your hand also gets scratched pretty badly.
                \n\nYou maintain your cold blood and swing your weapon at the fox that wants to bite your leg. It tries to dodge, but not quickly enough - you land a hit, and the whining beast moves away, leaving a trail of blood behind it. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01
        else: # complete success with no punishment
            if not ruinedshelter_duskfoxes_wounded:
                $ ruinedshelter_duskfoxes_wounded = 1
            $ ruinedshelter_duskfoxes_hp = 0
            $ ruinedshelter_duskfoxes_defeated = 1
            if ruinedshelter_firsttime00d:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            $ pc_battlecounter += 1
            if ruinedshelter_duskfoxes_item_wandused:
                $ custom3 = "The foxes have enough time to regain their vision, and the brave one"
            else:
                $ custom3 = "The brave fox"
            if armor >= 3:
                $ custom2 = "Your fine armor stops the pain completely, and as you raise your arm,"
            elif armor == 2:
                $ custom2 = "Your fine armor is not enough to stop the pain, and as you raise your arm,"
            else:
                $ custom2 = "Your armor is unable to stop the pain, and as you scream,"
            if ruinedshelter_duskfoxes_item == "shield":
                $ custom1 = "shield"
            else:
                $ custom1 = "armored shoulder"
            $ ruinedshelter_duskfoxes_item = 0
            $ ruinedshelter_duskfoxes_item_wandused = 0
            menu:
                '[custom3] is quick and nimble. You try to keep it at a distance, aware that another fox is approaching you from the back slowly, but then you get hit by the golden critter, which is clinging to your [custom1] with its claws and reaching for your neck. [custom2] the fox’s jaw is almost at the edge of its teeth, but you’re conscious enough to grab it and throw it away, making it hit the wall with an unpleasant thud.
                \n\nYou maintain your cold blood and swing your weapon at the fox that wants to bite your leg. It tries to dodge, but not quickly enough - you land a hit, and the whining beast moves away, leaving a trail of blood behind it. The pain scares away the two stronger foxes, and the third one is unwilling to attack you without assistance. You raise your blade, and they wait no longer. The stronger two run for their pups, grab them by their necks, and, keeping their distance, carry them to the hole in the wall, near the bare tree. They get through it with confident jumps.
                \n\nBefore the lumbering one disappears into the wilderness, it gives the pack’s shelter one last glance.
                '
                'I get back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back to {color=#f6d6bd}%s{/color}.' %horsename)
                    stop music fadeout 4.0
                    play nature "audio/ambient/ruinedshelter01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                    jump ruinedshelterafterinteraction01

#########################

label ruinedshelterregular01defeatfirsttime:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You wait for a bit, but no fox comes to threaten you. It seems like they left the hamlet for good.
        '
        'I want to look around.' if not ruinedshelter_bushes or not ruinedshelter_mushrooms:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What are you looking for, or paying attention to? (example: gate)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump searchruinedshelter
        'There isn’t much left for me to do here. (disabled)' if ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared and ruinedshelter_mushrooms:
            pass
        'I approach the bushes growing next to the rock face.' if ruinedshelter_bushes == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the bushes growing next to the rock face.')
            jump ruinedshelter_bushes01
        'I enter the ruined building.' if not ruinedshelter_ruin_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the ruined building.')
            jump ruinedshelterinteractingwithhouse01

label ruinedshelterregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        '[ruinedshelter_fluff]
        '
        'I want to look around.' if not ruinedshelter_bushes or not ruinedshelter_mushrooms:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What are you looking for, or paying attention to? (example: gate)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump searchruinedshelter
        'There isn’t much left for me to do here. (disabled)' if ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared and ruinedshelter_mushrooms:
            pass
        'I approach the bushes growing next to the rock face.' if ruinedshelter_bushes == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the bushes growing next to the rock face.')
            jump ruinedshelter_bushes01
        'I enter the ruined building.' if not ruinedshelter_ruin_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the ruined building.')
            jump ruinedshelterinteractingwithhouse01

label ruinedshelterafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    label ruinedshelter_horsename_fluffloop:
        $ ruinedshelter_horsename_fluff = renpy.random.choice(['is scratching its side against a tree, unbothered by the surroundings.', 'is trying to nap, but gets interrupted by a bird that tries to rest on the top of the saddle.', 'is observing the short grass, judging if grazing on it is worth the effort.', 'is swishing its tail, trying to get rid of a couple of obnoxious flies.', 'is observing you, seemingly bored.'])
        if ruinedshelter_horsename_fluff_old == ruinedshelter_horsename_fluff:
            jump ruinedshelter_horsename_fluffloop
        else:
            $ ruinedshelter_horsename_fluff_old = ruinedshelter_horsename_fluff
    menu:
        '{color=#f6d6bd}[horsename]{/color} [ruinedshelter_horsename_fluff]
        '
        'I want to look around.' if not ruinedshelter_bushes or not ruinedshelter_mushrooms:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What are you looking for, or paying attention to? (example: gate)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump searchruinedshelter
        'There isn’t much left for me to do here. (disabled)' if ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared and ruinedshelter_mushrooms:
            pass
        'I approach the bushes growing next to the rock face.' if ruinedshelter_bushes == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the bushes growing next to the rock face.')
            jump ruinedshelter_bushes01
        'I enter the ruined building.' if not ruinedshelter_ruin_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the ruined building.')
            jump ruinedshelterinteractingwithhouse01

label ruinedshelter_bushes01all:
    label ruinedshelter_bushes01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not ruinedshelter_bushes:
            $ ruinedshelter_bushes = 1
            menu:
                'You start with the bushes growing in the front yard, not finding anything unusual about them, but you stop for longer at those growing just next to the rock face. The spot here smells with urine, and as you move the leaves away, you find a dark cave behind them. You can’t say for sure what it hides, but you hear no water or draft.
                \n\nThe wild plants are healthy.
                '
                'I could use the withering dust to get rid of these plants quickly.' if item_witheringdust:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the withering dust to get rid of these plants quickly.')
                    jump ruinedshelter_bushesremovingwithwitheringdust01
                'I grab my axe, gloves, and get to chopping.' ( condition="pc_hp >= 1 and quarters <= world_daylength-6" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe, gloves, and get to chopping.')
                    jump ruinedshelter_bushesremovingwithaxe01
                'It’s already almost nightfall, but I could still chop these plants with my axe.' ( condition="pc_hp >= 1 and quarters > world_daylength-6" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s already almost nightfall, but I could still chop these plants with my axe.')
                    jump ruinedshelter_bushesremovingwithaxe01
                'I’m too tired to remove these plants by chopping them. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1" ):
                    pass
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump ruinedshelterafterinteraction01
        else:
            menu:
                'The bushes are healthily growing, undisturbed by anyone.
                '
                'I could use the withering dust to get rid of these plants quickly.' if item_witheringdust:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the withering dust to get rid of these plants quickly.')
                    jump ruinedshelter_bushesremovingwithwitheringdust01
                'I grab my axe, gloves, and get to chopping.' ( condition="pc_hp >= 1 and quarters <= world_daylength-6" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe, gloves, and get to chopping.')
                    jump ruinedshelter_bushesremovingwithaxe01
                'It’s already almost nightfall, but I could still chop these plants with my axe.' ( condition="pc_hp >= 1 and quarters > world_daylength-6" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s already almost nightfall, but I could still chop these plants with my axe.')
                    jump ruinedshelter_bushesremovingwithaxe01
                'I’m too tired to remove these plants by chopping them. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1" ):
                    pass
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump ruinedshelterafterinteraction01

    label ruinedshelter_bushesremovingwithaxe01:
        $ quarters += 2
        $ ruinedshelter_bushes_cut = 1
        $ ruinedshelter_bushes = 2
        show ruinedshelteraxe 01 at basicfade
        menu:
            'There isn’t a convenient way to simply grab the plants and cut, as the wood is frustratingly resilient and the volume of leaves limits your movements. With no proper tools at your disposal, you take little steps - remove the twigs with your knife, then bend the branches to limit their flexibility, then slice, twist, and pull...
            \n\nIt takes almost half an hour, but you finally reach a point when you can get through while letting in enough light to take a good look.
            \n\nThe cave gets shorter the deeper it goes, getting too small for most humans after just a few feet, but the entrance was used by someone as a hideout. There’s a stool and trash inside, including a surprising amount of bones, and one thing that catches your attention - a bronze axe.
            '
            'I pick it up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick it up.')
                jump ruinedshelter_bushestakingtheaxehead01

    label ruinedshelter_bushesremovingwithwitheringdust01:
        $ ruinedshelter_bushes_cut = 1
        $ ruinedshelter_bushes = 2
        show ruinedshelteraxe 01 at basicfade
        menu:
            'You put on your thick, leather gloves, then spread the dust beneath the plants, even if sparingly. You fill up a wooden bowl with water and sprinkle it over the poison. You don’t need to wait long - the yellow smoke appears immediately, so you step away and cover your mouth and nose.
            \n\nThe sizzling bushes start to shake, losing their twigs and leaves - just enough to make you step forward, though you doubt the plants will ever recover.
            \n\nAfter a minute, you look inside. The cave gets shorter the deeper it goes, getting too small for most humans after just a few feet, but the entrance was used by someone as a hideout. There’s a stool and trash inside, including a surprising amount of bones, and one thing that catches your attention - a bronze axe.
            '
            'I pick it up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick it up.')
                jump ruinedshelter_bushestakingtheaxehead01

    label ruinedshelter_bushestakingtheaxehead01:
        $ ruinedshelter_duskfoxes_axe = 1
        show ruinedshelteraxe 02 at basicfade
        if item_axe03:
            $ custom1 = ", even though inferior to the axe you purchased in {color=#f6d6bd}Howler’s Dell{/color}. Still, a decent bronze can endure centuries. With some sharpening, it may serve you as a backup weapon, or you could sell it to someone right away."
        elif item_axe02:
            $ custom1 = ", though not of a higher quality than your own axe. Still, a decent bronze can endure centuries. With some sharpening, it may serve you as a backup weapon."
        else:
            $ custom1 = ", of a higher quality than your own axe. Still, a decent bronze can endure centuries. With some sharpening, it may serve you well in combat."
        menu:
            'The handle is eaten by rot, unpleasant to touch. You break off a part of it without even trying, then lift the rest of the weapon by its cold blade.
            \n\nIt’s free of decorations, with tiny notches on its still sharp blade, but you don’t doubt it’s a fine piece of artisanship[custom1] All you need to put it together is a set of tools - maybe a trader would have some.
            '
            'I remove the old handle and put the head with the rest of my bundles.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove the old handle and put the head with the rest of my bundles.')
                $ minutes += 10
                $ item_axehead = 1
                $ renpy.notify("You found a bronze axe head.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a bronze axe head.{/i}')
                jump ruinedshelterafterinteraction01

label ruinedshelterinteractingwithhouse01all:
    label ruinedshelterinteractingwithhouse01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if ruinedshelter_ruin_cleared:
            show areapicture ruinedshelter02 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
            show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b:
            if ruinedshelter_firsttime00c:
                show areapicture ruinedshelter00c at basicfade behind ruinedshelteraxe
            elif ruinedshelter_firsttime00d:
                show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
            else:
                show areapicture ruinedshelter00b at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00a at basicfade behind ruinedshelteraxe
        if ruinedshelter_duskfoxes_axe:
            show ruinedshelteraxe 02 at basicfade
        elif ruinedshelter_bushes_cut:
            show ruinedshelteraxe 01 at basicfade
        if not ruinedshelter_firsttime00d:
            $ ruinedshelter_firsttime00d = 1
            if ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
                show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
            else:
                show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
            $ ruinedshelter_name = "The Ruined Shelter"
            if ruinedshelter_duskfoxes_defeated:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description03 = "I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building."
            menu:
                'It’s a simple chamber with no furniture that would explain its purpose. The fireplace is buried beneath the roof. You inspect the walls, made of hundreds of small rocks dressed with a chisel.
                \n\nThe trash is heavy from the moisture. You push it with your boot, what starts a commotion among gray, disoriented bugs. Removing the rubble would take some effort, but for now it doesn’t look like there’s anything of value left behind. With enough wood, a group of builders could restore this hamlet in just a few days.
                '
                'I could hang around for a bit and clean up this mess.' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp >= 3 and quarters <= world_daylength-8" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could hang around for a bit and clean up this mess.')
                    jump ruinedsheltercleaning01
                'I could hang around for a bit and clean up this mess, but it’s almost nightfall. (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp >= 3 and quarters > world_daylength-8" ):
                    pass
                'I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time.' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp < 3 and pc_hp and quarters <= world_daylength-12" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time.')
                    jump ruinedsheltercleaning01alt
                'I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time, and it’s almost nightfall. (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp < 3 and pc_hp and quarters > world_daylength-12" ):
                    pass
                'I lack strength to clean up this mess. (Required vitality: 1) (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp <= 0" ):
                    pass
                'I step outside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step outside.')
                    jump ruinedshelterafterinteraction01
        else:
            menu:
                'The structure may be in bad shape, but remains a home for fungi, grass, and bugs.
                '
                'I could hang around for a bit and clean up this mess.' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp >= 3 and quarters <= world_daylength-8" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could hang around for a bit and clean up this mess.')
                    jump ruinedsheltercleaning01
                'I could hang around for a bit and clean up this mess, but it’s almost nightfall. (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp >= 3 and quarters > world_daylength-8" ):
                    pass
                'I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time.' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp < 3 and pc_hp and quarters <= world_daylength-12" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time.')
                    jump ruinedsheltercleaning01alt
                'I could hang around for a bit and clean up this mess, but I’m so tired it will take me a long time, and it’s almost nightfall. (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp < 3 and pc_hp and quarters > world_daylength-12" ):
                    pass
                'I lack strength to clean up this mess. (Required vitality: 1) (disabled)' ( condition="not ruinedshelter_ruin_cleared and ruinedshelter_duskfoxes_defeated and pc_hp <= 0" ):
                    pass
                'I step outside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step outside.')
                    jump ruinedshelterafterinteraction01

    label ruinedsheltercleaning01:
        $ quarters += 4
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment points.{/i}')
        $ ruinedshelter_ruin_cleared = 1
        if ruinedshelter_ruin_cleared:
            show areapicture ruinedshelter02 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
            show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b:
            if ruinedshelter_firsttime00c:
                show areapicture ruinedshelter00c at basicfade behind ruinedshelteraxe
            elif ruinedshelter_firsttime00d:
                show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
            else:
                show areapicture ruinedshelter00b at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00a at basicfade behind ruinedshelteraxe
        if ruinedshelter_duskfoxes_axe:
            show ruinedshelteraxe 02 at basicfade
        elif ruinedshelter_bushes_cut:
            show ruinedshelteraxe 01 at basicfade
        menu:
            'The task involves a lot of dirt, and you disturb whole armies of ants, worms, and bugs of all shapes and colors, which are feasting on wood, thatch, mushrooms, animal droppings, and one another. You prepare your gloves and some water.
            \n\nYou throw smaller pieces of the roof over the wall, and pull the larger ones through the main entrance. After an hour or so, you saw all there is to be found. The wood is beyond usage, but there are also no unpleasant surprises covered with dirt. If necessary, it would be easy to work with the remains.
            \n\nThere were some scraps of bones, clothes, and leather among the rubble, as well as a broken club, but the only thing of value you found are the two dragon bones dropped by someone under the wall.
            '
            'I wash the coins and put them in my pouch.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash the coins and put them in my pouch.')
                $ coins += 2
                $ quest_explorepeninsula_description06 = "I took a good look at the ruins placed at the northern road. It would be easy to turn it into a small daytime shelter."
                show screen notifyimage( "Journal updated: Explore the Peninsula.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula. +2 {image=cointest}{/i}')
                jump ruinedshelterafterinteraction01

    label ruinedsheltercleaning01alt:
        $ quarters += 8
        $ ruinedshelter_ruin_cleared = 1
        if ruinedshelter_ruin_cleared:
            show areapicture ruinedshelter02 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b and ruinedshelter_firsttime00c and ruinedshelter_firsttime00d:
            show areapicture ruinedshelter01 at basicfade behind ruinedshelteraxe
        elif ruinedshelter_firsttime00b:
            if ruinedshelter_firsttime00c:
                show areapicture ruinedshelter00c at basicfade behind ruinedshelteraxe
            elif ruinedshelter_firsttime00d:
                show areapicture ruinedshelter00d at basicfade behind ruinedshelteraxe
            else:
                show areapicture ruinedshelter00b at basicfade behind ruinedshelteraxe
        else:
            show areapicture ruinedshelter00a at basicfade behind ruinedshelteraxe
        if ruinedshelter_duskfoxes_axe:
            show ruinedshelteraxe 02 at basicfade
        elif ruinedshelter_bushes_cut:
            show ruinedshelteraxe 01 at basicfade
        menu:
            'The task involves a lot of dirt, and you disturb whole armies of ants, worms, and bugs of all shapes and colors, which are feasting on wood, thatch, mushrooms, animal droppings, and one another. You prepare your gloves and some water.
            \n\nYou throw smaller pieces of the roof over the wall, and pull the larger ones through the main entrance. In your current condition, the work is rather exhausting, and you need to take a bit of a break. After two hours or so, you saw all there is to be found. The wood is beyond usage, but there are also no unpleasant surprises covered with dirt. If necessary, it would be easy to work with the remains.
            \n\nThere were some scraps of bones, clothes, and leather among the rubble, as well as a broken club, but the only thing of value you found are the two dragon bones dropped by someone under the wall.
            '
            'I wash the coins and put them in my pouch.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash the coins and put them in my pouch.')
                $ coins += 2
                $ quest_explorepeninsula_description06 = "I took a good look at the ruins placed at the northern road. It would be easy to turn it into a small daytime shelter."
                show screen notifyimage( "Journal updated: Explore the Peninsula. +2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula. +2 {image=cointest}{/i}')
                jump ruinedshelterafterinteraction01

#################SEARCH

label searchruinedshelter:
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
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
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
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "fuck" or search == "sex" or search == "wtf" or search == "nigger" or search == "nigga" or search == "fag":
        menu:
            'Grow up.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
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
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
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
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    #IMPORTANT SEARCHES THAT DO NOTHING
    elif search == "air" or search == "wind" or search == "draft":
        menu:
            'The gentle wind moves the leaves and your hair, but is otherwise unnoticeable. There are no unusual drafts around.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "ground" or search == "exterior" or search == "grass" or search == "dirt" or search == "soil" or search == "crops" or search == "wheat" or search == "rye" or search == "barley":
        menu:
            'The beaten ground is marked with paw prints of dusk foxes, but is turning into a grassland. The soil is unremarkable - the spare bushes have little competition.
            \n\nThere’s a few spots where the grass grew unusually tall, and once you take a closer look, you realize those are weak stems of barley. They could be brought here by birds from one of the villages, or dropped by a human visitor.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "tree" or search == "trees" or search == "atree" or search == "thetree" or search == "baretree" or search == "foliagedtree" or search == "treebranches" or search == "branches" or search == "claws" or search == "clawmarks":
        menu:
            'The trees, especially the one that grew into the wall, visibly struggle to survive in the local soil, but still serve as a shelter for birds and squirrels. You notice claw marks on the trunks, but you don’t think they belong to the dusk foxes - they are way too large. If humans were to return to this place, it may take some time before the beasts realize this place is inhabited.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "otherside" or search == "othersideoftheroad" or search == "othersideofroad" or search == "road" or search == "forest" or search == "theforest" or search == "wilderness" or search == "thewilds" or search == "woods" or search == "the woods":
        menu:
            'The road is surrounded by a lush forest, with bushes and shrubs too dense to be crossed. But as you look farther south, downhill, you spot a few plumes of smoke.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "hamlet" or search == "thehamlet" or search == "entireplace":
        menu:
            'It could be a hunter’s shelter, a military outpost, or a storehouse for traders, but you spot no fresh human trails. The roof collapsed only a few years back, turning slowly into food for mushrooms. The outer wall looks generations old, but it used to be maintained. Some of its materials came from different times and areas.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "wall" or search == "walls" or search == "thewall" or search == "awall" or search == "stonewall" or search == "barrier":
        menu:
            'The outer wall looks generations old, but it used to be maintained. Some of its materials came from different times and areas. Having no parapet walk or a tower, it was meant to interfere with the roaming path of the wild creatures - it offers no real value in combat.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "cliff" or search == "precipice" or search == "crag" or search == "hillface" or search == "hill" or search == "mountain" or search == "rockface" or search == "therockface" or search == "crag":
        menu:
            'The rock face is tall, seemingly too steep for a human to climb it without proper equipment.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "stump" or search == "treestump" or search == "thetreestump" or search == "treestumps" or search == "atreestump" or search == "trunk" or search == "atrunk" or search == "astump" or search == "atreestump" or search == "thetrunk" or search == "thetreetrunk" or search == "treetrunk" or search == "stumps" or search == "thetreestumps" or search == "largetreestump" or search == "thelargetreestump":
        menu:
            'It’s hard to say if these trees were cut to use their lumber at this very shelter, or to carry them away. The stumps are already reclaimed by the fungi and bugs.
            \n\nThere’s also one trunk that was split in half horizontally, now serving as a table.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "cup" or search == "block" or search == "stool" or search == "log" or search == "resting" or search == "rest" or search == "restingarea" or search == "dinningarea" or search == "restingarea" or search == "dinningarea" or search == "diningarea" or search == "table" or search == "bench" or search == "counter" or search == "chair" or search == "seat" or search == "seats":
        menu:
            'One of the hamlet’s corners seemingly served as an outside dining area, or maybe a spot to play games and rest. There’s a table made from a trunk, stumps turned into seats, and even an old wooden cup. Now all of these things are getting overtaken by bugs and fungi.
            \n\nThis spot is also not so overgrown by grasses. The beaten path leads in two directions - toward the bushes and a large tree stump, and toward the hamlet’s entrance.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "food" or search == "meal" or search == "eat" or search == "forage" or search == "foraging":
        menu:
            'There’s nothing around that could be easily turned into a meal, at least not one edible for you. The mushrooms require long preparations, an access to a fireplace, and cooking instruments, while the bugs would need to be caught first, what’s not an easy task, especially without a trap.
            \n\nThe more convenient foods, such as the fruits or nuts, are already devoured or hidden by the dusk foxes, birds, and squirrels.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "remains" or search == "corpse" or search == "grave" or search == "tomb" or search == "bones" or search == "body" or search == "shell" or search == "dead" or search == "soul" or search == "person" or search == "people" or search == "ash":
        menu:
            'You search the area for a bit, but find no graves or ash piles hidden. Of course, you won’t know for sure without digging.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "animal" or search == "pet" or search == "animals" or search == "beast" or search == "beasts" or search == "creatures" or search == "creature" or search == "insects" or search == "insect" or search == "bird" or search == "birds" or search == "duskfox" or search == "duskfoxes" or search == "life":
        menu:
            'You see a few signs of living creatures, some of which are difficult to identify. There are large marks of claws on the trees, droppings, innumerable bugs.
            \n\nThe red squirrels are observing you from the branches, and birds sing and caw from the leaves loudly. None of them is larger than your head.
            \n\nThere are also traces of dusk foxes, as well as scraps of their food and fur.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    if search == "sound" or search == "sounds" or search == "noise" or search == "noises":
        menu:
            'The wind shakes the tree crowns gently. Birds are feasting, singing, and crowing above you, not afraid of any threats. You don’t notice any worrisome sounds.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "treasure" or search == "money" or search == "chest" or search == "gold" or search == "jewelry" or search == "diamonds" or search == "diamond" or search == "cash" or search == "gem" or search == "gems" or search == "secrettreasure" or search == "secret":
        menu:
            'If it’s here, you need to find it first.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "light" or search == "darkness" or search == "dark" or search == "weather":
        if quarters >= (world_daylength-12):
            $ custom1 = "It’s getting late, and the sunbeams get weaker. You don’t notice any artificial lights, nor shining eyes in the darkness."
        else:
            $ custom1 = "It’s a calm, summer day, and the sun helps you look around. There’s no fire in sight."
        menu:
            '[custom1]
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "stone" or search == "rock" or search == "stones" or search == "rocks" or search == "brick" or search == "bricks":
        menu:
            'There are some rocks spread on the ground, and most of them came from the wall. They were dressed by stonecutters into uneven, but matching bricks.
            \n\nYou look beneath some of the loose ones, but they hide nothing of value. Their shadow provides a shelter for clans of worms and insects.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "plant" or search == "plants" or search == "flower" or search == "flowers" or search == "herb" or search == "herbs":
        menu:
            'The local plants are not too humble. The majority of the trees were cut down, all of the bushes seem similar, and the flowers are struggling.
            \n\nThere’s a few spots where the grass grew unusually tall, and once you take a closer look, you realize those are weak stems of barley. They could be brought here by birds from one of the villages, or dropped by a human visitor.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "trash" or search == "garbage" or search == "rubbish" or search == "litter" or search == "cloth" or search == "clothes" or search == "material":
        menu:
            'The old trash left by humans includes a soggy cup in the dining area and scraps of old, rotting clothes in the yard. The animals, on the other hand, have kept all sorts of leftovers - nutshells, pieces of fruit, destroyed mushrooms, bones, furs.
            \n\nNone of these things seems to be of value to you, though the flies are happy to take care of them.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "door" or search == "doors" or search == "thedoor" or search == "adoor" or search == "gate" or search == "thegate" or search == "agate" or search == "gates" or search == "entrance" or search == "theentrance" or search == "wood" or search == "timber" or search == "roof":
        menu:
            'There’s a lot of timber outside the building. They were destroyed by time, with no effort put into sustaining them with tar or oil. Now, soggy and slowly consumed by the worms and fungi, they are beyond restoration.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "wheel" or search == "circle" or search == "thewheel" or search == "thecircle" or search == "awheel" or search == "acircle" or search == "sparewheel" or search == "thesparewheel":
        menu:
            'The wheel leaning on the outer wall has not a single scrap of iron left on it. It’s much younger than the gate, but already soggy and unusable.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "stick" or search == "twig" or search == "branch" or search == "sticks" or search == "twigs" or search == "branches" or search == "brushwood":
        menu:
            'The branches and twigs that have fallen on the ground are already cleaned of their leaves, offering a brief home for fungi and worms. You move some of them around, but find nothing behind them.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    #IMPORTANT SEARCHES THAT DO SOMETHING
    elif search == "path" or search == "thepath" or search == "trail" or search == "atrail" or search == "beatenpath" or search == "beatenground" or search == "roadinhamlet" or search == "hamletroad" or search == "pathway" or search == "apathway" or search == "foothpath" or search == "afoothpath":
        menu:
            'The beaten path in the hamlet is getting replaced by grasses, scrap by scrap, but you still identify the most common routes preserved by animals. From the gate to the door, and from it to the dining area in the corner, but there are also many tracks behind the building, close to the bushes.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "prints" or search == "track" or search == "tracks" or search == "footprint" or search == "bootprint" or search == "footprints" or search == "bootprints" or search == "shoeprint" or search == "shoeprints" or search == "feetprint" or search == "boot" or search == "foot" or search == "print" or search == "trail" or search == "trace" or search == "paws" or search == "paw" or search == "pawprints" or search == "pawmarks":
        menu:
            'You spot some marks left here by animal hooves and long claws, some of which disturbed the grass, but it’s easier for you to focus on those left on the beaten path. Most of them belong to dusk foxes - their tracks are wolf-like, but much smaller, with fingers a bit more spread out. They are especially gathered near the bushes behind the building.
            \n\nOther tracks belong to even smaller creatures, mostly squirrels and birds, but there are also some boot prints, focused around the dining area in the corner. These tracks are much older than the others, and quite distorted.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "peespot" or search == "latrine" or search == "toilet" or search == "outhouse" or search == "cesspool" or search == "cloaca" or search == "cesspit" or search == "thelatrine" or search == "thetoilet" or search == "theouthouse" or search == "thelatrine" or search == "thetoilet" or search == "theouthouse" or search == "thecesspool" or search == "thecloaca" or search == "thecesspit" or search == "alatrine" or search == "atoilet" or search == "aouthouse" or search == "acesspool" or search == "acloaca" or search == "acesspit" or search == "urine" or search == "piss" or search == "shit":
        menu:
            'It doesn’t look like there’s a specific outhouse, nor even a large hole serving as such, but the closer you get to the bushes growing next to the rock face, the more intense the smell of urine gets.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "bush" or search == "bushes" or search == "shrubs" or search == "thebushes" or search == "theshrubs" or search == "shrub" or search == "theshrub" or search == "abush" or search == "ashrub" or search == "brake" or search == "brushwood" or search == "thethicket" or search == "thicket" or search == "behindbushes" or search == "behindbushes" or search == "behindthebushes" or search == "behindbush" or search == "behindthebush" or search == "behindabush" or search == "behindacave":
        if ruinedshelter_bushes < 2:
            jump ruinedshelter_bushes01
        else:
            menu:
                'You take another look at the local bushes, but find nothing unusual about them.
                '
                'I look for something else.':
                    python:
                        search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump searchruinedshelter
                'I leave the hamlet.':
                    jump ruinedshelterafterinteraction01
    elif search == "cave" or search == "thecave" or search == "acave" or search == "cavern" or search == "thecavern" or search == "acavern" or search == "tunnel" or search == "thetunnel" or search == "atunnel":
        if ruinedshelter_bushes < 2:
            $ search = "nothing"
            jump searchruinedshelter
        else:
            menu:
                'The cave gets shorter the deeper it goes, getting too small for most humans after just a few feet, but the entrance was used by someone as a hideout. There is a stool and trash inside, including a surprising amount of bones that avoided the hungry deers and bears.
                '
                'I look for something else.':
                    python:
                        search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump searchruinedshelter
                'I leave the hamlet.':
                    jump ruinedshelterafterinteraction01
    elif search == "mushroom" or search == "mushrooms" or search == "fungi" or search == "themushrooms" or search == "amushroom" or search == "themushroom":
        $ ruinedshelter_mushrooms = 1
        if ruinedshelter_bushes == 2 and ruinedshelter_mushrooms:
            menu:
                'Molds are covering the dead trees and moist lumber, but as you look around, you realize that the hamlet could be quite a treat for some brave foragers. You don’t fully trust your judgment in this matter, but most of the large mushrooms growing here resemble those eaten by you at various points in your life. Worms also feast on some of them, but they are still in a fair shape.
                '
                'I leave the hamlet.':
                    jump ruinedshelterafterinteraction01
        else:
            menu:
                'Molds are covering the dead trees and moist lumber, but as you look around, you realize that the hamlet could be quite a treat for some brave foragers. You don’t fully trust your judgment in this matter, but most of the large mushrooms growing here resemble those eaten by you at various points in your life. Worms also feast on some of them, but they are still in a fair shape.
                '
                'I look for something else.':
                    python:
                        search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump searchruinedshelter
                'I leave the hamlet.':
                    jump ruinedshelterafterinteraction01
    elif search == "insidehouse" or search == "enterhouse" or search == "house" or search == "building" or search == "hut" or search == "structure" or search == "thebuilding" or search == "abuilding" or search == "cabin" or search == "shelter" or search == "ruins" or search == "theshelter" or search == "ashelter" or search == "theruins":
        if not ruinedshelter_ruin_cleared:
            jump ruinedshelterinteractingwithhouse01
        else:
            menu:
                'The floor is cleared, but the wood is beyond usage. If necessary, it would be easy to work with the remains, especially since the outer wall would help protect the carpenters and masons.
                '
                'I look for something else.':
                    python:
                        search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump searchruinedshelter
                'I leave the hamlet.':
                    jump ruinedshelterafterinteraction01
    elif search == "smell" or search == "smells" or search == "odor" or search == "scent" or search == "breath" or search == "breathe" or search == "aroma" or search == "wiff":
        menu:
            'You take a deep breath, bringing images of rotting wood, moss, and cool, highland wind. As you wander, you notice quite an intense smell of old urine somewhere behind the building, as well as of animal feces.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    elif search == "burrow" or search == "burrows" or search == "den" or search == "animalhouse" or search == "lair":
        menu:
            'The dusk foxes’ burrow, placed beneath the back wall of the building, is not much longer than your arm. It’s rather empty, as if the animals abandoned their efforts once they had found another shelter.
            \n\nThere’s also not that many paw prints near the burrow. Most of them are closer to the rock face.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
    else:
        menu:
            'Either you don’t find it, or I can’t understand you.
            '
            'I look for something else.':
                python:
                    search = renpy.input("What are you looking for, or paying attention to?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump searchruinedshelter
            'I leave the hamlet.':
                jump ruinedshelterafterinteraction01
