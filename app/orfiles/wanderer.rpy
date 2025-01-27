###################### WANDERER
default wanderer_firsttime = 0
default wanderer_name = "The Statue of a Woman"

default wanderer_fluff = ""
default wanderer_fluff_old = ""

default wanderer_interacted = 0
default wanderer_offering = 0
default wanderer_offering_timer = 0
default wanderer_offering_disappeared = 0

default wanderer_cleared = 0
default wanderer_cleared_why = 0
default wanderer_coin_taken = 0
default wanderer_coin_gone = 0
default wanderer_coin_timer = 0

default wanderer_foragers = 0
default wanderer_foragers_about_cleaning = 0
default wanderer_foragers_about_statue = 0

default wanderer_fishtrap = 0
default wanderer_fishtrap_working = 0
default wanderer_fishtrap_daychecked = 0
default wanderer_fishtrap_fishtimer = 0
default wanderer_fishtrap_badthingmodifier = 0

label wanderer01:
    nvl clear
    $ pc_area = "wanderer"
    stop music fadeout 4.0
    play nature "audio/ambient/wanderer01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if not wanderer_cleared:
        show areapicture wanderer01 behind fishtrap at basicfade
    else:
        show areapicture wanderer02 behind fishtrap at basicfade
    if wanderer_fishtrap:
        show fishtrap wanderer01 at basicfade
    if wanderer_coin_timer and (wanderer_coin_timer+2) < day:
        $ wanderer_coin_gone = 1
    if (wanderer_offering == "coin" and wanderer_offering_timer and (wanderer_offering_timer+2) < day) or (wanderer_offering == "food" and wanderer_offering_timer and (wanderer_offering_timer+1) < day):
        $ wanderer_offering_disappeared = 1
    label wanderer_fluffloop:
        $ wanderer_fluff = renpy.random.choice(['The willow’s twigs are swinging gently, sending the leaves toward the lake. The road is covered with a rustling blanket.', 'Loud toads are sitting on the banks. Some of them observe you with large, round eyes, ready to hide in the water.', 'The gentle wind is swinging the willow’s twigs. One, maybe two more years and their tips will pierce the brook’s surface.', 'The brook carries down leaves and branches from the hills, sending them into the lake.', 'The lake’s surface is gentle, interrupted only by the jumping fish and shiny dragonflies.', 'The brook is cleaner than ever, and your palfrey happily takes a short break to quench its thirst.'])
        if wanderer_fluff_old == wanderer_fluff:
            jump wanderer_fluffloop
        else:
            $ wanderer_fluff_old = wanderer_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not wanderer_firsttime:
        $ world_known_npcs += 0
        $ wanderer_firsttime = 1
        $ world_known_areas += 1
        $ foragingground_unlocked = 1
        $ foggylake_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if foragingground_foragers_toforagingground:
            jump wandererfirsttime01foragers
        else:
            jump wandererfirsttime01
    else:
        if foragingground_foragers_toforagingground:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            jump wandererregular01foragers
        else:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            jump wandererregular01

