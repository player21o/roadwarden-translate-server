################################# ENDING THE GAME
default endgame_mode = 0
default endgame_asterion_invitation = 0
default endgame_newlife_selected = 0
default endgame_epilogue_evil = 0
default endgame_skip_villages = 0
default endgame_epilogue_fluff = ""
default endgame_creeks_destroyed = 0
default endgame_foggy_destroyed = 0
default endgame_monastery_survived = 0
default endgame_howlers_destroyed = 0

default endgame_howlersdell_leader_points = 0
default endgame_oldpagos_leader_points = 0
default endgame_whitemarshes_leader_points = 0
default endgame_creeks_leader_points = 0
default endgame_galerocks_leader_points = 0

default endgame_howlersdell_leader_option = 0
default endgame_oldpagos_leader_option = 0
default endgame_whitemarshes_leader_option = 0
default endgame_creeks_leader_option = 0
default endgame_galerocks_leader_option = 0

default epilogue_bonus_savings_tier = 0
default epilogue_bonus_equipment_tier = 0
default epilogue_bonus_equipment_points = 0

label hovlavan_roadALL:
    label hovlavan_road01:
        hide areapicture
        scene empty
        scene layoutfull
        $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        stop nature fadeout 4.0
        $ endgame_mode = 1
        $ attitudes = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        hide screen characterstatus
        nvl clear
        if pc_dead:
            # $ endgame_epilogue_fluff = ""
            $ quest_explorepeninsula_result = "fail1"
            jump epilogue_slides01
        jump hovlavan_road02

    label hovlavan_road02:
        show areapicture ep_01 at basicfade
        nvl clear
        with Fade(1.8, 1.5, 1.8, color="#0f2a3f")
        if tulia_about_bandits_grateful and tulia_friendship >= tulia_about_highisland_recruited_threshold:
            $ custom1 = "You spend the night in a proper bed, holding a mug of steaming pigeon soup - this time around, {color=#f6d6bd}Tulia{/color} pays for the stay. She’s a good companion, willing to share the discomforts of the road and to kill boredom with an idle chat." # _("You spend the night in a proper bed, holding a mug of steaming pigeon soup - this time around, {color=#f6d6bd}Tulia{/color} pays for the stay. She’s a good companion, willing to share the discomforts of the road and to kill boredom with an idle chat.")
        elif coins >= 10:
            $ custom1 = "This time around, you’ve got a few dragon bones to spare, and you spend the night in a proper bed, holding a mug of steaming pigeon soup."
        else:
            $ custom1 = "Once again, your pouch is light, and you have to spend the night in the common room, chewing on watered-down gruel."
        if tulia_about_bandits_grateful:
            if tulia_friendship >= tulia_about_highisland_recruited_threshold:
                $ custom2 = ""
            elif tulia_friendship >= 6:
                $ custom2 = " Still, she’s a good companion, eager to kill boredom with an idle chat."
            elif tulia_friendship >= 2:
                $ custom2 = " She’s a good companion, a bit quiet, but resourceful."
            elif tulia_friendship >= 0:
                $ custom2 = " She’s a good companion, though you discuss only the most crucial events."
            else:
                $ custom2 = " Most of the time she keeps to herself, but at least she’s resourceful."
        elif tulia_about_bandits_hopeless:
            if tulia_friendship >= 6:
                $ custom2 = " She’s a good companion, a bit quiet, but resourceful. Judging by what you overheard in one of the villages you passed through, she’s eager to find another job."
            elif tulia_friendship >= 2:
                $ custom2 = " She’s a good companion, though you discuss only the most crucial events. Judging by what you overheard in one of the villages you passed through, she’s eager to find another job."
            else:
                $ custom2 = " Most of the time she keeps to herself, but at least she’s resourceful. Judging by what you overheard in one of the villages you passed through, she’s eager to find another job."
        elif tulia_about_bandits_indebt:
            if tulia_friendship >= tulia_about_highisland_recruited_threshold:
                $ custom2 = " Still, she’s a good companion, eager to kill boredom with an idle chat. One evening, after she had had one mug of cider too many, she admitted her grudge, mentioning the “debt” you placed upon her. Since then, the mood has gotten a bit lighter."
            elif tulia_friendship >= 6:
                $ custom2 = " She’s a good companion, a bit quiet, but resourceful. One evening, after she had had one mug of cider too many, she admitted her grudge, mentioning the “debt” you placed upon her. Since then, the mood has gotten a bit lighter."
            elif tulia_friendship >= 2:
                $ custom2 = " She’s a good companion, though you discuss only the most crucial events. One evening, after she had had one mug of cider too many, she admitted her grudge, mentioning the “debt” you placed upon her. Since then, the mood has gotten even heavier."
            else:
                $ custom2 = " Most of the time she keeps to herself, but at least she’s resourceful. One evening, after she had had one mug of cider too many, she admitted her grudge, mentioning the “debt” you placed upon her. Since then, the mood has gotten even heavier."
        else:
            if tulia_friendship >= tulia_about_highisland_recruited_threshold:
                $ custom2 = " Still, she’s a good companion, eager to kill boredom with an idle chat."
            elif tulia_friendship >= 6:
                $ custom2 = " She’s a good companion, a bit quiet, but resourceful."
            elif tulia_friendship >= 2:
                $ custom2 = " She’s a good companion, though you discuss only the most crucial events."
            elif tulia_friendship >= 0:
                $ custom2 = " Most of the time she keeps to herself, but at least she’s resourceful."
            else:
                $ custom2 = " Most of the time she keeps to herself, and one time she outright refuses to take the riskier route, forcing you to waste a few more tiresome hours."
        menu:
            'The owners recognize you in the {color=#f6d6bd}Bless The Empress{/color} inn. [custom1]
            \n\nThe days fade away slowly. With {color=#f6d6bd}Tulia{/color} by your side, you can’t simply outrun the autumn predators, and a few times your journey gets violent.[custom2]
            '
            'With all the coins I’ve been carrying, I could live in an inn for a year.' if coins >= 100:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With all the coins I’ve been carrying, I could live in an inn for a year.')
                jump hovlavan_road03
            'Coins aren’t as important as the equipment I now have.' if coins < 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Coins aren’t as important as the equipment I now have.')
                jump hovlavan_road03
            'After all the fighting I did in the North, the road isn’t too rough.' if (pc_battlecounter >= 9 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 29 and item_sharpeningpotion_used == day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After all the fighting I did in the North, the road isn’t too rough.')
                jump hovlavan_road03
            'It’s good to have an experienced fighter with me.' if (pc_battlecounter < 9 and item_sharpeningpotion_used != day) or (pc_battlecounter < 29 and item_sharpeningpotion_used == day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s good to have an experienced fighter with me.')
                jump hovlavan_road03
            'I wonder if it will be the last time I stay at roadside inns.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if it will be the last time I stay at roadside inns.')
                jump hovlavan_road03

    label hovlavan_road03:
        if pc_goal == "iwanttohelp" and pc_goal_iwanttohelppoints >= 15 and quest_pc_goal == 1:
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            menu:
                'You think of the people you’ve encountered, of what you’ve done for them. You picture the rough roads and their monsters, the claws hidden in all the places where you can’t be at once. Humans torn limb by limb, burnt villages, poisoned wells, cut throats...
                \n\nYou keep waking up, not sure if these thoughts are a dream, a memory, or a vision. You stand up, walk around, and breathe, slowly, deeply, your stomach rising and falling.
                '
                'I focus on its movements.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on its movements.')
                    menu:
                        'You came North to help people, change their lives for the better, to heal the land. But after many struggles and sacrifices, the North is almost the same. You think of the past days, and find both the light of your deeds and the gloom of the things that are out of your reach. You can save some people, but not the entire realm.
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
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04
                        'I may not be all-powerful, but I do as much as I can. I need to accept my limitations.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may not be all-powerful, but I do as much as I can. I need to accept my limitations.')
                            $ quest_pc_goal_description_completed_iwanttohelp = "I helped many people and changed things in the North for the better. My duty has been fulfilled."
                            $ achievement_pc_goal_description = "I helped many people and changed things in the North for the better."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You can give yourself a break,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
        if pc_goal == "iwantstatus" and pc_goal_iwantstatuspoints >= 4 and quest_pc_goal == 1:
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            if pc_lies >= 10 or (thais_about_magicfruit_received and not thais_about_magicfruit_barter) or (quest_glauciasupport == 2 and not glaucia_about_galerocksdecision_liedto):
                menu:
                    'You think of the leaders you’ve encountered, the work you’ve done for them, and the sacrifices you had to make to get on their good side. You’ve spun the first threads of your web of connections. Yet something distorts your new beginning, a shadow that grows greater with every heartbeat.
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
                            $ custom3 = "Who can tell what sort of havoc {color=#f6d6bd}Glaucia’s{/color} anger will bring to this place in the years to come. "
                        else:
                            $ custom3 = ""
                        menu:
                            'The gloom comes straight from the soul of a very different being than the one who came to this peninsula. Is the [pcname] you knew gone? Is this new creature the {i}real{/i} you?
                            \n\nIf it is {i}just{/i} a mask after all, you still don’t know how to handle it. [custom1][custom2][custom3]You’ve reached for power and control, but something about all this is now chasing after you, plaguing your thoughts like a spirit of judgment.
                            '
                            'I reject this thought. I {i}had to{/i} be ruthless. I’ve made sacrifices, but they will be the beginning of something great.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reject this thought. I {i}had to{/i} be ruthless. I’ve made sacrifices, but they will be the beginning of something great.')
                                $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and will have a great advantage when talking to the members of the guild. It took a heavy price, but what matters is that {i}I{/i} will be fine."
                                $ endgame_epilogue_evil = 2
                                $ achievement_pc_goal_description = "I’ve paid a high price for making some powerful connections in the North, but it was all worth it."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                menu:
                                    'Your heart is filled with both determination and cruel satisfaction. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. After all, keeping people dancing to your tune requires a strong soul, and you’ll need your wits to keep making the {i}right{/i} choices.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        jump hovlavan_road04
                            'I wish I could move back in time, fix all of this. But all I can do is try to be better from now on.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish I could move back in time, fix all of this. But all I can do is try to be better from now on.')
                                $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and will have a great advantage when talking to the members of the guild, but I feel like something about me is changing. I regret the things I’ve done."
                                $ endgame_epilogue_evil = 1
                                $ achievement_pc_goal_description = "I’ve paid a high price for making some powerful connections in the North. Maybe even too high."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                menu:
                                    'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “Turn back, while you still can,” you hear, or maybe say.
                                    '
                                    'I lie down and return to sleep.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to sleep.')
                                        jump hovlavan_road04
            else:
                if pc_lies:
                    $ custom1 = "You sometimes lied, but not overly much"
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
                        $ pc_hp_can5 = 1
                        menu:
                            'As you look around, thinking of your journey, you feel relaxed and complete. You smile, thinking of the things you’ve accomplished, and of what still awaits you.
                            '
                            'The next chapter of my life.' if pc_class == "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next chapter of my life.')
                                jump hovlavan_road04
                            'The next stage of my life.' if pc_class != "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next stage of my life.')
                                jump hovlavan_road04
                    'I don’t really care about any of that. I just did what I thought was more beneficial for me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t really care about any of that. I just did what I thought was more beneficial for me.')
                        $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and didn’t hurt too many people in the process. I’ll have a great advantage when talking to the members of the guild."
                        $ endgame_epilogue_evil = 2
                        $ achievement_pc_goal_description = "I’ve made some powerful connections and didn’t hurt too many people in the process."
                        $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                        $ quest_pc_goal = 2
                        $ pc_hp_can5 = 1
                        menu:
                            'As you look around, thinking of your journey, you feel relaxed and ready. You smile, thinking of the new possibilities you’ve unlocked, and of what still awaits you.
                            '
                            'I lie down.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                jump hovlavan_road04
        if pc_goal == "iwanttoberemembered" and pc_goal_iwanttoberememberedpoints >= 6 and quest_pc_goal == 1:
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
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
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You are a hero, after all. You need to look the part.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04
                        'I’ve done so much, yet this place is still similar to what it had been like before my arrival. I must admit that I’m yet another roadwarden who arrived at the peninsula, nothing more.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve done so much, yet this place is still similar to what it had been like before my arrival. I must admit that I’m yet another roadwarden who arrived at the peninsula, nothing more.')
                            $ quest_pc_goal_description_completed_iwanttoberemembered = "I’ve done as much as I could, but who knows if it was enough to make me a hero. Time will tell."
                            $ achievement_pc_goal_description = "I’ve done as much as I could, and I can’t know if it was enough to make me a hero."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You can give yourself a break,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to sleep.')
                                    jump hovlavan_road04
        if pc_goal == "ineedmoney":
            if coins >= 100 and quest_pc_goal == 1:
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of the soul you care for the most. You came North to find the coins they need, and your journey was so long... You wonder how far away you are from reaching your goal.
                    '
                    'I get to my bags and start to count the dragon bones I own.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get to my bags and start to count the dragon bones I own.')
                        menu:
                            'You unpack your pouch, or rather your heavy {i}sack{/i}. Counting its contents is satisfying, both because of how many of them there are, and the stories the coins carry with them. Some of them you remember from the specific transactions you made, or the places where you found them. Others make you think of the dozens of years that they have behind them. They’re in different shapes and colors. Who knows where some of them have been?
                            \n\nA hundred dragon bones.
                            \n\nThis is all you need. You take a deep breath. You’ve done it.
                            '
                            'I take a wooden box and fill it with rags and coins.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags and coins.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
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
                                        jump hovlavan_road04
            elif quest_pc_goal_description_completed_ineedmoney and quest_pc_goal == 1 and item_asterionwine and item_asterionwine_pcknows_2:
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of the soul you care for the most. You came here to find the coins they need, and your journey was so long... But now it seems like you’ve finally reached the goal of your journey.
                    '
                    'I go to my bags and grab the bottle of Night’s Bane.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get to my bags and grab the bottle of Night’s Bane.')
                        menu:
                            'You unpack the wine, remembering the way you earned it. You sniff the expensive contents, even though to you it smells like any other drink based on fermented fruits. It’s strange to realize that this very bottle may be your saviour.
                            \n\nYour soul is filled with visions of opulence, but you push them away. You know what you need to do with it. You take a deep breath. You’ve done it. This is it.
                            '
                            'I take a wooden box and fill it with rags to secure the bottle.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags to secure the bottle.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
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
                                        jump hovlavan_road04
            else:
                pass
        if pc_goal == "iwantmoney":
            if coins >= 100 and quest_pc_goal == 1:
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of all the plans you have for your future life in {color=#f6d6bd}Hovlavan{/color}. You came North to find the coins you need, and your journey was so long... You wonder how far away you are from reaching your goal.
                    '
                    'I go to my bags and start to count the dragon bones I own.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and start to count the dragon bones I own.')
                        menu:
                            'You unpack your pouch, or rather your heavy {i}sack{/i}. Counting its contents is satisfying, both because of how many of them there are, and the stories the coins carry with them. Some of them you remember from the specific transactions you made, or the places where you found them. Others make you think of the dozens of years that they have behind them. They’re in different shapes and colors. Who knows where some of them have been?
                            \n\nA hundred dragon bones.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nThis is all you need. You take a deep breath. You’ve done it.
                            '
                            'I take a wooden box and fill it with rags and coins.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags and coins.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
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
                                        jump hovlavan_road04
            elif quest_pc_goal_description_completed_iwantmoney and quest_pc_goal == 1 and item_asterionwine and item_asterionwine_pcknows_2:
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You struggle to sleep, thinking of all the plans you have for your future life in {color=#f6d6bd}Hovlavan{/color}. You came North to find the coins you need, and your journey was so long... But now it seems like you’ve finally reached your goal.
                    '
                    'I go to my bags and grab the bottle of Night’s Bane.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and grab the bottle of Night’s Bane.')
                        menu:
                            'You unpack the wine, remembering the way you earned it. You sniff the expensive contents, even though to you it smells like any other drink based on fermented fruits. It’s strange to realize that this very bottle may lay the path to your future.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nYou take a deep breath. You’ve done it. This is it.
                            '
                            'I take a wooden box and fill it with rags to secure the bottle.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a wooden box and fill it with rags to secure the bottle.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
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
                                        jump hovlavan_road04
            else:
                pass
        if (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_howlersdell and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_creeks and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_monastery and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_bandits and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_galerocks and quest_pc_goal == 1):
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
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
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I keep my eyes shut for as long as it takes.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep my eyes shut for as long as it takes.')
                                    jump hovlavan_road04
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
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04
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
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04
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
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04
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
                            $ pc_hp_can5 = 1
                            menu:
                                'This thought is not easy for you, but once you fully shape it into words, a sudden wave of tiredness hits your shell. Some sort of tension has left your soul. “You don’t have to stay on your path,” you hear, or maybe say.
                                '
                                'I lie down and return to sleep.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down and return to my sleep.')
                                    jump hovlavan_road04
                        'I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knew I was going to risk it all. I faced beasts and scoundrels, and I won’t let some merchants take away what I have left.')
                            $ quest_pc_goal_description_completed_iwanttostartanewlife = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ achievement_pc_goal_description = "I was planning to build a new life for myself, and I will stay on course, no matter what."
                            $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ quest_pc_goal = 2
                            $ pc_hp_can5 = 1
                            menu:
                                'Your heart is filled with both anger and determination. It keeps you awake for another half an hour, but you finally force yourself to return to sleep. You need strength for the rest of the journey, after all.
                                '
                                'I lie down.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                    jump hovlavan_road04

    label hovlavan_road04:
        show areapicture ep_02 at basicfade
        nvl clear
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
        if description_hovlavan04 == "nooldstatues":
            $ custom1 = "After two days you join forces with an encountered caravan. The roads get wider and harder, and you meet the first patrol of soldiers."
        elif description_hovlavan04 == "oldstatuesnoattention":
            $ custom1 = "After two days, the roads get wider and harder, and you meet the first patrol of soldiers, as well as spot the familiar stone statues."
        elif description_hovlavan04 == "oldstatuesofheroes":
            $ custom1 = "After two days, the roads get wider and harder, and you meet the first patrol of soldiers, as well as spot the familiar stone statues of local heroes."
        elif description_hovlavan04 == "oldstatuesofthemselves":
            $ custom1 = "After two days, the roads get wider and harder. You join forces with an encountered caravan, and their leader, a wealthy merchant, mentions that one of the statues you ride by portrays her mother."
        elif description_hovlavan04 == "oldstatuesofimportantplaces":
            $ custom1 = "After two days, the roads get wider and harder, and you meet the first patrol of soldiers, as well as spot the familiar stone statues honoring the old, now destroyed villages and almost-forgotten tragedies."
        else:
            $ custom1 = "After two days you join forces with an encountered caravan. The roads get wider and harder, and you meet the first patrol of soldiers."
        if asterion_lie:
            if asterion_lie == "monsters" or asterion_lie == "bandits":
                $ custom2 = "After exchanging a few words with them, {color=#f6d6bd}Tulia{/color} gestures toward you. “The roadwarden is who should be thanked for finding him.”\n\nThe strangers keenly listen to your tale, then, with smiles clouded by grief, thank you for your bravery. After a silent, yet delicious meal, you resume your journey."
            elif asterion_lie == "solitude":
                $ custom2 = "After exchanging a few words with them, {color=#f6d6bd}Tulia{/color} gestures toward you. “The roadwarden is who should be thanked for finding him.”\n\nThe strangers keenly listen to your tale, then, with looks clouded by grief and anger, and keep pushing for answers. After a few tense minutes, you resume your journey."
        elif quest_asterion == 2 or tulia_highisland_joined:
            if asterion_found_burnt:
                $ endgame_asterion_invitation = 1
                $ custom2 = "After exchanging a few words with them, {color=#f6d6bd}Tulia{/color} gestures toward you. “The roadwarden is who should be thanked for finding him.”\n\nThe strangers keenly listen to your tale, then, with smiles clouded by grief, thank you for your bravery. A man who looks younger than the rest can’t stop his tears once he hears his “pa” has been spared the “cursed fate” and found his end in the flames.\n\nAfter a silent, yet delicious meal, you resume your journey, carrying with you their names and invitation."
            elif asterion_found:
                $ custom2 = "After exchanging a few words with them, {color=#f6d6bd}Tulia{/color} gestures toward you. “The roadwarden is who should be thanked for finding him.”\n\nThe strangers keenly listen to your tale, then, with smiles clouded by grief, thank you for your bravery. After a silent, yet delicious meal, you resume your journey."
        else:
            $ custom2 = "After exchanging a few words with them, she heads toward your palfrey and starts to unpack {color=#f6d6bd}Asterion’s{/color} possessions. The strangers spare you only a glance, and while their eyes remain troubled, they politely accept their inheritance."
            $ quest_asterion_description00badresult = "I wasn’t able to find {color=#f6d6bd}Asterion{/color} on time."
            $ quest_asterion = 3
        menu:
            '[custom1]
            \n\n“We’re here,” says {color=#f6d6bd}the lieutenant{/color} in the last village you visit before reaching the city walls. Without explaining, she approaches a few red-haired farmers that are observing you curiously from the bench in front of their pit-house. [custom2]
            '
            'It’s weird how many questions they had about the place where I “found” him. And about the wolves.' if asterion_lie == "monsters":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s weird how many questions they had about the place where I “found” him. And about the wolves.')
                jump hovlavan_arrival01
            'It’s weird how many questions they had about these “bandits”. And about the peninsula in general.' if asterion_lie == "bandits":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s weird how many questions they had about these “bandits”. And about the peninsula in general.')
                jump hovlavan_arrival01
            'I don’t think they’re going to let go of their father so easily.' if asterion_lie == "solitude":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t think they’re going to let go of their father so easily.')
                jump hovlavan_arrival01
            'I guess I’ll take the truth straight to the council.' if (quest_asterion == 1 and asterion_found) or (asterion_lie and asterion_found):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess I’ll take the truth straight to the council.')
                jump hovlavan_arrival01
            'Maybe I’ll meet with them in spring.' if endgame_asterion_invitation:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I’ll meet with them in spring.')
                jump hovlavan_arrival01
            'I wonder what really happened to him.' if not asterion_found and asterion_lie:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder what really happened to him.')
                jump hovlavan_arrival01
            'I wonder what happened to him.' if not asterion_found and not asterion_lie:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder what happened to him.')
                jump hovlavan_arrival01
            'Their father pushed his limits. I’m glad his family knows this.' if asterion_found_pcthought == "readyforanadventure":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Their father pushed his limits. I’m glad his family knows this.')
                jump hovlavan_arrival01
            'I don’t wish any family to go through this.' if asterion_found_pcthought == "readytoplayitsafe":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t wish any family to go through this.')
                jump hovlavan_arrival01
            'I wish I knew what really pushed their father to do all this.' if asterion_found_pcthought == "annoyedwithunsolvedmystery":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish I knew what really pushed their father to do all this.')
                jump hovlavan_arrival01
            'This is the end of their father’s tale.' if asterion_found_pcthought == "readytoletthemysterygo":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is the end of their father’s tale.')
                jump hovlavan_arrival01
            'Their father tried his best.' if asterion_found_pcthought == "believeshewasrational":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Their father tried his best.')
                jump hovlavan_arrival01
            'It’s over, finally.' if asterion_found_pcthought == "doesntcareatall":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s over, finally.')
                jump hovlavan_arrival01
            'I don’t think I can be a warden any longer.' if asterion_found_pcthought == "pchasseriousdoubts":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t think I can be a warden any longer.')
                $ asterion_found_pcthought = "pchasseriousdoubts2"
                jump hovlavan_arrival01
            'Before we leave, I grab myself a juicy pear.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before we leave, I grab myself a juicy pear.')
                jump hovlavan_arrival01
            'Before we leave, I ask for some hay for {color=#f6d6bd}[horsename]{/color}.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before we leave, I ask for some hay for {color=#f6d6bd}%s{/color}.' %horsename)
                jump hovlavan_arrival01

