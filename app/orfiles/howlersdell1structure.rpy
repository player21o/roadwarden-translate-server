###################### Howler's Dell - a home of farmers, set at a clean brook. druids
default howlersdell_firsttime = 0
default howlersdell_firsttime_night = 0
default howlersdell_firsttime_goodimpression = 0
default howlersdell_dayvisit = 0

default howlersdell_reputation = 0
default howlersdell_reputation_points = 0
default howlersdell_reputation_status = 0
default howlersdell_mundanework_day = 0

default howlersdell_food_free = 0

default howlersdell_fluff_relaxing = 0
default howlersdell_fluff_relaxingold = 0
default howlersdell_fluff_01 = ""
default howlersdell_fluff_02 = ""
default howlersdell_square_fluff = ""
default howlersdell_rumor_fluff = ""
default howlersdell_rumor_fluff_old = ""
default howlersdell_rumor_firsttime = 0
default howlersdell_rumor_counter = 0

default howlersdell_square_children_tale = 0
default howlersdell_square_thais_fluff = ""
default howlersdell_square_akakios_fluff = ""
default howlersdell_square_eryx_fluff = ""

default howlersdell_horsename_feeding = 0 # day
default howlersdell_horsename_feeding_firsttime = 0
default howlersdell_horsename_feeding_canceled = 0
default howlersdell_horsename_feeding_refused_counter = 0

default howlersdell_mundanework_available = 0
default howlersdell_mundanework_numberoftimes = 0
default howlersdell_mundanework_payment_base = 1
default howlersdell_mundanework_payment_bonus = 0
default howlersdell_mundanework_payment_total = 0
default howlersdell_mundanework_blocked = 0
default howlersdell_mundanework_type = ""
default howlersdell_mundanework_type_old = ""
default howlersdell_mundanework_type_day = 0
default howlersdell_mundanework_riskchance = 0

label howlersdell01:
    nvl clear
    $ pc_area = "howlersdell"
    if ruinedvillage_truth and not thais_defeated:
        $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    else:
        $ renpy.music.play("audio/track_03howlersdell.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not howlersdell_firsttime:
        $ world_known_npcs += 2
        $ howlersdell_firsttime = 1
        $ world_known_areas += 1
        $ rockslide_unlocked = 1
        $ beholder_unlocked = 1
        $ westerncrossroads_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ thais_inn = day
        $ howlersdell_dayvisit = day
        if ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
            $ pyrrhos_quest_tohowlersdell = 1
        if howlersdell_firsttime_night:
            $ howlersdell_firsttime_night = 0
            jump howlersdellfirsttimeALT01north
        elif howlersdellforestgardendescription:
            jump howlersdellfirsttime01north
        else:
            jump howlersdellfirsttime01south
    else:
        $ can_leave = 1
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        if pyrrhos_quest_escorting == 1:
            $ pyrrhos_quest_escorting = 0
            $ pc_battlecounter += 1
            $ pyrrhos_howlersdell_arrivalcounter = day
            $ pyrrhos_howlersdell = 1
            if description_pyrrhos01 and pyrrhos_quest_escorting == 1:
                $ pyrrhos_howlersdell_fluff = "{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with {color=#f6d6bd}the trader{/color}."
            else:
                $ pyrrhos_howlersdell_fluff = "{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with {color=#f6d6bd}the trader{/color}."
            jump pyrrhoshowlers01arrival
        elif rockslide_cleared and not rockslide_workers_druids:
            jump howlersdell_elpis_returningfromhamletALL
        elif druidcave_druid_about_plague_travel == 1:
            jump druidcave_druid_about_plague03b
        elif not thais_about_plague_cured and oldpagos_cured:
            $ thais_about_plague_cured = 1
            jump howlersdellthais_about_healingtheplague00
        else:
            jump howlersdellregular01

label howlersdellregular01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    show areapicture howlersdellfull at basicfade
    if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail" or thais_bigmad_beaten:
        $ howlersdell_fluff_01 = renpy.random.choice(['The tense looks of the locals don’t last for long. They either keep their distance or walk by you, observing the guards nervously.'])
        $ howlersdell_fluff_02 = renpy.random.choice([''])
    else:
        $ howlersdell_fluff_01 = renpy.random.choice(['A group of children covered in mud gathers by your mount and argues loudly about what’s “better” - horses or donkeys.', 'You see a crying boy, surrounded by three older girls. They clean his injured knee while stopping themselves from laughter.', 'A washwoman is singing about the last sunbeams of summer, but her heavy accent makes her words difficult to understand.', 'You smell the pleasant aroma of ground herbs, as well as freshly baked bread.', 'An upset mouflon is bleating time and again, waiting for someone’s attention.', 'An old fisher is walking nearby, pointing at a tiny, sparkling fish he’s just caught.', 'A young couple is holding hands as they wish you a great day.', 'Three drunken youngsters are having something between a conversation and a mumbling exchange of jokes.', 'A couple of older people are gossiping with excitement while they grind grains with mill stones.', 'A young man is reprimanding a little girl who had dropped and shattered a clay bowl.', 'A young woman is chasing after a loose chicken, embarrassed by the giggling of bystanders.', 'Two guards are having a duel with blunt spears in the yard.', 'A woman in a brown robe observes you from a distance and walks away when you make eye contact.', 'A field worker walks by you, coughing loudly as he tries to open his waterskin.', 'A young man is hanging laundry, humming a melody you’ve never heard before.', 'On the islet in the center of the village an old woman is telling a group of children a story about the lethal shouts of howlers.', 'A woman and a young boy are sitting on a bench as she shows him how to weave a basket.', 'Two men in light clothing are carrying a wooden log, insulting each other in friendly banter.', 'A man is showing a teenage girl how to chop firewood with a bone axe.', 'Two red-haired twins are weeding a flower garden.', 'A group of laughing villagers is chasing after a runaway hog.', 'A gray-haired, muscular guard is trying to hammer out the dents in her rusty helmet.', 'A short-tempered hunter tries to explain to his parents that there are no bears where he’s going.'])
        label howlersdellregular01after:
            $ howlersdell_fluff_02 = renpy.random.choice(['A group of children covered in mud gathers by your mount and argues loudly about what’s “better” - horses or donkeys.', 'You see a crying boy, surrounded by three older girls. They clean his injured knee while stopping themselves from laughter.', 'A washwoman is singing about the last sunbeams of summer, but her heavy accent makes her words difficult to understand.', 'You smell the pleasant aroma of ground herbs, as well as freshly baked bread.', 'An upset mouflon is bleating time and again, waiting for someone’s attention.', 'An old fisher is walking nearby, pointing at a tiny, sparkling fish he’s just caught.', 'A young couple is holding hands as they wish you a great day.', 'Three drunken youngsters are having something between a conversation and a mumbling exchange of jokes.', 'A couple of older people are gossiping with excitement while they grind grains with mill stones.', 'A young man is reprimanding a little girl who had dropped and shattered a clay bowl.', 'A young woman is chasing after a loose chicken, embarrassed by the giggling of bystanders.', 'Two guards are having a duel with blunt spears in the yard.', 'A woman in a brown robe observes you from a distance and walks away when you make eye contact.', 'A field worker walks by you, coughing loudly as he tries to open his waterskin.', 'A young man is hanging laundry, humming a melody you’ve never heard before.', 'On the islet in the center of the village an old woman is telling a group of children a story about the lethal shouts of howlers.', 'A woman and a young boy are sitting on a bench as she shows him how to weave a basket.', 'Two men in light clothing are carrying a wooden log, insulting each other in friendly banter.', 'A man is showing a teenage girl how to chop firewood with a bone axe.', 'Two red-haired twins are weeding a flower garden.', 'A group of laughing villagers is chasing after a runaway hog.', 'A gray-haired, muscular guard is trying to hammer out the dents in her rusty helmet.', 'A short-tempered hunter tries to explain to his parents that there are no bears where he’s going.'])
            if howlersdell_fluff_02 == howlersdell_fluff_01:
                jump howlersdellregular01after
    if pc_hp > 1:
        $ custom1 = "swiftly"
    else:
        $ custom1 = "carefully"
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail" or thais_bigmad_beaten:
        $ can_leave = 1
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        menu:
            'You ride through the open gate, then dismount [custom1]. The guards give you distrustful looks and no one shows up to greet you.
            '
            'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                jump howlersdell_steephouseconfrontation00
            'I go to the main square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                jump howlersdellsquareregular01
            'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                jump howlersdell_erastos01
            'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                if howlersdell_bion_firsttime:
                    jump howlersdelltailor01
                else:
                    jump howlersdelltailorfirsttime01
            'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                pass
            'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                if howlersdell_elpis_firsttime_theywant:
                    jump howlersdelldruids01yes
                else:
                    jump howlersdelldruids01no
            'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                pass
            'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                jump howlersdelldruids01yes
            'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                jump howlersdelldruids01
            'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                jump howlersdellsinglepeople01firsttime
            'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                jump howlersdellsinglepeople01firsttime
            'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                jump howlersdellsinglepeople01
            'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                pass
            'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                pass
            'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                jump howlersdellinstalingrodwithpermission01
            'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                pass
            'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                jump howlersdellfisherhamletupdates03b
            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                pass
            'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                pass
            '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                pass
            '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                pass
    if howlersdell_dayvisit == day:
        if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
            menu:
                'You ride through the open gate, then [custom1] dismount. There’s too many people around to let {color=#f6d6bd}[horsename]{/color} run among them.
                '
                'I head to the stables.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stables.')
                    jump howlersdell_horsename_feeding_firsttime01
        elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
            menu:
                'You ride through the open gate, then [custom1] dismount. There’s too many people around to let {color=#f6d6bd}[horsename]{/color} run among them.
                '
                'I head to the stables.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stables.')
                    jump howlersdell_horsename_feeding01
        else:
            $ can_leave = 1
            if howlersdell_eryx_about_room:
                $ can_rest = 1
            $ can_items = 1
            menu:
                'You ride through the open gate, then [custom1] dismount. [howlersdell_fluff_01] [howlersdell_fluff_02]
                '
                'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                    jump howlersdell_steephouseconfrontation00
                'I go to the main square.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                    jump howlersdellsquareregular01
                'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                    jump howlersdell_erastos01
                'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                    if howlersdell_bion_firsttime:
                        jump howlersdelltailor01
                    else:
                        jump howlersdelltailorfirsttime01
                'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                    pass
                'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    if howlersdell_elpis_firsttime_theywant:
                        jump howlersdelldruids01yes
                    else:
                        jump howlersdelldruids01no
                'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                    pass
                'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    jump howlersdelldruids01yes
                'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                    jump howlersdelldruids01
                'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                    jump howlersdellsinglepeople01firsttime
                'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                    jump howlersdellsinglepeople01firsttime
                'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                    jump howlersdellsinglepeople01
                'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                    pass
                'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                    pass
                'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                    jump howlersdellinstalingrodwithpermission01
                'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                    pass
                'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                    jump howlersdellfisherhamletupdates03b
                'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                    pass
                'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                    pass
                '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                    pass
                '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                    pass
    elif appearance <= 1:
        $ howlersdell_dayvisit = day
        if cleanliness <= 1:
            $ custom2 = "after you notice your own smell and the dirt on your clothes, you no longer wonder why"
        elif cleanliness_clothes_torn and not item_fancyclothes:
            $ custom2 = "your clothes, torn and worn, make you look like a vagabond"
        elif cleanliness_clothes_blood and not item_fancyclothes:
            $ custom2 = "your clothes, covered in blood, lure the disgusted glances"
        else:
            $ custom2 = "something in your appearance makes your presence unwelcome"
        if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
            menu:
                'You ride through the open gate, then [custom1] dismount. Some of the locals greet you politely, but they keep their distance - [custom2].
                '
                'I head to the stables.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stables.')
                    jump howlersdell_horsename_feeding_firsttime01
        elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
            menu:
                'You ride through the open gate, then [custom1] dismount. Some of the locals greet you politely, but they keep their distance - [custom2].
                '
                'I head to the stables.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stables.')
                    jump howlersdell_horsename_feeding01
        else:
            $ can_leave = 1
            if howlersdell_eryx_about_room:
                $ can_rest = 1
            $ can_items = 1
            menu:
                'You ride through the open gate, then [custom1] dismount. Some of the locals greet you politely, but they keep their distance - [custom2].
                '
                'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                    jump howlersdell_steephouseconfrontation00
                'I go to the main square.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                    jump howlersdellsquareregular01
                'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                    jump howlersdell_erastos01
                'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                    if howlersdell_bion_firsttime:
                        jump howlersdelltailor01
                    else:
                        jump howlersdelltailorfirsttime01
                'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                    pass
                'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    if howlersdell_elpis_firsttime_theywant:
                        jump howlersdelldruids01yes
                    else:
                        jump howlersdelldruids01no
                'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                    pass
                'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    jump howlersdelldruids01yes
                'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                    jump howlersdelldruids01
                'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                    jump howlersdellsinglepeople01firsttime
                'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                    jump howlersdellsinglepeople01firsttime
                'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                    jump howlersdellsinglepeople01
                'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                    pass
                'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                    pass
                'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                    jump howlersdellinstalingrodwithpermission01
                'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                    pass
                'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                    jump howlersdellfisherhamletupdates03b
                'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                    pass
                'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                    pass
                '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                    pass
                '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                    pass
    else:
        $ howlersdell_dayvisit = day
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if (howlersdell_reputation+appearance_charisma) >= 12:
            menu:
                'You approach the opening gate, then [custom1] dismount. A guard approaches you, ready to take your mount to a stable. “Good to see you! How are your journeys?”
                '
                'We gossip for a bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We gossip for a bit.')
                    jump howlersdellsquareregular01rumors
                'I don’t have time to talk. I enter the village.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to talk. I enter the village.')
                    if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding_firsttime01
                    elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding01
                    else:
                        jump howlersdellafterinteraction
        elif (howlersdell_reputation+appearance_charisma) > 8:
            menu:
                'You approach the opening gate, then [custom1] dismount. A guard approaches you, ready to take your mount to a stable. “Welcome, [pcname]. How’s the outside world for you?”
                '
                'We gossip for a bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We gossip for a bit.')
                    jump howlersdellsquareregular01rumors
                'I don’t have time to talk. I enter the village.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to talk. I enter the village.')
                    if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding_firsttime01
                    elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding01
                    else:
                        jump howlersdellafterinteraction
        elif (howlersdell_reputation+appearance_charisma) > 4:
            menu:
                'You approach the opening gate, then [custom1] dismount. A guard approaches you, ready to take your mount to a stable. “Greetings, roadwarden. What news do you bring?”
                '
                'We gossip for a bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We gossip for a bit.')
                    jump howlersdellsquareregular01rumors
                'I don’t have time to talk. I enter the village.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to talk. I enter the village.')
                    if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding_firsttime01
                    elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding01
                    else:
                        jump howlersdellafterinteraction
        else:
            menu:
                'You approach the opening gate, then [custom1] dismount. A guard approaches you, ready to take your mount to a stable. “Hello, stranger. What news do you bring?”
                '
                'We gossip for a bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We gossip for a bit.')
                    jump howlersdellsquareregular01rumors
                'I don’t have time to talk. I enter the village.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have time to talk. I enter the village.')
                    if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding_firsttime01
                    elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
                        jump howlersdell_horsename_feeding01
                    else:
                        jump howlersdellafterinteraction

