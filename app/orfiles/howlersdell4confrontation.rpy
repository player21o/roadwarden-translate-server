default howlersdell_steephouseconfrontation_firsttime = 0
default howlersdell_steephouseconfrontation_childrenshame = 0

default howlersdell_steephouseconfrontation_elpis_points = 0
default howlersdell_steephouseconfrontation_elpis_points_required = 12

default howlersdell_steephouseconfrontation_elpis_argument_steephouse = 0
default howlersdell_steephouseconfrontation_elpis_argument_curse = 0 # if quest_ruins_insideclues06
default howlersdell_steephouseconfrontation_elpis_argument_treepicture = 0 # if quest_ruins_treepicture
default howlersdell_steephouseconfrontation_elpis_argument_nextattack = 0 # if quest_orentius_thais_description00 and not whitemarshes_attacked
default howlersdell_steephouseconfrontation_elpis_argument_childrenshame = 0 # if howlersdell_steephouseconfrontation_childrenshame

default howlersdell_steephouseconfrontation_elpis_argument_thais = 0
default howlersdell_steephouseconfrontation_elpis_argument_thaisletter = 0 # if item_thaisletter_read
default howlersdell_steephouseconfrontation_elpis_argument_glauciahostility = 0 # if default glaucia_about_steephouse3
default howlersdell_steephouseconfrontation_elpis_argument_aboutthais = 0 # if howlersdell_elpis_about_thais
default howlersdell_steephouseconfrontation_elpis_argument_olddruid = 0 # if druidcave_druid_about_robes and oldpagos_cured and druidcave_druid_about_druids1

default howlersdell_steephouseconfrontation_elpis_argument_trust = 0
default howlersdell_steephouseconfrontation_elpis_argument_faith = 0

default howlersdell_steephouseconfrontation_thais_points = 0
default howlersdell_steephouseconfrontation_thais_points_required = 18

default howlersdell_steephouseconfrontation_thais_argument_curse = 0
default howlersdell_steephouseconfrontation_thais_argument_treepicture = 0
default howlersdell_steephouseconfrontation_thais_argument_elpis = 0
default howlersdell_steephouseconfrontation_thais_argument_thaisletter = 0
default howlersdell_steephouseconfrontation_thais_argument_childrenshame = 0
default howlersdell_steephouseconfrontation_thais_argument_regret = 0
default howlersdell_steephouseconfrontation_thais_argument_mouflons = 0

label howlersdell_steephouseconfrontation00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to decide what to do with what I’ve learned about {color=#f6d6bd}Steep House{/color}.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if howlersdell_steephouseconfrontation_firsttime:
        jump howlersdell_steephouseconfrontation00alt
    else:
        $ howlersdell_steephouseconfrontation_firsttime = 1
    menu:
        'You’re standing in the middle of the islet, taking a good look at the village. The locals follow their daily routines, children are playing tag, the trees are turning gold and brown. You listen to the humming creek and a singing old woman.
        \n\nYet, you can see what’s beneath all that - a home to raiders who led dozens of humans to their death.
        \n\nIf you decide to act, you’ll have only one shot at this. Starting a storm without the firm support of the locals will paint you as a threat. If {color=#f6d6bd}Thais{/color} was able to keep her power despite her deeds, she surely has strong support, and she may not yield to you even if openly confronted.
        '
        'It’d be easier for me to get the most from the village if I were to let {color=#f6d6bd}Steep House{/color} fade into the past.' if pc_goal == "iwantstatus":
            jump howlersdell_steephouseconfrontationFORGOTTEN00alt
        'I ought to do my best to weaken {color=#f6d6bd}the mayor’s{/color} position. {color=#f6d6bd}The druids{/color} may help me with that.' if howlersdell_elpis_about_thais and not thais_rumor_elpis_treason or (item_thaisletter_read and howlersdell_elpis_firsttime >= 2 and not thais_rumor_elpis_treason):
            jump howlersdell_steephouseconfrontationANTIthais00
        'I don’t know of anyone who could help me take the mayor down. (disabled)' if (not howlersdell_elpis_about_thais and not item_thaisletter_read and not thais_rumor_elpis_treason):
            pass
        'Elpis won’t help me take the mayor down. Not after I betrayed her. (disabled)' if thais_rumor_elpis_treason:
            pass
        'I could offer {color=#f6d6bd}Thais{/color} an alliance... In exchange for my silence.' if not thais_bigmad:
            jump howlersdell_steephouseconfrontationPROthais00
        'Since Thais doesn’t trust me, confronting her directly will only cause me trouble. (disabled)' if thais_bigmad:
            pass
        'I already did my part. I’m going to report everything to the city officials, let them decide if they should get involved.':
            jump howlersdell_steephouseconfrontationCITY00
        'Nothing good would come out of opening old wounds. It’s better to let {color=#f6d6bd}Steep House{/color} fade into the past.' if pc_goal != "iwantstatus":
            jump howlersdell_steephouseconfrontationFORGOTTEN00
        'I’m not ready to choose.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not ready to choose.')
            jump howlersdellafterinteraction

    label howlersdell_steephouseconfrontation00alt:
        menu:
            'You reconsider your options.
            '
            'It’d be easier for me to get the most from the village if I were to let {color=#f6d6bd}Steep House{/color} fade into the past.' if pc_goal == "iwantstatus":
                jump howlersdell_steephouseconfrontationFORGOTTEN00alt
            'I ought to do my best to weaken {color=#f6d6bd}the mayor’s{/color} position. {color=#f6d6bd}The druids{/color} may help me with that.' if howlersdell_elpis_about_thais and not thais_rumor_elpis_treason or (item_thaisletter_read and howlersdell_elpis_firsttime >= 2 and not thais_rumor_elpis_treason):
                jump howlersdell_steephouseconfrontationANTIthais00
            'I don’t know of anyone who could help me take the mayor down. (disabled)' if (not howlersdell_elpis_about_thais and not item_thaisletter_read and not thais_rumor_elpis_treason):
                pass
            'Elpis won’t help me take the mayor down. Not after I betrayed her. (disabled)' if thais_rumor_elpis_treason:
                pass
            'I could offer {color=#f6d6bd}Thais{/color} an alliance... In exchange for my silence.' if not thais_bigmad:
                jump howlersdell_steephouseconfrontationPROthais00
            'Since Thais doesn’t trust me, confronting her directly will only cause me trouble. (disabled)' if thais_bigmad:
                pass
            'I already did my part. I’m going to report everything to the city officials, let them decide if they should get involved.':
                jump howlersdell_steephouseconfrontationCITY00
            'Nothing good would come out of opening old wounds. It’s better to let {color=#f6d6bd}Steep House{/color} fade into the past.' if pc_goal != "iwantstatus":
                jump howlersdell_steephouseconfrontationFORGOTTEN00
            'I’m not ready to choose.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not ready to choose.')
                jump howlersdellafterinteraction

label howlersdell_steephouseconfrontationCITY00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I already did my part. I’m going to report everything to the city officials, let them decide if they should get involved.')
    menu:
        'You think about the city chief, as well as the merchant guild - they are driven by their goals, not morals. The United Church can be vengeful, but cares little about outsiders.
        \n\nIt’s likely that they’ll forgive all of {color=#f6d6bd}Thais’{/color} wrongdoings if it helps them put their hands on the peninsula.
        '
        'I’ll let them figure this out.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll let them figure this out.')
            $ quest_ruins = 2
            $ renpy.notify("Quest completed: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
            $ quest_ruins_choice = "lefttocity"
            menu:
                'You return to {color=#f6d6bd}[horsename]{/color} and glance at the inn. Will your employers turn it to ashes, or sit at its tables, negotiating trade deals? It’s no longer your call.
                '
                'It’s better than putting such a responsibility on a single soul.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s better than putting such a responsibility on a single soul.')
                    $ minutes += 5
                    jump howlersdellafterinteraction
                'I trust the officials. They’ll know what to do.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I trust the officials. They’ll know what to do.')
                    $ minutes += 5
                    jump howlersdellafterinteraction
                'I don’t want to put the merchants’ investments at risk.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t want to put the merchants’ investments at risk.')
                    $ minutes += 5
                    jump howlersdellafterinteraction
        'I have second thoughts...':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have second thoughts...')
            jump howlersdell_steephouseconfrontation00alt