label wandererfirsttime01ALL:
    label wandererfirsttime01:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        if foggylake_firsttime:
            $ custom1 = "The air is fresh, just as it was in the tavern."
            if foragingground_firsttime:
                $ custom2 = ""
            else:
                $ custom2 = "In the south, you see uninviting hills, cut with tiresome roads."
        else:
            $ custom1 = "The air is humid, but fresh, vitalizing."
            if foggylake_firsttime:
                $ custom2 = ""
            else:
                $ custom2 = "The path leading farther north is green, bright, and calming."
        menu:
            '[custom1] The light touches the road and shrubs, blocked only by the single willow, wild and untrimmed. You’re by a lake, too large for you to see its other bank, but the local soil isn’t too fertile. There are only a few trees on the horizon, while the struggling bushes and grasses fight with layers of rocks. [custom2]
            \n\nA gray rabbit is cleaning its fur near the brook, but the sound of hooves makes it hop toward the nearest shrub. Right after it sinks into the leaves, you hear its squeal, cut off quickly. Whatever its hunter was, it leaves behind only the rustling of the thicket and a trail of blood.
            \n\nYou wait for a long minute with a hand on your axe, but the creature doesn’t return. You relax a bit, then turn toward the stone statue of a young woman.
            '
            'I ride a bit closer to it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride a bit closer to it.')
                menu:
                    'Such a monument would be a better fit for a temple, or a rich cityfolk’s house. Here, without any cover, it’s already losing its shape from the rains and dust. Chunks of the face and hair have already broken off.
                    \n\nIt has detailed eyes and human-like proportions, and the clothes are like fabric petrified by a spell. The statue carries the usual traveling equipment - a walking staff, a gambeson, simple pants, now covered by leaves.
                    '
                    'It’s a shame to see it deteriorating.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a shame to see it deteriorating.')
                        jump wandererfirsttime01wondering
                    'I look at the pedestal. Maybe someone left a valuable offering here.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the pedestal. Maybe someone left a valuable offering here.')
                        $ wanderer_cleared_why = 1
                        jump wandererfirsttime01treasure

    label wandererfirsttime01wondering:
        menu:
            'You observe its delicate face and the broken fingers, the last bits of which still hold the staff. You wonder why someone would place such a thing here.
            '
            'It may be a statue of a long gone hero.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a statue of a long gone hero.')
                jump wandererfirsttime01wondering03
            'It was made in the likeness of a person who placed it here. She wanted to be remembered.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was made in the likeness of a person who placed it here. She wanted to be remembered.')
                jump wandererfirsttime01wondering03
            'She welcomes the travelers heading to the sea.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- She welcomes the travelers heading to the sea.')
                jump wandererfirsttime01wondering03
            'Someone had to drop it after their wagon broke.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone had to drop it after their wagon broke.')
                jump wandererfirsttime01wondering03
            'I think it marks a place of great importance.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think it marks a place of great importance.')
                jump wandererfirsttime01wondering03
            'I shrug. All that matters is that it’s pretty.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. All that matters is that it’s pretty.')
                jump wandererfirsttime01wondering03

    label wandererfirsttime01wondering03:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'There are no answers to find in the statue’s absent eyes.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wandererregular01reasontoclear:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ wanderer_cleared_why = 1
        menu:
            'What for?
            '
            'There may be something valuable hidden beneath it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- There may be something valuable hidden beneath it.')
                jump wandererfirsttime01treasure
            'The locals may appreciate someone looking after their relics.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The locals may appreciate someone looking after their relics.')
                jump wandererregular01reasontoclear02
            'I want to make it clear that there’s a new roadwarden around, someone who cares.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to make it clear that there’s a new roadwarden around, someone who cares.')
                jump wandererregular01reasontoclear02
            'It’s a part of the local history. It should be protected.' if pc_religion == "ordersoftruth":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a part of the local history. It should be protected.')
                $ pc_faithpoints += 1
                jump wandererregular01reasontoclear02
            'The statue may represent an ancestor of one of the local families. It ought to be protected.' if pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The statue may represent an ancestor of one of the local families. It ought to be protected.')
                $ pc_faithpoints += 1
                jump wandererregular01reasontoclear02
            'I don’t know. Someone should do this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t know. Someone should do this.')
                jump wandererregular01reasontoclear02

    label wandererregular01reasontoclear02:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'You dismount and approach the bushes. You try to push them away, but their stems are thick and healthy, crowded with insects and spiderwebs. Thankfully, you see no thorns, and the touch of a leaf doesn’t make your finger itchy.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wandererfirsttime01treasure:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ wanderer_cleared_why = 1
        menu:
            'You dismount and approach the bushes covering the legs and the pedestal. You see some old wooden bowls, as well as rocks. You try to push the leaves away, but their stems are thick and healthy, crowded with insects and spiderwebs. Until you remove the thicket, you won’t be able to see if there’s anything worth stealing - thankfully, there are no thorns, and the touch of a leaf doesn’t make your finger itchy.
            '
            'It’s not stealing. An abandoned statue needs no gifts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not stealing. An abandoned statue needs no gifts.')
                menu:
                    'If you say so.
                    '
                    'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                        jump wandererregular01reasontoclear
                    'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                        pass
                    'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                        jump wandererregular02removingwithaxe
                    'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        pass
                    'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                        jump wandererregular02removingwithwitheringdust
                    'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                        jump wandererregular02takingthecoin
                    'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                        jump wandererregular02leavinganoffering
                    'I consider washing myself in the stream.':
                        jump wandererstream01
                    ###########################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                        jump wanderer_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                        jump wanderer_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                        jump wanderer_fishtrap03
                    'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                        jump wanderer_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                        pass
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