label howlersdellsquareregular01rumors:
    $ howlersdell_rumor_fluff = ""
    $ howlersdell_rumor_fluff = renpy.random.choice(['three kids had had a pretty severe fever, but the druids have managed to keep it under control', 'during the last hunting trip one of the hunters was badly injured. If spells won’t help, she may even lose an arm', 'a massive beast has tried to make a lair among the hemp fields. It may be the time to form a night watch', 'two teens suddenly announced their engagement, and no soul knows when it started', 'a baker fell asleep while making pies, wasting meat and flour', 'a cart with wooden logs has collapsed, so there was quite a mess in the main square', 'it turned out that a couple of houses need to fix their roofs before winter, which won’t be easy with so little time', 'quite a bunch of fish have showed up in the creek, so the locals will have some refreshing pies tomorrow', 'the fields could use some more rain, and no one is happy to have to water them with buckets', 'the mouflons are getting weirdly fat, but no one can tell yet if they’re pregnant or not', 'a couple of kids had stolen a cask of mead, but were caught before they reached its bottom', 'the roaring of dragons gets louder every day, so maybe they’re trying to overcome the local hunt-queen', 'the fresh cheese spoiled very quickly. Maybe there’s a new evil spirit around', 'the mayor was arguing with the druids, but no soul knows why', 'there’s a dispute between two local families, both of which claim to have the best mouflon shearer in the village. They’re very competitive', 'two groups of local kids have invented a new way to wrestle for points, and they are now trying to outdo one other in small contests'])
    if howlersdell_rumor_fluff == howlersdell_rumor_fluff_old:
        jump howlersdellsquareregular01rumors
    $ howlersdell_rumor_fluff_old = howlersdell_rumor_fluff
    $ howlersdell_reputation_points += 3
    $ quarters += 1
    if not howlersdell_rumor_firsttime:
        $ howlersdell_rumor_firsttime = 1
        $ custom1 = "Even though {color=#f6d6bd}Howler’s Dell{/color} is a large village, the life here is slow. "
    else:
        $ custom1 = ""
    $ howlersdell_rumor_counter += 1
    menu:
        '[custom1]The curious locals gather around to take part in your conversation. Recently, [howlersdell_rumor_fluff].
        '
        'I enter the village.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the village.')
            if not howlersdell_horsename_feeding_firsttime and not howlersdell_horsename_feeding_canceled:
                jump howlersdell_horsename_feeding_firsttime01
            elif howlersdell_horsename_feeding != day and not howlersdell_horsename_feeding_canceled:
                jump howlersdell_horsename_feeding01
            else:
                jump howlersdellafterinteraction

label howlersdell_horsename_feeding_firsttime01:
    $ howlersdell_horsename_feeding_firsttime = 1
    menu:
        'You spend a few minutes with {color=#f6d6bd}[horsename]{/color}, but before you reach the square, someone clears their throat. You turn toward a man in his fifties, with large hands, an elegant beard, and no hair. “{color=#f6d6bd}The stablemaster{/color},” he both introduces himself and answers an unspoken question. You frown, then realize that you indeed saw him before, and your palfrey was nicely taken care of during your first visit to the village.
        \n\n“Or rather, I’m one when ‘tis necessary, but I’d rather grind flour,” he says with annoyance. “You do ne think your beast waters itself, brings itself fodder from a storehouse, and cleans its own shit, nae? Takes time en hay. If ‘tis,” he points at your companion, “is ne going to work for it, you better have a pouch at hand.”
        \n\nYou look behind you. The “stables” are not much more than an open shed, with piles of planks, two donkeys, and a bunch of napping chickens.
        '
        '“Would a dragon bone be enough?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would a dragon bone be enough?”')
            if pc_class == "scholar":
                $ at_unlock_knowledge = 1
                $ at = 0
            menu:
                'He nods. “For one day... Aye, tha’s fair.”
                \n\nHe looks around, rubbing his hands together.
                '
                '“Come to think of it... It’s an opportunity for the village. Horse manure makes for great plant food.”' ( condition="at == 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come to think of it... It’s an opportunity for the village. Horse manure makes for great plant food.”')
                    $ at = 0
                    $ howlersdell_horsename_feeding_canceled = 1
                    $ howlersdell_horsename_feeding = day
                    $ at_unlock_knowledge = 0
                    menu:
                        'You describe what you’ve learned during your studies, and the man stops paying any attention. “Fine, fine,” he sighs and turns around. “I’ll grab a shovel en a barrow.”
                        '
                        'Issue solved.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                            jump howlersdellafterinteraction
                'I show him {color=#f6d6bd}Thais’{/color} parchment.' if item_howlersdelltoken:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show him {color=#f6d6bd}Thais’{/color} parchment.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    $ howlersdell_horsename_feeding_canceled = 1
                    $ howlersdell_horsename_feeding = day
                    menu:
                        'He scowls at you in silence and picks up a brush from a wooden beam.
                        '
                        'Issue solved.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                            jump howlersdellafterinteraction
                'I smile. “Don’t you think I’ve done enough for the village to get some free hay?”' if (howlersdell_reputation+appearance_charisma) >= 20:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Don’t you think I’ve done enough for the village to get some free hay?”')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    $ howlersdell_horsename_feeding_canceled = 1
                    $ howlersdell_horsename_feeding = day
                    menu:
                        'He looks at you in silence, then smiles back at you, even if only politely. “You may be right, [pcname]. Do ne worry about this any more.” He turns away and heads toward the brush that rests on a wooden beam
                        '
                        'Issue solved.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                            jump howlersdellafterinteraction
                '“Here you go.”' if coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here you go.”')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    $ howlersdell_horsename_feeding = day
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                    $ coins -= 1
                    $ howlersdell_reputation_points += 1
                    menu:
                        'He nods with gratitude and throws the bone into a leaky bucket hanging from a nail, then grabs a wooden pitchfork.
                        '
                        'I let him work in peace.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let him work in peace.')
                            jump howlersdellafterinteraction
                '“I’m broke. My mount needs only some hay, water, and peace.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m broke. My mount needs only some hay, water, and peace.”')
                    $ howlersdell_horsename_feeding = day
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    $ howlersdell_horsename_feeding_refused_counter += 1
                    if howlersdell_horsename_feeding_refused_counter >= 3:
                        $ howlersdell_horsename_feeding_refused_counter -= 3
                        $ howlersdell_reputation -= 1
                    menu:
                        'He scowls at you, but points at an empty bucket and steps away.
                        '
                        'I fill the trough with water from the creek and make sure {color=#f6d6bd}[horsename]{/color} is comfortable.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill the trough with water from the creek and make sure {color=#f6d6bd}%s{/color} is comfortable.' %horsename)
                            $ quarters += 1
                            jump howlersdellafterinteraction

    label howlersdell_horsename_feeding01:
        $ howlersdell_horsename_feeding = day
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            '{color=#f6d6bd}The stablemaster{/color} shows up soon after you step away from {color=#f6d6bd}[horsename]{/color}. His lips are thinned, and he gives a longing glance toward the bridge.
            '
            '“Come to think of it... It’s an opportunity for the village. Horse manure makes for great plant food.”' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come to think of it... It’s an opportunity for the village. Horse manure makes for great plant food.”')
                $ at = 0
                $ howlersdell_horsename_feeding_canceled = 1
                $ howlersdell_horsename_feeding = day
                $ at_unlock_knowledge = 0
                menu:
                    'You describe what you’ve learned during your studies, and the man stops paying any attention. “Fine, fine,” he sighs and turns around. “I’ll grab a shovel en a barrow.”
                    '
                    'Issue solved.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                        jump howlersdellafterinteraction
            'I show him {color=#f6d6bd}Thais’{/color} parchment.' if item_howlersdelltoken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show him {color=#f6d6bd}Thais’{/color} parchment.')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ howlersdell_horsename_feeding_canceled = 1
                $ howlersdell_horsename_feeding = day
                menu:
                    'He scowls at you in silence and picks up a brush from a wooden beam.
                    '
                    'Issue solved.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                        jump howlersdellafterinteraction
            'I smile. “Don’t you think I’ve done enough for the village to get some free hay?”' if (howlersdell_reputation+appearance_charisma) >= 20:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Don’t you think I’ve done enough for the village to get some free hay?”')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ howlersdell_horsename_feeding_canceled = 1
                $ howlersdell_horsename_feeding = day
                menu:
                    'He looks at you in silence, then smiles back at you, even if only politely. “You may be right, [pcname]. Do ne worry about this any more.” He turns away and heads toward the brush that rests on a wooden beam
                    '
                    'Issue solved.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Issue solved.')
                        jump howlersdellafterinteraction
            '“Here you go.”' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here you go.”')
                $ at_unlock_knowledge = 0
                $ at = 0
                $ howlersdell_horsename_feeding = day
                show screen notifyimage( "-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                $ coins -= 1
                $ howlersdell_reputation_points += 1
                menu:
                    'He nods with gratitude and throws the bone into a leaky bucket hanging from a nail, then grabs a wooden pitchfork.
                    '
                    'I let him work in peace.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let him work in peace.')
                        jump howlersdellafterinteraction
            '“I’m broke. My mount needs only some hay, water, and peace.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m broke. My mount needs only some hay, water, and peace.”')
                $ howlersdell_horsename_feeding = day
                $ at_unlock_knowledge = 0
                $ at = 0
                $ howlersdell_horsename_feeding_refused_counter += 1
                if howlersdell_horsename_feeding_refused_counter >= 3:
                    $ howlersdell_horsename_feeding_refused_counter -= 3
                    $ howlersdell_reputation -= 1
                menu:
                    'He scowls at you, but points at an empty bucket and steps away.
                    '
                    'I fill the trough with water from the creek and make sure {color=#f6d6bd}[horsename]{/color} is comfortable.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill the trough with water from the creek and make sure {color=#f6d6bd}%s{/color} is comfortable.' %horsename)
                        $ quarters += 1
                        jump howlersdellafterinteraction

label howlersdellafterinteraction:
    show areapicture howlersdellfull at basicfade
    hide howlersdellsquareutensils
    $ can_leave = 1
    if howlersdell_eryx_about_room:
        $ can_rest = 1
    $ can_items = 1
    if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail" or thais_bigmad_beaten:
        $ howlersdell_fluff_01 = renpy.random.choice(['The tense looks of the locals don’t last for long. They either keep their distance or walk by you, observing the guards nervously.'])
        $ howlersdell_fluff_02 = renpy.random.choice([''])
    else:
        $ howlersdell_fluff_01 = renpy.random.choice(['A group of children covered in mud gathers by your mount and argues loudly about what’s “better” - horses or donkeys.', 'You see a crying boy, surrounded by three older girls. They clean his injured knee while stopping themselves from laughter.', 'A washwoman is singing about the last sunbeams of summer, but her heavy accent makes her words difficult to understand.', 'You smell the pleasant aroma of ground herbs, as well as freshly baked bread.', 'An upset mouflon is bleating time and again, waiting for someone’s attention.', 'An old fisher is walking nearby, pointing at a tiny, sparkling fish he’s just caught.', 'A young couple is holding hands as they wish you a great day.', 'Three drunken youngsters are having something between a conversation and a mumbling exchange of jokes.', 'A couple of older people are gossiping with excitement while they grind grains with mill stones.', 'A young man is reprimanding a little girl who had dropped and shattered a clay bowl.', 'A young woman is chasing after a loose chicken, embarrassed by the giggling of bystanders.', 'Two guards are having a duel with blunt spears in the yard.', 'A woman in a brown robe observes you from a distance and walks away when you make eye contact.', 'A field worker walks by you, coughing loudly as he tries to open his waterskin.', 'A young man is hanging laundry, humming a melody you’ve never heard before.', 'On the islet in the center of the village an old woman is telling a group of children a story about the lethal shouts of howlers.', 'A woman and a young boy are sitting on a bench as she shows him how to weave a basket.', 'Two men in light clothing are carrying a wooden log, insulting each other in friendly banter.', 'A man is showing a teenage girl how to chop firewood with a bone axe.', 'Two red-haired twins are weeding a flower garden.', 'A group of laughing villagers is chasing after a runaway hog.', 'A gray-haired, muscular guard is trying to hammer out the dents in her rusty helmet.', 'A short-tempered hunter tries to explain to his parents that there are no bears where he’s going.'])
        label howlersdellafterinteractionafter:
            $ howlersdell_fluff_02 = renpy.random.choice(['A group of children covered in mud gathers by your mount and argues loudly about what’s “better” - horses or donkeys.', 'You see a crying boy, surrounded by three older girls. They clean his injured knee while stopping themselves from laughter.', 'A washwoman is singing about the last sunbeams of summer, but her heavy accent makes her words difficult to understand.', 'You smell the pleasant aroma of ground herbs, as well as freshly baked bread.', 'An upset mouflon is bleating time and again, waiting for someone’s attention.', 'An old fisher is walking nearby, pointing at a tiny, sparkling fish he’s just caught.', 'A young couple is holding hands as they wish you a great day.', 'Three drunken youngsters are having something between a conversation and a mumbling exchange of jokes.', 'A couple of older people are gossiping with excitement while they grind grains with mill stones.', 'A young man is reprimanding a little girl who had dropped and shattered a clay bowl.', 'A young woman is chasing after a loose chicken, embarrassed by the giggling of bystanders.', 'Two guards are having a duel with blunt spears in the yard.', 'A woman in a brown robe observes you from a distance and walks away when you make eye contact.', 'A field worker walks by you, coughing loudly as he tries to open his waterskin.', 'A young man is hanging laundry, humming a melody you’ve never heard before.', 'On the islet in the center of the village an old woman is telling a group of children a story about the lethal shouts of howlers.', 'A woman and a young boy are sitting on a bench as she shows him how to weave a basket.', 'Two men in light clothing are carrying a wooden log, insulting each other in friendly banter.', 'A man is showing a teenage girl how to chop firewood with a bone axe.', 'Two red-haired twins are weeding a flower garden.', 'A group of laughing villagers is chasing after a runaway hog.', 'A gray-haired, muscular guard is trying to hammer out the dents in her rusty helmet.', 'A short-tempered hunter tries to explain to his parents that there are no bears where he’s going.'])
            if howlersdell_fluff_02 == howlersdell_fluff_01:
                jump howlersdellafterinteractionafter
    menu:
        'You’re wandering through the village. [howlersdell_fluff_01] [howlersdell_fluff_02]
        '
        'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
            jump howlersdell_steephouseconfrontation00
        'I go to the main square.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
            jump howlersdellsquareregular01
        'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
            jump howlersdell_erastos01
        'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
            if howlersdell_bion_firsttime:
                jump howlersdelltailor01
            else:
                jump howlersdelltailorfirsttime01
        'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
            pass
        'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
            if howlersdell_elpis_firsttime_theywant:
                jump howlersdelldruids01yes
            else:
                jump howlersdelldruids01no
        'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
            pass
        'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
            jump howlersdelldruids01yes
        'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
            jump howlersdelldruids01
        'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
            jump howlersdellsinglepeople01firsttime
        'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
            jump howlersdellsinglepeople01firsttime
        'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
            jump howlersdellsinglepeople01
        'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
            pass
        'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
            pass
        'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
            jump howlersdellinstalingrodwithpermission01
        'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
            pass
        'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
            jump howlersdellfisherhamletupdates03b
        'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
            pass
        'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
            pass
        '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
            jump howlersdell_mundanework01
        '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
            pass
        '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
            pass
        '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
            jump howlersdell_mundanework01
        '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
            pass
        '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
            pass