label howlersdell_steephouseconfrontationFORGOTTEN00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Nothing good would come out of opening old wounds. It’s better to let {color=#f6d6bd}Steep House{/color} fade into the past.')
    label howlersdell_steephouseconfrontationFORGOTTEN00b:
        menu:
            'You think about the ruins, the signs of life that you found among them. The road you want to take may not be the just one, but at least it may help avoid any further harm.
            '
            'It’s for the best.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s for the best.')
                $ quest_ruins = 2
                $ renpy.notify("Quest completed: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
                $ quest_ruins_choice = "forgotten"
                menu:
                    'You return to {color=#f6d6bd}[horsename]{/color} and glance at the inn. Most likely, it was here where the loot taken out of {color=#f6d6bd}Steep House{/color} was split between the guards.
                    '
                    'Cruel or not, neither the attackers nor the attacked were tied to the city. They have the right to their own laws and judgment.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Cruel or not, neither the attackers nor the attacked were tied to the city. They have the right to their own laws and judgment.')
                        $ minutes += 5
                        if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                            $ pc_goal_iwantstatuspoints += 2
                        if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                        jump howlersdellafterinteraction
                    'I’m not going to risk my life for a pile of debris.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not going to risk my life for a pile of debris.')
                        $ minutes += 5
                        if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                            $ pc_goal_iwantstatuspoints += 2
                        if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                        jump howlersdellafterinteraction
                    'Time to get back to work.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to get back to work.')
                        $ minutes += 5
                        if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                            $ pc_goal_iwantstatuspoints += 2
                        if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                        jump howlersdellafterinteraction
            'I have second thoughts...':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have second thoughts...')
                jump howlersdell_steephouseconfrontation00alt

    label howlersdell_steephouseconfrontationFORGOTTEN00alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’d be easier for me to get the most from the village if I were to let {color=#f6d6bd}Steep House{/color} fade into the past.')
        jump howlersdell_steephouseconfrontationFORGOTTEN00b

label howlersdell_steephouseconfrontationANTIthaisALL:
    label howlersdell_steephouseconfrontationANTIthais00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ought to do my best to weaken {color=#f6d6bd}the mayor’s{/color} position. {color=#f6d6bd}The druids{/color} may help me with that.')
        menu:
            'You think of your previous conversations with {color=#f6d6bd}Elpis{/color}. While she is surely respected in the village and seems to have unusual talents, so far her attitude toward {color=#f6d6bd}the mayor{/color} has been rather timid. Unless you can present a good case to make her turn against {color=#f6d6bd}Thais{/color}, you doubt she’s going to keep your conversation a secret.
            '
            'Let’s hope she’ll listen to reason.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope she’ll listen to reason.')
                jump howlersdell_steephouseconfrontationANTIthais01
            'I have second thoughts...':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have second thoughts...')
                jump howlersdell_steephouseconfrontation00alt

    label howlersdell_steephouseconfrontationANTIthais01:
        $ quarters += 1
        show areapicture howlersdellforestgarden at basicfade
        stop music fadeout 4.0
        play nature "audio/ambient/prologuebirds01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'After some time, the two of you are wandering in the forest garden. The thumping of {color=#f6d6bd}the druidess’{/color} staff as she walks disappears in the overwhelming noise. A few hunters and other druids are on the verge of sight, looking out for beasts.
            \n\nShe finally breaks the silence. “Why do you want to speak of {color=#f6d6bd}Steep House{/color}?”
            \n\nBefore you left the village, the suspicious looks of the guards convinced you {color=#f6d6bd}the mayor{/color} already knows about your stroll.
            '
            '“{color=#f6d6bd}Thais{/color} is both ambitious and cruel. I won’t allow her to hurt other tribes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is both ambitious and cruel. I won’t allow her to hurt other tribes.”')
                $ custom1 = "“She may be much worse than that, but our neighbors see her as a sow, protective of her boarlets.” She reaches for a rotten apple. The branch from which it was hanging suddenly falls on the ground, even though it’s still green, “We do ne choose our leaders through violence or intrigues, but through the votes of all. I may have ma doubts, but I’m trusted to never seek control, only to give advice.”"
                jump howlersdell_steephouseconfrontationANTIthais02
            '“{color=#f6d6bd}Thais{/color} is unpredictable and manipulative. It’s time for the druids to restore order to the village.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is unpredictable and manipulative. It’s time for the druids to restore order to the village.”')
                $ howlersdell_elpis_friendship -= 1
                $ custom1 = "“We do ne choose our leaders through violence or intrigues, but through the votes of all our neighbors. She {i}is{/i} trusted by the others, for she already makes their lives {i}orderly{/i}, en much easier than they used to be.” She reaches for a rotten apple. The branch from which it was hanging suddenly dries out. “Ma gathering seeks nae power. I do ne know what you expected to hear.”"
                jump howlersdell_steephouseconfrontationANTIthais02
            '“{color=#f6d6bd}Howler’s Dell{/color} doesn’t need to grow any more. We must stop {color=#f6d6bd}Thais{/color}, for she will never be full.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Howler’s Dell{/color} doesn’t need to grow any more. We must stop {color=#f6d6bd}Thais{/color}, for she will never be full.”')
                $ howlersdell_elpis_friendship += 1
                $ custom1 = "She doesn’t respond at first, instead staring at an apple, rotting on a branch. She picks it gently, then touches the branch. Its leaves grow stronger and larger. “You’re right,” she says carefully, “but now there are many like her. I may have ma doubts, but I’m trusted to never seek control, only to give advice.”"
                label howlersdell_steephouseconfrontationANTIthais02:
                    menu:
                        '[custom1]
                        \n\nYou keep following the many beaten trails. The bright, sparse woods are nothing like those you’ve seen in the other parts of the peninsula. “I’m listening.”
                        '
                        '“You must admit that what happened to the village was terrible.”' if not howlersdell_steephouseconfrontation_elpis_argument_steephouse:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must admit that what happened to the village was terrible.”')
                            jump howlersdell_steephouseconfrontation_elpis_argument_steephouse01
                        '“Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”' if not howlersdell_steephouseconfrontation_elpis_argument_thais:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”')
                            jump howlersdell_steephouseconfrontation_elpis_argument_thais01
                        '{image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”' if not howlersdell_steephouseconfrontation_elpis_argument_trust:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”')
                            jump howlersdell_steephouseconfrontation_elpis_argument_trust01
                        '{image=d6} “I also follow my ancestors. I’m trying to make things right.”' if not howlersdell_steephouseconfrontation_elpis_argument_faith and pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I also follow my ancestors. I’m trying to make things right.”')
                            jump howlersdell_steephouseconfrontation_elpis_argument_faith01
                        '“What’s your decision? Will you speak with your tribe?”' if howlersdell_steephouseconfrontation_elpis_argument_steephouse and howlersdell_steephouseconfrontation_elpis_argument_thais:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your decision? Will you speak with your tribe?”')
                            jump howlersdell_steephouseconfrontationANTIthais03

    label howlersdell_steephouseconfrontationANTIthais02part2:
        menu:
            '[custom1]
            '
            '“You must admit that what happened to the village was terrible.”' if not howlersdell_steephouseconfrontation_elpis_argument_steephouse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must admit that what happened to the village was terrible.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse01
            '“Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”' if not howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”')
                jump howlersdell_steephouseconfrontation_elpis_argument_thais01
            '{image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”' if not howlersdell_steephouseconfrontation_elpis_argument_trust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_trust01
            '{image=d6} “I also follow my ancestors. I’m trying to make things right.”' if not howlersdell_steephouseconfrontation_elpis_argument_faith and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I also follow my ancestors. I’m trying to make things right.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_faith01
            '“What’s your decision? Will you speak with the others?”' if howlersdell_steephouseconfrontation_elpis_argument_steephouse and howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your decision? Will you speak with the others?”')
                jump howlersdell_steephouseconfrontationANTIthais03

    label howlersdell_steephouseconfrontation_elpis_argument_steephouse01:
        $ howlersdell_steephouseconfrontation_elpis_argument_steephouse = 1
        if whitemarshes_attacked or (whitemarshes_destroyed and not whitemarshes_attacked and thais_about_nomoreundead):
            $ howlersdell_steephouseconfrontation_elpis_points -= 2
            $ custom1 = "She quickens her pace. “Ne much worse than what you left behind in {color=#f6d6bd}White Marshes{/color}.”"
        else:
            $ custom1 = "She slackens her pace. “I must.”"
        menu:
            '[custom1]
            '
            '“I know the druids played a role in the raid. The village fields are cursed to this day.”' if quest_ruins_insideclues06 and not howlersdell_steephouseconfrontation_elpis_argument_curse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know the druids played a role in the raid. The village fields are cursed to this day.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_curse = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse_curse01
            '“Whatever the reasons behind the attack, it was fueled by rage. I saw the tree painted with blood inside one of the buildings. It reeks of hatred.”' if quest_ruins_treepicture and not howlersdell_steephouseconfrontation_elpis_argument_treepicture:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Whatever the reasons behind the attack, it was fueled by rage. I saw the tree painted with blood inside one of the buildings. It reeks of hatred.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_treepicture = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ custom1 = "“There was ne {i}good{/i} cause behind any of it,” she states matter-of-factly, “but at the time, ma neighbors felt otherwise. Threatened, desperate, betrayed, en cornered. They lost their hamlet, merchants, and the pact. I can ne justify what they’ve done, but they are nae monsters.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“{color=#f6d6bd}Thais{/color} is planning to strike {color=#f6d6bd}White Marshes{/color} next. How many villages does she need to destroy?”' if quest_orentius_thais_description00 and not whitemarshes_attacked and not whitemarshes_destroyed and not howlersdell_steephouseconfrontation_elpis_argument_nextattack:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is planning to strike {color=#f6d6bd}White Marshes{/color} next. How many villages does she need to destroy?”')
                $ howlersdell_steephouseconfrontation_elpis_argument_nextattack = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "You notice her surprised frown, but she doesn’t respond. She leads you north, closer to the main road."
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“You act as if your neighbors have acknowledged their deeds, but everyone treats it like a secret. The youngest generation isn’t even aware of what happened.”' if howlersdell_steephouseconfrontation_childrenshame and not howlersdell_steephouseconfrontation_elpis_argument_childrenshame:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You act as if your neighbors have acknowledged their deeds, but everyone treats it like a secret. The youngest generation isn’t even aware of what happened.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_childrenshame = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "“It was ma... {color=#f6d6bd}The elder’s from the cave{/color} last request before he left us. {i}I’ll spare you ma wrath{/i}, he said, {i}if you keep the childrens’ hearts unstained, until they reach a certain age. The forest speakers ought to help them find a lesson in your greed en cruelty.{/i}”\n\nShe stops in place, observing a red, dotted mushroom. She crouches, digs it out with a knife, and puts it into a sack. “When {color=#f6d6bd}Thais{/color} made the decision that this {i}certain age{/i} would never come, I did ne dare to oppose her - our neighbors trusted her.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“Well, you know more about those days than I do.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, you know more about those days than I do.”')
                $ custom1 = "You carry on in silence."
                jump howlersdell_steephouseconfrontationANTIthais02part2

    label howlersdell_steephouseconfrontation_elpis_argument_steephouse02:
        menu:
            '[custom1]
            '
            '“I know the druids played a role in the raid. The village fields are cursed to this day.”' if quest_ruins_insideclues06 and not howlersdell_steephouseconfrontation_elpis_argument_curse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know the druids played a role in the raid. The village fields are cursed to this day.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_curse = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse_curse01
            '“Whatever the reasons behind the attack, it was fueled by rage. I saw the tree painted with blood inside one of the buildings. It reeks of hatred.”' if quest_ruins_treepicture and not howlersdell_steephouseconfrontation_elpis_argument_treepicture:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Whatever the reasons behind the attack, it was fueled by rage. I saw the tree painted with blood inside one of the buildings. It reeks of hatred.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_treepicture = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ custom1 = "“There was ne {i}good{/i} cause behind any of it,” she states matter-of-factly, “but at the time, ma neighbors felt otherwise. Threatened, desperate, betrayed, en cornered. They lost their hamlet, merchants, and the pact. I can ne justify what they’ve done, but they are nae monsters.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“{color=#f6d6bd}Thais{/color} is planning to strike {color=#f6d6bd}White Marshes{/color} next. How many villages does she need to destroy?”' if quest_orentius_thais_description00 and not whitemarshes_attacked and not whitemarshes_destroyed and not howlersdell_steephouseconfrontation_elpis_argument_nextattack:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is planning to strike {color=#f6d6bd}White Marshes{/color} next. How many villages does she need to destroy?”')
                $ howlersdell_steephouseconfrontation_elpis_argument_nextattack = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "You notice her surprised frown, but she doesn’t respond. She leads you north, closer to the main road."
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“You act as if your neighbors have acknowledged their deeds, but everyone treats it like a secret. The youngest generation isn’t even aware of what happened.”' if howlersdell_steephouseconfrontation_childrenshame and not howlersdell_steephouseconfrontation_elpis_argument_childrenshame:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You act as if your neighbors have acknowledged their deeds, but everyone treats it like a secret. The youngest generation isn’t even aware of what happened.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_childrenshame = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "“It was ma... {color=#f6d6bd}The elder’s from the cave{/color} last request before he left us. {i}I’ll spare you ma wrath{/i}, he said, {i}if you keep the childrens’ hearts unstained, until they reach a certain age. The forest speakers ought to help them find a lesson in your greed en cruelty.{/i}”\n\nShe stops in place, observing a red, dotted mushroom. She crouches, digs it out with a knife, and puts it into a sack. “When {color=#f6d6bd}Thais{/color} made the decision that this {i}certain age{/i} would never come, I did ne dare to oppose her - our neighbors trusted her.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“That’s all I have to say about that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I have to say about that.”')
                $ custom1 = "As you move forward, her staff rhythmically hits the ground."
                jump howlersdell_steephouseconfrontationANTIthais02part2

    label howlersdell_steephouseconfrontation_elpis_argument_steephouse_curse01:
        menu:
            '“As the gathering, we did ne agree to the raid, but we agreed to {i}protect{/i} our children, siblings, en cousins during their strike, with pneuma en advice.” A long pause. “After we breached the wall, {color=#f6d6bd}Thais{/color} {i}forced{/i} us to keep pushing. Some elders were hurt. Others caved in.”
            \n\nHer voice cracks.
            '
            '“Does your gathering regret helping her?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does your gathering regret helping her?”')
                $ howlersdell_elpis_friendship += 1
                $ custom1 = "“We do,” she says softly. “Some were broken by it.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02
            '“Now you have an opportunity to fix your mistakes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Now you have an opportunity to fix your mistakes.”')
                $ custom1 = "“Ne at all,” she says harshly. “The dead will ne return, their homes are but a bird’s nest. We ought to stay in shame, yet be of use - redemption will never come, but we have to climb higher.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse02

    label howlersdell_steephouseconfrontation_elpis_argument_thais01:
        $ howlersdell_steephouseconfrontation_elpis_argument_thais = 1
        if quest_fisherhamlet_description09 or quest_fisherhamlet_description10:
            $ custom1 = "She stops and observes the carcass of a hedgehog. Judging by the tracks, it was butchered by a badger. “It may be true that, so far, you have ne added fuel to her plans.” She crouches slightly, giving the shell a closer look. “Ants,” she says, then steps around it. “Ma neighbors gained a lot from her past choices. {i}Ma{/i} judgment means a lot to them, but she showed she will protects us, eva if the price is too high.”"
        else:
            $ howlersdell_steephouseconfrontation_elpis_points -= 2
            $ custom1 = "She stops and observes the carcass of a hedgehog. Judging by the tracks, it was butchered by a badger. “You say it as if you have ne added fuel to her plans.” She pushes the shell with her staff, then turns toward you. “Ever since you revealed the truth about the hamlet, ma neighbors trust that she’s leading them toward greater days. {i}Ma{/i} judgment means eva less now.”"
        menu:
            '[custom1]
            '
            '“We already talked about her. You know how impulsive she gets. There must be someone else who can lead your tribe.”' if howlersdell_elpis_about_thais and not howlersdell_steephouseconfrontation_elpis_argument_aboutthais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We already talked about her. You know how impulsive she gets. There must be someone else who can lead your tribe.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_aboutthais = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                jump howlersdell_steephouseconfrontation_elpis_argument_thais_aboutthais01
            'I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”' if item_thaisletter_read and not howlersdell_steephouseconfrontation_elpis_argument_thaisletter and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ pc_faithpoints_opportunities += 1
                if pc_religion == "pagan":
                    $ pc_faithpoints += 5
                if pc_religion == "ordersoftruth":
                    $ pc_faithpoints -= 2
                if pc_religion == "fellowship":
                    $ pc_faithpoints -= 1
                $ description_druids10 = "I told {color=#f6d6bd}Elpis{/color} about {color=#f6d6bd}Thais’{/color} betrayal."
                $ custom1 = "She glances at the parchment hanging from your hand, then looks at you, listening to your story patiently. The more you say, the shinier her eyes become, getting closer to a venom-like green.\n\nOnce you’re done, she rubs her staff and looks at its tip, as if she’s measuring it before a strike. “I see.”\n\nNo matter her gestures, her words are filled with pain."
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            'Even though it’s strictly against The United Church’s interest, I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”' if item_thaisletter_read and not howlersdell_steephouseconfrontation_elpis_argument_thaisletter and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Even though it’s strictly against The United Church’s interest, I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”')
                $ pc_faithpoints_opportunities += 1
                $ pc_faithpoints = -10
                $ description_druids10 = "I told {color=#f6d6bd}Elpis{/color} about {color=#f6d6bd}Thais’{/color} betrayal."
                $ howlersdell_steephouseconfrontation_elpis_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ custom1 = "She glances at the parchment hanging from your hand, then looks at you, listening to your story patiently. The more you say, the shinier her eyes become, getting closer to a venom-like green.\n\nOnce you’re done, she rubs her staff and looks at its tip, as if she’s measuring it before a strike. “I see.”\n\nNo matter her gestures, her words are filled with pain."
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“You must be aware how vengeful {color=#f6d6bd}Glaucia{/color} is. She’s going to seek a way to {i}punish{/i} {color=#f6d6bd}Thais{/color}. If your village was to stand in her way, she would burn it to the ground.”' if glaucia_about_steephouse3 and not howlersdell_steephouseconfrontation_elpis_argument_glauciahostility:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must be aware how vengeful {color=#f6d6bd}Glaucia{/color} is. She’s going to seek a way to {i}punish{/i} {color=#f6d6bd}Thais{/color}. If your village was to stand in her way, she would burn it to the ground.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_glauciahostility = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "Her eyes are like a violent ocean wave. “You misjudge her. Eva soon after the raid she paid us little attention, en traded with our hunters. She knows {color=#f6d6bd}Thais{/color} can ne be reached.”\n\nYou share what you’ve learned about her determination, and that her {i}patience{/i} shouldn’t be mistaken for {i}forgiveness{/i}. She glances at the scouts, then meets your eyes. “I doubt she’ll find a way. The’s but a few lost souls by her side. Yet I must agree - we may face a sore price for all the deeds we’ve looked away from.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“Aren’t you worried about the future of your gathering? You grow in comfort, but from what I’ve seen, you are detached from the teachings you shared with me, or the ones I’ve heard from the {color=#f6d6bd}altar warden{/color}.”' if (druidcave_druid_about_robes and druidcave_druid_about_druids1 and howlersdell_elpis_about_faith2 and not howlersdell_steephouseconfrontation_elpis_argument_olddruid) or (howlersdell_elpis_about_faith2 and oldpagos_cured and not howlersdell_steephouseconfrontation_elpis_argument_olddruid):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Aren’t you worried about the future of your gathering? You grow in comfort, but from what I’ve seen, you are detached from the teachings you shared with me, or the ones I’ve heard from the {color=#f6d6bd}altar warden{/color}.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_olddruid = 1
                if item_wingedhourglass_worn:
                    $ howlersdell_steephouseconfrontation_elpis_points -= 1
                    $ custom1 = "She looks at the hourglass on your neck and her lips form a thin line. “Do ne pretend you care for any of us, slaver.”"
                else:
                    $ howlersdell_steephouseconfrontation_elpis_points += 1
                    $ custom1 = "“We pay close attention to the teachings of our ancestors, en are ne too proud to see that the seasons are ne the same as they used to be, the animals come en go, some pacts were broken, en new tribes moved in. Our village is bound to change as well, en we would be blind to think our teachings will never have to grow.” She stops and looks back, in the direction of {color=#f6d6bd}Howler’s{/color}, though you see only tree trunks and shrubs. “‘Tis true that these changes occur too fast for ma heart.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“I’d rather not wait until it’s too late, but as you wish.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather not wait until it’s too late, but as you wish.”')
                $ custom1 = "You carry on in silence."
                jump howlersdell_steephouseconfrontationANTIthais02part2

    label howlersdell_steephouseconfrontation_elpis_argument_thais02:
        menu:
            '[custom1]
            '
            '“We already talked about her. You know how impulsive she gets. There must be someone else who can lead your tribe.”' if howlersdell_elpis_about_thais and not howlersdell_steephouseconfrontation_elpis_argument_aboutthais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We already talked about her. You know how impulsive she gets. There must be someone else who can lead your tribe.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_aboutthais = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                jump howlersdell_steephouseconfrontation_elpis_argument_thais_aboutthais01
            'I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”' if item_thaisletter_read and not howlersdell_steephouseconfrontation_elpis_argument_thaisletter and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ pc_faithpoints_opportunities += 1
                if pc_religion == "pagan":
                    $ pc_faithpoints += 5
                if pc_religion == "ordersoftruth":
                    $ pc_faithpoints -= 2
                if pc_religion == "fellowship":
                    $ pc_faithpoints -= 1
                $ description_druids10 = "I told {color=#f6d6bd}Elpis{/color} about {color=#f6d6bd}Thais’{/color} betrayal."
                $ custom1 = "She glances at the parchment hanging from your hand, then looks at you, listening to your story patiently. The more you say, the shinier her eyes become, getting closer to a venom-like green.\n\nOnce you’re done, she rubs her staff and looks at its tip, as if she’s measuring it before a strike. “I see.”\n\nNo matter her gestures, her words are filled with pain."
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            'Even though it’s strictly against The United Church’s interest, I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”' if item_thaisletter_read and not howlersdell_steephouseconfrontation_elpis_argument_thaisletter and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Even though it’s strictly against The United Church’s interest, I show her the letter to the guild. “She wants to bring Wright’s missionaries to this place. Behind your back.”')
                $ pc_faithpoints_opportunities += 1
                $ pc_faithpoints = -10
                $ description_druids10 = "I told {color=#f6d6bd}Elpis{/color} about {color=#f6d6bd}Thais’{/color} betrayal."
                $ howlersdell_steephouseconfrontation_elpis_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ custom1 = "She glances at the parchment hanging from your hand, then looks at you, listening to your story patiently. The more you say, the shinier her eyes become, getting closer to a venom-like green.\n\nOnce you’re done, she rubs her staff and looks at its tip, as if she’s measuring it before a strike. “I see.”\n\nNo matter her gestures, her words are filled with pain."
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“You must be aware how vengeful {color=#f6d6bd}Glaucia{/color} is. She’s going to seek a way to {i}punish{/i} {color=#f6d6bd}Thais{/color}. If your village was to stand in her way, she would burn it to the ground.”' if glaucia_about_steephouse3 and not howlersdell_steephouseconfrontation_elpis_argument_glauciahostility:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must be aware how vengeful {color=#f6d6bd}Glaucia{/color} is. She’s going to seek a way to {i}punish{/i} {color=#f6d6bd}Thais{/color}. If your village was to stand in her way, she would burn it to the ground.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_glauciahostility = 1
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ custom1 = "Her eyes are like a violent ocean wave. “You misjudge her. Eva soon after the raid she paid us little attention, en traded with our hunters. She knows {color=#f6d6bd}Thais{/color} can ne be reached.”\n\nYou share what you’ve learned about her determination, and that her {i}patience{/i} shouldn’t be mistaken for {i}forgiveness{/i}. She glances at the scouts, then meets your eyes. “I doubt she’ll find a way. The’s but a few lost souls by her side. Yet I must agree - we may face a sore price for all the deeds we’ve looked away from.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“Aren’t you worried about the future of your gathering? You grow in comfort, but from what I’ve seen, you are detached from the teachings you shared with me, or the ones I’ve heard from the {color=#f6d6bd}altar warden{/color}.”' if (druidcave_druid_about_robes and druidcave_druid_about_druids1 and howlersdell_elpis_about_faith2 and not howlersdell_steephouseconfrontation_elpis_argument_olddruid) or (howlersdell_elpis_about_faith2 and oldpagos_cured and not howlersdell_steephouseconfrontation_elpis_argument_olddruid):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Aren’t you worried about the future of your gathering? You grow in comfort, but from what I’ve seen, you are detached from the teachings you shared with me, or the ones I’ve heard from the {color=#f6d6bd}altar warden{/color}.”')
                $ howlersdell_steephouseconfrontation_elpis_argument_olddruid = 1
                if item_wingedhourglass_worn:
                    $ howlersdell_steephouseconfrontation_elpis_points -= 1
                    $ custom1 = "She looks at the hourglass on your neck and her lips form a thin line. “Do ne pretend you care for any of us, slaver.”"
                else:
                    $ howlersdell_steephouseconfrontation_elpis_points += 1
                    $ custom1 = "“We pay close attention to the teachings of our ancestors, en are ne too proud to see that the seasons are ne the same as they used to be, the animals come en go, some pacts were broken, en new tribes moved in. Our village is bound to change as well, en we would be blind to think our teachings will never have to grow.” She stops and looks back, in the direction of {color=#f6d6bd}Howler’s{/color}, though you see only tree trunks and shrubs. “‘Tis true that these changes occur too fast for ma heart.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                $ custom1 = "“What else there is to say?”"
                jump howlersdell_steephouseconfrontationANTIthais02part2

    label howlersdell_steephouseconfrontation_elpis_argument_thais_aboutthais01:
        menu:
            '“Yet she’s trusted for her wits en talents.” Interrupted by a screeching bird, she seeks it among the leaves. “The {color=#f6d6bd}Thais{/color} you’ve met is shaped by many sorrows, but her laughter has ne always been as dead as ‘tis now. Many of us owe her our lives, en since our gathering promised to ne interfere with the choices of our neighbors, we took a step back, eva when we realized her {i}determination{/i} hides cruelty en stubbornness. Nae soul dares to oppose her now.”
            '
            '“How did she become a mayor in the first place?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How did she become a mayor in the first place?”')
                $ howlersdell_elpis_friendship += 1
                $ description_thais10 = "According to {color=#f6d6bd}Elpis{/color}: “Her parents were adventurers, they stayed with us after a few grand journeys, bringing many treasures en sacks of dragon rings. Realizing the illness of her weak shell, they wanted for her a life of comfort, without bloodshed. While others dug in soil or trained with spears, they taught her to count en read, then sent her with a caravan to {color=#f6d6bd}Hovlavan{/color}, used their ties to squeeze her into the guild. But the war disturbed her learning. She returned, en said she would protect us from the Southerners, as long as we trusted her. En she did. With poison en betrayal, aye. But she saved all of us.”"
                menu:
                    '“Her parents were adventurers, they stayed with us after a few grand journeys, bringing many treasures en sacks of dragon rings. Realizing the illness of her weak shell, they wanted for her a life of comfort, without bloodshed. While others dug in soil or trained with spears, they taught her to count en read, then sent her with a caravan to {color=#f6d6bd}Hovlavan{/color}, used their ties to squeeze her into the guild. But the war disturbed her learning. She returned, en said she would protect us from the Southerners, as long as we trusted her. En she did. With poison en betrayal, aye. But she saved all of us.”
                    '
                    '“She was ready to protect you in desperate days, I get it. But now, her decisions can bring only destruction. You need to find another way.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She was ready to protect you in desperate days, I get it. But now, her decisions can bring only destruction. You need to find another way.”')
                        $ howlersdell_steephouseconfrontation_elpis_points += 1
                        $ custom1 = "Her steps grow more confident. She nods in agreement."
                        jump howlersdell_steephouseconfrontation_elpis_argument_thais02
                    '“Your inaction helped her plans bloom. It’s time to do something about the responsibility that you carry.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your inaction helped her plans bloom. It’s time to do something about the responsibility that you carry.”')
                        $ custom1 = "She hesitates. “Nea one of us is free of guilt. The’s nae one soul who {i}ought to{/i} be a leader - only those who are trusted, either more, or less. If we were to follow your word, we would replace one tyrant with another.”"
                        jump howlersdell_steephouseconfrontation_elpis_argument_thais02
            '“Your inaction helped her plans bloom. It’s time to do something about the responsibility that you carry.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your inaction helped her plans bloom. It’s time to do something about the responsibility that you carry.”')
                $ custom1 = "She hesitates. “Nea one of us is free of guilt. The’s nae one who {i}ought to{/i} be a leader - only those who are trusted, either more, or less. If we were to follow your word, we would replace one tyrant with another.”"
                jump howlersdell_steephouseconfrontation_elpis_argument_thais02

    label howlersdell_steephouseconfrontation_elpis_argument_trust01:
        $ howlersdell_steephouseconfrontation_elpis_argument_trust = 1
        if howlersdell_elpis_friendship <= 1:
            $ howlersdell_steephouseconfrontation_elpis_points -= 3
            $ custom1 = "She stops in place and turns toward you, grasping her staff firmly. The anger you find in her ice-cold eyes and thin lips makes you think of another topic."
        elif howlersdell_elpis_friendship < 4:
            $ howlersdell_steephouseconfrontation_elpis_points -= 2
            $ custom1 = "She stops in place and turns toward you, grasping her staff. Her eyes are ice-cold, but not angry - mostly puzzled. You think of adding something, then carry on with your walk."
        elif howlersdell_elpis_friendship < 8:
            $ howlersdell_steephouseconfrontation_elpis_points -= 1
            $ custom1 = "She stops in place and turns toward you, holding her staff by her side. Her eyes are cold like a gentle rain. “I’m ne so sure, traveler.” You find no words to add, so you carry on with your walk."
        elif howlersdell_elpis_friendship >= 8 and howlersdell_reputation >= 10:
            $ howlersdell_steephouseconfrontation_elpis_points += 2
            $ custom1 = "She stops in place and turns toward you, holding her staff by her side. Her eyes are warm like a spring day, and she smiles gently. “I trust you, en so do ma neighbors. I can ne be sure what you’re saying is true, but I doubt you’re lying.”"
        else:
            $ howlersdell_steephouseconfrontation_elpis_points += 1
            $ custom1 = "She stops in place and turns toward you, holding her staff by her side. Her eyes are warm, betraying her cold voice. “I trust you, more so than ma neighbors. I’m ne one to close my ears to the warnings of others, but I doubt you’re one to lie.”"
        menu:
            '[custom1]
            '
            '“You must admit that what happened to the village was terrible.”' if not howlersdell_steephouseconfrontation_elpis_argument_steephouse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must admit that what happened to the village was terrible.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse01
            '“Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”' if not howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”')
                jump howlersdell_steephouseconfrontation_elpis_argument_thais01
            '{image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”' if not howlersdell_steephouseconfrontation_elpis_argument_trust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_trust01
            '{image=d6} “I also follow my ancestors. I’m trying to make things right.”' if not howlersdell_steephouseconfrontation_elpis_argument_faith and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I also follow my ancestors. I’m trying to make things right.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_faith01
            '“What’s your decision? Will you speak with the others?”' if howlersdell_steephouseconfrontation_elpis_argument_steephouse and howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your decision? Will you speak with the others?”')
                jump howlersdell_steephouseconfrontationANTIthais03

    label howlersdell_steephouseconfrontation_elpis_argument_faith01:
        $ howlersdell_steephouseconfrontation_elpis_argument_faith = 1
        if pc_faithpoints_opportunities >= 8:
            if pc_faithpoints+(achievement_animalssavedpoints/3) >= pc_faithpoints_opportunities:
                $ howlersdell_steephouseconfrontation_elpis_points += 2
                $ howlersdell_elpis_friendship += 1
                $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. Her hand is weak, but not gentle. Her blue eyes turn bright, then blink with shame. Without a word, she gives you a respectful nod and steps away."
            elif pc_faithpoints+(achievement_animalssavedpoints/3) >= (pc_faithpoints_opportunities*0.75):
                $ howlersdell_steephouseconfrontation_elpis_points += 1
                $ howlersdell_elpis_friendship += 1
                $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. Her hand is weak, but not gentle. Her blue eyes turn bright, she raises her chin respectfully. After a polite nod, she steps away."
            elif pc_faithpoints+(achievement_animalssavedpoints/3) >= (pc_faithpoints_opportunities*0.5):
                $ howlersdell_steephouseconfrontation_elpis_points += 0
                $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. Her hand is weak, but not gentle. Her blue eyes remain her color, but her frown is filled with disappointment. She releases her grasp and steps away, sparing you not even a word."
            elif pc_faithpoints+(achievement_animalssavedpoints/3) >= (pc_faithpoints_opportunities*0.25):
                $ howlersdell_steephouseconfrontation_elpis_points -= 1
                $ howlersdell_elpis_friendship -= 1
                $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. As her blue eyes turn the color of a thunderstorm, she takes away her hand and wipes it into her sleeve, making a disgusted wry."
            else:
                $ howlersdell_steephouseconfrontation_elpis_points -= 2
                $ howlersdell_elpis_friendship -= 1
                $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. Her hand is weak, but as her blue eyes turn the color of a thunderstorm, she pushes you away with a disgusted wry. “How dare you.”"
        else:
            $ howlersdell_steephouseconfrontation_elpis_points -= 1
            $ howlersdell_elpis_friendship -= 1
            $ custom1 = "She stops you in place and, without asking, squeezes your wrist, then spits on your open palm and stares into your face. Her hand is weak, but not gentle. Her blue eyes remain her color, but her frown is filled with disappointment. She releases her grasp and steps away. “But a weakling.”"
        menu:
            '[custom1]
            '
            '“You must admit that what happened to the village was terrible.”' if not howlersdell_steephouseconfrontation_elpis_argument_steephouse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must admit that what happened to the village was terrible.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_steephouse01
            '“Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”' if not howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really believe {color=#f6d6bd}Thais{/color} can stay? That she won’t cause further harm?”')
                jump howlersdell_steephouseconfrontation_elpis_argument_thais01
            '{image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”' if not howlersdell_steephouseconfrontation_elpis_argument_trust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “You know I’m trustworthy. I wouldn’t try to sabotage your neighbors.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_trust01
            '{image=d6} “I also follow my ancestors. I’m trying to make things right.”' if not howlersdell_steephouseconfrontation_elpis_argument_faith and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I also follow my ancestors. I’m trying to make things right.”')
                jump howlersdell_steephouseconfrontation_elpis_argument_faith01
            '“What’s your decision? Will you speak with the others?”' if howlersdell_steephouseconfrontation_elpis_argument_steephouse and howlersdell_steephouseconfrontation_elpis_argument_thais:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your decision? Will you speak with the others?”')
                jump howlersdell_steephouseconfrontationANTIthais03

    label howlersdell_steephouseconfrontationANTIthais03:
        $ quarters += 1
        if howlersdell_reputation >= 20:
            $ howlersdell_steephouseconfrontation_elpis_points += 4
        elif howlersdell_reputation >= 15:
            $ howlersdell_steephouseconfrontation_elpis_points += 3
        elif howlersdell_reputation >= 10:
            $ howlersdell_steephouseconfrontation_elpis_points += 2
        elif howlersdell_reputation >= 5:
            $ howlersdell_steephouseconfrontation_elpis_points += 1
        elif howlersdell_reputation < 0:
            $ howlersdell_steephouseconfrontation_elpis_points -= 3
        if howlersdell_steephouseconfrontation_elpis_points >= howlersdell_steephouseconfrontation_elpis_points_required:
            menu:
                'You approach a giant oak, older than any other tree in the garden. It’s surrounded by trails of shoes and paws, yet is oddly quiet, even though there are dozens of birds in its crown, spread among the branches like the faithful on temple pews.
                \n\n{color=#f6d6bd}Elpis{/color} reaches for the long claw marks left on the bark. She strokes them gently, makes a fist, and steps away. The cuts are now thinner, sealed like a wound, forming nothing more than a dark scar.
                \n\nSuddenly, the clamor of creatures tears the sky. You look up, but the singing, cawing, and twittering seems to have no cause - some birds raise their heads, others make tiny jumps or spread their wings, but they uphold their choir for a good few minutes, long after you and your companion leave them behind.
                \n\n“Let’s go back. {color=#f6d6bd}Thais{/color} will ne give us time to organize, I need to speak to ma gathering right away. But {i}I{/i} will be the one to speak with ma neighbors.”
                '
                '“You’re doing the right thing.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re doing the right thing.”')
                    $ custom1 = "“I do what I believe will cure our village,” her voice is cold. “Having a cityfolk’s encouragement only makes me doubtful. I do ne know your goals, but at least they seem to align with ours.”"
                    jump howlersdell_steephouseconfrontationANTIthais03success01
                '“Should we expect violence?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should we expect violence?”')
                    $ custom1 = "Her lips form a line. “From her? Always.”"
                    jump howlersdell_steephouseconfrontationANTIthais03success01
                '“I can handle this.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can handle this.”')
                    $ custom1 = "“You do ne even speak like one of us,” there’s venom in her soft voice. “Nae soul is going to make you our guide. All I need is to have you there en swear that your speech is honest.”"
                    label howlersdell_steephouseconfrontationANTIthais03success01:
                        menu:
                            '[custom1]
                            \n\nOn your way to the gate, you discuss the steps to come. Judging a mayor in power is no easy feat, not to mention seeking punishment for them or selecting their successor. The best you can hope for is that the locals will agree to hear your arguments and allow the druids to prepare a winter court. “Most of what we have to discuss involves {color=#f6d6bd}Steep House{/color}. You are ne needed for any of it,” {color=#f6d6bd}Elpis{/color} concludes.
                            '
                            '“Let’s get to it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get to it.”')
                                $ howlersdell_elpis_friendship += 2
                                $ howlersdell_reputation += 2
                                show areapicture howlersdellfull at basicfade
                                $ quarters += 6
                                $ renpy.music.play("audio/track_03howlersdell.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                                stop nature fadeout 4.0
                                nvl clear
                                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                                menu:
                                    'It’s an exhausting hour, and in this time you say only a few words. The amount of spite and reproach dwelling among the locals was hard to predict - it was not only the gathering who stood united behind {color=#f6d6bd}Elpis{/color}. She knew exactly who should be asked to speak out - the souls held in melancholy and guilt for ten years now, as well as those wounded during either the raid, or the earlier or later events, many of which you’d never heard of before.
                                    \n\n{color=#f6d6bd}Thais{/color}, accused of pointless violence and putting her pride above the well-being of her people, was calm at first, even eager to turn the entire case against you, but the trust you’ve earned and your familiarity with the raid’s cruelties shielded you from her manipulations. Finally, it comes to a vote.
                                    \n\n“For now, we see her as innocent, but suspicious,” announces the selected guard. “The court en judgment will occur in the middle of winter. Until then, she remains {color=#f6d6bd}our mayor{/color} in name only.”
                                    \n\nThe crowd disperses from the islet. If {color=#f6d6bd}Thais{/color} could curse people with her gaze, you would only have a few breaths left. The others seem either puzzled or suspicious, whispering between themselves, pointing at you, at the druids, at the guards, at the inn. Still, in their voices you recognize more excitement than worry.
                                    '
                                    'I return to {color=#f6d6bd}[horsename]{/color}.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}%s{/color}.' %horsename)
                                        $ quest_ruins = 2
                                        $ quest_ruins_choice = "thais_defeated"
                                        $ thais_afk = day
                                        $ thais_bigmad = 1
                                        $ thais_defeated = 1
                                        $ thais_friendship = -10
                                        if pc_goal == "iwanttoberemembered":
                                            $ pc_goal_iwanttoberememberedpoints += 2
                                        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                                            $ renpy.notify("Quest completed: The Ruined Village.\nJournal updated: %s" %quest_pc_goal_name)
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village. Journal updated: %s{/i}' %quest_pc_goal_name)
                                        else:
                                            $ renpy.notify("Quest completed: The Ruined Village")
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
                                        $ can_leave = 1
                                        if howlersdell_eryx_about_room:
                                            $ can_rest = 1
                                        $ can_items = 1
                                        menu:
                                            'Your mount welcomes you with a hearty snort and you pat its neck. Whatever happens now, you leave this place different than you found it - for better or worse.
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
            menu:
                'You approach a giant oak, older than any other tree in the garden. It’s surrounded by trails of shoes and paws, yet is oddly quiet, even though there are dozens of birds in its crown, spread among the branches like the faithful on temple pews.
                \n\n{color=#f6d6bd}Elpis{/color} reaches for the long claw marks left on the bark. She touches them with a palm of her hand gently, then scratches them with her fingernails, adding a few more cuts, fresh and dripping with sap.
                \n\nThe birds, still without as much as a caw, take off loudly, maybe a hundred of them at once, and in such a panic that a few of them crash into branches or one another. Before you can take a closer look, your companion moves her staff in front of you, then nods for you to follow her away from here. You glance at the claw marks once more - worms are already rushing toward them.
                \n\nAfter another minute of the stroll, the woman speaks again. “I can ne help you. It may be better for you to stay away from {color=#f6d6bd}Howler’s Dell{/color} from this day on - {color=#f6d6bd}Thais{/color} is ne kind to her enemies.”
                '
                '“We could just keep it between us.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We could just keep it between us.”')
                    $ custom1 = "“Do ne be naive,” she says with pity. “You think she does ne know already why you came to see me? That nae one here,” she raises her weapon and points at one of the scouts, “is wearing a spell to hear us? She’ll ask me, en {i}I{/i} will ne lie to her.”"
                    jump howlersdell_steephouseconfrontationANTIthais03fail01
                '“Have you no shame? You’re leading innocent souls to their deaths.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you no shame? You’re leading innocent souls to their deaths.”')
                    $ custom1 = "Her lips form a line, but she spares you not a word of response. She quickens her pace, holding her weapon firmly."
                    $ howlersdell_elpis_friendship -= 2
                    jump howlersdell_steephouseconfrontationANTIthais03fail01
                '“I ask you to reconsider.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I ask you to reconsider.”')
                    $ custom1 = "“I can ne sacrifice the future of ma village for your games. You’re but a stranger,” she says it like an insult."
                    label howlersdell_steephouseconfrontationANTIthais03fail01:
                        menu:
                            '[custom1]
                            \n\nYour steps are heavy. You look around - not only would you not escape the scouts and hunters, your mount and equipment are still in the village. You try to come up with a new argument, a point of view, to remind yourself of something you’ve seen in the ruins...
                            '
                            'I’ve nothing more to say.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve nothing more to say.')
                                show areapicture howlersdellfull at basicfade
                                $ quarters += 2
                                if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
                                    play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
                                stop nature fadeout 4.0
                                nvl clear
                                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                                menu:
                                    'Soon after you enter the gates, you’re welcomed by five guards, led by {color=#f6d6bd}the mayor{/color} herself. “You have something to tell me, forest speaker?” She asks {color=#f6d6bd}your companion{/color} and spares you little more than a disdainful chuckle.
                                    \n\nYou’re led into {color=#f6d6bd}Ape Ale{/color} and placed on a chair, with a muscular hand keeping you in place. {color=#f6d6bd}Elpis{/color} hides nothing, not even her own willingness to listen to your accusations. You follow the guards’ faces - no matter what they hear, they obediently observe their boss, putting their trust in her decisions.
                                    \n\nFinally, the first kick reaches your stomach. You can’t even tell which word or gesture led to it, but it’s soon followed by a hit in the jaw. “Go,” {color=#f6d6bd}Thais{/color} tells {color=#f6d6bd}the druidess{/color}, who leaves without a word.
                                    '
                                    '“Please...”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Please...”')
                                        jump howlersdell_steephouseconfrontationANTIthais03fail02
                                    '“I’m warning you!”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m warning you!”')
                                        jump howlersdell_steephouseconfrontationANTIthais03fail02
                                    'I say nothing.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                                        label howlersdell_steephouseconfrontationANTIthais03fail02:
                                            $ quarters += 1
                                            $ quest_ruins = 3
                                            if item_howlersdelltoken:
                                                $ item_howlersdelltoken = 0
                                                $ renpy.notify("You lost the “token of gratitude.”\nQuest completed: The Ruined Village")
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the “token of gratitude.” Quest completed: The Ruined Village{/i}')
                                            else:
                                                $ renpy.notify("Quest completed: The Ruined Village")
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
                                            $ quest_ruins_choice = "thais_won"
                                            $ thais_afk = day
                                            $ thais_bigmad = 1
                                            $ thais_friendship = -10
                                            $ howlersdell_reputation -= 5
                                            $ pc_hp = limit_pc_hp(pc_hp-3)
                                            show minus3hp at hpchange onlayer myoverlay
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                            if not cleanliness_clothes_blood:
                                                show minus1appearance at appearancechange onlayer myoverlay
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                                                $ cleanliness_clothes_blood = 1
                                            menu:
                                                'The beating is short, but effective. The blood from your mouth covers your clothes, your ribs ache at every move. “You’re still a roadwarden, so {i}I guess{/i} we ought to let you be,” {color=#f6d6bd}the mayor’s{/color} voice is bored and carries not a hint of the cityfolk accent. “Now get out, en do ne return unless you’re going to handsomely {i}support{/i} our artisans.”
                                                \n\nYou place careful steps through the square, surrounded by whispers and worried looks. Your mount welcomes you with a hearty snort, but to you it sounds like mockery. Tasting iron, you wash your mouth and think of the last smirk formed on {color=#f6d6bd}Thais’{/color} wine-colored lips - {i}I won{/i}.
                                                '
                                                'I head to the gate and climb on the saddle.':
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the gate and climb on the saddle.')
                                                    $ travel_destination = "westerncrossroads"
                                                    jump finaldestinationafterevent

label howlersdell_steephouseconfrontationPROthaisALL:
    label howlersdell_steephouseconfrontationPROthais00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could offer {color=#f6d6bd}Thais{/color} an alliance... In exchange for my silence.')
        menu:
            'You gather your thoughts, but it’s hard to predict her response. If she sees you only as a threat, she may spare you little patience - or mercy.
            '
            'Time to use both her trust and my knowledge.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to use both her trust and my knowledge.')
                jump howlersdell_steephouseconfrontationPROthais01
            'I have second thoughts...':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have second thoughts...')
                jump howlersdell_steephouseconfrontation00alt

    label howlersdell_steephouseconfrontationPROthais01:
        $ quarters += 1
        show areapicture howlersdellbehindinn01 at basicfade
        hide howlersdellsquareutensils
        $ renpy.music.play("audio/track_12steephouse.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            '“We need to talk. Just the two of us,” you start with a serious look, and soon after you sit down by the creek, away from curious glances.
            \n\n“I hope you’re bringing {i}good{/i} news, [pcname].” Her confident voice is strengthened by her smile, but her foot is dangling nervously, playing with her sandal. The air is filled with the scent of roses, but the green cape on her shoulder forms a wall between you.
            '
            '“I’ve learned of what you did to {color=#f6d6bd}Steep House{/color}. If you don’t want the city officials to learn the truth, you’re going to make me a tasty offer.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve learned of what you did to {color=#f6d6bd}Steep House{/color}. If you don’t want the city officials to learn the truth, you’re going to make me a tasty offer.”')
                $ custom1 = "“So you’re ready to finally flex your muscles. I thought you’d be smarter than that, though.” She’s holding her buckle, stroking its antlers. Without meeting your eyes, her voice turns squeaky and trembling. “{i}Honorable chief, I do ne understand!” She sounds both like a desperate girl and a confused elder. She raises her hands pleadingly, directing them at an invisible judge. “{color=#f6d6bd}Steep House{/color} en we were in conflict for many years! They took our mouflons en beat our farmers, eva ma own son! We retaliated, yes, but with no cruelty, en we would never wish angry spirits upon them!{/i}”\n\nShe covers her mouth with her fist and clears her throat. “It’s been a long while since I’ve had to do that. It’s your word against mine. And whoever you think is going to speak ill of me,” she leans back and puts her pale hand on your shoulder, giving you a disarming smile, “think again. Every soul has something to lose, en I’m {i}very{/i} good at taking things.”"
                jump howlersdell_steephouseconfrontationPROthais02
            '“I enjoy our collaboration, {color=#f6d6bd}Thais{/color}, I do. I want to help you keep what happened in {color=#f6d6bd}Steep House{/color} between the Northerners, but it goes against my duties. I want to be sure you’ll make my efforts worth the risk.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I enjoy our collaboration, {color=#f6d6bd}Thais{/color}, I do. I want to help you keep what happened in {color=#f6d6bd}Steep House{/color} between the Northerners, but it goes against my duties. I want to be sure you’ll make my efforts worth the risk.”')
                $ thais_friendship += 1
                $ custom1 = "“So considerate of you! But you should already know we can handle ourselves.” She’s holding her buckle, stroking its antlers. Without meeting your eyes, her voice turns squeaky and trembling. “{i}Honorable chief, I do ne understand!” She sounds both like a desperate girl and a confused elder. She raises her hands pleadingly, directing them at an invisible judge. “{color=#f6d6bd}Steep House{/color} en we were in conflict for many years! They took our mouflons en beat our farmers, eva ma own son! We retaliated, yes, but with no cruelty, en we would never wish angry spirits upon them!{/i}”\n\nShe covers her mouth with her fist and clears her throat. “It’s been a long while since I’ve had to do that. I can handle {i}very{/i} uncomfortable questions, and even if {color=#f6d6bd}Hovlavan{/color} was to charge me with {i}despicable deeds{/i}, they’ll never send enough forces to drag me out of here.” Her pale fingers start to playfully tap against your arm as she gives you a disarming smile. “We can build our own silence, with or without your help.”"
                jump howlersdell_steephouseconfrontationPROthais02

    label howlersdell_steephouseconfrontationPROthais02:
        menu:
            '[custom1]
            '
            '“First, hear me. I’ve managed to learn {i}quite a bit{/i}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “First, hear me. I’ve managed to learn {i}quite a bit{/i}.”')
                $ custom1 = "“It’s not so easy to surprise me, but go ahead. Entertain me.”"
                jump howlersdell_steephouseconfrontationPROthais03
            '“Don’t get cocky.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t get cocky.”')
                $ custom1 = "She chuckles. “Or what?”"
                jump howlersdell_steephouseconfrontationPROthais03

    label howlersdell_steephouseconfrontationPROthais03:
        menu:
            '[custom1]
            '
            '“You left strong evidence of your malicious intent. The fields of {color=#f6d6bd}Steep House{/color} still bear the curse. It would be difficult to explain yourself out of this.”' if quest_ruins_insideclues06 and not howlersdell_steephouseconfrontation_thais_argument_curse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='-“You left strong evidence of your malicious intent. The fields of {color=#f6d6bd}Steep House{/color} still bear the curse. It would be difficult to explain yourself out of this.”')
                $ howlersdell_steephouseconfrontation_thais_argument_curse = 1
                $ howlersdell_steephouseconfrontation_thais_points += 3
                $ custom1 = "She opens her mouth slightly, but then exhales loudly and keeps staring in the distance."
                jump howlersdell_steephouseconfrontationPROthais03
            '“I saw the tree painted with blood inside one of the buildings. Who knows how many clues another roadwarden could find there...”' if quest_ruins_treepicture and not howlersdell_steephouseconfrontation_thais_argument_treepicture:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw the tree painted with blood inside one of the buildings. Who knows how many clues another roadwarden could find there...”')
                $ howlersdell_steephouseconfrontation_thais_argument_treepicture = 1
                $ howlersdell_steephouseconfrontation_thais_points += 3
                $ custom1 = "“And I’m to assume {i}you{/i} could clear that place for good?” Seeing your shrug, she clicks her tongue. “Too bad it didn’t burn to the ground. Now, when it’s overrun by birds and rats, we shouldn’t take down their lairs.”"
                jump howlersdell_steephouseconfrontationPROthais03
            '“We both know you and {color=#f6d6bd}Elpis{/color} don’t always see eye to eye. You don’t want to reveal the weaknesses of your old plans.”' if howlersdell_elpis_about_thais and not item_thaisletter_read and not howlersdell_steephouseconfrontation_thais_argument_elpis:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We both know you and {color=#f6d6bd}Elpis{/color} don’t always see eye to eye. You don’t want to reveal the weaknesses in your old plans.”')
                $ howlersdell_steephouseconfrontation_thais_argument_elpis = 1
                $ howlersdell_steephouseconfrontation_thais_points += 1
                $ custom1 = "“There are many ways to prove that I can handle such difficulties,” she narrows her eyes. “If anything, I’d do better by {i}removing{/i} threats, not hiding them.”"
                jump howlersdell_steephouseconfrontationPROthais03
            '“You {i}care{/i} about the deal with the city. So much so that you’re willing to invite Wright’s priests. I could speak with them, make sure they realize it’s a {i}delicate{/i} matter.”' if item_thaisletter_read and not howlersdell_elpis_about_thais and not howlersdell_steephouseconfrontation_thais_argument_thaisletter:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You {i}care{/i} about the deal with the city. So much so that you’re willing to invite Wright’s priests. I could speak with them, make sure they realize it’s a {i}delicate{/i} matter.”')
                $ howlersdell_steephouseconfrontation_thais_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_thais_points += 2
                $ custom1 = "“What sort of messenger opens a sealed letter?” She takes a deep breath, but you notice a hint of admiration in her eyes."
                jump howlersdell_steephouseconfrontationPROthais03
            '“You {i}care{/i} about the deal with the city. So much so that you’re willing to invite Wright’s priests. I could speak with them, make sure they realize it’s a {i}delicate{/i} matter. After all, you and {color=#f6d6bd}Elpis{/color} don’t always see eye to eye.”' if item_thaisletter_read and howlersdell_elpis_about_thais and not howlersdell_steephouseconfrontation_thais_argument_thaisletter:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You {i}care{/i} about the deal with the city. So much so that you’re willing to invite Wright’s priests. I could speak with them, make sure they realize it’s a {i}delicate{/i} matter. After all, you and {color=#f6d6bd}Elpis{/color} don’t always see eye to eye.”')
                $ howlersdell_steephouseconfrontation_thais_argument_elpis = 1
                $ howlersdell_steephouseconfrontation_thais_argument_thaisletter = 1
                $ howlersdell_steephouseconfrontation_thais_points += 4
                $ custom1 = "“What sort of messenger opens a sealed letter?” Her eyes widen, staring at you with admiration. “There are many ways for me to prove I can handle all sorts of obstacles. If anything, I’d do better {i}removing{/i} the threats, not hiding them.” She gives you a telling look."
                jump howlersdell_steephouseconfrontationPROthais03
            '“I know for a fact you hide the truth about your ride from the younger generation. You don’t want someone here who would ask the {i}wrong{/i} questions to the {i}wrong{/i} souls.”' if howlersdell_steephouseconfrontation_childrenshame and not howlersdell_steephouseconfrontation_thais_argument_childrenshame:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know for a fact you hide the truth about your ride from the younger generation. You don’t want someone here who would ask the {i}wrong{/i} questions to the {i}wrong{/i} souls.”')
                $ howlersdell_steephouseconfrontation_thais_argument_childrenshame = 1
                $ howlersdell_steephouseconfrontation_thais_points += 1
                $ custom1 = "Her piercing gaze makes you look away. You hit where it hurts."
                jump howlersdell_steephouseconfrontationPROthais03
            '“Do you regret what you did to those people?”' if not howlersdell_steephouseconfrontation_thais_argument_regret:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you regret what you did to those people?”')
                $ howlersdell_steephouseconfrontation_thais_argument_regret = 1
                $ pc_faithpoints_opportunities += 1
                menu:
                    'She adjusts her dress, giving you a puzzled look. “Does it really matter?”
                    '
                    '“It would be helpful to know you don’t plan to repeat your deeds.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It would be helpful to know you don’t plan to repeat your deeds.”')
                        $ thais_friendship -= 1
                        $ custom1 = "She gives you a mocking glance, then looks away. “Of course I don’t.”"
                        jump howlersdell_steephouseconfrontationPROthais03
                    '“Of course. And so does admitting you’re wrong.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Of course. And so does admitting you’re wrong.”')
                        $ thais_friendship -= 1
                        $ pc_faithpoints += 1
                        $ custom1 = "“I seek no forgiveness,” she says after a long pause, “and I don’t need you to understand why.”"
                        jump howlersdell_steephouseconfrontationPROthais03
                    '“I guess not.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess not.”')
                        $ thais_friendship += 1
                        $ custom1 = "“Yeah,” her eyes soften. “Feelings are but an obstacle.”"
                        jump howlersdell_steephouseconfrontationPROthais03
            '“Did they actually steal your mouflons?”' if howlersdell_steephouseconfrontation_thais_argument_regret and not howlersdell_steephouseconfrontation_thais_argument_mouflons:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did they actually steal your mouflons?”')
                $ howlersdell_steephouseconfrontation_thais_argument_mouflons = 1
                $ custom1 = "She snorts and clasps her hands around her knee."
                jump howlersdell_steephouseconfrontationPROthais03
            '“I’ve told you enough. Do with it as you please.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve told you enough. Do with it as you please.”')
                jump howlersdell_steephouseconfrontationPROthaisRESULT01

    label howlersdell_steephouseconfrontationPROthaisRESULT01:
        $ howlersdell_steephouseconfrontation_thais_points += (thais_friendship/2)
        if howlersdell_steephouseconfrontation_thais_points >= howlersdell_steephouseconfrontation_thais_points_required:
            menu: # success
                '{color=#f6d6bd}Thais{/color} sighs, stands up, and approaches the bank, staring in the distance. Her arms are crossed, and for once she doesn’t pay attention to her loose strands of hair.
                \n\n“I must admit, your words make me hesitant.” Thanks to your recent conversations, the remains of the local accent have now completely left her voice. “We had a good run so far, you and I. Let’s keep it that way. Leave us,” she says to no one in particular, and you hear footsteps leaving the boar pen. Whoever was there, they must have heard everything you’ve been talking about so far.
                \n\nShe meets your eyes. “Whatever happens, you’ll have my support. Want to stay with us? You’ll live in peace and comfort, as {i}our{/i} warden. Of course, I won’t bother you with too many tasks, just enough to put down any questions. And if you were to find someone to your liking among us... We’ll figure something out.” There’s cruelty in her smile, but also complete confidence.
                \n\n“If you’d rather stay with the guild, we’ll make sure they’ll {i}have to{/i} keep you around as my {i}trusted envoy{/i}. Once the deal is complete, you’ll get a nice chunk of our taxes. In a few years, you’ll secure yourself a small fortune. But I’d also like to cut a new path to the guild for myself. Together, we could go far.”
                \n\nShe raises her chin.
                '
                '“We’ve got a deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve got a deal.”')
                    $ custom1 = "“Very well,” she adjusts her purple dress and looks up."
                    jump howlersdell_steephouseconfrontationPROthaisRESULTsuccess01
                '“Lovely!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Lovely!”')
                    $ custom1 = "There’s something different in her laughter. It’s much shorter, and for once doesn’t avoid her green eyes."
                    jump howlersdell_steephouseconfrontationPROthaisRESULTsuccess01
                'I reach out to her.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach out to her.')
                    $ custom1 = "Her soft hand may be fragile, but the spark in her green eyes reminds you of her strength."
                    label howlersdell_steephouseconfrontationPROthaisRESULTsuccess01:
                        $ quarters += 1
                        $ thais_friendship += 5
                        # $ renpy.music.play("audio/track_03howlersdell.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                        $ howlersdell_reputation += 2
                        $ quest_ruins = 2
                        $ quest_ruins_choice = "thais_alliance"
                        if pc_goal == "iwantstatus":
                            $ pc_goal_iwantstatuspoints += 3
                        if pc_goal == "iwanttostartanewlife":
                            $ pc_goal_iwantnewlife_howlersdell = 1
                        if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                            $ renpy.notify("Quest completed: The Ruined Village.\nJournal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village. Journal updated: %s' %quest_pc_goal_name)
                        elif pc_goal == "iwanttostartanewlife":
                            $ renpy.notify("Quest completed: The Ruined Village.\nJournal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village. Journal updated: %s' %quest_pc_goal_name)
                        else:
                            $ renpy.notify("Quest completed: The Ruined Village")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
                        show areapicture howlersdellsquare01 at basicfade behind howlersdellsquareutensils
                        if quarters < 39:
                            show howlersdellsquareutensils 02 at basicfade
                        elif quarters < (world_daylength-28):
                            show howlersdellsquareutensils 03 at basicfade
                        elif quarters < (world_daylength-12):
                            show howlersdellsquareutensils 01 at basicfade
                        else:
                            show howlersdellsquareutensils 04 at basicfade
                        $ questionpreset = "thais1"
                        menu:
                            '[custom1] “Let’s get back. Lengthy conversations without witnesses are in bad taste for a mayor.”
                            \n\nShe leads you back to your usual table, stopping for a minute to chat with a farmer briefly, but also to pick up one of her younger sons, laughing at his big yawn.
                            \n\nBefore she joins you, you look at the nearby faces and listen to the innkeep, who shares a laugh with his neighbors. This could be your home.
                            '
                            '(thais1 preset)':
                                pass
        else:
            menu: # fail
                '{color=#f6d6bd}Thais{/color} sighs, stands up, and approaches the bank, staring in the distance. Her arms are crossed, and for once she doesn’t pay attention to her loose strands of hair.
                \n\n“I’ve listened, but I’m ne impressed,” she raises her voice slightly, with no trace of the cityfolk accent left. “You can come out. Take the outsider upstairs.”
                \n\nYou hear footsteps. Three armed men jump over the fence and dash toward you. You spring up, but seeing the crossbow aimed at your chest, you don’t reach for your blade. Soon, someone grabs your hands and pulls them behind your back.
                '
                '“What are you going to do, {color=#f6d6bd}Thais{/color}?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are you going to do, {color=#f6d6bd}Thais{/color}?”')
                    $ custom1 = "“Teach you a lesson,” she shrugs without sparing you so much as a glance. "
                    jump howlersdell_steephouseconfrontationPROthaisRESULTfail01
                'I look a guard in the eyes. “Let me go, or you’ll face consequences.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look a guard in the eyes. “Let me go, or you’ll face consequences.”')
                    $ custom1 = "“Somehow I doubt it,” he scoffs. "
                    jump howlersdell_steephouseconfrontationPROthaisRESULTfail01
                'Shit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Shit.')
                    $ custom1 = ""
                    label howlersdell_steephouseconfrontationPROthaisRESULTfail01:
                        menu:
                            '[custom1]The guards disarm you swiftly. After a kick in the stomach, you lean forward, allowing someone to hold your neck low. They lead you into the square - you hear gasps and moving chairs. The locals chatter and get to their feet, but no one comes to the rescue.
                            \n\nOnce you’re in {color=#f6d6bd}Ape Ale’s{/color} main chamber, you’re thrown on the floor. The fighters surround you, taking off their heavy equipment and cracking their knuckles. Two more have already joined them.
                            \n\nYou catch a whiff of burning stew.
                            '
                            '“Please...”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Please...”')
                                jump howlersdell_steephouseconfrontationPROthaisRESULTfail02
                            '“I’m warning you...”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m warning you...”')
                                jump howlersdell_steephouseconfrontationPROthaisRESULTfail02
                            'I say nothing.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                                label howlersdell_steephouseconfrontationPROthaisRESULTfail02:
                                    $ quarters += 1
                                    $ quest_ruins = 3
                                    if item_howlersdelltoken:
                                        $ item_howlersdelltoken = 0
                                        $ renpy.notify("You lost the “token of gratitude.”\nQuest completed: The Ruined Village")
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the “token of gratitude.” Quest completed: The Ruined Village{/i}')
                                    else:
                                        $ renpy.notify("Quest completed: The Ruined Village")
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Ruined Village{/i}')
                                    $ quest_ruins_choice = "thais_alliance_fail"
                                    $ thais_afk = day
                                    $ thais_bigmad = 1
                                    $ thais_friendship = -10
                                    $ howlersdell_reputation -= 5
                                    $ pc_hp = limit_pc_hp(pc_hp-3)
                                    show minus3hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                    if not cleanliness_clothes_blood:
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                                        $ cleanliness_clothes_blood = 1
                                    menu:
                                        'The beating is short, but effective. The blood from your mouth covers your clothes, your ribs ache at every move. You don’t even notice when {color=#f6d6bd}the mayor{/color} joins you. “You’re still a roadwarden, so {i}I guess{/i} we ought to let you be. Now get out, en do ne return unless you’re going to handsomely {i}support{/i} our artisans.”
                                        \n\nYou place careful steps through the square, surrounded by whispers and worried looks. Your mount welcomes you with a heartfy snort, but to you it sounds like mockery. Tasting iron, you wash your mouth and think of the last smirk formed on {color=#f6d6bd}Thais’{/color} wine-colored lips - {i}I won{/i}.
                                        '
                                        'I head to the gate and climb on the saddle.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the gate and climb on the saddle.')
                                            $ travel_destination = "westerncrossroads"
                                            jump finaldestinationafterevent
