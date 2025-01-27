# ###################### NORTHERN ROAD
default northernroad_firsttime = 0
default northernroad_fluff = ""
default northernroad_fluff_old = ""
default northernroad_monkeys_fluff = ""
default northernroad_monkeys_earplugs_fluff = ""

default northernroad_monkeys = 1 # 0 - are running away, 1 - are around, 2 - are pissed off, 3 - are pissed off, but not present right now
default northernroad_monkeys_bravery = 0
default northernroad_monkeys_fear = 0
default northernroad_monkeys_scaredday = 0
default northernroad_monkeys_earplugs = 0

default northernroad_rawhide_taken = 0
default northernroad_rawhide_owner = 0

default northernroad_trail = 0

default northernroad_fishtrap = 0
default northernroad_fishtrap_working = 0
default northernroad_fishtrap_daychecked = 0
default northernroad_fishtrap_fishtimer = 0
default northernroad_fishtrap_badthingmodifier = 0

label northernroad01:
    nvl clear
    $ pc_area = "northernroad"
    stop music fadeout 4.0
    if not northernroad_rawhide_taken:
        show areapicture northernroad01 at basicfade behind fishtrap
    else:
        show areapicture northernroad02 at basicfade behind fishtrap
    if northernroad_fishtrap:
        show fishtrap northernroad01 at basicfade
    $ northernroad_monkeys_earplugs_fluff = ""
    label northernroad_fluffloop:
        $ northernroad_fluff = renpy.random.choice(['Your mount’s hooves are pounding the ground loudly, and a few ducks flee into the lake.', 'There’s hardly any wind. The lake smells of reeds and wet.', 'Even the loud crickets can’t hide the loud splash of a creature that just jumped into the lake.', 'You prepare your axe, hearing a suspicious rustle coming from the meadows, but whatever was behind it is now running away from you.', 'A multitude of bubbles is coming from the lake, and there’s a group of crows circling high above it.', 'A stout, brown beaver clumsily carries a pile of twigs in its front paws. Noticing your arrival, it lets out a terrified whine and disappears in the lake. It left one of the sticks behind it.'])
        if northernroad_fluff_old == northernroad_fluff:
            jump northernroad_fluffloop
        else:
            $ northernroad_fluff_old = northernroad_fluff
    if not northernroad_monkeys:
        $ northernroad_monkeys_fluff = "The howlers are spread on the branches, but as you get closer, they flee through the tall grasses. Only a few stay nearby, observing you with a mixture of curiosity and caution."
    if northernroad_monkeys == 1:
        $ northernroad_monkeys_fluff = "The howlers gather around as you approach their tree. The smallest of them are hanging from the branches, while a few larger ones get on the ground, observing you from the tall grasses."
        if northernroad_monkeys_earplugs:
            $ northernroad_monkeys_earplugs_fluff = " You plug your ears quickly."
        else:
            $ northernroad_monkeys_earplugs_fluff = ""
    if northernroad_monkeys == 2:
        $ northernroad_monkeys_fluff = "The howlers are yelling at you from among the leaves, giving you quite a headache. The smallest of them are swinging their arms or hanging from the branches by their tails, while a few larger ones get on the ground, getting a bit too close."
        if northernroad_monkeys_earplugs:
            $ northernroad_monkeys_earplugs_fluff = " You plug your ears quickly."
        else:
            $ northernroad_monkeys_earplugs_fluff = ""
    if northernroad_monkeys == 3:
        if northernroad_monkeys_scaredday < day:
            $ northernroad_monkeys = 2
            $ northernroad_monkeys_fluff = "The howlers are back. They shake their heads and swing their arms as you get closer to the tree."
            if northernroad_monkeys_earplugs:
                $ northernroad_monkeys_earplugs_fluff = " You plug your ears quickly."
            else:
                $ northernroad_monkeys_earplugs_fluff = ""
        else:
            $ northernroad_monkeys_fluff = "From the north come the shouts of howlers, but you see none of them around."
    if not northernroad_monkeys:
        play nature "audio/ambient/northernroad02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if northernroad_monkeys == 1:
        if not northernroad_monkeys_earplugs:
            play nature "audio/ambient/northernroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        else:
            play nature "audio/ambient/northernroad01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if northernroad_monkeys == 2:
        if not northernroad_monkeys_earplugs:
            play nature "audio/ambient/northernroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        else:
            play nature "audio/ambient/northernroad01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if northernroad_monkeys == 3:
        play nature "audio/ambient/northernroad02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not northernroad_firsttime:
        $ world_known_areas += 1
        $ northernroad_firsttime = 1
        $ ruinedshelter_unlocked = 1
        $ foggylake_unlocked = 1
        jump northernroadfirsttime01
    else:
        jump northernroadregular01