label hovlavan_arrivalALL:
    label hovlavan_arrival01:
        if thais_hovlavan02 == 1:
            $ custom6 = "You consider taking your equipment to {color=#f6d6bd}The Backwood Corner{/color}, but a kind merchant is quick to mention the recent wave of break-ins. You take your chance at the nearby ale house, and borrow an extra padlock from a friend."
        elif thais_hovlavan02 == 2:
            $ custom6 = "You take your equipment to {color=#f6d6bd}The Backwood Corner{/color}. It’s a bit pricey, but your friends at {color=#f6d6bd}The Apple And The Boar{/color} will be happy to offer you a short stay."
        elif thais_hovlavan02 == 3:
            $ custom6 = "You take your equipment to {color=#f6d6bd}The Backwood Corner{/color}. It’s a dangerous alley, but you know a place where a coin will keep your bundles untouched - {color=#f6d6bd}The Boarhead Inn{/color}."
        elif thais_hovlavan02 == 4:
            $ custom6 = "Having no close friends working in the alehouses and inns, you take your belongings to the guild’s public warehouse. It’s a costly service, but sure to save your “treasures”. You then stay at a cheap tavern in the harbor."
        else:
            $ custom6 = "Having no close friends working in the alehouses and inns, you take your belongings to the guild’s public warehouse. It’s a costly service, but sure to save your “treasures”. You then stay at a cheap tavern in the harbor."
        if thais_hovlavan02 == 1:
            show areapicture ep_03a at basicfade
        elif thais_hovlavan02 == 2:
            show areapicture ep_03b at basicfade
        elif thais_hovlavan02 == 3:
            show areapicture ep_03c at basicfade
        elif thais_hovlavan02 == 4:
            show areapicture ep_03d at basicfade
        else:
            show areapicture ep_03d at basicfade
        nvl clear
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
        if pc_hasfamily:
            $ custom2 = "Before you spend a few hours with your relatives, you leave your mount in the stables, which, as it often happens, are almost empty. "
        elif pc_home_druid == "notfromthecity":
            $ custom2 = "After taking care of a few chores, you leave your mount in the stables, which, as it often happens, are almost empty. "
        else:
            $ custom2 = "After taking care of some chores and meeting a few friendly faces, you leave your mount in the stables, which, as it often happens, are almost empty. "
        if thais_hovlavan01 == 1:
            $ custom1 = "In {color=#f6d6bd}Hovlavan{/color}, every street seems to be more crowded than an entire Northern village, and you frown the moment you hear the busy marketplace. You may be back home, but you’ll need a few days to get used to the local scents, noise, and the overall lack of green."
        elif thais_hovlavan01 == 2:
            $ custom1 = "Your eyes are used to the usual conglomerate of ruins; the makeshift huts and sheds; the restored, whitewashed houses; and the few well-kept residences that managed to outlast The Invasion. The streets are busy, with plenty of children and their young, working parents. {color=#f6d6bd}Hovlavan{/color} may have been sick in the past, but it’s been healing patiently."
        elif thais_hovlavan01 == 3:
            $ custom1 = "Your eyes are used to the usual conglomerate of ruins; the makeshift huts and sheds; the restored, whitewashed houses; and the few well-kept residences that managed to outlast the invasion. You nod toward a few passersby, but aside from the marketplace, {color=#f6d6bd}Hovlavan{/color} is quiet."
        else:
            $ custom1 = renpy.random.choice(['In {color=#f6d6bd}Hovlavan{/color}, every street seems to be more crowded than an entire Northern village, and you frown the moment you hear the busy marketplace. You may be back home, but you’ll need a few days to get used to the local scents, noise, and the overall lack of green.', 'Your eyes are used to the usual conglomerate of ruins; the makeshift huts and sheds; the restored, whitewashed houses; and the few well-kept residences that managed to outlast The Invasion. The streets are busy, with plenty of children and their young, working parents. {color=#f6d6bd}Hovlavan{/color} may have been sick in the past, but it’s been healing patiently.', 'Your eyes are used to the usual conglomerate of ruins; the makeshift huts and sheds; the restored, whitewashed houses; and the few well-kept residences that managed to outlast the invasion. You nod toward a few passersby, but aside from the marketplace, {color=#f6d6bd}Hovlavan{/color} is quiet.'])
        if bestiary_seamonsters_city == "creaturesstayaway":
            $ custom5 = "The “band of undead” on the road has been taken care of."
        elif bestiary_seamonsters_city == "creaturesattackdrunkards":
            $ custom5 = "The beasts of the harbor keep bothering workers, but there have been no deaths recently."
        elif bestiary_seamonsters_city == "creaturesgetontheland":
            $ custom5 = "The corpse of the tentacled monster that recently entered the streets has been claimed by a vendor, and they’re selling it skewered."
        elif bestiary_seamonsters_city == "flyingmonsters":
            $ custom5 = "The harpies have taken a few lambs from a traveling merchant, but at least the kids are safe."
        else:
            $ custom5 = renpy.random.choice(['The “band of undead” on the road has been taken care of.', 'The beasts of the harbor keep bothering workers, but there have been no deaths recently.', 'The corpse of the tentacled monster that recently entered the streets has been claimed by a vendor, and they’re selling it skewered.', 'The harpies have taken a few lambs from a traveling merchant, but at least the kids are safe.'])
        menu:
            '[custom2][custom1]
            \n\n[custom6]
            \n\nYou listen to the rumors, but as the minutes go by, no one approaches you, or asks you for help. The trade goes fine, you hear. The city chief has a daughter now. The new ship is ready to sail. The taxes are coming. [custom5]
            '
            'I listen carefully. Maybe someone will have a job for me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I listen carefully. Maybe someone will have a job for me.')
                jump hovlavan_arrival02
            'I remain watchful. Things are not as quiet as they seem.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remain watchful. Things are not as quiet as they seem.')
                jump hovlavan_arrival02
            'I keep to myself, enjoying the calm before the storm.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep to myself, enjoying the calm before the storm.')
                jump hovlavan_arrival02
            'I join a group of patrons. “Let’s have a drink!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I join a group of patrons. “Let’s have a drink!”')
                jump hovlavan_arrival02

    label hovlavan_arrival02:
        show areapicture ep_04 at basicfade
        nvl clear
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
        if description_hovlavan19:
            $ custom3 = "You ignore the growing, drunken crowd, so familiar to you, and get a good sleep. You head downstairs and ask for the remains of the last-day supper -"
        else:
            $ custom3 = "The noises of the drunken crowd hinder your sleep. You head downstairs and fully wake up only after you get served the remains of the last-day supper -"
        if thais_hovlavan05 == 1:
            $ custom7 = "ibex stew, a piece of rat pie, and a mug of kefir."
        elif thais_hovlavan05 == 2:
            $ custom7 = "mutton stew, a piece of rat pie, and a mug of kefir."
        elif thais_hovlavan05 == 3:
            $ custom7 = "fish pie with a few slices of boar ham and a mug of weak beer."
        elif thais_hovlavan05 == 4:
            $ custom7 = "a bowl of now-mixed fried crickets in various spices, as well as a mug of hemp tisane."
        else:
            $ custom7 = renpy.random.choice(['ibex stew, a piece of rat pie, and a mug of kefir.', 'mutton stew, a piece of rat pie, and a mug of kefir.', 'fish pie with a few slices of boar ham and a mug of weak beer.', 'a bowl of now-mixed fried crickets in various spices, as well as a mug of hemp tisane.'])
        if hovlavan_music == "chanties":
            $ custom8 = "You listen to the sea shanties coming from the window - {color=#f6d6bd}Hovlavan{/color} is returning to work."
        elif hovlavan_music == "oldtunes":
            $ custom8 = "You listen to The Emperor’s Mask, the hymn from the old times, coming from the window - {color=#f6d6bd}Hovlavan{/color} is returning to work."
        elif hovlavan_music == "tame":
            $ custom8 = "Judging by the arguments of the laborers and the raised voice of a priest’s sermon, {color=#f6d6bd}Hovlavan{/color} is returning to work."
        elif hovlavan_music == "no":
            $ custom8 = "Judging by the arguments of the laborers, {color=#f6d6bd}Hovlavan{/color} is returning to work."
        else:
            $ custom8 = renpy.random.choice(['You listen to the sea shanties coming from the window - {color=#f6d6bd}Hovlavan{/color} is returning to work.', 'You listen to The Emperor’s Mask, the hymn from the old times, coming from the window - {color=#f6d6bd}Hovlavan{/color} is returning to work.', 'Judging by the arguments of the laborers and the raised voice of a priest’s sermon, {color=#f6d6bd}Hovlavan{/color} is returning to work.', 'Judging by the arguments of the laborers, {color=#f6d6bd}Hovlavan{/color} is returning to work.'])
        if hovlavan_nakedness == "prudeness":
            $ custom9 = "You pay for some time in a small bathhouse and prepare"
        elif hovlavan_nakedness == "justbaths":
            $ custom9 = "You spend some time at a public bathhouse and prepare"
        elif hovlavan_nakedness == "ribald":
            $ custom9 = "You spend some time at a public bathhouse, chatting with your tales-hungry, naked neighbors, then prepare"
        elif hovlavan_nakedness == "status":
            $ custom9 = "You spend some time at a small, public bathhouse - you wouldn’t be allowed in the one for the rich folk - and prepare"
        else:
            $ custom9 = renpy.random.choice(['You pay for some time in a small bathhouse and prepare', 'You spend some time at a public bathhouse and prepare', 'You spend some time at a public bathhouse, chatting with your tales-hungry, naked neighbors, then prepare', 'You spend some time at a small, public bathhouse - you wouldn’t be allowed in the one for the rich folk - and prepare'])
        if item_fancyclothes:
            $ custom1 = "the outfit you bought at {color=#f6d6bd}Howler’s{/color}. It will let you blend in with the “elite” crowd."
        else:
            $ custom1 = "your somewhat clean outfit. In the streets, you blend in with the working folk."
        if hovlavan_humaninteraction == "trueloneliness" or hovlavan_humaninteraction == "okloneliness":
            $ custom4 = "On your way, the familiar faces spare you a few nods, but, as always, the cityfolk are too busy trying to make ends meet."
        elif hovlavan_humaninteraction == "onlyfamilies":
            $ custom4 = "On your way, the familiar faces spare you a few nods, but, as always, the cityfolk stick to their own kin."
        elif hovlavan_humaninteraction == "closefriendships":
            $ custom4 = "A friend meets you by the bathhouse and walks you to the guild’s gate."
        elif hovlavan_humaninteraction == "thinfriendships":
            $ custom4 = "Your group of friends meet you by the bathhouse, and walk you to the guild’s gate."
        elif hovlavan_humaninteraction == "okdistrust" or hovlavan_humaninteraction == "truedistrust":
            $ custom4 = "On your way, the familiar faces spare you a few nods, but, as always, the cityfolk are too busy trying to outcompete one another, seeking dignity in the realm that belongs to the rich and the priests."
        else:
            $ custom4 = "On your way, the familiar faces spare you a few nods, but, as always, the cityfolk are too busy trying to make ends meet."
        menu:
            '[custom3] [custom7] [custom8]
            \n\nWhen the messenger shows up, you let out a sigh. The merchants want to see you in an hour. [custom9] [custom1]
            \n\n[custom4]
            '
            'I will miss the long conversations I had with the tribes.' if hovlavan_humaninteraction == "trueloneliness" or not hovlavan_humaninteraction:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I will miss the long conversations I had with the tribes.')
                jump hovlavan_council01
            'At least no one’s wasting my time.' if hovlavan_humaninteraction == "okloneliness" or not hovlavan_humaninteraction:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least no one’s wasting my time.')
                jump hovlavan_council01
            'Only my family was aware of my absence.' if hovlavan_humaninteraction == "onlyfamilies" and pc_hasfamily:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Only my family was aware of my absence.')
                jump hovlavan_council01
            'They didn’t even notice my absence.' if hovlavan_humaninteraction == "onlyfamilies" and not pc_hasfamily:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They didn’t even notice my absence.')
                jump hovlavan_council01
            'We catch up, as much as we can.' if hovlavan_humaninteraction == "closefriendships":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We catch up, as much as we can.')
                jump hovlavan_council01
            'I don’t even know where to start.' if hovlavan_humaninteraction == "closefriendships":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even know where to start.')
                jump hovlavan_council01
            'We talk about this and that.' if hovlavan_humaninteraction == "thinfriendships":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We talk about this and that.')
                jump hovlavan_council01
            'They ask me mostly about the beasts I faced.' if hovlavan_humaninteraction == "thinfriendships":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They ask me mostly about the beasts I faced.')
                jump hovlavan_council01
            'Yet it’s {i}me{/i} who’s going to win a better life here.' if hovlavan_humaninteraction == "okdistrust":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yet it’s {i}me{/i} who’s going to win a better life here.')
                jump hovlavan_council01
            'There’s no better life to find in these walls.' if hovlavan_humaninteraction == "truedistrust":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no better life to find in these walls.')
                jump hovlavan_council01
            'I’ll buy {color=#f6d6bd}[horsename]{/color} a few apples on my way back.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy {color=#f6d6bd}%s{/color} a few apples on my way back.' %horsename)
                jump hovlavan_council01
            'To gather my thoughts, I spend some time wandering in the marketplace.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- To gather my thoughts, I spend some time wandering in the marketplace.')
                jump hovlavan_council01
            'I head to the guild quickly. I want to be done with this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the guild quickly. I want to be done with this.')
                jump hovlavan_council01

