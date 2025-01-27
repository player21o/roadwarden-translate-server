###################### Southern Crossroads
default southerncrossroads_firsttime = 0
default southerncrossroads_blocked = 0
default southerncrossroads_fluff = ""
default southerncrossroads_fluff_old = ""

default southerncrossroads_cliff_tried = 0
default southerncrossroads_cliff_alternative = 0
default southerncrossroads_undead = 0

default southerncrossroads_wildplants_start = 15
default southerncrossroads_wildplants_left = 2
default southerncrossroads_wildplants_display = 0

label southerncrossroads01:
    nvl clear
    if day >= militarycamp_destroyed_day:
        if militarycamp_destroyed_firsttime_southerncrossroads and militarycamp_destroyed_firsttime_southerncrossroads < day-1:
            show areapicture southerncrossroads03 at basicfade behind southerncrossroadsbronzerod
        else:
            show areapicture southerncrossroads02 at basicfade behind southerncrossroadsbronzerod
    else:
        show areapicture southerncrossroads01 at basicfade behind southerncrossroadsbronzerod
    if eudocia_bronzerod_rodin_southerncrossroads:
        show southerncrossroadsbronzerod at basicfade
    label southerncrossroads_fluffloop:
        $ southerncrossroads_fluff = renpy.random.choice(['The forest is uncannily quiet.', 'A termite larger than your hand moves out of your path, hiding among the bushes.', 'A loud roar comes from the north. Your palfrey stops and observes the forest, then swishes its tail and moves ahead.', 'You notice fresh pawprints. At least one goblin was searching this area.', 'The signpost seems untouched.'])
        if southerncrossroads_fluff_old == southerncrossroads_fluff:
            jump southerncrossroads_fluffloop
        else:
            $ southerncrossroads_fluff_old = southerncrossroads_fluff
    if day < southerncrossroads_wildplants_start-24 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 8
    elif day < southerncrossroads_wildplants_start-20 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 7
    elif day < southerncrossroads_wildplants_start-16 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 6
    elif day < southerncrossroads_wildplants_start-12 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 5
    elif day < southerncrossroads_wildplants_start-8 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 4
    elif day < southerncrossroads_wildplants_start-4 and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 3
    elif day < southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 2
    elif day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
        $ southerncrossroads_wildplants_display = 1
    else:
        $ southerncrossroads_wildplants_display = 0
    if not southerncrossroads_firsttime:
        $ world_known_areas += 1
        $ southerncrossroads_firsttime = 1
        $ peltnorth_unlocked = 1
        $ dolmen_unlocked = 1
        play nature "audio/ambient/southerncrossroads01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump southerncrossroads_firsttime01
    elif day >= militarycamp_destroyed_day and not militarycamp_destroyed_firsttime_southerncrossroads:
        if militarycamp_destroyed_firsttime_tulia and not world_endmode:
            $ militarycamp_destroyed_firsttime_southerncrossroads = day
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            stop music fadeout 4.0
            play nature "audio/ambient/southerncrossroads01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump southerncrossroadsregular02alt
        else:
            $ militarycamp_destroyed_firsttime_southerncrossroads = day
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            stop music fadeout 4.0
            play nature "audio/ambient/southerncrossroads01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump southerncrossroadsregular02
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        stop music fadeout 4.0
        play nature "audio/ambient/southerncrossroads01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump southerncrossroadsregular01