label northenroadhowlersALL:
    label northernroadfirsttime01:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        if persistent.deafmode:
            $ deafcustom1 = "Your lively surroundings are filled with the chirping of crickets, the flapping wings of dragonflies, and the occasional quacks and splashes of ducks. Still, the sounds that strike you the harshest are the deep, loud yells of howlers, which spark an image of the painful shout of an undead, of a cracking tree, or of the battle cry of a nightmarish spirit.\n\n"
        else:
            $ deafcustom1 = "The deep, loud yells of howlers are piercing your ears, concealing any other sound in the area. "
        menu:
            '[deafcustom1]They’re sitting on branches and in the tall grass, not really trying to hide. Their thick black-and-gold furs cover their entire shells, aside from the charcoal-black faces with roundish, flat noses and wide nostrils. The younger members of the pack are about the size of your mount’s head, but the larger ones would be chest-high if it wasn’t for the fact they walk on all fours. Their long tails are like an additional arm, helping them climb, hang from the branches, or hold food while they eat.
            \n\nThey aren’t particularly muscular, but when they form their pink lips into the shape of a cup to release their howls, their mouths are so wide they could fit your entire arm inside. As you listen to the shouts, you reach for your head - you feel a weird itch, but somehow you can’t scratch it.
            '
            'Keeping my distance, I take a look at the hide behind the boulder.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Keeping my distance, I take a look at the hide behind the boulder.')
                menu:
                    'The whitish rawhide covers the grass like a blanket, surrounded by paw prints. The howlers don’t wait for you to approach it - one of the larger ones jumps on the ground, leaning on its hands and challenging you with its gaze. It has rather blunt teeth.
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass

    label northernroadusingearplugs01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Just in case, I plug my ears.')
        play nature "audio/ambient/northernroad01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        $ northernroad_monkeys_earplugs = 1
        if item_earplugs == "wool":
            $ custom1 = "You stick the wool into your ears. The first touch is soft, but as you push more of it inside, the plugs keep falling out, and distract you with the newly muffled sounds."
            $ minutes += 5
        elif item_earplugs == "cotton":
            $ custom1 = "You stick the cotton into your ears. The first touch is soft, but as you push more of it inside, the plugs keep falling out, and distract you with the newly muffled sounds."
            $ minutes += 5
        elif item_earplugs == "wax":
            $ custom1 = "You stick the wax into your ears. The first touch is rather unpleasant, but after only a few attempts the plugs seem to stay in their place, even after you shake your head. The one issue is that they distract you with the newly muffled sounds."
        else:
            $ custom1 = "You’re a bit distracted by the newly muffled sounds"
        menu:
            '[custom1] The howling gets less intrusive, but as long as you have ears, some of it will reach you.
            '
            'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                jump northernroadusingearplugs01
            'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                pass
            '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                jump northernroadfightinghowlers01
            'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                pass
            'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                pass
            'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                jump northernroadrawhidetryingtotake00
            '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                jump northernroadrawhidetryingtotake01
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                pass
            '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                jump northernroadrawhidetryingtotake02
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                pass
            ##################################################
            'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                jump northernroadrawhidetryingtofindthetraces01
            'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                pass
            'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                pass
            'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                $ travel_destination = "howlerslair"
                jump finaldestination
            'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                pass
            ##################################################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                jump northernroad_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                jump northernroad_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                jump northernroad_fishtrap03
            'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                jump northernroad_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                pass

    label northernroadfightinghowlers01all:
        label northernroadfightinghowlers01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I try to scare the howlers away.')
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                'You’re yards away from the closest tree. The howlers are climbing, swinging, browsing the leaves, and seeking bugs in the meadow. Only a few of them pay attention to you.
                \n\nYou could start with an attack from a distance, but there’s no way for you to take down an entire pack. The best you can hope for is scaring them off.
                '
                'That’s a job for my crossbow.' if item_crossbow and item_crossbowquarrels:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- That’s a job for my crossbow.')
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    $ northernroad_monkeys_fear -= 1
                    menu:
                        'You load the smooth weapon and take some time to aim, looking for a beast focused on eating, rather than playing. You pull the trigger, the monkey screams - still alive, but holding its wounded side. It falls on the ground, miraculously landing on its paws.
                        \n\nYou get noticed right after that. The creatures howl even louder, pointing at you and jumping between branches. The wounded howler runs north, into the meadow, complaining through its shouts.
                        \n\nIts largest companions land on the grass.
                        '
                        'I move forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                            $ custom3 = "The confused howlers step back, not sure why you are not running away."
                            jump northernroadfightinghowlers02
                'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and not item_crossbowquarrels:
                    pass
                'I don’t have a crossbow. (disabled)' if not item_crossbow:
                    pass
                '{image=d6} I cast a few rocks at them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I cast a few rocks at them.')
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
                        $ d100roll -= (pc_battlecounter*4)
                    else:
                        $ d100roll -= (pc_battlecounter*2)
                    if d100roll > 40: # fail
                        $ northernroad_monkeys_bravery += 1
                        menu:
                            'Your poor aim makes you hit the trunk, drawing the monkeys’ attention. They howl even louder, pointing at you and jumping between branches. Your rocks don’t hurt them much - they stay still thanks to their tails and cover their faces with their hands.
                            \n\nThe largest ones land on the grass.
                            '
                            'I move forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                                $ custom3 = "The confused howlers step back, not sure why you are not running away."
                                jump northernroadfightinghowlers02
                    else: # success
                        $ northernroad_monkeys_fear += 1
                        menu:
                            'You hit a few of them. Three of the monkeys shout at everything in sight with an outraged complaint, then start to point at you. They howl even louder, a few jump between branches.
                            \n\nThe largest ones land on the grass.
                            '
                            'I move forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                                $ custom3 = "The confused howlers step back, not sure why you are not running away."
                                jump northernroadfightinghowlers02
                'I’d rather get closer.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather get closer.')
                    $ custom3 = "You get noticed right away. The creatures howl even louder, pointing at you and jumping between branches. The largest monkeys land on the grass, displaying their muscular chests."
                    jump northernroadfightinghowlers02
                'Forget it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                    jump northernroadafterinteraction01

        label northernroadfightinghowlers02:
            menu:
                '[custom3]
                '
                'I rise and swing the head of the furless wolf.' if item_furlesswolftrophy:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rise and swing the head of the furless wolf.')
                    $ northernroad_monkeys_fear += 1
                    menu:
                        'The bloody and smelly flesh makes for a haunting totem. The howlers point at it, making somewhat higher howls. The smaller monkeys cuddle with each other and hide their faces. Those on the ground take the first few steps forward, but they keep looking at each other, waiting for one of them to start.
                        '
                        'Time for the confrontation.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                            $ custom3 = "You leap forward, reaching for the..."
                            jump northernroadfightinghowlers03
                'Maybe the troll urine will be of help here.' if item_trollurine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the troll urine will be of help here.')
                    $ northernroad_monkeys_fear += 2
                    menu:
                        'You open the jar and splash some of its content before you. The howls get higher and whinier, the beasts leap away. One of the larger ones flees through the meadow, shouting in panic.
                        \n\nThe smaller monkeys start cuddling, hiding their faces, or disappear behind the tree trunk. Those on the ground take the first few steps forward, but they keep looking at each other, waiting for one of them to start.
                        '
                        'Time for the confrontation.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                            $ custom3 = "You leap forward, reaching for the..."
                            jump northernroadfightinghowlers03
                'I blow into the dragon horn.' if item_dragonhorn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blow into the dragon horn.')
                    $ northernroad_monkeys_fear += 2
                    menu:
                        'You press the horn to your lips and after the first, failed attempt, you fill the grasslands and the lake with the terrifying shout of a monster. The howls get higher and whinier, and some of the beasts leap away. One of the larger ones flees through the meadow, shouting in panic.
                        \n\nThe smaller monkeys start cuddling, hiding their faces, or disappear behind the tree trunk. Those on the ground take the first few steps forward, but they keep looking at each other, waiting for one of them to start.
                        '
                        'Time for the confrontation.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                            $ custom3 = "You leap forward, reaching for the..."
                            jump northernroadfightinghowlers03
                '{image=d6} I shout at the monkeys and swing my arms.' if northernroad_monkeys != 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I shout at the monkeys and swing my arms.')
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ d100roll -= (pc_hp*5)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if d100roll > 40: # fail
                        $ northernroad_monkeys_bravery += 1
                        menu:
                            'Your shout is overshadowed by the furious howls. The monkeys take the first few steps forward.
                            '
                            'Time for the confrontation.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                                $ custom3 = "You leap forward, reaching for the..."
                                jump northernroadfightinghowlers03
                    else: # success
                        $ northernroad_monkeys_fear += 1
                        menu:
                            'At first you doubt your shout is going to be heard, but once you add to it your aggressive gestures, the creatures get quieter, allowing your voice to spread wider. Some of the smaller monkeys cuddle to each other and hide their faces. Those on the ground take the first few steps forward, but they keep looking at each other, as if hoping another one will get to you first.
                            '
                            'Time for the confrontation.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                                $ custom3 = "You leap forward, reaching for the..."
                                jump northernroadfightinghowlers03
                'They howl so furiously that they won’t even notice my humble shouts. (disabled)' if northernroad_monkeys == 2:
                    pass
                'I’ve nothing that could scare them. (disabled)' if not item_furlesswolftrophy and not item_trollurine and not item_dragonhorn:
                    pass
                'Time for the confrontation.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for the confrontation.')
                    $ custom3 = "The monkeys on the ground step forward. You reach for the..."
                    jump northernroadfightinghowlers03

        label northernroadfightinghowlers03:
            if northernroad_monkeys_earplugs:
                $ custom1 = "You get dizzy, but try to keep your movements swift and confident. The muffled sounds, while annoying, remain at the edge of your senses.\n\n"
            else:
                $ custom1 = "Your head aches as if you’re getting hit by a smith’s hammer, time and time again. You want to touch your stomach to stop its strange movements - it’s as if your guts are shaking and hitting one another.\n\n"
            if pc_class == "mage":
                $ at_unlock_spell = 1
                $ at = 0
                $ manacost = 3
            menu:
                '[custom1][custom3]
                '
                'My wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My wand.')
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ northernroad_monkeys_fear += 1
                    $ mana = limit_mana(mana-manacost)
                    menu:
                        'You unwrap the linen sheet and grab the willow twig, still as smooth as on the day you bought it. It’s pointy and thin, but heavy from the injected quicksilver. You raise it as if you are about to stab the air with a dagger, then make a swipe.
                        \n\nThe invisible wave hits the monkey as it tries to jump at you, and sends it right back, plunging it to the ground. The other creatures are standing still, not sure what exactly happened.
                        '
                        'I reach for my blade.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for my blade.')
                            jump northernroadfightinghowlersfinal
                'My pneuma is too weak for a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost" ):
                    pass
                'The blinding powder.' if item_blindingpowder:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The blinding powder.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ northernroad_monkeys_fear += 1
                    menu:
                        'You throw it in front of you and jump away from the monkeys. You don’t look at them for a few heartbeats, but their painful screams assure you that the dust is working. They cover their faces with their large hands, landing on their buns or moving away in panic. The remaining few are standing still, not sure what exactly happened.
                        '
                        'I reach for my blade.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for my blade.')
                            jump northernroadfightinghowlersfinal
                'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                    pass
                '{image=d6} The spear.' if item_asterionspear or item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} The spear.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ d100roll -= (pc_hp*5)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if pc_class == "warrior":
                        $ d100roll -= (pc_battlecounter*4)
                    else:
                        $ d100roll -= (pc_battlecounter*2)
                    if d100roll > 60: # fail
                        $ northernroad_monkeys_bravery += 1
                        menu:
                            'You stab two of the creatures from a safe distance, but the others dodge your attacks with little effort. You put your strength into a precise thrust, surprising one of the assailants with a lunge, then move back, but they’re already trying to surround you.
                            '
                            'I turn toward the next opponent.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the next opponent.')
                                jump northernroadfightinghowlersfinal
                    else: # success
                        $ northernroad_monkeys_fear += 1
                        menu:
                            'You lunge forward, surprising one of the assailants with a stab in its chest. The painful scream is soon followed by its rapid, chaotic escape. You then move back swiftly, keeping the safe distance before they surround you.
                            '
                            'I turn toward the next opponent.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the next opponent.')
                                jump northernroadfightinghowlersfinal
                '{image=d6} The shield and axe.' if item_shield:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} The shield and axe.')
                    label northernroadfightinghowlers03part2:
                        $ at_unlock_spell = 0
                        $ at = 0
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        $ d100roll -= (pc_hp*5)
                        if not pc_food:
                            $ d100roll += 5
                        if pc_food == 3:
                            $ d100roll -= 5
                        if armor == 4:
                            $ d100roll -= 5
                        if pc_food == 4:
                            $ d100roll -= 10
                        if pc_class == "warrior":
                            $ d100roll -= (pc_battlecounter*4)
                        else:
                            $ d100roll -= (pc_battlecounter*2)
                        if item_shield:
                            $ d100roll -= 10
                        if item_golemglove:
                            $ d100roll -= 10
                        if item_axe03:
                            $ d100roll -= 20
                        elif item_axe02 or item_axe02alt:
                            $ d100roll -= 10
                        if d100roll > 30: # fail
                            $ northernroad_monkeys_bravery += 1
                            if item_shield:
                                $ custom2 = "At least the shield helps you focus on the more vulnerable parts of your defense."
                            else:
                                $ custom2 = "Having no shield, you’re vulnerable from all sides."
                            menu:
                                'You clash with one of the creatures. The blunt side of the weapon lands on its arm. You escape the beast’s grapple, but the assailant doesn’t even yell. You leap away, struggling to keep the distance. Your next hit finally spills some blood, getting into the howler’s shoulder, but the others are already surrounding you.
                                \n\nYou look for a way to escape their approach. [custom2]
                                '
                                'I turn toward the next opponent.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the next opponent.')
                                    jump northernroadfightinghowlersfinal
                        else: # success
                            $ northernroad_monkeys_fear += 1
                            if item_axe03:
                                $ custom1 = "your fine axe gets so deep that you almost chop away the entire arm, and the beast lands on the ground, screaming, then tries to get away on its three other limbs"
                            elif item_axe02 or item_axe02alt:
                                $ custom1 = "your axe cuts fairly deep. The beast jumps away, screaming, then tries to get away on its three other limbs"
                            else:
                                $ custom1 = "you release the beast’s blood, and it jumps away, screaming. It’s limping around you, then flees into the meadow"
                            if item_shield:
                                $ custom2 = ", and the shield helps you focus on the more vulnerable parts of your defense. You are in control."
                            else:
                                $ custom2 = ". You’re not sure you can protect yourself from all sides at once, especially without a shield, but for now, you are in control."
                            menu:
                                'You clash with one of the creatures, and the weapon lands on its shoulder - [custom1]. You make a few dangerous swings, keeping the other beasts at a distance. They try to surround you, but you manage to keep up with them[custom2]
                                '
                                'I turn toward the next opponent.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the next opponent.')
                                    jump northernroadfightinghowlersfinal
                '{image=d6} My axe.' if not item_shield:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} My axe.')
                    $ at = 0
                    jump northernroadfightinghowlers03part2

        label northernroadfightinghowlersfinal:
            $ northernroad_monkeys_scaredday = day
            if northernroad_monkeys_bravery > northernroad_monkeys_fear: # harsh fail
                $ northernroad_monkeys = 2
                $ northernroad_monkeys_bravery = 0
                $ northernroad_monkeys_fear = 0
                menu:
                    'You look around, then duck - another creature tries to jump at you from your left. The monkeys are determined to get to you, led more by their fury than fear. There’s no chance you could face them in a fair fight.
                    '
                    'I run as fast as I can.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run as fast as I can.')
                        jump northernroadleaving01
            elif northernroad_monkeys_bravery == northernroad_monkeys_fear: # soft fail
                $ northernroad_monkeys = 3
                $ northernroad_monkeys_bravery = 0
                $ northernroad_monkeys_fear = 0
                play nature "audio/ambient/northernroad02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                menu:
                    'You look around, then duck - another creature tries to jump at you from your left. You land a hit, step away, and take a breath, considering escape. However, the wounded monkeys flee, and the others follow them soon after. From time to time, they turn around and give you angry looks.
                    \n\nThey’ll be back.
                    '
                    'I put away my weapons.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put away my weapons.')
                        jump northernroadafterinteraction01
            else: # full success
                $ howlerslair_advantage_points_bonus += 1
                $ northernroad_monkeys = 0
                $ northernroad_monkeys_bravery = 0
                $ northernroad_monkeys_fear = 0
                play nature "audio/ambient/northernroad02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                menu:
                    'You look around, but no more creatures try to approach you. You step forward and raise your blade. The wounded monkeys run away, and the others follow them soon after. They don’t look back.
                    \n\nYou doubt they’ll forget the threat you pose.
                    '
                    'I put away my weapons.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put away my weapons.')
                        jump northernroadafterinteraction01

    label northernroadrawhidetryingtotake00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since there are no monkeys around, I approach the rawhide.')
        $ northernroad_rawhide_taken = 1
        show areapicture northernroad02 at basicfade behind fishtrap
        $ item_rawhide = 1
        $ renpy.notify("You picked up the old rawhide.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
        menu:
            'Having no resistance, you check for snakes by stepping onto the rawhide, then pick it up. The wet, torn blanket is now worth as much as a bread crust.
            \n\nStill, it’s not rotten - if the owner is around, they may recognize it.
            '
            'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                jump northernroadusingearplugs01
            'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                pass
            '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                jump northernroadfightinghowlers01
            'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                pass
            'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                pass
            'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                jump northernroadrawhidetryingtotake00
            '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                jump northernroadrawhidetryingtotake01
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                pass
            '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                jump northernroadrawhidetryingtotake02
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                pass
            ##################################################
            'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                jump northernroadrawhidetryingtofindthetraces01
            'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                pass
            'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                pass
            'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                $ travel_destination = "howlerslair"
                jump finaldestination
            'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                pass
            ##################################################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                jump northernroad_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                jump northernroad_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                jump northernroad_fishtrap03
            'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                jump northernroad_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                pass

    label northernroadrawhidetryingtotake01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.')
        $ northernroad_rawhide_taken = 1
        show areapicture northernroad02 at basicfade behind fishtrap
        $ item_rawhide = 1
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        $ d100roll -= (pc_hp*5)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if northernroad_monkeys_earplugs:
            $ d100roll -= 20
        if d100roll > 60: # harsh success
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ renpy.notify('You picked up the old rawhide.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                $ custom1 = "pushing your jacket to its limits"
            else:
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                $ renpy.notify("You picked up the old rawhide.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                $ custom1 = "painfully rubbing your skin"
            if northernroad_monkeys_earplugs:
                $ custom2 = "You get dizzy, but not much more than that - your movements are swift and confident as you ignore the muffled sounds.\n\n"
            else:
                $ custom2 = "You get dizzy, and soon the pain enters your skull, as if you’re getting hit by a smith’s hammer, time and time again. Yet you manage to stay calm, focused on your goal.\n\n"
            menu:
                'You stretch out your legs, then dash ahead. At first, the monkeys move away with a few unconvinced yells, but then those from above start to howl, even deeper than before, and you feel as if your guts are starting to move, hitting against each other. [custom2] The larger creatures try to cut your path, but, being on the ground, they can’t keep up with your legs. Without stopping, you grab the rawhide, then carry on, waiting for a few heartbeats before you change direction rapidly, now getting closer to {color=#f6d6bd}[horsename]{/color}...
                \n\nThe largest beast leaps from behind a tree and lands right next to you. Its hit flings you back, you crush into the ground and scrape against the beaten ground, [custom1]. Your side hurts, but you get back on your feet, still holding the blanket.
                \n\nYour mount snorts and walks away, ready to flee.
                '
                'I chase after it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I chase after it.')
                    jump northernroadleaving01withrawhide
        else: # full success
            if northernroad_monkeys_earplugs:
                $ custom2 = "You get dizzy, but not much more than that - your movements are swift and confident as you ignore the muffled sounds.\n\n"
            else:
                $ custom2 = "You get dizzy, and soon the pain enters your skull, as if you’re getting hit by a smith’s hammer, time and time again. Yet you manage to stay calm, focused on your goal.\n\n"
            $ renpy.notify("You picked up the old rawhide.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
            menu:
                'You stretch out your legs, then dash ahead. At first, the monkeys move away with a few unconvinced yells, but then those from above start to howl, even deeper than before, and you feel as if your guts are starting to move, hitting against each other. [custom2] The larger creatures try to cut your path, but, being on the ground, they can’t keep up with your legs. Without stopping, you grab the rawhide, then carry on, waiting for a few heartbeats before you change direction rapidly, now getting closer to {color=#f6d6bd}[horsename]{/color}. By the time you reach the saddle, the beasts have already abandoned their pursuit.
                \n\nYou take a few deep breaths, then inspect the rawhide. The wet, torn blanket is now worth as much as a bread crust.
                \n\nStill, it’s not rotten - if the owner is around, they may recognize it.
                '
                'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                    jump northernroadusingearplugs01
                'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                    pass
                '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                    jump northernroadfightinghowlers01
                'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                    pass
                'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                    pass
                'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                    jump northernroadrawhidetryingtotake00
                '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                    jump northernroadrawhidetryingtotake01
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                    pass
                '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                    jump northernroadrawhidetryingtotake02
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                    pass
                ##################################################
                'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                    jump northernroadrawhidetryingtofindthetraces01
                'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                    pass
                'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                    pass
                'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                    $ travel_destination = "howlerslair"
                    jump finaldestination
                'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                    pass
                ##################################################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                    jump northernroad_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                    jump northernroad_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                    jump northernroad_fishtrap03
                'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                    jump northernroad_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                    pass

    label northernroadrawhidetryingtotake02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.')
        $ northernroad_rawhide_taken = 1
        show areapicture northernroad02 at basicfade behind fishtrap
        $ item_rawhide = 1
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        $ d100roll -= (pc_hp*5)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if northernroad_monkeys_earplugs:
            $ d100roll -= 20
        if d100roll > 65: # harsh success
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ renpy.notify('You picked up the old rawhide.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                $ custom1 = "pushing your jacket to its limits"
            elif armor == 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ renpy.notify('You picked up the old rawhide.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                $ custom1 = "pushing your jacket to its limits and painfully rubbing your skin"
            else:
                $ renpy.notify("You picked up the old rawhide.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-2)
                $ custom1 = "painfully rubbing your skin"
            if northernroad_monkeys_earplugs:
                $ custom2 = "You get dizzy, but not much more than that - your movements are swift and confident as you ignore the muffled sounds.\n\n"
            else:
                $ custom2 = "You get dizzy, and soon the pain enters your skull, as if you’re getting hit by a smith’s hammer, time and time again. Yet you manage to stay calm, focused on your goal.\n\n"
            menu:
                'You stretch out your legs, then dash ahead. At first, the monkeys move away with a few unconvinced yells, but then those from above start to howl, even deeper than before, and you feel as if your guts are starting to move, hitting against each other. [custom2] The larger creatures try to cut your path, and one of them manages to keep up with you. It tries to grab your legs, but your boot lands on its face. You have already slowed down - another creature grabs you, and you use all the strength you can muster to get away.
                \n\nWithout stopping, you grab the rawhide, then carry on, waiting for a few heartbeats before you change direction rapidly, now getting closer to {color=#f6d6bd}[horsename]{/color}...
                \n\nThe largest beast leaps from behind a tree and lands right next to you. Its hit flings you back, you crush into the ground and scrape against the beaten ground, [custom1]. Your side hurts, but you get back on your feet, still holding the blanket.
                \n\nYour mount snorts and walks away, ready to flee.
                '
                'I chase after it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I chase after it.')
                    jump northernroadleaving01withrawhide
        elif d100roll > 40: # light success
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ renpy.notify('You picked up the old rawhide.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                $ custom1 = "pushing your jacket to its limits"
            else:
                $ renpy.notify("You picked up the old rawhide.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                $ custom1 = "painfully rubbing your skin"
            if northernroad_monkeys_earplugs:
                $ custom2 = "You get dizzy, but not much more than that - your movements are swift and confident as you ignore the muffled sounds.\n\n"
            else:
                $ custom2 = "You get dizzy, and soon the pain enters your skull, as if you’re getting hit by a smith’s hammer, time and time again. Yet you manage to stay calm, focused on your goal.\n\n"
            menu:
                'You stretch out your legs, then dash ahead. At first, the monkeys move away with a few unconvinced yells, but then those from above start to howl, even deeper than before, and you feel as if your guts are starting to move, hitting against each other. [custom2] The larger creatures try to cut your path, but, being on the ground, they can’t keep up with your legs. Without stopping, you grab the rawhide, then carry on, waiting for a few heartbeats before you change direction rapidly, now getting closer to {color=#f6d6bd}[horsename]{/color}...
                \n\nThe largest beast leaps from behind a tree and lands right next to you. Its hit flings you back. Your mount snorts and walks away, ready to flee. Once you hit the ground, still holding the thin material in your fingers, you scrape against the beaten ground, [custom1]. Your side hurts, but you get back on your feet, and chase after your horse.
                '
                'I run as fast as I can.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run as fast as I can.')
                    jump northernroadleaving01withrawhide
        else: # full success
            if northernroad_monkeys_earplugs:
                $ custom2 = "You get dizzy, but not much more than that - your movements are swift and confident as you ignore the muffled sounds.\n\n"
            else:
                $ custom2 = "You get dizzy, and soon the pain enters your skull, as if you’re getting hit by a smith’s hammer, time and time again. Yet you manage to stay calm, focused on your goal.\n\n"
            $ renpy.notify("You picked up the old rawhide.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up the old rawhide.{/i}')
            menu:
                'You stretch out your legs, then dash ahead. At first, the monkeys move away with a few unconvinced yells, but then those from above start to howl, even deeper than before, and you feel as if your guts are starting to move, hitting against each other. [custom2] The larger creatures try to cut your path, but, being on the ground, they can’t keep up with your legs. Without stopping, you grab the rawhide, then carry on, waiting for a few heartbeats before you change direction rapidly, now getting closer to {color=#f6d6bd}[horsename]{/color}. By the time you reach the saddle, the beasts have already abandoned their pursuit.
                \n\nYou take a few deep breaths, then inspect the rawhide. The wet, torn blanket is now worth as much as a bread crust.
                \n\nStill, it’s not rotten - if the owner is around, they may recognize it.
                '
                'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                    jump northernroadusingearplugs01
                'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                    pass
                '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                    jump northernroadfightinghowlers01
                'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                    pass
                'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                    pass
                'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                    jump northernroadrawhidetryingtotake00
                '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                    jump northernroadrawhidetryingtotake01
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                    pass
                '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                    jump northernroadrawhidetryingtotake02
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                    pass
                ##################################################
                'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                    jump northernroadrawhidetryingtofindthetraces01
                'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                    pass
                'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                    pass
                'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                    $ travel_destination = "howlerslair"
                    jump finaldestination
                'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                    pass
                ##################################################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                    jump northernroad_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                    jump northernroad_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                    jump northernroad_fishtrap03
                'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                    jump northernroad_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                    pass

    label northernroadrawhidetryingtofindthetraces01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the area, looking for any traces of the owner of the rawhide.')
        $ northernroad_trail = 1
        $ howlerslair_unlocked = 1
        $ quarters += 2
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'After half an hour you find no corpse, but the trail of the fight tells you enough. A human was dining near the tree. A large cat jumped them and dragged them through the meadow, north. For a few minutes, you follow the broken blades of tall grasses, losing track more than once, deceived by the paths used by howlers - which are now following your march anxiously.
            \n\nYou reach a gully, then to a thick forest growing in a cauldron-shaped basin. The branchy trees are taller than three houses placed on one another. The beast dragged the human through the thicket, and the scratched skin left blood on the edges of the twigs. You consider walking in, but as you look around, the howlers are getting more numerous and confident, sitting on every tree in sight, threatening you with their shouts.
            \n\nThe path is too overgrown for {color=#f6d6bd}[horsename]{/color} to follow you.
            '
            'To enter the woods, I’ll need to leave it at {color=#f6d6bd}Foggy’s{/color}. For now, I step back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- To enter the woods, I’ll need to leave it at {color=#f6d6bd}Foggy’s{/color}. For now, I step back.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You approach your bundles.
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass
            'It’s rather clear that the huntress can’t be helped anymore.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s rather clear that the huntress can’t be helped anymore.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'You approach your bundles.
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass

label northernroadregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        '[northernroad_fluff]
        \n\n[northernroad_monkeys_fluff][northernroad_monkeys_earplugs_fluff]
        '
        'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
            jump northernroadusingearplugs01
        'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
            pass
        '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
            jump northernroadfightinghowlers01
        'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
            pass
        'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
            pass
        'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
            jump northernroadrawhidetryingtotake00
        '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
            jump northernroadrawhidetryingtotake01
        'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
            pass
        '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
            jump northernroadrawhidetryingtotake02
        'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
            pass
        ##################################################
        'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
            jump northernroadrawhidetryingtofindthetraces01
        'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
            pass
        'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
            pass
        'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
            $ travel_destination = "howlerslair"
            jump finaldestination
        'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
            pass
        ##################################################
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
            jump northernroad_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
            jump northernroad_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
            jump northernroad_fishtrap03
        'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
            jump northernroad_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
            pass

label northernroadafterinteraction01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You return to grazing {color=#f6d6bd}[horsename]{/color}.
        '
        'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
            jump northernroadusingearplugs01
        'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
            pass
        '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
            jump northernroadfightinghowlers01
        'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
            pass
        'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
            pass
        'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
            jump northernroadrawhidetryingtotake00
        '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
            jump northernroadrawhidetryingtotake01
        'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
            pass
        '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
            jump northernroadrawhidetryingtotake02
        'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
            pass
        ##################################################
        'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
            jump northernroadrawhidetryingtofindthetraces01
        'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
            pass
        'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
            pass
        'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
            $ travel_destination = "howlerslair"
            jump finaldestination
        'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
            pass
        ##################################################
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
            jump northernroad_fishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
            jump northernroad_fishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
            jump northernroad_fishtrap03
        'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
            jump northernroad_fishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
            pass

label northernroadleaving01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You get into the saddle, followed by the angry shouts. {color=#f6d6bd}[horsename]{/color} is more than ready to flee - its ears are held back, nostrils wrinkled. You wonder if it suffers from the howls.
        '
        'We ride forward. (disabled)' if pc_likeshorsename:
            pass
        'I ride forward. (disabled)' if not pc_likeshorsename:
            pass

label northernroadleaving01withrawhide:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'By the time you reach the saddle, the beasts have already abandoned their pursuit, though they still shout angrily. {color=#f6d6bd}[horsename]{/color} is more than ready to flee - its ears are held back, nostrils wrinkled. You wonder if it suffers from the howls.
        \n\nYou ride away and take a few deep breaths, then inspect the rawhide. The wet, torn blanket is worth as much as a bread crust.
        \n\nStill, it’s not rotten - if the owner is around, they may recognize it.
        '
        'We ride forward. (disabled)' if pc_likeshorsename:
            pass
        'I ride forward. (disabled)' if not pc_likeshorsename:
            pass

label northernroad_fishtrapALL:
    label northernroad_fishtrap01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend some time setting up a fish trap at the bank.')
        show fishtrap northernroad01 at basicfade
        $ quarters += 2
        $ item_fishtrap -= 1
        $ northernroad_fishtrap = 1
        $ northernroad_fishtrap_daychecked = day
        $ northernroad_fishtrap_working = day
        $ northernroad_fishtrap_fishtimer = renpy.random.randint(1, 5)
        $ northernroad_fishtrap_fishtimer = (northernroad_fishtrap_fishtimer+day)
        menu:
            'You place the basket on the ground, then grab a bowl and start digging, looking for a few larger worms. You bait the stick and push it inside the basket, locking it between the sides, then cover the entrance with the lid - tying it together takes you a few good moments, but will be easier later on. You attach the entire trap to a rock and push it into the lake, far enough that it sinks entirely.
            \n\nWho knows how long it will take before something large enough swims inside. Still, it would be better to not wait for too long - otherwise, the prey may die of hunger.
            '
            'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                jump northernroadusingearplugs01
            'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                pass
            '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                jump northernroadfightinghowlers01
            'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                pass
            'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                pass
            'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                jump northernroadrawhidetryingtotake00
            '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                jump northernroadrawhidetryingtotake01
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                pass
            '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                jump northernroadrawhidetryingtotake02
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                pass
            ##################################################
            'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                jump northernroadrawhidetryingtofindthetraces01
            'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                pass
            'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                pass
            'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                $ travel_destination = "howlerslair"
                jump finaldestination
            'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                pass
            ##################################################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                jump northernroad_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                jump northernroad_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                jump northernroad_fishtrap03
            'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                jump northernroad_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                pass

    label northernroad_fishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the fish trap had any luck.')
        if northernroad_fishtrap_fishtimer > day:
            $ northernroad_fishtrap_daychecked = day
            $ minutes += 5
            menu:
                'Unfortunately, it’s still empty.
                '
                'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                    jump northernroadusingearplugs01
                'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                    pass
                '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                    jump northernroadfightinghowlers01
                'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                    pass
                'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                    pass
                'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                    jump northernroadrawhidetryingtotake00
                '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                    jump northernroadrawhidetryingtotake01
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                    pass
                '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                    jump northernroadrawhidetryingtotake02
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                    pass
                ##################################################
                'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                    jump northernroadrawhidetryingtofindthetraces01
                'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                    pass
                'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                    pass
                'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                    $ travel_destination = "howlerslair"
                    jump finaldestination
                'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                    pass
                ##################################################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                    jump northernroad_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                    jump northernroad_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                    jump northernroad_fishtrap03
                'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                    jump northernroad_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                    pass
        elif northernroad_fishtrap_fishtimer+3 > day:
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            $ d100roll += northernroad_fishtrap_badthingmodifier
            $ minutes += 5
            if d100roll > 110: # harsh fail
                $ northernroad_fishtrap_badthingmodifier = 0
                $ northernroad_fishtrap_working = 0
                # $ northernroad_fishtrap = 0
                $ northernroad_fishtrap_fishtimer = 0
                $ northernroad_fishtrap_daychecked = 0
                menu:
                    'Sadly, it’s not only empty, the bait is already gone. Whatever had squeezed into the trap was small enough to catch the worms and swim outside.
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass
            elif d100roll > 90: # soft fail
                $ northernroad_fishtrap_fishtimer = 0
                $ northernroad_fishtrap_working = 0
                menu:
                    'Sadly, it’s not only empty, the bait is already gone. Whatever had squeezed into the trap was small enough to catch the worms and swim outside.
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass
            else: # success
                $ northernroad_fishtrap_fishtimer = 0
                $ quarters += 1
                if northernroad_fishtrap_badthingmodifier:
                    $ northernroad_fishtrap_badthingmodifier += 10
                $ northernroad_fishtrap_working = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if d100roll > 50:
                    $ item_rawfishtotalnumber += 1
                    $ achievement_fish += 1
                    $ item_rawfish_gaining = 1
                    $ renpy.notify("You caught a fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught a fish.{/i}')
                    $ custom1 = "You pull the rope and see a flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animal with two careful blows to the top of its head, then finish it off with a knife, cutting it underneath the gill plate. You spend another minute or two bleeding out the fish in the lake, then cover it with a waxed linen sheet.\n\nYou should eat it soon, before it spoils."
                elif d100roll > 20:
                    $ item_rawfishtotalnumber += 2
                    $ achievement_fish += 2
                    $ item_rawfish_gaining = 2
                    $ renpy.notify("You caught 2 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 2 fish.{/i}')
                    $ custom1 = "You pull the rope and see two flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows to the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the lake, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                else:
                    $ item_rawfishtotalnumber += 3
                    $ achievement_fish += 3
                    $ item_rawfish_gaining = 3
                    $ renpy.notify("You caught 3 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 3 fish.{/i}')
                    $ custom1 = "You pull the rope and see three flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows to the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the lake, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                menu:
                    '[custom1]
                    '
                    'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                        jump northernroadusingearplugs01
                    'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                        pass
                    '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                        jump northernroadfightinghowlers01
                    'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                        pass
                    'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                        pass
                    'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                        jump northernroadrawhidetryingtotake00
                    '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                        jump northernroadrawhidetryingtotake01
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                        pass
                    '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                        jump northernroadrawhidetryingtotake02
                    'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                        pass
                    ##################################################
                    'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                        jump northernroadrawhidetryingtofindthetraces01
                    'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                        pass
                    'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                        pass
                    'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                        $ travel_destination = "howlerslair"
                        jump finaldestination
                    'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                        pass
                    ##################################################
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                        jump northernroad_fishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                        jump northernroad_fishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                        jump northernroad_fishtrap03
                    'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                        jump northernroad_fishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                        pass
        else:
            $ northernroad_fishtrap_working = 0
            $ northernroad_fishtrap_fishtimer = 0
            $ minutes += 5
            menu:
                'Sadly, you’re too late. Your catch has already starved to death and is now being eaten by dozens of little creatures. You open the lid and pour its contents out into the lake.
                '
                'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                    jump northernroadusingearplugs01
                'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                    pass
                '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                    jump northernroadfightinghowlers01
                'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                    pass
                'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                    pass
                'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                    jump northernroadrawhidetryingtotake00
                '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                    jump northernroadrawhidetryingtotake01
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                    pass
                '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                    jump northernroadrawhidetryingtotake02
                'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                    pass
                ##################################################
                'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                    jump northernroadrawhidetryingtofindthetraces01
                'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                    pass
                'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                    pass
                'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                    $ travel_destination = "howlerslair"
                    jump finaldestination
                'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                    pass
                ##################################################
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                    jump northernroad_fishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                    jump northernroad_fishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                    jump northernroad_fishtrap03
                'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                    jump northernroad_fishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                    pass

    label northernroad_fishtrap03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I set the fish trap again.')
        $ northernroad_fishtrap_working = day
        $ minutes += 5
        $ northernroad_fishtrap = 1
        show fishtrap northernroad01 at basicfade
        $ northernroad_fishtrap_daychecked = day
        $ northernroad_fishtrap_fishtimer = renpy.random.randint(1, 4)
        $ northernroad_fishtrap_fishtimer = (northernroad_fishtrap_fishtimer+day)
        menu:
            'You need to look for worms again, but at least sealing the lid takes only a moment.
            '
            'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                jump northernroadusingearplugs01
            'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                pass
            '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                jump northernroadfightinghowlers01
            'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                pass
            'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                pass
            'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                jump northernroadrawhidetryingtotake00
            '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                jump northernroadrawhidetryingtotake01
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                pass
            '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                jump northernroadrawhidetryingtotake02
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                pass
            ##################################################
            'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                jump northernroadrawhidetryingtofindthetraces01
            'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                pass
            'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                pass
            'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                $ travel_destination = "howlerslair"
                jump finaldestination
            'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                pass
            ##################################################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                jump northernroad_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                jump northernroad_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                jump northernroad_fishtrap03
            'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                jump northernroad_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                pass

    label northernroad_fishtrap04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the trap back')
        $ minutes += 5
        $ item_fishtrap += 1
        $ renpy.notify("You dismantled the trap.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You dismantled the trap.{/i}')
        $ northernroad_fishtrap = 0
        hide fishtrap
        $ northernroad_fishtrap_daychecked = 0
        $ northernroad_fishtrap_working = 0
        $ northernroad_fishtrap_fishtimer = 0
        menu:
            'You shake the basket, expecting it will get drier during your ride, then attach it to your saddle.
            '
            'Just in case, I plug my ears.' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and item_earplugs" ):
                jump northernroadusingearplugs01
            'Too bad I have nothing to plug my ears with. (disabled)' ( condition="northernroad_monkeys and northernroad_monkeys != 3 and not northernroad_monkeys_earplugs and not item_earplugs" ):
                pass
            '{image=d6} I try to scare the howlers away.' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp:
                jump northernroadfightinghowlers01
            'I’m too exhausted to face the howlers right now. (Required vitality: 1) (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday != day and pc_hp <= 0:
                pass
            'The howlers are already furious. I won’t be able to scare them away today. (disabled)' if northernroad_monkeys and northernroad_monkeys != 3 and northernroad_monkeys_scaredday == day:
                pass
            'Since there are no monkeys around, I approach the rawhide.' if (not northernroad_monkeys and not northernroad_rawhide_taken) or (northernroad_monkeys == 3 and not northernroad_rawhide_taken):
                jump northernroadrawhidetryingtotake00
            '{image=d6} The monkeys may try to attack me, so I grab the rawhide quickly and flee.' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp >= 1:
                jump northernroadrawhidetryingtotake01
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 1) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 1 and pc_hp <= 0:
                pass
            '{image=d6} These monkeys hate me. I try to grab the rawhide, hoping my armor will defend me.' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp >= 2:
                jump northernroadrawhidetryingtotake02
            'I can’t get to the rawhide fast enough to outrun the monkeys. (Required vitality: 2) (disabled)' if not northernroad_rawhide_taken and northernroad_monkeys == 2 and pc_hp <= 1:
                pass
            ##################################################
            'I search the area, looking for any traces of the owner of the rawhide.' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters <= (world_daylength-8))" ):
                jump northernroadrawhidetryingtofindthetraces01
            'It’s too dark to look for the trail of the owner of the rawhide. (disabled)' ( condition="(northernroad_rawhide_taken and not northernroad_monkeys and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8)) or (northernroad_rawhide_taken and northernroad_monkeys == 3 and northernroad_rawhide_owner and not northernroad_trail and quarters > (world_daylength-8))" ):
                pass
            'I can’t look for the owner of the rawhide while the monkeys are around. (disabled)' if northernroad_rawhide_taken and northernroad_monkeys and northernroad_monkeys != 3 and northernroad_rawhide_owner and not northernroad_trail:
                pass
            'I leave {color=#f6d6bd}[horsename]{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave {color=#f6d6bd}%s{/color} at {color=#f6d6bd}Foggy’s{/color} and enter the lair of howlers.' %horsename)
                $ travel_destination = "howlerslair"
                jump finaldestination
            'It’s too late to enter the lair of howlers. (disabled)' if howlerslair_unlocked and not howlerslair_firsttime and (quarters+tohowlerslair) > (world_daylength-4):
                pass
            ##################################################
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not northernroad_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not northernroad_fishtrap and quarters <= (world_daylength-8)" ):
                jump northernroad_fishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not northernroad_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked != day:
                jump northernroad_fishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if northernroad_fishtrap and northernroad_fishtrap_working and northernroad_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if northernroad_fishtrap and not northernroad_fishtrap_working:
                jump northernroad_fishtrap03
            'I take the fish trap back.' if northernroad_fishtrap and not northernroad_fishtrap_working and not item_fishtrap:
                jump northernroad_fishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if northernroad_fishtrap and not northernroad_fishtrap_working and item_fishtrap:
                pass