label wandererregular01ALL:
    label wandererregular01:
        if wanderer_cleared:
            $ custom1 = "The statue stands in all its glory, observing the road and those who use it."
        else:
            $ custom1 = "The statue is left to itself, with its purpose forgotten."
        if wanderer_coin_gone or (wanderer_offering == "coin" and wanderer_offering_disappeared):
            $ custom3 = " The coin you left in the wooden bowl is no longer here."
        elif wanderer_cleared and not wanderer_coin_taken:
            $ custom3 = " There’s still a coin in the wooden bowl."
        else:
            $ custom3 = ""
        if wanderer_offering == "food" and wanderer_offering_disappeared:
            $ custom4 = " All that’s left of your food are scraps, mostly nut shells."
        else:
            $ custom4 = ""
        $ renpy.force_autosave(take_screenshot=True, block=True)
        menu:
            '[wanderer_fluff]
            \n\n[custom1][custom3][custom4]
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wandererregular02removingwithaxe:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ quarters += 2
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment points.{/i}')
        $ wanderer_coin_timer = day
        $ wanderer_cleared = 1
        if quest_easternpath == 1 and quest_easternpath_description01:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description07 = "I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place."
        show areapicture wanderer02 behind fishtrap at basicfade
        menu:
            'You tether {color=#f6d6bd}[horsename]{/color} to the tree, letting it choose between drinking, grazing, and napping. You prepare your equipment, keeping an eye on the bush where you saw the rabbit’s last moments.
            \n\nYou use your weight to move the plants to one side, then cut right above the ground. The stems are healthy and flexible, so getting through them is rough, but you have enough strength to deal with them in a couple of minutes, then throw them into the lake. The work goes on for a bit, but once you’re done, the statue stands in its former glory.
            \n\nA couple of old offerings are still on the pedestal. Polished rocks, bone figurines, and moldy bowls and plates that used to store food.
            \n\nIn one vessel you see a dragon bone. It’s dark and could be older than a generation, but it would surely be accepted by any merchant.
            '
            'This coin was left here for a good reason. I should leave it behind.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This coin was left here for a good reason. I should leave it behind.')
                jump wandererregular03afterinteraction
            'I pick it up and put it in my pouch.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick it up and put it in my pouch.')
                jump wandererregular02takingthecoin

    label wandererregular02removingwithwitheringdust:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 5
        $ wanderer_coin_timer = day
        $ wanderer_cleared = 1
        if quest_easternpath == 1 and quest_easternpath_description01:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description07 = "I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place."
        show areapicture wanderer02 behind fishtrap at basicfade
        menu:
            'You tether {color=#f6d6bd}[horsename]{/color} to the tree, letting it choose between drinking, grazing, and napping. You prepare your equipment, keeping an eye on the bush where you saw the rabbit’s last moments.
            \n\nYou put on your gloves, use your weight to move the plants to one side, then spread the dust beneath them. With a wooden bowl, you draw water from the brook and sprinkle it over the poison. You don’t need to wait long - the yellow smoke shows up immediately, so you step away, covering your nose and mouth.
            \n\nThe sizzling bush starts to wiggle, losing its twigs and leaves. In less than a minute you throw the plant to the river. After repeating this for a few minutes, you finish the job with your axe.
            \n\nA couple of old offerings are still on the pedestal. Polished rocks, bone figurines, and moldy bowls and plates that used to store food.
            \n\nIn one vessel you see a dragon bone. It’s dark and could be older than a generation, but it would surely be accepted by any merchant.
            '
            'This coin was left here for a good reason. I should leave it behind.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This coin was left here for a good reason. I should leave it behind.')
                jump wandererregular03afterinteraction
            'I pick it up and put it in my pouch.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick it up and put it in my pouch.')
                jump wandererregular02takingthecoin

    label wandererregular02takingthecoin:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ wanderer_coin_timer = 0
        $ wanderer_coin_taken = 1
        $ coins += 1
        if pc_religion == "pagan":
            $ pc_faithpoints -= 1
        show screen notifyimage( "+1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
        menu:
            'You wash it in the brook and straighten up just a tiny bit richer. The statue is silent.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wandererregular02leavinganoffering:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'Your surroundings are silent, as if they’re holding their breath.
            '
            'I place a fair share of food on the pedestal.' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I place a fair share of food on the pedestal.')
                $ custom1 = "On the top of the cold stone you form a small pile of dried fruits, nuts, and a sausage. There’s no sign of Wanderer’s gratefulness - she doesn’t bow, nod, nor smile. Not a single beautiful bird sits down or her head, no squirrels show up on the tree. After a minute or so, you return to your mount, feeling tranquil and prepared."
                $ wanderer_offering = "food"
                $ pc_faithpoints += 1
                $ item_rations -= 1
                $ renpy.notify("You lost a food ration.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                jump wandererregular02leavinganoffering02
            'I don’t have any food to spare. (disabled)' if item_rations < 1:
                pass
            'I place a coin on the pedestal.' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I place a coin on the pedestal.')
                $ wanderer_offering = "coin"
                $ custom1 = "You open your pouch and place a dragon bone on the cold stone. There’s no sign of Wanderer’s gratefulness - she doesn’t bow, nod, nor smile. Not a single beautiful bird sits down or her head, no squirrels show up on the tree. After a minute or so, you return to your mount, feeling tranquil and prepared."
                $ pc_faithpoints += 1
                $ coins -= 1
                show screen notifyimage( "-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                jump wandererregular02leavinganoffering02
            'I don’t have any coins to spare. (disabled)' if coins < 1:
                pass
            'Maybe later.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe later.')
                jump wandererregular03afterinteraction

    label wandererregular02leavinganoffering02:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

label wandererregular03afterinteraction:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You return to {color=#f6d6bd}[horsename]{/color}.
        '
        'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
            jump wandererregular01reasontoclear
        'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
            pass
        'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
            jump wandererregular02removingwithaxe
        'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
            pass
        'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
            jump wandererregular02removingwithwitheringdust
        'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
            jump wandererregular02takingthecoin
        'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
            jump wandererregular02leavinganoffering
        'I consider washing myself in the stream.':
            jump wandererstream01
        ###########################
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
            jump wanderer_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
            jump wanderer_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
            jump wanderer_fishtrap03
        'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
            jump wanderer_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
            pass

########################################################

label wandererfirsttime01foragersALL:
    label wandererfirsttime01foragers:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        if foggylake_firsttime:
            $ custom1 = "The air is fresh, just as it was in the tavern."
            if foragingground_firsttime:
                $ custom2 = ""
            else:
                $ custom2 = "In the south, you see uninviting hills, cut with tiresome roads."
        else:
            $ custom1 = "The air is humid, but fresh, vitalizing."
            if foggylake_firsttime:
                $ custom2 = ""
            else:
                $ custom2 = "The path leading farther north is green, bright, and calming."
        menu:
            '[custom1] The light touches the road and shrubs, blocked only by the single willow, wild and untrimmed. You’re by a lake, too large for you to see its other bank, but there are only a few trees on the horizon, while the struggling bushes and grasses fight with layers of rocks. {color=#f6d6bd}Tzvi{/color} mentions that while the soil here is poor, one can still find plenty of berry shrubs around.
            \n\n{color=#f6d6bd}Ilan{/color} points at the gray rabbit cleaning its fur near the brook. Noticing your gaze, it hops toward the nearest shrub. Right after it sinks into the leaves, you hear its squeal, cut off quickly. “Oh dear,” shouts {color=#f6d6bd}the large man{/color}, while {color=#f6d6bd}his companion{/color} starts to laugh. “Caught between two stones!”
            \n\nYou wait for a long minute with a hand on your axe, but the creature doesn’t return. “Don’t worry, friend,” says {color=#f6d6bd}Ilan{/color}. “Just don’t follow its lead.”
            \n\nCarrying your belongings on your own is surprisingly tiring, and you make noises with every turn. You relax a bit, then turn toward the stone statue of a young woman.
            '
            'I approach it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach it.')
                menu:
                    'Such a monument would be a better fit for a temple, or a rich cityfolk’s house. Here, without any cover, it’s already losing its shape from the rains and dust. Chunks of the face and hair have already broken off.
                    \n\nIt has detailed eyes and human-like proportions, and the clothes are like fabric petrified by a spell. The statue carries the usual traveling equipment - a walking staff, a gambeson, simple pants, now covered by leaves.
                    \n\n“A nice thing, isn’t it?” {color=#f6d6bd}Ilan{/color} thunders behind you. “It’s older than our home.”
                    '
                    '“It’s a shame to see it deteriorating.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a shame to see it deteriorating.”')
                        jump wandererfirsttime01wonderingforagers
                    'I look at the pedestal. Maybe someone left here something valuable.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the pedestal. Maybe someone left here something valuable.')
                        $ wanderer_cleared_why = 1
                        jump wandererfirsttime01treasureforagers

    label wandererfirsttime01wonderingforagers:
        menu:
            'You observe the statue’s delicate face and its broken fingers, the last bits of which still hold the staff. “Hwat d’you say?” {color=#f6d6bd}Tzvi{/color} interrupts you. “D’you have such things by {color=#f6d6bd}Hovlavan{/color}, on the roads?”
            '
            '“We do, but they’re old. From before the war.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We do, but they’re old. From before the war.”')
                if pc_religion == "theunitedchurch":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    'He makes a satisfied grin. “The war has {i}ruined{/i} everything, hasn’t it? All the monuments, and palaces, and temples, and slave owners. Poor, poor Northerners.”
                    \n\nAfter a short chuckle, the larger man goes on. “Hwat sort of statues used to be there?”
                    '
                    'I’m not going to let them offend The Ten Cities and the Church that protects them. “The cityfolk are the only reason you have a home in these woods. Don’t spit on their graves.”' if pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not going to let them offend The Ten Cities and the Church that protects them. “The cityfolk are the only reason you have a home in these woods. Don’t spit on their graves.”')
                        $ pc_faithpoints += 2
                        $ creeks_reputation -= 1
                        $ foragers_friendship -= 1
                        $ description_hovlavan04 = "oldstatuesofheroes"
                        menu:
                            '{color=#f6d6bd}Tzvi{/color} spares no venom. “You’re right, in a way. They {i}are{/i} the reason, but not in the way you think. Not in the way of builders and wildtamers, but in the way of chainmakers.”
                            \n\nAfter a short moment, {color=#f6d6bd}Ilan{/color} walks down the road. “Let’s move on. We’ll find better reasons to give one another a black eye.” Soon after these words, {color=#f6d6bd}his companion{/color} follows him.
                            '
                            'I do so as well.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do so as well.')
                                $ travel_destination = "foragingground"
                                jump finaldestinationafterevent
                    'I bite my tongue. “All sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”' if pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bite my tongue. “All sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”')
                        $ pc_faithpoints -= 1
                        $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “How ‘bout you put those dragons into building homes for the families of those champions, or taking care of the old folks of those adventurers? I bet they’re not as important as a cold rock on a half-forgotten road.”"
                        $ description_hovlavan04 = "oldstatuesofheroes"
                        jump wandererfirsttime01wondering03foragers
                    'I try to ignore him. “People pay sculptors to honor themselves. To be remembered after their passing.”' if pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to ignore him. “People pay sculptors to honor themselves. To be remembered after their passing.”')
                        $ pc_faithpoints -= 1
                        $ custom1 = "Both of them laugh. “But of course! What else could be expected of those who have more than they can eat,” says {color=#f6d6bd}Tzvi{/color}.\n\n“After a few decades,” {color=#f6d6bd}Ilan{/color} points with his chin at the statue, “they’ll be just like this one, lost to time. At least sculptors get some food from it.”"
                        $ description_hovlavan04 = "oldstatuesofthemselves"
                        jump wandererfirsttime01wondering03foragers
                    'I take a deep breath and don’t address their insults. “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”' if pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and don’t address their insults. “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”')
                        $ pc_faithpoints -= 1
                        $ description_hovlavan04 = "oldstatuesofimportantplaces"
                        $ custom1 = "{color=#f6d6bd}Ilan{/color} nods. “Stories over people, aye? That’s hwat you get hwen you base prayers and gods on old Tablets. Some of The Southern Tribes do the very same.”"
                        jump wandererfirsttime01wondering03foragers
                    '“Ah, all sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”' if not pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Ah, all sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”')
                        $ description_hovlavan04 = "oldstatuesofheroes"
                        $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “How ‘bout you put those dragons into building homes for the families of those champions, or taking care of the old folks of those adventurers? I bet they’re not as important as a cold rock on a half-forgotten road.”"
                        jump wandererfirsttime01wondering03foragers
                    '“People pay sculptors to honor themselves. To make themselves remembered after their passing.”' if not pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “People pay sculptors to honor themselves. To make themselves remembered after their passing.”')
                        $ custom1 = "Both of them laugh. “But of course! What else could be expected of those who have more than they can eat,” says {color=#f6d6bd}Tzvi{/color}.\n\n“After a few decades,” {color=#f6d6bd}Ilan{/color} points with his chin at the statue, “they’ll be just like this one, lost to time. At least sculptors get some food from it.”"
                        $ description_hovlavan04 = "oldstatuesofthemselves"
                        jump wandererfirsttime01wondering03foragers
                    '“They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”' if not pc_religion == "theunitedchurch":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”')
                        $ custom1 = "{color=#f6d6bd}Ilan{/color} nods. “Stories over people, aye? That’s hwat you get hwen you base prayers and gods on old Tablets. Some of The Southern Tribes do the very same.”"
                        $ description_hovlavan04 = "oldstatuesofimportantplaces"
                        jump wandererfirsttime01wondering03foragers
            '“Not really. The statues of humans are seen as a sign of pride.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really. The statues of humans are seen as a sign of pride.”')
                $ description_hovlavan04 = "nooldstatues"
                menu:
                    '“And hwy not be proud hwen you’ve done something great,” {color=#f6d6bd}Ilan{/color} shrugs. “The statues may be a dumb way to do so, but heroes deserve to be remembered.”
                    '
                    '“Statues are a waste of time and coin.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Statues are a waste of time and coin.”')
                        $ custom1 = "“True, true. You have bards and scrolls anyway. Songs are warmer than rocks.”"
                        jump wandererfirsttime01wondering03foragers
                    '“Pride blinds people, makes them commit stupid mistakes. It’s a good thing that priests teach others to avoid it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pride blinds people, makes them commit stupid mistakes. It’s a good thing that priests teach others to avoid it.”')
                        $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “You say it as if the preachers are not some of the most prideful people of all.”"
                        jump wandererfirsttime01wondering03foragers
                    '“I don’t know. It’s stupid.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know. It’s stupid.”')
                        $ custom1 = "He laughs. “Sure, who cares. They are there, we are here. They have no power over this road.”"
                        jump wandererfirsttime01wondering03foragers
            '“A few, but I haven’t paid much attention to them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A few, but I haven’t paid much attention to them.”')
                $ description_hovlavan04 = "oldstatuesnoattention"
                $ custom1 = "He laughs. “Sure, who cares. They are there, we are here. They have no power over this road.”"
                jump wandererfirsttime01wondering03foragers

    label wandererfirsttime01wondering03foragers:
        menu:
            '[custom1]
            \n\nThe absent eyes of the statue have nothing to add.
            '
            '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                jump wandererregular01aboutstatueforagers
            '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                jump wandererregular01aboutcleaningforagers
            '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                jump wandererregular01aboutcleaningforagersalt
            '“We should move on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                jump wandererregular01aboutleavingforagers

    label wandererfirsttime01treasureforagers:
        $ wanderer_cleared_why = 1
        menu:
            'You dismount and approach the bushes covering the legs and the pedestal. You see some old wooden bowls, as well as rocks. You try to push the leaves away, but their stems are thick and healthy, crowded with insects and spiderwebs. Until you remove the thicket, you won’t be able to see if there’s anything worth stealing - thankfully, there are no thorns, and the touch of a leaf doesn’t make your finger itchy.
            \n\n{color=#f6d6bd}Tzvi{/color} chuckles. “Hwat, looking for offerings?”
            '
            'It’s not stealing. An abandoned statue needs no gifts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not stealing. An abandoned statue needs no gifts.')
                menu:
                    'If you say so.
                    '
                    '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                        jump wandererregular01aboutstatueforagers
                    '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                        jump wandererregular01aboutcleaningforagers
                    '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                        jump wandererregular01aboutcleaningforagersalt
                    '“We should move on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                        jump wandererregular01aboutleavingforagers
            '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                jump wandererregular01aboutstatueforagers
            '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                jump wandererregular01aboutcleaningforagers
            '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                jump wandererregular01aboutcleaningforagersalt
            '“We should move on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                jump wandererregular01aboutleavingforagers

    label wandererregular01aboutstatueforagers:
        $ wanderer_foragers_about_statue = 1
        menu:
            '“Nah.” {color=#f6d6bd}Ilan{/color} is more focused on the fish breaking through the surface of the lake. “It’s old, and the woman is a stranger. I heard no stories of it. My ma could.”
            '
            '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                jump wandererregular01aboutstatueforagers
            '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                jump wandererregular01aboutcleaningforagers
            '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                jump wandererregular01aboutcleaningforagersalt
            '“We should move on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                jump wandererregular01aboutleavingforagers

    label wandererregular01aboutcleaningforagers:
        $ wanderer_foragers_about_cleaning = 1
        menu:
            '“But hwat for?” {color=#f6d6bd}Tzvi{/color} narrows his eyes. “Let it to someone who cares. We have things to do.”
            '
            '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                jump wandererregular01aboutstatueforagers
            '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                jump wandererregular01aboutcleaningforagers
            '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                jump wandererregular01aboutcleaningforagersalt
            '“We should move on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                jump wandererregular01aboutleavingforagers

    label wandererregular01aboutcleaningforagersalt:
        $ wanderer_foragers_about_cleaning = 1
        $ foggy_friendship += 1
        $ foggy_about_clearedstatue = 1
        menu:
            '{color=#f6d6bd}Tzvi{/color} narrows his eyes, but speaks with a cheerful tone. “Ah, and I thought a beast ate the leaves, but there are no paw prints around, aye?”
            \n\n“I don’t think anyone on the coast is going to kneel before it,” adds {color=#f6d6bd}the larger man{/color}, “though I guess it does look nicer now.”
            '
            '“So, do you know who this is?”' if not wanderer_foragers_about_statue:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, do you know who this is?”')
                jump wandererregular01aboutstatueforagers
            '“The bushes are covering its legs. We could clean this place a bit. Reveal them.”' if not wanderer_foragers_about_cleaning and not wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The bushes are covering its legs. We could clean this place a bit. Reveal them.”')
                jump wandererregular01aboutcleaningforagers
            '“It was me who got rid of those bushes, you know.”' if not wanderer_foragers_about_cleaning and wanderer_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was me who got rid of those bushes, you know.”')
                jump wandererregular01aboutcleaningforagersalt
            '“We should move on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should move on.”')
                jump wandererregular01aboutleavingforagers

    label wandererregular01aboutleavingforagers:
        menu:
            '“Aye. Let’s not linger,” says {color=#f6d6bd}Ilan{/color} as he walks down the road.
            '
            'We move forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We move forward.')
                $ travel_destination = "foragingground"
                jump finaldestinationafterevent