label howlersdellsquareregular01:
    show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
    if quarters < 39:
        show howlersdellsquareutensils 02 at basicfade
        $ howlersdell_square_fluff = "A couple of laborers eat gruel and leftovers, too sleepy to gossip. The only people who aren’t yawning are the two elderly ladies who sit on a bench, holding hands and observing the creek."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is sitting near the door, from time to time carrying out another bowl with either stew or gruel."
        if quarters < 35:
            $ howlersdell_square_akakios_fluff = ""
        else:
            $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is preparing his stall, unpacking crates and ordering some young people around."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting at one of the tables, having a conversation with a girl half her age."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    elif quarters < (world_daylength-28):
        show howlersdellsquareutensils 03 at basicfade
        $ howlersdell_square_fluff = "The few souls sitting at the tables converse with one another while holding their mugs or snacking on bread with either honey or salted butter."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper {/color}spends most of the time inside, cooking things for dinner, but occasionally he takes a break to make sure that his daughter, who is sitting behind the counter, doesn’t need his assistance."
        $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is bartering with a bunch of people at once, from time to time taking something from the wagon and putting it on the counter, then, for some reason, moving it back to where he took it from."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is leaning against a table, listening to a group of squabbling workers."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    elif quarters < (world_daylength-12):
        show howlersdellsquareutensils 01 at basicfade
        $ howlersdell_square_fluff = "The stools and benches are filled. People share meals, news, and plans for later. The air is lively and filled with soothing routine."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is walking among the tables cheerfully, taking care of empty bowls and plates, or bringing new servings from inside the building."
        $ howlersdell_square_akakios_fluff = "\n\nThe stall is in perfect order, but draws little of the locals’ attention. {color=#f6d6bd}The trader{/color} walks around, gossiping. Whenever someone approaches the counter, he moves back quickly."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting in her chair, sharing a meal with a couple of fancy-looking folks."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    else:
        show howlersdellsquareutensils 04 at basicfade
        $ howlersdell_square_fluff = "It’s getting darker, but not much colder. More than a dozen locals are gathered at or by the tables, playing dice or other games, drinking, eating supper, or simply chatting."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is standing behind his counter, filling mugs with beer or buttermilk, while his daughter is cleaning the tables with a wet cloth and carrying around a bucket of stream water."
        if quarters < (world_daylength-4):
            $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is packing his goods, though with no rush. He’s talking with a man who’s sewing sacks on a nearby stool."
        else:
            $ howlersdell_square_akakios_fluff = ""
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is standing near the bank, giving commands to a group of armored guards."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    if pyrrhos_howlersdell == 1:
        $ pyrrhos_howlersdell_fluff = ""
        if description_pyrrhos01:
            $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
        else:
            $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
    else:
        $ pyrrhos_howlersdell_fluff = ""
    if thais_afk == day:
        $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    $ can_leave = 0
    if howlersdell_eryx_about_room:
        $ can_rest = 1
    $ can_items = 1
    if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail" or thais_bigmad_beaten:
        $ howlersdell_square_fluff = "The locals spread, leaving you alone with the merchants and guards."
    if quarters >= (world_daylength-4) and quarters < 88 and not howlersdell_square_children_tale and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
        jump howlersdell_square_children_tale00
    else:
        menu:
            'You approach the inn. [howlersdell_square_fluff]
            \n\n[howlersdell_square_eryx_fluff] [howlersdell_square_thais_fluff][howlersdell_square_akakios_fluff][pyrrhos_howlersdell_fluff]
            '
            'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
                jump howlersdelloldsailor01
            'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
                $ thais_inn = day
                jump howlersdellwaitingforthais01
            'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
                jump howlersdelltalkingtothais01
            'Thais won’t speak with me today. (disabled)' if thais_afk == day:
                pass
            'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
                if howlersdell_eryx_firsttime:
                    jump howlersdellinnkeeper01
                else:
                    $ howlersdell_eryx_firsttime = 1
                    jump howlersdellinnkeeperfirsttime01
            'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01
            '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01waiting
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01waiting
            'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump howlersdellafterinteraction

label howlersdellsquaafterinteraction01:
    show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
    if quarters < 39:
        show howlersdellsquareutensils 02 at basicfade
        $ howlersdell_square_fluff = "A couple of laborers eat gruel and leftovers, too sleepy to gossip. The only people who aren’t yawning are the two elderly ladies who sit on a bench, holding hands and observing the creek."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is sitting near the door, from time to time carrying out another bowl with either stew or gruel."
        if quarters < 35:
            $ howlersdell_square_akakios_fluff = ""
        else:
            $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is preparing his stall, unpacking crates and ordering some young people around."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting at one of the tables, having a conversation with a girl half her age."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    elif quarters < (world_daylength-28):
        show howlersdellsquareutensils 03 at basicfade
        $ howlersdell_square_fluff = "The few souls sitting at the tables converse with one another while holding their mugs or snacking on bread with either honey or salted butter."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper {/color}spends most of the time inside, cooking things for dinner, but occasionally he takes a break to make sure that his daughter, who is sitting behind the counter, doesn’t need his assistance."
        $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is bartering with a bunch of people at once, from time to time taking something from the wagon and putting it on the counter, then, for some reason, moving it back to where he took it from."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is leaning against a table, listening to a group of squabbling workers."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    elif quarters < (world_daylength-12):
        show howlersdellsquareutensils 01 at basicfade
        $ howlersdell_square_fluff = "The stools and benches are filled. People share meals, news, and plans for later. The air is lively and filled with soothing routine."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is walking among the tables cheerfully, taking care of empty bowls and plates, or bringing new servings from inside the building."
        $ howlersdell_square_akakios_fluff = "\n\nThe stall is in perfect order, but draws little of the locals’ attention. {color=#f6d6bd}The trader{/color} walks around, gossiping. Whenever someone approaches the counter, he moves back quickly."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting in her chair, sharing a meal with a couple of fancy-looking folks."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    else:
        show howlersdellsquareutensils 04 at basicfade
        $ howlersdell_square_fluff = "It’s getting darker, but not much colder. More than a dozen locals are gathered at or by the tables, playing dice or other games, drinking, eating supper, or simply chatting."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is standing behind his counter, filling mugs with beer or buttermilk, while his daughter is cleaning the tables with a wet cloth and carrying around a bucket of stream water."
        if quarters < (world_daylength-4):
            $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is packing his goods, though with no rush. He’s talking with a man who’s sewing sacks on a nearby stool."
        else:
            $ howlersdell_square_akakios_fluff = ""
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is standing near the bank, giving commands to a group of armored guards."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    if thais_afk == day:
        $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
    $ can_leave = 0
    if howlersdell_eryx_about_room:
        $ can_rest = 1
    $ can_items = 1
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail" or thais_bigmad_beaten:
        $ howlersdell_square_fluff = "The locals spread, leaving you alone with the merchants and guards."
    if quarters >= (world_daylength-4) and quarters < 88 and not howlersdell_square_children_tale and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
        jump howlersdell_square_children_tale00
    menu:
        'You’re in front of the {color=#f6d6bd}Ape Ale{/color} inn.
        '
        'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
            jump howlersdelloldsailor01
        'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
            $ thais_inn = day
            jump howlersdellwaitingforthais01
        'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
            jump howlersdelltalkingtothais01
        'Thais won’t speak with me today. (disabled)' if thais_afk == day:
            pass
        'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
            if howlersdell_eryx_firsttime:
                jump howlersdellinnkeeper01
            else:
                $ howlersdell_eryx_firsttime = 1
                jump howlersdellinnkeeperfirsttime01
        'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
            if howlersdell_akakios_firsttime:
                jump howlersdelltrader01
            else:
                $ howlersdell_akakios_firsttime = 1
                jump howlersdelltraderfirsttime01
        '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
            if howlersdell_akakios_firsttime:
                jump howlersdelltrader01waiting
            else:
                $ howlersdell_akakios_firsttime = 1
                jump howlersdelltraderfirsttime01waiting
        'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
            pass
        'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
            jump pyrrhoshowlers01insidetalkingwithpyrrhos
        'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
            jump pyrrhoshowlers01insidetalkingwithpyrrhos
        'I leave the square.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
            jump howlersdellafterinteraction