label hovlavan_councilALL:
    label hovlavan_council01:
        show areapicture ep_05 at basicfade
        nvl clear
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
        if thais_hovlavan03 == 1 or thais_hovlavan03 == 4:
            $ custom1 = "Their jewelry and colorful fabrics could provide for many Northern families, maybe even pay for a new stronghold."
        elif thais_hovlavan03 == 2:
            $ custom1 = "Their jewelry and rare furs could provide for many Northern families, maybe even pay for a new stronghold."
        elif thais_hovlavan03 == 3:
            $ custom1 = "Their fancy hats and colorful fabrics could provide for many Northern families, maybe even pay for a new stronghold."
        else:
            $ custom1 = renpy.random.choice(['Their jewelry and colorful fabrics could provide for many Northern families, maybe even pay for a new stronghold.', 'Their jewelry and rare furs could provide for many Northern families, maybe even pay for a new stronghold.', 'Their fancy hats and colorful fabrics could provide for many Northern families, maybe even pay for a new stronghold.'])
        if thais_hovlavan06 == 1 or thais_hovlavan06 == 2:
            $ custom2 = "You wouldn’t recognize the priests of The United Church if it wasn’t for their familiar faces."
        elif thais_hovlavan06 == 3:
            $ custom2 = "The priests of The United Church look like peacocks next to the humble cowls of the monks."
        elif thais_hovlavan06 == 4:
            $ custom2 = "The few veterans sitting by the table wear gambesons so decorative you doubt anyone would use them in combat."
        elif thais_hovlavan06 == 5:
            $ custom2 = "Aside from the chief and his most-trusted advisors, the room is filled with members of the guild - though some of the more {i}significant{/i} individuals did not deign to show up."
        else:
            $ thais_hovlavan06 = 2
            $ custom2 = "You wouldn’t recognize the priests of The United Church, if it wasn’t for their familiar faces."
        if asterion_found:
            $ quest_explorepeninsula_points += 2
            $ custom3 = "“At least you had more luck than that poor wretch,” mentions one of the traders. No one here remembers {color=#f6d6bd}Asterion’s{/color} name. “The news you brought from the island is of {i}great{/i} value.”"
        elif asterion_highisland_knowsabout:
            $ quest_explorepeninsula_points += 1
            $ custom3 = "“At least you had more luck than that poor wretch,” mentions one of the traders. No one here remembers {color=#f6d6bd}Asterion’s{/color} name. “Too bad we won’t learn more about the island anytime soon.”"
        else:
            $ custom3 = "“Too bad you haven’t found that poor wretch,” mentions one of the traders. No one here remembers {color=#f6d6bd}Asterion’s{/color} name. “Let’s just assume he’s not coming back. Objections?” There are none."
        if world_known_areas >= 40:
            $ quest_explorepeninsula_points += 3
            $ custom4 = "Your detailed description of the peninsula made quite an impression, and you may be asked to speak with a cartographer later"
        elif world_known_areas >= 30:
            $ quest_explorepeninsula_points += 2
            $ custom4 = "Your detailed description of the peninsula was welcomed with approval"
        elif world_known_areas >= 20:
            $ quest_explorepeninsula_points += 1
            $ custom4 = "Your general description of the peninsula was met with many more questions"
        elif world_known_areas >= 10:
            $ custom4 = "Your vague description of the peninsula was met with reservation"
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom4 = "Your vague description of the peninsula was met with angry questions"
        if world_known_npcs >= 40:
            $ quest_explorepeninsula_points += 3
            $ custom5 = ", and you could talk about your connections in the North for the rest of the day."
        elif world_known_npcs >= 30:
            $ quest_explorepeninsula_points += 2
            $ custom5 = ", and getting in touch with so many Northerners helped you describe the complex web of connections."
        elif world_known_npcs >= 22:
            $ quest_explorepeninsula_points += 1
            $ custom5 = ", and it’s clear you’re familiar with quite a few Northerners."
        elif world_known_npcs >= 13:
            $ custom5 = ". While you’re familiar with a few Northerners, you don’t have much to say about them."
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom5 = ". Having hardly anything to say about the locals, you’re met with annoyed looks."
        if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls:
            $ custom9 = ", your familiarity with the heart of the woods"
            $ quest_explorepeninsula_points += 2
        elif shortcut_traveled >= 4 or (shortcut_traveled and quest_explorepeninsula_description04):
            $ custom9 = ", the few times you crossed the heart of the woods"
            $ quest_explorepeninsula_points += 1
        elif not shortcut_traveled:
            $ custom9 = ", the dangers of the heart of the woods"
            $ quest_explorepeninsula_points -= 1
        else:
            $ custom9 = ", the dangers of the heart of the woods"
        if quest_explorepeninsula_description15c:
            $ quest_explorepeninsula_points -= 1
            $ custom6 = ", {color=#f6d6bd}Eudocia’s{/color} stubbornness"
        elif item_golemglove:
            $ quest_explorepeninsula_points += 2
            $ custom6 = ", {color=#f6d6bd}Eudocia’s{/color} golem glove"
        elif not quest_explorepeninsula_description15b:
            $ quest_explorepeninsula_points += 1
            $ custom6 = ", the partnership with {color=#f6d6bd}Eudocia{/color}"
        elif quest_explorepeninsula_description15:
            $ custom6 = ", {color=#f6d6bd}Eudocia’s{/color} golems"
        elif not quest_explorepeninsula_description15:
            $ quest_explorepeninsula_points -= 1
            $ custom6 = ""
        if quest_explorepeninsula_description03:
            $ quest_explorepeninsula_points += 1
            $ custom7 = ", the rumored access from the coast"
        elif asterion_found:
            $ custom7 = ", the way you reached {color=#f6d6bd}High Island{/color}"
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom7 = ", the lack of access from the coast"
        if foragingground_foraging_vein and not foragingground_foraging_vein_sabotaged:
            $ quest_explorepeninsula_points += 2
            $ custom8 = ", the copper vein"
        elif foragingground_foraging_vein_sabotaged:
            $ custom8 = ", the copper vein in the hands of the locals"
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom8 = ""
        if watchtower_open == "key" and watchtower_tower_bugs_cleared:
            $ quest_explorepeninsula_points += 2
            $ custom10 = ", the decent state of the old watchtower"
        elif watchtower_open == "key" or watchtower_tower_bugs_cleared:
            $ quest_explorepeninsula_points += 1
            $ custom10 = ", the state of the old watchtower"
        elif watchtower_firsttime:
            $ custom10 = ", the poor state of the old watchtower"
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom10 = ", the state of some “watchtower”"
        if quest_explorepeninsula_description06:
            $ quest_explorepeninsula_points += 1
            $ custom10 = ", the shelter by the northern road"
        elif ruinedshelter_firsttime:
            $ custom10 = ", the shelter by the northern road"
        else:
            $ custom10 = ""
        if quest_explorepeninsula_description10c:
            $ quest_explorepeninsula_points += 1
            $ custom11 = ", the now-flooded mine in the south"
        else:
            $ custom11 = ", the mine in the south"
        menu:
            'After a few hours of exhausting examination, you lean against the wall, observing the arguing leaders. [custom1] [custom2]
            \n\n[custom3]
            \n\nYou ask for something to clear your throat. [custom4][custom5]
            \n\nYou fill the gaps in your report. You discuss the recent disappearance of a trading caravan[custom6][custom9][custom7][custom8][custom10][custom11]...
            \n\nStill, it’s your dealings with the tribes that will have the greatest impact on their decision.
            '
            'I recollect the blizzard of questions about the villages.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I recollect the blizzard of questions about the villages.')
                jump hovlavan_council02
            'I relax and wait for them to address me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I relax and wait for them to address me.')
                $ endgame_skip_villages = 1
                jump hovlavan_council02

    label hovlavan_council02:
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        $ custom5 = ""
        $ custom6 = ""
        $ custom7 = ""
        $ custom8 = ""
        $ custom9 = ""
        $ custom10 = ""
        $ custom11 = ""
        $ custom12 = ""
        $ custom13 = ""
        $ custom14 = ""
        $ custom15 = ""
        $ custom16 = ""
        $ custom17 = ""
        $ custom18 = ""
        $ custom19 = ""
        $ custom20 = ""
        if not howlersdell_firsttime:
            $ quest_explorepeninsula_points -= 2
            $ custom1 = "“{color=#f6d6bd}Howler’s Dell{/color} used to be one of the richest villages in the North, and placed just beyond {color=#f6d6bd}Steep House{/color}, at a convenient spot,” explained a priest, “even if led by pagans. It’s truly hard to believe you’d {i}omit{/i} them on your {i}patrols{/i},” her angry tone encouraged the suspicious looks of the others."
            $ custom2 = ""
            $ custom3 = ""
        else:
            if item_thaisletter_opened:
                $ endgame_howlersdell_leader_points += 1
                if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ endgame_howlersdell_leader_points += 1
                    $ custom1 = "While seeing the opened letter from {color=#f6d6bd}Howler’s Dell{/color} raised a few eyebrows, the promise of a future collaboration sparked great curiosity. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “and staying honest with them about the fishing hamlet will surely aid our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
                else:
                    $ custom1 = "While seeing the opened letter from {color=#f6d6bd}Howler’s Dell{/color} raised a few eyebrows, the promise of a future collaboration sparked great curiosity. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “though lying to them about the fishing hamlet will hinder our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
            elif item_thaisletter:
                $ endgame_howlersdell_leader_points += 2
                if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ endgame_howlersdell_leader_points += 1
                    $ custom1 = "Seeing the sealed letter from {color=#f6d6bd}Howler’s Dell{/color} earned you a few polite words, and the promise of a future collaboration sparked great curiosity. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “and staying honest with them about the fishing hamlet will surely aid our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
                else:
                    $ custom1 = "Seeing the sealed letter from {color=#f6d6bd}Howler’s Dell{/color} earned you a few polite words, and the promise of a future collaboration sparked great curiosity. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “though lying to them about the fishing hamlet will hinder our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
            else:
                if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ endgame_howlersdell_leader_points += 1
                    $ custom1 = "Having no letter from {color=#f6d6bd}Thais{/color}, you shared the general description of {color=#f6d6bd}Howler’s Dell{/color} and vaguely described the fishing hamlet. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “and staying honest with them about the fishing hamlet will surely aid our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
                elif quest_fisherhamlet_description09 or quest_fisherhamlet_description10:
                    $ endgame_howlersdell_leader_points += 1
                    $ custom1 = "Having no letter from {color=#f6d6bd}Thais{/color}, you shared the general description of {color=#f6d6bd}Howler’s Dell{/color} and vaguely described the fishing hamlet. “So it’s still the richest village in the North, even if led by pagans,” a priest summarized, “though lying to them about the fishing hamlet will hinder our negotiations. But what happened to {color=#f6d6bd}Steep House{/color}?”"
                else:
                    $ custom1 = "Having little to show from {color=#f6d6bd}Howler’s Dell{/color}, you shared the general description of the village. “So it’s still the richest place in the North, even if led by pagans, and placed at a convenient spot,” a priest summarized. “But what happened to {color=#f6d6bd}Steep House{/color}?”"
            if quest_ruins_choice == "lefttocity":
                $ endgame_howlersdell_leader_points += 1
                $ custom2 = "\n\nYour explanations made the city chief frown, but the council took your words kindly. “We’ll have no choice but to discuss if {color=#f6d6bd}Thais{/color} should be seen as guilty of her deeds,” an official let out a deep sigh. “Or,” a trader chipped in, “we could use it to our advantage.”\n\nWhile some of the council members spoke against it, raising their indignant voices, they were clearly outnumbered."
            elif quest_ruins_choice == "forgotten":
                $ custom2 = "\n\nWhile you described the village in detail, a few uncomfortable questions were left without answers. “At least there’s time to consider resettling this spot, knowing its condition,” concluded one of the artisans."
            elif quest_ruins_choice == "thais_defeated":
                $ endgame_howlersdell_leader_points -= 2
                $ custom2 = "\n\nYour explanations made the city chief frown, but it’s the mention of {color=#f6d6bd}Thais{/color} losing her position in the village that raised a few voices. A priest placed her chin or her hand. “Well, the druids are not going to greet us with open hands. We won’t be able to do much there.”"
            elif quest_ruins_choice == "thais_won":
                $ endgame_howlersdell_leader_points -= 2
                $ custom2 = "\n\nYour explanations made the city chief frown, but it’s the mention of {color=#f6d6bd}Thais’{/color} resentment that raised a few voices. “So you separated her from us, most likely for good.” One of the merchants shoots you a scowl. “Amateur.”\n\nThe discussion about the raided village got pushed to the side."
            elif quest_ruins_choice == "thais_alliance":
                $ endgame_howlersdell_leader_points += 2
                $ custom2 = "\n\nYou described the village in detail, and used as many convincing lies as you could to pin the responsibility for the fallen village onto the wrath of the herd, insisting that there’s no other threat that needs to be worried about. “At least there’s time to consider resettling this spot, knowing its condition,” concluded one of the artisans."
            elif quest_ruins_choice == "thais_alliance_fail":
                $ endgame_howlersdell_leader_points -= 1
                $ custom2 = "\n\nYour explanations made the city chief frown, but it’s the mention of {color=#f6d6bd}Thais’{/color} resentment that raised a few voices. “So you separated her from us, most likely for good.” One of the merchants shoots you a scowl. “Amateur.”\n\nThe discussion about the raided village got pushed to the side."
            elif ruinedvillage_truth:
                $ endgame_howlersdell_leader_points += 1
                $ custom2 = "\n\nYour explanations made the city chief frown, but the council took your words kindly. “We’ll have no choice but to discuss if {color=#f6d6bd}Thais{/color} should be seen as guilty of her deeds,” an official let out a deep sigh. “Or,” a trader chipped in, “we could use it to our advantage.”\n\nWhile some of the council members spoke against it, raising their indignant voices, they were clearly outnumbered."
            elif ruinedvillage_explored:
                $ custom2 = "\n\nWhile you described the village in detail, a few uncomfortable questions were left without answers. “At least there’s time to consider resettling this spot, knowing its condition,” concluded one of the artisans."
            elif ruinedvillage_firsttime:
                $ endgame_howlersdell_leader_points -= 1
                $ custom2 = "\n\nWhile you managed to vaguely describe the village, there were many unanswered questions. “We can’t even judge if the place is worth resettling,” lamented a clearly disappointed artisan."
            else:
                $ endgame_howlersdell_leader_points -= 2
                $ custom2 = "\n\nAfter your surprised look, you heard the mocking chuckle of an artisan. “Seriously? You haven’t even stumbled upon it?”"
            if quest_ruins_choice == "thais_defeated":
                $ custom3 = ""
            else:
                if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4:
                    $ endgame_howlersdell_leader_points += 2
                    if quest_explorepeninsula_description10b:
                        $ endgame_howlersdell_leader_points += 1
                        $ custom3 = "\n\nYou briefly described the recent prosperity you had brought to {color=#f6d6bd}Pelt of the North{/color}, as well as the general safety of the southern road, and after you explained that the druids will likely oppose any newcomers, you noticed the telling looks of the priests and the officials."
                    else:
                        $ custom3 = "\n\nYou ended with a brief description of the recent prosperity you had brought to {color=#f6d6bd}Pelt of the North{/color}, as well as the general safety of the southern road."
                elif iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2:
                    $ endgame_howlersdell_leader_points += 1
                    if quest_explorepeninsula_description10b:
                        $ endgame_howlersdell_leader_points += 1
                        $ custom3 = "\n\nYou briefly described the recent prosperity you had brought to {color=#f6d6bd}Pelt of the North{/color}, as well as the general safety of the southern road, and after you explained that the druids will likely oppose any newcomers, you noticed the telling looks of the priests and the officials."
                    else:
                        $ custom3 = "\n\nYou ended with a brief description of the recent prosperity you had brought to {color=#f6d6bd}Pelt of the North{/color}, as well as the general safety of the southern road."
                elif quest_explorepeninsula_description10b:
                    $ endgame_howlersdell_leader_points += 1
                    $ custom3 = "\n\nYou ended with a brief explanation that the druids will likely oppose any newcomers, and you noticed the telling looks of the priests and the officials."
                else:
                    $ custom3 = ""
            $ quest_explorepeninsula_points += endgame_howlersdell_leader_points
            if quest_ruins_choice == "thais_defeated" and endgame_howlersdell_leader_points >= 1:
                $ endgame_howlersdell_leader_points = 0
            if endgame_howlersdell_leader_points >= 4:
                $ endgame_howlersdell_leader_option = 1
                $ quest_explorepeninsula_points += 1
        if not oldpagos_firsttime:
            $ quest_explorepeninsula_points -= 2
            $ custom5 = "Learning that you’d never visited {color=#f6d6bd}Old Págos{/color} made the gathering worried. “Before the war, they used to be of great value to us, as stonecutters and builders,” you heard from one of the artisans. “I was hoping we could enter their hills with detailed plans for a new chapel, but now we risk wasting our time.”"
            $ custom6 = ""
        else:
            if quest_oldpagossupport == 2:
                $ endgame_oldpagos_leader_points += 3
                $ custom5 = "Learning about the plague of {color=#f6d6bd}Old Págos{/color} has “worried” the officials - mostly with the thought that you could have brought the illness with you. After some time, they discussed the promising future. “Pulling a tribe away from the verge of destruction wasn’t on the warden’s list of duties, but is a very welcome surprise,” you heard from one of the artisans, “and having them start the negotiations is just as much honey as I can swallow. Great job.”"
            elif quest_healingtheplague == 2:
                $ endgame_oldpagos_leader_points += 2
                $ custom5 = "Learning about the plague of {color=#f6d6bd}Old Págos{/color} has “worried” the officials - mostly with the thought that you could have brought the illness with you. After some time, they discussed the promising future. “Pulling a tribe away from the verge of destruction wasn’t on the warden’s list of duties, but is a very welcome surprise,” you heard from one of the artisans. “If we were to decide to move forward with our {i}investment{/i}, we could bring a few sketches to the village with our first spring caravan.”"
            else:
                $ endgame_oldpagos_leader_points -= 1
                $ custom5 = "Learning about the plague of {color=#f6d6bd}Old Págos{/color} has “worried” the officials - mostly with the thought that you could have brought the illness with you. After some time, they discussed the difficult future. “Having such a place weakened is against our interest,” you heard from one of the artisans. “I was hoping we could enter their hills with detailed plans for a new chapel, but now it would be waste of our time.”"
            if not monastery_firsttime:
                $ endgame_oldpagos_leader_points -= 1
                $ custom6 = "\n\n“Omitting {color=#f6d6bd}the monastery{/color} wasn’t wise,” mentioned a monk. “While their original thought comes from {color=#f6d6bd}Hovlavan{/color}, we’re not sure if they’re still loyal to The River of Truth.”"
            else:
                if quest_monasterysupport_description01:
                    $ endgame_oldpagos_leader_points += 2
                    $ custom6 = "\n\n“Gaining {color=#f6d6bd}the prelate’s{/color} trust is a great help,” a monk exchanged nods with the best-dressed priest. “We would be {i}glad{/i} to visit the place you described. Having the opportunity to send pilgrims to that {color=#f6d6bd}Library{/color} would bring even more life to those roads.”"
                elif quest_monasterysupport_description03:
                    $ endgame_oldpagos_leader_points -= 2
                    $ custom6 = "\n\n“Making {color=#f6d6bd}the prelate{/color} this distrustful is bad news,” a monk scowled at you. “We would be {i}glad{/i} to visit the place you described. Not a good bridge to burn, but I guess you simply lack the experience of handling {i}delicate{/i} negotiations.”"
                elif quest_monasterysupport_description01lie or quest_monasterysupport_description02:
                    $ custom6 = "\n\n“Too bad you weren’t able to gain {color=#f6d6bd}the monks’{/color} trust, but your description of {color=#f6d6bd}the monastery{/color} is a good foundation nevertheless,” added a monk after you shared what you knew, albeit “omitting” your visit to {color=#f6d6bd}The Library in Stone{/color}."
                else:
                    $ custom6 = "\n\n“Too bad you weren’t able to gain {color=#f6d6bd}the monks’{/color} trust, but your description of {color=#f6d6bd}the monastery{/color} is a good foundation nevertheless,” added a monk."
            if endgame_oldpagos_leader_points >= 3:
                $ endgame_oldpagos_leader_option = 1
            $ quest_explorepeninsula_points += endgame_oldpagos_leader_points
        if not whitemarshes_firsttime:
            $ quest_explorepeninsula_points -= 2
            $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that you had never actually reached the village, the inquisitive questions kept on coming for another few minutes. “Hard to believe you’d ignore such a crucial rumor,” chided one of the officials."
            $ custom9 = ""
        elif whitemarshes_destroyed:
            $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that the village is gone for good, the inquisitive questions kept on coming for another half an hour. “At least the issue of the undead is solved,” summed up one of the officials. “They got what they deserved.”"
            $ custom9 = ""
        else:
            if whitemarshes_nomoreundead:
                if whitemarshes_attacked:
                    $ endgame_whitemarshes_leader_points += 1
                    $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that the issue, while solved, has resulted in the bogs being closed for good, the inquisitive questions kept on coming for another half an hour. “At least we won’t need the services of a purging squad,” summed up a priest. “We can let the heretics rot in their tiny village.”"
                    if quest_explorepeninsula_description17:
                        $ endgame_whitemarshes_leader_points += 1
                        $ custom9 = "\n\nYou drew their attention to the vast peat field, and the artisans started to discuss the possibilities. “We could just take it all,” one of them finally mentioned, earning a scolding glance from the chief."
                    else:
                        $ custom9 = "\n\n“They had nothing we could use anyway,” one of the artisans waved it off."
                elif orentius_convinced:
                    $ endgame_whitemarshes_leader_points += 2
                    $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that the issue was not only solved, but has also most likely opened the village to the outside world, the inquisitive questions kept on coming for another half an hour. “Too bad that heretic is still around,” summed up a priest, “but at least we don’t have to send the purging squad. For now.”"
                    if quest_explorepeninsula_description17:
                        $ endgame_whitemarshes_leader_points += 1
                        $ custom9 = "\n\nYou drew their attention to the vast peat field, and the artisans started to discuss the possibilities. The room got a bit warmer."
                    else:
                        $ custom9 = "\n\n“They don’t really have anything we could use,” one of the artisans waved it off."
                elif orentius_banished:
                    $ endgame_whitemarshes_leader_points += 3
                    $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that the issue was not only solved, but has also most likely opened the village to the outside world, the inquisitive questions kept on coming for another half an hour. “With the heretic gone, it’s quite an opportunity,” summed up a priest, “and we don’t even have to send the purging squad. For now.”"
                    if quest_explorepeninsula_description17:
                        $ endgame_whitemarshes_leader_points += 1
                        $ custom9 = "\n\nYou drew their attention to the vast peat field, and the artisans started to discuss the possibilities. The room got a bit warmer."
                    else:
                        $ custom9 = "\n\n“They don’t really have anything we could use,” one of the artisans waved it off."
            else:
                if whitemarshes_attacked:
                    $ endgame_whitemarshes_leader_points -= 2
                    $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that not only were you not able to fix the issue, but the tribe will also most likely cut contact with the outside world for good, the inquisitive questions kept on coming for another half an hour. “At least we won’t need the services of a purging squad,” summed up a priest. “We can let the heretics rot in their tiny village.”"
                else:
                    $ endgame_whitemarshes_leader_points -= 1
                    $ custom8 = "“According to the reports of...” the city chief looked at a wax tablet, “{color=#f6d6bd}Tulia{/color}, I believe, {color=#f6d6bd}White Marshes{/color} is using the shells of the dead.”\n\nAfter you explained that you weren’t able to fix the issue, the inquisitive questions kept on coming for another half an hour. “Seems like we may need to send a purging squad,” summed up one of the priests."
                if quest_explorepeninsula_description17:
                    $ endgame_whitemarshes_leader_points += 1
                    $ custom9 = "\n\nYou drew their attention to the vast peat field, and the artisans started to discuss the possibilities. “We could just take it all,” one of them finally mentioned, earning a scolding glance from the chief."
                else:
                    $ custom9 = "\n\n“They have nothing we could use anyway,” one of the artisans waved it off."
            if endgame_whitemarshes_leader_points >= 3:
                $ endgame_whitemarshes_leader_option = 1
            $ quest_explorepeninsula_points += endgame_whitemarshes_leader_points
        if not creeks_firsttime:
            $ quest_explorepeninsula_points -= 2
            $ custom11 = "After hearing that you’d never visited {color=#f6d6bd}Creeks{/color}, the council’s confidence in you weakened, even though a few of the members were not aware of the tribe’s existence. “With no knowledge of what they can offer us, we’ll need to start everything from the ground,” said one of the traders. “Do we really need to send another spy?”"
            $ custom12 = ""
        else:
            if quest_creekssupport == 2:
                $ endgame_creeks_leader_points += 3
                $ custom11 = "After hearing that your visit to {color=#f6d6bd}Creeks{/color} has opened the gate for future negotiations, the council’s curiosity rose - a few of the members were not even aware of the tribe’s existence. “So you bring not just opportunities, but also promises,” said one of the traders. “Perhaps we could indeed use their weakness to our advantage.”"
            elif quest_creekssupport == 3:
                $ endgame_creeks_leader_points -= 2
                $ custom11 = "After hearing that your visit to {color=#f6d6bd}Creeks{/color} has closed the gate to future negotiations, the council’s disappointment was palpable, even though a few of the members were not even aware of the tribe’s existence. “So you put us in an even worse spot than we were before,” said one of the traders. “Now their weakness is of no value to us.”"
            elif quest_creekssupport == 1:
                $ endgame_creeks_leader_points += 1
                $ custom11 = "After hearing that your visit to {color=#f6d6bd}Creeks{/color} has opened the gate for future negotiations, the council’s curiosity rose - a few of the members were not even aware of the tribe’s existence. “So you bring no promises, just opportunities,” said one of the traders. “Perhaps we could indeed use their weakness to our advantage.”"
            elif quest_missinghunters:
                $ custom11 = "After hearing that your visit to {color=#f6d6bd}Creeks{/color} had ended with little to no promises, the council’s confidence in you weakened, even though a few of the members were not aware of the tribe’s existence. “So we hardly know of this place, and we’d need to start our work from the very beginning,” said one of the traders. “And not only that, the hunters there are {i}disappearing{/i}? Doesn’t seem to be worth the effort.”"
            else:
                $ endgame_creeks_leader_points -= 1
                $ custom11 = "After hearing that your visit to {color=#f6d6bd}Creeks{/color} had ended with little to no promises, the council’s confidence in you weakened, even though a few of the members were not aware of the tribe’s existence. “So we hardly know of this place, and we’d need to start our work from the very beginning,” said one of the traders. “Are some pelts and wood even worth the effort?”"
            if quest_explorepeninsula_description08:
                $ endgame_creeks_leader_points += 2
                $ custom12 = "\n\nYou were then confronted with {color=#f6d6bd}Tulia’s{/color} reports, now written down, about the dangers of the eastern trail. After the reassuring tale of your deeds, one of the clerks threw the tablet toward a bored guard. “Sounds like the trail can be tamed after all.”"
            elif quest_easternpath_points >= 4:
                $ endgame_creeks_leader_points += 1
                $ custom12 = "\n\nYou were then confronted with {color=#f6d6bd}Tulia’s{/color} reports, now written down, about the dangers of the eastern trail. After the reassuring tale of your deeds, one of the clerks threw the tablet toward a bored guard. “Could be better, could be worse. We can work with that.”"
            elif quest_easternpath_points >= 1:
                $ custom12 = "\n\nYou were then confronted with {color=#f6d6bd}Tulia’s{/color} reports, now written down on a tablet, about the dangers of the eastern trail, and while you didn’t have much reassurance to offer, one of the officials shrugged. “That’s a start, I guess."
            else:
                $ endgame_creeks_leader_points -= 1
                $ custom12 = "\n\nYou were then confronted with {color=#f6d6bd}Tulia’s{/color} reports, now written down on a tablet, about the dangers of the eastern trail, but you had no reassurance to offer."
            if endgame_creeks_leader_points >= 3:
                $ endgame_creeks_leader_option = 1
            $ quest_explorepeninsula_points += endgame_creeks_leader_points
        if not galerocks_firsttime:
            $ quest_explorepeninsula_points -= 2
            $ custom14 = "After hearing that you’d never visited {color=#f6d6bd}Gale Rocks{/color}, the council grew visibly upset. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Not knowing what to expect of them presents a great difficulty.”"
            $ custom15 = ""
            $ custom16 = ""
            $ custom17 = ""
        else:
            if quest_galerockssupport == 4:
                $ endgame_galerocks_leader_points -= 4
                $ custom14 = "After hearing that {color=#f6d6bd}Gale Rocks{/color} won’t budge when it comes to its relationship with the bandits, the council grew visibly upset. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Having the largest coastal village determined to act against the city’s interest presents a great difficulty.”"
            elif quest_galerockssupport == 3:
                $ endgame_galerocks_leader_points -= 2
                $ custom14 = "After hearing that {color=#f6d6bd}Gale Rocks{/color} is unwilling to loosen its relationship with the bandits, the council grew visibly upset. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Having the largest coastal village determined to act against the city’s interest presents a great difficulty.”"
            elif quest_galerockssupport == 2:
                $ endgame_galerocks_leader_points += 2
                $ custom14 = "The news of the relationship between {color=#f6d6bd}Gale Rocks{/color} and the bandits sparked a long discussion, but your assurance that the issue has been “taken care of” received a warm welcome. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Having the largest coastal village open to negotiations presents a great opportunity.”"
            elif quest_galerockssupport == 1:
                $ endgame_galerocks_leader_points += 1
                $ custom14 = "The news of the relationship between {color=#f6d6bd}Gale Rocks{/color} and the bandits sparked a long discussion, and your assurance that the issue can still be discussed further in spring did little to ease the tension. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Having the largest coastal village still irresolute presents some difficulties. At least you uncovered the hideout of, what’s her face, {color=#f6d6bd}Glaucia{/color}.”"
            else:
                $ custom14 = "The news that your time in {color=#f6d6bd}Gale Rocks{/color} didn’t lead to any promises received cold looks. “According to the scrolls, they used to be of great value to the guild,” said one of the traders. “Not knowing what to expect of them presents a great difficulty.”"
            if galerocks_iuno_about_oldtunnel_cleared:
                $ endgame_galerocks_leader_points += 1
                $ custom15 = "\n\n“At least reaching the village won’t be too difficult now, with the tribe ready to restore its tunnel,” added an official. "
            elif oldtunnel_inside_opened:
                $ custom15 = "\n\n“At least the tunnel is open now. Though who knows for how long,” added an official. "
            else:
                $ endgame_galerocks_leader_points -= 1
                $ custom15 = "\n\n“With the tunnel closed, even a small caravan would struggle to reach the village,” added an official. "
            if quest_explorepeninsula_description18:
                $ endgame_galerocks_leader_points += 1
                $ custom16 = "“We now have a good understanding of the village’s wares and needs,” another trader chipped in with a grateful nod."
            elif galerocks_resource_barrels or galerocks_resource_fish or galerocks_resource_salt:
                $ custom16 = "“Whatever we’re going to do, we don’t know enough about the village’s needs and wares to offer our prices from a position of strength,” another trader chipped in with an annoyed grimace."
            else:
                $ endgame_galerocks_leader_points -= 1
                $ custom16 = "“But why would we even head to the village, if we know almost nothing about its wares?” Another trader chipped in with frustration."
            if endgame_galerocks_leader_points >= 3:
                $ endgame_galerocks_leader_option = 1
            $ quest_explorepeninsula_points += endgame_galerocks_leader_points
        if greenmountaintribe_banned and not cephasgaiane_available:
            $ quest_explorepeninsula_points -= 1
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. You described the violent greeting you received, and were met with distrustful glances."
        elif greenmountaintribe_banned:
            $ quest_explorepeninsula_points += 0
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. You explained that {color=#f6d6bd}the chief and the shaman{/color} will most likely keep to themselves, but won’t be willing to accept any messengers from the city. In return, you were met with a mixture of relief and distrust."
        elif quest_greenmountainsupport == 2:
            $ quest_explorepeninsula_points += 3
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. After you explained that {color=#f6d6bd}the chief and the shaman{/color} may not be exactly {i}friendly{/i}, but are willing to meet with the city messengers, you received surprised, yet relieved looks."
        elif quest_greenmountainsupport == 3:
            $ quest_explorepeninsula_points += 2
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. After you described how, so far, your meetings with {color=#f6d6bd}the chief and the shaman{/color} were rather fruitful, you were met with relieved looks."
        elif cephasgaiane_available:
            $ quest_explorepeninsula_points += 1
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. After you explained that {color=#f6d6bd}the chief and the shaman{/color} will most likely keep to themselves, you were met with relieved looks."
        elif quest_reachthepaganvillage:
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you were asked at the end of the meeting. After you admitted that, while they seem to stay away from the main roads, you never spoke with them, you were met with a mixture of relief and distrust."
        else:
            $ quest_explorepeninsula_points -= 1
            $ custom20 = "“Should we expect any {i}difficulties{/i} from {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” you heard at the end of the meeting, but no one was keen to explain who they are, and your questions were met with distrustful glances."
        if endgame_skip_villages:
            jump hovlavan_council03
        menu:
            '[custom1][custom2][custom3]
            '
            '(continue)':
                menu:
                    '[custom5][custom6]
                    '
                    '(continue)':
                        menu:
                            '[custom8][custom9]
                            '
                            '(continue)':

                                menu:
                                    '[custom11][custom12]
                                    '
                                    '(continue)':
                                        menu:
                                            '[custom14][custom15][custom16]
                                            '
                                            '(continue)':
                                                menu:
                                                    '[custom20]
                                                    '
                                                    'I notice that someone’s looking at me.':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I notice that someone’s looking at me.')
                                                        jump hovlavan_council03

    label hovlavan_council03:
        menu:
            'The oldest soul at the table, who started her life in the guild as a simple innkeep, smiles at you.
            \n\n“Where do {i}you{/i} think we should start, [pcname]?”
            '
            '“What do you mean?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean?”')
                if endgame_howlersdell_leader_option or endgame_oldpagos_leader_option or endgame_whitemarshes_leader_option or endgame_creeks_leader_option or endgame_galerocks_leader_option:
                    if endgame_howlersdell_leader_option and quest_ruins_choice == "thais_alliance":
                        menu:
                            'One of the artisans chips in. “We need to discuss this in detail, of course, but we can’t bring guards and builders to all the villages at once. Since you know the peninsula better than anyone, where do you think would be the best starting point?”
                            '
                            'It’s too late for me to betray {color=#f6d6bd}Thais{/color}. “{color=#f6d6bd}Howler’s Dell{/color} is strong, prosperous, and placed close to the valley.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s too late for me to betray {color=#f6d6bd}Thais{/color}. “{color=#f6d6bd}Howler’s Dell{/color} is strong, prosperous, and placed close to the valley.”')
                                $ quest_explorepeninsula_mainvillage = "howlersdell"
                                jump hovlavan_council04
                    else:
                        menu:
                            'One of the artisans chips in. “We need to discuss this in detail, of course, but we can’t bring guards and builders to all the villages at once. Since you know the peninsula better than anyone, where do you think would be the best starting point?”
                            '
                            '“{color=#f6d6bd}Howler’s Dell{/color} is strong, prosperous, and placed close to the valley.”' if endgame_howlersdell_leader_option:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Howler’s Dell{/color} is strong, prosperous, and placed close to the valley.”')
                                $ quest_explorepeninsula_mainvillage = "howlersdell"
                                jump hovlavan_council04
                            '“{color=#f6d6bd}Old Págos{/color} will need you, yet has a lot to offer.”' if endgame_oldpagos_leader_option and not quest_monasterysupport_description01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Old Págos{/color} will need you, yet has a lot to offer.”')
                                $ quest_explorepeninsula_mainvillage = "oldpagos"
                                jump hovlavan_council04
                            '“{color=#f6d6bd}Old Págos{/color} has a lot to offer, and the monks will secure the tribe’s loyalty.”' if endgame_oldpagos_leader_option and quest_monasterysupport_description01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Old Págos{/color} has a lot to offer, and the monks will secure the tribe’s loyalty.”')
                                $ quest_explorepeninsula_mainvillage = "oldpagosandmonks"
                                jump hovlavan_council04
                            '“{color=#f6d6bd}White Marshes{/color} is weakened, and lacks guidance. You can turn them into the perfect outpost.”' if endgame_whitemarshes_leader_option:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} is weakened, and lacks guidance. You can turn them into the perfect outpost.”')
                                $ quest_explorepeninsula_mainvillage = "whitemarshes"
                                jump hovlavan_council04
                            '“{color=#f6d6bd}Gale Rocks{/color} is more experienced in trade than any other village. Together, you can skip the difficult first steps.”' if endgame_galerocks_leader_option:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Gale Rocks{/color} is more experienced in trade than any other village. Together, you can skip the difficult first steps.”')
                                $ quest_explorepeninsula_mainvillage = "galerocks"
                                jump hovlavan_council04
                            '“{color=#f6d6bd}Creeks{/color} may be small, but has great potential and ambitions.”' if endgame_creeks_leader_option:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} may be small, but has great potential and ambitions.”')
                                $ quest_explorepeninsula_mainvillage = "creeks"
                                jump hovlavan_council04
                            'I shrug. “I know nothing about trade.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “I know nothing about trade.”')
                                if endgame_howlersdell_leader_option:
                                    $ quest_explorepeninsula_mainvillage = "howlersdell"
                                elif endgame_galerocks_leader_option:
                                    $ quest_explorepeninsula_mainvillage = "galerocks"
                                elif endgame_oldpagos_leader_option:
                                    $ quest_explorepeninsula_mainvillage = "oldpagos"
                                elif endgame_whitemarshes_leader_option:
                                    $ quest_explorepeninsula_mainvillage = "whitemarshes"
                                elif endgame_creeks_leader_option:
                                    $ quest_explorepeninsula_mainvillage = "creeks"
                                jump hovlavan_council04
                else:
                    $ quest_explorepeninsula_mainvillage = 0
                    $ world_peninsulaname = "the northern peninsula"
                    if quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_3:
                        $ quest_explorepeninsula_result = "success3"
                    elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_2:
                        $ quest_explorepeninsula_result = "success2"
                    elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_1:
                        $ quest_explorepeninsula_result = "success1"
                    elif quest_explorepeninsula_points >= 4:
                        $ quest_explorepeninsula_result = "fail1"
                    else:
                        $ quest_explorepeninsula_result = "fail2"
                    menu:
                        'Before she responds, the city chief stands up and looks around the room. “We’ve heard enough,” he proclaims, “and now we rest. Let’s resume tomorrow,” he then glances at you, “and you, roadwarden, wait for our call.”
                        '
                        '“Very well.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                            jump hovlavan_aftercouncil01
                        'I frown.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown.')
                            jump hovlavan_aftercouncil01
                        '“Just don’t waste {i}my{/i} time now.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just don’t waste {i}my{/i} time now.”')
                            jump hovlavan_aftercouncil01

    label hovlavan_council04:
        $ world_peninsulaname = "the northern peninsula"
        if quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_3:
            $ quest_explorepeninsula_result = "success3"
        elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_2:
            $ quest_explorepeninsula_result = "success2"
        elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_1:
            $ quest_explorepeninsula_result = "success1"
        elif quest_explorepeninsula_points >= 4:
            $ quest_explorepeninsula_mainvillage = 0
            $ quest_explorepeninsula_result = "fail1"
        else:
            $ quest_explorepeninsula_mainvillage = 0
            $ quest_explorepeninsula_result = "fail2"
        if quest_explorepeninsula_result == "fail1" or quest_explorepeninsula_result == "fail2" or quest_explorepeninsula_result == "success1":
            jump hovlavan_aftercouncil01
        else:
            menu:
                'A clerk puts a wax tablet on top of the pile, then opens another one, letting out a long sigh. “I keep writing {i}the peninsula{/i}... Does that place have any name?”
                '
                '“There’s one I can think of...”':
                    python:
                        world_peninsulaname = renpy.input("How would you call the peninsula?", default="", pixel_width=800, exclude="<>?;][}{,./1234567890!@#$%^&*()-_=+")
                        world_peninsulaname = world_peninsulaname.strip()
                        if not world_peninsulaname:
                            world_peninsulaname = "the northern peninsula"
                    nvl clear
                    pause 0.05
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s one I can think of...{color=#f6d6bd}%s{/color}.”' %world_peninsulaname)
                    jump hovlavan_aftercouncil01
                '“Not really.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really.”')
                    $ world_peninsulaname = "the northern peninsula"
                    nvl clear
                    jump hovlavan_aftercouncil01