label southerncrossroads_firsttime01ALL:
    label southerncrossroads_firsttime01:
        $ tutorial_achievements = 1
        $ achievement_01 = 1
        menu:
            'The road splits. According to what the soldiers have told you, you may find a safe inn by turning left. The forest to the right is lush, and the trail overgrown. Kids used to have this song, how did it go? \n\n{i}The harshest pathway leads\nTo the dragon’s lair\nThose who search for treasure,\nDo you truly dare?{/i}
            \n\nThe signpost in front of you doesn’t make your situation much clearer. It was put here by someone who can’t write, for folks who can’t read. Covered in old, red paint, it points east. “Blood there,” as people say. Danger to be found.
            \n\nThere’s not a soul to ask for guidance.
            '
            'I look at my horse.':
                $ renpy.force_autosave(take_screenshot=False, block=True)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at my horse.')
                python:
                    horsename = renpy.input("What’s its name?", default="Sodal", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    horsename = horsename.strip()
                    horsename_reduced = horsename.strip().lower().replace(" ", "")
                    if not horsename:
                        horsename = "Sodal"
                jump southerncrossroads_firsttime02

    label southerncrossroads_firsttime02:
        $ item_horse = 1
        $ tutorial_achievements = 0
        $ tutorial_finished = 1
        $ can_leave = 1
        $ can_items = 1
        $ waitunlocked = 1
        $ tutorial_map = 3
        $ achievement_01 = 1
        # $ tutorial_sheet = 1
        # $ tutorial_sheet_display = 1
        if not pc_likeshorsename:
            menu:
                '{color=#f6d6bd}[horsename]{/color} is focused. Maybe it can’t help you choose a path, but it’s well-trained. As long as you don’t try to charge at a troll, you can count on it.
                \n\nYou spot a few berry shrubs and wild cabbages, but they still need at least two weeks to gain maturity.
                '
                'Time to make a turn. (disabled)':
                    pass
        else:
            menu:
                '{color=#f6d6bd}[horsename]{/color} is peaceful as you stroke its mane. Maybe it can’t help you choose a path, but you’ve spent many years together. Happy to go on, it takes a couple of steps forward.
                \n\nYou spot a few berry shrubs and wild cabbages, but they still need at least two weeks to gain maturity.
                '
                'Time to make a turn. (disabled)':
                    pass

###################################

label southerncrossroadsregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[southerncrossroads_fluff]
        '
        'It would be really easy now to place a bronze rod at the top of the crag.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_blocked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be really easy now to place a bronze rod at the top of the crag.')
            jump southerncrossroadsinstallingrod03
        'I could spend some time placing a bronze rod at the top of the escarpment.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters < (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend some time placing a bronze rod at the top of the escarpment.')
            jump southerncrossroadsinstallingrod01
        'I could spend some time placing a bronze rod at the top of the escarpment, but it’s too dangerous to climb at such a late hour. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters >= (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
            pass
        'With the bone hook, it should be easy to place a bronze rod around here.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and item_bonehook and not southerncrossroads_blocked: # ropehook
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the bone hook, it should be easy to place a bronze rod around here.')
            jump southerncrossroadsinstallingrod01hook
        'I would need a grappling hook to place a bronze rod at the top of the escarpment. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and not item_bonehook and not southerncrossroads_blocked:
            pass
        'This area is overgrown, but I spend about an hour foraging for edible plants.' if southerncrossroads_wildplants_display == 1 and southerncrossroads_wildplants_left:
            jump southerncrossroadsforaging01
        'The wild plants here need just a few more days before they ripen. (disabled)' if southerncrossroads_wildplants_display == 2:
            pass
        'The wild plants here need maybe another week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 3:
            pass
        'The wild plants here need more than one week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 4:
            pass
        'The wild plants here need about two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 5:
            pass
        'The wild plants here need more than two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 6:
            pass
        'The wild plants here need about three more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 7:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if southerncrossroads_wildplants_display == 8:
            pass
        'No point in staying here. (disabled)' if southerncrossroads_wildplants_display == 0:
            pass

label southerncrossroadsforaging01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This area is overgrown, but I spend about an hour foraging for edible plants.')
    $ southerncrossroads_wildplants_display = 0
    $ item_wildplants += 2
    $ achievement_wildplants += 2
    $ southerncrossroads_wildplants_left = 0
    $ renpy.notify("You picked 2 bunches of wild plants.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 2 bunches of wild plants.{/i}')
    $ quarters += 4
    menu:
        'Not trusting your surroundings, you have to take {color=#f6d6bd}[horsename]{/color} with you, repeatedly tethering and releasing it as you make progress. With the help of your axe and a long stick, you push aside the barricade of leaves and thorns and prod the ripe plums and sour apples, then catch them into a spread bag. You could use an extra pair of hands.
        \n\nThe berries are much easier to collect, though most of them are poisonous, so you leave them for the birds. After digging out the wild cabbage and carrots and cutting away their inedible parts, you take a few minutes to wash everything in cold water from your supplies.
        '
        'I make sure the fruits won’t get squished among my bundles.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be really easy now to place a bronze rod at the top of the crag.')
            jump southerncrossroadsafterinteraction01

label southerncrossroadsafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You return to your mount.
        '
        'It would be really easy now to place a bronze rod at the top of the crag.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_blocked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be really easy now to place a bronze rod at the top of the crag.')
            jump southerncrossroadsinstallingrod03
        'I could spend some time placing a bronze rod at the top of the escarpment.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters < (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend some time placing a bronze rod at the top of the escarpment.')
            jump southerncrossroadsinstallingrod01
        'I could spend some time placing a bronze rod at the top of the escarpment, but it’s too dangerous to climb at such a late hour. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters >= (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
            pass
        'With the bone hook, it should be easy to place a bronze rod around here.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and item_bonehook and not southerncrossroads_blocked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the bone hook, it should be easy to place a bronze rod around here.')
            jump southerncrossroadsinstallingrod01hook
        'I would need a grappling hook to place a bronze rod at the top of the escarpment. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and not item_bonehook and not southerncrossroads_blocked:
            pass
        'This area is overgrown, but I spend about an hour foraging for edible plants.' if southerncrossroads_wildplants_display == 1 and southerncrossroads_wildplants_left:
            jump southerncrossroadsforaging01
        'The wild plants here need just a few more days before they ripen. (disabled)' if southerncrossroads_wildplants_display == 2:
            pass
        'The wild plants here need maybe another week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 3:
            pass
        'The wild plants here need more than one week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 4:
            pass
        'The wild plants here need about two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 5:
            pass
        'The wild plants here need more than two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 6:
            pass
        'The wild plants here need about three more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 7:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if southerncrossroads_wildplants_display == 8:
            pass
        'No point in staying here. (disabled)' if southerncrossroads_wildplants_display == 0:
            pass