label howlersdell_sleepandrest:
    label howlersdellwakinguphall:
        show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
        show howlersdellsquareutensils 02 at basicfade
        $ howlersdell_square_fluff = "A couple of laborers eat gruel and leftovers, too sleepy to gossip. The only people who aren’t yawning are the two elderly ladies who sit on a bench, holding hands and observing the creek."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is sitting near the door, from time to time carrying out another bowl with either stew or gruel."
        $ howlersdell_square_akakios_fluff = ""
        if pyrrhos_howlersdell == 1:
            $ pyrrhos_howlersdell_fluff = ""
            if description_pyrrhos01:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
            else:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
        else:
            $ pyrrhos_howlersdell_fluff = ""
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting at one of the tables, having a conversation with a girl half her age."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if thais_afk == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        $ can_leave = 0
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        if ruinedvillage_truth and not thais_defeated:
            $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        else:
            $ renpy.music.play("audio/track_03howlersdell.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
            $ renpy.notify("The days are getting shorter.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
        menu:
            'It’s warm here, but the mouflon skin allows your back to rest a bit. You wake up a couple of times during the night. The smell of the cooked stew fuels your hunger, and the staff returns to the room once every hour or so to stir the pot. You wake up early, but leave the building to check up on {color=#f6d6bd}[horsename]{/color} and give it water from the creek.
            \n\n[howlersdell_square_eryx_fluff] [howlersdell_square_thais_fluff][pyrrhos_howlersdell_fluff]
            '
            'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
                jump howlersdelloldsailor01
            'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
                $ thais_inn = day
                jump howlersdellwaitingforthais01
            'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
                jump howlersdelltalkingtothais01
            'Thais won’t speak with me today. (disabled)' if thais_afk == day:
                pass
            'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
                if howlersdell_eryx_firsttime:
                    jump howlersdellinnkeeper01
                else:
                    $ howlersdell_eryx_firsttime = 1
                    jump howlersdellinnkeeperfirsttime01
            'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01
            '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01waiting
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01waiting
            'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump howlersdellafterinteraction

    label howlersdellafterrelaxing01:
        show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
        show howlersdellsquareutensils 04 at basicfade
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is standing behind his counter, filling mugs with beer or buttermilk, while his daughter is cleaning the tables with a wet cloth and carrying around a bucket of stream water."
        $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is packing his goods, though with no rush. He’s talking with a man who’s sewing sacks on a nearby stool."
        $ howlersdell_square_fluff = "It’s getting darker, but not much colder. More than a dozen of locals are gathered at or by the tables, playing dice or other games, drinking, eating supper, or simply chatting."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is standing near the bank, giving commands to a group of armored guards."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if pyrrhos_howlersdell == 1:
            $ pyrrhos_howlersdell_fluff = ""
            if description_pyrrhos01:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
            else:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
        else:
            $ pyrrhos_howlersdell_fluff = ""
        if thais_afk == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if pc_relax_dayof < (day-8):
            $ pc_relax_fluff = "Turns out the rest was much more necessary than you expected. Your belongings are a mess, the sacks and the blanket have too many holes to count, and you spend a good hour brushing and cleaning your mount. At the end of the day, you’re still a bit tired, but at least you feel prepared."
        elif pc_relax_dayof < (day-4):
            $ pc_relax_fluff = "You were pretty busy today, but not exhaustingly so. Taking care of your mount, as well as all the patches, scratches, bandages, and the general mess among your possessions took some reorganizing, but at the end of the day your muscles are grateful for not spending hours on riding."
        elif pc_relax_dayof < (day-2):
            $ pc_relax_fluff = "It’s been a relaxing day, but free of boredom. You spent almost an hour taking care of your mount, but at least it’s now clean and cheerful. You patch holes in your bundles to the soothing sounds of a late summer drizzle."
        else:
            $ pc_relax_fluff = "It’s been a lazy day. Repairing your equipment and taking care of your mount didn’t take nearly as much time as you'd expected, and you instead enjoy refreshing water, observe your surroundings with a clear head, wander about, and stretch out. After a few hours, you feel rather bored, but at least you have the opportunity to gather your thoughts."
        $ pc_relax_dayof = day
        label howlersdell_fluff_relaxingloop:
            $ howlersdell_fluff_relaxing = ""
            $ howlersdell_fluff_relaxing = renpy.random.choice(['For most of the time, the locals were keeping their distance, focused on their own busy days, though you had an opportunity to chit chat a bit with the elders who kept an eye on the idle kids.', 'Every now and then some of the younger locals invited you to a friendly chit-chat, asking you for the stories from the wide world.', 'At one point, a few of the workers invited you for a drink, asking you about the news from {color=#f6d6bd}Hovlavan{/color}.', 'The villagers organized some sort of druidic ritual, so the atmosphere was rather solemn. You were not invited to participate.', 'At one point a group of traders from a different village showed up, too busy to engage in small talk.', 'Before the end of your rest, a couple of guards came to you to ask what you’ve seen on the distant roads, but you couldn’t tell if any of your tales caught their attention.'])
            if howlersdell_fluff_relaxingold == howlersdell_fluff_relaxing:
                jump howlersdell_fluff_relaxingloop
            else:
                $ howlersdell_fluff_relaxingold = howlersdell_fluff_relaxing
        $ can_leave = 0
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if quarters >= (world_daylength-4) and quarters < 88 and not howlersdell_square_children_tale and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
            jump howlersdell_square_children_tale00
        menu:
            '[pc_relax_fluff] [howlersdell_fluff_relaxing]
            \n\n[howlersdell_square_fluff] [howlersdell_square_eryx_fluff] [howlersdell_square_thais_fluff][howlersdell_square_akakios_fluff][pyrrhos_howlersdell_fluff]
            '
            'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
                jump howlersdelloldsailor01
            'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
                $ thais_inn = day
                jump howlersdellwaitingforthais01
            'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
                jump howlersdelltalkingtothais01
            'Thais won’t speak with me today. (disabled)' if thais_afk == day:
                pass
            'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
                if howlersdell_eryx_firsttime:
                    jump howlersdellinnkeeper01
                else:
                    $ howlersdell_eryx_firsttime = 1
                    jump howlersdellinnkeeperfirsttime01
            'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01
            '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01waiting
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01waiting
            'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump howlersdellafterinteraction

    label howlersdellafterrelaxing02:
        show howlersdellsquareutensils 04 at basicfade
        show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
        $ randomgoodmeal = renpy.random.choice(['fresh rye bread, a sausage, a bowl of berries, and a mug of malty beer', 'a decent stew with white bread to dip', 'a fried salmon in sorrel sauce and a bowl of gruel', 'two boiled eggs, a cup of buttermilk, and some mouflon offals', 'a bowl of oatmeal based on mouflon milk, with berries, nuts, and honey', 'a fresh pie with deer meat, onions, and coriander', 'baked artichokes with a weird, but tasty, roasted lizard and a few of slices of cheese', 'an eggplant soup, a bowl of pears, and some crumbly biscuits', 'a raw cabbage head, a smoked quail wing, and a cup of yogurt', 'a pie with hare and cabbage, a bowl of plums and grapes, and a cup of mouflon milk', 'a cup of mint tisane, three chicken eggs, and baked duck meat', 'fried, breaded mushrooms with gravy, a slice of bread with butter and cheese, and chamomile tisane', 'a warm mutton stew and a cold yogurt'])
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is standing behind his counter, filling mugs with beer or buttermilk, while his daughter is cleaning the tables with a wet cloth and carrying around a bucket of stream water."
        $ howlersdell_square_akakios_fluff = "\n\n{color=#f6d6bd}The trader{/color} is packing his goods, though with no rush. He’s talking with a man who’s sewing sacks on a nearby stool."
        $ howlersdell_square_fluff = "It’s getting darker, but not much colder. More than a dozen of locals are gathered at or by the tables, playing dice or other games, drinking, eating supper, or simply chatting."
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is standing near the bank, giving commands to a group of armored guards."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if pyrrhos_howlersdell == 1:
            $ pyrrhos_howlersdell_fluff = ""
            if description_pyrrhos01:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
            else:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
        else:
            $ pyrrhos_howlersdell_fluff = ""
        if thais_afk == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if pc_relax_dayof < (day-8):
            $ pc_relax_fluff = "Turns out the rest was much more necessary than you expected. Your belongings are a mess, the sacks and the blanket have too many holes to count, and the staff spends a good hour looking after your mount. At the end of the day, one of the girls wipes the sweat from her forehead, but no soul makes excuses during their work. Not being forced to bother with any of it yourself may be the most relaxing part of this entire endeavor."
        elif pc_relax_dayof < (day-4):
            $ pc_relax_fluff = "The staff was pretty busy today, but not exhaustingly so. Taking care of your mount, as well as all the patches, scratches, bandages, and the general mess among your possessions took some reorganizing, but they finished their work before noon. Not being forced to bother with any of it yourself may be the most relaxing part of this entire endeavor."
        elif pc_relax_dayof < (day-2):
            $ pc_relax_fluff = "It’s been a relaxing day, and you didn’t give the staff that much to work with. They spent almost an hour looking after your mount, but at least it’s now clean and cheerful. There were also holes in some of your bundles, but patching and sewing them took them little time, as the they seem to be quite experienced with a needle. Your assistance wasn’t really required."
        else:
            $ pc_relax_fluff = "It’s been a lazy day. Repairing your equipment and taking care of your mount didn’t take nearly as much time as you'd expected, and the staff returned to other tasks quickly. In the meantime, you had a chance to enjoy refreshing water, observe your surroundings with a clear head, wander about, and stretch out. After a few hours, you are already quite bored, but at least you have the opportunity to gather your thoughts."
        label howlersdell_fluff_relaxingloopb:
            $ howlersdell_fluff_relaxing = ""
            $ howlersdell_fluff_relaxing = renpy.random.choice(['For most of the time, the locals were keeping their distance, focused on their own busy days, though you had an opportunity to chit chat a bit with the elders who kept an eye on the idle kids.', 'Every now and then some of the younger locals invited you to a friendly chit-chat, asking you for the stories from the wide world.', 'At one point, a few of the workers invited you for a drink, asking you about the news from {color=#f6d6bd}Hovlavan{/color}.', 'The villagers organized some sort of druidic ritual, so the atmosphere was rather solemn. You were not invited to participate.', 'At one point a group of traders from a different village showed up, too busy to engage in small talk.', 'Before the end of your rest, a couple of guards came to you to ask what you’ve seen on the distant roads, but you couldn’t tell if any of your tales caught their attention.'])
            if howlersdell_fluff_relaxingold == howlersdell_fluff_relaxing:
                jump howlersdell_fluff_relaxingloopb
            else:
                $ howlersdell_fluff_relaxingold = howlersdell_fluff_relaxing
        $ can_leave = 0
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if quarters >= (world_daylength-4) and quarters < 88 and not howlersdell_square_children_tale and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
            jump howlersdell_square_children_tale00
        menu:
            '[pc_relax_fluff] During the dinner time, you were served [randomgoodmeal]. [howlersdell_fluff_relaxing]
            \n\n[howlersdell_square_fluff] [howlersdell_square_eryx_fluff] [howlersdell_square_thais_fluff][howlersdell_square_akakios_fluff][pyrrhos_howlersdell_fluff]
            '
            'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
                jump howlersdelloldsailor01
            'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
                $ thais_inn = day
                jump howlersdellwaitingforthais01
            'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
                jump howlersdelltalkingtothais01
            'Thais won’t speak with me today. (disabled)' if thais_afk == day:
                pass
            'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
                if howlersdell_eryx_firsttime:
                    jump howlersdellinnkeeper01
                else:
                    $ howlersdell_eryx_firsttime = 1
                    jump howlersdellinnkeeperfirsttime01
            'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01
            '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01waiting
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01waiting
            'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump howlersdellafterinteraction

    label howlersdellwakinguproom:
        show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
        show howlersdellsquareutensils 02 at basicfade
        $ randomgoodmeal = renpy.random.choice(['fresh rye bread, a sausage, a bowl of berries, and a mug of malty beer', 'a decent stew with white bread to dip', 'a fried salmon in sorrel sauce and a bowl of gruel', 'two boiled eggs, a cup of buttermilk, and some mouflon offals', 'a bowl of oatmeal based on mouflon milk, with berries, nuts, and honey', 'a fresh pie with deer meat, onions, and coriander', 'baked artichokes with a weird, but tasty, roasted lizard and a few of slices of cheese', 'an eggplant soup, a bowl of pears, and some crumbly biscuits', 'a raw cabbage head, a smoked quail wing, and a cup of yogurt', 'a pie with hare and cabbage, a bowl of plums and grapes, and a cup of mouflon milk', 'a cup of mint tisane, three chicken eggs, and baked duck meat', 'fried, breaded mushrooms with gravy, a slice of bread with butter and cheese, and chamomile tisane', 'a warm mutton stew and a cold yogurt'])
        $ howlersdell_square_fluff = "A couple of laborers eat gruel and leftovers, but they don’t talk much and the general mood is slow and sleepy. The only people who don’t seem to be yawning are the two elderly ladies who sit on a bank, holding hands and observing the creek."
        $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is sitting near the door, from time to time carrying out another bowl with either stew or gruel."
        $ howlersdell_square_akakios_fluff = ""
        if pyrrhos_howlersdell == 1:
            $ pyrrhos_howlersdell_fluff = ""
            if description_pyrrhos01:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
            else:
                $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
        else:
            $ pyrrhos_howlersdell_fluff = ""
        if thais_inn == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting at one of the tables, having a conversation with a girl half her age."
        else:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        if thais_afk == day:
            $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
        $ can_leave = 0
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        if ruinedvillage_truth and not thais_defeated:
            $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        else:
            $ renpy.music.play("audio/track_03howlersdell.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
            $ renpy.notify("The days are getting shorter.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
        menu:
            'You spend the night in peace, in a clean bed, with a tightly shut window and a warm blanket. In the morning, you find a stool placed by your bed, covered with [randomgoodmeal]. Once you get dressed and go downstairs, a young boy, who’s covered in mud and speaks unusually loud and enthusiastically, mentions that {color=#f6d6bd}[horsename]{/color} has already been brushed and watered. You nod, but he runs outside without noticing it.
            \n\n[howlersdell_square_eryx_fluff] [howlersdell_square_thais_fluff][howlersdell_square_akakios_fluff][pyrrhos_howlersdell_fluff]
            '
            'I approach {color=#f6d6bd}the old sailor{/color}.' if asterion_highisland_knowsabout and not asterion_found and howlersdell_eryx_about_highisland and not howlersdell_sailor_firsttime:
                jump howlersdelloldsailor01
            'I ask a guard to look for {color=#f6d6bd}the mayor{/color}.' if thais_inn != day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask a guard to look for {color=#f6d6bd}the mayor{/color}.')
                $ thais_inn = day
                jump howlersdellwaitingforthais01
            'I head to {color=#f6d6bd}Thais{/color}, the mayor.' if thais_inn == day and not thais_afk == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the mayor.')
                jump howlersdelltalkingtothais01
            'Thais won’t speak with me today. (disabled)' if thais_afk == day:
                pass
            'I approach {color=#f6d6bd}Eryx{/color}, the innkeeper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the innkeeper.')
                if howlersdell_eryx_firsttime:
                    jump howlersdellinnkeeper01
                else:
                    $ howlersdell_eryx_firsttime = 1
                    jump howlersdellinnkeeperfirsttime01
            'I go to {color=#f6d6bd}Akakios{/color}, the trader.' ( condition="quarters >= 35 and quarters <= (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the trader.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01
            '{color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.' ( condition="quarters < 35" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}The trader{/color} is not around. I sit at a table and wait for him.')
                if howlersdell_akakios_firsttime:
                    jump howlersdelltrader01waiting
                else:
                    $ howlersdell_akakios_firsttime = 1
                    jump howlersdelltraderfirsttime01waiting
            'The trader’s stall is already closed. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I go to {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_howlersdell == 1 and description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I go to {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_howlersdell == 1 and not description_pyrrhos01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                jump pyrrhoshowlers01insidetalkingwithpyrrhos
            'I leave the square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                jump howlersdellafterinteraction

label howlersdellfirsttimeALL:
    label howlersdellfirsttimenorthALL:
        label howlersdellfirsttime01north:
            show howlersdelldarkbackground at basicfade
            show howlersdellscrap03 b at basicfade
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            if pc_hp > 3:
                $ custom1 = "You dismount smoothly, filled with vigor."
            if pc_hp > 1:
                $ custom1 = "You dismount smoothly, still having some vigor left."
            else:
                $ custom1 = "You dismount slowly, with not much vigor left."
            $ renpy.force_autosave(take_screenshot=False, block=True)
            menu:
                '{color=#f6d6bd}A young man{/color} is sitting in the shadow by the open gate. He’s young, tanned, and has a short, elegantly trimmed red beard. Beneath the green gambeson he wears an expensive tunic decorated with colorful trim. From his arm hangs a steel helmet, though the metal is so thin that it’s mostly made of wool and leather.
                \n\nHe gets up and takes the posture of a disciplined soldier, not a mercenary. He’s standing upright, with his chin up. There are two weapons on the ground, leaning on the wooden beams of the gate - an axe made of steel and a wooden club. He doesn’t reach for either.
                \n\n[custom1] {color=#f6d6bd}[horsename]{/color} holds its tail high.
                \n\nA narrow path leads south, toward two field workers - one with a hoe and one with a pitchfork. They wave to you. You can’t see their faces, but their clothes are simple - gray pants and vests, made from hemp and wool.
                '
                'I wave back. Why not.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wave back. Why not.')
                    $ howlersdell_reputation_points += 2
                    $ custom1 = "They talk for a bit, looking toward you and pointing at your mount, then walk away, disappearing behind the wall’s corner.\n\n"
                    jump howlersdellfirsttime01northb
                'It’s better to keep some distance. I just approach the guard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s better to keep some distance. I just approach the guard.')
                    $ custom1 = ""
                    jump howlersdellfirsttime01northb

        label howlersdellfirsttime01northb:
            $ description_howlersdell01 = "A prosperous village of farmers and animal breeders set on the western road."
            if not pc_firstvillage:
                $ pc_firstvillage = "howlersdell"
            menu:
                '[custom1]The guard smiles, yet avoids your eyes, and has to clear his throat before he speaks. “Welcome, traveler. If you’re ne here to make trouble, {color=#f6d6bd}Howler’s Dell{/color} welcomes you. We have the whitest flour there is.” When he bows, you realize it’s a well-practiced performance. “If it’s new garments you’re looking for, you can order everything you need right here, in all colors, shapes, en sizes. Capes, boots, vests, robes. Or, if you’re yourself a master of the needle, I can assure you we have the fabric you’re looking for.”
                \n\nHis act is over and he glances at your mount, in a moment of silence. His eyes widen.
                '
                '“This is {color=#f6d6bd}[horsename]{/color}, it helps me patrol the roads. You can pet its side, if you want, but no sudden movements.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is {color=#f6d6bd}%s{/color}. It helps me patrol the roads. You can pet its side, if you want, but no sudden movements.”' %horsename)
                    $ howlersdell_reputation_points += 3
                    menu:
                        'He follows your instructions. Even though your palfrey pays no attention to the man’s careful touch, the guard grins widely.
                        '
                        '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                            jump howlersdellfirsttime02north
                '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                    jump howlersdellfirsttime02north

        label howlersdellfirsttime02north:
            show howlersdellscrap03 a at basicfade
            show howlersdellscrap04 at basicfade
            if beholder_firsttime:
                $ custom1 = "The plant reminds you of the tree you saw in the South, next to the swamp altar."
            else:
                $ custom1 = "The plant carries no leaves, but you can’t tell if it’s truly withered."
            menu:
                '“A cityfolk, aye? The mayor is busy, but I’ll ask her. For now, come in, please. Take a look at our square!”
                \n\nIt’s not too crowded, with only a few buildings on the edges and a humming creek running west of here, through the center of the village. A large tree grows in the center, surrounded by dark water, held together by a thin wall, perfect for sitting, but the smell coming from the liquid makes you think of rotten eggs. [custom1]
                \n\nIn the north, you see the tallest building in the settlement, nicely whitewashed and very city-like. Judging by the tables, stools, and benches outside of it, it’s an inn, and it’s open for guests. The villagers, all of them tall, are chatting and dining loudly, and you catch their curious glances. On the side of this dining area, there’s a merchant’s stall - he’s currently arguing with a tall, broad-shouldered elder.
                \n\n{color=#f6d6bd}The guard{/color} closes the gate and blocks it with a wooden beam, then asks you to wait for a bit.
                '
                'I need a spot to tether {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need a spot to tether {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 10
                    menu:
                        'There’s a wide wooden roof right next to the gate that shelters carts, crates, and sacks. You move your mount next to a donkey, to a beam placed here just for this purpose. Without a moment of hesitation, {color=#f6d6bd}[horsename]{/color} starts to chew on the nearby haystack. You have some time to make sure it doesn’t struggle with your bundles.
                        \n\nWhen {color=#f6d6bd}the guard{/color} returns, he’s still alone. “She can ne come now. A friend of mine is in labor, aye? {color=#f6d6bd}The mayor{/color} wants to be there when the child arrives. But I was asked to show you the village.”
                        '
                        'I nod. “Fine.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “Fine.”')
                            show howlersdellscrap05 at basicfade
                            $ description_howlersdell06 = "It was set {i}centuries ago{/i} at the wide, but shallow Howler’s Creek."
                            menu:
                                'He takes you north, past the inn, through a narrow alley. You pass a tiny herbal garden, and a pasturage surrounded by a wooden fence, but the only animals you see around are a loose chicken and a boar tied to the building, even though you can hear the mouflon flock in the distance.
                                \n\nWithout haste, {color=#f6d6bd}the guard{/color} tells you about Howler’s Creek. It’s wide, yet shallow, gentle, and hasn’t overflowed the banks in years. Going to its source, you’d find no other settlement, so it stays clean and fresh, but there are hardly any fish in it, so only a select few are allowed to hunt for them. “We’re the cleanest village in the North!” He chuckles brightly.
                                \n\nHe walks to the ladder made of ropes and sticks, which leads to the top of the watchtower. “Come with me, traveler. The view from up there is gorgeous.”
                                '
                                'I climb after him.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb after him.')
                                    $ custom1 = ""
                                    jump howlersdellfirsttime03northa
                                'I nod and think of my knife. If it’s a trap, I’ll get him first.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and think of my knife. If it’s a trap, I’ll get him first.')
                                    $ custom1 = ", with no weapon in sight."
                                    jump howlersdellfirsttime03northa

        label howlersdellfirsttime03northa:
            menu:
                'Even though the ladder swings in all directions, {color=#f6d6bd}the guard{/color} gets to the top quickly, like a monkey climbing up creepers. You, on the other hand, need to stop and wait for the ladder to calm itself. When you join the man on the wooden platform, you’re a bit dizzy. He’s leaning on the wooden parapet, observing the area with a smile[custom1].
                '
                'I look around.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                    $ quarters += 1
                    hide howlersdellscrap03
                    hide howlersdellscrap04
                    hide howlersdellscrap05
                    hide howlersdelldarkbackground
                    show areapicture howlersdellfull at basicfade
                    $ description_howlersdell06a = "The locals are proud of their wealth and the goods they have to sell."
                    if quarters < (world_daylength-4):
                        $ custom1 = "sunlight"
                    else:
                        $ custom1 = "moonlight"
                    menu:
                        '“See? The’s nae place like {color=#f6d6bd}Howler’s Dell{/color}.” {color=#f6d6bd}The guard{/color} starts to point in all sorts of directions, giving you no time to contemplate. For the next few minutes, he describes the fields and their crops; the flocks in the pastures and the shepherds inspecting the fences; the ancient garden of trees and bushes, larger than the village itself; the [custom1] dancing on the stream to its own tune. If you were to believe everything he describes, this place has access to everything in abundance. The “sweetest” honey, the “most fragrant” bread, the “softest” wool. “En the beer? ‘Tis excellent!”
                        \n\nHe sounds like a city merchant who’s trying to sell an old house.
                        '
                        'What an annoying kid. Near {color=#f6d6bd}Hovlavan{/color}, you could find five larger and richer settlements in less than two days.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- What an annoying kid. Near {color=#f6d6bd}Hovlavan{/color}, you could find five larger and richer settlements in less than two days.')
                            jump howlersdellfirsttime04northb
                        'No wonder he’s so proud, why wouldn’t he be? They’ve tamed this scrap of land and live in comfort.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No wonder he’s so proud, why wouldn’t he be? They’ve tamed this scrap of land and live in comfort.')
                            jump howlersdellfirsttime04northb

        label howlersdellfirsttime04northb:
            $ description_howlersdell08 = "The inn placed at the village square is named {color=#f6d6bd}Ape Ale{/color}."
            menu:
                'The islet in the middle connects both parts of the village. There are three gates, though according to him, the northern one is hardly ever opened and “leads pretty much naewhere.” You’ve already seen the {color=#f6d6bd}Ape Ale inn{/color}, where you can find “a bed en victuals, en the’s the stall where {color=#f6d6bd}Akakios{/color} rewards our work, at least as long as we don’t annoy him with pointless talk.” He laughs briefly.
                \n\nOn the opposite side of the creek, there’s another white house - it belongs to “{color=#f6d6bd}Bion{/color}, the best clothier in the North.” The priests live in the southeast, near the wall, but “they do ne talk to strangers.” You also hear about the hunter, the cooper, the fisher, the miller. The piemaker lives with his sister, the baker. The smith and her husband, the carpenter, live with their kids...
                \n\nSome of the larger buildings could accommodate two, maybe even three generations at once. There could be more than a hundred dwellers here.
                \n\nYou consider stopping his speech, but he suddenly points at the islet again. “There, see? The mayor’s coming, the one wearing purple. You’re free to join her, traveler.”
                '
                'I nod and climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and climb down.')
                    show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
                    show howlersdellsquareutensils 02 at basicfade
                    menu:
                        'You try to get down quickly, but two steps are enough to make it clear that it’s a bad idea. You wait for the ladder to find its balance. You’re relieved when you touch the ground again.
                        \n\nThe tables in front of the inn are now crowded. The people on stools talk to each other loud enough to help the lone trader hear them. An old man is sitting by himself, eating a pie, with a walking stick leaning against the table. A young woman is cleaning empty mugs in the creek, speaking with a man at least twice her age, maybe her father.
                        '
                        'I look for the mayor and approach her.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the mayor and approach her.')
                            jump howlersdellfirsttimewiththais01

    ########################################################
    label howlersdellfirsttimesouthALL:
        label howlersdellfirsttime01south:
            show howlersdelldarkbackground at basicfade
            show howlersdellscrap01 at basicfade
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=False, block=True)
            menu:
                'The beaten road serves your palfrey well. The forest to your left becomes sparse and brighter and there are dozens of human-made paths among the fruit-bearing trees. On your right, there’s a large pasture, with at least a dozen massive mouflons. Two of them, already sheared, look comically small. Soon after that, you ride alongside vast, flourishing fields filled with rye, still green, preparing itself patiently for the second harvest.
                \n\nThe path ends with a massive wooden gate. The stone wall, separating you from the glow of lights behind it, isn’t as tall as the roofs, but you can’t imagine climbing to its top. There are pretty much no cracks, no missing bricks, a sign of many hours of labor, especially considering how massive the settlement is, as wide as a city district.
                \n\nThe birds and monkeys are now just a distant echo, replaced with the sounds of carts, running, hammers, saws, laughter, and shouts.
                '
                'Finally. Maybe I can rest here.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally. Maybe I can rest here.')
                    jump howlersdellfirsttime01southa
                '*sigh* I don’t feel comfortable in large settlements. Let’s get this over with.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- *sigh* I don’t feel comfortable in large settlements. Let’s get this over with.')
                    jump howlersdellfirsttime01southa

        label howlersdellfirsttime01southa:
            if pc_hp > 3:
                $ custom1 = "You dismount smoothly, filled with vigor."
            if pc_hp > 1:
                $ custom1 = "You dismount smoothly, still having some vigor left."
            else:
                $ custom1 = "You dismount slowly, with not much vigor left."
            menu:
                '{color=#f6d6bd}A young man{/color} is leaning against the closed gate, covered by its shadow. He’s young, tanned, and has a short, elegantly trimmed red beard. Beneath the green gambeson he wears an expensive tunic decorated with colorful trim. From his arm hangs a steel helmet, though the metal is so thin that it’s mostly made of wool and leather.
                \n\nHe moves into the light and takes on the posture of a disciplined soldier, not a mercenary. He’s standing upright, with his chin up. There are two weapons on the ground, leaning on the wooden beams of the gate - an axe made of steel and a wooden club. He doesn’t reach for either.
                \n\n[custom1] {color=#f6d6bd}[horsename]{/color} holds its tail high.
                \n\nA narrow path leads north, toward two field workers - one with a hoe and one with a pitchfork. They wave to you. You can’t see their faces, but their clothes are simple - gray pants and vests, made from hemp and wool.
                '
                'I wave back. Why not.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wave back. Why not.')
                    $ howlersdell_reputation_points += 3
                    $ custom1 = "They talk for a bit, looking toward you and pointing at your mount, then walk away, disappearing behind the wall’s corner.\n\n"
                    jump howlersdellfirsttime01southb
                'It’s better to keep some distance. I just approach the guard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s better to keep some distance. I just approach the guard.')
                    $ custom1 = ""
                    jump howlersdellfirsttime01southb

        label howlersdellfirsttime01southb:
            $ description_howlersdell01 = "A prosperous village of farmers and animal breeders set on the western road."
            if not pc_firstvillage:
                $ pc_firstvillage = "howlersdell"
            menu:
                '[custom1]The guard smiles, yet avoids your eyes, and has to clear his throat before he speaks. “Welcome, traveler. If you’re ne here to make trouble, {color=#f6d6bd}Howler’s Dell{/color} welcomes you. We have the whitest flour there is.” When he bows, you realize it’s a well-practiced performance. “If it’s new garments you’re looking for, you can order everything you need right here, in all colors, shapes, en sizes. Capes, boots, vests, robes. Or, if you’re yourself a master of the needle, I can assure you we have the fabric you’re looking for.”
                \n\nHis act is over and he glances at your mount in a moment of silence. His eyes get wider as he observes it with a child-like fascination.
                '
                '“This is {color=#f6d6bd}[horsename]{/color}, it helps me patrol the roads. You can pet its side, if you want, but no sudden movements.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is {color=#f6d6bd}%s{/color}. It helps me patrol the roads. You can pet its side, if you want, but no sudden movements.”' %horsename)
                    $ howlersdell_reputation_points += 3
                    menu:
                        'He follows your instructions. Even though your palfrey pays no attention to the man’s careful touch, the guard grins widely.
                        '
                        '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                            jump howlersdellfirsttime02south
                '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                    jump howlersdellfirsttime02south

        label howlersdellfirsttime02south:
            show howlersdellscrap02 at basicfade
            menu:
                '“A cityfolk, aye? {color=#f6d6bd}The mayor{/color} is busy, but I’ll ask her. Give us a moment to let you in.” He knocks at the gate, which is then pulled inwards by two other guards, a man and a woman, wearing their own gambesons - similarly green, but tailor-made to match their figures.
                \n\nThe nearby buildings are simple houses made of wooden beams and covered with thatch, while the store house is even more modest, with a roof made of planks. The watchtower has a ladder made of ropes and sticks, no stairs.
                \n\n“Just give me a moment!” {color=#f6d6bd}The guard{/color} strides away before he finishes the last word. The others close the gate behind you and observe your mount carefully. Your eyes run east, to a humming creek running through the center of the village
                '
                'I wait for the return of the messenger.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the return of the messenger.')
                    $ description_howlersdell06 = "It was set {i}centuries ago{/i} at the wide, but shallow, Howler’s Creek."
                    $ minutes += 5
                    menu:
                        '“Calming sound, aye? Tha’s Howler’s Creek.” {color=#f6d6bd}The guard{/color}, like most of the locals, is taller than you. “Wide, but shallow, there’s ne been a flood in years. Pa told me there used to be nae bridges - neighbors crossed it with their boots in their hands. En ‘tis clean like a raindrop, but there are ne many fish.”
                        \n\n“We’re the cleanest village in the North!” Her companion chuckles brightly.
                        \n\nWhen {color=#f6d6bd}the guard{/color} returns, he’s still alone. “She can ne come now. A friend of mine is in labor, aye? {color=#f6d6bd}The mayor{/color} wants to be there when the child arrives. But I was asked to show you the village.”
                        '
                        'I nod. “Fine.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “Fine.”')
                            menu:
                                'He approaches the watchtower. “Tie your mount here, we’ll keep the kids away. Most of the neighbors are getting ready to celebrate!”
                                \n\nOnce you’re done, he grabs the rope ladder. “The view from up there is gorgeous.”
                                '
                                'I climb after him.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb after him.')
                                    $ custom1 = ""
                                    jump howlersdellfirsttime03southa
                                'I nod and think of my knife. If it’s a trap, I’ll get him first.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and think of my knife. If it’s a trap, I’ll get him first.')
                                    $ custom1 = ", with no weapon in sight."
                                    jump howlersdellfirsttime03southa

        label howlersdellfirsttime03southa:
            menu:
                'Even though the ladder swings in all directions, {color=#f6d6bd}the guard{/color} gets to the top quickly, like a monkey climbing up creepers. You, on the other hand, need to stop and wait for the ladder to calm itself. When you join the man on the wooden platform, you’re a bit dizzy. He’s leaning on the wooden parapet, observing the area with a smile[custom1].
                '
                'I look around.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                    $ quarters += 1
                    hide howlersdellscrap01
                    hide howlersdellscrap02
                    hide howlersdelldarkbackground
                    show areapicture howlersdellfull at basicfade
                    $ description_howlersdell06a = "The locals are proud of their wealth and the goods they have to sell."
                    if quarters < (world_daylength-4):
                        $ custom1 = "sunlight"
                    else:
                        $ custom1 = "moonlight"
                    menu:
                        '“See? The’s nae place like {color=#f6d6bd}Howler’s Dell{/color}.” {color=#f6d6bd}The guard{/color} points in every direction, giving you no time to contemplate. For the next few minutes, he describes the fields and their crops; the flocks in the pastures and the shepherds inspecting the fences; the ancient garden of trees and bushes, larger than the village itself; the [custom1] dancing on the stream to its own tune. If you are to believe everything he describes, this place has access to everything in abundance. The “sweetest” honey, the “most fragrant” bread, the “softest” wool. “En the beer? ‘Tis excellent!”
                        \n\nHe sounds like a city merchant who’s trying to sell an old house.
                        '
                        'What an annoying kid. Near {color=#f6d6bd}Hovlavan{/color}, you could find five larger and richer settlements in less than two days.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- What an annoying kid. Near {color=#f6d6bd}Hovlavan{/color}, you could find five larger and richer settlements in less than two days.')
                            jump howlersdellfirsttime04southb
                        'No wonder he’s so proud, why wouldn’t he be? They’ve tamed this scrap of land and live in comfort.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No wonder he’s so proud, why wouldn’t he be? They’ve tamed this scrap of land and live in comfort.')
                            jump howlersdellfirsttime04southb

        label howlersdellfirsttime04southb:
            $ description_howlersdell08 = "The inn placed at the village square is named {color=#f6d6bd}Ape Ale{/color}."
            menu:
                'The islet in the middle connects both parts of the village. According to the man, the northern gate is hardly ever opened, as it “leads naewhere now.” Near the eastern gate, there’s {color=#f6d6bd}the Ape Ale inn{/color}, where you can find “a bed en victuals. En the’s the stall where {color=#f6d6bd}Akakios{/color} rewards our work, unless we annoy him with pointless talk,” he lets out a chuckle.
                \n\nOn the opposite side of the creek, there’s another white house - it belongs to “{color=#f6d6bd}Bion{/color}, the best clothier in the North.” The priests live in the southeast, near the wall, but “they do ne talk to strangers.” You also hear about the hunter, the cooper, the fisher, the miller. The piemaker lives with his sister, the baker. The smith and her husband, the carpenter, live with their kids...
                \n\nSome of the larger buildings could accommodate two, maybe even three generations at once. There could be more than a hundred dwellers here.
                \n\nYou consider stopping his speech, but he suddenly points at the islet again. “There, see? The mayor’s coming, the one wearing purple. You’re free to join her, traveler.”
                '
                'I nod and climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and climb down.')
                    $ quarters += 1
                    menu:
                        'You try to get down quickly, but two steps are enough to make you sure that it’s a bad idea. You wait for the ladder to find its balance. You’re relieved when you touch the ground again.
                        \n\nYou untie your palfrey and follow {color=#f6d6bd}the guard{/color}. You pass a small pasturage, surrounded by a wooden fence, a few loose chickens, and a tethered boar. The fancier buildings are covered with whitewash coating, and surrounded with vegetables, herbs, and flowers.
                        \n\nThe bridges are wide enough to carry even a wagon, but for {color=#f6d6bd}[horsename]{/color} walking on the wooden beams is far from pleasant. The islet is empty, but you notice an empty stall, painted with the shapes of colorful flowers.
                        '
                        'I walk over the second bridge.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk over the second bridge.')
                            jump howlersdellfirsttime05south

        label howlersdellfirsttime05south:
            $ quarters += 1
            if beholder_firsttime:
                $ custom1 = "The plant reminds you of the tree you saw in the South, next to the swamp altar."
            else:
                $ custom1 = "The plant carries no leaves, but you can’t tell if it’s truly withered."
            menu:
                'Along the entire path, you notice more and more people, observing you, smiling, or casually greeting you as they’re focused on their own tasks. Finally, you reach the main square. A large tree grows in the center, surrounded by dark water, held together by a thin wall, perfect for sitting, but the smell coming from the liquid makes you think of rotten eggs. [custom1]
                \n\nIn the north, you see the Ape Ale inn. Judging by the tables, stools, and benches outside of it, it’s open for guests. The villagers are chatting and dining loudly, and you catch their curious glances. On the side of the dining area, the merchant is arguing with a tall, broad-shouldered worker. An old man is sitting by himself, eating a pie, with a walking stick leaning against the table. A young woman is cleaning the empty mugs in the creek, speaking with a man at least twice her age, maybe her father.
                '
                'I need a spot to tether {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need a spot to tether {color=#f6d6bd}%s{/color}.' %horsename)
                    show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
                    show howlersdellsquareutensils 02 at basicfade
                    menu:
                        'There’s a wide wooden roof right next to the gate that shelters carts, crates, and sacks. You move your mount next to a donkey, to a beam placed here just for this purpose. Without a moment of hesitation, {color=#f6d6bd}[horsename]{/color} starts to chew on the nearby haystack. You have some time to make sure it doesn’t struggle with your bundles.
                        \n\nYou return to the inn.
                        '
                        'I look for the mayor and approach her.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the mayor and approach her.')
                            jump howlersdellfirsttimewiththais01

    ########################################################
    label howlersdellfirsttimenightattackALL:
        label howlersdellfirsttimeALT01north:
            show howlersdelldarkbackground at basicfade
            show howlersdellscrap03 darka at basicfade
            show howlersdellscrap04 dark at basicfade
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=False, block=True)
            menu:
                'You ride through the open gate, finding armed and armored guards who are holding lit lanterns. {color=#f6d6bd}A young man{/color} approaches you while you’re still in the saddle. He’s tanned and has a short, elegantly trimmed red beard. Beneath the green gambeson he wears an expensive tunic decorated with colorful trim. From his arm hangs a steel helmet, though the metal is so thin that it’s mostly made of wool and leather.
                \n\nHis companions close the gate and block it with a few beams. He’s standing upright, with his chin up. He has an axe made of steel and a wooden club, but doesn’t reach for either.
                \n\n{color=#f6d6bd}[horsename]{/color} holds its tail low, exhausted and wounded.
                '
                'I dismount slowly, with not much strength left.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount slowly, with not much strength left.')
                    $ description_howlersdell01 = "A prosperous village of farmers and animal breeders set on the western road."
                    if not pc_firstvillage:
                        $ pc_firstvillage = "howlersdell"
                    menu:
                        '“I’m sorry to see you in a time of need, stranger. If you’re ne here to make trouble, {color=#f6d6bd}Howler’s Dell{/color} welcomes you, en is happy to give you shelter. We have the whitest flour there is,” he bows to you slightly. His memorized invitation has marked his soul so that it overcomes the unusual situation you find yourselves in. “If it’s new garments you’re looking for, you can order everything you need right here, in all colors, shapes, en sizes. Capes, boots, vests, robes. Or, if you’re yourself a master of the needle, I can assure you we have the fabric you’re looking for.”
                        \n\nHis act is over and he glances at your mount, in a moment of silence. His eyes widen.
                        '
                        '“Thank you for saving my life. This is {color=#f6d6bd}[horsename]{/color}. It helps me patrol the roads.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for saving my life. This is {color=#f6d6bd}%s{/color}. It helps me patrol the roads.”' %horsename)
                            $ howlersdell_reputation_points += 3
                            menu:
                                '“‘Tis ne a problem,” he says with a smile, but also a hint of respect. “We’ll prepare the stables for the poor beast. En enough hay for it to fill its stomach.”
                                '
                                '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                                    jump howlersdellfirsttimeALT02north
                        '“I’m [pcname], your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, your new roadwarden. I want to see your {color=#f6d6bd}mayor{/color}.”' %pcname)
                            jump howlersdellfirsttimeALT02north

        label howlersdellfirsttimeALT02north:
            if beholder_firsttime:
                $ custom1 = "The plant reminds you of the tree you saw in the South, next to the swamp altar."
            else:
                $ custom1 = "The plant carries no leaves, but you can’t tell if it’s truly withered."
            menu:
                '“A cityfolk, aye? The mayor is resting, you’ll have to wait till the morning. For now, follow me to the stables, please!”
                \n\nA humming creek runs west of here, through the center of the village. The square of the village is lit much better than the nearby alleys. A large tree grows in the center, surrounded by dark water, held together by a thin wall, perfect for sitting, but the smell coming from the liquid makes you think of rotten eggs. [custom1]
                \n\nThere’s hardly a soul around. In the north, you see the tallest building in the settlement, nicely whitewashed and very city-like. There is one table outside of it, from which two villagers are observing you from above their mugs.
                '
                'I follow the guard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the guard.')
                    $ minutes += 10
                    menu:
                        'There’s a wide wooden roof right next to the gate that shelters carts, crates, and sacks. You move your mount next to a donkey, to a beam placed here just for this purpose. Without a moment of hesitation, {color=#f6d6bd}[horsename]{/color} starts to chew on the nearby haystack. You have some time to make sure it doesn’t struggle with your bundles.
                        \n\nOnce you’re done, {color=#f6d6bd}the guard{/color} leads you to the largest building, which turns out to be an inn. You’re so tired you struggle to speak. Someone helps you climb the stairs and leads you to a couple of furs placed on the floor in a warm corner. They move to take off your boots and clothes - at first you protest, but you lose consciousness soon after that.
                        '
                        'If they rob me now, I’ll be so pissed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- If they rob me now, I’ll be so pissed.')
                            $ can_leave = 0
                            $ can_rest = 0
                            $ can_items = 0
                            $ questionpreset = 0
                            if item_asterioncloak:
                                $ quarters = 34
                                if pc_food >= 2:
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    $ mana = limit_mana(mana+3)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
                            else:
                                $ quarters = 38
                                if pc_food >= 2:
                                    $ pc_hp = limit_pc_hp(pc_hp+0)
                                    $ mana = limit_mana(mana+2)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                            $ pc_food = limit_pc_food(pc_food-2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            $ howlersdell_square_fluff = "A couple of laborers eat gruel and leftovers, too sleepy to gossip. The only people who aren’t yawning are the two elderly ladies who sit on a bench, holding hands and observing the creek."
                            $ howlersdell_square_eryx_fluff = "{color=#f6d6bd}The innkeeper{/color} is sitting near the door, from time to time carrying out another bowl with either stew or gruel."
                            $ howlersdell_square_akakios_fluff = ""
                            if pyrrhos_howlersdell == 1:
                                $ pyrrhos_howlersdell_fluff = ""
                                if description_pyrrhos01:
                                    $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square. '])
                                else:
                                    $ pyrrhos_howlersdell_fluff = renpy.random.choice(['\n\n{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting on a bench near the creek bank, apparently napping, though he winks at you when he catches your glance.', '\n\n{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating gruel from a bowl.', '\n\n{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you reach the square.'])
                            else:
                                $ pyrrhos_howlersdell_fluff = ""
                            if thais_inn == day:
                                $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is sitting at one of the tables, having a conversation with a girl half her age."
                            else:
                                $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
                            if thais_afk == day:
                                $ howlersdell_square_thais_fluff = "{color=#f6d6bd}Thais{/color} is nowhere to be seen."
                            hide howlersdellscrap03
                            hide howlersdellscrap04
                            show howlersdelldarkbackground at basicfade
                            show howlersdellscrap03 a at basicfade
                            show howlersdellscrap04 at basicfade
                            nvl clear
                            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                            if day >= world_deadline-1:
                                $ world_endmode_howlers = 1
                                jump sleeping
                            else:
                                $ day += 1
                            menu:
                                'You wake up with bandages on your wounds and your clothes piled up nearby. You put them on slowly - you’re stiff, but you don’t feel pain. Judging by the sun and the noise outside, it’s late.
                                \n\n{color=#f6d6bd}The guard{/color} that spoke with you during the night clears his throat, drawing your attention. “Welcome again. {color=#f6d6bd}The mayor{/color} can ne come now. A friend of mine is in labor, en she wants to be there when the child arrives. But I was asked to show you the village.”
                                '
                                'I nod. “Fine.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “Fine.”')
                                    jump howlersdellfirsttimeALT03north
                                'I point at my bandaged stomach. “Do I pay for this...?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point at my bandaged stomach. “Do I pay for this...?”')
                                    $ howlersdell_reputation_points += 3
                                    menu:
                                        '“Do ne mention it. This one is out of the kindness of our forest speakers. Come, come. You should move your legs and arms for bit.”
                                        '
                                        'I nod. “Fine.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “Fine.”')
                                            jump howlersdellfirsttimeALT03north

        label howlersdellfirsttimeALT03north:
            show howlersdellscrap05 at basicfade
            $ description_howlersdell06 = "It was set {i}centuries ago{/i} at the wide, but shallow Howler’s Creek."
            menu:
                'Your head is still spinning a bit, but not for long. {color=#f6d6bd}The guard{/color} takes you north, past the inn, through a narrow alley. You pass a tiny herbal garden, and a pasturage surrounded by a wooden fence, but the only animals you see around are a loose chicken and a boar tied to the building, even though you can hear the mouflon flock in the distance.
                \n\nWithout haste, he tells you about Howler’s Creek. It’s wide, yet shallow, gentle, and hasn’t overflowed the banks in years. Going to its source, you’d find no other settlement, so it stays clean and fresh, but there are hardly any fish in it, so only a select few are allowed to hunt for them. “We’re the cleanest village in the North!” He chuckles brightly.
                \n\nHe walks to the ladder made of ropes and sticks, which leads to the top of the watchtower. “The view from up there is gorgeous.”
                '
                'My arms are a bit weak, but I climb after him.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My arms are a bit weak, but I climb after him.')
                    menu:
                        'Even though the ladder swings in all directions, {color=#f6d6bd}the guard{/color} gets to the top quickly, like a monkey climbing up creepers. You, on the other hand, need to stop and wait for the ladder to calm itself. When you join the man on the wooden platform, you’re a bit dizzy. He’s leaning on the wooden parapet, observing the area with a smile.
                        '
                        'I look around.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                            $ quarters += 1
                            hide howlersdellscrap03
                            hide howlersdellscrap04
                            hide howlersdellscrap05
                            hide howlersdelldarkbackground
                            show areapicture howlersdellfull at basicfade
                            $ description_howlersdell06a = "The locals are proud of their wealth and the goods they have to sell."
                            if quarters < (world_daylength-4):
                                $ custom1 = "sunlight"
                            else:
                                $ custom1 = "moonlight"
                            menu:
                                '“See? The’s nae place like {color=#f6d6bd}Howler’s Dell{/color}.” {color=#f6d6bd}The guard{/color} starts to point in every direction, giving you no time to contemplate. For the next few minutes, he describes the fields and their crops; the flocks on the pastures and the shepherds inspecting the fences; the ancient garden of trees and bushes, larger than the village itself; the [custom1] dancing on the stream to its own tune. If you were to believe everything he describes, this place has access to everything in abundance. The “sweetest” honey, the “most fragrant” bread, the “softest” wool. “En the beer? ‘Tis excellent!”
                                \n\nHe sounds like a city merchant who’s trying to sell an old house.
                                '
                                'What an annoying kid. He could find five richer settlements in less than two days near {color=#f6d6bd}Hovlavan{/color}.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What an annoying kid. He could find five richer settlements in less than two days near {color=#f6d6bd}Hovlavan{/color}.')
                                    jump howlersdellfirsttimeALT04northb
                                'No wonder he’s so proud. They’ve tamed this scrap of land and live in comfort.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- No wonder he’s so proud. They’ve tamed this scrap of land and live in comfort.')
                                    jump howlersdellfirsttimeALT04northb

        label howlersdellfirsttimeALT04northb:
            $ description_howlersdell08 = "The inn placed at the village square is named {color=#f6d6bd}Ape Ale{/color}."
            menu:
                'The islet in the middle connects both parts of the village. There are three gates, though according to him, the northern one is hardly ever opened and “leads pretty much naewhere.” You’ve already seen the {color=#f6d6bd}Ape Ale inn{/color}, where you can find “a bed en victuals, en the’s the stall where {color=#f6d6bd}Akakios{/color} rewards our work, at least as long as we don’t annoy him with pointless talks.” He laughs briefly.
                \n\nOn the opposite side of the creek, there’s another white house - it belongs to “{color=#f6d6bd}Bion{/color} the best clothier in the North.” The priests live in the southeast, near the wall, but “they do ne talk to strangers.” You also hear about the hunter, the cooper, the fisher, the miller. The piemaker lives with his sister, the baker. The smith and her husband, the carpenter, live with their kids...
                \n\nSome of the larger buildings could accommodate two, maybe even three generations at once. There could be more than a hundred dwellers here.
                \n\nYou consider stopping his speech, but he suddenly points at the islet again. “There, see? The mayor’s coming, the one wearing purple. You’re free to join her, traveler.”
                '
                'I nod and climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and climb down.')
                    show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
                    show howlersdellsquareutensils 02 at basicfade
                    menu:
                        'You try to get down quickly, but two steps are enough to make it clear that it’s a bad idea. You wait for the ladder to find its balance. You’re relieved when you touch the ground again.
                        \n\nThe tables in front of the inn are now crowded. The people on stools talk to each other loud enough to help the lone trader hear them. An old man is sitting by himself, eating a pie, with a walking stick leaning against the table. A young woman is cleaning empty mugs in the creek, speaking with a man at least twice her age, maybe her father.
                        '
                        'I look for the mayor and approach her.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the mayor and approach her.')
                            jump howlersdellfirsttimewiththais01

