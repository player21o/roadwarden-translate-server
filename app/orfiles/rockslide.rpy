###################### Rockslide
default rockslide_firsttime = 0
default rockslide_cleared = 0

default rockslide_firstblockade_seen = 0
default rockslide_firstblockade_cleared = 0
default rockslide_firstblockade_clearing_modifer = 0

default rockslide_workers = 0
default rockslide_workers_druids = 0
default rockslide_workers_hardass_points = 0
default rockslide_workers_kindness_points = 0
default rockslide_workers_digging = 0
default rockslide_workers_pcfightsalone = 0

label rockslide_firstblockadeALL:
    label rockslide_firstblockade00:
        $ quarters -= 1
        $ pc_area = "rockslide_firstblockade"
        $ torockslide = 1
        $ tofishinghamlet += 1
        $ tosoutherncrossroads -= 1
        $ tomilitarycamp -= 1
        $ towesterncrossroads -= 1
        $ towestgate -= 1
        $ tooldpagos -= 1
        $ tomonastery -= 1
        $ towatchtower -= 1
        $ toeudociahouse -= 1
        $ tostonesign -= 1
        $ tofoggylake -= 1
        $ tofoggylake -= 1
        $ tofoggylake -= 1
        $ tocreeks -= 1
        $ tooldtunnel -= 1
        $ togalerocks -= 1
        $ tobeach -= 1
        $ topeltnorth -= 1
        $ toruinedvillage -= 1
        $ tobeholder -= 1
        $ todruidcave -= 1
        $ tohowlersdell -= 1
        $ todolmen -= 1
        $ tofallentree -= 1
        $ tostonebridge -= 1
        $ toghoulcave -= 1
        $ togiantstatue -= 1
        $ tomountainroad -= 1
        $ togreenmountaintribe -= 1
        $ tohuntercabin -= 1
        $ toforagingground -= 1
        $ towanderer -= 1
        $ toford -= 1
        $ tobogentrance -= 1
        $ tobogcrossroads -= 1
        $ tobogroad -= 1
        $ topeatfield -= 1
        $ tovines -= 1
        $ towhitemarshes -= 1
        $ toruinedshelter -= 1
        $ tonorthernroad -= 1
        $ tohowlerslair -= 1
        $ rockslide_firstblockade_clearing_modifer = 0
        if day >= 30:
            $ rockslide_firstblockade_clearing_modifer = 6
            $ custom1 = "I should be done in more than three hours."
        elif day >= 25:
            $ rockslide_firstblockade_clearing_modifer = 5
            $ custom1 = "I should be done in three hours or so."
        elif day >= 20:
            $ rockslide_firstblockade_clearing_modifer = 4
            $ custom1 = "I should be done in three hours or so."
        elif day >= 15:
            $ rockslide_firstblockade_clearing_modifer = 3
            $ custom1 = "I should be done in more than two hours."
        elif day >= 10:
            $ rockslide_firstblockade_clearing_modifer = 2
            $ custom1 = "I should be done in more than two hours."
        elif day >= 5:
            $ rockslide_firstblockade_clearing_modifer = 1
            $ custom1 = "I should be done in two hours or so."
        else:
            $ custom1 = "I should be done in two hours or so."
        stop music fadeout 4.0
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/rockslide01.ogg":
            play nature "audio/ambient/rockslide01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        if not rockslide_firstblockade_seen:
            $ rockslide_firstblockade_seen = 1
            show areapicture rockslide00 at basicfade
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The path gets greener, and meanders between treacherous precipices. You ride slowly, passing by birds and ibexes, but in the distance you spot circling harpies, and below you - a roaming mountain cat pursuing a mouflon. You take a sip from your waterskin - the air here is a bit dry.
                '
                'Let’s hope that the echo of hooves won’t reach any larger beasts.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope that the echo of hooves won’t reach any larger beasts.')
                    show areapicture rockslide00a at basicfade
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'The path leads you down again, to a small, moist valley, impenetrable for a rider. The thicket is made of thorny shrubs, tall grasses, and the weak, fallen boughs that nourish mosses and mushrooms.
                        \n\nYou examine the remnants of the path covered with greenish puddles. Without the roots and with a fresh layer of pebbles, it may still be restored.
                        \n\nYou look behind you - the road is clear, no ambushes so far. But if you hope to clear this place, it’d be better to do so soon - it’ll only get denser with the passage of days.
                        '
                        'The withering dust is going to help me here.' if item_witheringdust:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust is going to help me here.')
                            $ custom1 = "You put on your thick, leather gloves, then spread the dust beneath the plants. The already moist surroundings need little help - the yellow smoke appears immediately, so you step away and cover your mouth and nose.\n\nThe sizzling bushes start to shake, losing their twigs and leaves. Soon, you throw the plant into the stream, then end the job with your axe, then repeat, again and again. Pushing the boughs away takes a bit more effort, but you need only enough space to let your palfrey get through."
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            $ quarters += 1
                            jump rockslide_firstblockade_clearing
                        '[custom1]' ( condition="pc_hp >= 1 and quarters < world_daylength-12-rockslide_firstblockade_clearing_modifer" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- %s' %custom1)
                            $ custom1 = "Your muscles, not used to such tiring work, grow tired quickly, so you take a few short breaks, avoiding the thorns and dirty water. When it comes to pushing aside the boughs, you breathe heavily, but you need only enough space to let your palfrey get through."
                            $ quarters += 8+rockslide_firstblockade_clearing_modifer
                            $ cleanliness = limit_cleanliness(cleanliness-2)
                            show minus2appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment point.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            jump rockslide_firstblockade_clearing
                        'I’m not afraid of getting tired. I’ll get this done in half the time.' ( condition="pc_hp >= 2 and quarters <= (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2))" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not afraid of getting tired. I’ll get this done in half the time.')
                            $ custom1 = "Your muscles, not used to such tiring work, grow tired quickly, but you don’t let yourself take a break. Soon, you push yourself even more, more from annoyance than anything, and only after you’re done you notice the torn parts on your pants and sleeves. When it comes to pushing aside the boughs, you breathe heavily, but you need only enough space to let your palfrey get through."
                            $ quarters += ((8+rockslide_firstblockade_clearing_modifer)/2)
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment point.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                $ cleanliness = limit_cleanliness(cleanliness-4)
                                show minus4appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
                            else:
                                $ armor = limit_armor(armor-1)
                                show minus1armor at armorchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                $ cleanliness = limit_cleanliness(cleanliness-3)
                                show minus3appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
                            jump rockslide_firstblockade_clearing
                        'I’m too exhausted for manual labor. (disabled)' ( condition="pc_hp == 0" ):
                            pass
                        'I’m so tired I’d have to work slowly. (disabled)' ( condition="pc_hp == 1" ):
                            pass
                        'If I want to get this done today, I need to work hard. (disabled)' ( condition="(quarters >= (world_daylength-12-rockslide_firstblockade_clearing_modifer)) and not (quarters > (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2)))" ):
                            pass
                        'It’s too late to get this done. (disabled)' ( condition="quarters > (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2))" ):
                            pass
                        'I don’t own any potion that could help me here. (disabled)' if not item_witheringdust:
                            pass
        else:
            show areapicture rockslide00a at basicfade
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The plants get denser with every day.
                '
                'The withering dust is going to help me here.' if item_witheringdust:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust is going to help me here.')
                    $ custom1 = "You put on your thick, leather gloves, then spread the dust beneath the plants. The already moist surroundings need little help - the yellow smoke appears immediately, so you step away and cover your mouth and nose.\n\nThe sizzling bushes start to shake, losing their twigs and leaves. Soon, you throw the plant into the stream, then end the job with your axe, then repeat, again and again. Pushing the boughs away takes a bit more effort, but you need only enough space to let your palfrey get through."
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ quarters += 1
                    jump rockslide_firstblockade_clearing
                '[custom1]' ( condition="pc_hp >= 1 and quarters < world_daylength-12-rockslide_firstblockade_clearing_modifer" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- %s' %custom1)
                    $ custom1 = "Your muscles, not used to such tiring work, grow tired quickly, so you take a few short breaks, avoiding the thorns and dirty water. When it comes to pushing aside the boughs, you breathe heavily, but you need only enough space to let your palfrey get through."
                    $ quarters += 8+rockslide_firstblockade_clearing_modifer
                    $ cleanliness = limit_cleanliness(cleanliness-2)
                    show minus2appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                    if pc_food:
                        $ pc_food = limit_pc_food(pc_food-2)
                        show minus2food at foodchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment point.{/i}')
                    elif pc_hp > 0:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    jump rockslide_firstblockade_clearing
                'I’m not afraid of getting tired. I’ll get this done in half the time.' ( condition="pc_hp >= 2 and quarters <= (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2))" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not afraid of getting tired. I’ll get this done in half the time.')
                    $ custom1 = "Your muscles, not used to such tiring work, grow tired quickly, but you don’t let yourself take a break. Soon, you push yourself even more, more from annoyance than anything, and only after you’re done you notice the torn parts on your pants and sleeves. When it comes to pushing aside the boughs, you breathe heavily, but you need only enough space to let your palfrey get through."
                    $ quarters += ((8+rockslide_firstblockade_clearing_modifer)/2)
                    if pc_food:
                        $ pc_food = limit_pc_food(pc_food-2)
                        show minus2food at foodchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment point.{/i}')
                    elif pc_hp > 0:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        $ cleanliness = limit_cleanliness(cleanliness-4)
                        show minus4appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
                    else:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ cleanliness = limit_cleanliness(cleanliness-3)
                        show minus3appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
                    jump rockslide_firstblockade_clearing
                'I’m too exhausted for manual labor. (disabled)' ( condition="pc_hp == 0" ):
                    pass
                'I’m so tired I’d have to work slowly. (disabled)' ( condition="pc_hp == 1" ):
                    pass
                'If I want to get this done today, I need to work hard. (disabled)' ( condition="(quarters >= (world_daylength-12-rockslide_firstblockade_clearing_modifer)) and not (quarters > (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2)))" ):
                    pass
                'It’s too late to get this done. (disabled)' ( condition="quarters > (world_daylength-8-(rockslide_firstblockade_clearing_modifer/2))" ):
                    pass
                'I don’t own any potion that could help me here. (disabled)' if not item_witheringdust:
                    pass

    label rockslide_firstblockade_clearing:
        $ rockslide_firstblockade_cleared = 1
        show areapicture rockslide00b at basicfade
        menu:
            '[custom1]
            '
            'Maybe the animals will start to roam this place again, beating the path.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the animals will start to roam this place again, beating the path.')
                $ quarters += 1
                $ torockslide = 0
                $ tofishinghamlet -= 1
                $ tosoutherncrossroads += 1
                $ tomilitarycamp += 1
                $ towesterncrossroads += 1
                $ towestgate += 1
                $ tooldpagos += 1
                $ tomonastery += 1
                $ towatchtower += 1
                $ toeudociahouse += 1
                $ tostonesign += 1
                $ tofoggylake += 1
                $ tofoggylake += 1
                $ tofoggylake += 1
                $ tocreeks += 1
                $ tooldtunnel += 1
                $ togalerocks += 1
                $ tobeach += 1
                $ topeltnorth += 1
                $ toruinedvillage += 1
                $ tobeholder += 1
                $ todruidcave += 1
                $ tohowlersdell += 1
                $ todolmen += 1
                $ tofallentree += 1
                $ tostonebridge += 1
                $ toghoulcave += 1
                $ togiantstatue += 1
                $ tomountainroad += 1
                $ togreenmountaintribe += 1
                $ tohuntercabin += 1
                $ toforagingground += 1
                $ towanderer += 1
                $ toford += 1
                $ tobogentrance += 1
                $ tobogcrossroads += 1
                $ tobogroad += 1
                $ topeatfield += 1
                $ tovines += 1
                $ towhitemarshes += 1
                $ toruinedshelter += 1
                $ tonorthernroad += 1
                $ tohowlerslair += 1
                jump rockslide01

label rockslide01:
    nvl clear
    $ pc_area = "rockslide"
    $ rockslidefluff = ""
    $ rockslidefluff = renpy.random.choice(['A brown critter gets startled by the sound of hooves and climbs up the crag.', 'The sky is cloudless. You see a large harpy trying to fall upon a resting seagull.','You’re startled by the sight of animal scales, but you realize it’s just a basking grass-snake. Soon, it vanishes among the rocks.', 'The shrubs above you try to withstand the cold, refresh wind.'])
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not rockslide_firstblockade_cleared:
        jump rockslide_firstblockade00
    if not rockslide_firsttime:
        $ world_known_npcs += 0
        $ world_known_areas += 1
        $ rockslide_firsttime = 1
        $ howlersdell_unlocked = 1
        $ world_known_areas += 1
        stop music fadeout 4.0
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/rockslide01.ogg":
            play nature "audio/ambient/rockslide01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        if not rockslide_cleared:
            show areapicture rockslide01 at basicfade
        else:
            show areapicture rockslide03 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump rockslidefirsttime01
    elif rockslide_workers == 1:
        $ rockslide_workers = 2
        jump travelingtorockslidewithworkers
    elif rockslide_workers == 2:
        $ rockslide_workers = 0
        if not rockslide_cleared:
            show areapicture rockslide01 at basicfade
        else:
            show areapicture rockslide03 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump rockslidewithworkers01
    else:
        stop music fadeout 4.0
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/rockslide01.ogg":
            play nature "audio/ambient/rockslide01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        if not rockslide_cleared:
            show areapicture rockslide01 at basicfade
        else:
            show areapicture rockslide03 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump rockslideregular01

label rockslidefirsttimeALL:
    label rockslidefirsttime01:
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'You reach a convenient mountain pass, with crags smoothed out by centuries of rain and wind. The sun warms up both the vegetation and the beaten road, and the only beasts you spot are loud rooks, glancing at you from the rocks and branches.
            \n\nClearing the rockslide would take hours of work and a large group of people, while forcing {color=#f6d6bd}[horsename]{/color} to climb up and down could break its legs.
            '
            'I dismount and look around.' if not quest_fisherhamlet_description01 and quest_fisherhamlet != 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and look around.')
                jump rockslidefirsttime02
            'I should dismount and look around so I can report back to {color=#f6d6bd}Thais{/color}.' if not quest_fisherhamlet_description01 and quest_fisherhamlet == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should dismount and look around so I can report back to {color=#f6d6bd}Thais{/color}.')
                jump rockslidefirsttime02
            'All I can do now is turn back. (disabled)':
                pass

        label rockslidefirsttime02:
            $ quarters += 1
            $ quest_fisherhamlet_description01 = "It looks like something might have been buried beneath the rocks. I should report this to Thais."
            if quest_fisherhamlet == 1:
                $ renpy.notify("Journal updated: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
            menu:
                'You climb up the rocks, having plenty of spots to rest your hands. Most of them won’t move even an inch.
                \n\nAs you get closer to the small, dead tree, you notice something odd among the stones. Pieces of old fabric, completely covered with mold - most likely the remains of a tunic.
                '
                'All I can do now is turn back. (disabled)' if quest_fisherhamlet != 1:
                    pass
                'I should get back to Howler’s. (disabled)' if quest_fisherhamlet == 1:
                    pass

label rockslideregular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'The rock slide has made the path impassable. [rockslidefluff]
        '
        'I dismount and look around.' if not quest_fisherhamlet_description01 and quest_fisherhamlet != 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and look around.')
            jump rockslidefirsttime02
        'I should dismount and look around so I can report back to {color=#f6d6bd}Thais{/color}.' if not quest_fisherhamlet_description01 and quest_fisherhamlet == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should dismount and look around so I can report back to {color=#f6d6bd}Thais{/color}.')
            jump rockslidefirsttime02
        'All I can do now is turn back. (disabled)':
            pass

label travelingtorockslidewithworkersALL:
    label travelingtorockslidewithworkers:
        nvl clear
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture howlersdelltorockslide at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ quarters -= 2
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'The workers carry clubs, spears, and a simple wheelbarrow, filled with food rations, waterskins, and tools. While one spade and one pickaxe were made of precious iron, other ones were made either from wooden planks, in case of the former, or deer antlers.
            \n\nStill being in the forest, your companions share memories about their time spent among the familiar trees. Some were helping the hunters carry a large saurian back to the village, others escorted the druids on their search for rare herbs.
            \n\nBut as you get closer to the hills, your companions lower their voices. One of the guards tells stories about the local goblin packs, without hiding any gory details. Her playful tone makes others carefully look around.
            '
            'Keeping the diggers on their toes could be a good thing. “Look out for the harpies, also.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Keeping the diggers on their toes could be a good thing. “Look out for the harpies, also.”')
                $ rockslide_workers_hardass_points += 1
                menu:
                    'The guard finishes one more of her tales, looking with a smirk at the workers. “That’s right,” you chip in, “and that’s why we need to keep our eyes open. Threats may hide in rocks, in clouds, and beneath our feet. I’ll ride last, so I’ve got our backs. Now lower your voices, let’s not cause any more landslides.”
                    \n\nThe others nod and after you regroup.
                    '
                    'We travel in silence.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We travel in silence.')
                        hide areapicture
                        jump rockslide01
            'I’d rather help them relax. I change the topic to something lighter.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather help them relax. I change the topic to something lighter.')
                $ rockslide_workers_kindness_points += 1
                menu:
                    'You interrupt her and describe what you saw last time you traveled through the hills. You mention some thoughts on getting rid of the larger rocks, and the workers are eager to join you, correcting your observations by sharing their own experiences. For some time, you talk about the weak tree growing above the path - it could be safer to get rid of it right away.
                    \n\nThe air warms up and your companions once again start to comment curiously on what you pass on your way.
                    '
                    'We move forward.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We move forward.')
                        hide areapicture
                        jump rockslide01

label rockslidewithworkersALL:
    label rockslidewithworkers01:
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/rockslide01.ogg":
            play nature "audio/ambient/rockslide01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        $ renpy.force_autosave(take_screenshot=False, block=True)
        $ quarters += 2
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'The diggers put on their leather gloves and grab the tools. They don’t need you to provide further directions - one of the older men, whose arms are covered with healed claw marks, assigns tasks and roles. The guards take place on both sides of the rockslide, as well as above it.
            \n\nFinally, as the first sound of the pickaxe cuts through the sky, {color=#f6d6bd}the overseer{/color} turns toward you. He stands silent for a moment, looking uncomfortable with the idea of ordering you around.
            '
            'My job is to keep them safe, nothing else. I’m going to join the guards.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My job is to keep them safe, nothing else. I’m going to join the guards.')
                jump rockslidewithworkers01a
            'I know it will be tiring, but I’ll join the others in clearing the road. At least we’ll finish faster.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know it will be tiring, but I’ll join the others in clearing the road. At least we’ll finish faster.')
                jump rockslidewithworkers01b
            'Since I have The Tool of Destruction, I should be able to save them a lot of swinging.' if item_magicchisel == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since I have The Tool of Destruction, I should be able to save them a lot of swinging.')
                jump rockslidewithworkers01c

    label rockslidewithworkers01a:
        $ rockslide_workers_hardass_points += 2
        menu:
            'You lead {color=#f6d6bd}[horsename]{/color} to the nearest few clumps of grass, then begin your patrol. The hours pass with little excitement, so at least you have enough time to brush your palfrey.
            '
            'I try to ignore the sounds of the pickaxes and gather my thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to ignore the sounds of the pickaxes and gather my thoughts.')
                jump rockslidewithworkers02

    label rockslidewithworkers01b:
        $ rockslide_workers_kindness_points += 2
        $ rockslide_workers_digging = 1
        menu:
            'You take off your gambeson and prepare your own pair of gloves, telling the guards to take care of {color=#f6d6bd}[horsename]{/color}. {color=#f6d6bd}The overseer{/color} tells you to gather the loose rocks and put them in the wooden wheelbarrow.
            \n\nThe workers are not eager to engage in idle chat. They breathe heavily and speak only when necessary, coordinating their efforts.
            '
            'It’s going to be a rough couple of hours.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s going to be a rough couple of hours.')
                jump rockslidewithworkers02

    label rockslidewithworkers01c:
        $ rockslide_workers_kindness_points += 3
        $ rockslide_workers_digging = 2
        menu:
            'You take off your gambeson and prepare your own pair of gloves, telling the guards to take care of {color=#f6d6bd}[horsename]{/color}. You explain to {color=#f6d6bd}the overseer{/color} how your tool works, and he asks you enthusiastically to give you a short demonstration. You approach a large boulder, pick up a hammer that belongs to the workers, and place the chisel in a crack. You take a swing, and a chunk twice as large as your fist breaks into shards, sparking laughter and surprised questions. One of them asks you to do it again, while another offers to replace you.
            \n\n{color=#f6d6bd}The overseer{/color} restores order. He instructs a couple of other workers to follow you and gather the loose rocks from the ground, then put them in the wooden wheelbarrow. At first, the work sparks laughter and jokes, but the crew quickly gets used to the wondrous tool.
            '
            'We’ll save {i}a lot{/i} of time.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We’ll save {i}a lot{/i} of time.')
                jump rockslidewithworkers02

    label rockslidewithworkers02:
        nvl clear
        show areapicture rockslide02 at basicfade
        if rockslide_workers_digging == 2:
            $ quarters += 3
            $ custom1 = "Such work feels refreshing after all the days spent in the saddle. {color=#f6d6bd}The overseer{/color} was right to let you take care of one of the lighter tasks - your arms get tired quickly."
        if rockslide_workers_digging == 1:
            $ quarters += 6
            $ custom1 = "Such work feels refreshing after all the days spent in the saddle. {color=#f6d6bd}The overseer{/color} was right to let you take care of one of the lighter tasks - your arms get tired quickly."
        else:
            $ custom1 = "The workers are in decent moods, and as far as you can tell, the work goes well."
            $ quarters += 8
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if rockslide_workers_digging == 1:
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        elif rockslide_workers_digging == 2:
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        menu:
            'The hours pass. [custom1]
            \n\nIt’s time for a break. Everyone leaves their tools where they stand, then sit on the flat boulders. They take out their food rations and start to talk about their plans for the evening.
            '
            'I’d rather stay vigilant. I walk away and look out for beasts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather stay vigilant. I walk away and look out for beasts.')
                jump rockslidewithworkers02a
            'I sit down with them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could use some companionship. I sit down with them.')
                jump rockslidewithworkers02b

    label rockslidewithworkers02a:
        $ quarters += 2
        $ rockslide_workers_hardass_points += 2
        if pc_likeshorsename:
            $ custom1 = "nickers at you, happy to take a long rest in such peaceful surroundings. It bows its head and you scratch the bottom of its neck firmly"
        else:
            $ custom1 = "welcomes you with a short snort and returns to pawing the ground loudly, for reasons only it can understand"
        menu:
            'You stretch out your arms and back, then go for a short walk. An ibex with long, dark horns and thick brown fur climbs up the rock face, not far away from here. It’s leaning against the rocks that seem too small to carry it, yet remains confident and quick. For a moment, it gives you a silent look, not aware that, unlike most predators, humans know very well how to cause harm to distant targets. It jumps on tiny shelves and reaches the top of the wall, where it gracefully walks away.
            \n\nYou approach {color=#f6d6bd}[horsename]{/color}, which [custom1]. {color=#f6d6bd}The overseer{/color} clears his throat, stands up, and addresses you.
            \n\n“So far, nae corpse,” he rubs his scars with a grunt, “but there was a boot, aye. Maybe the leg walked away on its own. Better grab your axe, we’ll strike as soon as we see it, awoken or not. You ready?”
            '
            '“Just leave it to me and the guards.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just leave it to me and the guards.”')
                jump rockslidewithworkers03a
            '“Time to use those spears you brought. Tell your people to form a circle around two or three diggers.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time to use those spears you brought. Tell your people to form a circle around two or three diggers.”')
                jump rockslidewithworkers03b

    label rockslidewithworkers02b:
        $ quarters += 2
        $ rockslide_workers_kindness_points += 2
        menu:
            'You sit among the chatting workers. The four loudest ones are happy to remain in the center of attention. Their friendly banter is casual, but difficult for you to follow. They keep referencing names and places that mean nothing to you, and many of their jokes are related to more or less casual romances. The mischievous laughter of the other folks makes you think about {color=#f6d6bd}Hovlavan{/color} harbor workers, who eat similar pies made of dough, poultry, and onions.
            \n\nOnce the meal is finished, the conversation turns toward the remaining work, as well as the hopes they have for the fishing hamlet. {color=#f6d6bd}The overseer{/color} clears his throat, stands up, and addresses you.
            \n\n“So far, nae corpse,” he rubs his scars with a grunt, “but there was a boot, aye. Maybe the leg walked away on its own. Better grab your axe, we’ll strike as soon as we see it, awoken or not. You ready?”
            '
            '“Just leave it to me and the guards.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just leave it to me and the guards.”')
                jump rockslidewithworkers03a
            '“Time to use those spears you brought. Tell your people to form a circle around two or three diggers.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time to use those spears you brought. Tell your people to form a circle around two or three diggers.”')
                jump rockslidewithworkers03b

    label rockslidewithworkers03a:
        $ rockslide_workers_hardass_points += 2
        $ rockslide_workers_pcfightsalone = 1
        menu:
            '“You that confident, aye? Do ne get yourself killed, witchcraft is witchcraft.” His relieved voice betrays his words. “Right, now,” he gestures for everyone to stand up and gather around him. “Do ne move more than two rocks at once. Anyone hears anything, or sees a bone, stop whatever you’re doing en shout. We do ne need nae adventurers.”
            \n\nThe workers move slowly, breaking, pushing, and carrying away the rocks. The tension is palpable, but since all of them work at once, the progress is good enough.
            '
            'I stand nearby, ready to strike.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand nearby, ready to strike.')
                $ quarters += 2
                jump rockslidewithworkers04

    label rockslidewithworkers03b:
        $ rockslide_workers_kindness_points += 2
        menu:
            'He nods. “Aye, let’s stay patient, we have all the numbers we need. Right, now,” he gestures for everyone to stand up and gather around him, then points at five people, calling them by their names. “You stay on guard. The rest, you dig. Don’t move more than one rock at once. Anyone hears anything, or sees a bone, stop whatever you’re doing en shout. We do ne need nae adventurers.”
            \n\nHalf of the workers grab the spears and form a semicircle around the diggers. The others move slowly, breaking, pushing, and carrying away the rocks. The tension is palpable and there are not enough hands to get through the rubble quickly.
            '
            'I stay close, ready to strike.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay close, ready to strike.')
                if rockslide_workers_digging == 2:
                    $ quarters += 3
                else:
                    $ quarters += 4
                jump rockslidewithworkers04

    label rockslidewithworkers04:
        if rockslide_workers_pcfightsalone:
            $ custom1 = "There’s no soul between you and {i}it{/i}, though the guards are close and you catch the glimpse of a moving spearhead."
        else:
            $ custom1 = "There’s no soul between you and {i}it{/i} and the panicked workers stupefy you with their screams."
        menu:
            'Time passes slowly, until one of the workers calls for help and you hear a couple of huge rocks fall to the ground. The workers run and, in one case, crawl away from the moving human bones. [custom1] You pull out your axe.
            '
            'I dash forward and strike it down.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dash forward and strike it down.')
                jump rockslidewithworkers04a
            '“Hold your positions!” I keep my distance and observe the corpse.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hold your positions!” I keep my distance and observe the corpse.')
                jump rockslidewithworkers04b

    label rockslidewithworkers04a:
        $ rockslide_workers_hardass_points += 1
        if pc_class == "warrior":
            $ custom1 = "You cut through the neck and the head flies away, hitting against the wall. The corpse stops moving and you step back, taking a defensive stance."
        else:
            $ custom1 = "You hit again and again, gasping for air as you try to break it to pieces. Finally, with a heavy breath, you realize the corpse has stopped moving. You step away from it."
        menu:
            'You crack the whitish skull, but the bones don’t stay still, trying to catch you. [custom1]
            \n\nThe crowd observes it all in silence, and after a couple of heartbeats, {color=#f6d6bd}the overseer{/color} points at the corpse. “The bloody bonehead has nae legs!”
            \n\nThe shock loses its grasp. The folks get closer and the first chuckle is followed by bursts of laughter. The loose bones scatter around. An older digger gives you a pat on the back. “Scary, aye? I almost ran away!”
            '
            'I’m not willing to rest yet. I push people away and approach the corpse.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not willing to rest yet. I push people away and approach the corpse.')
                $ rockslide_workers_hardass_points += 1
                jump rockslidewithworkers05
            'I smile back at her. “It sure was.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her. “It sure was.”')
                $ rockslide_workers_kindness_points += 1
                jump rockslidewithworkers05

    label rockslidewithworkers04b:
        $ rockslide_workers_kindness_points += 1
        menu:
            'You stand with a raised weapon, observing the moving creature. Its whitish skull is cracked and the thin arms, held together only by pneuma, are reaching out toward you. It doesn’t utter as much as a shout, and its empty eye sockets are like an abyss.
            \n\nThe crowd observes the creature, at first with frightened gasps, then in silence. After a couple of heartbeats, {color=#f6d6bd}the overseer{/color} points at the corpse. “The bloody bonehead has nae legs!”
            \n\nThe shock loses its grasp. One of the guards pokes the undead with a spear and before it manages to catch the weapon, it gets hit once, twice, and many more times, until it stops moving. The loose bones scatter around.
            \n\nThe first chuckle is followed by bursts of laughter. An older digger looks at you with a smile. “Scary, aye? I almost ran away!”
            '
            'I’m not willing to rest yet. I push people away and approach the corpse.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not willing to rest yet. I push people away and approach the corpse.')
                $ rockslide_workers_hardass_points += 1
                jump rockslidewithworkers05
            'Before I approach the corpse, I smile back at the worker. “It sure was.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I approach the corpse, I smile back at the worker. “It sure was.”')
                $ rockslide_workers_kindness_points += 1
                jump rockslidewithworkers05

    label rockslidewithworkers05:
        menu:
            'The undead didn’t even have its hips, and it was lucky to “sit” in an upward position. “Was this wretch buried by the tree, or did it get trapped after it died here,” wonders one of the guards, and a digger responds by spitting on the ground. “Let’s hope nae one was stupid enough to ne burn their dead.”
            \n\nThe hesitant workers try to stay away from the bones, but then {color=#f6d6bd}the overseer{/color} kicks the skull away, sparking another wave of laughter. He cups his head around his mouth. “Now, now! There may be another one here, en its legs may still be kicking! Grab your tools, we do ne have more than an hour ahead of us!”
            \n\nHe turns toward you and nods politely. “You know how to get rid of a corpse on the road. What do we do?”
            '
            'No point in wasting more time. “Cut the bones and throw them down the hill. Let wolves choke on them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No point in wasting more time. “Cut the bones and throw them down the hill. Let wolves choke on them.”')
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ pc_faithpoints_opportunities += 1
                jump rockslidewithworkers05a
            'My religion is clear on this. “The dead deserve dignity. We need to burn it.”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My religion is clear on this. “The dead deserve dignity. We need to burn it.”')
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints += 1
                jump rockslidewithworkers05b
            '“The dead deserve dignity. We need to burn it.”' if pc_religion == "pagan" or pc_religion == "none" or pc_religion == "unknown":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The dead deserve dignity. We need to burn it.”')
                jump rockslidewithworkers05b

    label rockslidewithworkers05a:
        $ rockslide_workers_hardass_points += 1
        $ minutes += 5
        menu:
            '“Good, ‘tis ne like ‘tis going to put itself back.” He rubs his hands together, then raises his voice and starts to assign new tasks.
            \n\nThe shattered remains are placed on the wheelbarrow - without the now-broken skull, they wouldn’t even resemble a human. You assist the workers on their way to the scarp, throwing down no more than a few bones at once, then going to the next spot.
            \n\nOn your way back, your companions discuss making a few charms once they get home. “If it saw us, it could still curse us,” says the man with a shaky voice.
            '
            'At least there are no other undead in sight.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least there are no other undead in sight.')
                if rockslide_workers_digging == 2:
                    $ quarters += 3
                else:
                    $ quarters += 4
                jump rockslidewithworkers06

    label rockslidewithworkers05b:
        $ achievement_pyrepoints += 1
        $ rockslide_workers_kindness_points += 1
        $ quarters += 4
        menu:
            'He sighs. “Aye, hard to argue with that. Take five souls with you.” He rubs his hands together, then raises his voice and starts to assign new tasks.
            \n\nCutting down branches with simple stone axes takes quite a bit of time. You take your tinderbox and gather at an old, dry bough standing in the middle of a meadow and cover it with broken twigs and bones. After a moment of silence, you step away from the burning remains.
            \n\nWithout a word, your companions observe the unusual pyre for another minute.
            '
            'I move back to the entrance. At least there are no other undead in sight.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move back to the entrance. At least there are no other undead in sight.')
                if rockslide_workers_digging == 2:
                    $ quarters += 1
                else:
                    $ quarters += 2
                jump rockslidewithworkers06

    label rockslidewithworkers06:
        show areapicture rockslide03 at basicfade
        $ quest_fisherhamlet_description03 = "We removed the rocks and got rid of an undead that was buried beneath them. I should report this to Thais."
        $ renpy.notify("Journal updated: The Old Hamlet")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
        $ fishinghamlet_unlocked = 1
        $ rockslide_cleared = 1
        if rockslide_workers_kindness_points > 6:
            $ howlersdell_reputation += 1
        if rockslide_workers_hardass_points > 6:
            $ howlersdell_reputation += 1
        menu:
            'As the end of the diggers’ work gets closer, they grow tired and annoyed, which starts a few squabbles. {color=#f6d6bd}The overseer{/color} has none of it, forcing them to focus. It doesn’t take long before the pass is cleared.
            \n\nIn silence, the workers remove their gloves, clean their chests with water, and gather the tools.
            '
            'I prepare {color=#f6d6bd}[horsename]{/color} for the rest of the journey.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare %s for the rest of the journey.' %horsename)
                $ travel_destination = "howlersdell"
                jump finaldestinationafterevent
