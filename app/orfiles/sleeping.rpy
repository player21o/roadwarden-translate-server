########SLEEPING
default sleep_options = 0
default sleep_destination = 0
default sleep_inprogress = 0

default sleep_dream01 = 0
default sleep_dream02 = 0
default sleep_dream03 = 0
default sleep_dream04 = 0
default sleep_dream05 = 0
default sleep_dream06 = 0
default sleep_dream07 = 0
default sleep_dream08 = 0
default sleep_dream09 = 0
default sleep_dream10 = 0
default sleep_dream_steephouse = 0
default sleep_dream_pc_battlecounter = 0
default sleep_dream_pc_murdered = 0
default sleep_peltnorth = 0
default sleep_monastery = 0
default sleep_howlersdell = 0
default sleep_druidcave = 0
default sleep_watchtower = 0
default sleep_eudociahouse = 0
default sleep_foggylake = 0
default sleep_galerocks = 0
default sleep_whitemarshes = 0
default sleep_greenmountaintribe = 0

default sleep_reminder_day15 = 0
default sleep_reminder_day25 = 0
default sleep_reminder_day29 = 0
default world_endmode = 0
default world_endmode_howlers = 0
default world_deadline = 30
default world_deadline_display = 30

default world_daylength_notification = 0

label sleeping:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ can_potions = 0
    $ sleep_inprogress = 1
    $ at = 0
    $ ruinedvillage_curse_points = 0
    $ ruinedvillage_curse_block = 0
    stop nature fadeout 2.0
    if weathermud:
        $ weathermud = 0
    if weatherfog:
        $ weatherfog = 0
    if bogroad_clotheswet:
        $ bogroad_clotheswet = 0
    scene empty #part A of...
    scene layoutfull #part B of hididng all images
    nvl clear
    $ questionpreset = 0
    if quest_birdhunting == 1 and quest_birdhunting_description06 and foragers_quest_message_timer < (day-1):
        $ quest_birdhunting_description07 = "The bird is already in {color=#f6d6bd}Creeks{/color}. It’s too late for me to deliver the message."
        $ quest_birdhunting = 2
        $ renpy.notify("Quest completed: Bird Hunting")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunting{/i}')
    if (shortcut_darkforest_bandit_toldabouthuntercabin+2) < day and shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_leftthepeninsula and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ shortcut_darkforest_bandit_leftTOpeltnorth = 1
        $ shortcut_darkforest_bandit_inpeltnorth = 1
        $ peltnorth_bonusnpcs += 1
    if sleep_destination == "prolcamp01newdaytent": #tutorial
        $ sleep_inprogress = 0
        if pc_class != "mage":
            $ day = 1
            $ quarters = 26
            $ militarycamp_sleep_tent = 0
            $ pc_hp = limit_pc_hp(pc_hp+0)
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ mana = limit_mana(mana+2)
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump prolcamp01newdaytent
        else:
            show areapicture nightsky01 at basicfade
            nvl clear
            $ manacost = 2
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You take a look at your amulets. For most people, they would be nothing more than trash, but you wouldn’t sell them for a pouch of dragon bones. You use them to shape pneuma to your will. With these little mementos, the few spells you’re familiar with are far more reliable. Who knows, maybe there’s already some power held in them.
                \n\nYou look at the old, though clean bandages that remember dozens of herbal balms and wounds. You can put them on your hurting muscles, bruises, and scratches, then hum an old song about time, which either heals all wounds, or kills us too soon to let us bother with our problems. After a few hours or so, the linen will warm up, confirming it did its job.
                \n\nThis tent may not be much, but your spell would make you feel as good as new - though you’d lose some of your energy.
                '
                'I don’t need to restore my pneuma tonight. I perform the ritual. [[Cost: {color=#f6d6bd}[manacost]{/color} pneuma]' if mana >= manacost:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need to restore my pneuma tonight. I perform the ritual. [[Cost: {color=#f6d6bd}%s{/color} pneuma]' %manacost)
                    $ pc_hp = limit_pc_hp(pc_hp+1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    $ day = 1
                    $ quarters = 26
                    $ militarycamp_sleep_tent = 0
                    $ pc_hp = limit_pc_hp(pc_hp+0)
                    $ pc_food = limit_pc_food(pc_food-2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ renpy.force_autosave(take_screenshot=True, block=True)
                    jump prolcamp01newdaytent
                'I’d rather keep my soul stronger than my shell.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather keep my soul stronger than my shell.')
                    $ day = 1
                    $ quarters = 26
                    $ militarycamp_sleep_tent = 0
                    $ pc_hp = limit_pc_hp(pc_hp+0)
                    $ pc_food = limit_pc_food(pc_food-2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ mana = limit_mana(mana+2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ renpy.force_autosave(take_screenshot=True, block=True)
                    jump prolcamp01newdaytent
    if sleep_destination == "prolcamp01newday": #tutorial
        $ sleep_inprogress = 0
        if pc_class != "mage":
            $ day = 1
            $ quarters = 28
            $ pc_hp = limit_pc_hp(pc_hp-1)
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ mana = limit_mana(mana+1)
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump prolcamp01newday
        else:
            show areapicture nightsky01 at basicfade
            nvl clear
            $ manacost = 2
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You take a look at your amulets. For most people, they would be nothing more than trash, but you wouldn’t sell them for a pouch of dragon bones. You use them to shape pneuma to your will. With these little mementos, the few spells you’re familiar with are far more reliable. Who knows, maybe there’s already some power held in them.
                \n\nYou look at the old, though clean bandages that remember dozens of herbal balms and wounds. You can put them on your hurting muscles, bruises, and scratches, then hum an old song about time, which either heals all wounds, or kills us too soon to let us bother with our problems. After a few hours or so, the linen will warm up, confirming it did its job.
                \n\nMaybe it will even out the pain of sleeping on the ground, though you’d lose some of your energy.
                '
                'I don’t need to restore my pneuma tonight. I perform the ritual. [[Cost: {color=#f6d6bd}[manacost]{/color} pneuma]' if mana >= manacost:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need to restore my pneuma tonight. I perform the ritual. [[Cost: {color=#f6d6bd}%s{/color} pneuma]' %manacost)
                    $ mana = limit_mana(mana-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 pneuma.{/i}')
                    $ day = 1
                    $ quarters = 28
                    $ pc_food = limit_pc_food(pc_food-2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ renpy.force_autosave(take_screenshot=True, block=True)
                    jump prolcamp01newday
                'My pneuma is more valuable, at least for now.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My pneuma is more valuable, at least for now.')
                    $ day = 1
                    $ quarters = 28
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    $ pc_food = limit_pc_food(pc_food-2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ mana = limit_mana(mana+1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ renpy.force_autosave(take_screenshot=True, block=True)
                    jump prolcamp01newday
    if sleep_destination == "peltnorthafterrelaxing":
        $ sleep_inprogress = 0
        $ quarters = 80
        $ pc_hp = limit_pc_hp(pc_hp+1)
        $ mana = limit_mana(mana+3)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
        $ renpy.force_autosave(take_screenshot=True, block=True)
        jump peltnorthafterrelaxing01
    if sleep_destination == "foggylakeafterrelaxing":
        $ sleep_inprogress = 0
        $ quarters = 80
        $ pc_hp = limit_pc_hp(pc_hp+1)
        $ mana = limit_mana(mana+3)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
        $ renpy.force_autosave(take_screenshot=True, block=True)
        jump foggylakeafterrelaxing01
    if sleep_destination == "howlersdellafterrelaxing":
        $ sleep_inprogress = 0
        $ quarters = 80
        $ pc_hp = limit_pc_hp(pc_hp+1)
        $ mana = limit_mana(mana+3)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
        $ renpy.force_autosave(take_screenshot=True, block=True)
        jump howlersdellafterrelaxing01
    if sleep_destination == "howlersdellafterrelaxingpremium":
        $ sleep_inprogress = 0
        $ quarters = 80
        $ pc_hp = limit_pc_hp(pc_hp+2)
        $ mana = limit_mana(mana+4)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
        $ pc_food = limit_pc_food(pc_food+3)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        $ renpy.force_autosave(take_screenshot=True, block=True)
        jump howlersdellafterrelaxing02
    label sleepingmainquests:
        if pc_goal == "iwanttohelp" and pc_goal_iwanttohelppoints >= 15 and quest_pc_goal == 1:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You think of the people you’ve encountered, of what you’ve done for them. You picture the rough roads and their monsters, the claws hidden in all the places where you can’t be at once. Humans torn limb by limb, burnt villages, poisoned wells, cut throats...
                \n\nYou keep waking up, not sure if these thoughts are a dream, a memory, or a vision. You stand up, walk around, and breathe, slowly, deeply, your stomach rising and falling.
                '
                'I focus on its movements.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on its movements.')
                    menu:
                        'You came here to help people, change their lives for the better, to heal the land. But after many struggles and sacrifices, this place is almost the same. You think of the past days, and find both the light of your deeds and the gloom of the things that are out of your reach. You can save some people, but not the entire realm.
                        \n\nYou’ve done so much, but you’re small and alone.
                        '
                        'I reject this thought. I need to be stronger. People need me, and I’m going to help them, no matter the cost.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reject this thought. I need to be stronger. People need me, and I’m going to help them, no matter the cost.')
                            $ quest_pc_goal_description_completed_iwanttohelp = "I’ve helped many people already, but I still need to change the North. I now know that my determination was not great enough."
                            $ endgame_epilogue_evil = 1
                            $ achievement_pc_goal_description = "I’ve helped many people already, but I still need to change the North."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I may not be all-powerful, but I do as much as I can. I need to accept my limitations.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may not be all-powerful, but I do as much as I can. I need to accept my limitations.')
                            $ quest_pc_goal_description_completed_iwanttohelp = "I helped many people and changed things about the North for the better. My duty has been fulfilled."
                            $ achievement_pc_goal_description = "I helped many people and changed things about the North for the better."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You can give yourself a break,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
        if pc_goal == "iwantstatus" and pc_goal_iwantstatuspoints >= 4 and quest_pc_goal == 1:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            if pc_lies >= 10 or (thais_about_magicfruit_received and not thais_about_magicfruit_barter) or (quest_glauciasupport == 2 and not glaucia_about_galerocksdecision_liedto):
                menu:
                    'You think of the leaders you’ve encountered, the work you’ve done for them, and the sacrifices you had to make to get on their good side. Here, in the far North, you spin the first threads of your web of connections. Yet something distorts your new beginning, a shadow that gets greater with every heartbeat.
                    \n\nYou keep waking up, not sure if these thoughts are a dream, a memory, or a vision. You stand up, walk around, and breathe, slowly, deeply, your stomach rising and falling.
                    '
                    'I focus on its movements.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on its movements.')
                        if pc_lies >= 15:
                            $ custom1 = "You spread so many lies, handling them like a dagger. "
                        elif pc_lies >= 10:
                            $ custom1 = "All the lies you carry with you are now twisting your tongue. "
                        else:
                            $ custom1 = ""
                        if thais_about_magicfruit_received and not thais_about_magicfruit_barter:
                            $ custom2 = "You abandoned the people of {color=#f6d6bd}Old Págos{/color}, and you can’t tell how many of them are going to die because of it. "
                        else:
                            $ custom2 = ""
                        if quest_glauciasupport == 2 and not glaucia_about_galerocksdecision_liedto:
                            $ custom3 = "Who can tell what sort of havoc will {color=#f6d6bd}Glaucia’s{/color} anger bring to this place across the years to come. "
                        else:
                            $ custom3 = ""
                        menu:
                            'The gloom comes straight from the soul of a very different being than the one who came to this peninsula. Is the [pcname] you knew gone? Is this new creature the {i}real{/i} you?
                            \n\nIf it is {i}just{/i} a mask after all, you still don’t know how to handle it. [custom1][custom2][custom3]You’ve reached for power and control, but something about all this is now chasing after you, plaguing your thoughts like a spirit of judgment.
                            '
                            'I reject this thought. I {i}had to{/i} be ruthless. I’ve made sacrifices, but they will be the beginning of something great.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reject this thought. I {i}had to{/i} be ruthless. I’ve made sacrifices, but they will be the beginning of something great.')
                                $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and will have a great advantage when talking to the members of the guild. It took a large price, but what matters is that {i}I{/i} will be fine."
                                $ endgame_epilogue_evil = 2
                                $ achievement_pc_goal_description = "I’ve paid a high price for making some powerful connections in the North, but it was all worth it."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                menu:
                                    'Your heart is hit with both determination and cruel satisfaction. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. After all, keeping people dancing to your tune requires a strong soul, and you need wits to keep making the {i}right{/i} choices.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
                            'I wish I could move back in time, fix all of this. But all I can do is try to be better from now on.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish I could move back in time, fix all of this. But all I can do is try to be better from now on.')
                                $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and will have a great advantage when talking to the members of the guild, but I feel like something about me is changing. I regret the things I’ve done."
                                $ endgame_epilogue_evil = 1
                                $ achievement_pc_goal_description = "I’ve paid a high price for making some powerful connections in the North. Maybe even too high."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                menu:
                                    'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “Turn back, while you still can,” you hear, or maybe say.
                                    '
                                    'I lie down and return to sleep.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
            else:
                if pc_lies:
                    $ custom1 = "You sometimes lie, but not unusually so"
                else:
                    $ custom1 = "You somehow managed to move forward without a single lie"
                menu:
                    'Your first sleep starts quickly and lasts a long time, relaxing and gentle. When you wake up after a few hours, you think of the leaders you’ve encountered, the work you’ve done for them, and the hardships you had to overcome to get on their good side. You’ve spun the first threads of your web of connections.
                    \n\nYour head is clear, and you start to recollect your time in the peninsula. [custom1], and you didn’t sacrifice people for your own well-being. It’s still you, the same soul who arrived here, so close to reaching your goal.
                    '
                    'I’ve managed to keep my conscience clean. I knew that being power-hungry would devour me as well.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve managed to keep my conscience clean. I knew that being power-hungry would devour me as well.')
                        $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and didn’t lose my identity in the process. I’ll have a great advantage when talking to the members of the guild."
                        $ achievement_pc_goal_description = "I’ve made some powerful connections and didn’t lose my identity in the process."
                        $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                        $ quest_pc_goal = 2
                        if not pc_hp_can5:
                            $ pc_hp_can5 = 1
                            $ pc_hp = limit_pc_hp(pc_hp+1)
                            show plus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        if not tutorial_5hp:
                            $ tutorial_5hp = 1
                        menu:
                            'As you look around, thinking of your journey, you feel relaxed and complete. You smile, thinking of the things you’ve accomplished, and of what still awaits you.
                            '
                            'The next chapter of my life.' if pc_class == "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next chapter of my life.')
                                $ tutorial_5hp = 2
                                jump sleepingmainquests
                            'The next stage of my life.' if pc_class != "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next stage of my life.')
                                $ tutorial_5hp = 2
                                jump sleepingmainquests
                    'I don’t really care about any of that. I just did what I thought was more beneficial for me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t really care about any of that. I just did what I thought was more beneficial for me.')
                        $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and didn’t hurt too many people in the process. I’ll have a great advantage when talking to the members of the guild."
                        $ endgame_epilogue_evil = 2
                        $ achievement_pc_goal_description = "I’ve made some powerful connections and didn’t hurt too many people in the process."
                        $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                        $ quest_pc_goal = 2
                        if not pc_hp_can5:
                            $ pc_hp_can5 = 1
                            $ pc_hp = limit_pc_hp(pc_hp+1)
                            show plus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        if not tutorial_5hp:
                            $ tutorial_5hp = 1
                        menu:
                            'As you look around, thinking of your journey, you feel relaxed and ready. You smile, thinking of the new possibilities you’ve unlocked, and of what still awaits you.
                            '
                            'I lie down.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                $ tutorial_5hp = 2
                                jump sleepingmainquests
        if pc_goal == "iwanttoberemembered" and pc_goal_iwanttoberememberedpoints >= 6 and quest_pc_goal == 1:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You think of the things that you’ve done, the places you’ve visited, the mysteries you’ve unraveled. You keep waking up, not sure if these thoughts are a dream, a memory, or a vision. You stand up, walk around, and breathe, slowly, deeply, your stomach rising and falling.
                '
                'I focus on its movements.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on its movements.')
                    menu:
                        'You think back on the spectacular deeds you’ve accomplished. Their weight is strangely light, as if all that you’ve done hardly means anything at all. Once you get back to {color=#f6d6bd}Hovlavan{/color}, no soul is going to care about your tales any more than you did about the sailors who {i}killed the beast of the seas{/i}, or the adventurers who {i}turned an emperor of the undead to ashes{/i}. Are your stories even worth a free bowl of stew?
                        '
                        'Rubbish. Dozens of lives were saved, and it’s all thanks to me. People here will remember me as a hero.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Rubbish. Dozens of lives were saved, and it’s all thanks to me. People here will remember me as a hero.')
                            $ quest_pc_goal_description_completed_iwanttoberemembered = "I’m the hero of the peninsula, I’m sure of it. People will remember my name for generations."
                            $ achievement_pc_goal_description = "I’m the hero of the peninsula. People will remember my name for generations. They have to."
                            $ endgame_epilogue_evil = 1
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You are a hero, after all. You need to look the part.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I’ve done so much, yet this place is still similar to what it had been like before my arrival. I must admit that I’m yet another roadwarden who arrived at the peninsula, nothing more.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve done so much, yet this place is still similar to what it had been like before my arrival. I must admit that I’m yet another roadwarden who arrived at the peninsula, nothing more.')
                            $ quest_pc_goal_description_completed_iwanttoberemembered = "I’ve done as much as I could, but who knows if it was enough to make me a hero. Time will tell."
                            $ achievement_pc_goal_description = "I’ve done as much as I could, and I can’t know if it was enough to make me a hero."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You can give yourself a break,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
        if pc_goal == "ineedmoney":
            if coins >= 100 and quest_pc_goal == 1:
                $ quarters = 95
                show areapicture nightsky01 at basicfade
                stop nature fadeout 4.0
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of the soul you care for the most. You came here to find the coins they need, and your journey was so long... You wonder how far away you are from reaching your goal.
                    '
                    'I get to my bags and start to count the dragon bones I own.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get to my bags and start to count the dragon bones I own.')
                        menu:
                            'You unpack your pouch, or rather your heavy {i}sack{/i}. Counting its contents is satisfying, both because of how many of them there are, and the stories the coins carry with them. Some of them you remember from the specific transactions you made, or the places where you found them. Others make you think of the dozens of years that they have behind them. They’re in different shapes and colors. Who knows where some of them have been?
                            \n\nA hundred dragon bones.
                            \n\nThis is all you need. You take a deep breath. You’ve done it.
                            '
                            'I take a wooden box and fill it with rags and coins. I want to be sure I don’t waste any of it before I leave the peninsula.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags and coins. I want to be sure I don’t waste any of it before I leave the peninsula.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ coins -= 100
                                $ pc_goal_lost100coins = 1
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve gathered one hundred dragon bones. They will surely help me save my sibling."
                                $ achievement_pc_goal_description = "I’ve gathered 100 dragon bones to support the soul I care about."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. You still need the pay from the merchant guild, but it’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down and get back to sleep.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and get back to sleep.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
                            'I still need to use some of these coins, but I’ll earn even more before I get back to the city. I put them back into the pouch.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to use some of these coins, but I’ll earn even more before I get back to the city. I put them back into the pouch.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve gathered at least one hundred dragon bones. They will surely help me save my sibling. I just need to be sure I don’t spend too much of it."
                                $ achievement_pc_goal_description = "I’ve gathered 100 dragon bones to support the soul I care about."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. You still need the pay from the merchant guild, but it’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
            elif quest_pc_goal_description_completed_ineedmoney and quest_pc_goal == 1 and item_asterionwine and item_asterionwine_pcknows_2:
                $ quarters = 95
                show areapicture nightsky01 at basicfade
                stop nature fadeout 4.0
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of the soul you care for the most. You came here to find the coins they need, and your journey was so long... But now it seems like you’ve finally reached the goal of your journey.
                    '
                    'I go to my bags and grab the bottle of Night’s Bane.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get to my bags and grab the bottle of Night’s Bane.')
                        menu:
                            'You unpack the wine, remembering the way you earned it. You sniff the expensive contents, even though to you it smells like any other drink based on fermented fruits. It’s strange to realize that this very bottle may be your saviour.
                            \n\nYour soul is filled with visions of opulence, but you push them away. You know what you need to do with it. You take a deep breath. You’ve done it. This is it.
                            '
                            'I take a wooden box and fill it with rags. I want to be sure I don’t damage the bottle before I get back to the city.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags. I want to be sure I don’t damage the bottle before I get back to the city.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal_description_completed_iwantmoney100 = "The bottle of Night’s Bane I found is going to help me save my sibling."
                                $ achievement_pc_goal_description = "The expensive bottle of Night’s Bane is going to help me save my sibling."
                                menu:
                                    'It sounds easy, but your hands are shaking. You still need the pay from the merchant guild, but it’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
            else:
                pass
        if pc_goal == "iwantmoney":
            if coins >= 100 and quest_pc_goal == 1:
                $ quarters = 95
                show areapicture nightsky01 at basicfade
                stop nature fadeout 4.0
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of all the plans you have for your future life in {color=#f6d6bd}Hovlavan{/color}. You came here to find the coins you need, and your journey was so long... You wonder how far away you are from reaching your goal.
                    '
                    'I go to my bags and start to count the dragon bones I own.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and start to count the dragon bones I own.')
                        menu:
                            'You unpack your pouch, or rather your heavy {i}sack{/i}. Counting its contents is satisfying, both because of how many of them there are, and the stories the coins carry with them. Some of them you remember from the specific transactions you made, or the places where you found them. Others make you think of the dozens of years that they have behind them. They’re in different shapes and colors. Who knows where some of them have been?
                            \n\nA hundred dragon bones.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nThis is all you need. You take a deep breath. You’ve done it.
                            '
                            'I take a wooden box and fill it with rags and coins. I want to be sure I don’t waste any of it before I leave the peninsula.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags and coins. I want to be sure I don’t waste any of it before I leave the peninsula.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ coins -= 100
                                $ pc_goal_lost100coins = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "With 100 dragon bones I can try to get rich in {color=#f6d6bd}Hovlavan{/color}."
                                $ achievement_pc_goal_description = "With 100 dragon bones I can try to get rich in {color=#f6d6bd}Hovlavan{/color}."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
                            'I still need to use some of these coins, but I’ll earn even more before I get back to the city. I put them back into the pouch.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to use some of these coins, but I’ll earn even more before I get back to the city. I put them back into the pouch.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "I’ve gathered at least one hundred dragon bones. It’s a good start to help me get rich in {color=#f6d6bd}Hovlavan{/color}. I just need to be sure I don’t spend too much of it."
                                $ achievement_pc_goal_description = "With 100 dragon bones I can try to get rich in {color=#f6d6bd}Hovlavan{/color}."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
            elif quest_pc_goal_description_completed_iwantmoney and quest_pc_goal == 1 and item_asterionwine and item_asterionwine_pcknows_2:
                $ quarters = 95
                show areapicture nightsky01 at basicfade
                stop nature fadeout 4.0
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of all the plans you have for your future life in {color=#f6d6bd}Hovlavan{/color}. You came here to find the coins you need, and your journey was so long... But now it seems like you’ve finally reached your goal.
                    '
                    'I go to my bags and grab the bottle of Night’s Bane.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and grab the bottle of Night’s Bane.')
                        menu:
                            'You unpack the wine, remembering the way you earned it. You sniff the expensive contents, even though to you it smells like any other drink based on fermented fruits. It’s strange to realize that this very bottle may lay the path to your future.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nYou take a deep breath. You’ve done it. This is it.
                            '
                            'I take a wooden box and fill it with rags. I want to be sure I don’t damage the bottle before I get back to the city.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags. I want to be sure I don’t damage the bottle before I get back to the city.')
                                $ quest_pc_goal = 2
                                if not pc_hp_can5:
                                    $ pc_hp_can5 = 1
                                    $ pc_hp = limit_pc_hp(pc_hp+1)
                                    show plus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                                if not tutorial_5hp:
                                    $ tutorial_5hp = 1
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal_description_completed_iwantmoney100 = "The bottle of Night’s Bane I found is a good start to help me get rich in {color=#f6d6bd}Hovlavan{/color}."
                                $ achievement_pc_goal_description = "The expensive bottle of Night’s Bane is a good start to help me get rich in {color=#f6d6bd}Hovlavan{/color}."
                                menu:
                                    'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, a single human being, and that the purpose of your journey is no longer a dream.
                                    \n\nYou suddenly feel tired. You deserve a good, long sleep.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        $ tutorial_5hp = 2
                                        jump sleepingmainquests
            else:
                pass
        if (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_howlersdell and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_creeks and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_monastery and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_bandits and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_galerocks and quest_pc_goal == 1):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'Your dreams are chaotic and vivid, mixing the animal fangs and blood from the recent days with the most deeply rooted events of your past, which shaped your soul as it is now. You’re sweating and keep waking up, not sure if these thoughts are memories, visions, or your imagination.
                \n\nYou stand up, walk around, and breathe, slowly, deeply, focusing on the movement of your stomach.
                '
                'I’m thinking about my recent stay at {color=#f6d6bd}Howler’s Dell{/color}.' if pc_goal_iwantnewlife_howlersdell:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about my recent stay at {color=#f6d6bd}Howler’s Dell{/color}.')
                    menu:
                        'This journey was meant to be the foundation of your new life, but as you think about all the things that would await you in the city, you are exhausted. You observe the scratches, cuts, and bruises you earned this summer, and while you’re sure the stories you carry with your shell are worth something, you know this fall and winter won’t bring you any rest. They may be but another fight, and you don’t know how much more you can endure.
                        \n\nBut considering what {color=#f6d6bd}Thais{/color} told you... There may be another way.
                        '
                        'I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the farmers and druids.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the farmers and druids.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ achievement_pc_goal_description = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I keep my eyes shut for as long as it takes.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep my eyes shut for as long as it takes.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                'I’m thinking about my recent stay at {color=#f6d6bd}Creeks{/color}.' if pc_goal_iwantnewlife_creeks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about my recent stay at {color=#f6d6bd}Creeks{/color}.')
                    menu:
                        'This journey was meant to be the foundation of your new life, but as you think about all the things that would await you in the city, you are exhausted. You observe the scratches, cuts, and bruises you earned this summer, and while you’re sure the stories you carry with your shell are worth something, you know this fall and winter won’t bring you any rest. They may be but another fight, and you don’t know how much more you can endure.
                        \n\nBut considering what the people at the village told you... There may be another way.
                        '
                        'I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the hunters. Maybe I could learn a few things about carpentry.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the hunters. Maybe I could learn a few things about carpentry.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was hoping to build a new life for myself, but it seems that another opportunity has found me instead."
                            $ achievement_pc_goal_description = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                'I’m thinking about the time I spent in {color=#f6d6bd}Gale Rocks{/color}.' if pc_goal_iwantnewlife_galerocks:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about the time I spent in {color=#f6d6bd}Gale Rocks{/color}.')
                    menu:
                        'This journey was meant to be the foundation of your new life, but as you think about all the things that would await you in the city, you are exhausted. You observe the scratches, cuts, and bruises you earned this summer, and while you’re sure the stories you carry with your shell are worth something, you know this fall and winter won’t bring you any rest. They may be but another fight, and you don’t know how much more you can endure.
                        \n\nBut considering what the people at the village told you... There may be another way.
                        '
                        'I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the fishers. They put work above all else, but are fair people.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may never be able to build a future for myself without giving up on my life in {color=#f6d6bd}Hovlavan{/color}. I should think about staying with the fishers. They put work above all else, but are fair people.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was hoping to build a new life for myself, but it seems that another opportunity has found me instead."
                            $ achievement_pc_goal_description = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                'I’m thinking about {color=#f6d6bd}the monastery{/color}.' if pc_goal_iwantnewlife_monastery:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about {color=#f6d6bd}the monastery{/color}.')
                    menu:
                        'This journey was meant to be the foundation of your new life, but as you think about all the things that would await you in the city, you are exhausted. You observe the scratches, cuts, and bruises you earned this summer, and while you’re sure the stories you carry with your shell are worth something, you know this fall and winter won’t bring you any rest. They may be but another fight, and you don’t know how much more you can endure.
                        \n\nBut seeing how the monks accepted your request... There is another way.
                        '
                        'It’s time to give up on my life in {color=#f6d6bd}Hovlavan{/color}. On the peak of the mountain, I will finally find peace.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to give up on my life in {color=#f6d6bd}Hovlavan{/color}. On the peak of the mountain, I will finally find peace.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was hoping to build a new life for myself, but it seems that another opportunity has found me instead."
                            $ achievement_pc_goal_description = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                'I’m thinking about {color=#f6d6bd}Glaucia’s{/color} invitation.' if pc_goal_iwantnewlife_bandits:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about {color=#f6d6bd}Glaucia’s{/color} invitation.')
                    menu:
                        'This journey was meant to be the foundation of your new life, but as you think about all the things that would await you in the city, you are exhausted. You observe the scratches, cuts, and bruises you earned this summer, and while you’re sure the stories you carry with your shell are worth something, you know this fall and winter won’t bring you any rest. They may be but another fight, and you don’t know how much more you can endure, especially on your own.
                        \n\nBut if you were to join a band, far from the city walls... You don’t {i}have to{/i} be alone.
                        '
                        'It’s time to give up on my life in {color=#f6d6bd}Hovlavan{/color}. If I find no better options, I’ll return to the hideout.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to give up on my life in {color=#f6d6bd}Hovlavan{/color}. If I find no better options, I’ll return to the hideout.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was hoping to build a new life for myself, but it seems that another opportunity has found me instead."
                            $ achievement_pc_goal_description = "I was hoping to build a new life for myself, but it seems like another opportunity has found me instead."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away from me what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            if not pc_hp_can5:
                                $ pc_hp_can5 = 1
                                $ pc_hp = limit_pc_hp(pc_hp+1)
                                show plus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if not tutorial_5hp:
                                $ tutorial_5hp = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    $ tutorial_5hp = 2
                                    jump sleepingmainquests
        if day == (world_deadline-1):
            $ world_endmode = 1
            jump sleepingafterevent
        if quest_asterion == 1 and pc_class == "scholar" and asterion_highisland_clues == 2 and not world_popupnarration_highisland1 and not world_popupnarration_highisland2 and not asterion_found and not foggy_about_highisland:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ asterion_highisland_clues += 1
            $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
            $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
            $ asterion_highisland_knowsabout = 1
            menu:
                'You think about the sparse clues you found about {color=#f6d6bd}Asterion’s{/color} whereabouts. If it’s true he was looking for something beyond the peninsula, maybe using a boat, the old tax codices you looked through years ago could provide you with a hint.
                \n\nThere’s only one large piece of land close to the coast - {color=#f6d6bd}High Island{/color}, a massive, green territory surrounding a volcano, with its surface spread high above the ocean surface. It’s a wild, forsaken place that used to belong to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, but ever since the army of {color=#f6d6bd}Hovlavan{/color} failed at conquesting it over two centuries ago, ships have been staying away from it. The rumors of the treasures hidden in the caves around the volcano were numerous, but not more reliable than the regular sailor tales.
                \n\nCome to think of it, even though you remember both official documents and vague scribbles focused on this “potential source of wood, fish, and ore,” you’ve seen not a word dedicated to {color=#f6d6bd}The Tribe{/color}, and neither to the description of its homeland.
                '
                'Someone {i}must{/i} know more about that place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone {i}must{/i} know more about that place.')
                    jump sleepingfurther
    label sleepingfurther:
        if item_sharpeningpotion_used == day:
            $ quarters = 95
            $ item_sharpeningpotion_used = 0
            $ pc_battlecounter -= 20
            $ pc_throwingxp -= 20
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            if pc_food >= 2:
                $ pc_food = limit_pc_food(pc_food-2)
                show minus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You get up and lean to the side. You vomit, then wipe off the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell with the remains of food.
                    '
                    'With an aching stomach, I wash the floor.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- With an aching stomach, I wash the floor.')
                        jump sleepingfurther
            elif pc_food >= 1:
                $ quarters = 95
                $ pc_food = limit_pc_food(pc_food-1)
                show minus1food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                menu:
                    'You get up and lean to the side. You vomit, then wipe off the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell with the remains of food and droplets of your own blood.
                    '
                    'I wait for a few minutes, then wash the floor.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for a few minutes, then wash the floor.')
                        jump sleepingfurther
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                $ quarters = 95
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-3)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
                menu:
                    'You get up and lean to the side. You vomit out blood, then wipe off the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell.
                    '
                    'My stomach hurts so much I have to lie down. I’ll wash the floor in the morning.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My stomach hurts so much I have to lie down. I’ll wash the floor in the morning.')
                        jump sleepingfurther
        if day == 5 and not tutorial_daylength:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'As you prepare your belongings, you realize that the days are getting noticeably shorter. The closer you get to autumn, the less time you’ll have before the beasts of the nights leave their lairs.
                '
                'For now, it won’t be that bad, but I better make sure to not waste too many hours.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, it won’t be that bad, but I better make sure to not waste too many hours.')
                    $ tutorial_daylength = 1
                    jump sleepingfurther
        if day == 3 and not weathermud:
            $ quarters = 95
            $ weathermud = 1
            $ weathermudreloaddistances = 1
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'The sounds of rain wake you up briefly. Before you return to sleep, you think about your plans. Riding in the mud is difficult - {color=#f6d6bd}[horsename]{/color} will have a rough time, especially on the unpaved grounds.
                '
                'It may be a good day to take a break at an inn.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a good day to take a break at an inn.')
                    jump finaldestinationmuddistances
        elif (day == 6 and not weathermud) or (day == 11 and not weathermud) or (day == 17 and not weathermud) or (day == 24 and not weathermud) or (day == 32 and not weathermud) or (day == 35 and not weathermud) or (day == 41 and not weathermud):
            $ quarters = 95
            $ weathermud = 1
            $ weathermudreloaddistances = 1
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'The rains once again hit the ground, interrupting your sleep.
                '
                'Another day of muddy roads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Another day of muddy roads.')
                    jump finaldestinationmuddistances
        elif (day == 18 and not weathermud) or (day == 42 and not weathermud):
            $ quarters = 95
            $ weathermud = 1
            $ weathermudreloaddistances = 1
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'The dark skies don’t let go - it’s yet another night of rainfall.
                '
                'Never a break, huh.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a good day to take a break at an inn.')
                    jump finaldestinationmuddistances
        if (not weatherfog and day == 7) or (not weatherfog and day == 14) or (not weatherfog and day == 21) or (not weatherfog and day == 27) or (not weatherfog and day == 33) or (not weatherfog and day == 37) or (not weatherfog and day == 43):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            $ weatherfog = 1
            if pc_area == "militarycamp":
                $ custom1 = "The shivers wake you up, you hear the soldiers gathering outside. The fog is so dense you hardly see the wall around you, and the screeches of beasts are so distorted you can’t tell them apart."
            if pc_area == "peltnorth":
                $ custom1 = "The shivers wake you up, you hear the hunters leaving the building. You look through the window, but the fog is so dense you hardly see the wall around you. Still, they are being patrolled by the night shift, which places torches and carries lanterns."
            if pc_area == "druidcave":
                $ custom1 = "The shivers wake you up, the cold breeze enters through the open door. {color=#f6d6bd}The old druid{/color} is standing outside, surrounded by the fog, whispering something in the Old Speech. The garden patches are hardly visible - you keep thinking that in just a few moments a glazing pair of eyes will sink its sharp teeth in the man’s neck, but the humming of the spring is gentle and undisturbed."
            if pc_area == "howlersdell":
                $ custom1 = "The shivers wake you up. You open the window and see the dense fog covering Howler’s Creek, spreading like milk throughout the entire village. You hear an amused quarrel coming from the main square, and spot the dancing light of torches and lanterns, yet the village remains calm and asleep."
            if pc_area == "monastery":
                $ custom1 = "The shivers wake you up. The winds are a bit calmer now, but the dense fog reaches the cool interiors of the shed, disappearing after it sinks just a few inches in. The loud singing reaches you from the mountain’s caves, distorted and nightmarish."
            if pc_area == "whitemarshes" and not whitemarshes_nomoreundead:
                $ custom1 = "The shivers wake you up and you open the door slightly, letting the dense fog in. There are hardly any lights outside, and you don’t even see the village’s wall. The locals gather their {i}awoken{/i} workers on the roads and while a few of them meet your eyes, the others refuse to acknowledge your gaze."
            if pc_area == "whitemarshes" and whitemarshes_nomoreundead:
                $ custom1 = "The shivers wake you up and you open the door slightly, letting the dense fog in. There are no lights outside, and you hear no guards, see no walls. The screams of a dying bird make you flinch."
            if pc_area == "watchtower":
                $ custom1 = "The shivers wake you up. You open the window, inviting the dense fog in, and letting the gentle droplets form on your skin. The entire tower is surrounded by darkness - you see no stars, nor the ground."
            if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                $ custom1 = "The shivers wake you up, the cold breeze enters through the ajar gate of the shed. You see {color=#f6d6bd}Eudocia{/color} in the yard, with a blanket on her shoulders and her feet sunk into the freezing ground. She greets you with a slight nod, then closes her eyes, taking in deep breaths. Her golems are just behind her, on the brink of visibliness."
            if pc_area == "greenmountaintribe":
                if cephasgaiane_dayvisit:
                    $ custom1 = "The shivers wake you up. You open the door, seeing a few people sitting on rocks and logs, {color=#f6d6bd}Gaiane{/color} among them. They’re covered with the dense fog and warm up their hands with cups of aromatic tisanes. They don’t talk to each other, just letting the pneuma enter their shells. Seeing the lights above the terrace walls, you’ve no doubt the guards are nearby."
                else:
                    $ custom1 = "The shivers wake you up. You open the door, seeing a few people sitting on rocks and logs. They’re covered with the dense fog and warm up their hands with cups of aromatic tisanes. They don’t talk to each other, just letting the pneuma enter their shells. Seeing the lights above the terrace walls, you’ve no doubt the guards are nearby."
            if pc_area == "foggylake":
                $ custom1 = "The shivers wake you up. {color=#f6d6bd}Foggy{/color} is standing by the open door, letting the dense fog in, with her back lit by a lantern. While she breathes slowly, her eyes are keenly observing the area, and after you focus, you hear the distorted shouts of roaming saurians."
            if pc_area == "creeks":
                $ custom1 = "Someone wakes you up, warning of the fog that covers the square so densely you can’t see further than four steps away from the door. The adults stand alert for more than an hour, keeping spears in their reach, and from time to time shouting at other houses, making sure everyone is still alive."
            if pc_area == "galerocks":
                $ custom1 = "The shivers wake you up and you open the door slightly, letting the dense fog in. You see a few lights, most likely lanterns, and you hear a few patrolling guards. One of them shouts at you to stay inside - the harpies may descend at lone wanderers."
            if not weatherfogtotalcounter:
                $ custom2 = "\n\nFogs tend to get more common in late summer, but the tribes of The Dragonwoods often see them as a bad sign. The wild spirits they carry are believed to impact both the visible and the invisible, and not in ways that help humankind."
            else:
                $ custom2 = ""
            menu:
                '[custom1][custom2]
                '
                'I allow the fog to touch my shell and fill it with pneuma.' if pc_class == "mage" and mana < 5:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow the fog to touch my shell and fill it with pneuma.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    $ mana = limit_mana(mana+2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    jump sleepingfurther
                'My pneuma is strong. I don’t need the fog’s touch. (disabled)' if pc_class == "mage" and mana >= 5:
                    pass
                'I sigh. If there are any undead in these woods, the fog will strengthen them.' if weatherfogtotalcounter == 0:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. If there are any undead in these woods, the fog will strengthen them.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    jump sleepingfurther
                'I stay inside, hoping there are no curses carried by the fog.' if weatherfogtotalcounter == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay inside, hoping there are no curses carried by the fog.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    jump sleepingfurther
                'While I’m looking for a candle, I think of the many times I’ve heard parents telling their naughty kids that {i}the fogs will take them{/i}.' if weatherfogtotalcounter == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- While I’m looking for a candle, I think of the many times I’ve heard parents telling their naughty kids that {i}the fogs will take them{/i}.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    jump sleepingfurther
                'The fall will make the fogs even more common... Soon, roads will get too dangerous for a single rider.' if weatherfogtotalcounter == 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The fall will make the fogs even more common... Soon, roads will get too dangerous for a single rider.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    jump sleepingfurther
                'It too shall pass.' if weatherfogtotalcounter >= 4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It too shall pass.')
                    $ weatherfogtotalcounter += 1
                    $ oldtunnel_inside_undead_hp += 1
                    jump sleepingfurther
        # if healingritual_using and healingritual_counter >= 5 and not healingritual_discount:
        #     $ healingritual_discount = 1
        #     $ quarters = 95
        #     show areapicture nightsky01 at basicfade
        #     stop nature fadeout 4.0
        #     if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
        #         play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
        #         with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        #         nvl clear
        #     menu:
        #         'This time, surrounding yourself with healing amulets feels just right, and your breath remains strong all the way through.
        #         '
        #         'From now on, preparing the ritual will be much easier for me.':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- From now on, preparing the ritual will be much easier for me.')
        #             jump sleepingfurther
        if item_furlesswolftrophy == 1 and item_furlesswolftrophy_day < (day-3):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'Your sleep gets interrupted by the foul smell coming from your bundles. The head of the monstrous wolf-like creature is now rotting. Its state will worsen with every passing day, but even now you struggle to imagine continuing your journey with this thing around. And you doubt anyone will be willing to buy it.
                '
                'I throw it somewhere where it won’t bother anyone and get back to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw it somewhere where it won’t bother anyone and get back to sleep.')
                    $ renpy.notify("You’ve lost the furless wolf’s head.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve lost the furless wolf’s head.{/i}')
                    $ item_furlesswolftrophy = 0
                    jump sleepingfurther
        if item_stoat and item_stoat_day < (day-4):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'Your sleep gets distorted by the foul smell coming from your bundles. The tiny carcass of the stoat is now rotting. Its state will get worse with every day, but even now you struggle to imagine that you could continue your journey with this thing around. And you doubt anyone will be willing to buy it.
                '
                'I throw it somewhere where it won’t bother anyone and get back to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw it somewhere where it won’t bother anyone and get back to sleep.')
                    $ renpy.notify("You’ve lost the stoat’s carcass.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve lost the stoat’s carcass.{/i}')
                    $ item_stoat = 0
                    jump sleepingfurther
        if item_rawfishtotalnumber < 0:
            $ item_rawfishtotalnumber = 0
        elif (item_rawfishtotalnumber == 0 and item_rawfish01) or (item_rawfishtotalnumber == 0 and item_rawfish02) or (item_rawfishtotalnumber == 0 and item_rawfish03) or (item_rawfishtotalnumber == 0 and item_rawfish04) or (item_rawfishtotalnumber == 0 and item_rawfish05) or (item_rawfishtotalnumber == 0 and item_rawfish06) or (item_rawfishtotalnumber == 0 and item_rawfish07) or (item_rawfishtotalnumber == 0 and item_rawfish08) or (item_rawfishtotalnumber == 0 and item_rawfish09) or (item_rawfishtotalnumber == 0 and item_rawfish10):
            $ item_rawfishtotalnumber = 0
            $ item_rawfish01 = 0
            $ item_rawfish02 = 0
            $ item_rawfish03 = 0
            $ item_rawfish04 = 0
            $ item_rawfish05 = 0
            $ item_rawfish06 = 0
            $ item_rawfish07 = 0
            $ item_rawfish08 = 0
            $ item_rawfish09 = 0
            $ item_rawfish10 = 0
            jump sleepingfurther
        elif (item_rawfish01 and item_rawfish01 < day) or (item_rawfish02 and item_rawfish02 < day) or (item_rawfish03 and item_rawfish03 < day) or (item_rawfish04 and item_rawfish04 < day) or (item_rawfish05 and item_rawfish05 < day) or (item_rawfish06 and item_rawfish06 < day) or (item_rawfish07 and item_rawfish07 < day) or (item_rawfish08 and item_rawfish08 < day) or (item_rawfish09 and item_rawfish09 < day) or (item_rawfish10 and item_rawfish10 < day):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'Your sleep gets distorted by the foul smell coming from your bundles. The raw fish meat is now rotting. Its state will get worse with every day, but even now you struggle to imagine that you could continue your journey with this smell around.
                '
                'I throw it somewhere where it won’t bother anyone and get back to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw it somewhere where it won’t bother anyone and get back to sleep.')
                    if item_rawfish01 and item_rawfish01 < day:
                        $ item_rawfish01 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish02 and item_rawfish02 < day:
                        $ item_rawfish02 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish03 and item_rawfish03 < day:
                        $ item_rawfish03 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish04 and item_rawfish04 < day:
                        $ item_rawfish04 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish05 and item_rawfish05 < day:
                        $ item_rawfish05 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish06 and item_rawfish06 < day:
                        $ item_rawfish06 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish07 and item_rawfish07 < day:
                        $ item_rawfish07 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish08 and item_rawfish08 < day:
                        $ item_rawfish08 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish09 and item_rawfish09 < day:
                        $ item_rawfish09 = 0
                        $ item_rawfishtotalnumber -= 1
                    if item_rawfish10 and item_rawfish10 < day:
                        $ item_rawfish10 = 0
                        $ item_rawfishtotalnumber -= 1
                        $ renpy.notify("You have %s fish left." %item_rawfishtotalnumber)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                    jump sleepingfurther
        if pc_murdered and pc_murdered+1 < day and not sleep_dream_pc_murdered:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            if whitemarshes_destroyed:
                $ custom1 = "You’re holding a massive, heavy codex, and keep smashing {color=#f6d6bd}Orentius’{/color} head, again, and again. He prays, no matter how much blood covers you, the table, and the walls of your prison."
            menu:
                '[custom1]
                \n\nYou try to make the noise go away. For a few days now, The Land is insufferably loud.
                '
                'I just wish I {i}knew{/i} if I made the right decision.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just wish I {i}knew{/i} if I made the right decision.')
                    $ sleep_dream_pc_murdered = "doubt"
                    jump sleepingfurther
                'I feel pain in my chest. I should never have done it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I feel pain in my chest. I should never have done it.')
                    $ sleep_dream_pc_murdered = "regret"
                    jump sleepingfurther
                'Let’s hope no one outside the peninsula will learn the truth.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope no one outside the peninsula will learn the truth.')
                    $ sleep_dream_pc_murdered = "shame"
                    jump sleepingfurther
                'I may need to buy an amulet for bad dreams, that’s all.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no regrets. I may need to buy an amulet for bad dreams, that’s all.')
                    $ sleep_dream_pc_murdered = "noregret"
                    jump sleepingfurther
        if sleep_destination == "monasteryaftersleep" and not sleep_monastery:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ sleep_monastery = 1
            menu:
                'You listen to the wind, then to the stream, then fall asleep, unable to focus on your own thoughts.
                \n\nYou wake up after a couple of hours, disturbed by a loud clap of thunder, or was it a dragon’s roar? You can’t say. You spend some time awake, listening to the peaceful breathing of {color=#f6d6bd}[horsename]{/color} and rolling over in the old hay. You even take a brief walk indoors, stretching your arms and neck. You’re both anxious and tired, with dreams and thoughts merged in an incoherent, aimless mass of impressions and half-real noises.
                \n\nWhen you lie down, you feel paralyzed, struggling to take a deep breath. It takes a long time before you close your eyes, but even when it happens, you have the feeling that someone is watching you with a pair of bright, gray eyes.
                '
                'After waking up, I’m not sure which parts of the night truly happened.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- After waking up, I’m not sure which parts of the night truly happened.')
                    jump sleepingafterevent
        if (sleep_destination == "howlersdellwakinguphall" and thais_bigmad and pc_hp >= 2 and not thais_bigmad_beaten) or (sleep_destination == "howlersdellwakinguproom" and thais_bigmad and pc_hp >= 2 and not thais_bigmad_beaten):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
                play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ sleep_howlersdell = 1
            menu:
                'They wake you up with a punch to your face. You hit the floor, taking a few kicks to the stomach and one to the chin. A hand holds your shirt, a few others your legs and arms. They carry you downstairs, and you crash against every step. Blood flows down your nose.
                '
                'I cry for help.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cry for help.')
                    jump thais_bigmad_beaten01
                '“Don’t you know who I am?!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you know who I am?!”')
                    jump thais_bigmad_beaten01
                'I try to kick someone, anyone.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to kick someone, anyone.')
                    label thais_bigmad_beaten01:
                        $ pc_hp = limit_pc_hp(pc_hp-3)
                        show minus3hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                        if cleanliness_clothes_blood and cleanliness_clothes_torn:
                            show minus3appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
                        elif cleanliness_clothes_blood or cleanliness_clothes_torn:
                            show minus4appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
                        else:
                            show minus5appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 appearance points.{/i}')
                        $ cleanliness_clothes_blood = 1
                        $ cleanliness_clothes_torn = 1
                        $ cleanliness = limit_cleanliness(cleanliness-3)
                        if item_howlersdelltoken:
                            $ item_howlersdelltoken = 0
                            $ renpy.notify("You lost the “token of gratitude.”")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the “token of gratitude.”{/i}')
                        menu:
                            'Another hit has you choking on blood. You cough and gasp for air, and your skin rubs against sand and pebbles. You’re not sure how much time passes before you’re thrown into Howler’s Creek. You want to curl up in pain, but you have to keep your head above the surface. The stream is shallow and cold, and you soon climb up the bank, soaked and shaking.
                            \n\nYou flinch when one of the guards steps closer, but after he gives you a good look, he puts his hands on his sides. “{color=#f6d6bd}Thais’{/color} message delivered,” he announces, and his group follows him deeper into the village. A few people are observing you from a distance, but your tired eyes don’t recognize them.
                            \n\nYou somehow return to the dark entrance hall. {color=#f6d6bd}Eryx{/color} holds a candle and says nothing, but offers you a dry cloth. Your face begs for it.
                            '
                            'I walk by him and return to my spot. I go back to sleep with a knife in my hand.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk by him and return to my spot. I go back to sleep with a knife in my hand.')
                                jump thais_bigmad_beaten02
                            '“Thanks,” I say, and allow him to help me climb up the stairs.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks,” I say, and allow him to help me climb up the stairs.')
                                label thais_bigmad_beaten02:
                                    if sleep_destination == "howlersdellwakinguphall":
                                        $ day += 1
                                        $ quarters = 32
                                        $ pc_food = limit_pc_food(pc_food-2)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                        $ renpy.force_autosave(take_screenshot=True, block=True)
                                        jump howlersdellwakinguphall
                                    if sleep_destination == "howlersdellwakinguproom":
                                        $ day += 1
                                        $ quarters = 30
                                        $ pc_food = limit_pc_food(pc_food+1)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
                                        jump howlersdellwakinguproom
        if (sleep_destination == "howlersdellwakinguphall" and not sleep_howlersdell and pc_hp) or (sleep_destination == "howlersdellwakinguproom" and not sleep_howlersdell and pc_hp):
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ sleep_howlersdell = 1
            menu:
                'Your first sleep ends, but your usual one-hour break is instantly disrupted by noise. You stand up, walk to the window, and see the reason for the commotion - a group of workers is just outside the inn, drinking and laughing. {color=#f6d6bd}Eryx{/color} the innkeeper is also among them.
                \n\nYou could join them, but if you do so, you won’t get a good sleep tonight, and after such a long day you may end up exhausted.
                '
                'I just want to rest.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just want to rest.')
                    $ description_hovlavan19 = "During my time there, I’ve learned how to ignore drunken crowds while sleeping."
                    menu:
                        'During your time in {color=#f6d6bd}Hovlavan{/color} you learned how to ignore drunken crowds. You can relax and return to your routine.
                        '
                        'I sharpen my blade and go back to sleep.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sharpen my blade and go back to sleep.')
                            jump sleepingafterevent
                'It’s an opportunity to show that I’m not an outsider. I can sacrifice a bit of sleep.' if pc_hp:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s an opportunity to show that I’m not an outsider. I can sacrifice a bit of sleep.')
                    $ howlersdell_reputation += 1
                    $ description_creeks02 = "I heard that the locals are lighthearted and eager to have fun, and appreciate those who approach them with a smile."
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    menu:
                        'You lose track of time, surrounded by the smells of old ale and cold roast lamb. The excuse for having this celebration is the recent birth, the very same that was occurring when you arrived at the village. The young mother is exhausted and is the first one to leave, but more than ten people stay, poking at her partner with kind-hearted jokes. “Use the next week the best you can,” says one of them. “Nae sleep for you after that!”
                        \n\nYou may be a stranger, but your presence is welcomed with joy. The small talk is just as engaging as you’d expect from people who have already slept for three to four hours today, but there’s something pleasant about them sharing their parenthood stories and plans for the future. The humming of Howler’s Creek and the lights in the dark make you feel as if you {i}belong{/i} here, and that’s a delightful illusion, especially in a group of strangers.
                        \n\nAt one point you’re asked about your own journeys, though you prefer to keep most of them to yourself. One of the hunters encourages you strongly to travel to {color=#f6d6bd}Creeks{/color}. “They’re a fun bunch, you see. They love to meet new people, but be ready to wake up with a spinning head! ”
                        '
                        'I’m one of the first people to get back to bed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m one of the first people to get back to bed.')
                            jump sleepingafterevent
        if (sleep_destination == "foggylakeatticaftersleep" and not sleep_foggylake) or (sleep_destination == "foggylakegroundflooraftersleep" and not sleep_foggylake):
            $ sleep_foggylake = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The monstrous shouts wake you up. The night is bright, and from the window of the tavern, you have a good look at the yard.
                \n\nA few massive dragonlings are exploring the courtyard, knocking over wooden tools with their tails, putting their noses into buckets and underneath the stairs. You count five of them so far, but you can’t see the entire area at once.
                \n\nOne of them spots your look, and moves closer. Still, it doesn’t try to climb to the door - maybe it’s experienced enough to know it won’t get through.
                '
                'I close the shutter slowly.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I close the shutter slowly.')
                    jump sleepingafterevent
                'I go back to sleep with an axe in my hand.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to sleep with an axe in my hand.')
                    jump sleepingafterevent
                'I scoff and leave the shutter open. “Stupid lizard.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scoff and leave the shutter open. “Stupid lizard.”')
                    jump sleepingafterevent
        if (sleep_destination == "watchtoweraftersleep01" and not sleep_watchtower) or (sleep_destination == "watchtoweraftersleep01nobugs" and not sleep_watchtower):
            $ sleep_watchtower = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The scratching from the lower floor wakes you up. You get out of the blanket, and look down the ladder. The main door shakes. Just in case, you open a window and glance outside. A pale, muscular frightape tries to open the entrance with its massive hands, but to no avail. After it hears the screeching of a shutter, it looks at you with its dead, black eyes, then grabs one of the bricks and bounces up, shortening the distance quickly.
                \n\nYou lock the window with every bolt and bar it has, just in time to keep the shouting monster away. The ape punches the planks fiercely, then climbs even higher, looking for another entrance, but is incapable of recognizing the trapdoor, and, after another few minutes, you think it gave up.
                '
                'I breathe a sigh of relief and get back to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I breathe a sigh of relief and get back to sleep.')
                    jump sleepingafterevent
                'Just to be sure, I inspect every window and the main entrance.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Just to be sure, I inspect every window and the main entrance.')
                    jump sleepingafterevent
                'I smile. It will take a dragon to knock down this tower.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. It will take a dragon to knock down this tower.')
                    jump sleepingafterevent
        if (sleep_destination == "peltnorthaftersleeproom" and not sleep_peltnorth) or (sleep_destination == "peltnorthaftersleepfloor" and not sleep_peltnorth) or (sleep_destination == "peltnorthafterbansleep" and not sleep_peltnorth):
            $ sleep_peltnorth = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You hear a thunderous roar. You rise to your feet and rub the sleep from your eyes. The doors are opening, people are shouting orders and words of warning. As you open the window, you see what’s behind the commotion - something is on the other side of the wall, trying to get through, and the guards are fighting it off with their torches, spears, and crossbows. Thanks to their light, you see the large, furry paws placed on the top of the wall walk - as far as you can tell, the beast is but a single leap away from getting inside.
                '
                'I need to help them.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to help them.')
                    $ description_bighunters02 = "According to"
                    $ description_bighunters02b = ", they are cautious and value teamwork above all else."
                    menu:
                        'You look for your gambeson and blade, still a bit foggy in your thoughts, and once you find them, you struggle to get inside the jacket. As your habits kick in, you see the innkeeper right in front of you, holding a candle.
                        \n\n“You’re a guest, stay here,” he says without a shadow of hesitation. “My team has no time to worry about outsiders.”
                        \n\nJust after his words, you hear cheerful laughter from the wall. Judging by the way they point their fingers and lower their weapons, the beast is fleeing.
                        '
                        'Well, I shouldn’t expect people will need my help {i}all{/i} the time.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, I shouldn’t expect people will need my help {i}all{/i} the time.')
                            jump sleepingafterevent
                        'If I had been there, maybe we could have caught it.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- If I had been there, maybe we could have caught it.')
                            jump sleepingafterevent
                'It’s not their first night, they know what they’re doing.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not their first night, they know what they’re doing.')
                    menu:
                        'It surely looks so. The guards are organized like a group of dancers, switching positions swiftly and using words that mean nothing to you. They pierce the creature’s shell with their long weapons, and one of them does her best to chop through the furry paw with an axe. After maybe a minute, the beast gives up and takes its limb back, to the group’s cheerful laughter.
                        '
                        'Quite impressive.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Quite impressive.')
                            jump sleepingafterevent
                        'That’s the kind of skill I would expect from a team living in the middle of nowhere.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- That’s the kind of skill I would expect from a team living in the middle of nowhere.')
                            jump sleepingafterevent
        if (sleep_destination == "creeksaftersleep" and not creeks_sleep):
            $ creeks_sleep = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'Your first sleep ends and you take care of your regular chores, doing your best to not draw the attention of the crowded room. Once you get back on your pile of furs, it’s as comfortable as an inn bed, but it’s not easy for you to doze off.
                \n\nThe noises that reach you are difficult to misinterpret. A man and a woman are moaning, moving in their spot, though you see mostly darkness. After another few minutes similar sounds reach you from another spot.
                '
                'Cringe. I {i}really{/i} try to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Cringe. I {i}really{/i} try to sleep.')
                    jump sleepingafterevent
                '“Just a bit quieter,” I whisper.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just a bit quieter,” I whisper.')
                    menu:
                        'You’re answered by an awkward giggle. “Sorry, most folks are used to it!”
                        \n\nThe moans indeed stop, and the distant palette and furs don’t shake so hard.
                        '
                        'I focus on my breath.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on my breath.')
                            jump sleepingafterevent
                        'I sigh, struggling to sleep for another half an hour.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh, struggling to sleep for another half an hour.')
                            jump sleepingafterevent
                '...This isn’t too bad.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...This isn’t too bad.')
                    jump sleepingafterevent
        if (sleep_destination == "galerocksaftersleeplabor" and not sleep_galerocks) or (sleep_destination == "galerocksaftersleepmoney" and not sleep_galerocks):
            $ sleep_galerocks = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'After {color=#f6d6bd}Fulvia{/color} blows out the candles - without considering if you’re ready for it - you are in complete darkness, and you only now realize how quiet this room is. The thick walls block the humming of the wind, birds, the river. The keeper heads to her own room, and you only occasionally hear the whispers or snores of other dwellers.
                '
                'My imagination sculpts terrifying creatures in the darkness, and it takes me a while before I calm down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My imagination sculpts terrifying creatures in the darkness, and it takes me a while before I calm down.')
                    jump sleepingafterevent
                'I grow anxious as I focus on my breath, then on the beating of my heart.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grow anxious as I focus on my breath, then on the beating of my heart.')
                    jump sleepingafterevent
                'I hold on to my dagger, and focus on the touch of my blanket.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hold on to my dagger, and focus on the touch of my blanket.')
                    jump sleepingafterevent
                'Finally some peace.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally some peace.')
                    jump sleepingafterevent
        if (sleep_destination == "whitemarshesaftersleep" and not sleep_whitemarshes) and not whitemarshes_nomoreundead and not thyrsus_orentius_canhelp and not whitemarshes_nomoreundeadfirstsleepdescription:
            $ sleep_whitemarshes = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ description_whitemarshes14 = "The locals’ necromantic “talents” are at least partially substituted by blood magic."
            menu:
                'A persistent, shouting voice wakes you up. Weak moonbeams squeeze through the smoke holes, but to have a proper look around, you open the door. There are flickering torches at the main gate, accompanied by a solemn prayer and timid shouts.
                \n\nYou put on your cloak and boots and leave the shed. A few of the locals, dressed in their regular worn and muddy clothes, surround a large group of the undead, touching their half-rotten limbs, revealed rib cages, emotionless heads. A hooded woman sonorously, singingly begs for Wright’s guidance and protection, but you don’t pay much attention to her words.
                \n\nThe man known as {color=#f6d6bd}Orentius{/color} is standing beside the gathering, with a revealed torso and a walking stick beneath his shoulder. Every now and then, he cuts his sides or his back, and fills a wooden bowl slightly. Then, a follower steps closer, puts two fingers inside the liquid, and takes it to one of the awoken creations. The lights dance around them, casting shadows that you could swear hide cruel spirits.
                \n\nYou don’t know how long you had been observing the ritual when the scar-covered man turns toward you. His innocent, sad eyes carry no judgment or reprimand, yet you suddenly notice how cold your calves and neck are. Autumn is surely getting closer.
                \n\nYou wade through the mud.
                '
                'What has happened to them that they feel justified in doing all this?':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What has happened to them that they feel justified in doing all this?')
                    if glaucia_about_spyonnecromancers == 1 and not whitemarshes_spying_completed:
                        $ custom5 = "Before you reach the door, you think about {color=#f6d6bd}Glaucia’s{/color} request. You saw no one on your way, so could spend some time looking around, though by doing so you won’t get much sleep."
                        jump whitemarshestryingtospy02
                    else:
                        jump sleepingafterevent
                'So not only do they awake the dead, they use blood magic... If The United Church learns about this, they won’t let it go.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- So not only do they awake the dead, they use blood magic... If The United Church learns about this, they won’t let it go.')
                    if glaucia_about_spyonnecromancers == 1 and not whitemarshes_spying_completed:
                        $ custom5 = "Before you reach the door, you think about {color=#f6d6bd}Glaucia’s{/color} request. You saw no one on your way, so you could spend some time looking around, though by doing so you won’t get much sleep."
                        jump whitemarshestryingtospy02
                    else:
                        jump sleepingafterevent
                'Let’s hope they’ll let me leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope they’ll let me leave this place.')
                    if glaucia_about_spyonnecromancers == 1 and not whitemarshes_spying_completed:
                        $ custom5 = "Before you reach the door, you think about {color=#f6d6bd}Glaucia’s{/color} request. You saw no one on your way, so you could spend some time looking around, though by doing so you won’t get much sleep."
                        jump whitemarshestryingtospy02
                    else:
                        jump sleepingafterevent
                'These people are beyond redemption. Fanatics.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- These people are beyond redemption. Fanatics.')
                    if glaucia_about_spyonnecromancers == 1 and not whitemarshes_spying_completed:
                        $ custom5 = "Before you reach the door, you think about {color=#f6d6bd}Glaucia’s{/color} request. You saw no one on your way, so you could spend some time looking around, though by doing so you won’t get much sleep."
                        jump whitemarshestryingtospy02
                    else:
                        jump sleepingafterevent
        if sleep_destination == "whitemarshesaftersleep" and glaucia_about_spyonnecromancers == 1 and not whitemarshes_spying_completed and not whitemarshes_nomoreundead and not thyrsus_orentius_canhelp and not whitemarshes_nomoreundeadfirstsleepdescription:
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ custom5 = "It’s still dark outside, and oddly quiet. You think about {color=#f6d6bd}Glaucia’s{/color} request - you could spend some time looking around, though by doing so you won’t get much sleep."
            label whitemarshestryingtospy02:
                $ quarters = 95
                show areapicture whitemarshes01night at basicfade
                stop nature fadeout 4.0
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                menu:
                    '[custom5]
                    '
                    'I need to examine the local defences.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to examine the local defences.')
                        $ whitemarshes_spying_completed = 1
                        show areapicture whitemarshes01night at basicfade
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        $ renpy.notify("Journal updated: Spy on White Marshes")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Spy on White Marshes{/i}')
                        menu:
                            'You underestimated how difficult it would be to cross the many puddles and muddy alleys of the village. You seek silent routes, try to hide from patrols - some of which may already be dead - and sometimes spend a few minutes crouching in the dark, waiting for the right time to walk away.
                            \n\nOnce you get back, you recollect your observations. The guards seem weak, almost sickly; a few spots in the walls could be crossed, but the entire backside of the village is surrounded by water; the houses won’t be taken down with fire easily; there are no obvious observation posts; the undead carry no equipment...
                            \n\nAside from the sheer number of potential enemies, the village is weak.
                            '
                            'It may be better to strike them quickly, before it’s too late.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be better to strike them quickly, before it’s too late.')
                                jump sleepingafterevent
                            'I’m not sure if {color=#f6d6bd}Glaucia{/color} should really learn about it. She may go too far.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not sure if {color=#f6d6bd}Glaucia{/color} should really learn about it. She may go too far.')
                                jump sleepingafterevent
                            'I’m just following orders. I wash my boots before I lie down.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m just following orders. I wash my boots before I lie down.')
                                jump sleepingafterevent
                    'I just go back to sleep.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just go back to sleep.')
                        jump sleepingafterevent
        if sleep_destination == "whitemarshesaftersleep" and not whitemarshes_nomoreundead and not orentius_spared and thyrsus_orentius_canhelp and not whitemarshes_nomoreundeadfirstsleepdescription:
            $ thyrsus_orentius_helped = 1
            $ quarters = 95
            show areapicture whitemarshes01night at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg":
                play music "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The door opens gently. You recognize {color=#f6d6bd}Thyrsus’{/color} silhouette, even though he has no creepers with him, together with a few hooded figures behind the threshold. Once he makes sure you’re awake, he also covers his head.
                \n\n“Quick, we’ve little time,” he whispers. “Dress up, axe behind. We’ll move your things onto the saddles, just in case.” He stands up and, just like his companions, starts to observe his surroundings.
                \n\nAlready prepared, you only need a few breaths. Finally, your hand touches the dagger in your boots.
                '
                'Words may not be enough to solve this.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Words may not be enough to solve this.')
                    $ orentius_dagger = 1
                    jump whitemarshesorentius01
                'I may need it to defend myself.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may need it to defend myself.')
                    $ orentius_dagger = 1
                    jump whitemarshesorentius01
                'I just have to speak with him. I leave it behind.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just have to speak with him. I leave it behind.')
                    jump whitemarshesorentius01
        if (sleep_destination == "greenmountaintribeaftersleep" and not sleep_greenmountaintribe):
            $ sleep_greenmountaintribe = 1
        if day >= 1 and not sleep_dream01:
            $ sleep_dream01 = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'Like most people, you wake in the middle of almost every night. Before your second sleep comes, you spend an hour or two taking care of your belongings, shell, and soul. Some people spend this time with their friends, families, or lovers, but your routine is different. If you don’t have to take care of essential tasks...
                '
                '...I stretch my muscles, work out a bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I stretch my muscles, work out a bit.')
                    jump sleepingafterevent
                '...I spend some time outside, observing stars and listening to the wild creatures.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I spend some time outside, observing stars and listening to the wild creatures.')
                    jump sleepingafterevent
                '...I check on {color=#f6d6bd}[horsename]{/color}. It’s a good time to brush it and make sure it has everything it needs.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I check on {color=#f6d6bd}%s{/color}. It’s a good time to brush it and make sure it has everything it needs.' %horsename)
                    jump sleepingafterevent
                '...it’s the best time to pray and think about my dreams.' if pc_religion != "none" and pc_religion != "none":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...it’s the best time to pray and think about my dreams.')
                    $ pc_faithpoints += 1
                    jump sleepingafterevent
                '...I just stay where I am, trying to ease my soul and focus on my breathing. I feel anxious during this time.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I just stay where I am, trying to ease my soul and focus on my breathing. I feel anxious during this time.')
                    jump sleepingafterevent
        if sleep_dream01 and not sleep_dream02 and day != 7:
            $ sleep_dream02 = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'It’s a calm, warm night. As your first sleep ends, you stretch out and prepare yourself for an active hour or two. It’s time to take care of some things that must be done at least once every few days, though they are a bit more challenging than your nightly routine.
                '
                'It’s time for my training. I practice cuts, stances, dodges, and steps, but also inspect every blade I own.' if pc_class == "warrior":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time for my training. I practice some attacks, stances, dodges, and steps, but also inspect every blade I own.')
                    jump sleepingafterevent
                'I gather my amulets and focus on my breath, practicing how the pneuma flows through my shell.' if pc_class == "mage":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my amulets and focus on my breath, practicing how the pneuma flows through my shell.')
                    jump sleepingafterevent
                'It’s time to check on my herbs and other ingredients. I get rid of the plants that have failed to dry out, throw away anything that’s rotten, and wash my jars before I fill them up again.' if pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to check on my herbs and other ingredients. I get rid of the plants that have failed to dry out, throw away anything that’s rotten, and wash my jars before I fill them up again.')
                    jump sleepingafterevent
        if sleep_dream02 and not sleep_dream03 and pc_hp <= 2 and day != 7:
            $ sleep_dream03 = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You lose your senses right after you lie down. In the middle of the warm, stuffy night you are entangled by your dreams, too tired to fully wake up, too accustomed to having a mid-sleep break to just get back to sleep.
                \n\nYou are between the realms, surrounded by visions so vivid you are tempted to reach out, touch them, and stretch them out. They are your playground.
                '
                'Once I realize I’m in power, I do my best to enjoy myself. I fly, defeat dragons, eat and drink whatever I want.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once I realize I’m in power, I do my best to enjoy myself. I fly, defeat dragons, eat and drink whatever I want.')
                    jump sleepingafterevent
                'I wouldn’t dare to disturb the natural flow of dreams. I accept them as they are, hoping to spot any visions they bring.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wouldn’t dare to disturb the natural flow of dreams. I accept them as they are, hoping to spot any visions they bring.')
                    jump sleepingafterevent
                'No matter how much I try, my nightmares interfere with even the most joyful dreams. I wake up sweating, gasping for air.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- No matter how much I try, my nightmares interfere with even the most joyful dreams. I wake up sweating, gasping for air.')
                    jump sleepingafterevent
                'I try to break free of this state, thinking of all the things I was meant to do tonight. When I wake up, I’m still not sure if I did anything at all.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to break free of this state, thinking of all the things I was meant to do tonight. When I wake up, I’m still not sure if I did anything at all.')
                    jump sleepingafterevent
        if sleep_dream03 and not sleep_dream04:
            $ sleep_dream04 = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The moon is bright, and so is the night. You recognize shapes of owls and bats, and spot movements on the ground.
                \n\nThere are many stories about the moon’s origins and purpose, and they’re older than any of the doctrines known in The Cities. These legends are shared not by religions, but rather by tribes, as if they’re a part of a deeper conviction, something spread through the milk of mothers and wet nurses, or through the whispers of the trees and winds.
                '
                'The moon is a powerful spirit who watches and guides humankind when we have no sun to protect us. That’s why we call what’s in its center {i}The Eye{/i}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The moon is a powerful spirit who watches and guides humankind when we have no sun to protect us. That’s why we call what’s in its center {i}The Eye{/i}.')
                    jump sleepingafterevent
                'It’s a large rock that one day will fall from the sky and crush everything that’s alive, starting a new age of darkness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a large rock that one day will fall from the sky and crush everything that’s alive, starting a new age of darkness.')
                    jump sleepingafterevent
                'For some reason, it controls the weather. It gathers weak clouds like a shepherd, and shapes the tides.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- For some reason, it controls the weather. For some reason, it controls the weather. It gathers weak clouds like a shepherd, and shapes the tides.')
                    jump sleepingafterevent
                'It’s a home of strange animals. They are different, but as bright as humans, and sometimes visit The Land.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a home of strange animals. They are different, but as bright as humans, and sometimes visit The Land.')
                    jump sleepingafterevent
                '...the moon is up there, and we are here, now. Who cares what it hides?':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...the moon is up there, and we are here, now. Who cares what it hides?')
                    jump sleepingafterevent
        if sleep_dream04 and not sleep_dream05 and pc_area != "druidcave" and pc_area != "greenmountaintribe" and not weathermud and not weatherfog:
            $ sleep_dream05 = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'Hardly any light reaches the ground through the clouded sky. The {i}deep night{/i}, as some people call it. So dark that you can’t see the fingertips of your extended hand.
                \n\nYou try to look outside, but to no avail. Even the predators will spend the next few hours hidden, unsure what surrounds their shelters and hideouts. Not all of them, though. You hear cheerful howling coming from the heart of the forest - a huntqueen, or maybe a huntlord, has already captured its next meal.
                '
                'I can’t stay on watch the entire night, but before my second sleep, I sit still with a single candle, looking for anything that may try to get inside.' if pc_area != "militarycamp" and pc_area != "peltnorth" and pc_area != "druidcave" and pc_area != "howlersdell" and pc_area != "monastery" and pc_area != "watchtower" and pc_area != "eudociahouse" and pc_area != "eudociahouseinside" and pc_area != "greenmountaintribe" and pc_area != "whitemarshes" and pc_area != "galerocks" and pc_area != "creeks":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t stay on watch the entire night, but before my second sleep, I sit still with a single candle, looking for anything that may try to get inside.')
                    jump sleepingafterevent
                'I can’t stay on watch the entire night, but before my second sleep, I sit still with a single candle, looking for anything that may try to get inside.' if pc_area == "militarycamp":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t stay on watch the entire night, but before my second sleep, I sit still with a single candle, looking for anything that may try to get inside.')
                    jump sleepingafterevent
                'I should feel safe in such a well-guarded stronghold... But just in case, I crawl to the window and make sure it’s closed.' if pc_area == "peltnorth":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should feel safe in such a well-guarded stronghold... But just in case, I crawl to the window and make sure it’s closed.')
                    jump sleepingafterevent
                'I don’t think any monster will get through such a heavy door... But just in case, I light a candle.' if pc_area == "druidcave":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t think any monster will get through such a heavy door... But just in case, I light a candle.')
                    jump sleepingafterevent
                'I should feel safe in such a well-guarded village... But just in case, I crawl to the window and make sure it’s closed.' if pc_area == "howlersdell" or pc_area == "galerocks" or pc_area == "whitemarshes" or pc_area == "creeks":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should feel safe in such a well-guarded village... But just in case, I crawl to the window and make sure it’s closed.')
                    jump sleepingafterevent
                'Listening to the howling wind makes this time even harder. I hardly get any sleep.' if pc_area == "monastery":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Listening to the howling wind makes this time even harder. I hardly get any sleep.')
                    jump sleepingafterevent
                'I light a candle and push one of the heavy barrels under the door.' if pc_area == "watchtower" and watchtower_open != "axe":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light a candle and push one of the heavy barrels under the door.')
                    jump sleepingafterevent
                'I light a candle and add another heavy barrel to my barricade.' if pc_area == "watchtower" and watchtower_open == "axe":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light a candle and add another heavy barrel to my barricade.')
                    jump sleepingafterevent
                'I know the golems will protect their master, but just in case, I sit still with a single candle, looking for anything that may try to get inside.' if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know the golems will protect their master, but just in case, I sit still with a single candle, looking for anything that may try to get inside.')
                    jump sleepingafterevent
        # if sleep_dream05 and not sleep_dream06:
        #     $ sleep_dream07 = 1
        #     $ quarters = 95
        #     show areapicture nightsky01 at basicfade
            # stop nature fadeout 4.0
            # if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                # play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
        #     nvl clear
        #     with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        #     menu:
        #         '
        #         \n\n
        #         '
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             jump sleepingafterevent
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             jump sleepingafterevent
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             jump sleepingafterevent
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             jump sleepingafterevent
        if ruinedvillage_truth and howlersdell_firsttime and not sleep_dream_steephouse and not quest_ruins_choice:
            $ sleep_dream_steephouse = 1
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You are in the labyrinth of alleys in {color=#f6d6bd}Steep House{/color}, which shifts after every step. You wander by the blooming gardens, burning houses, laughing newlyweds, cut-off limbs, fresh hare pies, chewed bones, carts loaded with barrels, and falling trees.
                \n\nYou’re sitting at a table in front of the {color=#f6d6bd}Ape Ale{/color} inn, surrounded by laughing skeletons. {color=#f6d6bd}Thais{/color}, naked and covered in blood and ashes, holds your hand, forcing you to stuff your mouth with raw meat from a bottomless bowl. Every bite, tasting like the metal of an old key, burns your mouth, but you can’t scream. The unyielding grasp brings pain and delight in equal measure, and you wouldn’t dare to try to escape it. The smoke coming from your roasting flesh starts to fill your eyes, but they have no tears to spare.
                \n\nYou wake up and reach for a water skin so you can rinse the ash from your hand. It takes you a few heartbeats before you realize where you are.
                '
                'Those monsters. If there was justice in this world, they would face the gravest punishment.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Those monsters. If there was justice in this world, they would face the gravest punishment.')
                    jump sleepingafterevent
                'The villagers wouldn’t have agreed to it if they knew what was to come. {color=#f6d6bd}Thais{/color} lied to them, and she’s the one who bears the responsibility.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The villagers wouldn’t have agreed to it if they knew what was to come. {color=#f6d6bd}Thais{/color} lied to them, and she’s the one who bears the responsibility.')
                    jump sleepingafterevent
                'I’ve only seen one side of the story. I’m sure the people of {color=#f6d6bd}Howler’s{/color} felt they were justified, and things just got out of control.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve only seen one side of the story. I’m sure the people of {color=#f6d6bd}Howler’s{/color} felt they were justified, and things just got out of control.')
                    jump sleepingafterevent
                'Another stupid dream. I go back to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Another stupid dream. I go back to sleep.')
                    jump sleepingafterevent
        if pc_battlecounter >= 6 and not sleep_dream_pc_battlecounter:
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'You notice it while you undress. One of your recent wounds is going to leave a mark.
                '
                'I first notice it by touch, then see it in the reflection on my blade. A long cut on my cheek.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I first notice it by touch, then see it in the reflection on my blade. A long cut on my cheek.')
                    $ sleep_dream_pc_battlecounter = "cheek"
                    jump sleepingafterevent
                'The deep cut in my hand still hurts, especially when I make a fist.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The deep cut in my hand still hurts, especially when I make a fist.')
                    $ sleep_dream_pc_battlecounter = "hand"
                    jump sleepingafterevent
                'I manage to ignore it, but the cut on my leg hurts with every step.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I manage to ignore it, but the cut on my leg hurts with every step.')
                    $ sleep_dream_pc_battlecounter = "leg"
                    jump sleepingafterevent
                'The bruises on my stomach look like a night sky.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bruises on my stomach look like a night sky.')
                    $ sleep_dream_pc_battlecounter = "stomach"
                    jump sleepingafterevent
                'Why would I care? It happens to all travelers, given enough time. Let’s just keep it clean.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Why would I care? It happens to all travelers, given enough time. Let’s just keep it clean.')
                    $ sleep_dream_pc_battlecounter = "whatever"
                    jump sleepingafterevent

    label sleepingafterevent:
        if not weathermud:
            $ sleepingreloaddistances = 1
            jump finaldestinationmuddistances
        else:
            jump sleepingafterevent2
    label sleepingafterevent2:
        scene empty #part A of...
        scene layoutfull #part B of hididng all images
        nvl clear
        $ sleep_inprogress = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ can_potions = 0
        $ questionpreset = 0
        $ day += 1
        if day == world_deadline:
            $ world_endmode = 1
        if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
            $ world_daylength -= 1
        if world_endmode_howlers:
            $ world_endmode_howlers = 0
            jump sleeping_endmode
        if persistent.demomode and day >= 6:
            $ quarters = 95
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            menu:
                'The further journey is not available in the demo. Thank you for your support and please add {color=#f6d6bd}Roadwarden{/color} to your wishlist on Steam!
                '
                'Move to main menu.':
                    $ MainMenu(confirm=False)()
        if day == (world_deadline/2) and not sleep_reminder_day15: # ((world_deadline+1)/2)
            $ quarters = 95
            $ sleep_reminder_day15 = 1
            $ custom1 = ((world_deadline+1)/2)
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'The halfway point is behind you. In just [custom1] days, you’ll need to ride back to {color=#f6d6bd}Hovlavan{/color}, otherwise the roads will get too dangerous for a lone rider.
                '
                'I just need to hope {color=#f6d6bd}Tulia{/color} can make it until autumn.' if travel_destination == "militarycamp" and not militarycamp_destroyed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just need to hope {color=#f6d6bd}Tulia{/color} can make it until autumn.')
                'I could also speak with {color=#f6d6bd}Tulia{/color}. Maybe she’ll be willing to head to the city earlier.' if travel_destination != "militarycamp" or militarycamp_destroyed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could also speak with {color=#f6d6bd}Tulia{/color}. Maybe she’ll be willing to head to the city earlier.')
        if day == (world_deadline-5) and not sleep_reminder_day25:
            $ quarters = 95
            $ sleep_reminder_day25 = 1
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'Five days left. If the peninsula hides any more secrets, you may not have enough time to unravel them.
                '
                'Then I shouldn’t waste another hour.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Then I shouldn’t waste another hour.')
                'Safety comes first.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Safety comes first.')
        if day == (world_deadline-1) and not sleep_reminder_day29:
            $ quarters = 95
            $ sleep_reminder_day29 = 1
            show areapicture nightsky01 at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                nvl clear
            menu:
                'It’s the last day of your journey. You feel it in your muscles - after a good winter of rest, you could become quite a rider.
                '
                'Tomorrow morning, I’ll head to {color=#f6d6bd}Tulia{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Tomorrow morning, I’ll head to {color=#f6d6bd}Tulia{/color}.')
        nvl clear
        if sleep_destination == "prolcamp01regularaftersleeping":
            if item_asterioncloak:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana-0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            else:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana-1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump prolcamp01regularaftersleeping
        if sleep_destination == "peltnorthafterbansleep":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump peltnorthaftersleepfloor
        if sleep_destination == "peltnorthaftersleepfloor":
            if item_asterioncloak:
                $ quarters = 25
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 27
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump peltnorthaftersleepfloor
        if sleep_destination == "peltnorthaftersleeproom":
            if item_asterioncloak:
                $ quarters = 22
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-0)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-0 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness+3)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump peltnorthaftersleeproom
        if sleep_destination == "druidcavecavernwakingup":
            if not sleep_druidcave:
                $ sleep_druidcave = 1
            if item_asterioncloak:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump druidcavecavernwakingup
        if sleep_destination == "howlersdellwakinguphall":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 27
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump howlersdellwakinguphall
        if sleep_destination == "howlersdellwakinguproom":
            if item_asterioncloak:
                $ quarters = 22
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food+1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness+3)
            $ cleanliness_clothes_blood = 0
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump howlersdellwakinguproom
        if sleep_destination == "monasteryaftersleep":
            if item_asterioncloak:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+5)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+5 pneuma.{/i}')
            else:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump monasterywakingupshed
        if sleep_destination == "watchtoweraftersleep01":
            $ quarters = 30
            if pc_food >= 2:
                if healingritual_using:
                    $ healingritual_counter += 1
                    $ healingritual_using = 0
                    $ pc_hp = limit_pc_hp(pc_hp+1)
                    $ mana = limit_mana(mana+0)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                else:
                    $ pc_hp = limit_pc_hp(pc_hp+0)
                    $ mana = limit_mana(mana+2)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-3)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump watchtoweraftersleep01
        if sleep_destination == "watchtoweraftersleep01nobugs":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump watchtoweraftersleep01nobugs
        if sleep_destination == "eudociahouseaftersleep":
            if not sleep_eudociahouse:
                $ sleep_eudociahouse = 1
            if item_asterioncloak:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump eudociahouseaftersleep
        if sleep_destination == "foggylakegroundflooraftersleep":
            if item_asterioncloak:
                $ quarters = 30
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            else:
                $ quarters = 32
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana-1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump foggylakegroundflooraftersleep
        if sleep_destination == "foggylakeatticaftersleep":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump foggylakeatticaftersleep
        if sleep_destination == "creeksaftersleep":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+4)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump creeksaftersleep01
        if sleep_destination == "creeksaftersleep2resting":
            $ healingritual_using = 0
            if item_asterioncloak:
                $ quarters = 28
                $ pc_hp = limit_pc_hp(pc_hp+3)
                $ mana = limit_mana(mana+5)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 30
                $ pc_hp = limit_pc_hp(pc_hp+2)
                $ mana = limit_mana(mana+4)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump creeksaftersleep2resting
        if sleep_destination == "creeksaftersleep2food":
            $ healingritual_using = 0
            if item_asterioncloak:
                $ quarters = 30
                $ pc_hp = limit_pc_hp(pc_hp+1)
                $ mana = limit_mana(mana+3)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 32
                # $ pc_hp = limit_pc_hp(pc_hp+0)
                $ mana = limit_mana(mana+2)
                # $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            # $ pc_food = limit_pc_food(pc_food-2)
            # $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump creeksaftersleep02food
        if sleep_destination == "creeksaftersleep2chatting":
            $ healingritual_using = 0
            if item_asterioncloak:
                $ quarters = 28
                $ pc_hp = limit_pc_hp(pc_hp+2)
                $ mana = limit_mana(mana+4)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 30
                $ pc_hp = limit_pc_hp(pc_hp+1)
                $ mana = limit_mana(mana+3)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump creeksaftersleep2chatting
        if sleep_destination == "creeksaftersleep2sex":
            $ healingritual_using = 0
            if item_asterioncloak:
                $ quarters = 28
                $ pc_hp = limit_pc_hp(pc_hp+2)
                $ mana = limit_mana(mana+4)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 pneuma.{/i}')
            else:
                $ quarters = 30
                $ pc_hp = limit_pc_hp(pc_hp+1)
                $ mana = limit_mana(mana+3)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump creeksaftersleep2sex
        if sleep_destination == "galerocksaftersleeplabor":
            if item_asterioncloak:
                $ quarters = 40
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 42
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-3)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump galerocksaftersleeplabor
        if sleep_destination == "galerocksaftersleepmoney":
            if item_asterioncloak:
                $ quarters = 24
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+3)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
            else:
                $ quarters = 26
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+3)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality points.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump galerocksaftersleepmoney
        if sleep_destination == "whitemarshesaftersleep":
            if item_asterioncloak:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            else:
                $ quarters = 30
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana-1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump whitemarshesaftersleep
        if sleep_destination == "greenmountaintribeaftersleep":
            if item_asterioncloak:
                $ quarters = 28
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        $ mana = limit_mana(mana+0)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana+2)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
            else:
                $ quarters = 30
                if pc_food >= 2:
                    if healingritual_using:
                        $ healingritual_counter += 1
                        $ healingritual_using = 0
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        $ mana = limit_mana(mana-1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 pneuma.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp+0)
                        $ mana = limit_mana(mana+1)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 pneuma.{/i}')
            $ pc_food = limit_pc_food(pc_food-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ renpy.force_autosave(take_screenshot=True, block=True)
            if world_endmode:
                jump sleeping_endmode
            jump greenmountaintribeaftersleep

    label sleeping_endmode:
        scene empty #part A of...
        scene layoutfull #part B of hididng all images
        nvl clear
        $ quarters = 36
        show areapicture nightsky01 at basicfade
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
            play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
        if whitemarshes_nomoreundeadfirstsleepdescription == 1:
            $ whitemarshes_nomoreundeadfirstsleepdescription = 0
            $ whitemarshes_nomoreundead = day
            $ orentius_convinced = 1
            $ quest_orentius = 2
            if pc_goal == "iwanttoberemembered":
                $ pc_goal_iwanttoberememberedpoints += 2
            if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                $ renpy.notify("Quest completed: Orentius, the Necromancer.\nJournal updated: %s" %quest_pc_goal_name)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer. Journal updated: %s{/i}' %quest_pc_goal_name)
            else:
                $ renpy.notify("Quest completed: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
            if thyrsus_orentius_helped:
                $ quest_orentius_thyrsus_description03 = "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
            if helvius_orentius_helped:
                $ quest_orentius_helvius_description03 = "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
            menu:
                'You wake up to the terrible stench of burning, rotten flesh. Once you leave the shed, you head to {color=#f6d6bd}[horsename]{/color} - it’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}.
                \n\nAs you spend a few minutes to help it relax, you finally realize there are no undead in sight - the pyres beneath their gathered corpses are far away, in the back of the village, but the flames and smoke are visible even from a great distance.
                \n\nThere’s a large group surrounding {color=#f6d6bd}Orentius’{/color} house. The rumor reaches you on its own quickly - soon after the first awoken was touched by fire, the priest collapsed. He now mutters through his visions, but doesn’t wake up.
                \n\nIt’s time for you to leave.
                '
                'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if militarycamp_destroyed_firsttime_tulia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                    $ travel_destination = "peltnorth"
                    jump finaldestinationafterevent
                'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                    $ travel_destination = "peltnorth"
                    jump finaldestinationafterevent
                'Time to return to the camp.' if not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to return to the camp.')
                    $ travel_destination = "southerncrossroads"
                    jump finaldestinationafterevent
        elif sleep_destination == "peltnorthafterbansleep" or sleep_destination == "peltnorthaftersleepfloor" or sleep_destination == "peltnorthaftersleeproom":
            menu:
                'You wake up later than usual, then think about feeding {color=#f6d6bd}[horsename]{/color}. It’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}.
                '
                'I get up and look for {color=#f6d6bd}Tulia{/color}.' if sleep_destination == "peltnorthafterbansleep" or sleep_destination == "peltnorthaftersleepfloor":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get up and look for {color=#f6d6bd}Tulia{/color}')
                    $ can_leave = 0
                    $ can_rest = 0
                    $ can_items = 0
                    show areapicture peltnorth01inside at basicfade
                    hide peltnorthbronzerod
                    if tulia_friendship >= 10:
                        $ custom1 = "She’s waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a smile. “I’m sure glad I don’t have to leave by myself.”"
                    else:
                        $ custom1 = "She’s waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a kind nod. “Today is the day, I believe.”"
                    nvl clear
                    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                    $ renpy.force_autosave(take_screenshot=False, block=True)
                    jump peltnorth_tulia01regularquestionsafter
                'I go downstairs and look for {color=#f6d6bd}Tulia{/color}.' if sleep_destination == "peltnorthaftersleeproom":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go downstairs and look for {color=#f6d6bd}Tulia{/color}.')
                    $ can_leave = 0
                    $ can_rest = 0
                    $ can_items = 0
                    show areapicture peltnorth01inside at basicfade
                    hide peltnorthbronzerod
                    if tulia_friendship >= 10:
                        $ custom1 = "She’s waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a smile. “I’m sure glad I don’t have to leave by myself.”"
                    else:
                        $ custom1 = "She’s waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a kind nod. “Today is the day, I believe.”"
                    nvl clear
                    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                    $ renpy.force_autosave(take_screenshot=False, block=True)
                    jump peltnorth_tulia01regularquestionsafter
        else:
            menu:
                'You wake up later than usual, then head to {color=#f6d6bd}[horsename]{/color} slowly. It’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}.
                '
                'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if militarycamp_destroyed_firsttime_tulia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                    $ travel_destination = "peltnorth"
                    jump finaldestinationafterevent
                'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                    $ travel_destination = "peltnorth"
                    jump finaldestinationafterevent
                'Time to return to the camp.' if not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to return to the camp.')
                    $ travel_destination = "southerncrossroads"
                    jump finaldestinationafterevent