label hovlavan_aftercouncilALL:
    label hovlavan_aftercouncil01:
        show areapicture ep_04 at basicfade
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_01main_theme_loop.ogg":
            play music "<loop 15.0>audio/track_01main_theme_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
        if item_asterionwine and item_asterionwine_pcknows_2:
            if coins >= 100:
                $ epilogue_bonus_savings_tier = 4
            elif coins >= 70:
                $ epilogue_bonus_savings_tier = 3
            elif coins >= 40:
                $ epilogue_bonus_savings_tier = 2
            else:
                $ epilogue_bonus_savings_tier = 1
        else:
            if coins >= 200:
                $ epilogue_bonus_savings_tier = 4
            elif coins >= 100:
                $ epilogue_bonus_savings_tier = 3
            elif coins >= 70:
                $ epilogue_bonus_savings_tier = 2
            elif coins >= 25:
                $ epilogue_bonus_savings_tier = 1
            else:
                $ epilogue_bonus_savings_tier = 0
        ########
        if item_axe03:
            $ epilogue_bonus_equipment_points += 3
        elif item_axe02 or item_axe02alt:
            $ epilogue_bonus_equipment_points += 2
        if item_gambeson02:
            $ epilogue_bonus_equipment_points += 2
        if item_crossbow:
            $ epilogue_bonus_equipment_points += 2
        if item_shield:
            $ epilogue_bonus_equipment_points += 1
        if item_golemglove:
            $ epilogue_bonus_equipment_points += 2
        if item_dragonhorn:
            $ epilogue_bonus_equipment_points += 1
        if item_magicchisel:
            $ epilogue_bonus_equipment_points += 1
        if item_blindingpowder:
            $ epilogue_bonus_equipment_points += 1
        if (pc_battlecounter >= 12 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 32 and item_sharpeningpotion_used == day):
            $ epilogue_bonus_equipment_points += 2
        elif (pc_battlecounter >= 9 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 29 and item_sharpeningpotion_used == day):
            $ epilogue_bonus_equipment_points += 1
        if epilogue_bonus_equipment_points >= 10:
            $ epilogue_bonus_equipment_tier = 3
        elif epilogue_bonus_equipment_points >= 7:
            $ epilogue_bonus_equipment_tier = 2
        elif epilogue_bonus_equipment_points >= 4:
            $ epilogue_bonus_equipment_tier = 1
        else:
            $ epilogue_bonus_equipment_tier = 0
        if quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_3:
            $ quest_explorepeninsula_result = "success3"
            $ quest_explorepeninsula = 2
            $ achievement_council = 3
        elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_2:
            $ quest_explorepeninsula_result = "success2"
            $ quest_explorepeninsula = 2
            $ achievement_council = 2
        elif quest_explorepeninsula_points >= quest_explorepeninsula_points_threshold_1:
            $ quest_explorepeninsula_result = "success1"
            $ quest_explorepeninsula = 2
            $ achievement_council = 1
        elif quest_explorepeninsula_points >= 4:
            $ quest_explorepeninsula_mainvillage = 0
            $ quest_explorepeninsula = 3
            $ quest_explorepeninsula_result = "fail1"
        else:
            $ quest_explorepeninsula_mainvillage = 0
            $ quest_explorepeninsula = 4
            $ quest_explorepeninsula_result = "fail2"
        $ renpy.notify("Quest completed: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Explore the Peninsula{/i}')
        if quest_explorepeninsula_result == "fail2":
            menu:
                'That very evening, the soldiers find you by the well - and take you to the interrogation chamber.
                \n\nThe accusations are brief, but hard to defend against. Failing your contract; sabotaging the city’s interest; wasting the guild’s resources; potential lies and manipulation; negligence of duty.
                \n\nAfter a night spent on the highest floor of the prison tower, you face the verdict. In the blink of an eye, your savings and possessions, including {color=#f6d6bd}[horsename]{/color}, are granted to the merchants. An armed squad takes you outside the gate and hands you a stone knife.
                \n\nWith no rations, armor, or dragon bones, you begin your banishment, with the sign of an hourglass burned into your cheek.
                '
                'I look above their shoulders at the crowd gathered to mock me, and seek the despaired eyes of my sibling.' if pc_goal == "ineedmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look above their shoulders at the crowd gathered to mock me, and seek the despaired eyes of my sibling.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'This is not the end. I’ll find the coins I need and fix it all.' if pc_goal == "ineedmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’ll find the coins I need and fix it all.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'I look above their shoulders, through the crowd gathered to mock me. This was meant to be my home, my safe haven.' if pc_goal == "iwantmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look above their shoulders, through the crowd gathered to mock me. This was meant to be my home, my safe haven.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'This is not the end. I’ll head for another city, start anew.' if pc_goal == "iwantmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’ll head for another city, start anew.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'I look above their shoulders, at the crowd gathered to mock me. This is not the way I wanted to be remembered.' if pc_goal == "iwanttoberemembered":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look above their shoulders, at the crowd gathered to mock me. This is not the way I wanted to be remembered.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'This is not the end. I’ll start anew, prove them all wrong.' if pc_goal == "iwanttoberemembered":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’ll start anew, prove them all wrong.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'I look above their shoulders, at the crowd gathered to mock me. Don’t they realize I’m their ally?' if pc_goal == "iwanttohelp":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look above their shoulders, at the crowd gathered to mock me. Don’t they realize I’m their ally?')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'This is not the end. They don’t see who I really am, but I’ll find a new home.' if pc_goal == "iwanttohelp":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. They don’t see who I really am, but I’ll find a new home.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'Can I ever really start anew? Wasn’t this my last chance?' if pc_goal == "iwanttostartanewlife":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Can I ever really start anew? Wasn’t this my last chance?')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'This is not the end. I can still find a new home.' if pc_goal == "iwanttostartanewlife":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I can still find a new home.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'I look above their shoulders, at the crowd gathered to mock me. The news about me will reach the other cities, sooner or later.' if pc_goal == "iwantstatus":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look above their shoulders, at the crowd gathered to mock me. The news about me will reach the other cities, sooner or later.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
                'Fuck them all. I’d rather leave The Dragonwoods for good than be like them.' if pc_goal == "iwantstatus":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Fuck them all. I’d rather leave The Dragonwoods for good than be like them.')
                    $ endgame_epilogue_fluff = "rip"
                    jump epilogue_slides01
        elif quest_explorepeninsula_result == "fail1":
            if pc_goal == "ineedmoney":
                if pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. Once you combine it with what you brought from the North, you’ve got enough to save your sibling from the debt collectors.
                        '
                        'Time to find the buyer for the Night’s Bane.' if item_asterionwine and item_asterionwine_pcknows_2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to find the buyer for the Night’s Bane.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                        'I should hire someone to help me protect my “wealth” before the deal is closed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should hire someone to help me protect my “wealth” before the deal is closed.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                        'I just can’t wait to bring them the good news.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just can’t wait to bring them the good news.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. You were paid fairly, but it’s still not enough to save the person for whom you left the city in the first place.
                        '
                        'Time to admit to them that I failed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to admit to them that I failed.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their impressive equipment and combat experience, they joined the ranks of the merchants’ guards, getting decent lawn terms. This, combined with selling the rider’s horse, was enough to rescue their loved one.\n\nThey spent long seasons observing the crates, barrels, and leaving, often craving their freedom, but clinging to hope that their path may change yet again. They knew that all it may take is meeting just the right soul at the right time."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their decent equipment and combat experience, they managed to join a group of mercenaries, losing an arm during a risky caravan trip through the late autumn.\n\nWhile it was enough to save their loved one, the rider had to sell their mount and weapons, using their scarce savings to learn a new trade."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, seeking risky, profitable opportunities between taking the harsh jobs in the harbor - but to no avail. With the arrival of winter, they knew they couldn’t wait for luck any longer - to save their loved one, they had to sell their mount to the guild.\n\nThey spent the next few brief, violent years paying off their debts as a mercenary, escorting expeditions of the wealthy."
                            jump epilogue_slides01
                        'This is not the end. I’ll find the coins I need, and fix it all.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’ll find the coins I need, and fix it all.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their impressive equipment and combat experience, they joined the ranks of the merchants’ guards, getting decent lawn terms. This, combined with selling the rider’s horse, was enough to rescue their loved one.\n\nThey spent long seasons observing the crates, barrels, and leaving, often craving their freedom, but clinging to hope that their path may change yet again. They knew that all it may take is meeting just the right soul at the right time."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their decent equipment and combat experience, they managed to join a group of mercenaries, losing an arm during a risky caravan trip through the late autumn.\n\nWhile it was enough to save their loved one, the rider had to sell their mount and weapons, using their scarce savings to learn a new trade."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, seeking risky, profitable opportunities between taking the harsh jobs in the harbor - but to no avail. With the arrival of winter, they knew they couldn’t wait for luck any longer - to save their loved one, they had to sell their mount to the guild.\n\nThey spent the next few brief, violent years paying off their debts as a mercenary, escorting expeditions of the wealthy."
                            jump epilogue_slides01
            if pc_goal == "iwantmoney":
                if pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. In combination with what you brought from the North, you’ve got enough to seek a decent room, and to add a few crates of wares to the caravans. The first of them should return just before winter.
                        '
                        'Time to find the buyer for the Night’s Bane.' if item_asterionwine and item_asterionwine_pcknows_2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to find the buyer for the Night’s Bane.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                        'Maybe I’ll invest in merchant ships instead.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I’ll invest in merchant ships instead.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                        'I deserve a luxurious evening.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I deserve a luxurious evening.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. You could try to invest in some wares, but definitely can’t stay idle at an inn - you have a mount to look after.
                        '
                        'I could look for some work for the colder months, I guess.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could look for some work for the colder months, I guess.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk, instead taking more risky tasks for the merchant guild. Thanks to their impressive equipment, decent combat experience, and resolve, they spent the remaining few decades among the high-ranking guards, though preferring to take care of things by themselves, rather than command the others.\n\nThose years were unremarkable, yet comfortable."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, taking the harsh jobs in the harbor. Every now and then, their decent equipment and combat experience allowed them to get a riskier task from the merchant guild, but they lacked resolve to commit to any trade for long.\n\nThey lived for a few boring, unremarkable years, finding their end on a road, during a robbery."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, taking the harsh jobs in the harbor. They lived a long, unremarkable life, looking after their horse and struggling to find a well-paying job."
                            jump epilogue_slides01
                        'I’ll just live comfortably until spring, then start another journey. That’s where the easy dragons are.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll just live comfortably until spring, then start another journey. That’s where the easy dragons are.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, spending their savings with little care, then taking the riskiest jobs for riders. Thanks to their impressive equipment, decent combat experience, and resolve, they spent a decade as a competent mercenary, until the weight of years and scars made them join a group of treasure-hunting adventurers.\n\nTheir final trip was meant to bring to the city a whole dragon corpse."
                            else:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, spending their savings with little care, then taking the riskiest jobs for riders. After a few violent years, their life, full of colorful memories of duty and pleasure, ended with a single mistake."
                            jump epilogue_slides01
            if pc_goal == "iwanttoberemembered":
                if quest_pc_goal == 2:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'My great deeds will need some time to reach these lands, now that the peninsula is abandoned for good.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My great deeds will need some time to reach these lands, now that the peninsula is abandoned for good.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next, violent decade earning new tales and songs among the northern tribes, yet even this wasn’t enough to satiate their hunger. Lost and confused, the rider took one last journey, not for glory, but for peace."
                                elif epilogue_bonus_equipment_tier >= 1:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons earning new tales and songs among the northern tribes, until their ever-hungry shell fed a pack of dragonlings. The rider was gone, but not forgotten."
                                else:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons seeking ways to be memorized by tales and songs, but soon fell to the hunting beasts, forgotten."
                            else:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times.\n\nTheir likeness has been carved in stone, to this day standing at the center of one of the northern villages."
                                else:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times."
                            jump epilogue_slides01
                        'This evening, I will revel like a hero.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This evening, I will revel like a hero.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next, violent decade earning new tales and songs among the northern tribes, yet even this wasn’t enough to satiate their hunger. Lost and confused, the rider took one last journey, not for glory, but for peace."
                                elif epilogue_bonus_equipment_tier >= 1:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons earning new tales and songs among the northern tribes, until their ever-hungry shell fed a pack of dragonlings. The rider was gone, but not forgotten."
                                else:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons seeking ways to be memorized by tales and songs, but soon fell to the hunting beasts, forgotten."
                            else:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times.\n\nTheir likeness has been carved in stone, to this day standing at the center of one of the northern villages."
                                else:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'This is not the way I wanted to be remembered. I wasted my journey.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the way I wanted to be remembered. I wasted my journey.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, and thanks to their impressive equipment, decent combat experience, and resolve, they managed to get a few decent tasks as a mercenary. Once their horse got caught by a massive cat, the rider reached a desolate village, where they started a new adventuring team, once again eager to chase after glory."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, and thanks to their decent equipment, combat experience, and resolve, they managed to get a few decent tasks as a mercenary. After a few brief, violent years, the rider got caught by a massive cat, to the very end thinking that they deserved {i}better{/i}."
                            else:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, but finding no opportunities for a rider, they offered their services to the guild. They spent the next few brief, violent years making ends meet as a mercenary, to the end thinking that they deserved {i}better{/i}."
                            jump epilogue_slides01
                        'This is not the end. I’m wiser and more experienced, I can still play my part, become the hero of The Dragonwoods.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’m wiser and more experienced, I can still play my part, become the hero of The Dragonwoods.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They put their impressive equipment, decent combat experience, and resolve, to use, and sought new, brave opportunities among the autumn fogs. They saved many, and while the rider has met a grievous end, their name was immortalized in a single song about their brave journeys."
                            elif epilogue_bonus_equipment_tier >= 1:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They put their decent equipment, combat experience, and resolve, to use, and sought new, brave opportunities among the autumn fogs. They saved many, but the only song that immortalized the rider’s name was the one about their violent death."
                            else:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They sought new, brave opportunities among the autumn fogs, but their name never reached any tales."
                            jump epilogue_slides01
            if pc_goal == "iwanttohelp":
                if quest_pc_goal == 2:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'With the peninsula abandoned, most of my efforts to keep the tribes safe will go to waste.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the peninsula abandoned, most of my efforts to keep the tribes safe will go to waste.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                elif epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                if epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                            jump epilogue_slides01
                        'I deserve my rest. I helped many people.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I deserve my rest. I helped many people.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                elif epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                if epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'I wasted my journey. I’m too weak to help people by myself.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wasted my journey. I’m too weak to help people by myself.')
                            if epilogue_bonus_savings_tier >= 2:
                                $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            jump epilogue_slides01
                        'I’m not done yet. I can still change this land.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not done yet. I can still change this land.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. The always-hungry desire to change The Dragonwoods for the better never left their soul. Soon, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            jump epilogue_slides01
            if pc_goal == "iwanttostartanewlife":
                if quest_pc_goal == 2:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It’s enough to help you start a new life.
                        '
                        'Thais isn’t going to accept my failure. (disabled)' if pc_goal_iwantnewlife_howlersdell:
                            pass
                        'I’ll buy some seeds and tools, and reach {color=#f6d6bd}Creeks{/color} before winter.' if pc_goal_iwantnewlife_creeks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some seeds and tools, and reach {color=#f6d6bd}Creeks{/color} before winter.')
                            $ endgame_newlife_selected = "creeks"
                            $ endgame_epilogue_fluff = "reached the people of {color=#f6d6bd}Creeks{/color} safely. Without the city’s support, the beasts kept the roads dangerous, and after a few years even the most experienced rider in the North found their end in the wilderness. But not before they shared countless memories with their new family."
                            jump epilogue_slides01
                        'I’ll buy some decent blades for the guards of {color=#f6d6bd}Gale Rocks{/color}, and travel there soon.' if pc_goal_iwantnewlife_galerocks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some decent blades for the guards of {color=#f6d6bd}Gale Rocks{/color}, and travel there soon.')
                            $ endgame_newlife_selected = "galerocks"
                            $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Gale Rocks{/color}. Without the city’s support, the beasts kept the roads dangerous, and there wasn’t much work left for a lone rider. They joined the other guards on their patrols and their days got dull, slow, and tiresome, but also - peaceful."
                            if glaucia_about_galerocksdecision_liedto:
                                $ endgame_epilogue_fluff = "spent some time with the people of {color=#f6d6bd}Gale Rocks{/color}, but {color=#f6d6bd}Glaucia{/color} had no mercy to spare. As soon as she learned about the rider’s betrayal, she set up a trap, using the connections she had in her tribe.\n\nShe made sure to properly burn the warden’s shell. The peninsula didn’t need another awoken."
                            jump epilogue_slides01
                        'I’ll buy a few rare ingredients from the alchemists and hide from my problems in {color=#f6d6bd}the monastery{/color}.' if pc_goal_iwantnewlife_monastery:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy a few rare ingredients from the alchemists and hide from my problems in {color=#f6d6bd}the monastery{/color}.')
                            $ endgame_newlife_selected = "monastery"
                            $ endgame_epilogue_fluff = "spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition.\n\nWithout the city’s support, the beasts kept the roads dangerous. In the following decades, the order only drifted further away from the orthodox beliefs of The River of Truth, luring curious heretics at first, then the inquisitors, and finally - the bloodshed."
                            jump epilogue_slides01
                        'I’ll buy some rare supplies and traveling equipment and get back to {color=#f6d6bd}Glaucia’s{/color} hideout.' if pc_goal_iwantnewlife_bandits:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some rare supplies and traveling equipment and get back to {color=#f6d6bd}Glaucia’s{/color} hideout.')
                            $ endgame_newlife_selected = "bandits"
                            $ endgame_epilogue_fluff = "bandits"
                            jump epilogue_slides01
                        'Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.' if endgame_asterion_invitation and not pc_goal_iwantnewlife_creeks and not pc_goal_iwantnewlife_monastery and not pc_goal_iwantnewlife_galerocks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.')
                            $ endgame_newlife_selected = "asterion"
                            $ endgame_epilogue_fluff = "spent a few seasons at {color=#f6d6bd}Asterion’s{/color} village, serving as a messenger between the city and the settlements that surround it. After some time, they learned about another opportunity - the owner of a roadside inn needed a full-time guard for their patrons.\n\nAfter working for a few years as a messenger and a mercenary, the roadwarden’s new friendships protected them from the consequences of their past."
                            jump epilogue_slides01
                        'I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.')
                            $ endgame_newlife_selected = "city"
                            $ endgame_epilogue_fluff = "tried to blend in with the routine of the cityfolk, drawing little attention and keeping their stories to themselves, but their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you until summer, but you doubt the tribes of the peninsula would take you in with open arms.
                        '
                        'Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.' if endgame_asterion_invitation:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.')
                            $ endgame_newlife_selected = "asterion"
                            $ endgame_epilogue_fluff = "spent a few seasons at {color=#f6d6bd}Asterion’s{/color} village, serving as a messenger between the city and the settlements that surround it. After some time, they learned about another opportunity - the owner of a roadside inn needed a full-time guard for their patrons.\n\nAfter working for a few years as a messenger and a mercenary, the roadwarden’s new friendships protected them from the consequences of their past."
                            jump epilogue_slides01
                        'I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.')
                            $ endgame_newlife_selected = "city"
                            $ endgame_epilogue_fluff = "tried to blend in with the routine of the cityfolk, drawing little attention and keeping their stories to themselves, but their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
                        'This is not the end. I can still find a new home.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I can still find a new home.')
                            $ endgame_newlife_selected = "journey"
                            $ endgame_epilogue_fluff = "didn’t receive the backing of the city officials. They sought new opportunities as a traveling mercenary, hoping to find a place that would hire them for longer, but, after drawing plenty of attention, their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
            if pc_goal == "iwantstatus":
                if quest_pc_goal == 2:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket in your hands, and a much heavier burden on your shoulders. Everything you tried to accomplish, your web of connections... For nothing.
                        '
                        'This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.')
                            $ endgame_epilogue_fluff = "sunk into the routine of the cityfolk, taking risky jobs from the guild, and sometimes earning a bit on the side. Yet, for whatever reason, those efforts earned them little gratitude as the merchants and officials kept their deals in coins, never asking for favors, and never returning them.\n\nFinally, the rider put everything on one, risky attempt, offering an employer of them some dirt on another, and the consequences of this betrayal quickly ended their story."
                            jump epilogue_slides01
                        'I’ll get on the first ship and head for another city, start anew.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll get on the first ship and head for another city, start anew.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, for a few years shaking the local underground, until they were forced to leave again, and again - and were never heard of thereafter."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, but this good fortune ended with the third dagger hitting them in the back."
                            else:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites, but they never rose above the lower-rank thugs. Then they left again, and again - and were never heard of thereafter."
                            jump epilogue_slides01
                else:
                    menu:
                        'After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment won’t proceed any further,” you finally hear, “but your services are much appreciated.”
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you until summer, but you’re now only further away from your original goal.
                        '
                        'This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.')
                            $ endgame_epilogue_fluff = "sunk into the routine of the cityfolk, taking risky jobs from the guild, and sometimes earning a bit on the side. Yet, for whatever reason, those efforts earned them little gratitude as the merchants and officials kept their deals in coins, never asking for favors, and never returning them.\n\nFinally, the rider put everything on one, risky attempt, offering an employer of them some dirt on another, and the consequences of this betrayal quickly ended their story."
                            jump epilogue_slides01
                        'I’ll get on the first ship and head for another city, start anew.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll get on the first ship and head for another city, start anew.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, for a few years shaking the local underground, until they were forced to leave again, and again - and were never heard of thereafter."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, but this good fortune ended with the third dagger hitting them in the back."
                            else:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites, but they never rose above the lower-rank thugs. Then they left again, and again - and were never heard of thereafter."
                            jump epilogue_slides01
        else:
            if pc_goal == "ineedmoney":
                if pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. Once you combine it with what you brought from the North, you’ve got enough to save your sibling from the debt collectors.
                        '
                        'Time to find the buyer for the Night’s Bane.' if item_asterionwine and item_asterionwine_pcknows_2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to find the buyer for the Night’s Bane.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                        'I should hire someone to help me protect my “wealth” before the deal is closed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should hire someone to help me protect my “wealth” before the deal is closed.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                        'I just can’t wait to bring them the good news.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just can’t wait to bring them the good news.')
                            if epilogue_bonus_savings_tier >= 4:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having quite a bag of savings with them, they faced a peaceful winter. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            elif epilogue_bonus_savings_tier >= 3:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having some savings to spare, they managed to get through the lean few seasons. The knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk. Having a mount to support and no savings left for themselves, they faced a few lean seasons, but the knowledge and skills they gathered on their journey, as well as the support of their loved ones, helped them become a reliable messenger, valued among the villages spread around {color=#f6d6bd}Hovlavan{/color}."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. You were paid fairly, but it’s still not enough to save the person for whom you left the city in the first place.
                        '
                        'Time to admit to them that I failed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to admit to them that I failed.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their impressive equipment and combat experience, they joined the ranks of the merchants’ guards, getting decent lawn terms. This, combined with selling the rider’s horse, was enough to rescue their loved one.\n\nThey spent long seasons observing the crates, barrels, and leaving, often craving their freedom, but clinging to hope that their path may change yet again. They knew that all it may take is meeting just the right soul at the right time."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their decent equipment and combat experience, they managed to join a group of mercenaries, losing an arm during a risky caravan trip through the late autumn.\n\nWhile it was enough to save their loved one, the rider had to sell their mount and weapons, using their scarce savings to learn a new trade."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, seeking risky, profitable opportunities between taking the harsh jobs in the harbor - but to no avail. With the arrival of winter, they knew they couldn’t wait for luck any longer - to save their loved one, they had to sell their mount to the guild.\n\nThey spent the next few brief, violent years paying off their debts as a mercenary, escorting expeditions of the wealthy."
                            jump epilogue_slides01
                        'This is not the end. I’ll find the coins I need, and fix it all.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’ll find the coins I need, and fix it all.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their impressive equipment and combat experience, they joined the ranks of the merchants’ guards, getting decent lawn terms. This, combined with selling the rider’s horse, was enough to rescue their loved one.\n\nThey spent long seasons observing the crates, barrels, and leaving, often craving their freedom, but clinging to hope that their path may change yet again. They knew that all it may take is meeting just the right soul at the right time."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk. Thanks to their decent equipment and combat experience, they managed to join a group of mercenaries, losing an arm during a risky caravan trip through the late autumn.\n\nWhile it was enough to save their loved one, the rider had to sell their mount and weapons, using their scarce savings to learn a new trade."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, seeking risky, profitable opportunities between taking the harsh jobs in the harbor - but to no avail. With the arrival of winter, they knew they couldn’t wait for luck any longer - to save their loved one, they had to sell their mount to the guild.\n\nThey spent the next few brief, violent years paying off their debts as a mercenary, escorting expeditions of the wealthy."
                            jump epilogue_slides01
            if pc_goal == "iwantmoney":
                if pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. In combination with what you brought from the North, you’ve got enough to seek a decent room, and to add a few crates of wares to the caravans. The first of them should return just before winter.
                        '
                        'Time to find the buyer for the Night’s Bane.' if item_asterionwine and item_asterionwine_pcknows_2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to find the buyer for the Night’s Bane.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                        'Maybe I’ll invest in merchant ships instead.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I’ll invest in merchant ships instead.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                        'I deserve a luxurious evening.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I deserve a luxurious evening.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, building a new one instead, slowly gathering returns from their risky investments - two steps forward, one step back. From time to time they used their growing connections in the merchant guild to find employment, more from boredom than need, and used the extra savings to surround themselves with delights and safety.\n\nYears later, they became famous for offering work to the ambitious, new generation of adventurers. Not one of them could tell they were speaking with an ex-rider."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. You could try to invest in some wares, but definitely can’t stay idle at an inn - you have a mount to look after.
                        '
                        'I could look for some work for the colder months, I guess.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could look for some work for the colder months, I guess.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "didn’t return to their routine of a cityfolk, instead taking more risky tasks for the merchant guild. Thanks to their impressive equipment, decent combat experience, and resolve, they spent the remaining few decades among the high-ranking guards, though preferring to take care of things by themselves, rather than command the others.\n\nThose years were unremarkable, yet comfortable."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, taking the harsh jobs in the harbor. Every now and then, their decent equipment and combat experience allowed them to get a riskier task from the merchant guild, but they lacked resolve to commit to any trade for long.\n\nThey lived for a few boring, unremarkable years, finding their end on a road, during a robbery."
                            else:
                                $ endgame_epilogue_fluff = "quickly returned to their routine of a cityfolk, taking the harsh jobs in the harbor. They lived a long, unremarkable life, looking after their horse and struggling to find a well-paying job."
                            jump epilogue_slides01
                        'I’ll just live comfortably until spring, then start another journey. That’s where the easy dragons are.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll just live comfortably until spring, then start another journey. That’s where the easy dragons are.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, spending their savings with little care, then taking the riskiest jobs for riders. Thanks to their impressive equipment, decent combat experience, and resolve, they spent a decade as a competent mercenary, until the weight of years and scars made them join a group of treasure-hunting adventurers.\n\nTheir final trip was meant to bring to the city a whole dragon corpse."
                            else:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, spending their savings with little care, then taking the riskiest jobs for riders. After a few violent years, their life, full of colorful memories of duty and pleasure, ended with a single mistake."
                            jump epilogue_slides01
            if pc_goal == "iwanttoberemembered":
                if quest_pc_goal == 2:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "Next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'My great deeds will reach these lands, now that the city will start to trade with the Northerners.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My great deeds will reach these lands, now that the city will start to trade with the Northerners.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next, violent decade earning new tales and songs among the northern tribes, yet even this wasn’t enough to satiate their hunger. Lost and confused, the rider took one last journey, not for glory, but for peace."
                                elif epilogue_bonus_equipment_tier >= 1:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons earning new tales and songs among the northern tribes, until their ever-hungry shell fed a pack of dragonlings. The rider was gone, but not forgotten."
                                else:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons seeking ways to be memorized by tales and songs, but soon fell to the hunting beasts, forgotten."
                            else:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times.\n\nTheir likeness has been carved in stone, to this day standing at the center of one of the northern villages."
                                else:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times."
                            jump epilogue_slides01
                        'This evening, I will revel like a hero.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This evening, I will revel like a hero.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next, violent decade earning new tales and songs among the northern tribes, yet even this wasn’t enough to satiate their hunger. Lost and confused, the rider took one last journey, not for glory, but for peace."
                                elif epilogue_bonus_equipment_tier >= 1:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons earning new tales and songs among the northern tribes, until their ever-hungry shell fed a pack of dragonlings. The rider was gone, but not forgotten."
                                else:
                                    $ endgame_epilogue_fluff = "rejected the routine of the cityfolk, and left the safe walls soon after the thaw. They spent the next few brief, violent seasons seeking ways to be memorized by tales and songs, but soon fell to the hunting beasts, forgotten."
                            else:
                                if epilogue_bonus_equipment_tier >= 3:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times.\n\nTheir likeness has been carved in stone, to this day standing at the center of one of the northern villages."
                                else:
                                    $ endgame_epilogue_fluff = "struggled to return to the routine of the cityfolk, feeling choked by the walls, but also pondering on the night when they had rejected the dream of becoming {i}the hero of the North{/i}.\n\nAfter a few slow seasons, they returned to the path of a roadwarden, earning grateful tales and favors over the decades, but putting their own well-being and safety before fame, at all times."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'This is not the way I wanted to be remembered. I wasted my journey.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the way I wanted to be remembered. I wasted my journey.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, and thanks to their impressive equipment, decent combat experience, and resolve, they managed to get a few decent tasks as a mercenary. Once their horse got caught by a massive cat, the rider reached a desolate village, where they started a new adventuring team, once again eager to chase after glory."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, and thanks to their decent equipment, combat experience, and resolve, they managed to get a few decent tasks as a mercenary. After a few brief, violent years, the rider got caught by a massive cat, to the very end thinking that they deserved {i}better{/i}."
                            else:
                                $ endgame_epilogue_fluff = "at first rejected the routine of the cityfolk, but finding no opportunities for a rider, they offered their services to the guild. They spent the next few brief, violent years making ends meet as a mercenary, to the end thinking that they deserved {i}better{/i}."
                            jump epilogue_slides01
                        'This is not the end. I’m wiser and more experienced, I can still play my part, become the hero of The Dragonwoods.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I’m wiser and more experienced, I can still play my part, become the hero of The Dragonwoods.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They put their impressive equipment, decent combat experience, and resolve, to use, and sought new, brave opportunities among the autumn fogs. They saved many, and while the rider has met a grievous end, their name was immortalized in a single song about their brave journeys."
                            elif epilogue_bonus_equipment_tier >= 1:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They put their decent equipment, combat experience, and resolve, to use, and sought new, brave opportunities among the autumn fogs. They saved many, but the only song that immortalized the rider’s name was the one about their violent death."
                            else:
                                $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. They sought new, brave opportunities among the autumn fogs, but their name never reached any tales."
                            jump epilogue_slides01
            if pc_goal == "iwanttohelp":
                if quest_pc_goal == 2:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'With the city sending its people North, my efforts to keep the tribes safe won’t go to waste.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- With the city sending its people North, my efforts to keep the tribes safe won’t go to waste.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                elif epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                if epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                            jump epilogue_slides01
                        'I deserve my rest. I helped many people.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I deserve my rest. I helped many people.')
                            if endgame_epilogue_evil:
                                if epilogue_bonus_equipment_tier >= 3:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better couldn’t leave their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Thanks to their impressive equipment and combat experience, they managed to find shelter in a friendly village, where they stayed for the remaining decades."
                                elif epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild.\n\nThe roadwarden aided many tribes, gathering friendships and help as the seasons went on, but their shell couldn’t handle the hardships of their path. They met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few tribes, but, being forced to stay on the move, they rarely received help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                if epilogue_bonus_equipment_tier >= 2:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again, signing a new contract with the merchant guild. This time, however, they understood they can’t “save” The Dragonwoods on their own.\n\nThe rider returned to Hag Hills, aiding the tribes both north and south from it, helping them while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the villages, spending the remaining lazy decades as a guard and a dear friend."
                                else:
                                    if epilogue_bonus_savings_tier >= 2:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of somewhat comfortable living, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                                    else:
                                        $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk. After a year of struggling to provide for their palfrey, they hit the road again - this time without the support of the merchant guild, but with the understanding they can’t “save” The Dragonwoods on their own.\n\nThe rider aided many tribes while putting their own well-being and safety above their sacrifice. After a few years, with their palfrey too exhausted to continue their travels, they settled in one of the befriended villages, spending the remaining lazy decades as a guard."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "\The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you and {color=#f6d6bd}[horsename]{/color} until summer.
                        '
                        'I wasted my journey. I’m too weak to help people by myself.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wasted my journey. I’m too weak to help people by myself.')
                            if epilogue_bonus_savings_tier >= 2:
                                $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of somewhat comfortable living, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            else:
                                $ endgame_epilogue_fluff = "tried to get used to the routine of the cityfolk, but the always-hungry desire to change The Dragonwoods for the better never left their soul. After a year of struggling to provide for their palfrey, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            jump epilogue_slides01
                        'I’m not done yet. I can still change this land.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not done yet. I can still change this land.')
                            $ endgame_epilogue_fluff = "rejected the routine of the cityfolk. The always-hungry desire to change The Dragonwoods for the better never left their soul. Soon, they hit the road again, this time without the support of the city officials.\n\nThe rider managed to aid a few travelers and hamlets, but, being forced to stay on the move, they received no help in return. It didn’t take long before they met their end in the middle of nowhere, shot dead while intervening in a robbery."
                            jump epilogue_slides01
            if pc_goal == "iwanttostartanewlife":
                if quest_pc_goal == 2:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It’s enough to help you start a new life.
                        '
                        'I buy myself some decent clothes, and something nice for {color=#f6d6bd}Thais{/color}.' if pc_goal_iwantnewlife_howlersdell:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I buy myself some decent clothes, and something nice for {color=#f6d6bd}Thais{/color}.')
                            $ endgame_newlife_selected = "howlersdell"
                            if quest_explorepeninsula_result == "success1":
                                $ endgame_epilogue_fluff = "spent a few years with the people of {color=#f6d6bd}Howler’s Dell{/color}, enjoying great pleasures for little work, but were never seen as a part of the village. Once their past caught up with them and they sought help from {color=#f6d6bd}Thais{/color}, she used the opportunity to trade her “ally’s” safety for her future gains."
                            elif quest_explorepeninsula_result == "success2":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Howler’s Dell{/color}, enjoying great pleasures for little work, yet finding approval among their neighbors, being seen as the person responsible for the village’s new prosperity.\n\nOnce their past caught up with them and they sought help from {color=#f6d6bd}Thais{/color}, she risked her own reputation for “her warden’s” sake, tightening the bond between them even further."
                            elif quest_explorepeninsula_result == "success3":
                                $ endgame_epilogue_fluff = "spent a few years with the people of {color=#f6d6bd}Howler’s Dell{/color}, enjoying great pleasures for little work, yet finding approval among their neighbors, being seen as the person responsible for the village’s new prosperity.\n\n{color=#f6d6bd}Thais{/color}, worried about the roadwarden’s strong position among her guards, decided to get rid of the risk, and sent them on a mission from which they never returned."
                            jump epilogue_slides01
                        'I’ll buy some seeds and tools, and reach {color=#f6d6bd}Creeks{/color} before winter.' if pc_goal_iwantnewlife_creeks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some seeds and tools, and reach {color=#f6d6bd}Creeks{/color} before winter.')
                            $ endgame_newlife_selected = "creeks"
                            if quest_explorepeninsula_result == "success1":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Creeks{/color}. The roads grew safer, adding even more kindling to the tribe’s ambitions. Finally, after ten years, the roadwarden found their end in the wilderness, but not before they shared countless memories with their new family."
                            elif quest_explorepeninsula_result == "success2":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Creeks{/color}. The roads grew safer, adding even more kindling to the tribe’s ambitions. Finally, once their shell was withered from age, the roadwarden found their end in the wilderness. But not before they shared countless memories with their new family."
                            elif quest_explorepeninsula_result == "success3":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Creeks{/color}. The roads grew safer quickly, adding even more kindling to the tribe’s ambitions. The roadwarden’s past finally caught up with them after a few colorful decades, but their family was there to protect them."
                            jump epilogue_slides01
                        'I’ll buy some decent blades for the guards of {color=#f6d6bd}Gale Rocks{/color}, and travel there soon.' if pc_goal_iwantnewlife_galerocks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some decent blades for the guards of {color=#f6d6bd}Gale Rocks{/color}, and travel there soon.')
                            $ endgame_newlife_selected = "galerocks"
                            if glaucia_about_galerocksdecision_liedto:
                                $ endgame_epilogue_fluff = "spent some time with the people of {color=#f6d6bd}Gale Rocks{/color}, but {color=#f6d6bd}Glaucia{/color} had no mercy to spare. As soon as she learned about the rider’s betrayal, she set up a trap, using the connections she had in her tribe.\n\nShe made sure to properly burn the warden’s shell. The peninsula didn’t need another awoken."
                            elif quest_explorepeninsula_result == "success1":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it. Once their palfrey died from the attack of a noble griffon, the rider became the protector of the tunnels.\n\nThey spent many years observing the road, hoping their past wouldn’t catch up with them."
                            elif quest_explorepeninsula_result == "success2":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it. Once their palfrey died from the attack of a noble griffon, the rider became the protector of the tunnels.\n\nAfter a few years, the roads became so crowded the warden had little time to worry about their past."
                            elif quest_explorepeninsula_result == "success3":
                                $ endgame_epilogue_fluff = "spent many years with the people of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it. Once their palfrey died from the attack of a noble griffon, the rider became the protector of the tunnels.\n\nThe roadwarden’s past finally caught up with them after a few busy years, but their new tribe was there to protect them."
                            jump epilogue_slides01
                        'I’ll buy a few rare ingredients from the alchemists and hide from my problems in {color=#f6d6bd}the monastery{/color}.' if pc_goal_iwantnewlife_monastery:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy a few rare ingredients from the alchemists and hide from my problems in {color=#f6d6bd}the monastery{/color}.')
                            $ endgame_newlife_selected = "monastery"
                            if quest_explorepeninsula_result == "success1":
                                $ endgame_epilogue_fluff = "spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition. They never had to confront their past, and died of old age, forgotten by all."
                            elif quest_explorepeninsula_result == "success2":
                                $ endgame_epilogue_fluff = "spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition. As the North became safer, the order’s unusual project grew famous. Whenever a new pilgrimage showed up at the gates, one of the monks hid in the darkest cave, afraid their past might still catch up with them."
                            elif quest_explorepeninsula_result == "success3":
                                $ endgame_epilogue_fluff = "spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition. As the North became safer, the order’s unusual project grew famous, and the old roadwarden, now reconciled with their past, gladly observed the new generations of The Dragonwoods as they seemed to forget the wounds left by The Southern Invasion."
                            jump epilogue_slides01
                        'I’ll buy some rare supplies and traveling equipment and get back to {color=#f6d6bd}Glaucia’s{/color} hideout.' if pc_goal_iwantnewlife_bandits:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll buy some rare supplies and traveling equipment and get back to {color=#f6d6bd}Glaucia’s{/color} hideout.')
                            $ endgame_newlife_selected = "bandits"
                            $ endgame_epilogue_fluff = "bandits"
                            jump epilogue_slides01
                        'Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.' if endgame_asterion_invitation and not pc_goal_iwantnewlife_howlersdell and not pc_goal_iwantnewlife_creeks and not pc_goal_iwantnewlife_galerocks and not pc_goal_iwantnewlife_monastery:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.')
                            $ endgame_newlife_selected = "asterion"
                            $ endgame_epilogue_fluff = "spent a few seasons at {color=#f6d6bd}Asterion’s{/color} village, serving as a messenger between the city and the settlements that surround it. After some time, they learned about another opportunity - the owner of a roadside inn needed a full-time guard for their patrons.\n\nAfter working for a few years as a messenger and a mercenary, the roadwarden’s new friendships protected them from the consequences of their past."
                            jump epilogue_slides01
                        'I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.')
                            $ endgame_newlife_selected = "city"
                            $ endgame_epilogue_fluff = "tried to blend in with the routine of the cityfolk, drawing little attention and keeping their stories to themselves, but their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you until summer, but you doubt the tribes of the peninsula would take you in with open arms.
                        '
                        'Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.' if endgame_asterion_invitation:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe {color=#f6d6bd}Asterion’s{/color} family could help me.')
                            $ endgame_newlife_selected = "asterion"
                            $ endgame_epilogue_fluff = "spent a few seasons at {color=#f6d6bd}Asterion’s{/color} village, serving as a messenger between the city and the settlements that surround it. After some time, they learned about another opportunity - the owner of a roadside inn needed a full-time guard for their patrons.\n\nAfter working for a few years as a messenger and a mercenary, the roadwarden’s new friendships protected them from the consequences of their past."
                            jump epilogue_slides01
                        'I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use these coins to protect myself. Find a new job in {color=#f6d6bd}Hovlavan{/color}.')
                            $ endgame_newlife_selected = "city"
                            $ endgame_epilogue_fluff = "tried to blend in with the routine of the cityfolk, drawing little attention and keeping their stories to themselves, but their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
                        'This is not the end. I can still find a new home.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is not the end. I can still find a new home.')
                            $ endgame_newlife_selected = "journey"
                            $ endgame_epilogue_fluff = "didn’t receive the backing of the city officials. They sought new opportunities as a traveling mercenary, hoping to find a place that would hire them for longer, but, after drawing plenty of attention, their past finally caught up with them - and the consequences were even more severe than they had expected."
                            jump epilogue_slides01
            if pc_goal == "iwantstatus":
                if quest_pc_goal == 2:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket under your shoulder, but the dragon bones inside it don’t really impress you.
                        '
                        'I should buy myself a fine robe. It’s time for me to tell the guild why they {i}can’t{/i} reject my candidacy for membership.' if not item_fancyclothes:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should buy myself a fine robe. It’s time for me to tell the guild why they {i}can’t{/i} reject my candidacy for membership.')
                            if endgame_epilogue_evil == 2:
                                $ endgame_epilogue_fluff = "spent over a decade spreading their influence, using their connections to blackmail and reward those who had a lot to offer. After a few years of hiding the true scale of their cruelty, maybe even from themselves, they were finally {i}pushed{/i} into using their first flask of poison. After that, they restrained themselves no longer.\n\nThe rider’s death, while painful, surprised no one and caused no grief, only further conflicts between those who claimed the right to their possessions."
                            elif endgame_epilogue_evil == 1:
                                $ endgame_epilogue_fluff = "spent two decades spreading their influence, using their connections to exchange favors with the leaders of the tribes and the guild. However, they made mistakes, often torn by doubt, and before they reached the end of their goals, their web got untangled.\n\nDuring their last few years using their sparse savings stored in another city, fallen from grace, but never forgetting the taste of their power."
                            else:
                                $ endgame_epilogue_fluff = "spent the next few decades spreading their influence slowly, using their connections to exchange favors with the leaders of the tribes and the guild. Their grasp was strong, but didn’t go too far, and they left the games of manipulation before anyone untangled their mysteries."
                            jump epilogue_slides01
                        'My fancy outfit could use some new jewelry. It’s time for me to tell the guild why they {i}can’t{/i} reject my candidacy for membership.' if item_fancyclothes:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My fancy outfit could use some new jewelry. It’s time for me to tell the guild why they {i}can’t{/i} reject my candidacy for membership.')
                            if endgame_epilogue_evil == 2:
                                $ endgame_epilogue_fluff = "spent over a decade spreading their influence, using their connections to blackmail and reward those who had a lot to offer. After a few years of hiding the true scale of their cruelty, maybe even from themselves, they were finally {i}pushed{/i} into using their first flask of poison. After that, they restrained themselves no longer.\n\nThe rider’s death, while painful, surprised no one and caused no grief, only further conflicts between those who claimed the right to their possessions."
                            elif endgame_epilogue_evil == 1:
                                $ endgame_epilogue_fluff = "spent two decades spreading their influence, using their connections to exchange favors with the leaders of the tribes and the guild. However, they made mistakes, often torn by doubt, and before they reached the end of their goals, their web got untangled.\n\nDuring their last few years using their sparse savings stored in another city, fallen from grace, but never forgetting the taste of their power."
                            else:
                                $ endgame_epilogue_fluff = "spent the next few decades spreading their influence slowly, using their connections to exchange favors with the leaders of the tribes and the guild. Their grasp was strong, but didn’t go too far, and they left the games of manipulation before anyone untangled their mysteries."
                            jump epilogue_slides01
                        'This is just the beginning. I struggle to hide my smirk.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is just the beginning. I struggle to hide my smirk.')
                            if endgame_epilogue_evil == 2:
                                $ endgame_epilogue_fluff = "spent over a decade spreading their influence, using their connections to blackmail and reward those who had a lot to offer. After a few years of hiding the true scale of their cruelty, maybe even from themselves, they were finally {i}pushed{/i} into using their first flask of poison. After that, they restrained themselves no longer.\n\nThe rider’s death, while painful, surprised no one and caused no grief, only further conflicts between those who claimed the right to their possessions."
                            elif endgame_epilogue_evil == 1:
                                $ endgame_epilogue_fluff = "spent two decades spreading their influence, using their connections to exchange favors with the leaders of the tribes and the guild. However, they made mistakes, often torn by doubt, and before they reached the end of their goals, their web got untangled.\n\nDuring their last few years using their sparse savings stored in another city, fallen from grace, but never forgetting the taste of their power."
                            else:
                                $ endgame_epilogue_fluff = "spent the next few decades spreading their influence slowly, using their connections to exchange favors with the leaders of the tribes and the guild. Their grasp was strong, but didn’t go too far, and they left the games of manipulation before anyone untangled their mysteries."
                            jump epilogue_slides01
                else:
                    if quest_explorepeninsula_result == "success1":
                        $ custom1 = "After five days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few clerks. “The discussed investment will proceed further, though with great caution,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success2":
                        $ custom1 = "After three days, you take part in a brief meeting in the guild’s chambers. You’re welcomed by a few council representatives. “We’re going to move forward with the investment,” you finally hear. “Your services are much appreciated.”"
                    elif quest_explorepeninsula_result == "success3":
                        $ custom1 = "The next day, you take part in another meeting in the guild’s chambers. The council representatives are not as numerous this time around, but you recognize a few of the main members, including the city chief. “You portrayed a troubled land with a promising future,” he tells you at the start, “and we’re going to be sure to direct that place accordingly. Good job, citizen.”"
                    menu:
                        '[custom1]
                        \n\nYou return to the street with a wooden casket, heavy with dragon bones. It will provide for you until summer, but you’re now only further away from your original goal.
                        '
                        'This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- This can’t be the end. I’ll meet with the guild again, become their messenger. Climb to the top.')
                            $ endgame_epilogue_fluff = "sunk into the routine of the cityfolk, taking risky jobs from the guild, and sometimes earning a bit on the side. Yet, for whatever reason, those efforts earned them little gratitude as the merchants and officials kept their deals in coins, never asking for favors, and never returning them.\n\nFinally, the rider put everything on one, risky attempt, offering an employer of them some dirt on another, and the consequences of this betrayal quickly ended their story."
                            $ endgame_epilogue_fluff = "sunk into the routine of the cityfolk, taking risky jobs from the guild, and sometimes earning a bit on the side. Yet, for whatever reason, those efforts earned them little gratitude as the merchants and officials kept their deals in coins, never asking for favors, and never returning them.\n\nFinally, the rider put everything on one, risky attempt, offering an employer of them some dirt on another, and the consequences of this betrayal quickly ended their story."
                            jump epilogue_slides01
                        'I’ll get on the first ship and head for another city, start anew.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll get on the first ship and head for another city, start anew.')
                            if epilogue_bonus_equipment_tier >= 3:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, for a few years shaking the local underground, until they were forced to leave again, and again - and were never heard of thereafter."
                            elif epilogue_bonus_equipment_tier >= 2:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites. Thanks to their decent equipment and combat experience, they managed to rise above the lower-rank thugs, but this good fortune ended with the third dagger hitting them in the back."
                            else:
                                $ endgame_epilogue_fluff = "reached another city, seeking a way to get on the good side of the local elites, but they never rose above the lower-rank thugs. Then they left again, and again - and were never heard of thereafter."
                            jump epilogue_slides01

label epilogue_slidesALL:
    label epilogue_slides01:
        nvl clear
        if quest_explorepeninsula_result != "fail2":
            $ quick_menu = 0
            hide screen quick_menu
            show screen endcredits()
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_01main_theme_loop.ogg":
            play music "<loop 15.0>audio/track_01main_theme_loop.ogg" fadeout 1.0 fadein 1.0
        if quest_explorepeninsula_result == "fail2":
            $ custom1 = "With each passing year, fewer and fewer people risked traveling North, until the forest reclaimed the valley, ending the trail for good. What happened to the tribes became a mystery, but according to the rumors, some of the villages fell, unwilling to unite despite the beasts, bandits, and undead."
            show areapicture ep_06a at basicfade
        elif quest_explorepeninsula_result == "fail1":
            $ custom1 = "As time went on, fewer and fewer people risked traveling North, until the valley became a dark trail, visited only by adventurers. The tribes grew even more distant, and were present only in rumors, as the dangerous {i}people of the woods{/i}, with mysterious beliefs, strange tongues, and never-healed grudges."
            show areapicture ep_06a at basicfade
        elif quest_explorepeninsula_result == "success1":
            $ custom1 = "The flow of merchants and supplies was slow, but steady. The decades went by, but the tribes kept their distance from the cityfolk, seeing in them only trading partners, but benefitting from the safer roads, restored shelters, and new inventions."
            show areapicture ep_06b at basicfade
        elif quest_explorepeninsula_result == "success2":
            $ custom1 = "The flow of merchants, soldiers, explorers, and supplies brought many changes to the North. While some of the tribes tried to stay independent, they couldn’t resist the temptation of new inventions, crops, and security.\n\nAfter a few generations, the sparse settlements were indistinguishable from the other regions of the province, with safe roads, strong walls, and regular visitors."
            show areapicture ep_06b at basicfade
        elif quest_explorepeninsula_result == "success3":
            $ custom1 = "The sudden flow of merchants, soldiers, explorers, and supplies shook the North. While at first the tribes opposed some of the presented opportunities, they couldn’t resist the temptation of new inventions, crops, and security.\n\nAfter a few years, artisans, herbalists, hunters, and poor cityfolk started to look for a new home in this rich land, and just a generation later, the officials of {color=#f6d6bd}Hovlavan{/color} cleared the wilderness in the southeast, preparing it for a new village loyal to its interests."
            show areapicture ep_06b at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            '[custom1]
            '
            '(continue)':
                if quest_explorepeninsula_result == "fail2":
                    jump epilogue_slides_pc
                jump epilogue_slides_pelt

    label epilogue_slides_pelt:
        if not peltnorth_firsttime:
            jump epilogue_slides_howlers
        $ endcredits_counter += 1
        $ custom2 = ""
        $ custom5 = ""
        if quest_explorepeninsula_result == "fail1":
            show areapicture ep_07a at basicfade
        else:
            show areapicture ep_07b at basicfade
        if quest_explorepeninsula_result == "fail1":
            if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "Despite the poor state of the peninsula, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s visit, allowing the innkeep to purchase steel traps for large game. A few years later, the inn was abandoned, to the goblins’ joy. The hunters moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad."
            else:
                $ custom1 = "The keeper of {color=#f6d6bd}Pelt of the North{/color} quickly forgot about the roadwarden’s visit. Once the roads got overgrown, further trade with the southern villages became close to impossible. After ten years, the hunters abandoned their inn, to the goblins’ joy, and disbanded soon after."
        elif quest_explorepeninsula_result == "success1" or quest_explorepeninsula_result == "success2":
            if quest_explorepeninsula_mainvillage == "howlersdell" or quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks" or quest_explorepeninsula_mainvillage == "whitemarshes":
                $ custom1 = "The trade route following the western trail greatly benefited the dwellers of {color=#f6d6bd}Pelt of the North{/color}. After a few more years, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad. The inn was sold to the city officials, and remained one of the few shelters in the dangerous North."
                if tulia_about_bandits_grateful or not tulia_about_bandits2:
                    $ custom5 = "\n\nOne of the new guards was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters. Unlike her new crew, she didn’t cross {color=#f6d6bd}Hag Hills{/color} ever again. Instead, she found work as a woodcutter in {color=#f6d6bd}Gale Rocks{/color}."
                else:
                    $ custom5 = ""
            elif iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "While the trade route was focused on the eastern trail, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s visit, allowing the innkeep to purchase steel traps for large game. After a few more years, the hunters moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad. The inn was sold to the city officials, and remained one of the few shelters in the dangerous North."
                if tulia_about_bandits_grateful or not tulia_about_bandits2:
                    $ custom5 = "\n\nOne of the new guards was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters. Unlike her new crew, she didn’t cross {color=#f6d6bd}Hag Hills{/color} ever again. Instead, she found work as a woodcutter in {color=#f6d6bd}Gale Rocks{/color}."
                else:
                    $ custom5 = ""
            elif iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1:
                $ custom1 = "While the trade route was focused on the eastern trail, {color=#f6d6bd}Pelt of the North{/color} could slowly pursue its financial goals. After another decade, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad. The inn, taken over by the city officials, remained one of the few shelters in the dangerous North."
                if tulia_about_bandits_grateful or not tulia_about_bandits2:
                    $ custom5 = "\n\nOne of the new guards was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters. Unlike her new crew, she didn’t cross {color=#f6d6bd}Hag Hills{/color} ever again. Instead, she found work as a woodcutter in {color=#f6d6bd}Gale Rocks{/color}."
                else:
                    $ custom5 = ""
            else:
                $ custom1 = "The keeper of {color=#f6d6bd}Pelt of the North{/color} quickly forgot about the roadwarden’s visit, and needed over ten years to complete his financial goal. Finally, the hunters moved to the city, living off their savings and occasional mercenary work, forming an experienced squad. The inn, taken over by the city officials, remained one of the few shelters in the dangerous North."
                if tulia_about_bandits_grateful or not tulia_about_bandits2:
                    $ custom5 = "\n\nOne of the new guards was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters. Unlike her new crew, she didn’t cross {color=#f6d6bd}Hag Hills{/color} ever again. Instead, she found work as a woodcutter in {color=#f6d6bd}Gale Rocks{/color}."
                else:
                    $ custom5 = ""
        elif quest_explorepeninsula_result == "success3":
            if quest_explorepeninsula_mainvillage == "howlersdell" or quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks" or quest_explorepeninsula_mainvillage == "whitemarshes":
                $ custom1 = "The trade route following the western trail greatly benefited the dwellers of {color=#f6d6bd}Pelt of the North{/color}. After five more years, they moved to the city to live off their savings, but a few of them got attached to their now-safe home. They remained in the inn and started to expand it, making room for the next generation to join them."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, allowed needy travelers to rest inside free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, put the safety of her people above all else."
                else:
                    $ custom2 = ""
                if tulia_about_bandits_grateful or not tulia_about_bandits2:
                    $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                else:
                    $ custom5 = ""
            elif iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "While the trade route was focused on the eastern trail, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s journey, and finally became an obligatory stop for most traders. After five more years, they moved to the city to live off their savings, but a few of them got attached to their now-safe home. They remained in the inn and started to expand it, making room for the next generation to join them."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, allowed needy travelers to rest inside free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this new hamlet, put the safety of her people above all else."
                else:
                    $ custom2 = ""
                if dalit_firsttime:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
                else:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color} arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
            elif iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1:
                $ custom1 = "While the trade route was focused on the eastern trail, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s journey, and finally became an obligatory stop for most traders. After another five years, the hunters moved to the city, living off their savings and occasional mercenary work, forming an experienced squad. The inn, taken over by the city officials, remained one of the most reputable shelters in the peninsula."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, looked after needy travelers free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, put the safety of her squad above all else."
                else:
                    $ custom2 = ""
                if dalit_firsttime:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
                else:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color} arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
            else:
                $ custom1 = "While the trade route was focused on the eastern trail, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from its presence. After another ten years, the hunters moved to the city, living off their savings and occasional mercenary work, forming an experienced squad. The inn, taken over by the city officials, remained one of the most reputable shelters in the peninsula."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, looked after needy travelers free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, put the safety of her squad above all else."
                else:
                    $ custom2 = ""
                if dalit_firsttime:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
                else:
                    if tulia_about_bandits_grateful or not tulia_about_bandits2:
                        $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color} arrived to {color=#f6d6bd}Pelt{/color} soon after losing her squad, seeking stable work among the hunters."
                    else:
                        $ custom5 = ""
        menu:
            '[custom1][custom2][custom5]
            '
            '(continue)':
                jump epilogue_slides_howlers

    label epilogue_slides_howlers:
        if not howlersdell_firsttime:
            jump epilogue_slides_oldpagos
        $ endcredits_counter += 1
        if quest_explorepeninsula_result == "success3" and quest_explorepeninsula_mainvillage == "howlersdell":
            $ endgame_howlers_destroyed = 1
            show areapicture ep_08b at basicfade
        else:
            show areapicture ep_08a at basicfade
        if quest_explorepeninsula_result == "fail1":
            if quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities.\n\nThe tribe lacked a charismatic leader"
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = ", and, having no interest in mining the copper or returning to the fishing hamlet, didn’t grow much."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = ", and, having no interest in returning to the fishing hamlet, didn’t grow much."
                elif thais_rumor_vein:
                    $ custom2 = ", and, having no interest in mining the copper, didn’t grow much."
                else:
                    $ custom2 = ", and didn’t grow much."
                if druidcave_firsttime:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. {color=#f6d6bd}The archdruidess{/color} sought help from {color=#f6d6bd}the hermit in the cave{/color}, but the doors to his chambers were buried beneath heavy boulders. The desperate locals turned toward the altar in the swamps, feeding the tree and its offspring more lavishly than ever before."
                elif beholder_firsttime:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. The desperate locals sought help from the altar in the swamps, feeding the tree and its offspring more lavishly than ever before."
                else:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. Many believe that it’s the blood magic of the desperate locals that’s responsible for the many disappearances and kidnappings occurring in the North."
            elif quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                $ custom1 = "After asserting her dominance over the druids, {color=#f6d6bd}Thais{/color} ruled {color=#f6d6bd}Howler’s Dell{/color} with an iron fist, increasing the influence of the village guards and limiting the training of the younger druids. The villagers stayed loyal to the prayers of their ancestors, but as long as their ruler was alive, they remained in many ways close to the city customs.\n\nHaving a charismatic leader, but lacking in resources"
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems, and increased their supplies thanks to the restored fishing hamlet."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = ", the locals increased their supplies thanks to the restored fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems."
                else:
                    $ custom2 = ", the village didn’t grow much, but also didn’t face many threats."
                if druidcave_firsttime:
                    $ custom3 = " One day, the locals brought gifts to {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. From time to time, they were returning to the old altar, keeping their traditions alive."
                elif beholder_firsttime:
                    $ custom3 = " From time to time, they returned to the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color} didn’t change much, stuck in the conflict between {color=#f6d6bd}Thais{/color} and the druids. The villagers stayed loyal to the prayers of their ancestors, slowly drifting away from the city customs.\n\nHaving a charismatic leader, but lacking in resources"
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems, and increased their supplies thanks to the restored fishing hamlet."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = ", the locals increased their supplies thanks to the restored fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems."
                else:
                    $ custom2 = ", the village didn’t grow much, but also didn’t face many threats."
                if druidcave_firsttime:
                    $ custom3 = " From time to time, they sought advice from {color=#f6d6bd}the hermit in the cave{/color}, keeping their rituals at the altar alive."
                elif beholder_firsttime:
                    $ custom3 = " From time to time, they returned to the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
        elif quest_explorepeninsula_result == "success1":
            if quest_explorepeninsula_mainvillage == "howlersdell":
                $ custom1 = "Not all people in {color=#f6d6bd}Howler’s Dell{/color} were eager to accommodate the cityfolk, but no one could oppose {color=#f6d6bd}Thais{/color} and her guards, who received a juicy cut of the inflowing wealth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals soon left the other tribes behind, and many caravans had no reason to travel farther north."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. The influence of the druids began to dwindle, but they haven’t spoken their last words yet."
            elif endgame_howlersdell_leader_option or quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                    $ custom1 = "While {color=#f6d6bd}Howler’s Dell{/color} wasn’t at first considered a crucial part of the new trade route, {color=#f6d6bd}Thais’{/color} charm managed to bridge the gap between her and the council representatives - and if there were any objections, they were muffled underneath her iron fist. "
                else:
                    $ custom1 = "The people of {color=#f6d6bd}Howler’s Dell{/color} gladly became a part of the new trade route - and if there were any objections, they were muffled underneath {color=#f6d6bd}Thais’{/color} iron fist. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals could negotiate the best prices, and their standard of life rose, though for some more so than for the others."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. The influence of the druids began to dwindle, but they haven’t said their last words yet."
            elif quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They allowed the caravans to ride through the village and exchange wares, but had little interest in growth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
                else:
                    $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
                $ custom3 = "\n\nFor the most part, the gates kept the priests, bards, and drifters away, and so the next generations continued to pray to their ancestors."
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color}, torn by the conflict between {color=#f6d6bd}Thais’{/color} guards and the druids’ calls for isolation, needed some time before they joined the new trade route. They allowed the caravans to ride through the village and exchange wares, but their lives didn’t change much. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals didn’t need help from the outsiders, especially as the nearby roads were getting safer."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "However, thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "However, the copper from the new mining hamlet was used to secure their village and the roads around it."
                else:
                    $ custom2 = "Lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, but for the next few decades, their gates were closed to any priests of The Wright."
        elif quest_explorepeninsula_result == "success2":
            if quest_explorepeninsula_mainvillage == "howlersdell":
                $ custom1 = "Not all people in {color=#f6d6bd}Howler’s Dell{/color} were eager to accommodate the cityfolk, but no one could oppose {color=#f6d6bd}Thais{/color} and her guards, who received a juicy cut of the inflowing wealth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals soon left the other tribes behind, and many caravans had no reason to travel farther north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                else:
                    $ custom2 = "Despite lacking in resources, new hamlets of lumberjacks, stonecutters, and trappers were built, allowing them to cut their dependence on the other villages."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. The influence of the druids dwindled, never to recover."
            elif endgame_howlersdell_leader_option or quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                    $ custom1 = "While {color=#f6d6bd}Howler’s Dell{/color} wasn’t at first considered a crucial part of the new trade route, {color=#f6d6bd}Thais’{/color} charm managed to bridge the gap between her and the council representatives - and if there were any objections, they were muffled underneath her iron fist. "
                else:
                    $ custom1 = "The people of {color=#f6d6bd}Howler’s Dell{/color} gladly became a part of the new trade route - and if there were any objections, they were muffled underneath {color=#f6d6bd}Thais’{/color} iron fist. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals could negotiate the best prices, and their standard of life rose, though for some more so than for the others."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. The influence of the druids dwindled, never to recover."
            elif quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They allowed the caravans to ride through the village and exchange wares, but had little interest in growth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
                else:
                    $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
                $ custom3 = "\n\nFor the most part, the gates kept the priests, bards, and drifters away, and so the next generations continued to pray to their ancestors. However, as the other villages grew in power, the significance of the formerly richest village in the North dwindled."
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color}, torn by the conflict between {color=#f6d6bd}Thais’{/color} guards and the druids’ calls for isolation, needed some time before they joined the new trade route. They allowed the caravans to ride through the village and exchange wares, but their lives haven’t changed much. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals didn’t need help from the outsiders, especially as the nearby roads were getting safer."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "However, thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "However, the copper from the new mining hamlet was used to secure their village and the roads around it."
                else:
                    $ custom2 = "Lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, but for the next few decades, their gates were closed to any priests of The Wright. However, as the other villages grew in power, the significance of the formerly richest village in the North dwindled."
        elif quest_explorepeninsula_result == "success3":
            if quest_explorepeninsula_mainvillage == "howlersdell":
                $ custom1 = "Not all people in {color=#f6d6bd}Howler’s Dell{/color} were eager to accommodate the cityfolk, but no one could oppose {color=#f6d6bd}Thais{/color} and her guards, who received a juicy cut of the inflowing wealth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals soon left the other tribes behind, and many caravans had no reason to travel farther north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                    $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. Soon, the druids were banished from the village, giving way to an even more rapid expansion.\n\nToo rapid, in fact. After a few years, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                    $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. Soon, the druids were banished from the village, giving way to an even more rapid expansion.\n\nToo rapid, in fact. After a few years, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                    $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. Soon, the druids were banished from the village, giving way to an even more rapid expansion.\n\nToo rapid, in fact. After a few years, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
                else:
                    $ custom2 = "Despite lacking in resources, the new hamlets of lumberjacks, stonecutters, and trappers were built, allowing them to cut their dependence on the other villages."
                    $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. Soon, the druids were banished from the village, giving way to an even more rapid expansion.\n\nToo rapid, in fact. After a few years, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
            elif endgame_howlersdell_leader_option or quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                    $ custom1 = "While {color=#f6d6bd}Howler’s Dell{/color} wasn’t at first considered a crucial part of the new trade route, {color=#f6d6bd}Thais’{/color} charm managed to bridge the gap between her and the council representatives - and if there were any objections, they were muffled underneath her iron fist. "
                else:
                    $ custom1 = "The people of {color=#f6d6bd}Howler’s Dell{/color} gladly became a part of the new trade route - and if there were any objections, they were muffled underneath {color=#f6d6bd}Thais’{/color} iron fist. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals soon left the other tribes behind, and many caravans had no reason to travel farther north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it. Soon, new hamlets of lumberjacks, stonecutters, and trappers were built, some of them employing only the laborers from the city."
                else:
                    $ custom2 = "Despite lacking in resources, the new hamlets of lumberjacks, stonecutters, and trappers were built, allowing them to cut their dependence on the other villages."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, and as time went on, their customs changed. After the priests of The Wright arrived, {color=#f6d6bd}the mayor{/color} was among the first souls to convert. The influence of the druids dwindled, never to recover."
            elif quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They allowed the caravans to ride through the village and exchange wares, but had little interest in growth. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
                else:
                    $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
                $ custom3 = "\n\nFor the most part, the gates kept the priests, bards, and drifters away, and so the next generations continued to pray to their ancestors. However, as the other villages grew in power, the significance of the formerly richest village in the North dwindled, and after some time, the tribe lost any power over its lands, opening itself to the raids of inquisitors."
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color}, torn by the conflict between {color=#f6d6bd}Thais’{/color} guards and the druids’ calls for isolation, needed some time before they joined the new trade route. They allowed the caravans to ride through the village and exchange wares, but their lives didn’t change much. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals didn’t need help from the outsiders, especially as the nearby roads were getting safer."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "However, thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "However, the copper from the new mining hamlet was used to secure their village and the roads around it."
                else:
                    $ custom2 = "Lacking in resources, the village could never be fully free of its dependence on the other tribes."
                $ custom3 = "\n\nMore and more words of the cityfolk sunk into the speech of the locals, but for the next few decades, their gates were closed for any priests of The Wright. However, as the other villages grew in power, the significance of the formerly richest village in the North dwindled, and after some time, the tribe lost any power over its lands."
        if fishinghamlet_firsttime:
            if aegidia_about_steephouse_truth:
                $ custom5 = "\n\n{color=#f6d6bd}Aegidia{/color} never forgave the sins of her neighbors. Afraid to face her mother, she decided to leave the peninsula in spring, forming a group of adventurers who were eager to save innocent lives even without pay. While she couldn’t reverse the destruction of {color=#f6d6bd}Steep House{/color}, her noble deeds helped her spend her nights in peace."
            elif quest_ruins_choice == "thais_alliance" or quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom5 = "\n\nSoon after winter, {color=#f6d6bd}Aegidia{/color} was thrown out of the hamlet, then stripped of her possessions by the village guards and banished for good. Having only a stone dagger to defend herself, she barely reached one of the villages on the other side of {color=#f6d6bd}Hag Hills{/color}, where she was allowed to join a family of hunters. Her broken arm never held a bow again."
                else:
                    $ custom5 = "\n\n{color=#f6d6bd}Aegidia{/color} spent a few more seasons alone, practicing magic and archery, until she felt ready to return home - only to realize that her village was now fully under {color=#f6d6bd}Thais’{/color} control. She managed to reach {color=#f6d6bd}Hovlavan{/color}, then joined a group of adventurers, never staying in one place for long."
            elif quest_ruins_choice == "thais_defeated":
                $ custom5 = "\n\n{color=#f6d6bd}Aegidia{/color} spent a few more seasons alone, practicing magic and archery, until she felt ready to return home - only to realize that her village was no longer under {color=#f6d6bd}Thais’{/color} control. The druids welcomed her with open arms, and helped her master her pneuma. She soon became the youngest member of their ring."
            else:
                if quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom5 = "\n\nSoon after winter, {color=#f6d6bd}Aegidia{/color} was thrown out of the hamlet, then stripped of her possessions by the village guards and banished for good. Having only a stone dagger to defend herself, she barely reached one of the villages on the other side of {color=#f6d6bd}Hag Hills{/color}, where she was allowed to join a family of hunters. Her broken arm never held a bow again."
                else:
                    $ custom5 = "\n\n{color=#f6d6bd}Aegidia{/color} spent a few more seasons alone, practicing magic and archery, until she felt ready to return home. {color=#f6d6bd}Thais{/color} was furious at first, but the druids’ protection allowed her daughter to reclaim her position of huntress. While her life wasn’t free of conflict, she now truly belonged to her new family."
        else:
            $ custom5 = ""
        if ruinedvillage_truth:
            if quest_ruins_choice == "lefttocity":
                if quest_explorepeninsula_result == "fail1":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
                if quest_explorepeninsula_result == "success1":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, avoided by the caravans that cut a new path through the haunting clearing. It provided for a few more scavengers and gave shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
                elif quest_explorepeninsula_result == "success2":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} was quickly cleared by the passing caravans, then its ruins were destroyed for good, giving way to a secure, beaten path, surrounded by the awakening forest."
                elif quest_explorepeninsula_result == "success3":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} didn’t stay alone for long. The people of {color=#f6d6bd}Howler’s{/color} worked together with the cityfolk, turning the scattered bricks and logs into a wall to protect the trail from the beasts of the woodlands, and getting rid of any trace of the northerners’ wrongdoing."
            elif quest_ruins_choice == "thais_defeated":
                if quest_explorepeninsula_result == "fail1":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, but before it faded away, the people of {color=#f6d6bd}Howler’s Dell{/color} placed a humble, stone statue of a tree torn by lightning on the paved square. While it expressed regret, they have never avowed their authorship."
                else:
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, avoided by the caravans that cut a new path through the haunting clearing. Before it faded away, the people of {color=#f6d6bd}Howler’s Dell{/color} placed a humble, stone statue of a tree torn by lightning on the paved square. While it expressed regret, they have never avowed their authorship."
            elif quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance" or quest_ruins_choice == "thais_alliance_fail":
                if quest_explorepeninsula_result == "fail1" or quest_explorepeninsula_result == "success1":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} didn’t stay alone for long. The people of {color=#f6d6bd}Howler’s{/color} arrived with tools and torches, taking away anything of value and getting rid of any evidence of their wrongdoing. Soon, the only things left were a few loose bricks and the paved square, surrounded by the awakening forest."
                else:
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} didn’t stay alone for long. The people of {color=#f6d6bd}Howler’s{/color} worked together with the cityfolk, turning the scattered bricks and logs into a wall to protect the trail from the beasts of the woodlands, and getting rid of any trace of the northerners’ wrongdoing."
            else: # quest_ruins_choice == "forgotten"
                if quest_explorepeninsula_result == "fail1":
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
                else:
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, avoided by the caravans that cut a new path through the haunting clearing. It provided for a few more scavengers and gave shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
        else:
            $ custom6 = ""
        menu:
            '[custom1][custom2][custom3][custom5][custom6]
            '
            '(continue)':
                jump epilogue_slides_oldpagos

    label epilogue_slides_oldpagos:
        if not oldpagos_firsttime:
            jump epilogue_slides_monastery
        $ endcredits_counter += 1
        if not oldpagos_cured:
            show areapicture ep_09a at basicfade
            if oldpagos_plague_helpfromgalerocks:
                $ custom1 = "More than half of the tribe of {color=#f6d6bd}Old Págos{/color} lost their lives to the plague, including many children, and it would be even worse if it weren’t for the help brought by their friends from {color=#f6d6bd}Gale Rocks{/color}. "
            else:
                $ custom1 = "More than three-fourths of the tribe of {color=#f6d6bd}Old Págos{/color} lost their lives to the plague, including all of the children. "
            if quest_explorepeninsula_result == "fail1":
                $ custom2 = "The next spring, the first few families left the peninsula for good, and in just two years there were but four elders left inside the proud, tall walls.\n\nIt took decades before the scavengers dared to climb the “haunted” hill, but by that point, the place was overrun by monsters."
            elif quest_explorepeninsula_result == "success1":
                $ custom2 = "The next spring, the first few families left the peninsula for good, and in just two years there were but four elders left inside the proud, tall walls.\n\nIt took decades before new settlers dared to climb the “haunted” hill, but by that point, the place was overrun by monsters."
            elif quest_explorepeninsula_result == "success2":
                $ custom2 = "The next spring, the first few families left the peninsula for good, and in just two years there were but four elders left.\n\nA decade later, a new stone cutting hamlet was built in the shadow of the hill. Every night, the settlers heard haunting roars coming from behind the tall, proud walls."
            elif quest_explorepeninsula_result == "success3":
                $ custom2 = "The next spring, the first few families left the peninsula for good, and in just two years there were but four elders left.\n\nA decade later, the soldiers raided the walls, clearing the village of beasts and preparing the area for the next generation of settlers - but by that point, its past name was believed to be cursed."
            menu:
                '[custom1][custom2]
                '
                '(continue)':
                    jump epilogue_slides_monastery
        else:
            if oldpagos_plague_helpfromgalerocks:
                $ custom1 = "The tribe of {color=#f6d6bd}Old Págos{/color} lost many lives to the plague, but the supplies brought to them by their friends from {color=#f6d6bd}Gale Rocks{/color} helped them overcome the harsh winter. "
            else:
                $ custom1 = "The tribe of {color=#f6d6bd}Old Págos{/color} lost many lives to the plague, and even more so to the harsh winter, but the village survived, as united as ever. "
            if quest_explorepeninsula_result == "fail1":
                show areapicture ep_09a at basicfade
                $ custom2 = "Having hardly any caravans to trade with, the locals focused on farming and goat breeding, but the years to follow were lean, and with every generation more families left their homes to seek luck on the other side of {color=#f6d6bd}Hag Hills{/color}."
                if aeli_about_copper:
                    $ custom3 = "\n\n{color=#f6d6bd}Aeli{/color}, aware of the village’s poor state, kept the secret of the copper vein to his order."
                else:
                    $ custom3 = ""
                $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color}, torn by the plague, was among the first souls to leave. She finished her duty in the distant south, buried by a sandstorm in the lands of her ancestors, where she protected those spreading Wright’s teachings."
                if westgate_firsttime:
                    if quintus_left_gate:
                        $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next few years were full of brave hunts and drinking, until he mixed the two a bit too much."
                    else:
                        $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                else:
                    $ custom5 = ""
            elif quest_explorepeninsula_result == "success1":
                $ custom3 = ""
                if not aeli_about_copper:
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        show areapicture ep_09b at basicfade
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, they were sure, would come sooner rather than later."
                    elif endgame_oldpagos_leader_option:
                        show areapicture ep_09b at basicfade
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, indeed, came rather quickly."
                    else:
                        show areapicture ep_09a at basicfade
                        $ custom2 = "The slowly awakening trade route allowed them to return to working with stone, but the rare coins and supplies always left them just on the verge of making ends meet, and the villagers faced many more lean years. With every generation, more families left their homes to seek luck on the other side of {color=#f6d6bd}Hag Hills{/color}."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color}, torn by the plague, started a long journey. She finished her duty in the distant south, buried by a sandstorm in the lands of her ancestors, where she protected those spreading Wright’s teachings."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next few years were full of brave hunts and drinking, until he mixed the two a bit too much."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
                else:
                    show areapicture ep_09b at basicfade
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city. The tribe kept their savings for the darker days, but many years would pass before they felt hunger again."
                    elif endgame_oldpagos_leader_option:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, they were sure, would come sooner rather than later."
                    else:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, indeed, came rather quickly."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, wounded by a werebadger, she became a combat instructor."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next ten years were full of brave hunts and drinking, until he mixed the two a bit too much."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
            elif quest_explorepeninsula_result == "success2":
                show areapicture ep_09b at basicfade
                $ custom3 = ""
                if not aeli_about_copper:
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city. The tribe kept their savings for the darker days, but many years would pass before they felt hunger again."
                    elif endgame_oldpagos_leader_option:
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, they were sure, would come sooner rather than later."
                    else:
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, indeed, came rather quickly."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, wounded by a werebadger, she became a combat instructor."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
                else:
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city, and then traveled to distant provinces, unaware of the centuries they were about to witness.\n\nThe tribe kept their savings for the darker days, but they were always happy to open the gates for bards and actors, especially those portraying the grand deeds of heroes from Wright’s Tablets. After some time, another play, based on the stories of the tribe, was performed in {color=#f6d6bd}Hovlavan{/color} - {i}The Roadwarden Who Cured The Plague{/i}."
                    elif endgame_oldpagos_leader_option:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city. The tribe kept their savings for the darker days, but many years would pass before they felt hunger again."
                    else:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, they were sure, would come sooner rather than later."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, humbled by the selfless help she received during her struggles, she joined the monks on the mountain, guarding them from flying beasts and escorting them on their journeys to other monasteries."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
            elif quest_explorepeninsula_result == "success3":
                show areapicture ep_09b at basicfade
                $ custom3 = ""
                if not aeli_about_copper:
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city, and then traveled to distant provinces, unaware of the centuries they were about to witness.\n\nThe tribe kept their savings for the darker days, but they were always happy to open the gates for bards and actors, especially those portraying the grand deeds of heroes from Wright’s Tablets. After some time, another play, based on the stories of the tribe, was performed in {color=#f6d6bd}Hovlavan{/color} - {i}The Roadwarden Who Cured The Plague{/i}."
                    elif endgame_oldpagos_leader_option:
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city. The tribe kept their savings for the darker days, but many years would pass before they felt hunger again."
                    else:
                        $ custom2 = "Thanks to the revitalized trade route, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. The tribe kept their savings for the darker days, which, they were sure, would come sooner rather than later."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, humbled by the selfless help she received during her struggles, she joined the monks on the mountain, guarding them from flying beasts and escorting them on their journeys to other monasteries."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
                else:
                    if quest_explorepeninsula_mainvillage == "oldpagos" or quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city, and then traveled to distant provinces, unaware of the centuries they were about to witness.\n\nThe tribe kept their savings for the darker days, but they were always happy to open the gates for bards and actors, especially those portraying the grand deeds of heroes from Wright’s Tablets. After some time, another play, based on the stories of the tribe, was performed in {color=#f6d6bd}Hovlavan{/color} - {i}The Roadwarden Who Cured The Plague{/i}."
                    elif endgame_oldpagos_leader_option:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city, and then traveled to distant provinces, unaware of the centuries they were about to witness.\n\nThe tribe kept their savings for the darker days, but they were always happy to open the gates for bards and actors, especially those portraying the grand deeds of heroes from Wright’s Tablets. After some time, another play, based on the stories of the tribe, was performed in {color=#f6d6bd}Hovlavan{/color} - {i}The Roadwarden Who Cured The Plague{/i}."
                    else:
                        $ custom2 = "Thanks to the revitalized trade route and the earnings from their new copper mine built by the eastern road, the locals returned to their craft, providing an essential material to the now-growing security of the northern roads and settlements. Their famous statues soon reached the houses in the city. The tribe kept their savings for the darker days, but many years would pass before they felt hunger again."
                    $ custom4 = "\n\nAfter a few years of patrolling the roads, {color=#f6d6bd}Tertia{/color} realized that, despite the nightmares she had seen, the lives led by her friends and relatives were good, safe, and comfortable. Finally, she accepted a seat at the village council, ready to face the responsibilities of a leader until the end of her long life."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
            menu:
                '[custom1][custom2][custom3][custom4][custom5]
                '
                '(continue)':
                    jump epilogue_slides_monastery

    label epilogue_slides_monastery:
        if not monastery_firsttime:
            jump epilogue_slides_whitemarshes
        $ endcredits_counter += 1
        $ custom1 = ""
        if quest_explorepeninsula_result == "fail1":
            show areapicture ep_10a at basicfade
            $ custom1 = "{color=#f6d6bd}The monastery{/color}, left to itself, lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it was hollow inside."
        else:
            if not oldpagos_cured:
                if not quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                    show areapicture ep_10a at basicfade
                    $ custom1 = "Having no supplies and acolytes from {color=#f6d6bd}Old Págos{/color}, {color=#f6d6bd}the monastery{/color} lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it was hollow inside."
                elif quest_explorepeninsula_result == "success1":
                    show areapicture ep_10a at basicfade
                    $ custom1 = "Forced to accept the support of {color=#f6d6bd}Hovlavan{/color}, the monks completed {color=#f6d6bd}The Library in Stone{/color} during the following century. While it was indeed visited by a few groups of pilgrims, the monks’ poor planning and distrust toward the city architects led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                else:
                    show areapicture ep_10b at basicfade
                    $ custom1 = "Forced to accept the support of {color=#f6d6bd}Hovlavan{/color}, the monks completed {color=#f6d6bd}The Library in Stone{/color} during the following century. After the city artisans strengthened the support of the walls and ceiling in the hollowed mountain, the monastery survived even the tremendous earthquake that soon tore The Dragonwoods in half.\n\nThe monastery became the pearl of the province, luring thousands of pilgrims, but also thieves, seeking fabled treasures hidden among the tunnels."
            else:
                if quest_explorepeninsula_result == "success1":
                    show areapicture ep_10a at basicfade
                    if quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom1 = "With the support of {color=#f6d6bd}Hovlavan{/color}, the monks almost completed {color=#f6d6bd}The Library in Stone{/color} during the following century. However, their poor planning and distrust toward the city architects led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                    elif quest_explorepeninsula_mainvillage == "oldpagos" or endgame_oldpagos_leader_option:
                        if monastery_cave_firsttime:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies almost allowed them to finish the work on {color=#f6d6bd}The Library in Stone{/color}. However, their poor planning led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                        else:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies helped them sustain their work for a century. However, after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                    else:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color}, left to itself, lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it was hollow inside."
                elif quest_explorepeninsula_result == "success2":
                    show areapicture ep_10a at basicfade
                    if quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        $ custom1 = "With the support of {color=#f6d6bd}Hovlavan{/color}, the monks completed {color=#f6d6bd}The Library in Stone{/color} during the following century. While it was indeed visited by a few groups of pilgrims, the monks’ poor planning and distrust toward the city architects led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                    elif quest_explorepeninsula_mainvillage == "oldpagos" or endgame_oldpagos_leader_option:
                        if monastery_cave_firsttime:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies almost allowed them to finish the work on {color=#f6d6bd}The Library in Stone{/color}. However, their poor planning led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                        else:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies helped them sustain their work for a century. However, after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                    else:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color}, left to itself, lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it was hollow inside."
                elif quest_explorepeninsula_result == "success3":
                    if quest_explorepeninsula_mainvillage == "oldpagosandmonks":
                        show areapicture ep_10b at basicfade
                        $ endgame_monastery_survived = 1
                        $ custom1 = "With the support of {color=#f6d6bd}Hovlavan{/color}, the monks completed {color=#f6d6bd}The Library in Stone{/color} during the following century. After the city artisans strengthened the support of the walls and ceiling in the hollowed mountain, the monastery survived even the tremendous earthquake that soon tore The Dragonwoods in half.\n\nThe monastery became the pearl of the province, luring thousands of pilgrims, but also thieves, seeking fabled treasures hidden among the tunnels."
                    elif quest_explorepeninsula_mainvillage == "oldpagos" or endgame_oldpagos_leader_option:
                        show areapicture ep_10a at basicfade
                        if monastery_cave_firsttime:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies almost allowed them to finish the work on {color=#f6d6bd}The Library in Stone{/color}. However, their poor planning led to a disaster - after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                        else:
                            $ custom1 = "While {color=#f6d6bd}Hovlavan{/color} wasn’t eager to directly support the monks, the easier access to supplies helped them sustain their work for a century. However, after a violent earthquake, the mountain collapsed under its own weight, burying many souls alive."
                    else:
                        show areapicture ep_10a at basicfade
                        $ custom1 = "{color=#f6d6bd}The monastery{/color}, left to itself, lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it was hollow inside."
        menu:
            '[custom1]
            '
            '(continue)':
                jump epilogue_slides_whitemarshes

    label epilogue_slides_whitemarshes:
        if not whitemarshes_firsttime:
            if quest_explorepeninsula_result == "success3":
                jump epilogue_slides_foggy
            elif quest_explorepeninsula_result == "success2":
                $ endgame_foggy_destroyed = 1
                jump epilogue_slides_foggy
            else:
                $ endgame_creeks_destroyed = 1
                $ endgame_foggy_destroyed = 1
                jump epilogue_slides_foggy
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        if whitemarshes_destroyed:
            show areapicture ep_11a at basicfade
            if quest_explorepeninsula_result == "fail1":
                $ endgame_creeks_destroyed = 1
                $ endgame_foggy_destroyed = 1
                $ custom1 = "{color=#f6d6bd}White Marshes{/color} became the largest fortress of the undead in the North. After years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades. "
            elif quest_explorepeninsula_result == "success1":
                $ endgame_creeks_destroyed = 1
                $ endgame_foggy_destroyed = 1
                $ custom1 = "{color=#f6d6bd}White Marshes{/color} became the largest fortress of the undead in the North. After years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes and caravans, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
            elif quest_explorepeninsula_result == "success2":
                $ endgame_foggy_destroyed = 1
                $ custom1 = "{color=#f6d6bd}White Marshes{/color} became the largest fortress of the undead in the North. After years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a short campaign against the tribes and caravans, feeding on their blood, but, facing the fierce opposition of {color=#f6d6bd}Hovlavan{/color} soldiers, it was pushed into {color=#f6d6bd}Hag Hills{/color}, forced to wait for the fogs to come."
            elif quest_explorepeninsula_result == "success3":
                $ custom1 = "{color=#f6d6bd}White Marshes{/color} became the largest fortress of the undead in the North. After years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a short campaign against the tribes and caravans, but, facing the fierce opposition of {color=#f6d6bd}Hovlavan{/color} soldiers and the heroic adventurers, it was stopped before it could feed on their blood."
        elif not whitemarshes_nomoreundead:
            if whitemarshes_attacked:
                show areapicture ep_11b at basicfade
                if quest_explorepeninsula_result == "fail1":
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades. "
                elif quest_explorepeninsula_result == "success1":
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes and caravans, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
                elif quest_explorepeninsula_result == "success2":
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a short campaign against the tribes and caravans, feeding on their blood, but, facing the fierce opposition of {color=#f6d6bd}Hovlavan{/color} soldiers, it was pushed into {color=#f6d6bd}Hag Hills{/color}, forced to wait for the fogs to come."
                elif quest_explorepeninsula_result == "success3":
                    $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a short campaign against the tribes and caravans, but, facing the fierce opposition of {color=#f6d6bd}Hovlavan{/color} soldiers and the heroic adventurers, it was stopped before it could feed on their blood."
            else:
                if quest_explorepeninsula_result == "fail1":
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    show areapicture ep_11a at basicfade
                    $ custom1 = "{color=#f6d6bd}White Marshes{/color}, left to itself, collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades. "
                elif quest_explorepeninsula_result == "success1":
                    show areapicture ep_11b at basicfade
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "{color=#f6d6bd}White Marshes{/color}, facing growing pressure from the soldiers and inquisitors, buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes and caravans, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
                elif quest_explorepeninsula_result == "success2":
                    show areapicture ep_11b at basicfade
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "{color=#f6d6bd}White Marshes{/color}, facing growing pressure from the soldiers and inquisitors, buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a short campaign against the tribes and caravans, feeding on their blood, but, facing the fierce opposition of {color=#f6d6bd}Hovlavan{/color} soldiers, it was pushed into {color=#f6d6bd}Hag Hills{/color}, forced to wait for the fogs to come."
                elif quest_explorepeninsula_result == "success3":
                    show areapicture ep_11d at basicfade
                    $ custom1 = "Soon after {color=#f6d6bd}White Marshes{/color} refused to yield before the inquisitors, it was attacked by the city soldiers, and forced into submission. {color=#f6d6bd}Orentius’{/color} loyalists faced either banishment or execution, but the remaining families were allowed to stay in the now-occupied village, regressing into a hamlet, reliant on the supplies coming from the outside as they farmed peat for the use of the wealthy."
        elif whitemarshes_attacked:
            show areapicture ep_11b at basicfade
            $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. It took decades before it was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals roaming not only the northern lands, but also the woods south of {color=#f6d6bd}Hag Hills{/color}."
        else:
            if thyrsus_about_thyrsusgift_druidcomment:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} upheld his longing for family for another year until, without alerting anyone, he left to see the hermit in the southern caves, and stayed with him for another few seasons. Fighting shame and resentment, he finally found peace in letting go of his past, and found himself a new home in the distant wetlands of the south, where he was valued for his impressive talents - and where his quirks were seen as harmless."
            elif quest_thyrsusgift == 2:
                if thyrsus_highisland_joined:
                    $ custom2 = "\n\nAfter getting a taste of adventure on {color=#f6d6bd}High Island{/color}, {color=#f6d6bd}Thyrsus{/color} stopped waiting for his family’s acceptance. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he moved to another province, working as a guard for travelers and merchants traveling through its dark wetlands."
                else:
                    $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} kept looking for his family’s acceptance for another two years, but then his longing started to turn into resentment, and he left without saying his goodbyes. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he tried his luck as a herbalist, but was never able to carve himself a place where he would feel at home."
            elif thyrsus_highisland_joined:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} remained at the peatfield for another two years, but then abandoned his home without saying any goodbyes, inspired by the taste of adventure from {color=#f6d6bd}High Island{/color}. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he moved to another province, working as a guard for travelers and merchants traveling through its dark wetlands."
            else:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} stayed with his people, but his past dissent was never forgiven. He spent more and more time exploring the bogs, seeking something that would earn the acceptance of his family. Despite all the preparations he took to protect himself from the beasts, he died with his own stew in his mouth, poisoned by a wrongly picked mushroom."
            if orentius_convinced:
                if quest_explorepeninsula_result == "fail1":
                    show areapicture ep_11c at basicfade
                    $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were growing desperate, hungry and threatened by beasts. Led by {color=#f6d6bd}Helvius{/color}, the tribe stopped looking after the routes that connected it with the rest of the peninsula.\n\nIt took decades before this place was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
                elif quest_explorepeninsula_result == "success1":
                    show areapicture ep_11d at basicfade
                    if quest_explorepeninsula_mainvillage == "whitemarshes" or endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were locked in stagnation, trading sparingly with the cityfolk, but struggling under {color=#f6d6bd}Helvius’{/color} short-sighted leadership."
                    else:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were growing desperate, hungry and threatened by beasts. Led by {color=#f6d6bd}Helvius{/color}, the tribe stopped looking after the routes that connected it with the rest of the peninsula.\n\nIt took decades before this place was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
                elif quest_explorepeninsula_result == "success2":
                    show areapicture ep_11d at basicfade
                    if quest_explorepeninsula_mainvillage == "whitemarshes":
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were steadily growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil.\n\n{color=#f6d6bd}Helvius’{/color} short-sighted leadership hindered the {color=#f6d6bd}Hovlavan{/color} investments, but his tribe left behind the lean years once he grew too weak to uphold his position."
                    elif endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were steadily growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil. However, {color=#f6d6bd}Helvius’{/color} short-sighted leadership hindered the {color=#f6d6bd}Hovlavan{/color} investments, and his tribe struggled long after his death."
                    else:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were locked in stagnation, trading sparingly with the cityfolk, but struggling under {color=#f6d6bd}Helvius’{/color} short-sighted leadership."
                elif quest_explorepeninsula_result == "success3":
                    show areapicture ep_11d at basicfade
                    if quest_explorepeninsula_mainvillage == "whitemarshes":
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil.\n\nAfter {color=#f6d6bd}Helvius’{/color} short-sighted leadership hindered the {color=#f6d6bd}Hovlavan{/color} woodcutting investment, his tribe took away his power, pushing him back into hard labor, and giving an opportunity to a more moderate artisan."
                    elif endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil.\n\n{color=#f6d6bd}Helvius’{/color} short-sighted leadership hindered the {color=#f6d6bd}Hovlavan{/color} investments, but his tribe left behind the lean years once he grew too weak to uphold his position."
                    else:
                        $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were locked in stagnation, trading sparingly with the cityfolk, but struggling under {color=#f6d6bd}Helvius’{/color} short-sighted leadership."
            elif orentius_banished:
                if quest_explorepeninsula_result == "fail1":
                    show areapicture ep_11c at basicfade
                    $ custom1 = "Led by {color=#f6d6bd}Helvius{/color}, {color=#f6d6bd}White Marshes{/color} stopped looking after the routes that connected it with the rest of the peninsula. It took decades before it was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
                elif quest_explorepeninsula_result == "success1":
                    if quest_explorepeninsula_mainvillage == "whitemarshes" or endgame_whitemarshes_leader_option:
                        show areapicture ep_11d at basicfade
                        $ custom1 = "{color=#f6d6bd}White Marshes{/color} kept following the short-sighted leadership of {color=#f6d6bd}Helvius{/color}. While at first he opposed the influence of the cityfolk, the {color=#f6d6bd}Hovlavan{/color} spies quickly uncovered the growing grudge of his tribe. After a few seasons, the sparked rebellion replaced the violent mayor with a priest of The United Church and her loyal garrison of soldiers.\n\nSoon, the locals were completely dependent on peat harvesting, locked in stagnation for many decades."
                    else:
                        show areapicture ep_11b at basicfade
                        $ custom1 = "Led by {color=#f6d6bd}Helvius{/color}, {color=#f6d6bd}White Marshes{/color} stopped looking after the routes that connected it with the rest of the peninsula. It took decades before it was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
                elif quest_explorepeninsula_result == "success2":
                    show areapicture ep_11d at basicfade
                    if quest_explorepeninsula_mainvillage == "whitemarshes" or endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}White Marshes{/color} kept following the short-sighted leadership of {color=#f6d6bd}Helvius{/color}. While at first he opposed the influence of the cityfolk, the {color=#f6d6bd}Hovlavan{/color} spies quickly uncovered the growing grudge of his tribe. After a few seasons, the sparked rebellion replaced the violent mayor with a priest of The United Church and her loyal garrison of soldiers.\n\nSoon, the locals were steadily growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil."
                    else:
                        $ custom1 = "{color=#f6d6bd}White Marshes{/color} kept following the short-sighted leadership of {color=#f6d6bd}Helvius{/color}. While at first he opposed the influence of the cityfolk, the {color=#f6d6bd}Hovlavan{/color} spies quickly uncovered the growing grudge of his tribe. After a few seasons, the sparked rebellion replaced the violent mayor with a priest of The United Church and her loyal garrison of soldiers.\n\nSoon, the locals were completely dependent on peat harvesting, locked in stagnation for many decades."
                elif quest_explorepeninsula_result == "success3":
                    show areapicture ep_11d at basicfade
                    if quest_explorepeninsula_mainvillage == "whitemarshes" or endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}White Marshes{/color} kept following the short-sighted leadership of {color=#f6d6bd}Helvius{/color}. While at first he opposed the influence of the cityfolk, the {color=#f6d6bd}Hovlavan{/color} spies quickly uncovered the growing grudge of his tribe. After a few seasons, the sparked rebellion replaced the violent mayor with a priest of The United Church and her loyal garrison of soldiers.\n\nSoon, the locals were growing in comfort, not only trading with the cityfolk, but also offering their services as guards to the caravans and travelers, gaining more from such journeys than they ever would from their unusual soil."
                    elif endgame_whitemarshes_leader_option:
                        $ custom1 = "{color=#f6d6bd}White Marshes{/color} kept following the short-sighted leadership of {color=#f6d6bd}Helvius{/color}. While at first he opposed the influence of the cityfolk, the {color=#f6d6bd}Hovlavan{/color} spies quickly uncovered the growing grudge of his tribe. After a few seasons, the sparked rebellion replaced the violent mayor with a priest of The United Church and her loyal garrison of soldiers.\n\nSoon, the locals were completely dependent on peat harvesting, locked in stagnation for many decades."
        menu:
            '[custom1][custom2]
            '
            '(continue)':
                jump epilogue_slides_foggy

    label epilogue_slides_foggy:
        $ custom1 = ""
        $ custom2 = ""
        if not foggylake_firsttime:
            jump epilogue_slides_creeks
        elif endgame_foggy_destroyed:
            $ endcredits_counter += 1
            show areapicture ep_12a at basicfade
            menu:
                'The poorly guarded {color=#f6d6bd}Foggy Lake{/color} was among the first places taken over by the wave of the undead coming from {color=#f6d6bd}White Marshes{/color}. The fire that occurred during the break-in consumed the entire hamlet.
                '
                '(continue)':
                    jump epilogue_slides_creeks
        else:
            $ endcredits_counter += 1
            if quest_explorepeninsula_result == "fail1":
                show areapicture ep_12a at basicfade
                $ custom1 = "After years of accommodating caravans and travelers, {color=#f6d6bd}Foggy{/color} had to admit that the peninsula wasn’t going to flourish. She let the building stand, just in case any of the fishers from {color=#f6d6bd}Creeks{/color} wanted to use it, then spent a few more seasons with her tribe, helping them as a cook."
                if foragers_firsttime:
                    if foragers_about_gatherthecrew_tzvi_recruited and quest_birdhunting_description05:
                        $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color}, on the other hand, was accepted among the hunters, learning the craft back home."
                    elif foragers_about_gatherthecrew_tzvi_recruited:
                        $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} left the tavern together with {color=#f6d6bd}Ilan{/color}, only to get mauled to death by a pack of spotted wolves."
                    elif quest_birdhunting_description05:
                        $ custom2 = "\n\n{color=#f6d6bd}Ilan{/color} and, to a lesser extent, {color=#f6d6bd}Tzvi{/color}, were welcomed among the hunters, and were allowed to learn their craft."
            else:
                if foragers_firsttime and not quest_foggy2iason_description03:
                    if foragers_about_gatherthecrew_tzvi_recruited and quest_birdhunting_description05:
                        if quest_explorepeninsula_result == "success3":
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coins by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color}, on the other hand, learned a few things from the hunters, and worked as the inn’s head trapper till the end of his days."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color}, on the other hand, learned a few things from the hunters, and worked as the inn’s head trapper till the end of his days."
                    elif foragers_about_gatherthecrew_tzvi_recruited:
                        if quest_explorepeninsula_result == "success3":
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coins by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color} kept to his mother, aiding her in various tasks."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color} kept to his mother, aiding her in various tasks."
                    elif quest_birdhunting_description05:
                        $ custom2 = "\n\n{color=#f6d6bd}Ilan{/color} and, to a lesser extent, {color=#f6d6bd}Tzvi{/color}, were welcomed among the hunters, and after learning a few things from them, worked as the inn’s trappers till the end of their days."
                elif foragers_firsttime:
                    if foragers_about_gatherthecrew_tzvi_recruited and quest_birdhunting_description05:
                        if quest_explorepeninsula_result == "success3":
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coins by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color}, on the other hand, was accepted among the hunters, learning the craft back home."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color}, on the other hand, was accepted among the hunters, learning the craft back home."
                    elif foragers_about_gatherthecrew_tzvi_recruited:
                        if quest_explorepeninsula_result == "success3":
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coins by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color} kept to his mother, aiding her in various tasks."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color} kept to his mother, aiding her in various tasks."
                    elif quest_birdhunting_description05:
                        $ custom2 = "\n\n{color=#f6d6bd}Ilan{/color} and, in a lesser amount, {color=#f6d6bd}Tzvi{/color}, were welcomed among the hunters, and were allowed to learn their craft."
                if quest_explorepeninsula_result == "success1":
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "The sparse caravans made all the difference to {color=#f6d6bd}Foggy{/color}, who used the dragon bones to pay for the supplies and help that were needed to build a proper wall, then the first new buildings of her growing hamlet. While the exhausting combination of running the shelter and building new structures finally stopped her aging heart, she spent the last decade of her life being louder than ever, filled with goals and ambition.\n\nThe {color=#f6d6bd}Foggy Lake{/color} tavern, now seen as a safe shelter in the North, stands to this day, run by a newcomer from {color=#f6d6bd}Hovlavan{/color}."
                    elif not quest_foggy2iason_description03:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "The sparse caravans made all the difference to {color=#f6d6bd}Foggy{/color}. At first she hesitated, remembering her deal with {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color}, but finally she used the dragon bones to pay for the supplies and help that were needed to build a proper wall. While the exhausting combination of running the shelter and building new structures finally stopped her aging heart, she spent the last few years of her life being louder than ever, filled with goals and ambition.\n\nThe {color=#f6d6bd}Foggy Lake{/color} tavern stands to this day, run by a newcomer from {color=#f6d6bd}Hovlavan{/color}."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made {color=#f6d6bd}Foggy{/color} hesitant, and unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner”. After a few years, she sold the place to the merchants of {color=#f6d6bd}Hovlavan{/color}, then, feeling old, betrayed, and naive, she returned to {color=#f6d6bd}Creeks{/color}, aiding her tribe as a cook."
                elif quest_explorepeninsula_result == "success2":
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "The caravans made all the difference to {color=#f6d6bd}Foggy{/color}, who used the dragon bones to pay for the supplies and help that were needed to build a proper wall, then the first new buildings of her growing hamlet. While the exhausting combination of running the shelter and building new structures finally stopped her aging heart, she spent the last two decades of her life being louder than ever, filled with goals and ambition.\n\nThe place known as {color=#f6d6bd}Foggy’s Inn{/color} stands to this day on the bank of {color=#f6d6bd}Foggy Lake{/color}, run by the tribe of {color=#f6d6bd}Creeks{/color}."
                    elif not quest_foggy2iason_description03:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "The caravans made all the difference to {color=#f6d6bd}Foggy{/color}. At first she hesitated, remembering her deal with {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color}, but finally she used the dragon bones to pay for the supplies and help that were needed to build a proper wall, then the first new buildings of her growing hamlet. While the exhausting combination of running the shelter and building new structures finally stopped her aging heart, she spent the last decade of her life being louder than ever, filled with goals and ambition.\n\nThe {color=#f6d6bd}Foggy Lake{/color} tavern, now seen as a safe shelter in the North, stands to this day, run by a newcomer from {color=#f6d6bd}Hovlavan{/color}."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made {color=#f6d6bd}Foggy{/color} hesitant, and unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner”. After a few years, she sold the place to the merchants of {color=#f6d6bd}Hovlavan{/color}, then, feeling old, betrayed, and naive, she returned to {color=#f6d6bd}Creeks{/color}, aiding her tribe as a cook."
                elif quest_explorepeninsula_result == "success3":
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "The numerous caravans made all the difference to {color=#f6d6bd}Foggy{/color}, who used the dragon bones to pay for the supplies and help that were needed to build a proper wall, then the first new buildings of her growing hamlet. The wealth of trade helped her stick to tavernkeeping, and she spent the last three decades of her life gently aging, but being louder than ever, filled with goals and ambition.\n\nThe place known as {color=#f6d6bd}Foggy’s Home{/color} stands to this day on the bank of {color=#f6d6bd}Foggy Lake{/color}, run by the tribe of {color=#f6d6bd}Creeks{/color}, though many believe it may soon become its own village."
                    elif not quest_foggy2iason_description03:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "The numerous caravans made all the difference to {color=#f6d6bd}Foggy{/color}. At first she hesitated, remembering her deal with {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color}, but finally she used the dragon bones to pay for the supplies and help that were needed to build a proper wall, then the first new buildings of her growing hamlet. While the exhausting combination of running the shelter and building new structures finally stopped her aging heart, she spent the last two decades of her life being louder than ever, filled with goals and ambition.\n\nThe place known as {color=#f6d6bd}Foggy’s Inn{/color} stands to this day on the bank of {color=#f6d6bd}Foggy Lake{/color}, run by the tribe of {color=#f6d6bd}Creeks{/color}."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made {color=#f6d6bd}Foggy{/color} hesitant, and unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner”. After a few years, she sold the place to the merchants of {color=#f6d6bd}Hovlavan{/color}, then, feeling old, betrayed, and naive, she returned to {color=#f6d6bd}Creeks{/color}, aiding her tribe as a cook."
            menu:
                '[custom1][custom2]
                '
                '(continue)':
                    jump epilogue_slides_creeks

    label epilogue_slides_creeks:
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        if not creeks_firsttime:
            jump epilogue_slides_galerocks
        elif endgame_creeks_destroyed:
            $ endcredits_counter += 1
            if endgame_newlife_selected == "creeks":
                $ endgame_epilogue_fluff = "spent a few seasons with the people of {color=#f6d6bd}Creeks{/color}, sharing with them colorful memories before the arrival of the skeleton mage."
            show areapicture ep_13a at basicfade
            menu:
                '{color=#f6d6bd}Creeks{/color} couldn’t withstand the undead wave. Of the tribesfolk who sought help in the woods, only a small group of woodcutters survived and found shelter among the fishers of {color=#f6d6bd}Gale Rocks{/color}. The other locals soon joined the forces of the skeleton mage.
                '
                '(continue)':
                    jump epilogue_slides_galerocks
        else:
            $ endcredits_counter += 1
            if quest_explorepeninsula_result == "fail1":
                show areapicture ep_13a at basicfade
                if quest_easternpath == 2:
                    $ custom1 = "The children seen by the roadwarden during their visit in {color=#f6d6bd}Creeks{/color} turned out to be the village’s last generation. The inexperienced leaders couldn’t fix the lack of supplies, and the people grew desperate. The tribe took the chance and left the peninsula, seeking an abandoned hamlet or village beyond {color=#f6d6bd}Hag Hills{/color} - and while not all of them reached the new settlement alive, the family was able to start anew."
                else:
                    if endgame_newlife_selected == "creeks":
                        $ endgame_epilogue_fluff = "spent a few seasons with the people of {color=#f6d6bd}Creeks{/color}, sharing with them colorful memories before the arrival of the vengeful beasts."
                    $ custom1 = "The children seen by the roadwarden during their visit in {color=#f6d6bd}Creeks{/color} turned out to be the village’s last generation. The dangerous paths, shrinking supplies, and the scant experience of the village leaders led to hunger, then desperation. The hastily exploited woods sparked the wrath of the herds, and most of the tribesfolk died during the stampede."
                    $ custom3 = "\n\nOne of the few survivors was a local hunter, {color=#f6d6bd}Efren{/color}, who at the time happened to be placing traps by the pond. Devastated by grief, he left the peninsula and joined a group of adventurers who, like him, were seeking vengeance on the cruel spirits of nature."
            else:
                show areapicture ep_13b at basicfade
                if quest_easternpath == 2:
                    $ custom2 = "\n\n{color=#f6d6bd}Elah{/color} quickly realized that keeping the roads safe was a much better way to earn dragon bones than selling his crooked chairs and tables. While he wasn’t a fighter, he often joined the merchants traveling the peninsula, exchanging news and suggesting new investments. In the meantime, he was gladly engraving the shapes of animals on cups and plates."
                else:
                    $ custom2 = "\n\n{color=#f6d6bd}Elah’s{/color} experimentation with furniture making bore fruit only after many years, and never reached the greatness of the city-learned artisans. While his efforts didn’t bring much wealth to the village, his determination turned out to be a priceless feat for the first mayor of his tribe. And no one could dispute that the local huts, while humble, were of great beauty."
                if (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2) or (quest_missinghunters_admonfound == 2 and quest_missinghunters_vaschelfound == 2) or (quest_missinghunters_vaschelfound == 2 and quest_missinghunters_daliafound == 2):
                    $ custom3 = "\n\n{color=#f6d6bd}Efren{/color}, shaken by what happened to his friends, spent a few years traveling with caravans, and learning from other tribes about more efficient, disciplined ways of organizing hunts and foraging trips. While it wasn’t easy for him to influence his family, his efforts saved many lives of the younger generations."
                else:
                    $ custom3 = "\n\nWith the passage of time, {color=#f6d6bd}Efren{/color} saw many more deaths among his friends. He grew quiet and detached, spending days talking to his hat, until he left without a word."
                if creeks_reasonstojoin_feast_copper:
                    $ custom4 = "Thanks to the new supplies gained through trade and the copper coming from the new mining hamlet, "
                else:
                    $ custom4 = "Thanks to the new supplies gained through trade, "
                if quest_explorepeninsula_result == "success1":
                    if quest_explorepeninsula_mainvillage == "creeks":
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew in strength and comfort. The guild brought experienced tanners and fur makers with them, helping the locals mimic the techniques of the masters, but also discouraging any ambitions of farming and fishing. After a decade, the village was completely dependent on purchasing supplies from the outside, but managed to stick to its unusual customs."
                    elif endgame_creeks_leader_option:
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew strong, but far from being rich. While the village was bursting with life, constantly pursuing new ideas for a better tomorrow, most of them ended in nothing. On the other hand, the locals never tied themselves too strongly with the city, and maintained their unusual customs."
                    else:
                        if creeks_reasonstojoin_feast_copper:
                            $ custom4 = ""
                        else:
                            $ custom4 = ""
                        $ custom1 = "The children seen by the roadwarden during their visit in {color=#f6d6bd}Creeks{/color} turned out to be the village’s last generation. The inexperienced leaders couldn’t fix the lack of supplies, and the people grew desperate. The tribe took the chance and left the peninsula, seeking an abandoned hamlet or village beyond {color=#f6d6bd}Hag Hills{/color} - and while not all of them reached the new settlement alive, the family was able to start anew."
                elif quest_explorepeninsula_result == "success2":
                    if quest_explorepeninsula_mainvillage == "creeks":
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew in strength and comfort. The guild brought experienced tanners and fur makers with them, helping the locals mimic the techniques of the masters, but also discouraging any ambitions of farming and fishing.\n\nAfter a decade, the village was completely dependent on purchasing supplies from the outside, and soon after, it learned that it could get the help of the city architects - if, of course, the tribe agreed to building a small chapel of The Wright, and welcomed the priest who would just {i}love{/i} to run it."
                    elif endgame_creeks_leader_option:
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew in strength and comfort. The guild brought experienced tanners and fur makers with them, helping the locals mimic the techniques of the masters, but also discouraging any ambitions of farming and fishing. After a decade, the village was completely dependent on purchasing supplies from the outside, but managed to stick to its unusual customs."
                    else:
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew strong, but far from being rich. While the village was bursting with life, constantly pursuing new ideas for a better tomorrow, most of them ended in nothing. On the other hand, the locals never tied themselves too strongly with the city, and maintained their unusual customs."
                elif quest_explorepeninsula_result == "success3":
                    if quest_explorepeninsula_mainvillage == "creeks":
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew in strength and comfort. The guild brought experienced tanners and fur makers with them, helping the locals mimic the techniques of the masters, but also discouraging any ambitions of farming and fishing.\n\nAfter a decade, the village was completely dependent on purchasing supplies from the outside, and soon after, it learned that it could get the help of the city architects - if, of course, the tribe agreed to building a small chapel of The Wright, and welcomed the priest who would just {i}love{/i} to run it. Two generations later, no traveler would find a trace of the old, unusual customs of the tribe’s ancestors."
                    elif endgame_creeks_leader_option:
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew in strength and comfort. The guild brought experienced tanners and fur makers with them, helping the locals mimic the techniques of the masters, but also discouraging any ambitions of farming and fishing.\n\nAfter a decade, the village was completely dependent on purchasing supplies from the outside, and soon after, it learned that it could get the help of the city architects - if, of course, the tribe agreed to building a small chapel of The Wright, and welcomed the priest who would just {i}love{/i} to run it."
                    else:
                        $ custom1 = "the children of {color=#f6d6bd}Creeks{/color} grew strong, but far from being rich. While the village was bursting with life, constantly pursuing new ideas for a better tomorrow, most of them ended in nothing. On the other hand, the locals never tied themselves too strongly with the city, and maintained their unusual customs."
            menu:
                '[custom4][custom1][custom2][custom3]
                '
                '(continue)':
                    jump epilogue_slides_galerocks

    label epilogue_slides_galerocks:
        if not galerocks_firsttime:
            jump epilogue_slides_shortcut
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ endcredits_counter += 1
        show areapicture ep_14 at basicfade
        if quest_explorepeninsula_result == "fail1":
            $ custom1 = "The soil of {color=#f6d6bd}Gale Rocks{/color} couldn’t provide for the village’s hard-working people with crops alone. Groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
        elif quest_explorepeninsula_result == "success1":
            if quest_explorepeninsula_mainvillage == "galerocks":
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. In the years to come, their days were good, and, for the most part, remained the same."
            elif endgame_galerocks_leader_option:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} needed little, and after selling the excess of fish and salt, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
            elif quest_galerockssupport == 4 or quest_galerockssupport == 3:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} remained loyal to {color=#f6d6bd}Glaucia{/color}, and were in large part omitted by the new wave of traders. Facing hunger, Groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
            else:
                $ custom1 = "The soil of {color=#f6d6bd}Gale Rocks{/color} couldn’t provide for the village’s hard-working people with crops alone. Groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
        elif quest_explorepeninsula_result == "success2":
            if quest_explorepeninsula_mainvillage == "galerocks":
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. After a few years, they were able to purchase enough ore to equip themselves with fine blades, keeping their own caravans and hunters safe.\n\nTheir days were good, but the villagers remembered the teachings of their ancestors - just as all the lean years come to an end, so too do the ones of prosperity."
            elif endgame_galerocks_leader_option:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. In the years to come, their days were good, and, for the most part, remained the same."
            elif quest_galerockssupport == 4 or quest_galerockssupport == 3:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} remained loyal to {color=#f6d6bd}Glaucia{/color}, and were in large part omitted by the new wave of traders. However, they needed little, and after selling the excess of fish and salt, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
            else:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} needed little, and after selling the excess of fish and salt, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
        elif quest_explorepeninsula_result == "success3":
            if quest_explorepeninsula_mainvillage == "galerocks":
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. After a few years, they were able to purchase enough ore to equip themselves with fine blades, keeping their own travelers and hunters safe. Soon, their caravans crossed {color=#f6d6bd}Hag Hills{/color}, bringing home luxuries for prices better than those of the cityfolk.\n\nTheir days were good, but the villagers remembered the teachings of their ancestors - just as all the lean years come to an end, so too do the ones of prosperity."
            elif endgame_galerocks_leader_option:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. After a few years, they were able to purchase enough ore to equip themselves with fine blades, keeping their own caravans and hunters safe.\n\nTheir days were good, but the villagers remembered the teachings of their ancestors - just as all the lean years come to an end, so too do the ones of prosperity."
            elif quest_galerockssupport == 4 or quest_galerockssupport == 3:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} remained loyal to {color=#f6d6bd}Glaucia{/color}, and were in large part omitted by the new wave of traders. However, they needed little, and after selling the excess of fish and salt, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
            else:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} didn’t need much time to experience improvements. Selling the excess of fish and salt, they received much needed crops and tools, and strengthened their ties with The United Church. In the years to come, their days were good, and, for the most part, remained the same."
        menu:
            '[custom1][custom2][custom3]
            '
            '(continue)':
                jump epilogue_slides_shortcut

    label epilogue_slides_shortcut:
        if not shortcut_traveled:
            jump epilogue_slides_eudocia
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        if quest_explorepeninsula_result == "fail1":
            $ custom1 = "The heart of the forest soon sealed the forgotten remains of its only road, reclaiming its primeval shape."
            show areapicture ep_15a at basicfade
        elif quest_explorepeninsula_result == "success1":
            $ custom1 = "The road leading through the heart of the forest remained abandoned, reserved for the times of great need and hardly ever maintained by the soldiers from {color=#f6d6bd}Hovlavan{/color}."
            show areapicture ep_15b at basicfade
        elif quest_explorepeninsula_result == "success2":
            $ custom1 = "Though with difficulty, the road leading through the heart of the forest was restored, maintained by the combined efforts of soldiers and the locals."
            show areapicture ep_15b at basicfade
        elif quest_explorepeninsula_result == "success3":
            $ custom1 = "Though with difficulty, the road leading through the heart of the forest was restored, maintained by the combined efforts of soldiers and the locals. In its center, surrounding the ancient cairn, was built a hamlet for travelers, known as {color=#f6d6bd}Between Towers{/color}."
            show areapicture ep_15c at basicfade
        if asterion_lie == "monsters" and not pc_dead:
            $ custom2 = "\n\nOne day, a young man came to the peninsula looking for {color=#f6d6bd}Asterion{/color}, then, following the tale he had heard from another roadwarden years prior, he entered the wilderness, hoping to find the monster that was responsible for his father’s disappearance. Some claim that he is roaming the woods to this day."
        elif asterion_lie == "bandits" and not pc_dead:
            $ custom2 = "\n\nOne day, a young man came to the peninsula looking for {color=#f6d6bd}Asterion{/color}, then, following the tale he had heard from another roadwarden years prior, he entered the wilderness, hoping to find the band that was responsible for his father’s disappearance. Some claim that he is roaming the woods to this day."
        elif asterion_lie == "solitude" and not pc_dead:
            $ custom2 = "\n\nOne day, a young man came to peninsula looking for {color=#f6d6bd}Asterion{/color}, then, following the tale he had heard from another roadwarden years prior, he entered the wilderness, hoping to find the place where his father had been hiding. Some claim that he is roaming the woods to this day."
        if banditshideout_firsttime:
            if glaucia_willreturntogalerocks:
                $ custom3 = "\n\nAfter returning home to meet with her parents, {color=#f6d6bd}Glaucia{/color} took responsibility for breaking the trust of her tribe. She joined the fishers, and while she wasn’t eager to follow orders instead of giving them, she rarely raised her voice. She often wandered the beach by herself, despite the roaming saurians and harpies - after a few violent clashes, they learned to stay out of her way."
                if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                    $ custom4 = "\n\nNot all of {color=#f6d6bd}Glaucia’s{/color} thugs were eager to return to regular life, and it just so happens that {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, was ready to play the part of the new chief. Soon after reaching the camp, she convinced her new subordinates to start a somewhat honest life as mercenaries, but her luck hadn’t changed - most members of her group, including her, were dead within two years."
            elif quest_galerockssupport == 2:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} kept fighting on her own - though only briefly. She tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}, but once her supplies ran short, she got reckless, and, after a few seasons, was killed by a lucky arrow."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} refused to abandon her new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                else:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} refused to abandon her new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few seasons, but once her supplies ran short, she got reckless, and got caught by the village guards. She died with the sickle sword in her hand."
                if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                    $ custom4 = "\n\nAmong other thugs who also lost their lives was {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, who had returned to the only place that she knew would take her."
            elif quest_galerockssupport == 4 or quest_galerockssupport == 3 or quest_galerockssupport == 1:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} kept fighting. For years she tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "spent the remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nAmong other thugs who also lost their lives was {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, who had returned to the only place that she knew would take her."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}. After bothering them for years, she lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "spent the remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the necromancers. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nThe highwaymen felt lost at first, but accepted the leadership of {color=#f6d6bd}Tulia{/color}, who had been with them ever since she had been banished for her previous collaboration with the band. She convinced her new subordinates to start a somewhat honest life as mercenaries, and she managed to learn a few things from her previous chief. Her new group stuck together for almost a decade, and, before she lost her life during a dragon hunt, she led a squad of twenty fighters and spellcasters."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "was among the bandits captured by the guards of {color=#f6d6bd}Howler’s Dell{/color}. Scrapped of their possessions and their mount, they perished before they crossed {color=#f6d6bd}Hag Hills{/color}."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nAmong other thugs who also lost their lives was {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, who had returned to the only place that she knew would take her."
                else:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few years, but lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "lost their palfrey during one of the raids against {color=#f6d6bd}Howler’s Dell{/color}, but was in return the only bandit invited by {color=#f6d6bd}Glaucia{/color} to cross {color=#f6d6bd}Hag Hills{/color} with her. They had no other choice but to look for a new life once again."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nThe highwaymen felt lost at first, but accepted the leadership of {color=#f6d6bd}Tulia{/color}, who had been with them ever since she had been banished for her previous collaboration with the band. She convinced her new subordinates to start a somewhat honest life as mercenaries, and she managed to learn a few things from her previous chief. Her new group stuck together for almost a decade, and, before she lost her life during a dragon hunt, she led a squad of twenty fighters and spellcasters."
            else:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} kept fighting. For years she tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "spent the remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nAmong other thugs who also lost their lives was {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, who had returned to the only place that she knew would take her."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}. After bothering them for years, she lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "spent the remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the necromancers. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nThe highwaymen felt lost at first, but accepted the leadership of {color=#f6d6bd}Tulia{/color}, who had been with them ever since she had been banished for her previous collaboration with the band. She convinced her new subordinates to start a somewhat honest life as mercenaries, and she managed to learn a few things from her previous chief. Her new group stuck together for almost a decade, and, before she lost her life during a dragon hunt, she led a squad of twenty fighters and spellcasters."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "was among the bandits captured by the guards of {color=#f6d6bd}Howler’s Dell{/color}. Scrapped of their possessions and their mount, they perished before they crossed {color=#f6d6bd}Hag Hills{/color}."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nAmong other thugs who also lost their lives was {color=#f6d6bd}Tulia{/color}, banished for her previous collaboration with the band, who had returned to the only place that she knew would take her."
                else:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few years, but lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if endgame_newlife_selected == "bandits":
                        $ endgame_epilogue_fluff = "lost their palfrey during one of the raids against {color=#f6d6bd}Howler’s Dell{/color}, but was in return the only bandit invited by {color=#f6d6bd}Glaucia{/color} to cross {color=#f6d6bd}Hag Hills{/color} with her. They had no other choice but to look for a new life once again."
                    if (tulia_about_bandits_hopeless and not pc_dead) or (tulia_about_bandits_liedto and not pc_dead):
                        $ custom4 = "\n\nThe highwaymen felt lost at first, but accepted the leadership of {color=#f6d6bd}Tulia{/color}, who had been with them ever since she had been banished for her previous collaboration with the band. She convinced her new subordinates to start a somewhat honest life as mercenaries, and she managed to learn a few things from her previous chief. Her new group stuck together for almost a decade, and, before she lost her life during a dragon hunt, she led a squad of twenty fighters and spellcasters."
        menu:
            '[custom1][custom2][custom3][custom4]
            '
            '(continue)':
                jump epilogue_slides_eudocia

    label epilogue_slides_eudocia:
        if not eudocia_inside_firsttime:
            jump epilogue_slides_greenmountain
        $ endcredits_counter += 1
        if (not quest_explorepeninsula_description15a and not quest_explorepeninsula_description15b) or quest_explorepeninsula_result == "fail1" or quest_explorepeninsula_description15c:
            if eudocia_bronzerod_installed >= 6:
                if eudocia_about_flower_refusal:
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} had refused to “bother with the place outside.”"
                    show areapicture ep_16b at basicfade
                elif not quest_eudociaflower_description03:
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she spent many days locked in her house, meeting no one, even if they came to see her. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} was nowhere to be found."
                    show areapicture ep_16b at basicfade
                else:
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she sought joy in her work, sharpening her senses with snake bait, day after day, until her heart stopped beating a year later.\n\nSoon, her residence became overrun with beasts that made nothing of the motionless stone sentinels."
                    show areapicture ep_16a at basicfade
            else:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color}, bored with having nothing to challenge her, spent many days locked in her house, meeting no one, even if they came to see her. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} was nowhere to be found."
                show areapicture ep_16b at basicfade
        else:
            if eudocia_about_flower_refusal:
                show areapicture ep_16b at basicfade
                if quest_explorepeninsula_result == "success1":
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} agreed to do some work for the cityfolk, earning a great amount of luxurious wares, but since every request she got was a variation of making a weapon “even more lethal,” the boredom of repetition started to push her to her limits. She was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders.\n\nThe soldiers told stories of the many wonders they saw at her place, but claimed that {i}the witch{/i} had refused to “bother with the place outside.”"
                elif quest_explorepeninsula_result == "success2":
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} agreed to do some work for the cityfolk, earning a great amount of luxurious wares, but since every request she got was a variation of making a weapon “even more lethal,” the boredom of repetition started to push her to her limits.\n\nShe was often tempted to reach for snake bait, but instead she found enjoyment while chatting with soldiers garrisoned at the nearby tower, who often showed up at her pond. After they spread the news that the enchantress wasn’t, despite all the suspicions, {i}a crazy witch{/i}, more people dared to visit her, including those from her own tribe.\n\nShe died after many decades, not sure if she was happy, but free of the evil spirits that dragged her away from people in the first place."
                elif quest_explorepeninsula_result == "success3":
                    $ custom1 = "{color=#f6d6bd}Eudocia{/color} agreed to do some work for the cityfolk, earning a great amount of luxurious wares, but since every request she got was a variation of making a weapon “even more lethal,” the boredom of repetition started to push her to her limits.\n\nYet, to her surprise, she found enjoyment while chatting with soldiers garrisoned at the nearby tower, who often showed up at her pond. After they spread the news that the enchantress wasn’t, despite all the suspicions, {i}a crazy witch{/i}, more people dared to visit her, including those from her own tribe.\n\nEven though the growing commotion distracted her greatly, the flow of new ideas only helped her improve her talents. Two decades went by, but she finally accepted the invitation of the guild, reaching {color=#f6d6bd}Hovlavan{/color} as a master enchantress. While living in the city was much louder than she was used to, she never thought of snake bait again."
            elif not quest_eudociaflower_description03:
                show areapicture ep_16a at basicfade
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} agreed to do some work for the cityfolk, earning a great amount of luxurious wares, but since every request she got was a variation of making a weapon “even more lethal,” the boredom of repetition started to push her to her limits. She spent many days locked in her house, meeting no one, even if they came to see her. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nOne day, the soldiers barged in, worried about her long absence. They told stories of the many wonders they saw inside, but claimed that {i}the witch{/i} had died without any wounds, even though there was blood on her rotting lips."
            else:
                show areapicture ep_16a at basicfade
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} agreed to do some work for the cityfolk, earning a great amount of luxurious wares, but since every request she got was a variation of making a weapon “even more lethal,” the boredom of repetition started to push her to her limits. She sought joy in her own projects, sharpening her senses with snake bait, day after day, until her heart stopped beating a year later.\n\nSoon, her residence became occupied by the soldiers of {color=#f6d6bd}Hovlavan{/color}, who made nothing of the motionless stone sentinels."
        menu:
            '[custom1]
            '
            '(continue)':
                jump epilogue_slides_greenmountain

    label epilogue_slides_greenmountain:
        if not greenmountaintribe_firsttime:
            jump epilogue_slides_pc
        $ endcredits_counter += 1
        if quest_explorepeninsula_result == "fail1":
            if greenmountaintribe_banned:
                show areapicture ep_17a at basicfade
                if quest_gatheracrew:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence.\n\nTwo centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a prospering hamlet placed on the ruins just at the foot of the volcano."
                else:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence."
            elif cephasgaiane_available or quest_greenmountainsupport == 2 or quest_greenmountainsupport == 3:
                show areapicture ep_17b at basicfade
                $ custom1 = "While {color=#f6d6bd}The Tribe of The Green Mountain{/color} wasn’t keen on restoring its relationship with other villages, {color=#f6d6bd}Cephas{/color} kept sending out the patrols, observing the land from a distance. Seeing the progressing isolation of the tribes and the overgrowing valley of {color=#f6d6bd}Hag Hills{/color}, {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, putting their comfort above security."
            else:
                show areapicture ep_17a at basicfade
                if quest_gatheracrew:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence.\n\nTwo centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a prospering hamlet placed on the ruins just at the foot of the volcano."
                else:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence."
        elif quest_explorepeninsula_result == "success1":
            if quest_greenmountainsupport == 2 and not greenmountaintribe_banned:
                show areapicture ep_17c at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} and {color=#f6d6bd}Gaiane{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color} were surprised to learn of the diplomats at the gate to their village, arriving with a small token of {color=#f6d6bd}Hovlavan’s{/color} good will.\n\nAfter agreeing on the borders of the peninsula that ought not to be crossed, the cityfolk sometimes tested {color=#f6d6bd}The Tribe’s{/color} patience, but the next few generations went by without an open conflict. The village in the mountains was left to itself, learning to accept that {color=#f6d6bd}High Island{/color} might never be restored."
            elif quest_greenmountainsupport == 3 and not greenmountaintribe_banned:
                show areapicture ep_17c at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, decided to meet with the soldiers garrisoned at the watchtower by the eastern road and describe the borders of {color=#f6d6bd}The Tribe’s{/color} territory. While the tense negotiations would recur once every few years, at one point getting dangerously close to an open conflict, the village in the mountains was left to itself, learning to accept that {color=#f6d6bd}High Island{/color} might never be restored."
            elif cephasgaiane_available or greenmountaintribe_banned:
                show areapicture ep_17d at basicfade
                $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, ended up blocking the trail that connected it to the rest of the peninsula. Every once in a while, the rumors of “pagans of weird tongue” seen by the eastern trail spread among the merchants, but a keen listener would notice that such tales always differed when it came to describing {color=#f6d6bd}The Tribe’s{/color} clothing, weapons, and skin."
            else:
                show areapicture ep_17a at basicfade
                if quest_gatheracrew:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence.\n\nTwo centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a prospering hamlet placed on the ruins just at the foot of the volcano."
                else:
                    $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence."
        elif quest_explorepeninsula_result == "success2":
            if quest_greenmountainsupport == 2 and not greenmountaintribe_banned:
                show areapicture ep_17c at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} and {color=#f6d6bd}Gaiane{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color} were surprised to learn of the diplomats at the gate to their village, arriving with a small token of {color=#f6d6bd}Hovlavan’s{/color} good will. However, after agreeing on the borders of the peninsula that ought not to be crossed, the cityfolk sometimes tested {color=#f6d6bd}The Tribe’s{/color} patience.\n\nAfter a few decades, the caravans coming to the peninsula faced a great threat - a “mad” unicorn, capable of a merciless charge at an entire group of fighters. The desperate soldiers sought help from {color=#f6d6bd}The Tribe{/color}, and after receiving it, the ties between the two communities tightened, giving a start to a careful, but much appreciated trade deal."
            elif quest_greenmountainsupport == 3 and not greenmountaintribe_banned:
                show areapicture ep_17c at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, decided to meet with the soldiers garrisoned at the watchtower by the eastern road and describe the borders of {color=#f6d6bd}The Tribe’s{/color} territory.\n\nThe tense negotiations would recur once every few years, at one point turning into an open conflict, but the officials struggled to beat the locals on their own land. Finally, the village in the mountains was left to itself, and their recent victory gave them hope that {color=#f6d6bd}High Island{/color} might one day be reclaimed."
            else:
                show areapicture ep_17d at basicfade
                $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, ended up blocking the trail that connected it to the rest of the peninsula. Every once in a while, the rumors of “pagans of weird tongue” seen by the eastern trail spread among the merchants, but a keen listener would notice that such tales always differed when it came to describing {color=#f6d6bd}The Tribe’s{/color} clothing, weapons, and skin."
        elif quest_explorepeninsula_result == "success3":
            if quest_greenmountainsupport == 2 and not greenmountaintribe_banned:
                show areapicture ep_17a at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} and {color=#f6d6bd}Gaiane{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color} were surprised to learn of the diplomats at the gate to their village, arriving with a small token of {color=#f6d6bd}Hovlavan’s{/color} good will. However, after agreeing on the borders of the peninsula that ought not to be crossed, the cityfolk sometimes tested {color=#f6d6bd}The Tribe’s{/color} patience.\n\nAfter a few decades, the caravans coming to the peninsula faced a great threat - a “mad” unicorn, capable of a merciless charge at an entire group of fighters. The desperate soldiers sought help from {color=#f6d6bd}The Tribe{/color}, and after receiving it, the ties between the two communities tightened, giving a start to a careful, but much appreciated trade deal.\n\nHowever, the city chief got a bit {i}too{/i} daring in their negotiations, and sent a priest of The United Church to the village. It sparked a long and bloody conflict over the eastern trail."
            elif quest_greenmountainsupport == 3 and not greenmountaintribe_banned:
                show areapicture ep_17d at basicfade
                $ custom1 = "{color=#f6d6bd}Cephas{/color} of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, decided to meet with the soldiers garrisoned at the watchtower by the eastern road and describe the borders of {color=#f6d6bd}The Tribe’s{/color} territory.\n\nThe tense negotiations would recur once every few years, at one point turning into an open conflict, but the officials were too determined to let go of their recent prey. After losing many warriors, {color=#f6d6bd}The Tribe{/color} ended up blocking the trail that connected it to the rest of the peninsula."
            else:
                show areapicture ep_17d at basicfade
                $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color}, worried about the growing presence of the cityfolk, ended up blocking the trail that connected it to the rest of the peninsula. Every once in a while, the rumors of “pagans of weird tongue” seen by the eastern trail spread among the merchants, but a keen listener would notice that such tales always differed when it came to describing {color=#f6d6bd}The Tribe’s{/color} clothing, weapons, and skin."
        menu:
            '[custom1]
            '
            '(continue)':
                jump epilogue_slides_pc

    label epilogue_slides_pc:
        $ endcredits_counter += 1
        if endgame_epilogue_fluff == "":
            jump endingtransition
        elif endgame_epilogue_fluff == "highisland":
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                '{color=#f6d6bd}[pcname]{/color} never left {color=#f6d6bd}High Island{/color}. Some say they found the same safe haven as {color=#f6d6bd}Asterion{/color}, treasures so grand they both have no reason to return to The Dragonwoods. Others have no doubt the shell of the roadwarden has either been crushed by the teeth of a dragon, or is now roaming the woods as an undead, hungry for human blood, growing in strength with every fog.
                '
                '(continue)':
                    jump endingtransition
        elif endgame_epilogue_fluff == "rip":
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                '{color=#f6d6bd}[pcname]{/color} survived a few days on the road, chased off from one village to the next. Having sparse equipment, no allies, and no mount, they ended up as a snack for the beasts of autumn.
                '
                '(continue)':
                    jump endingtransition
        else:
            if endgame_newlife_selected == "monastery":
                if endgame_monastery_survived:
                    show areapicture ep_10b at basicfade
                else:
                    show areapicture ep_10a at basicfade
            elif endgame_newlife_selected == "howlersdell":
                if endgame_howlers_destroyed:
                    show areapicture ep_08b at basicfade
                else:
                    show areapicture ep_08a at basicfade
            elif endgame_newlife_selected == "creeks":
                if endgame_creeks_destroyed:
                    show areapicture ep_13a at basicfade
                else:
                    show areapicture ep_13b at basicfade
            elif endgame_newlife_selected == "galerocks" and not glaucia_about_galerocksdecision_liedto:
                show areapicture ep_14 at basicfade
            elif endgame_newlife_selected == "bandits":
                if quest_explorepeninsula_result == "fail1":
                    show areapicture ep_15a at basicfade
                elif quest_explorepeninsula_result == "success1":
                    show areapicture ep_15b at basicfade
                elif quest_explorepeninsula_result == "success2":
                    show areapicture ep_15b at basicfade
                elif quest_explorepeninsula_result == "success3":
                    show areapicture ep_15c at basicfade
            else:
                if pc_religion == "pagan":
                    show areapicture gameover_alt at basicfade
                else:
                    show areapicture gameover at basicfade
            if world_peninsulaname != "the northern peninsula":
                $ custom1 = "{color=#f6d6bd}"
                $ custom2 = "{/color}"
            else:
                $ custom1 = ""
                $ custom2 = ""
            menu:
                '{color=#f6d6bd}[pcname]{/color}, the roadwarden of [custom1][world_peninsulaname][custom2], [endgame_epilogue_fluff]
                '
                '(end the game)':
                    jump endingtransition

label endingtransition:
    nvl clear
    scene bg empty
    $ quick_menu = 0
    hide screen quick_menu
    hide screen endcredits
    hide screen achievements
    hide screen tutorialtooltips
    hide screen characterstatus
    show endscreen
    with Fade(1.0, 1.0, 0.1, color="#0f2a3f")
    $ MainMenu(confirm=False)()