label howlersdellinstalingrodALL:
    label howlersdellinstalingrodwithpermission01:
        menu:
            'You approach the same tower you’ve climbed before. There’s {color=#f6d6bd}a teenage girl{/color} crouching on the bank of the creek, washing laundry and bowls. With a smile, she offers to hold the rope ladder for you.
            '
            '“I don’t need help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need help.”')
                jump howlersdellinstalingrodwithpermission01a
            'I accept.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I accept.')
                jump howlersdellinstalingrodwithpermission01b

    label howlersdellinstalingrodwithpermission01a:
        $ quarters += 3
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ eudocia_bronzerod_rodin_howlersdell = 1
        $ item_bronzerod -= 1
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
            'She shrugs and turns away. You climb to the top, hoping that no soul sees you struggle when the wind gets stronger.
            \n\nIt takes you a fair bit of time, but with a couple of cords you attach the rod to the outer wall. You make sure that even a strong push won’t make it fall down.
            \n\nOnce you touch the ground, the girl gives you a bashfull glance, but doesn’t say anything.
            '
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump howlersdellafterinteraction

    label howlersdellinstalingrodwithpermission01b:
        $ quarters += 2
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ eudocia_bronzerod_rodin_howlersdell = 1
        $ item_bronzerod -= 1
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
            'She puts on her sandals and approaches the ladder. “Go ahead!” She keeps it still as you climb to the top. Even when the wind gets stronger, you feel in control.
            \n\nIt takes you a fair bit of time, but with a couple of cords you attach the rod to the outer wall. You make sure that even a strong push won’t make it fall down.
            \n\nOnce you touch the ground, the girl doesn’t walk up to you, but tries to make eye contact. “The’s a nice view from there, aye? Young kids, this tall,” she holds her hand near her waist, “always climb up when ne soul is watching.”
            \n\nHer kind smile contrasts with her bored, indifferent eyes.
            '
            '“I’m busy.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m busy.”')
                jump howlersdellinstalingrodwithpermission01c
            'Some chit-chat won’t hurt me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Some chit-chat won’t hurt me.')
                $ howlersdell_rumor_counter += 1
                jump howlersdellinstalingrodwithpermission01d

    label howlersdellinstalingrodwithpermission01c:
        menu:
            'She scoffs and walks back to the creek.
            '
            'I also walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I also walk away.')
                jump howlersdellafterinteraction

    label howlersdellinstalingrodwithpermission01d:
        $ description_druids04 = "To show them due respect, one should be humble and penitent, respect their efforts, and address them as {i}forest speakers{/i}."
        $ quarters += 1
        $ howlersdell_reputation_points += 3
        menu:
            'She craves any tales from the outside world. You tell her about {color=#f6d6bd}[horsename]{/color} and the hardships of your travels, while she tells you about her magical talents - she can “make water clean”, and hopes to put it to use once she gets more experienced with it. “I do ne get all the power-hungry sorcerers, you know? Why would one throw fire from their hands while their spoons need to get clean?”
            \n\nShe also mentions the strict rigor followed by the local druids. They take on the responsibility of teaching new generations how to live side-by-side with the woods. Because of this, “they’re like our other parents, you see, with their own rules en tasks, but aren’t so cranky if we speak to them humbly, like their own kids. It may be weird for an outsider,” she says with a smile, “but they are ne some mages of Wright, but our forest speakers.”
            \n\nSoon after that, she bids you farewell, stretching her arms and back, and returns to the wet clothes.
            '
            'I also walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I also walk away.')
                jump howlersdellafterinteraction