label southerncrossroadsinstallingrodALL:
    label southerncrossroadsinstallingrod01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ southerncrossroads_cliff_tried = 1
        if pc_class == "warrior":
            $ at_unlock_force = 1
            $ at = 0
        menu:
            'You tether {color=#f6d6bd}[horsename]{/color} to the signpost, so it can graze for a bit. The rock face is smooth and tall, uninviting. You don’t have proper tools to support you, and you don’t see any good spots where you could rest your hands while climbing.
            '
            'My grappling hook should do well here.' ( condition="at != 'force' and item_bonehook" ): # bonehook
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My grappling hook should do well here.')
                $ at_unlock_force = 0
                $ at = 0
                label southerncrossroadsinstallingrod01hook:
                    menu:
                        'Tying the rope to the bone hook is easy enough, though you struggle to throw it just right. After the fifth attempt it gets stuck between a branch and the stems of a shrub. You pull it for a bit, then jump in place, making sure the bushwood won’t break under your weight, then climb to the top slowly, “walking” on the surface of the wall.
                        \n\nAs you stand on the grass and look down, the crossroads are indeed not so far below you, but it catches your attention how fragile the {i}bridge{/i} between the two crags seems to be.
                        '
                        'I tie the rod to the bare tree.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tie the rod to the bare tree.')
                            jump southerncrossroadsinstallingrod02
            'I really could use a grappling hook. (disabled)' ( condition="at != 'force' and not item_bonehook" ):
                pass
            '{image=d6} All I can do is try. It’s not like I’m going to die after a fall.' ( condition="at != 'force' and not item_bonehook" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} All I can do is try. It’s not like I’m going to die after a fall.')
                $ at = 0
                $ quarters += 1
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                $ d100roll -= (pc_hp*5)
                if not pc_food:
                    $ d100roll += 10
                if pc_food == 3:
                    $ d100roll -= 10
                if pc_food == 4:
                    $ d100roll -= 20
                if d100roll > 25: # fail
                    menu:
                        'You place a boot on a small ledge, or rather in one of the holes, then stretch out your leg toward another spot that could handle your weight. Your hands find no rocks to grab, so all you can do is to cling to the cold, moist wall. After the second attempt, you manage to get a bit higher, but once you straighten up, the foot support crumbles, and you slide down. At least your hands are unscratched.
                        \n\nYou look at the escarpment again. You see no other spot to climb it.
                        '
                        'Maybe I’ll come back another time, with a better tool.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I’ll come back another time, with a better tool.')
                            jump southerncrossroadsafterinteraction01
                        'Just to be sure, I look for another climbing spot.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Just to be sure, I look for another climbing spot.')
                            $ quarters += 1
                            menu:
                                'You untether {color=#f6d6bd}[horsename]{/color} and take a bit of a stroll, observing both the woods and the cliffs, but it doesn’t look like you’ve missed anything. The only way to find another suitable part of the wall would require entering the forest.
                                '
                                'Fine.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Fine.')
                                    jump southerncrossroadsafterinteraction01
                else: # success
                    $ at_unlock_force = 0
                    $ at = 0
                    menu:
                        'You place a boot on a small ledge, or rather in one of the holes, then stretch out your leg toward another rock that could handle your weight. Your hands find no spot which you could grab, so all you can do is to cling to the cold, moist wall. After the second attempt, you manage to get a bit higher, but once you straighten up, your boot support crumbles, though only partially. Knowing that you may lose balance at any moment, you move slowly.
                        \n\nAfter a while, you reach the soil and grab a shrub to pull yourself up, trying to stop the leaves from entering your mouth. As you look down, the crossroads are indeed not so far below you, but it catches your attention how fragile the {i}bridge{/i} between the two crags seems to be.
                        '
                        'I tie the rod to the bare tree.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tie the rod to the bare tree.')
                            jump southerncrossroadsinstallingrod02
            'Nah. I just need to move between the ledges quickly.' ( condition="at == 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Nah. I just need to move between the ledges quickly.')
                $ at_unlock_force = 0
                $ at = 0
                menu:
                    'You do a few squats and stretches to help the fatigued muscles that usually support your riding endeavours, then make sure that the lowest ledge, or rather a small hole where you could rest your left foot, isn’t going to crumble under your weight. After a close examination, you’re confident you can do this, so you throw your tools on the grass above you, into the bushes. You put your right leg on the uneven surface, do three tests, then get to the top of the cliff in less than a breath. The rocks beneath you start to drop on the ground, but you don’t worry about them anymore.
                    \n\nAs you look down, the crossroads are indeed not so far below you, but it catches your attention how fragile the {i}bridge{/i} between the two crags seems to be.
                    '
                    'I tie the rod to the bare tree.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tie the rod to the bare tree.')
                        jump southerncrossroadsinstallingrod02
            'I’m too tired to put my experience to good use here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force == 1 and pc_hp <= 0" ):
                pass

    label southerncrossroadsinstallingrod02:
        show southerncrossroadsbronzerod at basicfade
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ item_bronzerod -= 1
        $ quarters += 1
        $ eudocia_bronzerod_rodin_southerncrossroads = 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
            if eudocia_bronzerod_installed < 4:
                $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
            elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
            elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
            else:
                $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
        else:
            if eudocia_bronzerod_installed >= 4:
                if not quest_bronzerod_description04:
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        menu:
            'You knock on the dead plant, and it’s still full of wood, strong. After just a bit more effort, the rod hugs the trunk, and even your deliberate efforts are not enough to make it fall down.
            '
            'I grab my belongings and slide down.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my belongings and slide down.')
                # if not southerncrossroads_undead:
                #     jump southerncrossroadsundead01
                # else:
                jump southerncrossroadsafterinteraction01

    label southerncrossroadsinstallingrod03:
        show southerncrossroadsbronzerod at basicfade
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ item_bronzerod -= 1
        $ quarters += 1
        $ eudocia_bronzerod_rodin_southerncrossroads = 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
            if eudocia_bronzerod_installed < 4:
                $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
            elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
            elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
            else:
                $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
        else:
            if eudocia_bronzerod_installed >= 4:
                if not quest_bronzerod_description04:
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        menu:
            'You get to the top of the pile of rocks, then reach for a root of the bare tree and get to the top of the cliff. You knock on the dead plant, and it’s still full of wood, strong. After just a bit more effort, the rod hugs the trunk, and even your deliberate efforts are not enough to make it fall down.
            '
            'I grab my belongings and climb down.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my belongings and climb down.')
                # if not southerncrossroads_undead:
                #     jump southerncrossroadsundead01
                # else:
                jump southerncrossroadsafterinteraction01

    # label southerncrossroadsundead01:
    #     $ southerncrossroads_undead = 1
    #     if item_crossbow:
    #         $ custom1 = "\n\nYour crossbow is also down below."
    #     else:
    #         $ custom1 = ""
    #     menu:
    #         '
    #         \n\n [custom1]
    #         '
    #         '':
    #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
    #             jump z