label wandererregular01foragers:
    if wanderer_cleared:
        $ custom1 = "The statue stands in all its glory, observing the road and those who use it."
    else:
        $ custom1 = "The statue is left to itself, with its purpose forgotten."
    if wanderer_coin_gone or (wanderer_offering == "coin" and wanderer_offering_disappeared):
        $ custom3 = " The coin you left in the wooden bowl is no longer here."
    elif wanderer_cleared and not wanderer_coin_taken:
        $ custom3 = " There’s still a coin in the wooden bowl."
    else:
        $ custom3 = ""
    if wanderer_offering == "food" and wanderer_offering_disappeared:
        $ custom4 = " All that’s left of your food are scraps, mostly nut shells."
    else:
        $ custom4 = ""
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[wanderer_fluff] [custom1][custom3][custom4]
        \n\n“A nice thing, isn’t it?” {color=#f6d6bd}Ilan{/color} thunders behind you. “It’s older than our home.”
        \n\n“Hwat d’you say?” chips in {color=#f6d6bd}Tzvi{/color}. “D’you have such things by {color=#f6d6bd}Hovlavan{/color}, on the roads?”
        \n\nCarrying your belongings on your own is surprisingly tiring, and you make noises with every turn.
        '
        '“We do, but they’re old. From before the war.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We do, but they’re old. From before the war.”')
            if pc_religion == "theunitedchurch":
                $ pc_faithpoints_opportunities += 1
            menu:
                'He makes a satisfied grin. “The war has {i}ruined{/i} everything, hasn’t it? All the monuments, and palaces, and temples, and slave owners. Poor, poor Northerners.”
                \n\nAfter a short chuckle, the larger man goes on. “Hwat sort of statues used to be there?”
                '
                'I’m not going to let them offend The Ten Cities and the Church that protects them. “The cityfolk are the only reason you have a home in these woods. Don’t spit on their graves.”' if pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not going to let them offend The Ten Cities and the Church that protects them. “The cityfolk are the only reason you have a home in these woods. Don’t spit on their graves.”')
                    $ pc_faithpoints += 2
                    $ creeks_reputation -= 1
                    $ foragers_friendship -= 1
                    $ description_hovlavan04 = "oldstatuesofheroes"
                    menu:
                        '{color=#f6d6bd}Tzvi{/color} spares no venom. “You’re right, in a way. They {i}are{/i} the reason, but not in the way you think. Not in the way of builders and wildtamers, but in the way of chainmakers.”
                        \n\nAfter a short moment, {color=#f6d6bd}Ilan{/color} walks down the road. “Let’s move on. We’ll find better reasons to give one another a black eye.” Soon after these words, {color=#f6d6bd}his companion{/color} follows him.
                        '
                        'I do so as well.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do so as well.')
                            $ travel_destination = "foragingground"
                            jump finaldestinationafterevent
                'I bite my tongue. “All sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”' if pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bite my tongue. “All sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”')
                    $ pc_faithpoints -= 1
                    $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “How ‘bout you put those dragons into building homes for the families of those champions, or taking care of the old folks of those adventurers? I bet they’re not as important as a cold rock on a half-forgotten road.”"
                    $ description_hovlavan04 = "oldstatuesofheroes"
                    jump wandererfirsttime01wondering03foragers
                'I try to ignore him. “People pay sculptors to honor themselves. To be remembered after their passing.”' if pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to ignore him. “People pay sculptors to honor themselves. To be remembered after their passing.”')
                    $ pc_faithpoints -= 1
                    $ custom1 = "Both of them laugh. “But of course! What else could be expected of those who have more than they can eat,” says {color=#f6d6bd}Tzvi{/color}.\n\n“After a few decades,” {color=#f6d6bd}Ilan{/color} points with his chin at the statue, “they’ll be just like this one, lost to time. At least sculptors get some food from it.”"
                    $ description_hovlavan04 = "oldstatuesofthemselves"
                    jump wandererfirsttime01wondering03foragers
                'I take a deep breath and don’t address their insults. “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”' if pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and don’t address their insults. “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”')
                    $ pc_faithpoints -= 1
                    $ description_hovlavan04 = "oldstatuesofimportantplaces"
                    $ custom1 = "{color=#f6d6bd}Ilan{/color} nods. “Stories over people, aye? That’s hwat you get hwen you base prayers and gods on old Tablets. Some of The Southern Tribes do the very same.”"
                    jump wandererfirsttime01wondering03foragers
                '“Ah, all sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”' if not pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Ah, all sorts of important figures. Heroes of Wright’s Tablets. Local champions. Famous adventurers.”')
                    $ description_hovlavan04 = "oldstatuesofheroes"
                    $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “How ‘bout you put those dragons into building homes for the families of those champions, or taking care of the old folks of those adventurers? I bet they’re not as important as a cold rock on a half-forgotten road.”"
                    jump wandererfirsttime01wondering03foragers
                '“People pay sculptors to honor themselves. To make themselves remembered after their passing.”' if not pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “People pay sculptors to honor themselves. To make themselves remembered after their passing.”')
                    $ custom1 = "Both of them laugh. “But of course! What else could be expected of those who have more than they can eat,” says {color=#f6d6bd}Tzvi{/color}.\n\n“After a few decades,” {color=#f6d6bd}Ilan{/color} points with his chin at the statue, “they’ll be just like this one, lost to time. At least sculptors get some food from it.”"
                    $ description_hovlavan04 = "oldstatuesofthemselves"
                    jump wandererfirsttime01wondering03foragers
                '“They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”' if not pc_religion == "theunitedchurch":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They mark places of importance, or spots where an important event has happened. They don’t portray actual people.”')
                    $ custom1 = "{color=#f6d6bd}Ilan{/color} nods. “Stories over people, aye? That’s hwat you get hwen you base prayers and gods on old Tablets. Some of The Southern Tribes do the very same.”"
                    $ description_hovlavan04 = "oldstatuesofimportantplaces"
                    jump wandererfirsttime01wondering03foragers
        '“Not really. The statues of humans are seen as a sign of pride.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really. The statues of humans are seen as a sign of pride.”')
            $ description_hovlavan04 = "nooldstatues"
            menu:
                '“And hwy not be proud hwen you’ve done something great,” {color=#f6d6bd}Ilan{/color} shrugs. “The statues may be a dumb way to do so, but heroes deserve to be remembered.”
                '
                '“Statues are a waste of time and coin.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Statues are a waste of time and coin.”')
                    $ custom1 = "“True, true. You have bards and scrolls anyway. Songs are warmer than rocks.”"
                    jump wandererfirsttime01wondering03foragers
                '“Pride blinds people, makes them commit stupid mistakes. It’s a good thing that priests teach others to avoid it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pride blinds people, makes them commit stupid mistakes. It’s a good thing that priests teach others to avoid it.”')
                    $ custom1 = "{color=#f6d6bd}Tzvi{/color} smirks. “You say it as if the preachers are not some of the most prideful people of all.”"
                    jump wandererfirsttime01wondering03foragers
                '“I don’t know. It’s stupid.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know. It’s stupid.”')
                    $ custom1 = "He laughs. “Sure, who cares. They are there, we are here. They have no power over this road.”"
                    jump wandererfirsttime01wondering03foragers
        '“A few, but I haven’t paid much attention to them.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A few, but I haven’t paid much attention to them.”')
            $ description_hovlavan04 = "oldstatuesnoattention"
            $ custom1 = "He laughs. “Sure, who cares. They are there, we are here. They have no power over this road.”"
            jump wandererfirsttime01wondering03foragers