label howlersdell_elpis_returningfromhamletALL:
    label howlersdell_elpis_returningfromhamlet01:
        show areapicture howlersdelltorockslide at basicfade
        $ howlersdell_elpis_firsttime_theywant = 1
        $ rockslide_workers_druids = 1
        $ world_known_npcs += 1
        $ can_leave = 0
        $ can_rest = 0
        $ quarters -= 2
        $ can_items = 0
        $ howlersdell_reputation += 1
        nvl clear
        with Fade(1.0, 0.5, 1.0, color="#0f2a3f")
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'A group of harpies follows your steps, but after half an hour they give up on you, seeing that you remain in large numbers. Your return trip is safe and the workers cheer up quickly.
            '
            'I keep an eye on our surroundings. Just in case.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep an eye on our surroundings. Just in case.')
                show areapicture howlersdellfull at basicfade
                $ thais_inn = day
                $ quarters += 2
                nvl clear
                with Fade(1.0, 0.5, 1.0, color="#0f2a3f")
                menu:
                    'Your loud expedition gets noticed long before you reach the gates, and the villagers gather by the open gate. The parents welcome their children, the siblings and friends mock the presumed cowardice of their equals, and the kids ask for stories. For many of the members of your group, it was the first time that they truly left their homes.
                    '
                    'Since no soul approaches me, I ride through the empty village and lead {color=#f6d6bd}[horsename]{/color} to the stables.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since no soul approaches me, I ride through the empty village and lead {color=#f6d6bd}%s{/color} to the stables.' %horsename)
                        if howlersdell_elpis_firsttime:
                            menu:
                                'As you’re crossing the first bridge, {color=#f6d6bd}a guard{/color} greets you with a smile. “{color=#f6d6bd}Our mayor{/color} will wait for you in the usual spot. She’s glad to see that you’re safe.”
                                \n\nYou lead your mount to the haystack and as you loosen up the saddle, yet another person shows up behind you. This time, it’s {color=#f6d6bd}the man with a large club{/color} whom you previously met on your path to the priests, though this time he’s wearing sandals.
                                \n\n“You’re summoned by {color=#f6d6bd}Elpis{/color}, the speaker of the forest,” he states solemnly. “En you should see her right away.”
                                '
                                '“And why is that?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And why is that?”')
                                    $ custom1 = "“‘Tis ne me who they call. But ‘tis urgent. Do ne make them wait.”\n\nHe turns away and heads south, with his club leaning against his shoulder."
                                    jump howlersdell_elpis_returningfromhamlet03
                                '“And what if I won’t?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if I won’t?”')
                                    $ custom1 = "“Then naething,” he shrugs. “But if you hope to one day seek their advice, you better be ready to offer them your time.”\n\nHe turns away and heads south, swinging his club as if he’s aiming at invisible quails."
                                    jump howlersdell_elpis_returningfromhamlet03
                                '“I’ll be there right away.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be there right away.”')
                                    $ custom1 = "He nods. “We’ll see, traveler. We’ll see.” He turns away and heads south."
                                    jump howlersdell_elpis_returningfromhamlet03
                        else:
                            $ howlersdell_elpis_firsttime_spokewithguardfishhamlet = 1
                            menu:
                                'As you’re crossing the first bridge, {color=#f6d6bd}a guard{/color} greets you with a smile. “{color=#f6d6bd}Our mayor{/color} will wait for you in the usual spot. She’s glad to see that you’re safe.”
                                \n\nYou lead your mount to the haystack and as you loosen up the saddle, yet another person shows up behind you. This time, it’s {color=#f6d6bd}a large man{/color} close to his fifties, taller than most people you’ve seen in your life, and broad shouldered. His hair and short beard are brown, matching his elegant woolen robe. A thick club is attached to his right wrist with a leather strap.
                                \n\n“You’re summoned by {color=#f6d6bd}Elpis{/color}, the speaker of the forest,” he states solemnly. “En you should see them right away.”
                                '
                                '“And why is that?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And why is that?”')
                                    $ custom1 = "“‘Tis ne me who they call. But ‘tis urgent. Do ne make them wait.”\n\nHe turns away and heads south, with his club leaning against his shoulder."
                                    jump howlersdell_elpis_returningfromhamlet03
                                '“And what if I won’t?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if I won’t?”')
                                    $ custom1 = "“Then naething,” he shrugs. “But if you hope to one day seek their advice, you better be ready to offer them your time.”\n\nHe turns away and heads south, swinging his club as if he’s aiming at invisible quails."
                                    jump howlersdell_elpis_returningfromhamlet03
                                '“I’ll be there right away.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be there right away.”')
                                    $ custom1 = "He nods. “We’ll see, traveler. We’ll see.” He turns away and heads south."
                                    jump howlersdell_elpis_returningfromhamlet03

    label howlersdell_elpis_returningfromhamlet03:
        $ can_leave = 1
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            \n\nFinally alone, you’re left standing near the main square.
            '
            'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                jump howlersdell_steephouseconfrontation00
            'I go to the main square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                jump howlersdellsquareregular01
            'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                jump howlersdell_erastos01
            'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                if howlersdell_bion_firsttime:
                    jump howlersdelltailor01
                else:
                    jump howlersdelltailorfirsttime01
            'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                pass
            'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                if howlersdell_elpis_firsttime_theywant:
                    jump howlersdelldruids01yes
                else:
                    jump howlersdelldruids01no
            'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                pass
            'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                jump howlersdelldruids01yes
            'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                jump howlersdelldruids01
            'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                jump howlersdellsinglepeople01firsttime
            'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                jump howlersdellsinglepeople01firsttime
            'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                jump howlersdellsinglepeople01
            'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                pass
            'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                pass
            'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                jump howlersdellinstalingrodwithpermission01
            'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                pass
            'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                jump howlersdellfisherhamletupdates03b
            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                pass
            'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                pass
            '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                pass
            '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                pass