label southerncrossroadsregularALL:
    label southerncrossroadsregular02:
        if peltnorth_ban_perm:
            $ peltnorth_ban_perm = 0
            $ peltnorth_ban_perm_past = 1
        if peltnorth_ban_temp == day:
            $ peltnorth_ban_temp = (day-1)
        menu:
            'A flock of rooks and crows flees the crossroads, the bushes are rustling. The wolf carcass is fresh, and so are the bootprints.
            '
            'I should investigate the trail.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should investigate the trail.')
                menu:
                    'A wounded human, either of a large shell or with heavy equipment, has reached this spot from the south, shuffling with one foot. The wolf, lured by the scent of blood, ran through the shrubs, breaking a few twigs, but the few stabs it received were deadly precise, reaching the organs.
                    \n\nThe fighter turned west.
                    '
                    'I follow the bootprints, west.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the bootprints, west.')
                        $ travel_destination = "peltnorth"
                        jump finaldestinationafterevent
                    'I ride to the camp.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride to the camp.')
                        $ travel_destination = "militarycamp"
                        jump finaldestinationafterevent
            'I don’t have time for this.' if not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time for this.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You step away.
                    '
                    'It would be really easy now to place a bronze rod at the top of the crag.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_blocked:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be really easy now to place a bronze rod at the top of the crag.')
                        jump southerncrossroadsinstallingrod03
                    'I could spend some time placing a bronze rod at the top of the escarpment.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters < (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend some time placing a bronze rod at the top of the escarpment.')
                        jump southerncrossroadsinstallingrod01
                    'I could spend some time placing a bronze rod at the top of the escarpment, but it’s too dangerous to climb at such a late hour. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters >= (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
                        pass
                    'With the bone hook, it should be easy to place a bronze rod around here.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and item_bonehook and not southerncrossroads_blocked:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the bone hook, it should be easy to place a bronze rod around here.')
                        jump southerncrossroadsinstallingrod01hook
                    'I would need a grappling hook to place a bronze rod at the top of the escarpment. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and not item_bonehook and not southerncrossroads_blocked:
                        pass
                    'This area is overgrown, but I spend about an hour foraging for edible plants.' if southerncrossroads_wildplants_display == 1 and southerncrossroads_wildplants_left:
                        jump southerncrossroadsforaging01
                    'The wild plants here need just a few more days before they ripen. (disabled)' if southerncrossroads_wildplants_display == 2:
                        pass
                    'The wild plants here need maybe another week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 3:
                        pass
                    'The wild plants here need more than one week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 4:
                        pass
                    'The wild plants here need about two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 5:
                        pass
                    'The wild plants here need more than two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 6:
                        pass
                    'The wild plants here need about three more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 7:
                        pass
                    'The wild plants here will be ripe just before the end of summer. (disabled)' if southerncrossroads_wildplants_display == 8:
                        pass
                    'No point in staying here. (disabled)' if southerncrossroads_wildplants_display == 0:
                        pass

    label southerncrossroadsregular02alt:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'A flock of rooks and crows flees the crossroads, the bushes are rustling. The carcass is fresh, and so are the bootprints.
            \n\nYou take a quick look around. {color=#f6d6bd}Tulia’s{/color} work. The wolf, lured by the scent of blood, ran through the shrubs, breaking a few twigs, but the few stabs it received were deadly precise, reaching the organs.
            '
            'It would be really easy now to place a bronze rod at the top of the crag.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_blocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be really easy now to place a bronze rod at the top of the crag.')
                jump southerncrossroadsinstallingrod03
            'I could spend some time placing a bronze rod at the top of the escarpment.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters < (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could spend some time placing a bronze rod at the top of the escarpment.')
                jump southerncrossroadsinstallingrod01
            'I could spend some time placing a bronze rod at the top of the escarpment, but it’s too dangerous to climb at such a late hour. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and quarters >= (world_daylength-1) and not southerncrossroads_cliff_tried and not southerncrossroads_blocked:
                pass
            'With the bone hook, it should be easy to place a bronze rod around here.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and item_bonehook and not southerncrossroads_blocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the bone hook, it should be easy to place a bronze rod around here.')
                jump southerncrossroadsinstallingrod01hook
            'I would need a grappling hook to place a bronze rod at the top of the escarpment. (disabled)' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_southerncrossroads and southerncrossroads_cliff_tried and not item_bonehook and not southerncrossroads_blocked:
                pass
            'This area is overgrown, but I spend about an hour foraging for edible plants.' if southerncrossroads_wildplants_display == 1 and southerncrossroads_wildplants_left:
                jump southerncrossroadsforaging01
            'The wild plants here need just a few more days before they ripen. (disabled)' if southerncrossroads_wildplants_display == 2:
                pass
            'The wild plants here need maybe another week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 3:
                pass
            'The wild plants here need more than one week before they ripen. (disabled)' if southerncrossroads_wildplants_display == 4:
                pass
            'The wild plants here need about two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 5:
                pass
            'The wild plants here need more than two more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 6:
                pass
            'The wild plants here need about three more weeks before they ripen. (disabled)' if southerncrossroads_wildplants_display == 7:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if southerncrossroads_wildplants_display == 8:
                pass
            'No point in staying here. (disabled)' if southerncrossroads_wildplants_display == 0:
                pass
