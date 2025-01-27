################################# ENDING THE GAME - SABOTAGING THE CITY

default anti_epilogue_village_selected = 0
default anti_epilogue_village_tulia_fate = 0 # "city" "pelt" "bandits" 
default quest_pc_goal_ineedmoney_points = 0
default anti_epilogue_pc_survived = 0
default anti_epilogue_pc_survival_deathcause = 0 # "beasts" "bounty" "undead" "glaucia" "thais_bounty" "pc_goal"
default anti_epilogue_pc_survival_deathdescription = ""
default anti_epilogue_peace_points = 0
default anti_epilogue_peace_tier = 0
default anti_epilogue_peace_threshold_1 = 4
default anti_epilogue_peace_threshold_2 = 8
default anti_epilogue_peace_threshold_3 = 12
default endgame_creeks_withered = 0
default antiepilogue_oldpagos_destroyed = 0

label anti_hovlavanALL:
    label anti_hovlavan01:
        hide areapicture
        scene empty
        scene layoutfull
        stop nature fadeout 4.0
        $ endgame_mode = 1
        $ attitudes = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        hide screen characterstatus
        nvl clear
        if pc_goal == "iwanttohelp" and pc_goal_iwanttohelppoints >= 15 and quest_pc_goal == 1:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            menu:
                'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                \n\nYou think of the people you’ve encountered, of what you’ve done for them. You picture the rough roads and their monsters, the claws hidden in all the places where you can’t be at once. Humans torn limb from limb, burnt villages, poisoned wells, cut throats...
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
                                    jump anti_hovlavan04
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
                                    jump anti_hovlavan04
        if pc_goal == "iwantstatus" and pc_goal_iwantstatuspoints >= 4 and quest_pc_goal == 1:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            if pc_lies >= 10 or (thais_about_magicfruit_received and not thais_about_magicfruit_barter) or (quest_glauciasupport == 2 and not glaucia_about_galerocksdecision_liedto):
                menu:
                    'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                    \n\nYou think of the leaders you’ve encountered, the work you’ve done for them, and the sacrifices you had to make to get on their good side. You’ve spun the first threads of your web of connections. Yet something distorts your new beginning, a shadow that grows greater with every heartbeat.
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
                            'The gloom comes straight from the soul of a very different being than the one who came to this peninsula. Is the {color=#f6d6bd}[pcname]{/color} you knew gone? Is this new creature the {i}real{/i} you?
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
                                        jump anti_hovlavan04
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
                                        jump anti_hovlavan04
            else:
                if pc_lies:
                    $ custom1 = "You sometimes lied, but not overly much"
                else:
                    $ custom1 = "You somehow managed to move forward without a single lie"
                menu:
                    'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                    \n\nWhen you wake up after a few hours, you think of the leaders you’ve encountered, the work you’ve done for them, and the hardships you had to overcome to get on their good side. You’ve spun the first threads of your web of connections.
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
                            'As you sift through the memories of your journey, you feel complete. You smile, thinking of the things you’ve accomplished, and of what still awaits you.
                            '
                            'The next chapter of my life.' if pc_class == "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next chapter of my life.')
                                jump anti_hovlavan04
                            'The next stage of my life.' if pc_class != "scholar":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The next stage of my life.')
                                jump anti_hovlavan04
                    'I don’t really care about any of that. I just did what I thought was most beneficial for me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t really care about any of that. I just did what I thought was most beneficial for me.')
                        $ quest_pc_goal_description_completed_iwantstatus = "I’ve made some powerful connections and didn’t hurt too many people in the process. I’ll have a great advantage when talking to the members of the guild."
                        $ endgame_epilogue_evil = 2
                        $ achievement_pc_goal_description = "I’ve made some powerful connections and didn’t hurt too many people in the process."
                        $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                        $ quest_pc_goal = 2
                        $ pc_hp_can5 = 1
                        menu:
                            'As you sift through the memories of your journey, you feel ready. You smile, thinking of the new possibilities you’ve unlocked, and of what still awaits you.
                            '
                            'I lie down.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                jump anti_hovlavan04
        if pc_goal == "iwanttoberemembered" and pc_goal_iwanttoberememberedpoints >= 6 and quest_pc_goal == 1:
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            menu:
                'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                \n\nYou think of the things that you’ve done, the places you’ve visited, the mysteries you’ve unraveled. You keep waking up, not sure if these thoughts are a dream, a memory, or a vision. You stand up, walk around, and breathe, slowly, deeply, your stomach rising and falling.
                '
                'I focus on its movements.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on its movements.')
                    menu:
                        'You think back on the spectacular deeds you’ve accomplished. Their weight is strangely light, as if all that you’ve done hardly means anything at all. You may have started many tales here, at the northern edge of the province, but will any soul south of {color=#f6d6bd}Hag Hills{/color} ever hear them, or would they even care? Are these stories even worth a free bowl of stew at an inn?
                        '
                        'Rubbish. Dozens of lives were saved, and it’s all thanks to me. People here will remember me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Rubbish. Dozens of lives were saved, and it’s all thanks to me. People here will remember me.')
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
                                    jump anti_hovlavan04
                        'I’ve done so much, yet I must admit that I’m yet another roadwarden, nothing more.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve done so much, yet I must admit that I’m yet another roadwarden, nothing more.')
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
                                    jump anti_hovlavan04
        if (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_howlersdell and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_creeks and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_monastery and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_bandits and quest_pc_goal == 1) or (pc_goal == "iwanttostartanewlife" and pc_goal_iwantnewlife_galerocks and quest_pc_goal == 1):
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            show areapicture nightsky01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            menu:
                'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                \n\nYour dreams are chaotic and vivid, mixing the animal fangs and blood from the recent days with the most deeply rooted events of your past, which shaped your soul to what it is now. You’re sweating and keep waking up, not sure if these thoughts are memories, visions, or your imagination.
                \n\nYou stand up, walk around, and breathe, slowly, deeply, focusing on the movement of your stomach. You observe the scratches, cuts, and bruises you earned this summer. You don’t know how much more you can endure.
                '
                'I’m thinking about my betrayal. I could never find real peace in {color=#f6d6bd}Hovlavan{/color}. I was lying to myself.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m thinking about my betrayal. I could never find real peace in {color=#f6d6bd}Hovlavan{/color}. I was lying to myself.')
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
                            jump anti_hovlavan04
        if pc_goal == "iwantmoney":
            if quest_pc_goal == 2:
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                    \n\nYou keep thinking of all the plans you had for your future life in {color=#f6d6bd}Hovlavan{/color}. You came North to find the coins you needed, and your journey was so long... Yet it’s all over now.
                    '
                    'This is my choice. Giving up on wealth, but gaining freedom.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is my choice. Giving up on wealth, but gaining freedom.')
                        $ quest_pc_goal_description_completed_iwantmoney100 = "I abandoned my dreams of a comfortable, lazy life."
                        $ achievement_pc_goal_description = "I abandoned my dreams of a comfortable, lazy life."
                        $ renpy.notify("Quest abandoned: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest abandoned: %s{/i}' %quest_pc_goal_name)
                        menu:
                            'It’s still hard to believe how much you own, as a single human being. And yet... It’s worth so little. The dream is gone.
                            \n\nAnd that’s why you deserve a good, long sleep now.
                            '
                            'I lie down.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                jump anti_hovlavan04
                    'It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.')
                        $ endgame_epilogue_evil = 1
                        $ quest_pc_goal_description_completed_iwantmoney100 = "With 100 dragon bones I can still find a way to get rich here, in the North."
                        $ achievement_pc_goal_description = "With 100 dragon bones I can still find a way to get rich here, in the North."
                        menu:
                            'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, as a single human being, and yet the purpose of your journey is still a dream.
                            \n\nBut not for much longer.
                            '
                            'I lie down. I need to gather my strength.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down. I need to gather my strength.')
                                jump anti_hovlavan04
            elif coins >= 100 and quest_pc_goal == 1:
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                    \n\nYou keep thinking of all the plans you had for your future life in {color=#f6d6bd}Hovlavan{/color}. You came North to find the coins you needed, and your journey was so long... Yet it’s all over now.
                    '
                    'I go to my bags and start to count the dragon bones I own.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and start to count the dragon bones I own.')
                        menu:
                            'You unpack your pouch, or rather your heavy {i}sack{/i}. Counting its contents is soul-crushing, both because of how many of them there are, and because of the stories the coins carry with them. Some of them you remember from the specific transactions you made, or the places where you found them. Others make you think of the dozens of years that they have behind them. They’re all different shapes and colors. Who knows where some of them have been?
                            \n\nA hundred dragon bones.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nYou take a deep breath. All of these opportunities are now gone. You’re just another laborer from the North. A wealthy fighter, true, but still - just a mercenary.
                            '
                            'This is my choice. Giving up on wealth, but gaining freedom.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is my choice. Giving up on wealth, but gaining freedom.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "I abandoned my dreams of a comfortable, lazy life."
                                $ achievement_pc_goal_description = "I abandoned my dreams of a comfortable, lazy life."
                                $ renpy.notify("Quest abandoned: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest abandoned: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It’s still hard to believe how much you own, as a single human being. And yet... It’s worth so little. The dream is gone.
                                    \n\nAnd that’s why you deserve a good, long sleep now.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        jump anti_hovlavan04
                            'It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.')
                                $ endgame_epilogue_evil = 1
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "With 100 dragon bones I can still find a way to get rich here, in the North."
                                $ achievement_pc_goal_description = "With 100 dragon bones I can still find a way to get rich here, in the North."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, as a single human being, and yet the purpose of your journey is still a dream.
                                    \n\nBut not for much longer.
                                    '
                                    'I lie down. I need to gather my strength.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down. I need to gather my strength.')
                                        jump anti_hovlavan04
            elif quest_pc_goal_description_completed_iwantmoney and quest_pc_goal == 1 and item_asterionwine and item_asterionwine_pcknows_2:
                if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                    play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
                show areapicture nightsky01 at basicfade
                nvl clear
                with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
                menu:
                    'You fall asleep right away, exhausted, but relaxed. Tomorrow will be another journey, and another struggle. There may be beasts, or inconvenient questions. But for now - it’s yet another night on the peninsula.
                    \n\nYou keep thinking of all the plans you had for your future life in {color=#f6d6bd}Hovlavan{/color}. You came North to find the coins you needed, and your journey was so long... Yet it’s all over now.
                    '
                    'I go to my bags and grab the bottle of Night’s Bane.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my bags and grab the bottle of Night’s Bane.')
                        menu:
                            'You unpack the wine, remembering the way you earned it. You sniff the expensive contents, even though to you it smells like any other drink based on fermented fruits. It’s strange to realize that this very bottle may lay the path to your future.
                            \n\nYour soul is filled with visions of opulence. The safety of your own house, new stables, or maybe even a stud farm. The tasty food, the clean clothes, the warm bed, a {i}real{/i} bed...
                            \n\nYou take a deep breath. All of these opportunities are now gone. You’re just another laborer from the North. A wealthy fighter, true, but still - just a mercenary.
                            '
                            'This is my choice. Giving up on wealth, but gaining freedom.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is my choice. Giving up on wealth, but gaining freedom.')
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "I abandoned my dreams of a comfortable, lazy life."
                                $ achievement_pc_goal_description = "I abandoned my dreams of a comfortable, lazy life."
                                $ renpy.notify("Quest abandoned: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest abandoned: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It’s still hard to believe how much you own, as a single human being. And yet... It’s worth so little. The dream is gone.
                                    \n\nAnd that’s why you deserve a good, long sleep now.
                                    '
                                    'I lie down.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down.')
                                        jump anti_hovlavan04
                            'It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t be true. I’ll find a way, figure out a plan that will lead me to wealth.')
                                $ endgame_epilogue_evil = 1
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_iwantmoney100 = "With 100 dragon bones I can still find a way to get rich here, in the North."
                                $ achievement_pc_goal_description = "With 100 dragon bones I can still find a way to get rich here, in the North."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                                menu:
                                    'It sounds easy, but your hands are shaking. It’s hard to believe how much you own, as a single human being, and yet the purpose of your journey is still a dream.
                                    \n\nBut not for much longer.
                                    '
                                    'I lie down. I need to gather my strength.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lie down. I need to gather my strength.')
                                        jump anti_hovlavan04
            else:
                pass
        if pc_goal == "ineedmoney":
            if not renpy.music.get_playing(channel='music') == "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg":
                play music "<loop 10.0>audio/hinterheimearthwork_sleep_loop.ogg" fadeout 1.0 fadein 1.0
            show areapicture ep_01 at basicfade
            nvl clear
            with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
            if tulia_about_bandits_grateful and tulia_friendship >= tulia_about_highisland_recruited_threshold:
                $ custom1 = "You spend the night in a proper bed, holding a mug of steaming pigeon soup - this time around, {color=#f6d6bd}Tulia{/color} pays for the stay. She’s a good companion, willing to share the discomforts of the road and to kill boredom with an idle chat."
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
                    $ custom2 = " She keeps to herself, and one time she outright refused to take the riskier route, forcing you to waste a few more tiresome hours."
            if coins >= 200:
                $ quest_pc_goal_ineedmoney_points += 2
            elif coins >= 100:
                $ quest_pc_goal_ineedmoney_points += 1
            if pc_goal_lost100coins:
                $ quest_pc_goal_ineedmoney_points += 1
            if item_asterionwine and item_asterionwine_pcknows_2:
                $ quest_pc_goal_ineedmoney_points += 1
            if quest_pc_goal_ineedmoney_points >= 2:
                $ custom3 = ", and who needs to receive the savings you brought with you"
            else:
                $ custom3 = ", and which parts of the city to avoid"
            menu:
                'The owners recognize you in the {color=#f6d6bd}Bless The Empress{/color} inn, but this time you use a different name. [custom1]
                \n\nThe days fade away slowly. With {color=#f6d6bd}Tulia{/color} by your side, you can’t simply outrun the autumn predators, and a few times your journey gets violent.[custom2]
                \n\nOnce you get close to the city gates, you explain in detail where to find your sibling[custom3]. Then, you wait another two days, looking through the window tensely.
                '
                '{color=#f6d6bd}Tulia{/color} wouldn’t trick me.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Tulia{/color} wouldn’t trick me.')
                    jump anti_hovlavan01_ineedmoney_bonus
                'I should have gone with her, maybe hidden in the shadows, moved from alehouse to alehouse...':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have gone with her, maybe hidden in the shadows, moved from alehouse to alehouse...')
                    label anti_hovlavan01_ineedmoney_bonus:
                        $ quest_pc_goal_ineedmoney_points = 0
                        if quest_pc_goal_ineedmoney_points >= 2:
                            if quest_pc_goal == 1:
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve managed to rescue my sibling."
                                $ achievement_pc_goal_description = "I’ve managed to rescue my sibling."
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            menu:
                                'Finally, you see them. They’re covered in a dark cloak, but you recognize their silhouette right away. 
                                '
                                'It worked. We’re free.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It worked. We’re free.')
                                    jump anti_hovlavan04
                        elif quest_pc_goal_ineedmoney_points >= 1:
                            if quest_pc_goal == 2:
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ achievement_pc_goal_description = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ renpy.notify("Completed quest updated: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            elif quest_pc_goal == 1:
                                $ quest_pc_goal = 2
                                $ pc_hp_can5 = 1
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ achievement_pc_goal_description = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ endgame_epilogue_evil = 1
                            menu:
                                'Finally, you see them. They’re covered in a dark cloak, but you recognize their silhouette right away. 
                                '
                                'We may not have enough to pay the debt collectors yet... But we’ll use my savings to hide in the North.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We may not have enough to pay the debt collectors yet... But we’ll use my savings to hide in the North.')
                                    jump anti_hovlavan04
                        else:
                            if quest_pc_goal == 2:
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ achievement_pc_goal_description = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ renpy.notify("Completed quest updated: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            elif quest_pc_goal == 1:
                                $ quest_pc_goal = 2
                                $ quest_pc_goal_description_completed_ineedmoney100 = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ achievement_pc_goal_description = "I’ve managed to help my sibling flee the city... But will it be enough?"
                                $ renpy.notify("Quest completed: %s" %quest_pc_goal_name)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: %s{/i}' %quest_pc_goal_name)
                            $ endgame_epilogue_evil = 2
                            menu:
                                'Finally, you see them. They’re covered in a dark cloak, but you recognize their silhouette right away. 
                                '
                                'We may not have enough to pay the debt collectors... But we’ll find a place to hide in the North.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We may not have enough to pay the debt collectors... But we’ll find a place to hide in the North.')
                                    jump anti_hovlavan04

    label anti_hovlavan04:
        show screen endcredits()
        $ quick_menu = 0
        hide screen quick_menu
        if not whitemarshes_nomoreundead or whitemarshes_destroyed:
            $ endgame_foggy_destroyed = 1
            $ endgame_creeks_destroyed = 1
            $ anti_epilogue_peace_points -= 4
            if quest_easternpath_points <= 4:
                $ anti_epilogue_peace_points -= 1
        else:
            if orentius_convinced:
                $ anti_epilogue_peace_points += 2
            elif whitemarshes_attacked:
                $ anti_epilogue_peace_points += 1
            if quest_explorepeninsula_description08:
                $ anti_epilogue_peace_points += 2
            elif quest_easternpath_points >= 4:
                $ anti_epilogue_peace_points += 1
            elif quest_easternpath_points <= 2:
                $ anti_epilogue_peace_points -= 1
        if quest_ruins_choice == "thais_defeated":
            $ anti_epilogue_peace_points += 2
        if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
            $ anti_epilogue_peace_points -= 1
        if quest_healingtheplague == 2:
            $ anti_epilogue_peace_points += 2
        else:
            $ anti_epilogue_peace_points -= 2
        if quest_monasterysupport_description01:
            $ anti_epilogue_peace_points += 1
        elif quest_monasterysupport_description03:
            $ anti_epilogue_peace_points -= 1
        if quest_galerockssupport == 2:
            $ anti_epilogue_peace_points += 1
        elif quest_galerockssupport == 3 or quest_galerockssupport == 4:
            $ anti_epilogue_peace_points -= 1
        if oldtunnel_inside_opened:
            $ anti_epilogue_peace_points += 1
        if quest_greenmountainsupport == 3:
            $ anti_epilogue_peace_points += 2
        elif quest_greenmountainsupport == 2:
            $ anti_epilogue_peace_points += 1
        elif greenmountaintribe_banned or (asterion_found and not cephasgaiane_about_highisland_permission):
            $ anti_epilogue_peace_points -= 1
        if glaucia_willreturntogalerocks:
            $ anti_epilogue_peace_points += 1
        if eudocia_bronzerod_installed >= 6 and eudocia_about_flower_refusal:
            $ anti_epilogue_peace_points += 1
        if anti_epilogue_peace_points >= anti_epilogue_peace_threshold_3 and whitemarshes_nomoreundead and not whitemarshes_destroyed and orentius_convinced and not whitemarshes_attacked and quest_ruins_choice == "thais_defeated" and quest_healingtheplague == 2 and quest_galerockssupport == 2:
            $ anti_epilogue_peace_tier = 3
        elif anti_epilogue_peace_points >= anti_epilogue_peace_threshold_2 and whitemarshes_nomoreundead and not whitemarshes_destroyed and orentius_convinced and not whitemarshes_attacked and quest_healingtheplague == 2:
            $ anti_epilogue_peace_tier = 2
        elif (anti_epilogue_peace_points >= anti_epilogue_peace_threshold_1 and quest_healingtheplague == 2) or (anti_epilogue_peace_points >= anti_epilogue_peace_threshold_1 and whitemarshes_nomoreundead and not whitemarshes_destroyed and orentius_convinced and not whitemarshes_attacked):
            $ anti_epilogue_peace_tier = 1
        else:
            $ anti_epilogue_peace_tier = 0
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
        nvl clear
        show areapicture ep_04 at basicfade
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_01main_theme_loop.ogg":
            play music "<loop 15.0>audio/track_01main_theme_loop.ogg" fadeout 1.0 fadein 1.0
        with Fade(1.8, 1.5, 1.8, color="#0f2a3f")
        $ world_peninsulaname = "the northern peninsula"
        if anti_epilogue_peace_tier >= 3:
            $ quest_explorepeninsula = 2
            $ achievement_anticity = 3
        elif anti_epilogue_peace_tier == 2:
            $ quest_explorepeninsula = 2
            $ achievement_anticity = 2
        elif anti_epilogue_peace_tier == 1:
            $ quest_explorepeninsula = 2
            $ achievement_anticity = 1
        elif anti_epilogue_peace_tier == 0:
            $ quest_explorepeninsula = 3
        else:
            $ quest_explorepeninsula = 4
        $ renpy.notify("Quest abandoned: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest abandoned: Explore the Peninsula{/i}')
        #$ endcredits_counter += 1
        menu:
            'It took many years before the guild sent another roadwarden to the northern peninsula - a realm that, to this day, is known for its obscure customs and secrets. 
            '
            '(continue)':
                $ endcredits_counter += 1
                if anti_epilogue_village_selected == "monastery":
                    if anti_epilogue_peace_tier >= 3:
                        $ custom1 = "cared little about the surprised looks, and headed directly for the monastery.\n\nThe leaders of the North, on the other hand, were now eager to strengthen the bonds between them, and began the slow process of healing old wounds. For the first time in a generation, they shared a meal at the stronghold of {color=#f6d6bd}Gale Rocks{/color}, where they agreed to outline a direction for the future. They put together a group of experienced guards and hunters, each coming from a different tribe. These trail cutters moved as a group, securing new trails and restoring small shelters.\n\nWhile this wasn’t enough to start a proper trading route, it became easier to aid the sparse caravans and travelers, and to share goods and supplies in times of need.\n\nThe peninsula was in no way safe, but life was easier, and its people kept their independence."
                        show areapicture ep_06b at basicfade
                    elif anti_epilogue_peace_tier >= 2:
                        $ custom1 = "cared little about the surprised looks, and headed directly for the monastery. The leaders of the North, on the other hand, were now eager to strengthen the bonds between them, and began the slow process of healing old wounds.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south maintained its bad reputation. At the same time, the locals were more open to seek goods, supplies, and friendships beyond their homes, overcoming the arriving times of trouble."
                        show areapicture ep_06b_alt at basicfade
                    elif anti_epilogue_peace_tier >= 1:
                        $ custom1 = "cared little about the surprised looks, and headed directly for the monastery.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south became mercilessly ovegrown. The locals, as distrustful as always, maintained some contact with the other tribes, but many of the past wounds would never heal."
                        show areapicture ep_06a at basicfade
                    else:
                        $ custom1 = "cared little about the hesitant looks, and headed directly for the monastery. The leaders of the North, torn apart by their grievances, were unable to heal old wounds, and focused on caring for their neighbors.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south became mercilessly ovegrown."
                        show areapicture ep_06a at basicfade
                else:
                    if anti_epilogue_peace_tier >= 3:
                        $ custom1 = "faced curious questions, but, widely admired, quickly returned to maintaining the roads, aiding trade, and forwarding messages. Their “betrayal” was met with curiosity and relief, and they soon rejuvenated the ties between the people of the North.\n\nFor the first time in a generation, all the leaders shared a meal at the stronghold of {color=#f6d6bd}Gale Rocks{/color}, where they agreed to outline a direction for the future. They put together a group of experienced guards and hunters, each coming from a different tribe. These trail cutters moved as a group, assisting the rider in their work while also securing new trails and restoring small shelters.\n\nWhile this wasn’t enough to start a proper trading route, it became easier to aid the sparse caravans and travelers, and to share goods and supplies in times of need.\n\nThe peninsula was in no way safe, but life was easier, and its people kept their independence."
                        show areapicture ep_06b at basicfade
                    elif anti_epilogue_peace_tier >= 2:
                        $ custom1 = "faced surprised questions, but, respected by most, quickly returned to maintaining the roads, aiding trade, and forwarding messages. While their “betrayal” was met with hesitancy, after a few seasons of trying to find balance between the quarreling leaders, they strengthened the ties between the people of the North.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south maintained its bad reputation. At the same time, the locals were more open to seek goods, supplies, and friendships beyond their homes, overcoming the arriving times of trouble."
                        show areapicture ep_06b_alt at basicfade
                    elif anti_epilogue_peace_tier >= 1:
                        $ custom1 = "faced hesitant looks, and their “betrayal” was met with suspicion. Since there was still a shred of respect attached to the newcomer’s name, they returned to maintaining the roads, aiding trade, and forwarding messages. Despite the flow of seasons, they only slightly strengthened the ties between the people of the North, constantly seeking balance between the quarreling leaders.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south became mercilessly ovegrown. The locals, as distrustful as always, maintained some contact with the closest tribes, but many of the past wounds would never heal."
                        show areapicture ep_06a at basicfade
                    else:
                        $ custom1 = "were welcomed with kindness by some, but their “betrayal” was met with suspicion. They were still getting paid for maintaining the roads and dealing with threats, but they were rarely aiding in trade, and the leaders avoided sharing any news of great importance with them. Despite the flow of seasons, they weren’t able to restore their reputation.\n\nThe now-abandoned camp in {color=#f6d6bd}Hag Hills{/color} offered no protection, and the route south overgew mercilessly. The locals, still struggling with their grievances, drifted apart."
                        show areapicture ep_06a at basicfade
                menu:
                    'At first, the locals were unaware that {color=#f6d6bd}[pcname]{/color} wasn’t merely continuing their patrols, and had instead decided to stick around for good. Once they revealed their new plan, they [custom1]
                    '
                    '(continue)':
                        jump epilogue_alt_slides_pelt


    label epilogue_alt_slides_pelt:
        if not peltnorth_firsttime:
            jump epilogue_alt_slides_howlers
        $ endcredits_counter += 1
        $ custom2 = ""
        $ custom5 = ""
        if anti_epilogue_peace_tier == 0:
            show areapicture ep_07a at basicfade
        else:
            show areapicture ep_07b at basicfade
        if anti_epilogue_peace_tier == 0 or anti_epilogue_peace_tier == 1:
            if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "Despite the poor state of the peninsula, {color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s visit, allowing the innkeep to purchase steel traps for large game. A few years later, the hunters abandoned the inn and moved to the city, to the goblins’ joy."
            else:
                $ custom1 = "The keeper of {color=#f6d6bd}Pelt of the North{/color} avoided the roadwarden’s services, unless necessary. Once the roads became overgrown, further trade with the southern villages became close to impossible. After ten years, the hunters left their inn, to the goblins’ joy, and disbanded soon after."
            if anti_epilogue_village_tulia_fate == "pelt":
                $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color}, who soon changed her name, was the last soul to join the hunters, but unlike her new crew, she never crossed {color=#f6d6bd}Hag Hills{/color} again. She found work as a woodcutter in {color=#f6d6bd}Gale Rocks{/color}, where she avoided the gaze of travelers."
            else:
                $ custom5 = ""
        elif anti_epilogue_peace_tier == 2:
            if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "{color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s visit, allowing the innkeep to purchase steel traps for large game. This, in combination with the recent growth of prosperity in the peninsula, led the hunters to play an important part in maintaining the southern road. A few years later, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad.\n\nThe inn was sold to brave adventurers from the south, then to a group of lumberjacks, then to ambitious merchants, until it was finally reclaimed by the hunters of {color=#f6d6bd}Howler’s Dell{/color}."
                if anti_epilogue_village_tulia_fate == "pelt":
                    $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color}, who soon changed her name, was the last soul to join the hunters, but unlike them, she never crossed {color=#f6d6bd}Hag Hills{/color} again. She remained within the familiar walls, offering her services as the building’s overseer and hiding her face from travelers."
                else:
                    $ custom5 = ""
            else:
                $ custom1 = "{color=#f6d6bd}Pelt of the North{/color} slowly pursued its financial goals. Thanks to the recent growth of prosperity in the peninsula, the hunters played an important part in maintaining the southern road. After another decade, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad.\n\nThe inn, known for its harsh conditions and dangerous surroundings, was left to a group of hunters from {color=#f6d6bd}Howler’s Dell{/color}."
                if anti_epilogue_village_tulia_fate == "pelt":
                    $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color}, who soon changed her name, was the last soul to join the hunters, but unlike them, she never crossed {color=#f6d6bd}Hag Hills{/color} again. She remained within the familiar walls, offering her services as the building’s overseer and hiding her face from travelers."
                else:
                    $ custom5 = ""
        elif anti_epilogue_peace_tier == 3:
            if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3:
                $ custom1 = "{color=#f6d6bd}Pelt of the North{/color} gained quite a lot from the roadwarden’s visit, allowing the innkeep to purchase steel traps for large game. This, in combination with the recent growth of prosperity in the peninsula, led the hunters to play an important part in maintaining the southern road. A few years later, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad.\n\nThe inn became a safe trading outpost connecting the settlements on both sides of {color=#f6d6bd}Hag Hills{/color}, guarded by the combined forces of the northern tribes."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this slowly growing hamlet, allowed needy travelers to rest inside free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this slowly growing hamlet, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the leader of this slowly growing hamlet, put the safety of her people above all else."
                else:
                    $ custom2 = ""
                if dalit_firsttime:
                    if anti_epilogue_village_tulia_fate == "pelt":
                        $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who soon changed her name and became the building’s overseer, hiding her face from travelers."
                    else:
                        $ custom5 = ""
                else:
                    if anti_epilogue_village_tulia_fate == "pelt":
                        $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color}, who soon changed her name, was the last soul to join the hunters, but unlike them, she never crossed {color=#f6d6bd}Hag Hills{/color} again. She remained within the familiar walls, offering her services as the building’s overseer and hiding her face from travelers."
                    else:
                        $ custom5 = ""
            else:
                $ custom1 = "{color=#f6d6bd}Pelt of the North{/color} slowly pursued its financial goals. Thanks to the recent growth of prosperity in the peninsula, the hunters played an important part in maintaining the southern road. After another five years, they moved to {color=#f6d6bd}Hovlavan{/color}, living off their savings and occasional mercenary work, forming an experienced squad.\n\nThe inn, known for its harsh conditions and dangerous surroundings, was now run by the combined forces of the northern tribes."
                if dalit_friendship >= 25:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, allowed needy travelers to rest inside free of charge."
                elif dalit_friendship >= 10:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, did her best to keep good relationships with her trading partners from the other settlements."
                elif dalit_firsttime:
                    $ custom2 = " {color=#f6d6bd}Dalit{/color}, the new innkeep, put the safety of her people above all else."
                else:
                    $ custom2 = ""
                if dalit_firsttime:
                    if anti_epilogue_village_tulia_fate == "pelt":
                        $ custom5 = "\n\nOne of her most trusted friends was {color=#f6d6bd}Tulia{/color}, who soon changed her name and became the building’s overseer, hiding her face from travelers."
                    else:
                        $ custom5 = ""
                else:
                    if anti_epilogue_village_tulia_fate == "pelt":
                        $ custom5 = "\n\n{color=#f6d6bd}Tulia{/color}, who soon changed her name, was the last soul to join the hunters, but unlike them, she never crossed {color=#f6d6bd}Hag Hills{/color} again. She remained within the familiar walls, offering her services as the building’s overseer and hiding her face from travelers."
                    else:
                        $ custom5 = ""
        menu:
            '[custom1][custom2][custom5]
            '
            '(continue)':
                jump epilogue_alt_slides_howlers


    label epilogue_alt_slides_howlers:
        if not howlersdell_firsttime:
            jump epilogue_alt_slides_oldpagos
        $ endcredits_counter += 1
        if anti_epilogue_peace_tier == 0  or anti_epilogue_peace_tier == 1:
            if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                $ endgame_howlers_destroyed = 1
                show areapicture ep_08b at basicfade
            else:
                show areapicture ep_08a at basicfade
        else:
            show areapicture ep_08a at basicfade
        if anti_epilogue_peace_tier == 0:
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
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. Many believe that it is the blood magic of the desperate locals that is responsible for the many disappearances and kidnappings occurring in the North."
            elif quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                $ custom1 = "After asserting her dominance over the druids, {color=#f6d6bd}Thais{/color} ruled {color=#f6d6bd}Howler’s Dell{/color} with an iron fist, increasing the influence of the village guards and limiting the training of the younger druids. The villagers stayed loyal to the prayers of their ancestors, but as long as their ruler was alive, they remained in many ways close to the city customs.\n\nHaving a charismatic leader, but lacking in resources"
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems, and increased their supplies thanks to the restored fishing hamlet. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = ", the locals increased their supplies thanks to the restored fishing hamlet. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                elif thais_rumor_vein:
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                else:
                    $ custom2 = ", the locals had no other option but to set up new hamlets. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                if druidcave_firsttime:
                    $ custom3 = " A few dissidents even sought help from {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. After a bit more than a decade, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
                else:
                    $ custom3 = "After a bit more than a decade, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
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
                    $ custom3 = " From time to time, they visited the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
        elif anti_epilogue_peace_tier == 1:
            if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                $ custom1 = "After asserting her dominance over the druids, {color=#f6d6bd}Thais{/color} ruled {color=#f6d6bd}Howler’s Dell{/color} with an iron fist, increasing the influence of the village guards and limiting the training of the younger druids. The villagers stayed loyal to the prayers of their ancestors, but as long as their ruler was alive, they remained in many ways close to the city customs.\n\nHaving a charismatic leader, but lacking in resources"
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems, and increased their supplies thanks to the restored fishing hamlet. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = ", the locals increased their supplies thanks to the restored fishing hamlet. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                elif thais_rumor_vein:
                    $ custom2 = ", the locals built a humble hamlet by the eastern road, mining copper and valuable gems. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                else:
                    $ custom2 = ", the locals had no other option but to set up new hamlets. And yet, no matter how much the tribe harvested, {color=#f6d6bd}their mayor{/color} pushed them further, ignoring any claims or words of warning coming from the other tribes."
                if druidcave_firsttime:
                    $ custom3 = " A few dissidents even sought help from {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. After a bit more than a decade, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
                else:
                    $ custom3 = "After a bit more than a decade, the beasts stormed the walls with all their wrath, putting an end to the village’s hunger."
            elif quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They had little interest in growth, but kept their corner of the peninsula rather safe. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
                else:
                    $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
                if druidcave_firsttime:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. {color=#f6d6bd}The archdruidess{/color} sought help from {color=#f6d6bd}the hermit in the cave{/color}, but the doors to his chambers were buried beneath heavy boulders. The desperate locals turned toward the altar in the swamps, feeding the tree and its offspring more lavishly than ever before."
                elif beholder_firsttime:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. The desperate locals sought help from the altar in the swamps, feeding the tree and its offspring more lavishly than ever before."
                else:
                    $ custom3 = "\n\nFinally, the days of trouble came, and no one answered the village’s call. Many believe that it is the blood magic of the desperate locals that is responsible for the many disappearances and kidnappings occurring in the North."
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color}, torn between {color=#f6d6bd}Thais’{/color} dreams of greatness and the druids’ dissent, slowly split in two, and the conflict remained strong even in the next generation, and the one after it. Some started to whisper that the {i}old faithers{/i} ought to be thrown outside, and maybe even shoved into the ruins by the southern road. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals could seek new sources of prosperity, though the mayor’s loyalists benefited from this more than the druids."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the village could never be fully free of its dependence on the other tribes."
                if druidcave_firsttime:
                    $ custom3 = " One day, the tribe brought gifts to {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. From time to time, they visited the old altar, keeping their traditions alive."
                elif beholder_firsttime:
                    $ custom3 = " From time to time, they visited the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
        elif anti_epilogue_peace_tier == 2:
            if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                $ custom1 = "As the number of caravans dwindled, {color=#f6d6bd}Howler’s Dell{/color} started to struggle for goods, but {color=#f6d6bd}Thais’{/color} iron fist made sure to muffle any doubts of her neighbors. She participated in new negotiations, claiming a large chunk of the peninsula for herself, and in return guarding it vigilantly and securing its trails. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals could seek new sources of prosperity, though the mayor’s loyalists benefited from this more than the druids."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the locals could never be fully free of their dependence on the other tribes."
                if druidcave_firsttime:
                    $ custom3 = " One day, they brought gifts to {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. From time to time, they visited the old altar, keeping their traditions alive."
                elif beholder_firsttime:
                    $ custom3 = " From time to time, they visited the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
            elif quest_ruins_choice == "thais_defeated":
                $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They had little interest in growth, but kept their corner of the peninsula rather safe, and were eager to negotiate with the other tribes as equals. "
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
                elif thais_rumor_vein:
                    $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
                else:
                    $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
                $ custom3 = "\n\nWhen the bad days came, {color=#f6d6bd}the hermit in the cave{/color} saw that his tribe was ready to take on the responsibility for their past misdeeds, and he answered {color=#f6d6bd}the archdruidess’{/color} call for help. While the rituals of blood still took place by the swamp altar, he made sure to limit his neighbors’ zeal, and to guide them toward a new balance."
            else:
                $ custom1 = "{color=#f6d6bd}Howler’s Dell{/color}, torn between {color=#f6d6bd}Thais’{/color} dreams of greatness and the druids’ dissent, slowly split in two, and the conflict remained strong even in the next generation, and the one after it. Some started to whisper that the {i}old faithers{/i} ought to be thrown outside, maybe even shoved into the ruins by the southern road."
                if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                    $ custom2 = "Thanks to the new sources of copper, gemstones, and saltfish, the locals could seek new sources of prosperity, though the mayor’s loyalists benefited from this more than the druids."
                elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                    $ custom2 = "Thanks to the restored fishing hamlet, the locals freed themselves from their reliance on the fishers from the north."
                elif thais_rumor_vein:
                    $ custom2 = "The locals used copper from the new mining hamlet to secure their village and the roads around it."
                else:
                    $ custom2 = "However, lacking in resources, the village could never be fully free of its dependence on the other tribes."
                if druidcave_firsttime:
                    $ custom3 = " One day, the locals brought gifts to {color=#f6d6bd}the hermit in the cave{/color}, but discovered that the doors to his chambers were buried beneath heavy boulders. From time to time, they visited the old altar, keeping their traditions alive."
                elif beholder_firsttime:
                    $ custom3 = " From time to time, they visited the old altar, keeping their traditions alive."
                else:
                    $ custom3 = ""
        elif anti_epilogue_peace_tier == 3:
            $ custom1 = "After banishing {color=#f6d6bd}Thais{/color} and limiting the influence of the village guards, the druids led {color=#f6d6bd}Howler’s Dell{/color} by themselves, drifting further away from the customs accepted among The Ten Cities. They had little interest in growth, but kept their corner of the peninsula rather safe, and were eager to negotiate with the other tribes as equals. "
            if (thais_rumor_vein and quest_fisherhamlet_description07) or (thais_rumor_vein and quest_fisherhamlet_description08):
                $ custom2 = "Their neighbors pressured them into restoring the fishing hamlet, but they refused to pursue the newly found copper vein."
            elif quest_fisherhamlet_description07 or quest_fisherhamlet_description08:
                $ custom2 = "Their neighbors finally pressured them into restoring the fishing hamlet."
            elif thais_rumor_vein:
                $ custom2 = "Despite their neighbors’ pressure, they refused to pursue the newly found copper vein. Lacking in resources, the village could never limit its reliance on the other villages."
            else:
                $ custom2 = "Lacking in resources, the village could never limit its reliance on the other villages."
            $ custom3 = "\n\nWhen the bad days came, {color=#f6d6bd}the hermit in the cave{/color} saw that his tribe was ready to take on the responsibility for their past misdeeds, and he answered {color=#f6d6bd}the archdruidess’{/color} call for help. While the rituals of blood still took place by the swamp altar, he made sure to limit his neighbors’ zeal, and to guide them toward a new balance."
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
                    $ custom5 = "\n\n{color=#f6d6bd}Aegidia{/color} spent a few more seasons alone, practicing magic and archery, until she felt ready to return home. {color=#f6d6bd}Thais{/color} was furious at first, but the druids’ protection allowed her daughter to reclaim her position as a huntress. While her life wasn’t free of conflict, she now truly belonged to her new family."
        else:
            $ custom5 = ""
        if ruinedvillage_truth:
            if quest_ruins_choice == "lefttocity":
                $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
            elif quest_ruins_choice == "thais_defeated":
                if anti_epilogue_peace_tier <= 2:
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, but before it faded away, the people of {color=#f6d6bd}Howler’s Dell{/color} placed a humble stone statue of a tree torn by lightning in the paved square. While it expressed regret, they have never avowed their authorship."
                else:
                    $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts. Before it faded away, the people of {color=#f6d6bd}Howler’s Dell{/color} placed a humble stone statue of a tree torn by lightning in the paved square, and used it as an opportunity to ask all the other tribes for forgiveness."
            elif quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance" or quest_ruins_choice == "thais_alliance_fail":
                $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} wasn’t left alone for long. The people of {color=#f6d6bd}Howler’s{/color} arrived with tools and torches, taking away anything of value and getting rid of any evidence of their wrongdoing. Soon, the only things left were a few loose bricks and the paved square, surrounded by the awakening forest."
            else:
                $ custom6 = "\n\n{color=#f6d6bd}Steep House{/color} stood in silence, providing for a few more scavengers and giving shelter to beasts, then slowly faded away, until there were but a few broken walls surrounding the paved square."
        else:
            $ custom6 = ""
        menu:
            '[custom1][custom2][custom3][custom5][custom6]
            '
            '(continue)':
                jump epilogue_alt_slides_oldpagos


    label epilogue_alt_slides_oldpagos:
        if not oldpagos_firsttime:
            jump epilogue_alt_slides_monastery
        $ endcredits_counter += 1
        if not oldpagos_cured:
            $ antiepilogue_oldpagos_destroyed = 1
            show areapicture ep_09a at basicfade
            if oldpagos_plague_helpfromgalerocks:
                $ custom1 = "More than half of the tribe of {color=#f6d6bd}Old Págos{/color} lost their lives to the plague, including many children, and it would have been even worse if it weren’t for the help brought by their friends from {color=#f6d6bd}Gale Rocks{/color}. "
            else:
                $ custom1 = "More than three-fourths of the tribe of {color=#f6d6bd}Old Págos{/color} lost their lives to the plague, including all of the children. "
            $ custom2 = "The next spring, the first few families left the peninsula for good, and in just two years there were but four elders left inside the proud, tall walls.\n\nIt took decades before the scavengers dared to climb the “haunted” hill, but by that point, the place was overrun by monsters."
            menu:
                '[custom1][custom2]
                '
                '(continue)':
                    jump epilogue_alt_slides_monastery
        else:
            if oldpagos_plague_helpfromgalerocks:
                $ custom1 = "The tribe of {color=#f6d6bd}Old Págos{/color} lost many lives to the plague, but the supplies brought to them by their friends from {color=#f6d6bd}Gale Rocks{/color} helped them overcome the harsh winter. "
            else:
                $ custom1 = "The tribe of {color=#f6d6bd}Old Págos{/color} lost many lives to the plague, and even more so to the harsh winter, but the village survived, as united as ever. "
            if anti_epilogue_peace_tier == 0 or anti_epilogue_peace_tier == 1:
                $ antiepilogue_oldpagos_destroyed = 1
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
            elif anti_epilogue_peace_tier == 2:
                show areapicture ep_09b at basicfade
                $ custom3 = ""
                if not aeli_about_copper:
                    $ custom2 = "In the new, more tranquil state of the peninsula, the locals returned to their craft, focusing on quarrying and building rather than sculpting, once again willing to travel to the neighboring villages. The tribe kept their savings for darker days, which, indeed, came rather quickly."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, wounded by a werebadger, she became a combat instructor."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
                else:
                    $ custom2 = "In the new, more tranquil state of the peninsula, the locals returned to their craft, focusing on quarrying and building rather than sculpting, once again willing to travel to the neighboring villages. With their new mining hamlet, they had access to an abundance of tools and new materials. The tribe kept their savings for darker days, which, they were sure, would come sooner rather than later."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, humbled by the selfless help she received during her struggles, she joined the monks on the mountain, guarding them from flying beasts and escorting them on their journeys to other monasteries."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
            elif anti_epilogue_peace_tier == 3:
                show areapicture ep_09b at basicfade
                $ custom3 = ""
                if not aeli_about_copper:
                    $ custom2 = "In the new, more tranquil state of the peninsula, they returned to their craft, focusing on quarrying and building rather than sculpting, once again willing to travel to the neighboring villages. They played a crucial part in securing the northern paths, and helping the people of {color=#f6d6bd}White Marshes{/color} tame their wetlands.\n\nThe tribe kept their savings for darker days, which, indeed, came rather quickly."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, wounded by a werebadger, she became a combat instructor."
                    if westgate_firsttime:
                        if quintus_left_gate:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} eagerly joined his friends at {color=#f6d6bd}Pelt{/color}. His next years were full of brave hunts and drinking, until he mixed the two a bit too much, barely escaping a runner. With the help of his companions, he began his path toward maturity."
                        else:
                            $ custom5 = "\n\n{color=#f6d6bd}Quintus{/color} stayed on the wall for the first few nights of autumn, but then, lured by hunger, got caught by an unusually patient treant."
                    else:
                        $ custom5 = ""
                else:
                    $ custom2 = "In the new, more tranquil state of the peninsula, they returned to their craft, focusing on quarrying and building rather than sculpting, once again willing to travel to the neighboring villages. They played a crucial part in securing the northern paths, and helping the people of {color=#f6d6bd}White Marshes{/color} tame their wetlands.\n\nOnce {color=#f6d6bd}Aeli{/color} shared the secret of the copper vein, the new mining hamlet was established, giving the locals access to an abundance of tools and new materials. After another generation of slow growth, the first stone statues were once again taken south of {color=#f6d6bd}Hag Hills{/color} by the caravans.\n\nThe tribe kept their savings for darker days, but many decades would pass before they felt hunger again."
                    $ custom4 = "\n\n{color=#f6d6bd}Tertia{/color} stayed in the village, but rejected the further responsibilities of a leader, returning the power to the elders. She spent a few years patrolling the roads, until, humbled by the selfless help she received during her struggles, she joined the monks on the mountain, guarding them from flying beasts and escorting them on their journeys to other monasteries."
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
                    jump epilogue_alt_slides_monastery


    label epilogue_alt_slides_monastery:
        if not monastery_firsttime:
            jump epilogue_alt_slides_whitemarshes
        $ endcredits_counter += 1
        $ custom1 = ""
        if anti_epilogue_peace_tier == 0 or not oldpagos_cured:
            show areapicture ep_10a at basicfade
            $ custom1 = "{color=#f6d6bd}The monastery{/color}, left to itself, lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, a group of adventurers sought treasures inside the ruins, but while there were many, the main mountain had mysteriously collapsed under its own weight, as if it were hollow inside."
        else:
            if anti_epilogue_village_selected == "monastery":
                if anti_epilogue_peace_tier == 1:
                    show areapicture ep_10a at basicfade
                    if antiepilogue_oldpagos_destroyed:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color} lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, the last two monks left the mountain, only to perish in the woods."                    
                    else:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color} lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, the last two monks left the mountain, serving the people of {color=#f6d6bd}Gale Rocks{/color} as humble priests."
                elif anti_epilogue_peace_tier == 2:
                    show areapicture ep_10b at basicfade
                    $ custom1 = "{color=#f6d6bd}The monastery{/color} played some part in the changes occurring among the village leaders, but the monks were valued more for their knowledge and potions than for their spiritual guidance. Thanks to their creations, they didn’t lack any crucial supplies, and every now and then a new soul reached the mountains, hoping to find answers, peace, The Wright, or a hideout.\n\nThe sounds of hammers continued for a few more generations, after which the Order splintered. One group remained, overseeing their caves, while others traveled south, spreading news of the great wonders their hands had immortalized, and luring many pilgrims to the peninsula."
                elif anti_epilogue_peace_tier == 3:
                    show areapicture ep_10b at basicfade
                    $ custom1 = "{color=#f6d6bd}The monastery{/color} played a major part in the changes occurring among the village leaders, and the monks were valued not only for their knowledge and potions, but also for having the once-roadwarden on their side, helping them {i}get things done{/i} when necessary. With these services, they didn’t lack any crucial supplies, and every now and then a new soul reached the mountains, hoping to find answers, peace, The Wright, or a hideout.\n\nThe sounds of hammers continued for a few more generations, after which the Order splintered. One group remained, overseeing {color=#f6d6bd}The Library in Stone{/color}, while others traveled south, spreading news of the great wonders their hands had immortalized, and luring many pilgrims to the peninsula."
            else:
                if anti_epilogue_peace_tier == 1:
                    show areapicture ep_10a at basicfade
                    if antiepilogue_oldpagos_destroyed:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color} lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, the last two monks left the mountain, only to perish in the woods."                    
                    else:
                        $ custom1 = "{color=#f6d6bd}The monastery{/color} lost any interest in the outside world. The years went on, and the sounds of hammers and chanting gave way to the wind. After a century, the last two monks left the mountain, serving the people of {color=#f6d6bd}Gale Rocks{/color} as humble priests."
                elif anti_epilogue_peace_tier == 2:
                    show areapicture ep_10a at basicfade
                    $ custom1 = "{color=#f6d6bd}The monastery{/color} played only a small part in the new wave covering the peninsula, but since their potions were valued among all of the tribes, the monks didn’t struggle. The years went on, but not many new acolytes reached the mountain, and after a few generations, all that was left of the Order was a few disillusioned elders asking The Wright for direction."
                elif anti_epilogue_peace_tier == 3:
                    show areapicture ep_10b at basicfade
                    $ custom1 = "{color=#f6d6bd}The monastery{/color} played some part in the changes occurring among the village leaders, but the monks were valued more for their knowledge and potions, than for their spiritual guidance. Thanks to their creations, they didn’t lack any crucial supplies, and every now and then a new soul reached the mountains, hoping to find answers, peace, The Wright, or a hideout.\n\nThe sounds of hammers continued for a few more generations, after which the Order splintered. One group remained, overseeing their caves, while others traveled south, spreading news of the great wonders their hands had immortalized, and luring many pilgrims to the peninsula."
        menu:
            '[custom1]
            '
            '(continue)':
                jump epilogue_alt_slides_whitemarshes


    label epilogue_alt_slides_whitemarshes:
        if not whitemarshes_firsttime:
            if anti_epilogue_peace_tier == 3:
                jump epilogue_alt_slides_foggy
            elif anti_epilogue_peace_tier == 2:
                $ endgame_foggy_destroyed = 1
                jump epilogue_alt_slides_foggy
            else:
                $ endgame_creeks_destroyed = 1
                $ endgame_foggy_destroyed = 1
                jump epilogue_alt_slides_foggy
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        if whitemarshes_destroyed:
            show areapicture ep_11a at basicfade
            $ endgame_creeks_destroyed = 1
            $ endgame_foggy_destroyed = 1
            $ custom1 = "{color=#f6d6bd}White Marshes{/color} became the largest fortress of the undead in the North. After years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
        elif not whitemarshes_nomoreundead:
            if whitemarshes_attacked:
                show areapicture ep_11b at basicfade
                $ endgame_creeks_destroyed = 1
                $ endgame_foggy_destroyed = 1
                $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
            else:
                if anti_epilogue_peace_tier == 0:
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    show areapicture ep_11a at basicfade
                    $ custom1 = "{color=#f6d6bd}White Marshes{/color}, left to itself, collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
                else:
                    show areapicture ep_11b at basicfade
                    $ endgame_creeks_destroyed = 1
                    $ endgame_foggy_destroyed = 1
                    $ custom1 = "{color=#f6d6bd}White Marshes{/color}, facing growing pressure from the other tribes, buried the routes that connected it with the rest of the peninsula. Troubled, yet isolated, it collapsed after {color=#f6d6bd}Orentius’{/color} sudden death, becoming the largest fortress of the undead in the North.\n\nAfter years of waiting, the growing strength of one of the skeletons gave it a human-like mastery of pneuma. This {i}mage{/i} began a long campaign against the tribes, feeding on their blood, until its army of shells crossed {color=#f6d6bd}Hag Hills{/color}, to the realm of shorter walls and fewer blades."
        elif whitemarshes_attacked:
            show areapicture ep_11b at basicfade
            $ custom1 = "After the attack, {color=#f6d6bd}White Marshes{/color} buried the routes that connected it with the rest of the peninsula. It took decades before it was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals roaming not only the northern lands, but also the woods south of {color=#f6d6bd}Hag Hills{/color}."
        else:
            if thyrsus_about_thyrsusgift_druidcomment:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} upheld his longing for family for another year until, without alerting anyone, he left to see the hermit in the southern caves, and stayed with him for another few seasons. Fighting shame and resentment, he finally found peace in letting go of his past, and found himself a new home in the distant wetlands of the south, where he was valued for his impressive talents - and where his quirks were seen as harmless."
            elif quest_thyrsusgift == 2:
                if thyrsus_highisland_joined:
                    if anti_epilogue_peace_tier <= 1:
                        $ custom2 = "\n\nAfter getting a taste of adventure on {color=#f6d6bd}High Island{/color}, {color=#f6d6bd}Thyrsus{/color} stopped waiting for his family’s acceptance. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he moved to another province, working as a guard for travelers and merchants traveling through its dark wetlands."
                    else:
                        $ custom2 = "\n\nAfter getting a taste of adventure on {color=#f6d6bd}High Island{/color}, {color=#f6d6bd}Thyrsus{/color} stopped waiting for his family’s acceptance and became one of the first bogwardens of the peninsula, using the uncanny strength of his plants to explore the wetlands and its sparse trails. As a guard for hunters, monks, pathfinders, foragers, and herbalists, his life was brief, but appreciated by many."
                else:
                    $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} kept looking for his family’s acceptance for another two years, but then his longing started to turn into resentment, and he left without saying his goodbyes. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he tried his luck as a herbalist, but was never able to carve himself a place where he would feel at home."
            elif thyrsus_highisland_joined:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} remained at the peatfield for another two years, but then abandoned his home without saying any goodbyes, inspired by the taste of adventure from {color=#f6d6bd}High Island{/color}. Having no plants to bend in {color=#f6d6bd}Hovlavan{/color}, he moved to another province, working as a guard for travelers and merchants traveling through its dark wetlands."
            else:
                $ custom2 = "\n\n{color=#f6d6bd}Thyrsus{/color} stayed with his people, but his past dissent was never forgiven. He spent more and more time exploring the bogs, seeking something that would earn the acceptance of his family. Despite all the preparations he took to protect himself from the beasts, he died with his own stew in his mouth, poisoned by a wrongly picked mushroom."
            if orentius_convinced:
                if anti_epilogue_peace_tier <= 1:
                    show areapicture ep_11c at basicfade
                    $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were growing desperate, hungry, and threatened by beasts. Led by {color=#f6d6bd}Helvius{/color}, the tribe stopped looking after the routes that connected it with the rest of the peninsula.\n\nIt took decades before this place was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
                elif anti_epilogue_peace_tier == 2:
                    show areapicture ep_11d at basicfade
                    $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} were slowly expanding beyond their corner of the wetlands, trading sparingly with the other tribes, which as a result provided them with a broader perspective on what a decent mayor should be like. After years of struggling under {color=#f6d6bd}Helvius’{/color} short-sighted leadership, he lost his position, going back to his work as a regular guard.\n\nThe new council of elders focused more on farming than on defensive measures, hoping that the other settlements wouldn’t stab each other in the back - at least for the next few years."
                elif anti_epilogue_peace_tier == 3:
                    show areapicture ep_11d at basicfade
                    $ custom1 = "{color=#f6d6bd}Orentius{/color} kept his word and steered clear of black magic, stepping into the background of local politics. While he guided his neighbors spiritually, he no longer claimed to be {i}a prophet{/i}.\n\nThe people of {color=#f6d6bd}White Marshes{/color} slowly expanded beyond their corner of the wetlands, trading sparingly with the other tribes, which as a result provided them with a broader perspective on what a decent mayor should be like. After years of struggling under {color=#f6d6bd}Helvius’{/color} short-sighted leadership, he lost his position, going back to his work as a regular guard.\n\nThe new council of elders focused more on farming than on defensive measures, hoping that the other settlements wouldn’t stab each other in the back - at least for the next few years. After a few generations of collecting stone from {color=#f6d6bd}Old Págos{/color} and peat from the bogs, the wetlands became famous for their strong walls and cobbled trails, and for their abundance of alchemical ingredients."
            elif orentius_banished:
                show areapicture ep_11c at basicfade
                $ custom1 = "Led by {color=#f6d6bd}Helvius{/color}, {color=#f6d6bd}White Marshes{/color} stopped looking after the routes that connected it with the rest of the peninsula. It took decades before it was reached by a group of adventurers, who were seeking the source of the growing number of monstrous, deformed animals that were crossing {color=#f6d6bd}Hag Hills{/color}, spreading destruction among the villages."
        menu:
            '[custom1][custom2]
            '
            '(continue)':
                jump epilogue_alt_slides_foggy


    label epilogue_alt_slides_foggy:
        $ custom1 = ""
        $ custom2 = ""
        if not foggylake_firsttime:
            jump epilogue_alt_slides_creeks
        elif endgame_foggy_destroyed:
            $ endcredits_counter += 1
            show areapicture ep_12a at basicfade
            menu:
                'The poorly guarded {color=#f6d6bd}Foggy Lake{/color} was among the first places taken over by the wave of the undead coming from {color=#f6d6bd}White Marshes{/color}. The fire that occurred during the break-in consumed the entire hamlet.
                '
                '(continue)':
                    jump epilogue_alt_slides_creeks
        else:
            $ endcredits_counter += 1
            if anti_epilogue_peace_tier == 0:
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
                        if anti_epilogue_peace_tier == 3:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coin by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color}, on the other hand, learned a few things from the hunters, and worked as the inn’s head trapper till the end of his days."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color}, on the other hand, learned a few things from the hunters, and worked as the inn’s head trapper till the end of his days."
                    elif foragers_about_gatherthecrew_tzvi_recruited:
                        if anti_epilogue_peace_tier == 3:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coin by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color} kept to his mother, aiding her with various tasks."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color} kept to his mother, aiding her with various tasks."
                    elif quest_birdhunting_description05:
                        $ custom2 = "\n\n{color=#f6d6bd}Ilan{/color} and, to a lesser extent, {color=#f6d6bd}Tzvi{/color}, were welcomed among the hunters, and after learning a few things from them, worked as the inn’s trappers till the end of their days."
                elif foragers_firsttime:
                    if foragers_about_gatherthecrew_tzvi_recruited and quest_birdhunting_description05:
                        if anti_epilogue_peace_tier == 3:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coin by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color}, on the other hand, was accepted among the hunters, learning the craft back home."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color}, on the other hand, was accepted among the hunters, learning the craft back home."
                    elif foragers_about_gatherthecrew_tzvi_recruited:
                        if anti_epilogue_peace_tier == 3:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, traveling between The Ten Cities and earning coin by stealing from merchants, artisans, and priests. After a few years, he was sentenced to death by banishment.\n\n{color=#f6d6bd}Ilan{/color} kept to his mother, aiding her with various tasks."
                        else:
                            $ custom2 = "\n\nUsing the pay he got from the roadwarden, {color=#f6d6bd}Tzvi{/color} soon left the tavern, only to get mauled to death by a pack of spotted wolves. {color=#f6d6bd}Ilan{/color} kept to his mother, aiding her with various tasks."
                    elif quest_birdhunting_description05:
                        $ custom2 = "\n\n{color=#f6d6bd}Ilan{/color} and, to a lesser extent, {color=#f6d6bd}Tzvi{/color}, were welcomed among the hunters, and were allowed to learn their craft."
                if anti_epilogue_peace_tier == 1:
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "With even fewer caravans and travelers around, {color=#f6d6bd}Foggy{/color} was ready to admit that the peninsula wasn’t going to flourish. However, with the tribes growing a bit friendlier and the roads getting slightly safer, she decided to endure the lean years and focus on turning her inn into {color=#f6d6bd}Creeks’{/color} fishing settlement, of which she was an overseer - and the main cook. After years of hard work leading to the preparation of the new wall and boats, she welcomed a slower decade of rest.\n\nThe {color=#f6d6bd}Foggy Lake{/color} hamlet, now seen as a safe shelter in the North, stands to this day, owned by her tribe."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "With even fewer caravans and travelers around, {color=#f6d6bd}Foggy{/color} was ready to admit that the peninsula wasn’t going to flourish. The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made her hesitant, and unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner in trade”. After a few years, feeling old, betrayed, and naive, she returned to {color=#f6d6bd}Creeks{/color}, aiding her tribe as a cook. She let the building stand, just in case any of the fishers wanted to use it."
                elif anti_epilogue_peace_tier == 2:
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "With even fewer caravans and travelers around, {color=#f6d6bd}Foggy{/color} was relieved to see that the locals were starting to cross the northern trail again. While not all of the conflicts were solved, the tribes seemed to overcome a few harsh years, and after seasons of growing friendships and connections, the tavernkeep made enough lucrative deals to let her dreams take a new direction. A decade passed, and her fragile settlement was surrounded with stone walls from all sides, then boats for the fishers from {color=#f6d6bd}Creeks{/color}, then a proper, if small, stronghold.\n\nOn the day when her heart stopped working, exhausted after a life of noise and hard work, she had climbed the new stone watchtower for the first time, and looked around the lake and hills with a smile.\n\nThe {color=#f6d6bd}Foggy Lake{/color} hamlet, now seen as a safe shelter in the North, stands to this day, owned by her tribe."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "With even fewer caravans and travelers around, {color=#f6d6bd}Foggy{/color} was ready to admit that the peninsula wasn’t going to flourish. The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made her hesitant, unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner in trade”. However, with the tribes growing a bit friendlier and the roads getting slightly safer, she decided to endure the lean years and focus on turning her inn into {color=#f6d6bd}Creeks’{/color} fishing settlement, of which she was an overseer - and the main cook. After years of hard work leading to the preparation of the new wall and boats, she welcomed a slower decade of rest.\n\nThe {color=#f6d6bd}Foggy Lake{/color} hamlet, now seen as a safe shelter in the North, stands to this day, owned by her tribe."
                elif anti_epilogue_peace_tier == 3:
                    if quest_foggy2iason_description04:
                        show areapicture ep_12c at basicfade
                        $ custom1 = "With even fewer caravans and travelers around, {color=#f6d6bd}Foggy{/color} decided to engage fully in aiding the new trade deals and negotiations occurring between the tribes, quickly gathering new friendships and connections. She focused on turning her inn into a proper settlement, focusing less on distilling drinks and collecting trophies, and more on overseeing the growing walls and structures made from the combined efforts of {color=#f6d6bd}Creeks’{/color} workers, {color=#f6d6bd}Old Págos{/color} stonemasons, {color=#f6d6bd}Gale Rocks’{/color} guards, the grain supplies of {color=#f6d6bd}Howler’s Dell{/color}, and {color=#f6d6bd}White Marshes’{/color} peat, used for fuel. A few years before her heart stopped working, she was named the first mayor of {color=#f6d6bd}Foggy Lake{/color} - the youngest village in the North. She welcomed these slower years with gratitude, often observing the peaceful waters from the windows of her watchtower."
                    else:
                        show areapicture ep_12b at basicfade
                        $ custom1 = "The lies of {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt{/color} made {color=#f6d6bd}Foggy{/color} hesitant, unsure if she should spend her future toiling for the sake of her inn, or leave it to her “partner in trade”. However, she was relieved to see that the locals were starting to cross the northern trail again. While not all of the conflicts were solved, the tribes seemed to overcome a few harsh years, and after seasons of growing friendships and connections, the tavernkeep made enough lucrative deals to let her dreams take a new direction. A decade passed, and her fragile settlement was surrounded with stone walls from all sides, then boats for the fishers from {color=#f6d6bd}Creeks{/color}, then a proper, if small, stronghold.\n\nOn the day when her heart stopped working, exhausted after a life of noise and hard work, she had climbed the new stone watchtower for the first time, and looked around the lake and hills with a smile.\n\nThe {color=#f6d6bd}Foggy Lake{/color} hamlet, now seen as a safe shelter in the North, stands to this day, owned by her tribe."
            menu:
                '[custom1][custom2]
                '
                '(continue)':
                    jump epilogue_alt_slides_creeks


    label epilogue_alt_slides_creeks:
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        $ custom5 = ""
        if not creeks_firsttime:
            jump epilogue_alt_slides_galerocks
        elif endgame_creeks_destroyed:
            $ endcredits_counter += 1
            show areapicture ep_13a at basicfade
            menu:
                '{color=#f6d6bd}Creeks{/color} couldn’t withstand the undead wave. Of the tribesfolk who sought rescue in the woods, only a small group of woodcutters survived and found shelter among the fishers of {color=#f6d6bd}Gale Rocks{/color}. The other locals soon joined the forces of the skeleton mage.
                '
                '(continue)':
                    jump epilogue_alt_slides_galerocks
        else:
            $ endcredits_counter += 1
            if anti_epilogue_peace_tier == 0 or (anti_epilogue_peace_tier == 1 and not anti_epilogue_village_selected == "creeks" and not creeks_reasonstojoin_feast_copper):
                $ endgame_creeks_withered = 1
                show areapicture ep_13a at basicfade
                if quest_easternpath == 2:
                    $ custom1 = "The children seen by the roadwarden during their visit in {color=#f6d6bd}Creeks{/color} turned out to be the village’s last generation. The inexperienced leaders couldn’t fix the lack of supplies, and the people grew desperate. The tribe took a chance and left the peninsula, seeking an abandoned hamlet or village beyond {color=#f6d6bd}Hag Hills{/color} - and while not all of them reached the new settlement alive, the family was able to start anew."
                else:
                    $ custom1 = "The children seen by the roadwarden during their visit in {color=#f6d6bd}Creeks{/color} turned out to be the village’s last generation. The dangerous paths, shrinking supplies, and scant experience of the village leaders led to hunger, then desperation. The hastily exploited woods sparked the wrath of the herds, and most of the tribesfolk died during the stampede. The others sought shelter in {color=#f6d6bd}Gale Rocks{/color}."
                    $ custom3 = "\n\nOne of the few survivors was a local hunter, {color=#f6d6bd}Efren{/color}, who at the time happened to be placing traps by the pond. Devastated by grief, he left the peninsula and joined a group of adventurers who, like him, were seeking vengeance on the cruel spirits of nature."
            else:
                show areapicture ep_13b at basicfade
                if anti_epilogue_village_selected == "creeks":
                    $ custom5 = "Not only that, but the roadwarden also assisted their new tribesfolk by helping them explore their woods and meadows, as well as by patrolling the roads. "
                else:
                    $ custom5 = ""
                if anti_epilogue_peace_tier == 1:
                    if quest_easternpath == 2:
                        $ custom2 = "\n\n{color=#f6d6bd}Elah{/color} did his best looking after the eastern roads, but a decade later, when a whole year had passed without any travelers coming from that side, he abandoned this venture, focusing his tribe’s efforts on maintaining the nearest land. He switched from making crooked chairs and tables to building palisades and simple huts, slowly preparing the land for the future farmers and giving up on the hope of supporting his family with trade."
                    else:
                        $ custom2 = "\n\n{color=#f6d6bd}Elah’s{/color} experimentation with furniture making bore fruit only after many years, and never reached the greatness of properly-trained artisans. While his efforts didn’t bring much wealth, his determination turned out to be a priceless feat for the first mayor of his tribe. And no one could dispute that the local huts, while humble, were of great beauty."
                else:
                    if quest_easternpath == 2:
                        $ custom2 = "\n\nWhile {color=#f6d6bd}Elah{/color} might have been the “smallest” of the leaders, he was the first one to recognize the necessity of seeking new friendships in the North. He, assisted by the hunters, paid a visit to all of the settlements, bringing gifts and exchanging news. He then spent much time at {color=#f6d6bd}Foggy’s{/color}, gathering knowledge from other tribes on carpentry, masonry, fishing, hunting, and even learning how to read. Instead of becoming the first mayor of his village, he was valued as the kind-hearted negotiator, eventually earning the name of {color=#f6d6bd}The Uncle of the North{/color}. In his downtime, he gladly engraved the shapes of animals on cups and plates."
                    else:
                        $ custom2 = "\n\nWhile {color=#f6d6bd}Elah{/color} was more than open to collaborate with the other tribes, he found the outside world dangerous and too wild for his tastes. He spent most of his time behind the frail walls of his village, allowing the other leaders of the tribes to hold the reins. His experimentation with furniture making bore fruit only after many years, and never reached the greatness of properly-trained artisans. While his efforts didn’t bring much wealth, his determination turned out to be a priceless feat for the first mayor of his village. And no one could dispute that the local huts, while humble, were of great beauty."
                if anti_epilogue_peace_tier == 1:
                    if (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2) or (quest_missinghunters_admonfound == 2 and quest_missinghunters_vaschelfound == 2) or (quest_missinghunters_vaschelfound == 2 and quest_missinghunters_daliafound == 2):
                        $ custom3 = "\n\n{color=#f6d6bd}Efren{/color}, shaken by what had happened to his friends, spent a few years escorting the local foragers and hunters, but after another two tragic deaths he convinced his tribe to focus on setting only the safest, simplest traps for birds and small prey. While it wasn’t easy for him to influence his family as his ideas involved days of hunger and struggle, his efforts led to focusing more on farmed goods, and - as a result - stability."
                    else:
                        $ custom3 = "\n\nWith the passage of time, {color=#f6d6bd}Efren{/color} saw many more deaths among his friends. He grew quiet and detached, spending days talking to his hat, until he left without a word."
                else:
                    if (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2) or (quest_missinghunters_admonfound == 2 and quest_missinghunters_vaschelfound == 2) or (quest_missinghunters_vaschelfound == 2 and quest_missinghunters_daliafound == 2):
                        $ custom3 = "\n\n{color=#f6d6bd}Efren{/color}, shaken by what happened to his friends, spent a few years escorting the local foragers and hunters until he decided to travel to the other tribes, even those south of {color=#f6d6bd}Hag Hills{/color}. He learned about more efficient, disciplined ways of organizing hunts and foraging trips, and while it wasn’t easy for him to influence his family, his efforts saved many lives in the younger generations. Even before his death, each hunter and trapper in the North would carry a wolf’s tusk or claw - for good luck."
                    else:
                        $ custom3 = "\n\nWith the passage of time, {color=#f6d6bd}Efren{/color} saw many more deaths among his friends. He grew quiet and detached, spending days talking to his hat, until he left without a word."
                if anti_epilogue_peace_tier == 1:
                    $ custom1 = "The new generation grew strong, but far from being rich. The tribe remained open to the sparse travelers and kept its unusual customs, putting its freedom above wealth, and even security. While the village was bursting with life, constantly pursuing new ideas for a better tomorrow, most of them ended in nothing."
                elif anti_epilogue_peace_tier == 2:
                    if creeks_reasonstojoin_feast_copper:
                        $ custom4 = "The new copper hamlet allowed the people of {color=#f6d6bd}Creeks{/color} to produce much-needed tools and weapons, helping them tame their surroundings like never before. "
                    else:
                        $ custom4 = "Growing closer with the other tribes allowed the people of {color=#f6d6bd}Creeks{/color} to gain much-needed tools, weapons, and seeds, helping them tame their surroundings like never before. "
                    $ custom1 = "The new generation grew strong, and lacked little. The tribe welcomed many dissenters from the other villages, tempted by freedom and equity, and while some of the newcomers were a hindrance, most of them added strength and a creative spark to their community. The opportunities grew, and the people pursued ideas for a better tomorrow."
                elif anti_epilogue_peace_tier == 3:
                    if creeks_reasonstojoin_feast_copper:
                        $ custom4 = "The new copper hamlet allowed the people of {color=#f6d6bd}Creeks{/color} to produce the very needed tools and weapons, helping them tame their surroundings like never before. "
                    else:
                        $ custom4 = "Growing closer with the other tribes allowed the people of {color=#f6d6bd}Creeks{/color} to gain much-needed tools, weapons, and seeds, helping them tame their surroundings like never before. "
                    $ custom1 = "The new generation grew strong, and lacked little. The tribe welcomed many dissenters from the other villages, tempted by freedom and equity, and while some of the newcomers were a hindrance, most of them added strength and a creative spark to their community. The opportunities grew, and the people pursued ideas for a better tomorrow.\n\nAfter a few decades, the village, known for its openness, gained quite a reputation even outside of the peninsula, and was reached by a group of refugees from the south, survivors of the wrath of the herds. Taking a lesson from the help their ancestors received from {color=#f6d6bd}Gale Rocks{/color}, the people of {color=#f6d6bd}Creeks{/color} embraced those travelers, helping them find a new home."
            menu:
                '[custom4][custom5][custom1][custom2][custom3]
                '
                '(continue)':
                    jump epilogue_alt_slides_galerocks


    label epilogue_alt_slides_galerocks:
        if not galerocks_firsttime:
            jump epilogue_alt_slides_shortcut
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ endcredits_counter += 1
        show areapicture ep_14 at basicfade
        if anti_epilogue_peace_tier == 0:
            $ custom1 = "The soil of {color=#f6d6bd}Gale Rocks{/color} couldn’t provide for the village’s hard-working people with crops alone. Groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
        elif anti_epilogue_peace_tier == 1:
            if quest_galerockssupport == 4 or quest_galerockssupport == 3:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} remained loyal to {color=#f6d6bd}Glaucia{/color}, making the peninsula even more infamous. Facing hunger, groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
            else:
                $ custom1 = "The soil of {color=#f6d6bd}Gale Rocks{/color} couldn’t provide for the village’s hard-working people with crops alone. Groups of fishers were forced to seek game meat and fruits, but their lack of experience made them perish among the hungry, untamed forests and hills.\n\nLike many times before, the ancient tribe dwindled in the face of struggle, but, holding to its faith and stubbornness, survived long enough to see another dawn."
        elif anti_epilogue_peace_tier == 2:
            if quest_galerockssupport == 4 or quest_galerockssupport == 3:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} remained loyal to {color=#f6d6bd}Glaucia{/color}, making the peninsula even more infamous. However, they needed little, and by selling their excess fish and salt to their neighbors, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
            else:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} needed little, and by selling their excess fish and salt to their neighbors, they received enough crops and tools to prosper, sticking to their familiar edge of the world. In the years to come, their days were good, and, for the most part, remained the same."
        elif anti_epilogue_peace_tier == 3:
            if description_greenmountaintribe10:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} needed little, and by selling their excess fish and salt to their neighbors, they received enough crops and tools to prosper. After a few more years, they gathered enough wood and weapons to start organizing their own trading expeditions - not just a few humble carts, like in the past, but rather proper caravans, guarded well enough to reach any edge of the province.\n\nThanks to the supplies the traders brought back north, the tribes could experience both safety and luxury, and the experienced guards were well-prepared to patrol the northern trail.\n\nIn the years to come, the days were good, and the hard-working fishers could spend every fifth day resting - for the first time since {color=#f6d6bd}Hovlavan{/color} pillaged {color=#f6d6bd}The Tribe of The Green Mountain{/color}."
            else:
                $ custom1 = "The people of {color=#f6d6bd}Gale Rocks{/color} needed little, and by selling their excess fish and salt to their neighbors, they received enough crops and tools to prosper. After a few more years, they gathered enough wood and weapons to start organizing their own trading expeditions - not just a few humble carts, like in the past, but rather proper caravans, guarded well enough to reach any edge of the province.\n\nThanks to the supplies the traders brought back north, the tribes could experience both safety and luxury, and the experienced guards were well-prepared to patrol the northern trail.\n\nIn the years to come, the days were good, and the hard-working fishers could spend every fifth day resting - for the first time in generations."
        menu:
            '[custom1][custom2][custom3]
            '
            '(continue)':
                jump epilogue_alt_slides_shortcut


    label epilogue_alt_slides_shortcut:
        if not shortcut_traveled:
            jump epilogue_alt_slides_eudocia
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        if anti_epilogue_peace_tier <= 2:
            $ custom1 = "The locals were even more hesitant to clear the dangerous, though convenient, paths. The heart of the forest soon sealed their remains, reclaiming its primeval shape."
            show areapicture ep_15a at basicfade
        elif anti_epilogue_peace_tier == 3:
            $ custom1 = "After a few years, the road leading through the heart of the forest was restored - though with difficulty. It helped to connect the new hamlet set at the eastern watchtower with the rest of the peninsula, but it was never seen as a safe route - just a quick one."
            show areapicture ep_15b at basicfade
        if asterion_lie == "monsters" and anti_epilogue_village_tulia_fate == "city":
            $ custom2 = "\n\nOne day, a young man came to the peninsula looking for {color=#f6d6bd}Asterion{/color}. Then, following the tale he had heard from a disgraced soldier years prior, he entered the wilderness, hoping to find the monster that was responsible for his father’s disappearance. Some claim that he is roaming the woods to this day."
        elif asterion_lie == "bandits" and anti_epilogue_village_tulia_fate == "city":
            $ custom2 = "\n\nOne day, a young man came to the peninsula looking for {color=#f6d6bd}Asterion{/color}. Then, following the tale he had heard from a disgraced soldier years prior, he entered the wilderness, hoping to find the band that was responsible for his father’s disappearance. Some claim that he is roaming the woods to this day."
        elif asterion_lie == "solitude" and anti_epilogue_village_tulia_fate == "city":
            $ custom2 = "\n\nOne day, a young man came to peninsula looking for {color=#f6d6bd}Asterion{/color}. Then, following the tale he had heard from a disgraced soldier years prior, he entered the wilderness, hoping to find the place where his father had been hiding. Some claim that he is roaming the woods to this day."
        if banditshideout_firsttime:
            if glaucia_willreturntogalerocks:
                $ custom3 = "\n\nAfter returning home to meet with her parents, {color=#f6d6bd}Glaucia{/color} took responsibility for breaking the trust of her tribe. She joined the fishers, and while she wasn’t eager to follow orders instead of giving them, she rarely raised her voice. She often wandered the beach by herself, despite the roaming saurians and harpies - after a few violent clashes, they learned to stay out of her way."
            elif quest_galerockssupport == 2:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} kept fighting on her own - though only briefly. She tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}, but once her supplies ran short, she got reckless, and, after a few seasons, was killed by a lucky arrow."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} refused to abandon her new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                else:
                    $ custom3 = "\n\nWhile she no longer had her tribe’s support, {color=#f6d6bd}Glaucia{/color} refused to abandon her new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few seasons, but once her supplies ran short, she got reckless, and got caught by the village guards. She died with her sickle sword in her hand."
            elif quest_galerockssupport == 4 or quest_galerockssupport == 3 or quest_galerockssupport == 1:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} kept fighting. For years she tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                    if anti_epilogue_village_selected == "bandits" and anti_epilogue_village_tulia_fate == "bandits":
                        $ endgame_epilogue_fluff = "spent the next few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. Their days were harsh, but thanks to the friendship they shared with {color=#f6d6bd}Tulia{/color}, they were able to survive the final, brutal clash. They both left the peninsula for good, this time under new names."
                    elif anti_epilogue_village_selected == "bandits":
                        if pc_goal == "iwanttostartanewlife":
                            $ endgame_epilogue_fluff = "spent their remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                        else:
                            $ endgame_epilogue_fluff = "spent their remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. The camaraderie they’d shared helped them reach their end in dignity, no matter how brutal it turned out to be."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}. After bothering them for years, she lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if anti_epilogue_village_selected == "bandits" and anti_epilogue_village_tulia_fate == "bandits":
                        $ endgame_epilogue_fluff = "spent the next few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the necromancers. Their days were harsh, but both they and {color=#f6d6bd}Tulia{/color} remained in good health due to the friendship they shared.\n\nOnce their leader traveled south, the once-roadwarden and once-lieutenant assisted her at first, but then traveled into the darker parts of the province and - under new names - formed a decent group of pathfinders."
                    elif anti_epilogue_village_selected == "bandits":
                        if pc_goal == "iwanttostartanewlife":
                            $ endgame_epilogue_fluff = "spent their remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the necromancers. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                        else:
                            $ endgame_epilogue_fluff = "spent their remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the necromancers. The camaraderie they’d shared helped them reach their end in dignity, no matter how brutal it turned out to be."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                    if anti_epilogue_village_selected == "bandits" and anti_epilogue_village_tulia_fate == "bandits":
                        $ endgame_epilogue_fluff = "was among the bandits captured by the guards of {color=#f6d6bd}Howler’s Dell{/color}, but thanks to the desperate distraction caused by {color=#f6d6bd}Tulia{/color} - loyal to the end - the roadwarden was able to flee into the woods, alone. They left the peninsula for good, this time under a new name."
                    elif anti_epilogue_village_selected == "bandits":
                        $ endgame_epilogue_fluff = "was among the bandits captured by the guards of {color=#f6d6bd}Howler’s Dell{/color}. Stripped of their possessions and their mount, they perished before they crossed {color=#f6d6bd}Hag Hills{/color}."
                else:
                    $ custom3 = "\n\nHaving the support of her tribe, {color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few years, but lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                    if anti_epilogue_village_selected == "bandits" and anti_epilogue_village_tulia_fate == "bandits":
                        $ endgame_epilogue_fluff = "spent the next few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against {color=#f6d6bd}Howler’s Dell{/color}. Their days were harsh, but both they and {color=#f6d6bd}Tulia{/color} remained in good health due to the friendship they shared.\n\nOnce their leader traveled south, the once-roadwarden and once-lieutenant assisted her at first, but then traveled into the darker parts of the province and - under new names - formed a decent group of pathfinders."
                    elif anti_epilogue_village_selected == "bandits":
                        if pc_goal == "iwanttostartanewlife":
                            $ endgame_epilogue_fluff = "lost their palfrey during one of the raids against {color=#f6d6bd}Howler’s Dell{/color}, but in return was the only bandit invited by {color=#f6d6bd}Glaucia{/color} to cross {color=#f6d6bd}Hag Hills{/color} with her. They had no other choice but to look for a new life once again."
                        else:
                            $ endgame_epilogue_fluff = "lost their palfrey during one of the raids against {color=#f6d6bd}Howler’s Dell{/color}, but in return was the only bandit invited by {color=#f6d6bd}Glaucia{/color} to cross {color=#f6d6bd}Hag Hills{/color} with her. They had no other choice but to look for a new life."
            else:
                if whitemarshes_destroyed:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} kept fighting. For years she tried to stop the growing plague of undead, but, severely outnumbered, died of an infected wound."
                    if anti_epilogue_village_selected == "bandits":
                        $ endgame_epilogue_fluff = "spent their remaining few years among the bandits, assisting {color=#f6d6bd}Glaucia{/color} in her war against the undead. While their days were just as brutal as their end, their strength and responsibilities were enough to make them forget about their past."
                elif not whitemarshes_nomoreundead:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} kept raiding the people of {color=#f6d6bd}White Marshes{/color}. After bothering them for years, she lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
                elif thais_rumor_glaucia_found:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. However, the villagers, thanks to the roadwarden, knew exactly where to find her, and managed to execute her in her own camp."
                else:
                    $ custom3 = "\n\n{color=#f6d6bd}Glaucia{/color} found herself a new target - the people of {color=#f6d6bd}Howler’s Dell{/color}. She bothered them for a few years, but lost most of her companions to blades, claws, and illnesses. Ashamed of her weakness, she left her camp one spring dawn - never to return."
        menu:
            '[custom1][custom2][custom3][custom4]
            '
            '(continue)':
                jump epilogue_alt_slides_eudocia


    label epilogue_alt_slides_eudocia:
        if not eudocia_inside_firsttime:
            jump epilogue_alt_slides_greenmountain
        $ endcredits_counter += 1
        if eudocia_bronzerod_installed < 6 or anti_epilogue_peace_tier <= 1:
            if eudocia_friendship < eudocia_friendship_tierlevel:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color}, bored with having nothing to challenge her, spent many days locked in her house, meeting no one, even if they came to see her. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} was nowhere to be found."
                show areapicture ep_16b at basicfade
            else:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color}, bored with having nothing to challenge her, spent many days locked in her house, meeting hardly anyone. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nBut a few years later, the memories of her conversations with the two roadwardens sprouted into an uncanny craving. She started to open her gate more often, agreeing to welcome the sparse expeditions sent by the tribes, and in the final decade of her life she even used her golems to roam the overgrown roads, visiting every village and examining the ruins scattered across the North."
                show areapicture ep_16b at basicfade
        elif quest_eudociaflower_description03:
            $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored and having all the resources she needed, she sought joy in her work, sharpening her senses with snake bait, day after day, until her heart stopped beating a year later.\n\nSoon, her residence became overrun with beasts that made nothing of the motionless stone sentinels."
            show areapicture ep_16a at basicfade
        elif not eudocia_about_flower_refusal and not quest_eudociaflower_description03:
            $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she spent many days locked in her house, meeting no one, even if they came to see her. Often, the food delivered to her was left to rot in the barrel, right where it was dropped.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} was nowhere to be found."
            show areapicture ep_16a at basicfade
        elif anti_epilogue_peace_tier == 2:
            if eudocia_friendship < eudocia_friendship_tierlevel:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} had refused to “bother with the place outside.”"
                show areapicture ep_16b at basicfade
            else:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders.\n\nHer conversations with the latest roadwarden, and the memories of {color=#f6d6bd}Asterion{/color}, sprouted into an uncanny craving. She started to pay visits to the villages of the North, getting to know the people better, though she was more interested in watching them from above her mug than chatting. Still, she bothered no one, and was welcomed by most.\n\nIn the last decade of her life she met with many adventurers, curiously listening to their tales as she filled their equipment with pneuma."
                show areapicture ep_16b at basicfade
        elif anti_epilogue_peace_tier == 3:
            if eudocia_friendship < eudocia_friendship_tierlevel:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders. She had difficulties accepting the changes occurring in the North, finding even more reason to stay out of it all.\n\nAfter a few decades, a group of adventurers reached her house to ask her for help. They told stories of the many wonders they saw, but claimed that {i}the witch{/i} had refused to “bother with the place outside.”"
                show areapicture ep_16b at basicfade
            else:
                $ custom1 = "{color=#f6d6bd}Eudocia{/color} put the bronze rods to use, sending her creations beyond the boundaries of her sight. Bored with work and having all the resources she needed, she was often tempted to reach for snake bait, but instead started to tag along with her golems, observing the peninsula from their shoulders.\n\nHer conversations with the latest roadwarden, and memories of {color=#f6d6bd}Asterion{/color}, sprouted into an uncanny craving. She started to pay visits to the villages of the North, getting to know the people better, though she was more interested in watching them from above her mug than chatting. Still, she bothered no one, and was welcomed by most.\n\nSeeking ways to expand her knowledge of enchanting, she looked into the old tales, exploring desolate ruins set among and beyond {color=#f6d6bd}Hag Hills{/color} in search of the rare materials and rituals of the past. Her name became known even in the city, and she agreed - cautiously - to chat with the visiting adventurers, listening to their tales as she filled their equipment with pneuma.\n\nShe reached her end after many years, caught by a ghoul in a magnificent cavern, but by that point, her residence was far from being {i}secluded{/i} or {i}lonely{/i}."
                show areapicture ep_16b at basicfade
        menu:
            '[custom1]
            '
            '(continue)':
                jump epilogue_alt_slides_greenmountain


    label epilogue_alt_slides_greenmountain:
        if not greenmountaintribe_firsttime:
            jump epilogue_alt_slides_pc1
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        if greenmountaintribe_banned or not cephasgaiane_available:
            show areapicture ep_17a at basicfade
            if quest_gatheracrew:
                $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence.\n\nTwo centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a prospering hamlet built on the ruins just at the foot of the volcano."
            else:
                $ custom1 = "The trail leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color} was reclaimed by the woods, and after a few generations, people forgot about the village’s existence."
        else:
            show areapicture ep_17b at basicfade
            if quest_gatheracrew:
                $ custom2 = "\n\nTwo centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a prospering hamlet built on the ruins just at the foot of the volcano."
            if anti_epilogue_peace_tier == 0:
                $ custom1 = "While {color=#f6d6bd}The Tribe of The Green Mountain{/color} wasn’t keen on restoring its relationship with other villages, {color=#f6d6bd}Cephas{/color} kept sending out patrols, observing the land from a distance. Seeing the progressing isolation of the tribes and the overgrowing valley of {color=#f6d6bd}Hag Hills{/color}, {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, putting their comfort above security."
            elif anti_epilogue_peace_tier == 1:
                $ custom1 = "While {color=#f6d6bd}The Tribe of The Green Mountain{/color} wasn’t keen on restoring its relationship with other villages, {color=#f6d6bd}Cephas{/color} kept sending out patrols, observing the land from a distance. Seeing the progressing isolation of the tribes and the overgrowing valley of {color=#f6d6bd}Hag Hills{/color}, {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, putting their comfort above security. Then, they occupied the eastern watchtower, setting up a convenient route for their hunters."
            elif anti_epilogue_peace_tier == 2:
                if quest_greenmountainsupport == 2 or quest_greenmountainsupport == 3 or cephasgaiane_about_highisland_permission:
                    $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} was relieved to see that, with the passage of time, not much had changed in the North. {color=#f6d6bd}Cephas{/color} kept sending out patrols, observing the land and its inhabitants. Encouraged by the recent trust that their leaders had shown to the {i}radarden{/i}, the hunters and pathfinders were once again knocking at the gates of the northern villages. Still, they were instructed to never visit the same place more than once a year.\n\nSoon after, {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, and then another one, surrounding the eastern watchtower with a new wooden wall."
                else:
                    $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} was relieved to see that, with the passage of time, not much had changed in the North. {color=#f6d6bd}Cephas{/color} kept sending out patrols, observing the land from a distance, but still distrusting his neighbors. {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, putting their comfort above security. Then, they occupied the eastern watchtower, setting up a convenient route for their hunters."
            elif anti_epilogue_peace_tier == 3:
                if quest_greenmountainsupport == 2 or quest_greenmountainsupport == 3 or cephasgaiane_about_highisland_permission:
                    $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} was surprised to learn that their northern neighbors had formed a prospering alliance, while at the same time the cityfolk had not influenced their shared direction. {color=#f6d6bd}Cephas{/color} wasn’t too interested in joining the negotiations, but kept sending out patrols, observing the land and its inhabitants.\n\nEncouraged by the recent trust that their leaders had shown to the {i}radarden{/i}, the hunters and pathfinders were once again knocking at the gates of the northern villages, and after discovering that {color=#f6d6bd}Thais{/color} faced the consequences of her actions, the first friendships started to bloom.\n\nSoon after, {color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, and then another one, surrounding the eastern watchtower with a new wooden wall."
                    if quest_gatheracrew:
                        $ custom2 = " Two centuries later, when the explorers of {color=#f6d6bd}Hovlavan{/color} reached {color=#f6d6bd}High Island{/color}, they were surprised to discover a large village established among the ruins just at the foot of the volcano. The dwellers were the offspring of all the tribes living in the peninsula - turns out, the Northerners are great at keeping secrets."
                else:
                    $ custom1 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} was surprised to learn that their northern neighbors had formed a prospering alliance, while at the same time the cityfolk had not influenced their shared direction. {color=#f6d6bd}Cephas{/color} wasn’t too interested in joining these discussions, but kept sending out patrols, observing the land and its inhabitants.\n\n{color=#f6d6bd}The Tribe{/color} built its first hamlet by the river, putting their comfort above security. Then, they occupied the eastern watchtower, setting up a convenient route for their hunters. It did lead to a few conflicts with the other locals, but no blood was shed."
        menu:
            '[custom1][custom2]
            '
            '(continue)':
                jump epilogue_alt_slides_pc1


    label epilogue_alt_slides_pc1:
        $ endcredits_counter += 1
        if anti_epilogue_village_selected == "monastery":
            $ anti_epilogue_pc_survived = 1
            if anti_epilogue_peace_tier <= 1:
                show areapicture ep_10a at basicfade
            else:
                show areapicture ep_10b at basicfade
            if pc_goal == "iwanttohelp":
                $ custom1 = " abandoned their previous aspirations, as well as their path of a roadwarden. Instead, they stood with the monks of {color=#f6d6bd}The Library in Stone{/color}, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks."
            if pc_goal == "iwanttoberemembered":
                $ custom1 = " abandoned their previous aspirations, as well as their path of a roadwarden. Instead, they stood with the monks of {color=#f6d6bd}The Library in Stone{/color}, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks."
            if pc_goal == "iwantstatus":
                $ custom1 = " abandoned their previous aspirations, as well as their path of a roadwarden. Instead, they stood with the monks of {color=#f6d6bd}The Library in Stone{/color}, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks."
            if pc_goal == "iwantmoney":
                $ custom1 = " abandoned their previous aspirations, as well as their path of a roadwarden. Instead, they stood with the monks of {color=#f6d6bd}The Library in Stone{/color}, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks."
            if pc_goal == "ineedmoney":
                if anti_epilogue_peace_tier >= 2:
                    $ custom1 = " and their sibling kept a low profile and took on new names, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks together with the monks of {color=#f6d6bd}The Library in Stone{/color}. By the time the {i}debt collectors{/i} found them, The Order was ready to stand in their defense."
                else:
                    $ custom1 = " and their sibling kept a low profile and took on new names, finding peace in the merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks together with the monks of {color=#f6d6bd}The Library in Stone{/color}. The {i}debt collectors{/i} never found them."
            if pc_goal == "iwanttostartanewlife":
                if anti_epilogue_peace_tier >= 2:
                    $ custom1 = " spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks. Whenever a new pilgrim showed up at the gates, one of the monks hid in the darkest cave, afraid their past might still catch up with them."
                else:
                    $ custom1 = " spent many years with the monks of {color=#f6d6bd}The Library in Stone{/color}, getting lost in their merciless dance of repetition, hiding among the prayers, songs, and tiresome tasks. They never had to confront their past, and died of old age, forgotten by all."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1]
                '
                '(end the game)':
                    jump endingtransition_alt
        elif anti_epilogue_village_selected == "bandits":
            if anti_epilogue_peace_tier <= 2:
                show areapicture ep_15a at basicfade
            else:
                show areapicture ep_15b at basicfade
            if pc_goal == "iwanttohelp" or pc_goal == "iwanttoberemembered" or pc_goal == "iwantstatus" or pc_goal == "iwantmoney":
                $ custom1 = " abandoned their previous aspirations, as well as their path of a roadwarden. They"
            if pc_goal == "ineedmoney":
                if anti_epilogue_peace_tier >= 2:
                    $ custom1 = " and their sibling kept a low profile and took on new names. By the time the {i}debt collectors{/i} found them, their new band was ready to stand in their defence.\n\nThey"
                else:
                    $ custom1 = " and their sibling kept a low profile and took on new names. The {i}debt collectors{/i} never found them.\n\nThey"
            if pc_goal == "iwanttostartanewlife":
                $ custom1 = " found a way to escape their past. They"
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1] [endgame_epilogue_fluff]
                '
                '(end the game)':
                    jump endingtransition_alt
        else:
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
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
            if anti_epilogue_peace_tier == 0:
                $ custom1 = "The peninsula became even more desolate, and remained that way for centuries."
            elif anti_epilogue_peace_tier == 1:
                $ custom1 = "The peninsula faced difficulties, but the roadwarden struggled even more."
            elif anti_epilogue_peace_tier == 2:
                $ custom1 = "While the peninsula’s security was growing, the roadwarden still had to face many obstacles."
            else:
                $ custom1 = "The peninsula’s security was growing, and the patrols made the paths safer for most - but not exactly for the lone roadwarden."
            if not glaucia_willreturntogalerocks:
                $ custom5 = "the bandits on the loose, "
                $ custom7 = ","
            if not whitemarshes_nomoreundead:
                $ custom6 = "the threat posed by the undead, "
                $ custom7 = ","
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
                $ custom2 = "Thankfully, being an experienced fighter, the rider was able to get away from most obstacles unscathed"
                if epilogue_bonus_equipment_points >= 10:
                    $ epilogue_bonus_equipment_tier = 3
                    $ custom3 = ", and their impressive equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 7:
                    $ epilogue_bonus_equipment_tier = 2
                    $ custom3 = ", and their fine equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 4:
                    $ epilogue_bonus_equipment_tier = 1
                    $ custom3 = ", though their lacking equipment wasn’t much of a help."
                else:
                    $ epilogue_bonus_equipment_tier = 0
                    $ custom3 = ", though their poor equipment was a bit of a hindrance."
                if item_asterionwine and item_asterionwine_pcknows_2:
                    if coins >= 60:
                        $ epilogue_bonus_savings_tier = 2
                        $ custom4 = "Not only that, but their unusual wealth also allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                    elif coins >= 30:
                        $ epilogue_bonus_savings_tier = 1
                        $ custom4 = "Not only that, but their significant wealth also allowed them to use the help of healers, innkeeps, and guards."
                    else:
                        $ epilogue_bonus_savings_tier = 0
                        $ custom4 = "Still, they had to use the help of others sparingly, counting every dragon bone."
                else:
                    if coins >= 100:
                        $ custom4 = "Not only that, but their unusual wealth also allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 2
                    elif coins >= 60:
                        $ custom4 = "Not only that, but their significant wealth also allowed them to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 1
                    else:
                        $ custom4 = "Still, they had to use the help of others sparingly, counting every dragon bone."
                        $ epilogue_bonus_savings_tier = 0
            elif (pc_battlecounter >= 9 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 29 and item_sharpeningpotion_used == day):
                $ epilogue_bonus_equipment_points += 1
                $ custom2 = "Thankfully, being a decent fighter, the rider was able to get away from many obstacles mostly unscathed"
                if epilogue_bonus_equipment_points >= 10:
                    $ epilogue_bonus_equipment_tier = 3
                    $ custom3 = ", and their impressive equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 7:
                    $ epilogue_bonus_equipment_tier = 2
                    $ custom3 = ", and their fine equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 4:
                    $ epilogue_bonus_equipment_tier = 1
                    $ custom3 = ", though their lacking equipment wasn’t much of a help."
                else:
                    $ epilogue_bonus_equipment_tier = 0
                    $ custom3 = ", though their poor equipment was a bit of a hindrance."
                if item_asterionwine and item_asterionwine_pcknows_2:
                    if coins >= 60:
                        $ epilogue_bonus_savings_tier = 2
                        $ custom4 = "Not only that, but their unusual wealth also allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                    elif coins >= 30:
                        $ epilogue_bonus_savings_tier = 1
                        $ custom4 = "Not only that, but their significant wealth also allowed them to use the help of healers, innkeeps, and guards."
                    else:
                        $ epilogue_bonus_savings_tier = 0
                        $ custom4 = "Still, they had to use the help of others sparingly, counting every dragon bone."
                else:
                    if coins >= 100:
                        $ custom4 = "Not only that, but their unusual wealth also allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 2
                    elif coins >= 60:
                        $ custom4 = "Not only that, but their significant wealth also allowed them to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 1
                    else:
                        $ custom4 = "Still, they had to use the help of others sparingly, counting every dragon bone."
                        $ epilogue_bonus_savings_tier = 0
            else:
                $ custom2 = "Struggling in combat, the rider wasn’t always able to get away from those obstacles"
                if epilogue_bonus_equipment_points >= 10:
                    $ epilogue_bonus_equipment_tier = 3
                    $ custom3 = ", but their impressive equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 7:
                    $ epilogue_bonus_equipment_tier = 2
                    $ custom3 = ", but their fine equipment kept them in one piece whenever their skills were lacking."
                elif epilogue_bonus_equipment_points >= 4:
                    $ epilogue_bonus_equipment_tier = 1
                    $ custom3 = ", and their lacking equipment wasn’t much of a help."
                else:
                    $ epilogue_bonus_equipment_tier = 0
                    $ custom3 = ", and their poor equipment was yet another hindrance."
                if item_asterionwine and item_asterionwine_pcknows_2:
                    if coins >= 60:
                        $ epilogue_bonus_savings_tier = 2
                        $ custom4 = "At least their unusual wealth allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                    elif coins >= 30:
                        $ epilogue_bonus_savings_tier = 1
                        $ custom4 = "At least their significant wealth allowed them to use the help of healers, innkeeps, and guards."
                    else:
                        $ epilogue_bonus_savings_tier = 0
                        $ custom4 = "Not only that, but they also had to use the help of others sparingly, counting every dragon bone."
                else:
                    if coins >= 100:
                        $ custom4 = "At least their unusual wealth allowed them to gather better tools, and to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 2
                    elif coins >= 60:
                        $ custom4 = "At least their significant wealth allowed them to use the help of healers, innkeeps, and guards."
                        $ epilogue_bonus_savings_tier = 1
                    else:
                        $ custom4 = "Not only that, but they also had to use the help of others sparingly, counting every dragon bone."
                        $ epilogue_bonus_savings_tier = 0
            menu:
                '[custom1] With [custom5][custom6][custom8][custom9][custom10]hardly any travelers[custom7] and the roaming beasts, the roads remained a challenge to follow.
                \n\n[custom2][custom3] [custom4]
                '
                '(continue)':
                    jump epilogue_alt_slides_pc2


    label epilogue_alt_slides_pc2:
        $ endcredits_counter += 1
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
        if glaucia_about_galerocksdecision_liedto:
            if (anti_epilogue_peace_tier >= 2 and anti_epilogue_village_selected == "galerocks") or anti_epilogue_peace_tier >= 3:
                $ custom1 = "Once {color=#f6d6bd}Glaucia{/color} learned about the roardwarden’s lie, her anger threw her into a cruel pursuit. She managed to catch them in a trap, right next to the old tunnel, but was then stopped by her own tribesfolk. After a tense dispute, she agreed to let the rider go, though warned them to never be in her sight again.\n\n"
            elif epilogue_bonus_equipment_tier >= 3 or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2):
                $ custom1 = "Once {color=#f6d6bd}Glaucia{/color} learned about the roardwarden’s lie, her anger threw her into a cruel pursuit. She managed to catch them in a trap, right next to the old tunnel, and even wound them, but her enemy turned out to be better prepared than she expected. After a grim clash, she agreed to let the rider go in exchange for her companion’s life, though she warned them to never be in her sight again.\n\n"
            elif anti_epilogue_pc_survival_deathcause == 0:
                $ anti_epilogue_pc_survival_deathcause = "glaucia"
                $ custom1 = ""
                $ anti_epilogue_pc_survival_deathdescription = "Once {color=#f6d6bd}Glaucia{/color} learned about the roardwarden’s lie, her anger threw her into a cruel pursuit. She caught them in a trap, right next to the old tunnel, and after a brief exchange, she ended their life with a single cut of her sword."
            else:
                $ custom1 = "Once {color=#f6d6bd}Glaucia{/color} learned about the roardwarden’s lie, her anger threw her into a cruel pursuit. She managed to catch them in a trap, right next to the old tunnel, and severely wounded them. The rider was lucky to get away, though their pursuer warned them to never be in her sight again.\n\n"
        if (anti_epilogue_peace_tier < 3 and quest_ruins_choice == "thais_won") or (anti_epilogue_peace_tier < 3 and quest_ruins_choice == "thais_alliance_fail"):
            $ anti_epilogue_pc_survival_deathcause = "thais_bounty"
            $ custom2 = ""
            $ anti_epilogue_pc_survival_deathdescription = "After a few years, the news of the roadwarden’s betrayal reached the city officials, and a group of bounty hunters began their search right away. Finding the rider would have been difficult if it wasn’t for {color=#f6d6bd}Thais{/color}, who was happy to split the reward.\n\nThey caught the roadwarden on their next visit in {color=#f6d6bd}Howler’s Dell{/color}. They didn’t bother with keeping their captive alive, but spared the expensive palfrey."
        elif anti_epilogue_peace_tier >= 2:
            $ custom2 = "After a few seasons, the news of the roadwarden’s betrayal reached the city officials and a group of bounty hunters began their search right away. Finding the rider presented some difficulties, but they received permission to keep all of their prey’s belongings.\n\nHowever, to their surprise, the locals were far from willing to give them any clues, and even started to threaten them. Knowing better, the hunters gave up.\n\n"
        elif epilogue_bonus_equipment_tier >= 2:
            $ custom2 = "After a few seasons, the news of the roadwarden’s betrayal reached the city officials, and a group of bounty hunters began their search right away. Finding the rider presented some difficulties, but they received permission to keep all of their prey’s belongings.\n\nHiding in the tall grass, they caught them by the western ford - but to their surprise, the roadwarden managed to get out with just a scratch, grievously wounding one of the pursuers. Knowing better, the hunters gave up.\n\n"
        elif epilogue_bonus_savings_tier >= 3:
            $ epilogue_bonus_savings_tier -= 3
            $ custom2 = "After a few seasons, the news of the roadwarden’s betrayal reached the city officials, and a group of bounty hunters began their search right away. Finding the rider presented some difficulties, but they received permission to keep all of their prey’s belongings.\n\nThe warden knew they couldn’t face such an opponent, and they generously paid a group of local brawlers for protection. After the hunters got beaten up during a stay at an inn, they abandoned their pursuit, but the roadwarden had to continue with hardly any savings left.\n\n"
        elif anti_epilogue_pc_survival_deathcause == 0:
            $ anti_epilogue_pc_survival_deathcause = "bounty"
            $ custom2 = ""
            $ anti_epilogue_pc_survival_deathdescription = "After a few years, the news of the roadwarden’s betrayal reached the city officials, and a group of bounty hunters began their search right away. Finding the rider presented some difficulties, but they received permission to keep all of their prey’s belongings.\n\nHiding in the tall grass, they caught the roadwarden by the western ford. “Pity that the horse had to die,” said their leader after executing the final strike. “We’d have got a pretty coin for it.”"
        else:
            $ custom2 = "After a few seasons, the news of the roadwarden’s betrayal reached the city officials, and a group of bounty hunters began their search right away. Finding the rider presented some difficulties, but they received permission to keep all of their prey’s belongings.\n\nHiding in the tall grass, they caught them by the western ford. The rider was just lucky enough to get away with a grievous wound, and while the hunters stayed around for some time still, they had to give up with the arrival of winter.\n\n"
        if not whitemarshes_nomoreundead:
            if anti_epilogue_village_selected == "creeks" and epilogue_bonus_equipment_tier < 2:
                $ anti_epilogue_pc_survival_deathcause = "undead_creeks"
                $ custom3 = ""
                if epilogue_bonus_equipment_tier >= 3:
                    $ anti_epilogue_pc_survival_deathdescription = "When the skeleton mage brought its undead band to {color=#f6d6bd}Creeks{/color}, the roadwarden was one of the few souls who managed to get out of the village alive. He then tried to blend in with the other tribes, preparing them for the next strike, but the grief kept their heart locked in thorns for the rest of their days."
                else:
                    $ anti_epilogue_pc_survival_deathdescription = "In the end, the roadwarden shared a few colorful seasons with the people of {color=#f6d6bd}Creeks{/color}, but they couldn’t alter the fate of their tribe, nor their own, with just their blade. Like many others, they joined the undead army."
            elif epilogue_bonus_equipment_tier >= 2 or epilogue_bonus_equipment_tier >= 1 and epilogue_bonus_savings_tier >= 3:
                $ custom3 = "Finally, the skeleton band managed to surround the rider, who just barely escaped the soulless shells. Licking their wounds, the roadwarden tried to wait out the undead horde, resuming their patrols only after the necromancer had left the peninsula for good.\n\n"
            elif anti_epilogue_pc_survival_deathcause == 0:
                $ anti_epilogue_pc_survival_deathcause = "undead"
                $ custom3 = ""
                $ anti_epilogue_pc_survival_deathdescription = "The roadwarden struggled to find their way around the growing undead horde, but the skeleton mage was much brighter than they expected. Its soldiers attacked at just the right time, surrounding the rider from all sides, and adding their shell to their ranks."
            else:
                $ custom3 = "Finally, the skeleton band managed to surround the rider, who just barely escaped from the soulless shells. Licking their wounds, the roadwarden tried to wait out the undead horde, resuming their patrols only after the necromancer had left the peninsula for good.\n\n"
        if (achievement_animalssavedpoints >= 5 and pc_religion == "pagan") or achievement_animalssavedpoints >= 7:
            $ custom4 = "Even without other threats, there were more than enough beasts to look out for. One of the patrols almost ended tragically, with the roadwarden having no other option but to ride through the night. A large, bipedal shape dropped from a tree and landed right in front of"
            $ custom6 = ", making it freeze in panic. The hunting lord gave the rider a peaceful look, as if to judge them, then let out a howl with its wolf-like head and moved aside, letting them ride forward. The warden often shared this tale, and while most people expressed disbelief, the elders mentioned it would be wise to {i}thank the spirits for their mercy{/i}."
        elif epilogue_bonus_equipment_tier >= 2 or (epilogue_bonus_equipment_tier >= 1 and epilogue_bonus_savings_tier >= 3):
            $ custom4 = "Even without other threats, there were more than enough beasts to look out for."
            $ custom6 = " struggled to outrun them all, but thanks to a mixture of luck, experience, and preparation, the roadwarden managed to stick with their trusty mount."
        elif anti_epilogue_peace_tier >= 3:
            $ custom4 = "Even without other threats, there were more than enough beasts to look out for."
            $ custom6 = " struggled to outrun them all, but thanks to the occasional patrols of the locals, the roadwarden managed to stick with their trusty mount."
        elif anti_epilogue_pc_survival_deathcause == 0:
            $ anti_epilogue_pc_survival_deathcause = "beasts"
            $ custom4 = "Even without other threats, there were more than enough beasts to look out for."
            $ custom6 = " struggled to outrun them all, and day by day, both the mount and its owner gained more scars."
            $ anti_epilogue_pc_survival_deathdescription = "In the end, it was yet another routine journey, one occurring just after dusk, that ended the roadwarden’s career. A large, bipedal shape dropped from a tree and landed right in front of the horse, making it freeze in panic. The hunting lord gave the rider a peaceful look, as if to judge them, then let out a howl with its wolf-like head and leaped forward, cutting through the heads of both the mount and its owner with a single swipe."
        else:
            $ custom4 = "Even without other threats, there were more than enough beasts to look out for."
            $ custom6 = " struggled to outrun them all, but thanks to a mixture of luck, experience, and preparation, the roadwarden managed to stick with their trusty mount."
        if anti_epilogue_village_selected == "howlersdell" and endgame_howlers_destroyed and anti_epilogue_pc_survival_deathcause == 0:
            $ anti_epilogue_pc_survival_deathcause = "howlerscolapse"
            $ anti_epilogue_pc_survival_deathdescription = "While {color=#f6d6bd}Thais{/color} wasn’t exactly happy about the roadwarden’s return, she allowed them to stay in the village, turning them into yet more muscle ready to {i}persuade{/i} any dissenters. In the end, they were one of many souls lost to the wrath of the herds."
        if not anti_epilogue_pc_survival_deathcause:
            $ custom5 = "\n\nThe days were harsh, and yet... The outsider survived."
        menu:
            '[custom1][custom2][custom3][custom4] {color=#f6d6bd}[horsename]{/color}[custom6][custom5]
            '
            '(continue)':
                if anti_epilogue_pc_survival_deathcause:
                    jump epilogue_alt_slides_pc3dead
                else:
                    jump epilogue_alt_slides_pc3alive


    label epilogue_alt_slides_pc3dead:
        $ endcredits_counter += 1
        if anti_epilogue_pc_survival_deathcause == "thais_bounty":
            show areapicture ep_08a at basicfade
        if anti_epilogue_pc_survival_deathcause == "undead_creeks":
            show areapicture ep_13a at basicfade
        if anti_epilogue_pc_survival_deathcause == "howlersdell":
            show areapicture ep_08b at basicfade
        if pc_goal == "iwanttohelp":
            if quest_pc_goal == 1 or endgame_epilogue_evil:
                $ custom1 = " tried to get used to their routine patrols, but their ever-present desire to change The Dragonwoods for the better wouldn’t leave their soul. To accomplish this, they kept looking for ways to help others - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\n"
            elif quest_pc_goal == 2:
                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. They did their best, putting their own well-being and safety above their sacrifice.\n\n"
        if pc_goal == "iwanttoberemembered":
            if quest_pc_goal == 1 or endgame_epilogue_evil:
                $ custom1 = " was convinced they could still save the North and claim the title of {i}hero{/i} that they clearly deserved. To accomplish this, they kept looking for ways to prove the strength of their will - another job here, a shared meal there, just one more kind word, just one sleepless night..."
            elif quest_pc_goal == 2:
                $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\n"
        if pc_goal == "iwantstatus":
            if quest_pc_goal == 1:
                $ custom1 = " was convinced they could still find a way to take a well-deserved spot among the village leaders, but to accomplish this, they kept looking for ways to earn even more favors and spin new intrigues. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\n"
            elif endgame_epilogue_evil:
                $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside. "
            elif quest_pc_goal == 2:
                $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside, but they managed to stick to the path that the locals saw as righteous. "
        if pc_goal == "iwantmoney":
            if quest_pc_goal == 1 or endgame_epilogue_evil:
                $ custom1 = " was convinced they could still start a prospering, safe trade in the North that would take little effort to maintain, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\n"
            elif quest_pc_goal == 2:
                $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, and keeping the quarreled tribes connected.\n\n"
        if pc_goal == "ineedmoney":
            $ custom1 = " spent the remaining few seasons in relative peace, under a new name and keeping a low profile together with their sibling. "
        if pc_goal == "iwanttostartanewlife":
            if anti_epilogue_village_selected == "creeks":
                $ custom1 = " took a new name and shelter with their found family of {color=#f6d6bd}Creeks{/color}, assisting their foragers and hunters.\n\n"
            if anti_epilogue_village_selected == "galerocks":
                $ custom1 = " took a new name and shelter with the hard-working tribe of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it.\n\n"
            if anti_epilogue_village_selected == "howlers":
                $ custom1 = " took a new name and shelter at the richest village in the North. {color=#f6d6bd}Thais{/color} was a demanding employer, but she offered a full stomach, silence, and colorful linen.\n\n"
            if anti_epilogue_village_selected == "travel":
                $ custom1 = " took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. "
        menu:
            '{color=#f6d6bd}[pcname]{/color}[custom1][anti_epilogue_pc_survival_deathdescription]
            '
            '(end the game)':
                jump endingtransition_alt


    label epilogue_alt_slides_pc3alive:
        $ endcredits_counter += 1
        $ custom1 = ""
        $ custom2 = ""
        $ custom3 = ""
        $ custom4 = ""
        $ custom5 = ""
        if pc_goal == "iwanttohelp":
            if quest_pc_goal == 1:
                if (epilogue_bonus_equipment_tier >= 3 and epilogue_bonus_savings_tier >= 2) or (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 3):
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    $ custom1 = " tried to get used to their routine patrols, but their ever-present desire to change The Dragonwoods for the better wouldn’t leave their soul. To accomplish this, they kept looking for ways to help others - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nTheir fate was predictable. After dashing forward in a bold attempt to stop a robbery, they were shot in the back from a crossbow. Those saved by them took them back to shelter, but the rider’s spine never recovered.\n\nThey saw a fine age, but their heart grew bitter, filled with dreams and questions."
                else:
                    $ anti_epilogue_pc_survived = 0
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    $ custom1 = " tried to get used to their routine patrols, but their ever-present desire to change The Dragonwoods for the better wouldn’t leave their soul. To accomplish this, they kept looking for ways to help others - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nTheir fate was predictable. After dashing forward in a bold attempt to stop a robbery, they were shot in the back from a crossbow."
            elif quest_pc_goal == 2:
                if endgame_epilogue_evil == 1:
                    if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                        $ custom1 = " tried to get used to their routine patrols, but their ever-present desire to change The Dragonwoods for the better wouldn’t leave their soul. To accomplish this, they kept looking for ways to help others, at all costs - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nThey eagerly aided the tribes, gathering friendships and help as the seasons went on. They stopped only after they had almost met their end in the middle of nowhere, shot in the back while intervening in a robbery. Those saved by them took them back to shelter, but the rider’s shell was no longer capable of staying in the saddle. Their remaining decades were spent on a mixture of hard work and sending sullen looks toward the {i}slothful{/i} youngsters."
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                    else:
                        $ anti_epilogue_pc_survived = 0
                        $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                        $ anti_epilogue_pc_survival_deathdescription = ""
                        $ custom1 = " tried to get used to their routine patrols, but their ever-present desire to change The Dragonwoods for the better wouldn’t leave their soul. To accomplish this, they kept looking for ways to help others - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nThey eagerly aided the tribes, gathering friendships and help as the seasons went on, but their fate was predictable. After dashing forward in a bold attempt to stop a robbery, they were shot in the back from a crossbow."
                else:
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    if anti_epilogue_village_selected == "howlersdell":
                        $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - following {color=#f6d6bd}Thais’s{/color} command and working to earn her forgiveness.\n\nShe was a demanding employer, bitter from the grudge she held against the roadwarden’s betrayal, but she offered a full stomach, silence, and colorful linen.\n\nAt times, it felt like they had replaced their old shadow with a new one - and it was suffocatingly comfortable."
                    elif anti_epilogue_peace_tier == 0:
                        $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "creeks":
                        if endgame_creeks_withered:
                            if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\n{color=#f6d6bd}Creeks{/color} lasted for only a few decades, but the rider’s experience played a crucial role when it came to letting their new family start anew on the other side of {color=#f6d6bd}Hag Hills{/color}."
                            else:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\n{color=#f6d6bd}Creeks{/color} lasted for only a few decades, but the rider’s experience played a crucial role when it came to letting their new family start anew on the other side of {color=#f6d6bd}Hag Hills{/color}."
                        else:
                            if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they spent their remaining lazy years as a guard and a dear friend in {color=#f6d6bd}Creeks{/color}."
                            else:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they spent their remaining lazy years as a guard in {color=#f6d6bd}Creeks{/color}."
                    elif anti_epilogue_village_selected == "galerocks":
                        if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                            $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they spent their remaining lazy years as a guard and a dear friend in {color=#f6d6bd}Gale Rocks{/color}."
                        else:
                            $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they spent their remaining lazy years as a guard in {color=#f6d6bd}Gale Rocks{/color}."
                    elif anti_epilogue_village_selected == "travel":
                        if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                            if anti_epilogue_peace_tier >= 2:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they settled at {color=#f6d6bd}Pelt of the North{/color}, spending their remaining lazy years as a guard and a dear friend."
                            else:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they had to finally select a village they could call {i}home{/i}, but they did so knowing they did the best they could."
                        else:
                            if anti_epilogue_peace_tier >= 2:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they settled at {color=#f6d6bd}Pelt of the North{/color}, spending their remaining lazy years as a guard."
                            if anti_epilogue_peace_tier >= 2:
                                $ custom1 = " abandoned their dream of helping others at all costs, understanding that they couldn’t “save” The Dragonwoods on their own. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety above their sacrifice.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nAfter a decade, with their palfrey too exhausted to continue their travels, they had to finally select a village they could call {i}home{/i}, but they did so knowing they did the best they could."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1]
                '
                '(end the game)':
                    jump endingtransition_alt
        if pc_goal == "iwanttoberemembered":
            if quest_pc_goal == 1:
                if (epilogue_bonus_equipment_tier >= 3 and epilogue_bonus_savings_tier >= 2) or (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 3):
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    $ custom1 = " was convinced they could still save the North and claim the title of {i}hero{/i} that they clearly deserved. To accomplish this, they kept looking for ways to prove the strength of their will - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nTheir fate was predictable. After landing on the ground in a bold attempt to save a traveling family from a large cat, they received grievous wounds, barely able to climb back into their saddle. Despite reaching their shelter, they lost an arm soon after.\n\nThey saw a fine age, but their heart grew bitter, filled with dreams and questions."
                else:
                    $ anti_epilogue_pc_survived = 0
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    $ custom1 = " was convinced they could still save the North and claim the title of {i}hero{/i} that they clearly deserved. To accomplish this, they kept looking for ways to prove the strength of their will - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nTheir fate was predictable. After landing on the ground in a bold attempt to save a traveling family from a large cat, they bled to death after getting dragged to the top of a tree."
            elif quest_pc_goal == 2:
                if endgame_epilogue_evil == 1:
                    if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                        $ custom1 = " was convinced they could still save the North and claim the title of {i}hero{/i} that they clearly deserved. To accomplish this, they kept looking for ways to prove the strength of their will - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nThey spent the next violent decade earning new tales and songs among the northern tribes, yet even this wasn’t enough to satiate their hunger. Lost and confused, the rider joined a crew that was meant to cross the sea, all the way toward the colonies. They, however, traveled not for wealth or glory, but for peace."
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                    else:
                        $ anti_epilogue_pc_survived = 0
                        $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                        $ anti_epilogue_pc_survival_deathdescription = ""
                        $ custom1 = " was convinced they could still save the North and claim the title of {i}hero{/i} that they clearly deserved. To accomplish this, they kept looking for ways to prove the strength of their will - another job here, a shared meal there, just one more kind word, just one sleepless night...\n\nThey spent the next few brief, violent seasons earning new tales and songs among the northern tribes, until their ever-hungry shell fed one of the hunting warlords. The rider was gone, but not forgotten."
                else:
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    if anti_epilogue_village_selected == "howlersdell":
                        $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - following {color=#f6d6bd}Thais’s{/color} command and working to earn her forgiveness.\n\nShe was a demanding employer, bitter from the grudge she held against the roadwarden’s betrayal, but she offered a full stomach, silence, and colorful linen.\n\nAt times, it felt like they had replaced their old shadow with a new one - and it was suffocatingly comfortable."
                    elif anti_epilogue_peace_tier == 0:
                        $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "creeks":
                        if endgame_creeks_withered:
                            $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\n{color=#f6d6bd}Creeks{/color} lasted for only a few decades, but the rider’s experience played a crucial role when it came to letting their new family start anew on the other side of {color=#f6d6bd}Hag Hills{/color}."
                        else:
                            if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                                $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nTheir likeness has been carved in stone, and to this day stands at the bridge leading to {color=#f6d6bd}Creeks{/color}."
                            else:
                                $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "galerocks":
                        if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                            $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nTheir likeness has been carved in stone, and to this day stands at the entrance to the stronghold of {color=#f6d6bd}Gale Rocks{/color}."
                        else:
                            $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "travel":
                        if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 2 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                            $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nTheir likeness has been carved in stone, and to this day stands by the southern crossroads."
                        else:
                            $ custom1 = " abandoned their dream of becoming {i}the hero of the North{/i}. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new neighbors. As the seasons passed by, the rider earned grateful tales and favors, putting their own well-being and safety before fame, at all times.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1]
                '
                '(end the game)':
                    jump endingtransition_alt
        if pc_goal == "iwantstatus":
            if quest_pc_goal == 1:
                if (epilogue_bonus_equipment_tier >= 3 and epilogue_bonus_savings_tier >= 2) or (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2):
                    $ custom1 = " was convinced they could still find a way to take a well-deserved spot among the village leaders, but to accomplish this, they kept looking for ways to earn even more favors and spin new intrigues. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir fate was predictable. After getting into a quarrel with a traveling merchant, they were sold a faulty rope, and fell on their leg from a great height. They managed to get to shelter, but their limb never recovered.\n\nThey saw a fine age, but their heart grew bitter, filled with dreams and questions."
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                else:
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    $ custom1 = " was convinced they could still find a way to take a well-deserved spot among the village leaders, but to accomplish this, they kept looking for ways to earn even more favors and spin new intrigues. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir fate was predictable. After getting into a quarrel with a traveling merchant, they were sold a faulty rope, and fell on their leg from a great height. Struggling to get back in the saddle, they failed to escape the wolves who were lured by the scent of blood."
            elif quest_pc_goal == 2:
                if endgame_epilogue_evil >= 2:
                    if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 3 and epilogue_bonus_savings_tier >= 2) or (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2 and epilogue_bonus_savings_tier >= 3):
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                        $ custom1 = " was a merciless player in the scene of local politics, no matter how shallow it seemed to be from the outside. As the years went by and the rider’s true nature started to reach the surface, they had to grow even more cautious, cunning, and paranoid to stay afloat. They used their good name among the villagers, fancy equipment, and bribes handsome enough to buy the services of the majority of the trained blades in the peninsula. They either silenced or eliminated their rivals.\n\nThey died from poison after a decade, a day before the feast that was meant to honor them with the title of {i}The Uniter of the North{/i}. Most souls were shocked, even terrified, but those who knew - knew."
                    else:
                        $ anti_epilogue_pc_survived = 0
                        $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                        $ anti_epilogue_pc_survival_deathdescription = ""
                        $ custom1 = " was a merciless player in the scene of local politics, no matter how shallow it seemed to be from the outside. As the years went by and the rider’s true nature started to reach the surface, they had to grow even more cautious, cunning, and paranoid to stay afloat. It was the time to either silence or eliminate their rivals.\n\nBut not everything went according to plan. The rider died in a dark valley, in a puddle of their co-conspirators’ blood. Some of the souls in the North were shocked, even terrified, but many others had a hint that such a sad end was coming."
                elif endgame_epilogue_evil == 1:
                    if (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                        $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside. As the years went by and the rider’s true nature started to reach the surface, they had to grow more cautious and cunning, using handsome bribes to buy the loyalty of the local guards.\n\nIn some ways, the plan worked. Banished by most tribes, the roadwarden found asylum in their new home, surrounded by keen eyes and firm hands. They reached a respectable age, but once their savings dried up, they were found in a latrine, with a cut throat. But at this point, no one was surprised."
                    elif (epilogue_bonus_equipment_tier >= 2 and epilogue_bonus_savings_tier >= 3):
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                        $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside. As the years went by and the rider’s true nature started to reach the surface, they had to grow more cautious and cunning while they tried to stay on the locals’ good side, using their kindness as a shield from consequences.\n\nIn some ways, the plan worked. Banished by the tribe they harmed the most, yet beloved by the others, the roadwarden reached a respectable age, and their voice was valued by many. When they were found by their table, with a dagger sticking out of their back, most souls were shocked, even terrified, but those who knew - knew."
                    else:
                        $ anti_epilogue_pc_survived = 0
                        $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                        $ anti_epilogue_pc_survival_deathdescription = ""
                        $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside. As the years went by and the rider’s true nature started to reach the surface, they had to grow more cautious and cunning while they tried to stay on the locals’ good side, using their kindness as a shield from consequences.\n\nBut not everything went according to plan. After a few comfortable years filled with intrigue and rivalry, the rider was taken captive by a group of guards, and was meant to stand in front of a jury. The charges were treason, theft, and conspiracy.\n\nThey died the next night, after they snuck out of the village and entered the woods with a stolen knife and a broomstick, sharpened into a spear."
                else:
                    $ custom1 = " was an ambitious player in the scene of local politics, no matter how shallow it seemed to be from the outside, but they managed to stick to the path that the locals saw as righteous. As the years went by, the roadwarden’s name started to carry even greater weight, granting them an honorable position at the table whenever there was a major dispute to be had.\n\nIt took a few decades before they were offered the position of a mayor, but at this point, no one was surprised with the nomination. Not every decision the rider made was correct, but they were ready to face the consequences of their actions - and once their end came to them in their sleep, they carried but a few regrets."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1]
                '
                '(end the game)':
                    jump endingtransition_alt
        if pc_goal == "iwantmoney":
            if quest_pc_goal == 1:
                if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 3):
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    $ custom1 = " was convinced they could still start a prospering, safe trade in the North that would take little effort to maintain, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir fate was predictable. After adding one bundle too many to their saddle, they failed to avoid a hungry pack of wolves, and while their sharp blade allowed them to escape, they reached their shelter with heavy wounds, and lost a leg soon after.\n\nThey saw a fine age, but their heart grew bitter, filled with dreams and questions."
                else:
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    $ custom1 = " was hoping that they could still start a prospering, safe trade in the North that would take little effort to maintain, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir end was predictable. After adding one bundle too many to their saddle, they failed to escape a hungry pack of wolves."
            elif quest_pc_goal == 2:
                if endgame_epilogue_evil == 1:
                    if (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                        $ custom1 = " was still hoping that they could start a prospering, safe outpost in the North, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir fate was predictable. After adding one bundle too many to their saddle, they failed to avoid a hungry pack of wolves, and while their sharp blade allowed them to escape, they reached their shelter with heavy wounds, and lost a leg soon after.\n\nBut since the northern tribes were also growing in luxuries as the roads were getting safer, the once-rider turned out to be truly ready. Thanks to the investments they set up at every village, they could spend their remaining years enjoying their rest, and only occasionally chatting with the caravan guides or making rather quirky requests toward passing adventurers and mercenaries.\n\nAt this point, most people wouldn’t believe it if they were told that this thriving merchant used to be a roadwarden."
                    elif epilogue_bonus_equipment_tier >= 3:
                        $ anti_epilogue_pc_survived = 1
                        if anti_epilogue_village_selected == "howlersdell":
                            show areapicture ep_08a at basicfade
                        elif anti_epilogue_village_selected == "creeks":
                            show areapicture ep_13b at basicfade
                        elif anti_epilogue_village_selected == "galerocks":
                            show areapicture ep_14 at basicfade
                        elif anti_epilogue_village_selected == "travel":
                            if anti_epilogue_peace_tier == 0:
                                show areapicture ep_07a at basicfade
                            else:
                                show areapicture ep_07b at basicfade
                        $ custom1 = " was still hoping that they could start a prospering, safe trade in the North that would take little effort to maintain, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir fate was predictable. After adding one bundle too many to their saddle, they failed to avoid a hungry pack of wolves, and while their sharp blade allowed them to escape, they reached their shelter with heavy wounds, and lost a leg soon after.\n\nThey saw a fine age, but their heart grew bitter, filled with dreams and questions."
                    else:
                        $ anti_epilogue_pc_survived = 0
                        $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                        $ anti_epilogue_pc_survival_deathdescription = ""
                        $ custom1 = " was convinced they could still start a prospering, safe trade in the North that would take little effort to maintain, but to accomplish this, they kept looking for ways to gather even greater wealth. Another job here, a saved coin there, just one more lie, just one sleepless night...\n\nTheir end was predictable. After adding one bundle too many to their saddle, they failed to escape a hungry pack of wolves."
                else:
                    $ anti_epilogue_pc_survived = 1
                    if anti_epilogue_village_selected == "howlersdell":
                        show areapicture ep_08a at basicfade
                    elif anti_epilogue_village_selected == "creeks":
                        show areapicture ep_13b at basicfade
                    elif anti_epilogue_village_selected == "galerocks":
                        show areapicture ep_14 at basicfade
                    elif anti_epilogue_village_selected == "travel":
                        if anti_epilogue_peace_tier == 0:
                            show areapicture ep_07a at basicfade
                        else:
                            show areapicture ep_07b at basicfade
                    if anti_epilogue_village_selected == "howlersdell":
                        $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - following {color=#f6d6bd}Thais’s{/color} command and working to earn her forgiveness.\n\nShe was a demanding employer, bitter from the grudge she held against the roadwarden’s betrayal, but she offered a full stomach, silence, and colorful linen.\n\nAt times, it felt like they had replaced their old shadow with a new one - and it was suffocatingly comfortable."
                    elif anti_epilogue_peace_tier == 0 or anti_epilogue_peace_tier == 1:
                        $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, keeping the quarreled tribes connected.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nFor as long as the Northerners were willing to accept their presence here, they’d stay. But they could always find home in another place, and then another - living in the moment."
                    elif anti_epilogue_village_selected == "creeks":
                        if endgame_creeks_withered:
                            $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\n{color=#f6d6bd}Creeks{/color} lasted for only a few decades, but the rider’s savings played a crucial role when it came to letting their new family start anew on the other side of {color=#f6d6bd}Hag Hills{/color}."
                        else:
                            $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe.\n\nWhile they held onto their savings for a few seasons, they finally decided to invest them in their new family - the people they had put above their own luxury. Thanks to the sack of seeds and iron tools that they brought to the village, {color=#f6d6bd}Creeks{/color} was able to enter the next part of their journey smoothly.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "galerocks":
                        if anti_epilogue_peace_tier < 3:
                            $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe.\n\nWhile they held onto their savings for a few seasons, they finally decided to invest them in their new neighbors - the people they had put above their own luxury. By bringing home a few ingots of copper and iron, they allowed {color=#f6d6bd}Gale Rocks{/color} to make their own tools, nails, and blades, and to enter the next part of their journey smoothly.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                        elif anti_epilogue_peace_tier == 3:
                            $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, protecting their new tribe.\n\nWhile they held onto their savings for a few seasons, they finally decided to invest them in their new neighbors - the people they had put above their own luxury. By allowing the newly born caravan to equip itself with a few more sets of jackets and spears, they were able to return from their first journey almost unscathed. {color=#f6d6bd}Gale Rocks{/color} could enter the next part of their journey smoothly.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud."
                    elif anti_epilogue_village_selected == "travel":
                        $ custom1 = " abandoned their dream of finding a way to live without risk and effort. Instead, they focused on the matters at hand - looking after their mount, patrolling the desolate paths, keeping the quarreled tribes connected. They put their present before the future - they slept when they needed to, ate as well as they could afford, and always had a pouch of coins “just in case”, though it was usually spent on potions and the help of healers.\n\nIt was a harsh life, and far from the one they were hoping for, but their eyes and thoughts were clear, as if they had stepped out of a poisonous cloud.\n\nFor as long as the Northerners were willing to accept their presence here, they’d stay. But they could always find home in another place, and then another - living in the moment."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom1]
                '
                '(end the game)':
                    jump endingtransition_alt
        if pc_goal == "ineedmoney":
            if endgame_epilogue_evil >= 2:
                if epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 3:
                    menu:
                        '{color=#f6d6bd}[pcname]{/color} spent their remaining two years in relative peace, under a new name and keeping a low profile. But, after one of their patrols, they discovered that their dearest family member was nowhere to be found. According to their surprised neighbors, a group of portly travelers had arrived just two days earlier, and the sibling had left with them {i}willingly{/i}, saying that {i}they didn’t want {color=#f6d6bd}[pcname]{/color} to look for them{/i}, for the {i}debt was now paid{/i}.
                        \n\nBut the roadwarden wasn’t the same soul anymore, and had both experience and friends to lean on. While the rider scouted ahead, their companions were right behind them, ready for the final clash with the bounty hunters from {color=#f6d6bd}Hovlavan{/color}.
                        '
                        '(end the game)':
                            jump endingtransition_alt
                else:
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    menu:
                        '{color=#f6d6bd}[pcname]{/color} spent their remaining two years in relative peace, under a new name and keeping a low profile. But, after one of their patrols, they discovered that their dearest family member was nowhere to be found. According to their surprised neighbors, a group of portly travelers had arrived just two days earlier, and the sibling had left with them {i}willingly{/i}, saying that {i}they didn’t want {color=#f6d6bd}[pcname]{/color} to look for them{/i}, for the {i}debt was now paid{/i}.
                        \n\nThe rider prepared their equipment and left soon after, ready to face the dark corners of {color=#f6d6bd}Hovlavan{/color} one last time.
                        '
                        '(end the game)':
                            jump endingtransition_alt
            elif endgame_epilogue_evil == 1:
                if (epilogue_bonus_equipment_tier >= 3 and anti_epilogue_peace_tier >= 2) or (epilogue_bonus_equipment_tier >= 2 and anti_epilogue_peace_tier >= 3):
                    menu:
                        '{color=#f6d6bd}[pcname]{/color} spent their remaining two years in relative peace, under a new name and keeping a low profile. But, after one of their patrols, they discovered that their dearest family member was nowhere to be found. According to their surprised neighbors, a group of portly travelers had arrived just two days earlier, and the sibling had left with them {i}willingly{/i}, saying that {i}they didn’t want {color=#f6d6bd}[pcname]{/color} to look for them{/i}, for the {i}debt was now paid{/i}.
                        \n\nBut the roadwarden wasn’t the same soul anymore, and had both experience and friends to lean on. While the rider scouted ahead, their companions were right behind them, ready for the final clash with the bounty hunters from {color=#f6d6bd}Hovlavan{/color}.
                        '
                        '(end the game)':
                            jump endingtransition_alt
                else:
                    $ anti_epilogue_pc_survival_deathcause = "pc_goal"
                    $ anti_epilogue_pc_survival_deathdescription = ""
                    menu:
                        '{color=#f6d6bd}[pcname]{/color} spent their remaining two years in relative peace, under a new name and keeping a low profile. But, after one of their patrols, they discovered that their dearest family member was nowhere to be found. According to their surprised neighbors, a group of portly travelers had arrived just two days earlier, and the sibling has left with them {i}willingly{/i}, saying that {i}they didn’t want {color=#f6d6bd}[pcname]{/color} to look for them{/i}, for the {i}debt was now paid{/i}.
                        \n\nThe rider prepared their equipment and left soon after, ready to face the dark corners of {color=#f6d6bd}Hovlavan{/color} one last time.
                        '
                        '(end the game)':
                            jump endingtransition_alt
            else:
                $ anti_epilogue_pc_survived = 1
                if anti_epilogue_village_selected == "howlersdell":
                    show areapicture ep_08a at basicfade
                elif anti_epilogue_village_selected == "creeks":
                    show areapicture ep_13b at basicfade
                elif anti_epilogue_village_selected == "galerocks":
                    show areapicture ep_14 at basicfade
                elif anti_epilogue_village_selected == "travel":
                    if anti_epilogue_peace_tier == 0:
                        show areapicture ep_07a at basicfade
                    else:
                        show areapicture ep_07b at basicfade
                if anti_epilogue_peace_tier == 0:
                    $ custom1 = ", dealing with the same struggles as the rest of their neighbors."
                elif anti_epilogue_peace_tier == 1:
                    $ custom1 = ", dealing with the same struggles as the rest of their neighbors."
                elif anti_epilogue_peace_tier == 2:
                    $ custom1 = ", prospering together with the rest of their neighbors."
                else:
                    $ custom1 = ", prospering together with the rest of their neighbors."
                if anti_epilogue_village_selected == "howlersdell":
                    $ custom2 = "{color=#f6d6bd}Thais{/color} was a demanding employer, bitter from the grudge she held against the roadwarden’s betrayal, but the village offered a full stomach, silence, and colorful linen.\n\nAt times, it felt like they had replaced the shadows of {color=#f6d6bd}Hovlavan{/color} with a new one - and it was suffocatingly comfortable."
                elif anti_epilogue_village_selected == "creeks":
                    if endgame_creeks_withered:
                        $ custom2 = "Their new home lasted for only a few decades, but they were lucky enough to join the tribe’s difficult journey through {color=#f6d6bd}Hag Hills{/color}.\n\nWhile their life was full of challenges, they could taste freedom again."
                    else:
                        $ custom2 = "\n\nTheir new home was growing in comfort and security, but the fresh air and the unusual customs that made the roadwarden drift toward {color=#f6d6bd}Creeks{/color} in the first place remained the same. Without the shadows of {color=#f6d6bd}Hovlavan{/color} looming over their family, they could taste freedom once again."
                elif anti_epilogue_village_selected == "galerocks":
                    $ custom2 = "\n\nTheir new home offered safety and stability, and without the shadows of {color=#f6d6bd}Hovlavan{/color} looming over their family, they could taste freedom once again."
                elif anti_epilogue_village_selected == "travel":
                    $ custom2 = "\n\nThe warden stuck to the roads, staying at inns and splitting their time between the tribes, helping their sibling find a new home. Without the shadows of {color=#f6d6bd}Hovlavan{/color} looming over their family, they could taste freedom once again."
                menu:
                    'With their debts paid off, {color=#f6d6bd}[pcname]{/color} and their sibling could spend the next few years in relative peace[custom1] [custom2]
                    '
                    '(end the game)':
                        jump endingtransition_alt
        if pc_goal == "iwanttostartanewlife":
            $ anti_epilogue_pc_survived = 1
            if anti_epilogue_village_selected == "howlersdell":
                show areapicture ep_08a at basicfade
            elif anti_epilogue_village_selected == "creeks":
                show areapicture ep_13b at basicfade
            elif anti_epilogue_village_selected == "galerocks":
                show areapicture ep_14 at basicfade
            elif anti_epilogue_village_selected == "travel":
                if anti_epilogue_peace_tier == 0:
                    show areapicture ep_07a at basicfade
                else:
                    show areapicture ep_07b at basicfade
            if anti_epilogue_village_selected == "howlersdell":
                $ custom2 = " took a new name and shelter at the richest village in the North. {color=#f6d6bd}Thais{/color} was a demanding employer, bitter from the grudge she held against the roadwarden’s betrayal, but she offered a full stomach, silence, and colorful linen.\n\nAt times, it felt like they had replaced the shadows of {color=#f6d6bd}Hovlavan{/color} with a new one - and it was suffocatingly comfortable."
            elif anti_epilogue_village_selected == "creeks":
                if endgame_creeks_withered:
                    $ custom2 = ", the local roadwarden, took a new name and shelter with their found family. After their palfrey was defeated by the beasts of the woods, they stuck to the nearest paths, looking after the hunters and foragers.\n\nThe village lasted for only a few decades, but they were lucky enough to join the tribe’s difficult journey through {color=#f6d6bd}Hag Hills{/color}.\n\nWhile their life was full of challenges, they left their difficult past behind."
                else:
                    if anti_epilogue_peace_tier == 0 or anti_epilogue_peace_tier == 1:
                        $ custom2 = ", the local roadwarden, took a new name and shelter with their found family. After their palfrey was defeated by the woods, the tribe helped them bring another mount from south of {color=#f6d6bd}Hag Hills{/color}. Their home was growing in security and comfort, but the fresh air and the unusual customs that made the rider drift toward {color=#f6d6bd}Creeks{/color} in the first place remained the same.\n\nWithout the city’s support, the beasts kept the trails dangerous, and after a few years even the most experienced rider in the North found their end in the wilderness. But not before they shared countless memories with their friends, free of their difficult past."
                    elif anti_epilogue_peace_tier == 2:
                        $ custom2 = ", the local roadwarden, took a new name and shelter with their found family. After their palfrey was defeated by the woods, the tribe helped them bring another mount from south of {color=#f6d6bd}Hag Hills{/color}. Their home was growing in security and comfort, but the fresh air and the unusual customs that made the rider drift toward {color=#f6d6bd}Creeks{/color} in the first place remained the same.\n\nWithout the city’s support, the beasts kept the trails dangerous, but thanks to the additional guards, newcomers ready to work, and rejuvenated trade, the rider reached old age almost in one piece. And even after that, they shared countless memories with their friends, free of their difficult past."
                    elif anti_epilogue_peace_tier == 3:
                        $ custom2 = ", the local roadwarden, took a new name and shelter with their found family. After their palfrey was defeated by the woods, the tribe helped them bring another mount from south of {color=#f6d6bd}Hag Hills{/color}. Their home was growing in security and comfort, but the fresh air and the unusual customs that made the rider drift toward {color=#f6d6bd}Creeks{/color} in the first place remained the same.\n\nWithout the city’s support, the beasts kept the trails dangerous, but thanks to the additional guards, newcomers ready to work, newly built settlements, and rejuvenated trade, the rider reached old age almost in one piece. And even after that, they shared countless memories with their friends, free of their difficult past."
            elif anti_epilogue_village_selected == "galerocks":
                if anti_epilogue_peace_tier == 0:
                    $ custom2 = ", the local roadwarden, took a new name and shelter with the hard-working tribe of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it.\n\nThe rider’s life became repetitive, but also simple, focused on the matters at hand. Without the city’s support, the trails remained dangerous, requiring a keen eye and quick decisions.\n\nThe newcomer’s life ended abruptly, from the strike of a noble griffon, but at this time, their heart was free of guilt or fear."
                elif anti_epilogue_peace_tier == 1 or anti_epilogue_peace_tier == 2:
                    $ custom2 = ", the local roadwarden, took a new name and shelter with the hard-working tribe of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it. Once their palfrey died from the attack of a noble griffon, the rider became the protector of the tunnels.\n\nSometimes, they observed the road nervously, as if their past was about to catch up with them, but they spent their old age in peace, resting in the safe shadow of the stone stronghold."
                elif anti_epilogue_peace_tier == 3:
                    $ custom2 = ", the local roadwarden, took a new name and shelter with the hard-working tribe of {color=#f6d6bd}Gale Rocks{/color}. After the locals restored the route to the lake, their new neighbor was invited to patrol it. Once their palfrey died from the attack of a noble griffon, the rider became the protector of the tunnels.\n\nAs the years went by and the villagers started to send out their caravans, the warden’s role kept growing. Sometimes, they observed the road nervously, as if their past was about to catch up with them, but once it happened, their new family was there to protect them. They spent their old age in peace, resting in the safe shadow of the stone stronghold."
            elif anti_epilogue_village_selected == "travel":
                if anti_epilogue_peace_tier == 0 or anti_epilogue_peace_tier == 1:
                    $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by and the wilderness became more encumbering, the rider could ask for even better pay for their services, but couldn’t really put down roots anywhere, and was, most of the time, alone.\n\nTheir life ended abruptly, when the consequences of their past finally caught up with them."
                elif anti_epilogue_peace_tier == 2:
                    $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by, the roads were getting slightly safer, and the rider could ask for something of much greater value than coins - favors.\n\nThey died a decade later, when their horse got too sick to flee a crimson ghoul. But not before they shared countless memories with their friends, free of their difficult past."
                elif anti_epilogue_peace_tier == 3:
                    if anti_epilogue_village_tulia_fate == "pelt" and dalit_friendship >= 10:
                        $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by, the roads were getting slightly safer, and the rider could ask for something of much greater value than coins - favors.\n\nWhen their horse got too sick to flee a crimson ghoul, the warden managed to find shelter at {color=#f6d6bd}Pelt of the North{/color}, where they spent their remaining years - in part working as a guard, but mainly just resting, exchanging tales of their adventurous life with travelers.\n\nSometimes, they observed the road nervously, as if their past was about to catch up with them, but once it happened, {color=#f6d6bd}Tulia{/color} and {color=#f6d6bd}Dalit{/color} were there to protect them."
                    elif anti_epilogue_village_tulia_fate == "pelt":
                        $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by, the roads were getting slightly safer, and the rider could ask for something of much greater value than coins - favors.\n\nWhen their horse got too sick to flee a crimson ghoul, the warden managed to find shelter at {color=#f6d6bd}Pelt of the North{/color}, where they spent their remaining years - in part working as a guard, but mainly just resting, exchanging tales of their adventurous life with travelers.\n\nSometimes, they observed the road nervously, as if their past was about to catch up with them, but once it happened, {color=#f6d6bd}Tulia{/color} was there to protect them."
                    elif dalit_friendship >= 10:
                        $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by, the roads were getting slightly safer, and the rider could ask for something of much greater value than coins - favors.\n\nWhen their horse got too sick to flee a crimson ghoul, the warden managed to find shelter at {color=#f6d6bd}Pelt of the North{/color}, where they spent their remaining years - in part working as a guard, but mainly just resting, exchanging tales of their adventurous life with travelers.\n\nSometimes, they observed the road nervously, as if their past was about to catch up with them, but once it happened, {color=#f6d6bd}Dalit{/color} was there to protect them."
                    elif dalit_friendship >= 10:
                        $ custom2 = ", the local roadwarden, took a new name, but stuck to the roads, staying at inns and splitting their time between the tribes. As the years went by, the roads were getting slightly safer, and the rider could ask for something of much greater value than coins - favors.\n\nWhen their horse got too sick to flee a crimson ghoul, the warden managed to find shelter at {color=#f6d6bd}Pelt of the North{/color}, where they spent their remaining years - in part working as a guard, but mainly just resting, exchanging tales of their adventurous life with travelers.\n\nSadly, their difficult past didn’t spare them. Their pursuers managed to put the tales together and caught the rider off guard."
            menu:
                '{color=#f6d6bd}[pcname]{/color}[custom2]
                '
                '(end the game)':
                    jump endingtransition_alt


label endingtransition_alt:
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