label howlersdell_mundaneworkALL:
    label howlersdell_mundanework01:
        $ can_leave = 1
        if howlersdell_eryx_about_room:
            $ can_rest = 1
        $ can_items = 1
        if thais_bigmad and not howlersdell_mundanework_blocked:
            $ howlersdell_mundanework_blocked = 1
            menu:
                'You approach a small group, and are quickly informed that your assistance will no longer be required. “{color=#f6d6bd}The mayor{/color} said you’re spying on us,” she explains while tossing a sling-stone. “Naething else to explain here.”
                \n\nYou return to {color=#f6d6bd}[horsename]{/color} and notice that some of the locals keep a greater distance from you than they used to.
                '
                'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                    jump howlersdell_steephouseconfrontation00
                'I go to the main square.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                    jump howlersdellsquareregular01
                'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                    jump howlersdell_erastos01
                'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                    if howlersdell_bion_firsttime:
                        jump howlersdelltailor01
                    else:
                        jump howlersdelltailorfirsttime01
                'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                    pass
                'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    if howlersdell_elpis_firsttime_theywant:
                        jump howlersdelldruids01yes
                    else:
                        jump howlersdelldruids01no
                'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                    pass
                'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    jump howlersdelldruids01yes
                'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                    jump howlersdelldruids01
                'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                    jump howlersdellsinglepeople01firsttime
                'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                    jump howlersdellsinglepeople01firsttime
                'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                    jump howlersdellsinglepeople01
                'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                    pass
                'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                    pass
                'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                    jump howlersdellinstalingrodwithpermission01
                'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                    pass
                'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                    jump howlersdellfisherhamletupdates03b
                'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                    pass
                'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                    pass
                '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                    pass
                '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                    pass
        else:
            if howlersdell_mundanework_type_day != day:
                $ howlersdell_mundanework_type_day = day
                label howlersdell_mundanework_typeloop:
                    if elpis_about_thyrsusgift1:
                        $ howlersdell_mundanework_type = "elpis"
                        if howlersdell_reputation >= 12:
                            $ howlersdell_mundanework_payment_base = 2
                        else:
                            $ howlersdell_mundanework_payment_base = 1
                        if howlersdell_mundanework_type == "fishers":
                            $ howlersdell_mundanework_payment_bonus = 2
                        elif howlersdell_mundanework_type == "hunters" or howlersdell_mundanework_type == "pathclearing":
                            $ howlersdell_mundanework_payment_bonus = 1
                        else:
                            $ howlersdell_mundanework_payment_bonus = 0
                        $ howlersdell_mundanework_payment_total = (howlersdell_mundanework_payment_base+howlersdell_mundanework_payment_bonus)
                        show screen mundanejob() with dissolve
                        menu:
                            'The guard looks at you tensely, exchanging with you telling nods.
                            '
                            'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                                jump howlersdell_steephouseconfrontation00
                            'I go to the main square.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                                jump howlersdellsquareregular01
                            'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                                jump howlersdell_erastos01
                            'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                                if howlersdell_bion_firsttime:
                                    jump howlersdelltailor01
                                else:
                                    jump howlersdelltailorfirsttime01
                            'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                                pass
                            'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                                if howlersdell_elpis_firsttime_theywant:
                                    jump howlersdelldruids01yes
                                else:
                                    jump howlersdelldruids01no
                            'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                                pass
                            'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                                jump howlersdelldruids01yes
                            'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                                jump howlersdelldruids01
                            'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                                jump howlersdellsinglepeople01firsttime
                            'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                                jump howlersdellsinglepeople01firsttime
                            'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                                jump howlersdellsinglepeople01
                            'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                                pass
                            'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                                pass
                            'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                                jump howlersdellinstalingrodwithpermission01
                            'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                                pass
                            'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                                jump howlersdellfisherhamletupdates03b
                            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                                pass
                            'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                                pass
                            '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                                jump howlersdell_mundanework01
                            '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                                pass
                            '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                                pass
                            '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                                jump howlersdell_mundanework01
                            '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                                pass
                            '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                                pass
                    else:
                        if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                            $ howlersdell_mundanework_type = renpy.random.choice(['herbalists', 'hunters', 'pathclearing', 'farmers', 'lumberjacks', 'fishers'])
                        else:
                            $ howlersdell_mundanework_type = renpy.random.choice(['herbalists', 'hunters', 'pathclearing', 'farmers', 'lumberjacks'])
                        if howlersdell_mundanework_type_old == howlersdell_mundanework_type:
                            jump howlersdell_mundanework_typeloop
                        else:
                            $ howlersdell_mundanework_type_old = howlersdell_mundanework_type
            if howlersdell_reputation >= 12:
                $ howlersdell_mundanework_payment_base = 2
            else:
                $ howlersdell_mundanework_payment_base = 1
            if howlersdell_mundanework_type == "fishers":
                $ howlersdell_mundanework_payment_bonus = 2
            elif howlersdell_mundanework_type == "hunters" or howlersdell_mundanework_type == "pathclearing":
                $ howlersdell_mundanework_payment_bonus = 1
            else:
                $ howlersdell_mundanework_payment_bonus = 0
            $ howlersdell_mundanework_payment_total = (howlersdell_mundanework_payment_base+howlersdell_mundanework_payment_bonus)
            show screen mundanejob() with dissolve
            menu:
                'After a brief exchange of greetings, you are introduced to an overseer who’s in need of a rider.
                '
                'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                    jump howlersdell_steephouseconfrontation00
                'I go to the main square.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                    jump howlersdellsquareregular01
                'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                    jump howlersdell_erastos01
                'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                    if howlersdell_bion_firsttime:
                        jump howlersdelltailor01
                    else:
                        jump howlersdelltailorfirsttime01
                'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                    pass
                'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    if howlersdell_elpis_firsttime_theywant:
                        jump howlersdelldruids01yes
                    else:
                        jump howlersdelldruids01no
                'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                    pass
                'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                    jump howlersdelldruids01yes
                'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                    jump howlersdelldruids01
                'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                    jump howlersdellsinglepeople01firsttime
                'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                    jump howlersdellsinglepeople01firsttime
                'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                    jump howlersdellsinglepeople01
                'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                    pass
                'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                    pass
                'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                    jump howlersdellinstalingrodwithpermission01
                'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                    pass
                'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                    jump howlersdellfisherhamletupdates03b
                'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                    pass
                'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                    pass
                '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                    pass
                '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                    jump howlersdell_mundanework01
                '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                    pass
                '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                    pass

    label howlersdell_mundanework02:
        $ howlersdell_mundanework_day = day
        $ howlersdell_mundanework_numberoftimes += 1
        $ howlersdell_reputation_points += 4
        if howlersdell_mundanework_type == "herbalists":
            $ howlersdell_mundanework_riskchance += 20
        elif howlersdell_mundanework_type == "hunters":
            $ howlersdell_mundanework_riskchance += 25
        elif howlersdell_mundanework_type == "pathclearing":
            $ howlersdell_mundanework_riskchance += 20
        elif howlersdell_mundanework_type == "farmers":
            $ howlersdell_mundanework_riskchance += 10
        elif howlersdell_mundanework_type == "lumberjacks":
            $ howlersdell_mundanework_riskchance += 15
        elif howlersdell_mundanework_type == "fishers":
            $ howlersdell_mundanework_riskchance += 25
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pc_class == "warrior":
            $ d100roll += (pc_battlecounter)
        else:
            $ d100roll += (pc_battlecounter/2)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if d100roll < howlersdell_mundanework_riskchance/2:
            $ howlersdell_mundanework_riskchance = 0
            $ custom1 = "The expedition faced a few difficulties, and at one point you had to flee desperately toward safety. You’re tired, and your clothes got torn in the process."
            if armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness_clothes_torn = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus3appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            $ quarters += 20
        elif d100roll < howlersdell_mundanework_riskchance:
            $ howlersdell_mundanework_riskchance -= 20
            if armor < 2:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "For most of the time you stay safe, but at one point you find yourself evading a pack of predators, and your clothes are now soaked in sweat."
            else:
                $ custom1 = "For most of the time you stay safe, but at one point you find yourself evading a pack of predators, and your clothes are now soaked in sweat. Thankfully, your armor was able to keep you in one piece."
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ quarters += 16
        else:
            $ custom1 = "It turns out you don’t have much to do. You get your job done quickly and with little difficulty."
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ quarters += 12
        $ coins += howlersdell_mundanework_payment_total
        show screen notifyimage( "+%s" %howlersdell_mundanework_payment_total, "gui/coin2.png" )
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+%s {image=cointest}{/i}' %howlersdell_mundanework_payment_total)
        menu:
            '[custom1]
            '
            'I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.' if quest_ruins == 1 and quest_ruinsconflictopen == 1:
                jump howlersdell_steephouseconfrontation00
            'I go to the main square.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the main square.')
                jump howlersdellsquareregular01
            'I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.' if not quest_recruitahunter_spokento_erastos and quest_recruitahunter == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to speak with {color=#f6d6bd}Erastos{/color} for {color=#f6d6bd}Dalit{/color}.')
                jump howlersdell_erastos01
            'I head to {color=#f6d6bd}Bion{/color}, the tailor.' ( condition="quarters < world_daylength" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}Bion{/color}, the tailor.')
                if howlersdell_bion_firsttime:
                    jump howlersdelltailor01
                else:
                    jump howlersdelltailorfirsttime01
            'The tailor has closed her workshop for today. (disabled)' ( condition="quarters >= world_daylength" ):
                pass
            'I go to the local {color=#f6d6bd}priests{/color}.' if not howlersdell_elpis_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                if howlersdell_elpis_firsttime_theywant:
                    jump howlersdelldruids01yes
                else:
                    jump howlersdelldruids01no
            'The druids won’t agree to see me. (disabled)' if howlersdell_elpis_firsttime and not howlersdell_elpis_firsttime_theywant:
                pass
            'I go to {color=#f6d6bd}the druids{/color}.' if howlersdell_elpis_firsttime < 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the local {color=#f6d6bd}priests{/color}.')
                jump howlersdelldruids01yes
            'I go to {color=#f6d6bd}Elpis{/color}, the druidess.' if howlersdell_elpis_firsttime >= 2 and howlersdell_elpis_firsttime_theywant:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Elpis{/color}, the druidess.')
                jump howlersdelldruids01
            'Maybe there are some locals looking for a match in other villages.' ( condition="not howlersdell_timo_firsttime and quest_matchmaking == 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
                jump howlersdellsinglepeople01firsttime
            'I look for {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="not howlersdell_timo_firsttime and howlersdell_eryx_about_job2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Timo{/color}, the washwoman.')
                jump howlersdellsinglepeople01firsttime
            'I return to {color=#f6d6bd}Timo{/color}, the washwoman.' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and galerocks_singlepeople_firsttime and not howlersdell_timo_paulus) or (howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and galerocks_singlepeople_paulus_work)" ):
                jump howlersdellsinglepeople01
            'Timo is still looking for a match. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and not galerocks_singlepeople_firsttime and not howlersdell_timo_paulus)" ):
                pass
            'Timo is waiting for me to speak with Paulus in Gale Rocks. (disabled)' ( condition="(howlersdell_timo_firsttime and quest_matchmaking == 1 and not howlersdell_timo_matched and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work)" ):
                pass
            'Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed == 1 and not thais_about_bronzerod_allowed == -1 and not eudocia_bronzerod_rodin_howlersdell:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since {color=#f6d6bd}Thais{/color} has allowed me to do so, I’ll place a bronze rod on the top of a watchtower. I should be done in about half an hour.')
                jump howlersdellinstalingrodwithpermission01
            'If I want to place a bronze rod on one of these watchtowers, I need to first ask the mayor for her permission. (disabled)' if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed < 1 and not eudocia_bronzerod_rodin_howlersdell and not thais_about_bronzerod_allowed == -1:
                pass
            'I tell some workers to gather at the gate. It’s time to get them to the rockslide.' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell some workers to gather near the gate. It’s time to get them to the rockslide.')
                jump howlersdellfisherhamletupdates03b
            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and quarters >= 40" ):
                pass
            'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not thais_bigmad and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                pass
            '{color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Elpis{/color} wants me to offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to help Elpis. (Required vitality: 2) (disabled)' ( condition="elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work and help Elpis. (disabled)' ( condition="(elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day) or (elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day)" ):
                pass
            '{image=cointest} I offer my services to the guards.' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp >= 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I offer my services to the guards.')
                jump howlersdell_mundanework01
            '{image=coingray} I’m too tired to offer my services to the guards. (Required vitality: 2) (disabled)' ( condition="not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters <= ((world_daylength/2)+11) and pc_hp < 2 and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked" ):
                pass
            '{image=coingray} It’s too late to ask the locals about work. (disabled)' ( condition="(not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and quarters > ((world_daylength/2)+11) and howlersdell_mundanework_day != day and not howlersdell_mundanework_blocked) or (not elpis_about_thyrsusgift1 and howlersdell_mundanework_available and howlersdell_mundanework_day == day and not howlersdell_mundanework_blocked)" ):
                pass