#########################################

label wanderer_fishtrapALL:
    label wanderer_fishtrap01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend some time setting up a fish trap at the bank.')
        show fishtrap wanderer01 at basicfade
        $ quarters += 2
        $ item_fishtrap -= 1
        $ wanderer_fishtrap = 1
        $ wanderer_fishtrap_daychecked = day
        $ wanderer_fishtrap_working = day
        $ wanderer_fishtrap_fishtimer = renpy.random.randint(1, 2)
        $ wanderer_fishtrap_fishtimer = (wanderer_fishtrap_fishtimer+day)
        menu:
            'You place the basket on the ground, then grab a bowl and start digging, looking for a few larger worms. You bait the stick and push it inside the basket, locking it between the sides, then cover the entrance with the lid - tying it together takes you a few good moments, but will be easier later on. You attach the entire trap to the tree and place it into the brook, moving it around to make sure it stays in place.
            \n\nWho knows how long it will take before something large enough swims inside. Still, it would be better to not wait for too long - otherwise, the prey may die of hunger.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wanderer_fishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the fish trap had any luck.')
        if wanderer_fishtrap_fishtimer > day:
            $ wanderer_fishtrap_daychecked = day
            $ minutes += 5
            menu:
                'Unfortunately, it’s still empty.
                '
                'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                    jump wandererregular01reasontoclear
                'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                    pass
                'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                    jump wandererregular02removingwithaxe
                'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                    pass
                'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                    jump wandererregular02removingwithwitheringdust
                'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                    jump wandererregular02takingthecoin
                'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                    jump wandererregular02leavinganoffering
                'I consider washing myself in the stream.':
                    jump wandererstream01
                ###########################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                    jump wanderer_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                    jump wanderer_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                    jump wanderer_fishtrap03
                'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                    jump wanderer_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                    pass
        elif wanderer_fishtrap_fishtimer+3 > day:
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            $ d100roll += wanderer_fishtrap_badthingmodifier
            $ minutes += 5
            if d100roll > 110: # harsh fail
                $ wanderer_fishtrap_badthingmodifier = 0
                $ wanderer_fishtrap_working = 0
                $ wanderer_fishtrap = 0
                hide fishtrap
                $ wanderer_fishtrap_fishtimer = 0
                $ wanderer_fishtrap_daychecked = 0
                menu:
                    'Sadly, the trap is not only empty, but also damaged beyond repairs. Some sort of predator, might have been a saurian, a wolf, a runner, or a different creature with large claws, had decided to steal your catch. To do so, it tore the vines apart and broke through the wood.
                    '
                    'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                        jump wandererregular01reasontoclear
                    'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                        pass
                    'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                        jump wandererregular02removingwithaxe
                    'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        pass
                    'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                        jump wandererregular02removingwithwitheringdust
                    'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                        jump wandererregular02takingthecoin
                    'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                        jump wandererregular02leavinganoffering
                    'I consider washing myself in the stream.':
                        jump wandererstream01
                    ###########################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                        jump wanderer_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                        jump wanderer_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                        jump wanderer_fishtrap03
                    'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                        jump wanderer_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                        pass
            else: # success
                $ wanderer_fishtrap_fishtimer = 0
                $ quarters += 1
                if wanderer_fishtrap_badthingmodifier:
                    $ wanderer_fishtrap_badthingmodifier += 20
                $ wanderer_fishtrap_working = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if d100roll > 50:
                    $ item_rawfishtotalnumber += 2
                    $ achievement_fish += 2
                    $ item_rawfish_gaining = 2
                    $ renpy.notify("You caught 2 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 2 fish.{/i}')
                    $ custom1 = "You pull the rope and see two flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the brook, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                else:
                    $ item_rawfishtotalnumber += 3
                    $ achievement_fish += 3
                    $ item_rawfish_gaining = 3
                    $ renpy.notify("You caught 3 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 3 fish.{/i}')
                    $ custom1 = "You pull the rope and see three flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the brook, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                menu:
                    '[custom1]
                    '
                    'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                        jump wandererregular01reasontoclear
                    'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                        pass
                    'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                        jump wandererregular02removingwithaxe
                    'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        pass
                    'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                        jump wandererregular02removingwithwitheringdust
                    'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                        jump wandererregular02takingthecoin
                    'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                        jump wandererregular02leavinganoffering
                    'I consider washing myself in the stream.':
                        jump wandererstream01
                    ###########################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                        jump wanderer_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                        jump wanderer_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                        jump wanderer_fishtrap03
                    'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                        jump wanderer_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                        pass
        else:
            $ wanderer_fishtrap_badthingmodifier = 0
            $ wanderer_fishtrap_working = 0
            $ wanderer_fishtrap = 0
            hide fishtrap
            $ wanderer_fishtrap_fishtimer = 0
            $ wanderer_fishtrap_daychecked = 0
            menu:
                'Sadly, the trap is not only empty, but also damaged beyond repairs. Some sort of predator, might have been a saurian, a wolf, a runner, or a different creature with large claws, had decided to steal your catch. To do so, it tore the vines apart and broke through the wood.
                '
                'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                    jump wandererregular01reasontoclear
                'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                    pass
                'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                    jump wandererregular02removingwithaxe
                'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                    pass
                'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                    jump wandererregular02removingwithwitheringdust
                'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                    jump wandererregular02takingthecoin
                'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                    jump wandererregular02leavinganoffering
                'I consider washing myself in the stream.':
                    jump wandererstream01
                ###########################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                    jump wanderer_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                    jump wanderer_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                    jump wanderer_fishtrap03
                'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                    jump wanderer_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                    pass

    label wanderer_fishtrap03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I set the fish trap again.')
        $ wanderer_fishtrap_working = day
        $ minutes += 5
        $ wanderer_fishtrap = 1
        show fishtrap wanderer01 at basicfade
        $ wanderer_fishtrap_daychecked = day
        $ wanderer_fishtrap_fishtimer = renpy.random.randint(1, 4)
        $ wanderer_fishtrap_fishtimer = (wanderer_fishtrap_fishtimer+day)
        menu:
            'You need to look for worms again, but at least sealing the lid takes only a moment.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

    label wanderer_fishtrap04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the trap back')
        $ minutes += 5
        $ item_fishtrap += 1
        $ renpy.notify("You dismantled the trap.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You dismantled the trap.{/i}')
        $ wanderer_fishtrap = 0
        hide fishtrap
        $ wanderer_fishtrap_daychecked = 0
        $ wanderer_fishtrap_working = 0
        $ wanderer_fishtrap_fishtimer = 0
        menu:
            'You shake the basket, expecting it will get drier during your ride, then attach it to your saddle.
            '
            'I could get rid of these branches. Clear the space in front of the statue.' if not wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could get rid of these branches. Clear the space in front of the statue.')
                jump wandererregular01reasontoclear
            'I’m too tired to clean the statue with my axe. (Required vitality: 1) (disabled)' ( condition="pc_hp < 1 and not wanderer_cleared and wanderer_cleared_why" ):
                pass
            'In about half an hour I could use my axe to cut down the bushes and twigs.' ( condition="pc_hp and not wanderer_cleared and wanderer_cleared_why" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In about half an hour I could use my axe to cut down the bushes and twigs.')
                jump wandererregular02removingwithaxe
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                pass
            'I have the “withering dust.” I can use it to get rid of these bushes.' if item_witheringdust and not wanderer_cleared and wanderer_cleared_why:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use the “withering dust” I have to get rid of these bushes.')
                jump wandererregular02removingwithwitheringdust
            'I don’t care anymore. I take the coin.' if wanderer_cleared and not wanderer_coin_taken and not wanderer_coin_gone and not wanderer_offering:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care anymore. I take the coin.')
                jump wandererregular02takingthecoin
            'I make an offering to The Wanderer to ask her for protection.' if wanderer_cleared and not wanderer_offering and not wanderer_coin_taken and wanderer_name == "The Wanderer":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make an offering to The Wanderer to ask her for protection.')
                jump wandererregular02leavinganoffering
            'I consider washing myself in the stream.':
                jump wandererstream01
            ###########################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not wanderer_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not wanderer_fishtrap and quarters <= (world_daylength-8)" ):
                jump wanderer_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not wanderer_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked != day:
                jump wanderer_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if wanderer_fishtrap and wanderer_fishtrap_working and wanderer_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if wanderer_fishtrap and not wanderer_fishtrap_working:
                jump wanderer_fishtrap03
            'I take the fish trap back.' if wanderer_fishtrap and not wanderer_fishtrap_working and not item_fishtrap:
                jump wanderer_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if wanderer_fishtrap and not wanderer_fishtrap_working and item_fishtrap:
                pass

label wandererstream01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider washing myself in the stream.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
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
        'The brook would hardly cover your feet, but you could sit on the pebbles and splash yourself with water.
        \n\n[custom1][custom2]
        '
        'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
            jump wandererstreamwashing01
        'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump wandererstreamwashing01
        'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
            jump wandererstreamwashing01
        'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'In less than an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- In less than an hour I’ll remove blood stains from my clothes.')
            jump wandererstreamlaundry01
        'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump wandererregular03afterinteraction

    label wandererstreamwashing01:
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
            'As you wash your sweaty skin, {color=#f6d6bd}[horsename]{/color} quenches its thirst and looks for intruders.
            '
            'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
                jump wandererstreamwashing01
            'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump wandererstreamwashing01
            'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump wandererstreamwashing01
            'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In less than an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In less than an hour I’ll remove blood stains from my clothes.')
                jump wandererstreamlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump wandererregular03afterinteraction

    label wandererstreamlaundry01:
        $ cleanliness_clothes_blood = 0
        $ quarters += 3
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'You soak and rub the fabric in the crystal clear flowing water and, when necessary, you pound them on the flat rocks. It takes you hardly any time.
            '
            'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
                jump wandererstreamwashing01
            'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump wandererstreamwashing01
            'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump wandererstreamwashing01
            'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In less than an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- In less than an hour I’ll remove blood stains from my clothes.')
                jump wandererstreamlaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump wandererregular03afterinteraction
