###################### Iason
default iason_name = "Pelt’s innkeep"
default iason_friendship = 0
default iason_dayofvisit = 0
default iason_stance = "behindcounter" # "behindcounter", "swiping", "sittingatstove", "sittingattable"

default iason_food_day = 0
default iason_food_roll = 0
default iason_food = 0
default iason_food_berries = 0
default iason_food_berries_refused = 0
default iason_food_berries_day = 0

default iason_shop = 0
default iason_shop_foodrations_day = 0
default iason_shop_furprice_base = 0
default iason_shop_furprice = 0
default iason_shop_furbought = 0
default iason_shop_soap = 0
default iason_shop_potion_10coins = 0
default iason_shop_potions_sold = 0
default iason_shop_potions_block = 0
default iason_shop_quarrels = 0
default iason_shop_shield_price = 5
default iason_shop_shield = 0
default iason_shop_shield_bought = 0
default iason_shop_shield_announced = 0
default iason_shop_wine = 0
default iason_shop_cidercask_price = 7
default iason_shop_bow_price = 10
default iason_shop_potion_price = 8
default iason_shop_ironingot_price = 18
default iason_shop_crossbow_price = 30
default iason_shop_crossbow_discount = 0
default iason_shop_crossbow_bought = 0
default iason_shop_wingedhourglass_sold = 0

default iason_freeroom = 0
default iason_about_ban = 0
default iason_about_pagans = 0
default iason_about_pagans_hunterdruid = 0
default iason_about_pagans_encourages = 0
default iason_about_tertia = 0
default iason_about_hava = 0
default iason_about_highisland = 0
default iason_about_steephouse = 0
default iason_about_steephouse_gray = 0
default iason_about_steephouse_price_base = 40
default iason_about_steephouse_price = 0

default iason_about_fish = 0
# default iason_fish_delivered = 0 # out of iason_fish_delivered_max
# default iason_fish_delivered_max = 10
default iason_fish_delivered_total = 0
default iason_fish_delivered_current = 0
default iason_fish_frienship_level = 6

default iason_about_asterion1 = 0
default iason_about_asterion_found = 0
default iason_about_directions = 0
default iason_about_directions_west = 0
default iason_about_directions_east = 0
default iason_about_directions_north = 0
default iason_about_inn = 0
default iason_about_inn_bonus1 = 0
default iason_about_inn_bonus2 = 0
default iason_about_quest_glaucia = 0
default iason_about_quest_glaucia_thais = 0
default iason_about_plague = 0
default iason_about_nomoreundead = 0
default iason_about_workforquintus = 0

default iason_rumors_threshold = 0
default iason_rumors_introduction = 0
default iason_about_eudocia_parents = 0
default iason_about_akakios = 0
default iason_about_missinghunters = 0
default iason_about_navica = 0
default iason_about_timo = 0
default iason_about_severina = 0
default iason_about_greenmountaintribe = 0
default iason_about_whitemarshes_destroyed = 0
default iason_about_nalia = 0
default iason_about_prelate = 0
default iason_about_shortcut_bandit = 0
default iason_about_valens = 0
default iason_about_jocasta = 0

default iason_alliance_threshold = 14
default iason_alliance = 0

label peltnorthfirstvisit04:
    $ shop = "peltnorth"
    $ renpy.notify("New shelter unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
    $ peltnorth_resting = 1
    show areapicture peltnorth01insidemug at basicfade
    $ iason_stance = "behindcounter"
    if quarters <= (world_daylength-12):
        $ custom2 = "“You’re lucky to show up,” his voice is deep and soft, with a city-like accent. He observes you with keen attention, yet avoids your eyes. “I’ve a keg of decent ale. Wormwood, bog myrtle, juniper berries, catsfoot...” He fills a mug carefully and puts it on the countertop. “It’s going to spoil soon, today maybe, and we don’t drink here before the even. I hate to see the good stuff going to waste.”"
    else:
        $ custom2 = "“You’re lucky to show up,” his voice is deep and soft, with a city-like accent. He observes you with keen attention, yet avoids your eyes. “I’ve a keg of decent ale. Wormwood, bog myrtle, juniper berries, catsfoot...” He fills a mug carefully and puts it on the countertop. “It’s going to spoil before tomorrow, so we need to drink as much as we can. I hate to see the good stuff going to waste.”"
    if quarters < 36:
        $ peltnorthroomdescription = "The locked windows make the air stuffy, and the weak fire in the stove hardly lightens up the hall."
    elif quarters < 48:
        $ peltnorthroomdescription = "Only some of the windows are open, revealing the dust dancing in the sunbeams. The air is a bit stuffy."
    elif quarters < (world_daylength-60):
        $ peltnorthroomdescription = "The windows are open, but the heat of the burning stove makes you warm."
    elif quarters < world_daylength:
        $ peltnorthroomdescription = "The open windows fill the hall with refreshing air and the sounds of conversations."
    else:
        $ peltnorthroomdescription = "The locked windows make the air stuffy, and both the counter and the tables are lit with candles."
    menu:
        '[peltnorthroomdescription] {color=#f6d6bd}A muscular man{/color} is sweeping the floor near the stairs, but after he glances at you, he leans the broom against the wall and heads behind the counter.
        \n\n[custom2]
        \n\nHis skin is dark, almost purple, rare even among The Southern Tribes, and his hair is naturally blueish. His clothes are quite fancy for manual labor - the elegant tunic wouldn’t stand out in the city square.
        '
        'I stand at the counter.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand at the counter.')
            if quarters < 36:
                $ tutorial_restatinn = 1
            $ at_activate = 1
            $ at = 0
            menu:
                'The planks let out a creak after every step you make, so you slow down a bit. You could swear that {color=#f6d6bd}the innkeeper{/color} made little to no noise.
                \n\n“Here you go,” he pushes the mug forward. “But just so you know, my {color=#f6d6bd}Pelt of the North{/color} doesn’t belong to {color=#f6d6bd}Hovlavan{/color}. You can sleep on the floor if you wish so, but if you want a bed or a meal, you have to pay. We may have some leftovers from dinner, but I’d need to check.”
                '
                ' (disabled)' ( condition="at == 0" ):
                    pass
                '“Thanks for the drink. I see you know how to make friends with a roadwarden.”' ( condition="at == 'friendly'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Thanks for the drink. I see you know how to make friends with a roadwarden.”')
                    $ at_activate = 0
                    $ at = 0
                    $ iason_friendship -= 1
                    menu:
                        'He meets your eyes with a puzzled look, then grabs a wet cloth and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in a wooden bucket.
                        \n\n“Well, nothing is truly free. I have work for a soul of the road, but I don’t need a new mouth to babble.” He speaks slowly, yet audibly. “I value my time, you should value yours.”
                        '
                        'I drink the ale.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drink the ale')
                            jump peltnorthfirstvisit06ale
                        'I ignore the ale and tell the man I have a couple of questions.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore the ale and tell the man I have a couple of questions.')
                            jump peltnorthregularquestionsv01
                '“Happy to help! As a roadwarden, I’m more than capable of taking care of the entire cask, if you need me to.”' ( condition="at == 'playful'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Happy to help! As a roadwarden, I’m more than capable of taking care of the entire cask, if you need me to.”')
                    $ at_activate = 0
                    $ at = 0
                    $ iason_friendship -= 2
                    menu:
                        'He sighs, grabs a wet cloth, and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in a wooden bucket.
                        \n\n“You’re already making me regret this,” he speaks slowly, yet audibly. “What do you want?”
                        '
                        'I drink the ale.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drink the ale')
                            jump peltnorthfirstvisit06ale
                        'I ignore the ale and tell the man I have a couple of questions.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore the ale and tell the man I have a couple of questions.')
                            jump peltnorthregularquestionsv01
                '“I won’t stay here for long.” I introduce myself.' ( condition="at == 'distanced'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I won’t stay here for long.” I introduce myself.')
                    $ at_activate = 0
                    $ at = 0
                    $ iason_friendship += 1
                    menu:
                        'He nods and fills another mug, this time with water.
                        \n\n“I guess there’s no point in waiting for {color=#f6d6bd}Asterion{/color}, then. I’m glad to see someone taking his place. Even my crew here hits the road only if they need to see the healers of {color=#f6d6bd}Howler’s Dell{/color}, and they’re more than resourceful. A roadwarden is always going to find work here, in the North. Though maybe not on the eastern road.”
                        \n\nHe takes a mouthful of water and drinks it with a pleased sigh.
                        \n\n“There are no guests here at this time, or hardly ever. I can take a short break.” For a brief moment, he meets your eyes.
                        '
                        'I drink the ale.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drink the ale')
                            jump peltnorthfirstvisit06ale
                        'I ignore the ale and tell the man I have a couple of questions.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore the ale and tell the man I have a couple of questions.')
                            jump peltnorthregularquestionsv01
                '“I’m not here to pay compliments to piss in a mug. I’m a roadwarden, and I’m looking for answers.”' ( condition="at == 'intimidating'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I’m not here to pay compliments to piss in a mug. I’m a roadwarden, and I’m looking for answers.”')
                    $ at_activate = 0
                    $ at = 0
                    jump peltnorthfirstvisit06intimidating
                '“Thank you. I’m a roadwarden, so I’d never refuse a free drink.”' ( condition="at == 'vulnerable'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Thank you. I’m a roadwarden, so I’d never refuse a free drink.”')
                    $ at_activate = 0
                    $ at = 0
                    menu:
                        'He meets your eyes with a frown, then grabs a wet cloth and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in a wooden bucket.
                        \n\n“Just don’t get used to it. Coins aren’t worth much here, in the North, surely less than work. And there are days of hunger,” he speaks slowly, yet audibly. “You won’t fill your stomach with words alone.”
                        '
                        'I drink the ale.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drink the ale')
                            jump peltnorthfirstvisit06ale
                        'I ignore the ale and tell the man I have a couple of questions.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore the ale and tell the man I have a couple of questions.')
                            jump peltnorthregularquestionsv01

    label peltnorthfirstvisit06intimidating: #“I don’t have time to help you feel better about some piss in a mug. I’m here to find answers.”
        $ iason_friendship -= 2
        $ dalit_friendship -= 1
        menu:
            'His face shifts from indifference to anger.
            \n\n“Now listen here! This inn ain’t a shelter for brigands, no matter if they work for The Cities or not! You better know your place, goblin-ass!”
            \n\nHe grabs a mace with a head made of bronze that was resting behind the counter. “I need no guards to knock your head off.”
            \n\nEven though he says so, the door opens. Harsh looks and blades fill up the room.
            '
            'I apologize. “I’m not looking for trouble.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I apologize. “I’m not looking for trouble.”')
                $ peltnorth_ban_temp = day
                $ iason_friendship += 1
                $ quarters += 1
                if quarters <= (world_daylength-4):
                    show areapicture peltnorth01 at basicfade
                    $ can_leave = 1
                    $ can_items = 1
                    menu:
                        '“I couldn’t care less,” {color=#f6d6bd}the innkeeper{/color} responds, but his posture relaxes a bit. He asks for your name and trade, then points at the door with his mace. “You ain’t welcome here. Come back tomorrow, get your shit together.”
                        \n\nYou pass the guards. They observe you with caution, but you can see they don’t really treat you like a threat. Most of their weapons are still hidden or sheathed. They move aside to let you get to the door and assist you on the way to {color=#f6d6bd}[horsename]{/color}. They keep their distance, talking about their next hunting trip. You pack your things - it looks like nothing is missing.
                        '
                        'I ride through the gate and leave the inn. (disabled)':
                            pass
                else:
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        '“I couldn’t care less,” {color=#f6d6bd}the innkeeper{/color} responds, but lowers his weapon. He asks for your name, then points his mace at one of the corners. “I’m not a monster, I won’t push you into the forest right before the night. Spend a night here, we’ll talk tomorrow. Try to cool off.”
                        \n\nThe guards spread. Some sit at the tables and make plans for their next hunting trip, others walk outside, and everyone ignores you. You prepare yourself for sleep and walk outside to see how {color=#f6d6bd}[horsename]{/color} is doing, but quite soon the boredom makes you drowsy.
                        '
                        'I put my blanket on the wooden floor. At least it’s warmer here than it is outside. (disabled)':
                            pass
            'I walk away in silence.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away in silence.')
                show areapicture peltnorth01 at basicfade
                $ peltnorth_ban_temp = day
                $ iason_friendship -= 2
                $ dalit_friendship -= 2
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ quarters += 1
                menu:
                    'The guards observe you with caution, but don’t reach for their weapons. Before you walk outside, you hear {color=#f6d6bd}the innkeeper’s{/color} voice:
                    \n\n“Don’t come back before tomorrow, stranger. Cool your bloody head and learn how to behave.”
                    \n\nThe guards assist you on the way to {color=#f6d6bd}[horsename]{/color}, but they do so in silence. You pack your things - it looks like nothing is missing.
                    '
                    'I ride through the gate and leave the inn. (disabled)':
                        pass

    label peltnorthfirstvisit06ale:
        show areapicture peltnorth01inside at basicfade
        menu:
            'The dark room and wooden walls of the mug make the liquid look as brown as a chestnut. The lea in spring hits your nose, and the first sip is even too complex, too flowery. While the brewer has used fancy ingredients, the exotic liquorice ruins the aftertaste.
            \n\nNow you know why there’s so much left. Maybe it takes an acquired taste.
            \n\nThe innkeeper nods. “I was hoping to see someone willing to patrol the roads. Maybe you’ll help me with a worrying thought I have.”
            '
            '“Which is?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Which is?”')
                label peltnorth_tulia_meeting_firsttime04:
                    $ iason_about_quest_glaucia = 1
                    $ description_howlersdell01 = "A prosperous village of farmers and animal breeders set along the western road."
                    $ banditshideout_bandits_pchearedabout = 1
                    menu:
                        '“There are brigands in the woods. Our place is a stronghold, so I’m not afraid of an open strike, but they’ve gotten more active in the last two years. One day, they {i}may{/i} steal our furs, and I’ve no doubt they’re the reason why merchants come here only once. Having bandits around gets expensive.”
                        \n\nHe rubs his hands together, camouflaging his pause. “I want you to reach {color=#f6d6bd}Howler’s Dell{/color}, northwest from here. It’s the largest settlement around, I’m sure you’ll get there sooner or later. Ask {color=#f6d6bd}Thais{/color}, the mayor, about {color=#f6d6bd}Glaucia{/color}, that bloodthirsty wolf of a woman. I’ve heard rumors about a raid in the North. If {color=#f6d6bd}Glaucia’s{/color} ready to break the truce with the locals, I’m willing to join forces with them to get rid of her band.”
                        \n\nHe looks at a nearby dragon bone. “Not too difficult, right? Just do it when you have a chance, a couple of days won’t make much of a difference. I’ll pay you two coins when you get back with the news. Fine?”
                        '
                        'I nod.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                            $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me two dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
                            $ quest_intelforpeltnorth_rewardvalue = 2
                            $ quest_intelforpeltnorth = 1
                            $ renpy.notify("New entry: Glaucia’s Band")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
                            jump peltnorthregularquestionsv05
                        '“Three.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Three.”')
                            if iason_friendship > 0:
                                $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me three dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
                                $ quest_intelforpeltnorth_rewardvalue = 3
                                $ quest_intelforpeltnorth = 1
                                $ renpy.notify("New entry: Glaucia’s Band")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
                                $ can_rest = 1
                                $ can_items = 1
                                $ questionpreset = "iason1"
                                menu:
                                    'He nods with a smile. “What else do you need?”
                                    '
                                    '(iason1 set)':
                                        pass
                            else:
                                $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me two dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
                                $ quest_intelforpeltnorth_rewardvalue = 2
                                $ quest_intelforpeltnorth = 1
                                $ renpy.notify("New entry: Glaucia’s Band")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
                                $ can_rest = 1
                                $ can_items = 1
                                $ questionpreset = "iason1"
                                menu:
                                    'He observes you for a moment. “Two,” he growls.
                                    '
                                    '(iason1 set)':
                                        pass

###########################

label peltnorth01insidetalkingwithiason:
    $ shop = "peltnorth"
    $ questionpreset = "iason1"
    $ can_rest = 1
    if whitemarshes_attacked and whitemarshes_attack_companion_pelt and not iason_about_nomoreundead:
        $ iason_about_nomoreundead = 1
        if whitemarshes_nomoreundead:
            if orentius_convinced:
                $ iason_friendship += 1
                menu:
                    '[peltnorthroomdescription] [peltnorth_iason_fluff]
                    \n\n“Nice job at {color=#f6d6bd}White Marshes{/color},” he gives you an encouraging nod. “Though I doubt {color=#f6d6bd}Orentius{/color} will keep his word. I hope I’m wrong.”
                    '
                    '(iason1 set)':
                        pass
            elif orentius_banished:
                $ iason_friendship += 2
                menu:
                    '[peltnorthroomdescription] [peltnorth_iason_fluff]
                    \n\n“Great job at {color=#f6d6bd}White Marshes{/color},” his smile disappears as quickly as it showed up. “Having {color=#f6d6bd}Orentius{/color} away from the village means we don’t have to worry about him.”
                    '
                    '(iason1 set)':
                        pass
            elif whitemarshes_destroyed:
                $ iason_friendship += 1
                menu:
                    '[peltnorthroomdescription] [peltnorth_iason_fluff]
                    \n\n“Nice job at {color=#f6d6bd}White Marshes{/color},” he gives you an encouraging nod. “Having fewer people to trade with and more monsters against us will give us a rough couple of years, but it’s better than fighting off a power-hungry necromancer.”
                    '
                    '(iason1 set)':
                        pass
        else:
            $ iason_friendship -= 1
            menu:
                '[peltnorthroomdescription] [peltnorth_iason_fluff]
                \n\n“You didn’t do all that well in {color=#f6d6bd}White Marshes{/color},” he gives you an annoyed scowl. “I guess we now need to prepare ourselves against the counter attack led by necromancers. Yet another war, even if a small one,” he sighs.
                '
                '(iason1 set)':
                    pass
    if peltnorth_ban_temp < day and peltnorth_ban_temp and not iason_about_ban:
        $ iason_about_ban = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“So, you again. Let’s forget the past and act like soul carriers, fine?”
            '
            '(iason1 set)':
                pass
    elif dalit_pc_tools == 1:
        $ dalit_pc_tools = 2
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“So, you again. Let’s forget the past and act like soul carriers, fine?”
            '
            '(iason1 set)':
                pass
    elif shortcut_darkforest_bandit_inpeltnorth and not iason_about_shortcut_bandit and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ iason_about_shortcut_bandit = 1
        $ shortcut_bandit_identity = 1
        $ iason_friendship += 1
        $ iason_friendship_moneybonus_points += 3
        $ banditshideout_bandits_pchearedabout = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\nHe’s looking toward {color=#f6d6bd}the man you found at the shortcut{/color}. His voice is thoughtful. “Weird times, hm? I was hoping to learn more about the bandits, and now one of them is right here, drinking my ale. Too bad he doesn’t talk,” he glances toward you. “He said he knows you, that you faced some beasts... I mean, coin is coin, but couldn’t you bring me some merchants instead?”
            '
            '(iason1 set)':
                pass
    elif iason_shop_shield_announced and not iason_shop_shield:
        $ iason_shop_shield = 1
        $ renpy.notify("You can now trade for a new item.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“I have something new to sell you,” he says without a proper greeting. “A shield. It’s large, a bit heavy, but firm. One of my huntresses tried to put it to use, but prefers a long spear. Let me know if you want it.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level1_given and not iason_friendship_moneybonus_level1_reaction:
        $ iason_friendship_moneybonus_level1_reaction = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“Finally,” he nods to you. “Someone with coins shows up.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level2_given and not iason_friendship_moneybonus_level2_reaction:
        $ iason_friendship_moneybonus_level2_reaction = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“Well,” he nods to you. “There ain’t been a lot of trade going on here, but things are starting to change since your arrival. Are you looking for something to buy?”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level3_given and not iason_friendship_moneybonus_level3_reaction:
        if iason_food_berries == 3 and iason_food_berries_refused:
            $ iason_food_berries = 2
            $ iason_friendship += 2
            $ iason_friendship_moneybonus_level3_reaction = 1
            menu:
                '[peltnorthroomdescription] [peltnorth_iason_fluff]
                \n\n“Hello, warden,” he nods to you. “I must say, after you refused to help me with those berries I saw you as too proud to be of use, but the longer you’re around, the more coins land in my pouch. You really are a busy soul. Just tell me if you need anything, food included. I may have some leftovers.”
                '
                '(iason1 set)':
                    pass
        else:
            menu:
                '[peltnorthroomdescription] [peltnorth_iason_fluff]
                \n\n“Hello, warden,” he nods to you. “The longer you’re around, the more coins land in my pouch. Just tell me if you need anything.”
                '
                '(iason1 set)':
                    pass
    elif iason_friendship_moneybonus_level4_given and not iason_friendship_moneybonus_level4_reaction:
        $ iason_friendship_moneybonus_level4_reaction = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“You truly are a regular, huh?” he welcomes you with a gentle smile. “Good to see you again.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level5_given and not iason_friendship_moneybonus_level5_reaction:
        $ iason_friendship_moneybonus_level5_reaction = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\nA wide grin shows up on the keeper’s face as he serves you a fresh mug of ale.
            '
            '(iason1 set)':
                pass
    elif iason_dayofvisit != day:
        $ iason_dayofvisit = day
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“So, you again. Need anything?”
            '
            '(iason1 set)':
                pass
    else:
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“Something bothering you?”
            '
            '(iason1 set)':
                pass

label peltnorth01insidetalkingwithiasonalt:
    $ shop = "peltnorth"
    $ questionpreset = "iason1"
    $ can_rest = 1
    if whitemarshes_attacked and whitemarshes_attack_companion_pelt and not iason_about_nomoreundead:
        $ iason_about_nomoreundead = 1
        if whitemarshes_nomoreundead:
            if orentius_convinced:
                $ iason_friendship += 1
                menu:
                    '“Nice job at {color=#f6d6bd}White Marshes{/color},” he gives you an encouraging nod. “Though I doubt {color=#f6d6bd}Orentius{/color} will keep his word. I hope I’m wrong.”
                    '
                    '(iason1 set)':
                        pass
            elif orentius_banished:
                $ iason_friendship += 2
                menu:
                    '“Great job at {color=#f6d6bd}White Marshes{/color},” his smile disappears as quickly as it showed up. “Having {color=#f6d6bd}Orentius{/color} away from the village means we don’t have to worry about him.”
                    '
                    '(iason1 set)':
                        pass
            elif whitemarshes_destroyed:
                $ iason_friendship += 1
                menu:
                    '“Nice job at {color=#f6d6bd}White Marshes{/color},” he gives you an encouraging nod. “Having fewer people to trade with and more monsters against us will give us a rough couple of years, but it’s better than fighting off a power-hungry necromancer.”
                    '
                    '(iason1 set)':
                        pass
        else:
            $ iason_friendship -= 1
            menu:
                '“You didn’t do all that well in {color=#f6d6bd}White Marshes{/color},” he gives you an annoyed scowl. “I guess we now need to prepare ourselves against the counter attack led by necromancers. Yet another war, even if a small one,” he sighs.
                '
                '(iason1 set)':
                    pass
    if peltnorth_ban_temp < day and peltnorth_ban_temp and not iason_about_ban:
        $ iason_about_ban = 1
        menu:
            '[peltnorthroomdescription] [peltnorth_iason_fluff]
            \n\n“So, you again. Let’s forget the past and act like soul carriers, fine?”
            '
            '(iason1 set)':
                pass

    if peltnorth_ban_temp < day and peltnorth_ban_temp and not iason_about_ban:
        $ iason_about_ban = 1
        menu:
            '“So, you again. Let’s forget the past and act like soul carriers, fine?”
            '
            '(iason1 set)':
                pass
    elif dalit_pc_tools == 1:
        $ dalit_pc_tools = 2
        menu:
            '“So, you again. Let’s forget the past and act like soul carriers, fine?”
            '
            '(iason1 set)':
                pass
    elif shortcut_darkforest_bandit_inpeltnorth and not iason_about_shortcut_bandit and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ iason_about_shortcut_bandit = 1
        $ shortcut_bandit_identity = 1
        $ iason_friendship += 1
        $ iason_friendship_moneybonus_points += 3
        menu:
            'He’s looking toward {color=#f6d6bd}the man you found at the shortcut{/color}. His voice is thoughtful. “Weird times, hm? I was hoping to learn more about the bandits, and now one of them is right here, drinking my ale. Too bad he doesn’t talk,” he glances toward you. “He said he knows you, that you faced some beasts... I mean, coin is coin, but couldn’t you bring me some merchants instead?”
            '
            '(iason1 set)':
                pass
    elif iason_shop_shield_announced and not iason_shop_shield:
        $ iason_shop_shield = 1
        $ renpy.notify("You can now trade for a new item.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
        menu:
            '“So, you again. I have something new to sell you. A shield. It’s large, a bit heavy, but firm. One of my huntresses tried to put it to use, but prefers a long spear. Let me know if you want it.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level1_given and not iason_friendship_moneybonus_level1_reaction:
        $ iason_friendship_moneybonus_level1_reaction = 1
        menu:
            '“Finally,” he nods to you. “Someone with coins shows up.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level2_given and not iason_friendship_moneybonus_level2_reaction:
        $ iason_friendship_moneybonus_level2_reaction = 1
        menu:
            '“Well,” he nods to you. “There ain’t been a lot of trade going on here, but things are starting to change since your arrival. Are you looking for something to buy?”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level3_given and not iason_friendship_moneybonus_level3_reaction:
        $ iason_friendship_moneybonus_level3_reaction = 1
        menu:
            '“Hello, warden,” he nods to you. “The longer you’re around, the more coins land in my pouch. Just tell me if you need anything.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level4_given and not iason_friendship_moneybonus_level4_reaction:
        $ iason_friendship_moneybonus_level4_reaction = 1
        menu:
            '“You truly are a regular, huh?” he welcomes you with a gentle smile. “Good to see you again.”
            '
            '(iason1 set)':
                pass
    elif iason_friendship_moneybonus_level5_given and not iason_friendship_moneybonus_level5_reaction:
        $ iason_friendship_moneybonus_level5_reaction = 1
        menu:
            'A wide grin shows up on the keeper’s face as he serves you a fresh mug of ale.
            '
            '(iason1 set)':
                pass
    elif iason_dayofvisit != day:
        $ iason_dayofvisit = day
        menu:
            '“So, you again. Need anything?”
            '
            '(iason1 set)':
                pass
    else:
        menu:
            '“Something bothers you?”
            '
            '(iason1 set)':
                pass

label peltnorthregularquestionsv01:
    $ shop = "peltnorth"
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "iason1"
    menu:
        '“Sure. Go ahead.”
        '
        '(iason1 set)':
            pass

    label peltnorthleftoversyesorno:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any leftovers?”')
        if (iason_food_roll-iason_friendship-dalit_friendship+appearance_charisma) <= 25:
            $ pc_food = limit_pc_food(pc_food+2)
            show plus2food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
            $ can_rest = 1
            $ can_items = 1
            $ quarters += 1
            $ questionpreset = "iason1"
            menu:
                '“Yep, you’re lucky. I was planning to give it to the boar.” He goes to the stove and in a couple of minutes prepares you a meal. “Here.” You see [randommeal]. While you’re eating, he asks if you need anything else.
                '
                '(iason1 set)':
                    pass
        else:
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                '“Not today, no. Maybe tomorrow.”
                '
                '(iason1 set)':
                    pass

    label peltnorthregularquestionsv02:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            '“What do you need?”
            '
            '(iason1 set)':
                pass

    label peltnorthregularquestionsv03:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            '“Need anything?”
            '
            '(iason1 set)':
                pass

    label peltnorthregularquestionsv04:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        if tutorial_selling == 1:
            $ tutorial_selling = 2
        if tutorial_selling2 == 1:
            $ tutorial_selling2 = 2
        menu:
            'He nods. “What else do you need?”
            '
            '(iason1 set)':
                pass

    label peltnorthregularquestionsv05:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            '“Great. What else do you need?”
            '
            '(iason1 set)':
                pass

###########################

label peltnorthleftoversquestforberries01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could eat something. “Do you have any leftovers?”')
    $ minutes += 5
    $ iason_stance = "behindcounter"
    menu:
        '“Yes, I feed them to our boar. I won’t give them away for nothing.”
        \n\nHe tells you to wait, then leaves the building for a few minutes and returns with a wooden bucket and a long stick ending with a hook.
        \n\n“Go through the gate and turn left, you’ll see a bunch of bushes. We need some berries. Bring me a bucketful, you’ll be done in half an hour or so. Your horse could use a nap anyway. And I’ll prepare something to fill you.”
        \n\nThe hook is not made of metal or wood. It’s a long, curved claw, almost black.
        '
        'I reach for the tools. “Half an hour? That’s quite a lot for berry picking.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the tools. “Half an hour? That’s quite a lot for berry picking.”')
            $ iason_food_berries_day = day
            $ iason_food_berries = 1
            $ item_peltnorthberrytools = 1
            $ renpy.notify("You received a set of tools.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a set of tools.{/i}')
            menu:
                'The tools are cold, not too heavy. You notice a pair of thick gloves at the bottom of the bucket.
                \n\n“Ah, the berries are not a problem,” {color=#f6d6bd}the innkeeper{/color} smirks. “Unlike the snakes. Better scare them away with a stick, or move them with a hook. And protect your hands. The little ones won’t eat you, but don’t get bitten. I’m sure you know how to be patient.”
                '
                '“Fine. I’ll go right away.”' ( condition="quarters <= (world_daylength-4)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll go right away.”')
                    jump leavingthepeltnorth
                '“I have other questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have other questions.”')
                    jump peltnorthregularquestionsv02
        'I won’t do that. “Do I look like someone who forages for berries?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do I look like someone who forages for berries?”')
            $ iason_friendship -= 1
            $ iason_food_berries_refused = 1
            $ iason_food_berries = 3
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                '“And do I look like someone who cares? I didn’t expect a traveler to be afraid of splinters.” He shrugs and puts the tools away. “Fine, but I won’t cook just for you. I can sell you some food rations, that’s it.”
                '
                '(iason1 set)':
                    pass

    label peltnorthleftoversquestforberries04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put his fruits on the counter.')
        $ item_peltnorthberries = 0
        $ renpy.notify("You lost the berries.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the berries.{/i}')
        $ iason_food_berries = 2
        $ pc_food = limit_pc_food(pc_food+2)
        show plus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        $ can_items = 0
        $ iason_stance = "behindcounter"
        menu:
            '“Great,” he peeks inside the bucket. “I’ve got cabbage stew with a few goose chunks for you. I’d serve it even to merchants, if there were any around.”
            \n\nThe meal is warm and filling. It’s well-seasoned and not overcooked.
            \n\n“And like I’ve said, I rarely have food to spare, but feel free to ask if you ever stop by. You may be lucky, and I’ve been cooking my whole life.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthleftoversquestforberries05
            'I keep chewing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep chewing.')
                jump peltnorthleftoversquestforberries05

    label peltnorthleftoversquestforberries05:
        menu:
            '“And how did that ol’ hook of mine work out for you? I see you still have your hands.”
            '
            'I give him the hook. “I’m fine.”' ( condition="item_peltnorthberrytools" ):
                $ renpy.notify("You lost the hook.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook.{/i}')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give him the hook. “I’m fine.”')
                $ item_peltnorthberrytools = 0
                $ can_items = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He takes the tools from you and nods. “Need anything else?”
                    '
                    '(iason1 set)':
                        pass
            'I don’t have the hook anymore. (disabled)' ( condition="not item_peltnorthberrytools" ):
                pass
            '“I’d like to buy it from you.”' ( condition="item_peltnorthberrytools" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to buy it from you.”')
                jump peltnorthleftoversquestforberries05b
            '(lie) “I’ve lost it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’ve lost it.”')
                $ pc_lies += 1
                jump peltnorthleftoversquestforberries05c

    label peltnorthleftoversquestforberries05b:
        menu:
            'He narrows his eyes. “Can’t you make one for yourself?”
            '
            '“Just name your price.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just name your price.”')
                jump peltnorthleftoversquestforberries05ba
            '“I won’t have time for it. And I hate snakes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t have time for it. And I hate snakes.”')
                jump peltnorthleftoversquestforberries05ba
            '“It’s the claw that grabs my interest, honestly.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s the claw that grabs my interest, honestly.”')
                jump peltnorthleftoversquestforberries05bb

    label peltnorthleftoversquestforberries05ba:
        menu:
            '“If you say so,” he shrugs. “I want two coins for it, though. It’s a damn fine tool.”
            '
            'I pay him.' if coins >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pay him.')
                show screen notifyimage( "-2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 {image=cointest}{/i}')
                $ coins -= 2
                $ iason_friendship_moneybonus_points += 1
                jump peltnorthleftoversquestforberries05baa
            'I don’t have enough coins. (disabled)' if coins < 2:
                pass
            '“That’s too much.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s too much.”')
                jump peltnorthleftoversquestforberries05bab
            '“Forget it.” I give him the hook.' if item_peltnorthberrytools:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the hook.')
                $ renpy.notify("You lost the hook.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook.{/i}')
                $ can_items = 1
                $ item_peltnorthberrytools = 0
                jump peltnorthleftoversquestforberries05bac
            '“Forget it.” I give him the claw and the handle.' if item_peltnorthberryclaw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the claw and the handle.')
                $ renpy.notify("You lost the claw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the claw.{/i}')
                $ can_items = 1
                $ item_peltnorthberryclaw = 0
                jump peltnorthleftoversquestforberries05bad

    label peltnorthleftoversquestforberries05bab:
        menu:
            '“I guess so. I don’t ask for what it’s worth, but what it’s worth for me.”
            '
            'I pay him.' if coins >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pay him.')
                show screen notifyimage( "-2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 {image=cointest}{/i}')
                $ coins -= 2
                $ iason_friendship_moneybonus_points += 1
                jump peltnorthleftoversquestforberries05baa
            'I don’t have enough coins. (disabled)' if coins < 2:
                pass
            '“Forget it.” I give him the hook.' if item_peltnorthberrytools:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the hook.')
                $ renpy.notify("You lost the hook.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook.{/i}')
                $ can_items = 1
                $ item_peltnorthberrytools = 0
                jump peltnorthleftoversquestforberries05bac
            '“Forget it.” I give him the claw and the handle.' if item_peltnorthberryclaw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the claw and the handle.')
                $ renpy.notify("You lost the claw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the claw.{/i}')
                $ can_items = 1
                $ item_peltnorthberryclaw = 0
                jump peltnorthleftoversquestforberries05bad

    label peltnorthleftoversquestforberries05bb:
        menu:
            '“Ah, I see. It’s a nice one, ain’t it? My guards once had to get rid of a pebbler. You can’t really eat them, but their claws and bones are durable enough, so we put them to good use.” For a moment, he observes your face. “A single coin will be fair.”
            '
            'I pay him.' if coins >= 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pay him.')
                show screen notifyimage( "-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                $ coins -= 1
                $ iason_friendship_moneybonus_points += 1
                jump peltnorthleftoversquestforberries05baaa
            'My pouch is empty. (disabled)' if coins < 1:
                pass
            '“Forget it.” I give him the hook.' if item_peltnorthberrytools:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the hook.')
                $ renpy.notify("You lost the hook.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook.{/i}')
                $ can_items = 1
                $ item_peltnorthberrytools = 0
                jump peltnorthleftoversquestforberries05bac
            '“Forget it.” I give him the claw and the handle.' if item_peltnorthberryclaw:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.” I give him the claw and the handle.')
                $ renpy.notify("You lost the claw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the claw.{/i}')
                $ can_items = 1
                $ item_peltnorthberryclaw = 0
                jump peltnorthleftoversquestforberries05bad

    label peltnorthleftoversquestforberries05baa:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He takes them with a nod. “Need anything else?”
            '
            '(iason1 set)':
                pass

    label peltnorthleftoversquestforberries05baaa:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He takes it with a nod. “Need anything else?”
            '
            '(iason1 set)':
                pass

    label peltnorthleftoversquestforberries05bac:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He takes the hook, barely paying any attention to it. “Need anything else?”
            '
            '(iason1 set)':
                pass

    label peltnorthleftoversquestforberries05bad:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'Seeing the pieces of the hook, he frowns. “Oh, so the cord got cut? Should be easy to fix it.” He grabs a cord from one of the shelves and starts banding the parts together. “Need anything else?”
            '
            '(iason1 set)':
                pass

    label peltnorthleftoversquestforberries05c:
        $ can_rest = 1
        $ can_items = 1
        $ iason_friendship -= 1
        $ questionpreset = "iason1"
        menu:
            '“You’ve lost the claw? How did that even happen?” He scoffs. “A snake ate it?”
            \n\nYou {i}explain{/i} that you tried to move a large pile of snakes at once and they started to wrap around the handle with their shells. Last you saw it was pulled down among them. That’s when you knew you should walk away.
            \n\nYou’re not sure if {color=#f6d6bd}the innkeeper{/color} believes you. You hear his “mhm,” and after a moment he asks you if there’s anything else you wanted to talk about. His deep voice sounds cold.
            '
            '(iason1 set)':
                pass

################################

label peltnorthtrade01:
    $ shop = "peltnorth"
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What do you have for sale?”')
    $ renpy.notify("New trader unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
    menu:
        '“I can go and pick up a few things for you. Some food for your travels, to start with. Apples, nuts, sausage. Not too many at once, we need to maintain our supplies. I’ve got an elk fur I don’t need, its buyer was caught by a pack of red wolves. Nice for a sleeping spot, just as nice for a wall. An almost untouched bowl of soap, {i}priceless{/i} for a traveler.” You can’t tell if he’s being sarcastic. “Made of fine oak ash. Strong, though you should have some better supplies before you start your own bathhouse.”
        \n\nAfter you mention you’d like something more useful on these roads, he looks down. “I don’t have any blades or armor to spare, but if you pay well, you can take one of our crossbows and a bunch of quarrels. A yew bow, wool cords, and the trigger needs just a little bit of oil. It’s as good as you can get without soaking it in magic. Takes a bit of muscle to draw, but even a sixteen-year-old could handle it. I won’t sell it cheap, but I’m ready to give a discount to a helpful ally.”
        '
        '“Let me take a look at what you have first.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me take a look at what you have first.”')
            $ quarters += 1
            $ iason_shop = 1
            show screen shopscreen with dissolve
            jump peltnorthtrade02

    label peltnorthtrade02:
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He leaves you for a few minutes and gathers his wares. “Come back in the future, I may have something new that I’ll be willing to part with.”
            '
            '(preset iason1)':
                pass

    label peltnorthtrade03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Show me your wares.”')
        $ shop = "peltnorth"
        show screen shopscreen with dissolve
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He places them on the counter.
            '
            '(preset iason1)':
                pass

##############################################

label peltnorth_selling01:
    $ shop = "peltnorth"
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do I have anything you’d like to buy?”')
    $ peltnorth_selling = 1
    $ thingstosell = 0
    if item_axe02alt or item_axehead or item_axeset:
        $ thingstosell += 1
    if item_furlesswolftrophy:
        $ thingstosell += 1
    if item_stoat:
        $ thingstosell += 1
    if item_antlers:
        $ thingstosell += 1
    if item_boartusks:
        $ thingstosell += 1
    if item_cidercask:
        $ thingstosell += 1
    if item_brokenknife:
        $ thingstosell += 1
    if item_ironscraps:
        $ thingstosell += 1
    if item_ironingot:
        $ thingstosell += 1
    if item_bonebuckle:
        $ thingstosell += 1
    if item_linen:
        $ thingstosell += 1
    if item_rawfishtotalnumber and not iason_about_fish:
        $ thingstosell += 1
    if item_asterionbow:
        $ thingstosell += 1
    if item_wingedhourglass and item_wingedhourglass_worn and not iason_shop_wingedhourglass_sold:
        $ thingstosell += 1
    if item_asterionwine and not item_asterionwine_pcknows_2:
        $ thingstosell += 1
    if item_asterionwine and item_asterionwine_pcknows_2 and not iason_shop_wine:
        $ thingstosell += 1
    if item_potiondolmen and item_potiondolmen_known and not iason_shop_potions_block:
        $ thingstosell += 1
    if item_generichealingpotion and not iason_shop_potions_block:
        $ thingstosell += 1
    if item_griffonegg:
        $ thingstosell += 1
    if not tutorial_selling:
        $ tutorial_selling = 1
    if thingstosell:
        if not tutorial_selling2:
            $ tutorial_selling2 = 1
    if thingstosell:
        show screen selling()
        if iason_stance != "behindcounter":
            $ iason_stance = "behindcounter"
            $ custom1 = "He moves behind the counter. "
        else:
            $ custom1 = ""
        menu:
            '[custom1]“Let’s see what you’ve got.”
            '
            '“Forget it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                hide screen selling
                jump peltnorthregularquestionsv04
    else:
        menu:
            'You pull out some items, but {color=#f6d6bd}the innkeeper{/color} shakes his head. “I don’t need those, nor could I sell them to anyone. I’d rather make coins than waste them, so bring me something of value.”
            '
            'I pack my things.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                hide screen selling
                jump peltnorthregularquestionsv04

    label peltnorth_sellingaxe02alt:
        menu:
            '“It’s a pretty axe, but we don’t really need more of them,” he gives you back your bronze weapon. “Too bad it’s not engraved. It’s worth more than {color=#f6d6bd}five coins{/color}, but I don’t know what to do with it other than sell it.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the bronze axe.\n+5", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bronze axe. +5 {image=cointest}{/i}')
                $ item_axe02alt = 0
                $ coins += 5
                $ iason_friendship_moneybonus_points += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingaxehead:
        menu:
            '“It’s a pretty head, but we don’t really need more axes,” he gives it back. “Too bad it’s not engraved. I’ll pay you {color=#f6d6bd}four coins{/color} for it. It’s worth more, but I don’t know what to do with it other than sell it.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the axe head.\n+4", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bronze axe. +4 {image=cointest}{/i}')
                $ item_axehead = 0
                $ item_axeset = 0
                $ coins += 4
                $ iason_friendship_moneybonus_points += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingfurlesswolftrophy:
        menu:
            'You take the innkeep outside to show him the head of a beast. “Ah, a furless wolf. Such an ugly creature.” He examines its condition and gestures for you to follow him back to the building. “It’s not easy to say how much work it will take to make it look fine, and, let’s be honest, it’s never going to look {i}that{/i} good. Monster trophies are worth more when they don’t make you lose your appetite.” He returns behind the counter. “So, what do you say? {color=#f6d6bd}Four coins{/color}?”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the head of a beast.\n+4", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the head of a beast. +4 {image=cointest}{/i}')
                $ item_furlesswolftrophy = 0
                $ coins += 4
                $ iason_friendship_moneybonus_points += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingstoat:
        if item_stoat == 1:
            menu:
                '“I could use this dead stoat, even though it’s not the cleanest fur.” He points at the damaged part of the critter’s shell. “I bet you don’t have a place to dress it, so I’m doing you a favor. Is {color=#f6d6bd}three coins{/color} fine with you?”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the dead stout.\n+3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the dead stout. +3 {image=cointest}{/i}')
                    $ item_stoat = 0
                    $ coins += 3
                    $ iason_friendship_moneybonus_points += 1
                    jump peltnorth_selling02
                '“That’s all.”':
                    hide screen selling
                    jump peltnorthregularquestionsv04
        elif item_stoat == 2:
            menu:
                '“I could use this dead stoat.” He examines the carcass carefully. “You’ve done a nice job keeping the fur clean. We’ll need to put some effort to dress it, but I think {color=#f6d6bd}five coins{/color} are more than fine.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the dead stout.\n+5", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the dead stout. +5 {image=cointest}{/i}')
                    $ item_stoat = 0
                    $ coins += 5
                    $ iason_friendship_moneybonus_points += 1
                    jump peltnorth_selling02
                '“That’s all.”':
                    hide screen selling
                    jump peltnorthregularquestionsv04
    label peltnorth_sellingboartusks:
        menu:
            '“These are a bit rough around the edges, I’d say. And we kill boars often. I won’t give you more than {color=#f6d6bd}two decent meals{/color} for it.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                $ renpy.notify("You exchanged the boar tusks for two meals.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You exchanged the boar tusks for two meals.{/i}')
                $ item_boartusks -= 1
                $ item_rations += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingantlers:
        menu:
            '“I’m not too crazy about antlers, we’ve enough of them already,” he rubs one of the tines with his thumb. “I don’t expect to see a trader chasing after such a cheap trophy for their wall. I’ll give you {color=#f6d6bd}a single meal{/color} for it.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                $ renpy.notify("You exchanged the antlers for a meal.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You exchanged the antlers for a meal.{/i}')
                $ item_antlers -= 1
                $ item_rations += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingbonebuckle:
        menu:
            '“I could wear this during meetings with more {i}lofty{/i} visitors,” he holds the buckle at his waist. The silver and yellowish bone go well with his purple skin, though they may be more distracting in the sunlight. “But I already have a different one, just not so pretty. {color=#f6d6bd}Two coins{/color} should be enough.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the decorative buckle.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the decorative buckle. +2 {image=cointest}{/i}')
                $ item_bonebuckle -= 1
                $ coins += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingcidercask:
        $ iason_shop_cidercask_price = (7-appearance_price)
        menu:
            '“I could use some cider, but I doubt it will last through the winter.” After a bit of haggling he offers you {color=#f6d6bd}[iason_shop_cidercask_price] coins{/color} for it.
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                $ item_cidercask -= 1
                $ coins += iason_shop_cidercask_price
                $ iason_friendship_moneybonus_points += 2
                if quest_foggy3whitemarshes == 1:
                    $ quest_foggy3whitemarshes_description07 = "I sold the cask outside of {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Foggy{/color} won’t learn about it."
                    show screen notifyimage( "Journal updated: Cask of Cider.\n+%s" %iason_shop_cidercask_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider. +%s {image=cointest}{/i}' %iason_shop_cidercask_price)
                else:
                    show screen notifyimage( "You sold the cask of cider.\n+%s" %iason_shop_cidercask_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the cask of cider. +%s {image=cointest}{/i}' %iason_shop_cidercask_price)
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingbrokenknife:
        menu:
            '“That’s pretty, but I don’t have any blades to make use of it. I would have to buy one from a trader. I can give you {color=#f6d6bd}two bones{/color} for it.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the broken knife.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the broken knife. +2 {image=cointest}{/i}')
                $ item_brokenknife = 0
                $ coins += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingironingot:
        $ iason_shop_ironingot_price = (18-appearance_price)
        menu:
            'His eyes widen as soon as they land on the ingot. “Isn’t this,” he stops suddenly and glances at your boots. Before he speaks again, he clears his throat. “Yeah, I can grab it, why not. For... {color=#f6d6bd}[iason_shop_ironingot_price] coins{/color}. Not more than that - I need to sell it myself, we don’t have a furnace.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the iron ingot.\n+%s" %iason_shop_ironingot_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the iron ingot. +%s {image=cointest}{/i}' %iason_shop_ironingot_price)
                $ item_ironingot -= 1
                $ item_ironingot_sold_pelt = 1
                $ coins += iason_shop_ironingot_price
                $ iason_friendship += 1
                $ iason_friendship_moneybonus_points += 4
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingironscraps:
        menu:
            '“I could free you from this iron and steel, but we don’t have a furnace to work with them. Let’s say, {color=#f6d6bd}six coins{/color}.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the iron scraps.\n+6", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the iron scraps. +6 {image=cointest}{/i}')
                $ item_ironscraps -= 1
                $ coins += 6
                $ iason_friendship_moneybonus_points += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellinglinen:
        menu:
            '“We stay in touch with {color=#f6d6bd}Howler’s{/color}, so we have all the clothes we need. I could sell it to some travelers, though, sometime.” You describe how much fabric is in your possession. “It should be worth ten coins, don’t you think? {color=#f6d6bd}I can pay you that and add one coin{/color} for the delivery.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the stack of linen.\n+11", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the stack of linen. +11 {image=cointest}{/i}')
                $ item_linen -= 1
                $ coins += 11
                $ iason_friendship_moneybonus_points += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingasterionbow:
        $ iason_shop_bow_price = (10-appearance_price)
        menu:
            '“Didn’t it belong to Asterion?” He takes it for a moment and makes sure there are no cuts or other defects. “We have some bowfighters on the wall. {color=#f6d6bd}[iason_shop_bow_price] coins{/color}?”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold Asterion’s bow.\n+%s" %iason_shop_bow_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold Asterion’s bow. +%s {image=cointest}{/i}' %iason_shop_bow_price)
                $ item_asterionbow = 0
                $ coins += 10
                $ iason_friendship_moneybonus_points += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingwingedhourglass:
        menu:
            'He looks at your chest. “One of my hunters would gladly take care of an hourglass pendant like this one. For... nostalgic purposes. How about {color=#f6d6bd}two coins{/color}?”
            '
            'I take it off. “Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take it off. “Deal.”')
                show screen notifyimage( "You sold the winged hourglass.\n+2", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the winged hourglass. +2 {image=cointest}{/i}')
                $ item_wingedhourglass_worn = 0
                $ item_wingedhourglass -= 1
                $ pc_faithpoints -= -2
                $ coins += 2
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingasterionwine01:
        $ item_asterionwine_pcknows_1 = 1
        menu:
            '“What’s in here?” Without asking for your permission, he opens Asterion’s bottle and sniffs it. Once, twice, three times. “Some cheap wine, but still wine. {color=#f6d6bd}Six coins{/color} should be enough.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the bottle of wine.\n+6", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bottle of wine. +6 {image=cointest}{/i}')
                $ item_asterionwine = 0
                $ coins += 6
                $ iason_friendship_moneybonus_points += 1
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingasterionwine02:
        $ iason_shop_wine = 1
        menu:
            '“Night’s Bane? Never heard of it.” He puts the bottle away, but his gestures get gentler. “I guess you plan to sell it for some big coin. I ain’t going to hoard it.”
            '
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04
    label peltnorth_sellingpotiondolmen:
        if iason_shop_potions_sold < 3:
            $ iason_shop_potion_10coins = 1
            $ iason_shop_potion_price = (8-appearance_price)
            menu:
                '“My hunters always need more healing potions, but the monks are hesitant to sell them. {color=#f6d6bd}[iason_shop_potion_price] coins{/color}, I know how valuable such magic gets.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    $ item_potiondolmen = 0
                    $ quest_healingpotion_description04 = "I have lost the potion. I should speak with the merchant."
                    if quest_healingpotion == 1:
                        show screen notifyimage( "Journal updated: Merchant’s Medicament.\n+%s" %iason_shop_potion_price, "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament. +%s {image=cointest}{/i}' %iason_shop_potion_price)
                    else:
                        show screen notifyimage( "You sold the healing potion.\n+%s" %iason_shop_potion_price, "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the healing potion. +%s {image=cointest}{/i}' %iason_shop_potion_price)
                    $ coins += iason_shop_potion_price
                    $ iason_friendship_moneybonus_points += 2
                    $ iason_shop_potions_sold += 1
                    jump peltnorth_selling02
                '“That’s all.”':
                    hide screen selling
                    jump peltnorthregularquestionsv04
        else:
            $ iason_shop_potions_block = 1
            menu:
                '“I know I said my hunters {i}always{/i} need more potions, but I didn’t {i}actually{/i} mean it,” he smiles gently. “Three are already plenty, but thanks.”
                '
                '“That’s all.”':
                    hide screen selling
                    jump peltnorthregularquestionsv04
    label peltnorth_sellinggenerichealingpotion:
        if iason_shop_potions_sold < 3:
            if item_generichealingpotion:
                $ iason_shop_potion_10coins = 1
                $ iason_shop_potion_price = (8-appearance_price)
                menu:
                    '“My hunters always need more healing potions, but the monks are hesitant to sell them. {color=#f6d6bd}[iason_shop_potion_price] coins{/color}, I know how valuable such magic gets.”
                    '
                    '“Deal.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        show screen notifyimage( "You sold a healing potion.\n+%s" %iason_shop_potion_price, "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a healing potion. +%s {image=cointest}{/i}' %iason_shop_potion_price)
                        $ item_generichealingpotion -= 1
                        $ coins += iason_shop_potion_price
                        $ iason_friendship_moneybonus_points += 2
                        $ iason_shop_potions_sold += 1
                        jump peltnorth_selling02
                    '“That’s all.”':
                        hide screen selling
                        jump peltnorthregularquestionsv04
        else:
            $ iason_shop_potions_block = 1
            menu:
                '“I know I said my hunters {i}always{/i} need more potions, but I didn’t {i}actually{/i} mean it,” he smiles gently. “Three are already plenty, but thanks.”
                '
                '“That’s all.”':
                    hide screen selling
                    jump peltnorthregularquestionsv04
    label peltnorth_sellinggriffonegg:
        menu:
            'He raises his dark eyebrows, but then mumbles something with disapproval. “Dead? This ain’t an impressive trophy, what do you want me to do with it? Maybe {i}someone{/i} will buy it, but I’ll only give you {color=#f6d6bd}three coins{/color}, no more.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the griffon egg.\n+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the griffon egg. +3 {image=cointest}{/i}')
                $ item_griffonegg -= 1
                $ coins += 3
                jump peltnorth_selling02
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04

    label peltnorth_selling02:
        $ thingstosell = 0
        if item_axe02alt or item_axehead or item_axeset:
            $ thingstosell += 1
        if item_furlesswolftrophy:
            $ thingstosell += 1
        if item_stoat:
            $ thingstosell += 1
        if item_antlers:
            $ thingstosell += 1
        if item_boartusks:
            $ thingstosell += 1
        if item_cidercask:
            $ thingstosell += 1
        if item_brokenknife:
            $ thingstosell += 1
        if item_ironscraps:
            $ thingstosell += 1
        if item_ironingot:
            $ thingstosell += 1
        if item_bonebuckle:
            $ thingstosell += 1
        if item_linen:
            $ thingstosell += 1
        if item_rawfishtotalnumber and not iason_about_fish:
            $ thingstosell += 1
        if item_asterionbow:
            $ thingstosell += 1
        if item_wingedhourglass and item_wingedhourglass_worn and not iason_shop_wingedhourglass_sold:
            $ thingstosell += 1
        if item_asterionwine and not item_asterionwine_pcknows_2:
            $ thingstosell += 1
        if item_asterionwine and item_asterionwine_pcknows_2 and not iason_shop_wine:
            $ thingstosell += 1
        if item_potiondolmen and item_potiondolmen_known and not iason_shop_potions_block:
            $ thingstosell += 1
        if item_generichealingpotion and not iason_shop_potions_block:
            $ thingstosell += 1
        if item_griffonegg:
            $ thingstosell += 1
        if thingstosell:
            menu:
                '“What else did you bring?”
                '
                '“Forget it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                    hide screen selling
                    jump peltnorthregularquestionsv04
        else:
            hide screen selling
            menu:
                'You pull out some items, but {color=#f6d6bd}the innkeeper{/color} shakes his head. “I don’t need those, nor could I sell them to anyone. I’d rather make coins than waste them, so bring me something of value.”
                '
                'I pack my things.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                    jump peltnorthregularquestionsv04

##############################################

label peltnorthasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
    if iason_stance == "sittingatstove":
        $ custom1 = "He stands up, goes to the table, and invites you to sit down with him."
    elif iason_stance == "behindcounter":
        $ custom1 = "He goes to the table and invites you to sit down with him."
    elif iason_stance == "sweeping":
        $ custom1 = "He puts away the broom, goes to the table, and invites you to sit down with him."
    elif iason_stance == "sittingattable":
        $ custom1 = "He leans against the wall. "
    $ iason_stance = "sittingattable"
    menu:
        '“Are you, now?” [custom1] “I don’t think I’m going to be of much help,” he rests his elbow on the table top and grunts quietly to clear his throat. “But I do want you to find him, so.”
        \n\nWhen asked about his intentions, he measures his words.
        \n\n“{color=#f6d6bd}Asterion{/color} and I made a {i}risky{/i} deal. Well, a very promising one. Last time he was here, he took fifty coins. My half of the investment.” He knocks on the table with a fist, anxiously. “If you get my coin, or at least find out what happened to the guy, I’ll make sure you won’t be disappointed after bringing me the news.”
        '
        '“Could it be that {color=#f6d6bd}Asterion{/color} stole the coins and ran away?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could it be that {color=#f6d6bd}Asterion{/color} stole the coins and ran away?”')
            $ description_asterion02 = "According to "
            $ description_asterion02b =", {color=#f6d6bd}Asterion{/color} was meant to do something for the people of {color=#f6d6bd}White Marshes{/color} and disappeared soon after that. He and the innkeep have made some sort of deal, in which the latter invested - and lost - fifty dragons. He doesn’t think {color=#f6d6bd}Asterion{/color} has stolen them."
            menu:
                'He looks at a window and starts to play with a shutter. “I just think {color=#f6d6bd}Asterion{/color} ain’t the kind of soul that would do such a thing. For him it wasn’t much of a fortune and I’d risk saying he had earned my trust. Not only mine, you know. It’s easy for a roadwarden to make connections. He always had places to go, things to take care of.”
                \n\nHe rubs the table with his thumb, as if trying to clean an invisible stain. “I’ve asked travelers, I’ve sent a couple of my pals to find him. No real news. I know he stayed in {color=#f6d6bd}White Marshes{/color} for a day and was meant to do something for the people there. It’s a village in the northwest - just stay on the main road until you reach the bogs, then enter them. You may get there before dusk.”
                \n\n“So... Let me know once you find anything, and we may yet return to this whole {i}investment{/i} thing.”
                '
                '“I’ll think about it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                    $ renpy.notify("Journal updated: Find the Roadwarden")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                    $ quest_asterion_description02 = "I’ve heard in {color=#f6d6bd}Pelt{/color} that right before Asterion’s disappearance, the innkeeper gave him 50 dragons for some sort of investment. Asterion was last seen in {color=#f6d6bd}White Marshes{/color}, a village in the northwest."
                    jump peltnorthregularquestionsv04

#########################################

label iason_about_asterion_found01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
    $ minutes += 5
    $ can_rest = 0
    $ can_items = 0
    menu:
        'You tell an abridged version of your story, during which you struggle to read anything from the innkeep’s eyes. Once you’re done, he tensely moves his shoulders, waiting for something.
        '
        '“And here are the dragon bones he had with him in the cave. I’m afraid it’s not even close to fifty.”' if asterion_found_searched and coins >= 20:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And here are the dragon bones he had with him in the cave. I’m afraid it’s not even close to fifty.”')
            jump iason_about_asterion_found02a
        'I’ve already spent the coins I found in the cave. (disabled)' if asterion_found_searched and coins < 20:
            pass
        '(lie) “I’m afraid he had just a couple of dragons with him. I don’t know where your share is.”' if asterion_found_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m afraid he had just a couple of dragons with him. I don’t know where your share is.”')
            $ pc_lies += 1
            $ iason_friendship += 2
            $ dalit_friendship += 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                'He rubs his hands together and cracks his knuckles. “May an ape shit on his ashes. Looks like I’ve been conned.” The darkness of the room gives his eyes an ominous look.
                \n\n“People used to welcome roadwardens with trust, {i}order bringers{/i}, my pa used to say. How war changes things.” He raises his hands and looks at his pink, open palms, contrasting with his purple skin. “Though in some ways, for the better.”
                \n\nHe looks down. “I’m glad you’re trustworthy. Getting to an island like that... That ain’t an easy feat. This peninsula needs people like you. There’s too many things happening away from everyone’s eyes.”
                '
                '(iason1 set)':
                    pass
        '“I found no dragon bones with him. I don’t know where your share is.”' if not asterion_found_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found no dragon bones with him. I don’t know where your share is.”')
            $ iason_friendship += 2
            $ dalit_friendship += 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                'He rubs his hands together and cracks his knuckles. “May an ape shit on his ashes. Looks like I’ve been conned.” The darkness of the room gives his eyes an ominous look.
                \n\n“People used to welcome roadwardens with trust, {i}order bringers{/i}, my pa used to say. How war changes things.” He raises his hands and looks at his pink, open palms, contrasting with his purple skin. “Though in some ways, for the better.”
                \n\nHe looks down. “I’m glad you’re trustworthy. Getting to an island like that... That ain’t an easy feat. This peninsula needs people like you. There’s too many things happening away from everyone’s eyes.”
                '
                '(iason1 set)':
                    pass

    label iason_about_asterion_found02a:
        $ iason_friendship += 4
        $ dalit_friendship += 2
        $ coins -= 20
        $ iason_friendship_moneybonus_points += 5
        show screen notifyimage( "-20", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-20 {image=cointest}{/i}')
        if iason_stance == "sittingatstove":
            $ custom1 = "taps his fingers on the stove, but takes a deep breath"
        elif iason_stance == "behindcounter":
            $ custom1 = "taps his fingers on the counter, but takes a deep breath"
        elif iason_stance == "sweeping":
            $ custom1 = "makes an angry swipe with the broom, then takes a deep breath"
        elif iason_stance == "sittingattable":
            $ custom1 = "taps his fingers on the table, but takes a deep breath"
        menu:
            'He [custom1]. “Could be worse. Keep five of them.” He looks down. “May an ape shit on his head. Looks like I’ve been conned.” The darkness of the room gives his eyes a sad look.
            \n\n“You didn’t know him, but what do you think? Was he a crook?”
            '
            '“I’m not sure. I may still find a pouch of his somewhere.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not sure. I may still find a pouch of his somewhere.”')
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    '“I’m going to keep my hopes low.” He purses his lips. “I appreciate your efforts, though. Getting to an island like that... That ain’t an easy feat. This peninsula needs people like you. There’s too many things happening away from everyone’s eyes.”
                    '
                    '(iason1 set)':
                        pass
            '“I mean... It’s the simplest answer.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mean... It’s the simplest answer.”')
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He sighs. “He might have fooled me, but there’s only so much trust I’m willing to give him. “People used to welcome roadwardens with trust, {i}order bringers{/i}, my pa used to say. How war changes things.” He raises his hands and looks at his pink, open palms, contrasting with his purple skin. “Though in some ways, for the better.”
                    \n\nHe looks down. “I’m glad you’re trustworthy. Getting to an island like that... That ain’t an easy feat. This peninsula needs people like you. There’s too many things happening away from everyone’s eyes.”
                    '
                    '(iason1 set)':
                        pass
            '“I don’t think he would try to steal from you, and even if he did, he would have had a good reason for it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think he would try to steal from you, and even if he did, he would have had a good reason for it.”')
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He purses his lips. “Maybe, maybe not. There’s only so much trust I’m willing to give him.” He sighs. “I’m going to keep my hopes low.”
                    \n\nHe looks down. “I’m glad you’re trustworthy. Getting to an island like that... That ain’t an easy feat. This peninsula needs people like you. There’s too many things happening away from everyone’s eyes.”
                    '
                    '(iason1 set)':
                        pass

#########################################

label peltnorthaboutpeninsula01:
    if not iason_about_directions:
        $ iason_about_directions = 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the peninsula?”')
        $ description_iason02a = "He arrived here about ten years ago."
        if not quest_ruins_10yclue02 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue02 = "Newcomers arrived at {color=#f6d6bd}Pelt of the North{/color}."
        menu:
            '“What could anyone say? This place doesn’t even have a name, unless there’s an old book in an archive that no soul knows about. You know what I’d call everything from here to the coast? The {i}Hunting Ground{/i},” he glances at your eyes. “But it’s not us who hunt, keep that in heart, but the beasts in all shapes and forms.”
            \n\nHis words gains confidence slowly, which is strengthened by his deep voice. “I’ve lived in this inn for over ten years now and I’ve only seen a couple of roads, a couple of places. It’s just... Once you get here and you see how harsh it is to hit the road, you have only more reasons to stay at the warm stove, behind a wall. Even if it’s... suffocating.” He looks toward the windows.
            \n\n“I’m sure you’ve heard a lot already. That the people don’t build hamlets anymore. There are no more ibexes from the South, and the traders stay for only a few days. All of our iron is used for cauldrons, not swords or tools.”
            '
            '“What will I find traveling west?”' if not iason_about_directions_west:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I find traveling west?”')
                jump peltnorthaboutpeninsula02west
            '“Are the eastern roads as rough as I’ve heard?”' if not iason_about_directions_east:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the eastern roads as rough as I’ve heard?”')
                jump peltnorthregularquestionsv02east
            '“Have you ever been to the northern coast?”' if not iason_about_directions_north:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the northern coast?”')
                jump peltnorthregularquestionsv02north
            '“That’s all I need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need.”')
                jump peltnorthregularquestionsv02
    else:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the peninsula...”')
        menu:
            '“What about it?”
            '
            '“What will I find traveling west?”' if not iason_about_directions_west:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I find traveling west?”')
                jump peltnorthaboutpeninsula02west
            '“Are the eastern roads as rough as I’ve heard?”' if not iason_about_directions_east:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the eastern roads as rough as I’ve heard?”')
                jump peltnorthregularquestionsv02east
            '“Have you ever been to the northern coast?”' if not iason_about_directions_north:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the northern coast?”')
                jump peltnorthregularquestionsv02north
            '“That’s all I need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need.”')
                jump peltnorthregularquestionsv02

    label peltnorthaboutpeninsula02west:
        $ iason_about_directions_west = 1
        #$ description_druids01 = "I can find the local druids in their cave, near the large tree in the southwest corner of the peninsula, on the edge of the swamp."
        $ description_ruinedvillage01 = "According to"
        $ description_howlersdell01 = "A prosperous village of farmers and animal breeders set along the western road."
        $ description_howlersdell05 = "The locals are following the teachings of a group of druids."
        $ description_howlersdell08a = " I’ve heard in {color=#f6d6bd}Pelt{/color} that their prices are “absurd”."
        menu:
            '“Well, there are hills nearby, then you’ll find a village, maybe an hour away from here. It was destroyed by beasts almost a decade ago, nothing to see there. The goblins live there now, so most people just travel around it. And they say it’s haunted, but who knows, who cares.”
            \n\nHe crosses his arms and starts to sway back and forth, gathering his thoughts. “You’ll get to a large tree, on the edge of the swamp. For the locals, it’s sacred.” You’re not used to hearing someone mentioning pagans as if there’s nothing unusual about them. “There’s a small path south, which leads to an old mine in the mountains, nothing to find there. But keep riding north and you’ll find {color=#f6d6bd}Howler’s Dell{/color}, set at a clean brook. Farmers live there, and mouflons, and druids. They’ll let you stay for a night, but they’re not cheap. If anyone thinks my prices are bad, it means they ain’t been to the {color=#f6d6bd}Ape Ale{/color} inn yet.” He lets out a gentle smile.
            '
            'I nod.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                jump peltnorthaboutpeninsula02westb
            'I smile politely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile politely.')
                jump peltnorthaboutpeninsula02westb

    label peltnorthaboutpeninsula02westb:
        if not description_whitemarshes01:
            $ description_whitemarshes01 = "A village set among the western bogs."
        $ description_oldpagos01 = "A western village settled on barren soil. The locals exchange their stone for supplies."
        $ description_oldpagos02 = "It’s connected strongly with the nearby Order of Truth."
        $ description_oldpagos03 = "I heard that the nearby grounds are mostly peaceful."
        menu:
            '“I know only a bit about the next settlement, {color=#f6d6bd}Old Págos{/color}. The soil there ain’t too fertile, so they work in their quarry and help other settlements build things in exchange for crops. The forests and hills ain’t too harsh, but the Seekers have a small monastery nearby, in the mountains. I don’t care much about them. They keep to themselves, and they don’t pay well.”
            \n\n“The third village is unknown to me. {color=#f6d6bd}White Marshes{/color}, set at the bogs. I’ve heard it smells like a griffon’s lair. I’ve heard a lot of nasty rumors about the place, but I won’t share them. I don’t want to be a lie spreader.”
            \n\n“So, three villages, really. {color=#f6d6bd}Howler’s{/color}, the one near {color=#f6d6bd}the monastery{/color}, whatever it’s called, and {color=#f6d6bd}Marshes{/color}. Don’t let their beds and palisades fool you, though. Weird people live there, don’t tell them more than you need to.” You wonder if it’s something he would tell other travelers as well.
            '
            '“What will I find traveling west?”' if not iason_about_directions_west:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I find traveling west?”')
                jump peltnorthaboutpeninsula02west
            '“Are the eastern roads as rough as I’ve heard?”' if not iason_about_directions_east:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the eastern roads as rough as I’ve heard?”')
                jump peltnorthregularquestionsv02east
            '“Have you ever been to the northern coast?”' if not iason_about_directions_north:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the northern coast?”')
                jump peltnorthregularquestionsv02north
            '“That’s all I need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need.”')
                jump peltnorthregularquestionsv02

    label peltnorthregularquestionsv02east:
        $ iason_about_directions_east = 1
        $ eudocia_name = "Eudocia"
        $ shortcut_pcknowsabout = 1
        $ description_shortcut01 = "I heard that it connects the monastery in the west with the watchtower in the east."
        if not quest_ruins_10yclue08 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue08 = "{color=#f6d6bd}Eudocia{/color} left {color=#f6d6bd}Old Págos{/color}."
        menu:
            '“Pretty much. Don’t leave the main road, I’d say. Not so far from here you’ll find an old dolmen. A few of my people had to spend a night there, and monkeys stole food and gauds from their bags. It was their fault. One of them had fallen asleep in the middle of his watch, but you know. The eastern forests are wild, the roads are rough. Almost no soul lives there. One day all these roads will be swallowed by the trees again.”
            \n\n“The furthest my team has ever gone was the home of the {color=#f6d6bd}enchantress{/color}. Just stay on track until you reach the crossroads, right near an abandoned watchtower. From there, turn east. You’ll recognize the place. It’s a nice home in a lonely meadow, surrounded by a wall.” He looks toward the closed window, then at you again. “Kind of like our walls, but simpler, without coating. She lives as a hermit, {color=#f6d6bd}Eudocia{/color}. I don’t even know how she survives there. But if you don’t have decent coin, you won’t find much there.”
            \n\n“So, back to the crossroads. If you turn left instead, you’ll see a road. People stay away from it. It connects the tower and the monastery, a shortcut between the two sides of the peninsula. I was warned by the locals not to use it. It already belongs to the beasts.”
            '
            '“What will I find traveling west?”' if not iason_about_directions_west:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I find traveling west?”')
                jump peltnorthaboutpeninsula02west
            '“Are the eastern roads as rough as I’ve heard?”' if not iason_about_directions_east:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the eastern roads as rough as I’ve heard?”')
                jump peltnorthregularquestionsv02east
            '“Have you ever been to the northern coast?”' if not iason_about_directions_north:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the northern coast?”')
                jump peltnorthregularquestionsv02north
            '“That’s all I need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need.”')
                jump peltnorthregularquestionsv02

    label peltnorthregularquestionsv02north:
        $ iason_about_directions_north = 1
        menu:
            '“I only know about another inn. It’s far from here, maybe a day on foot, a bit less from the eastern side.” His eyes once again focus on the floor. “I’ve never been there, but I’ve heard it’s a safe place, close to villages of fishers and hunters, though I don’t know much about them.”
            '
            '“What will I find traveling west?”' if not iason_about_directions_west:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will I find traveling west?”')
                jump peltnorthaboutpeninsula02west
            '“Are the eastern roads as rough as I’ve heard?”' if not iason_about_directions_east:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the eastern roads as rough as I’ve heard?”')
                jump peltnorthregularquestionsv02east
            '“Have you ever been to the northern coast?”' if not iason_about_directions_north:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the northern coast?”')
                jump peltnorthregularquestionsv02north
            '“That’s all I need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need.”')
                jump peltnorthregularquestionsv02

##########################

label peltnorthaboutpeltnorth01:
    if not iason_about_inn:
        $ iason_about_inn = 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t expect to find an inn of this size in a place such as this.”')
        $ description_bighunters01 = "They are led by"
        $ description_bighunters03 = "Most of them came here from the South, but some were born in the peninsula."
        $ description_iason02 = "The leader of a team of big-game hunters."
        if iason_stance == "sittingatstove":
            $ custom1 = "He pokes the wood in the stove."
        elif iason_stance == "behindcounter":
            $ custom1 = "He moves to the window and peeks outside."
        elif iason_stance == "sweeping":
            $ custom1 = "He moves to the window and peeks outside, still holding the broom."
        elif iason_stance == "sittingattable":
            $ custom1 = "He relaxes in his chair."
        menu:
            '“Ah, so you know a thing or two after all,” his mocking tone is soon replaced by a gentle smile. “It was built long before we arrived. It didn’t work out well for the previous owners. Once the war ended, they left. Not enough travelers, bad trade, the villages stick to themselves. We, however, came prepared. And now we’re prospering.”
            \n\nWhen you ask him how they can afford all the supplies, he runs his fingers through his dark hair. “I’m not against running an inn, but we don’t rely on guests. We’re the ones doing all the trading. My hunters are a clever bunch and stay safe in the forest. In exchange for furs, claws, and bones, we get what we need, and more. Both from the South and the North.”
            \n\n[custom1] “We have a good life here. We spent a whole lot on armor, crossbows, lumber, spears... But in another ten, maybe twenty years, we’ll have enough savings to move to {color=#f6d6bd}Hovlavan{/color} and not work for another day of our lives. We take risks, but smartly. The team is stronger than ever, and I have big plans for us.”
            '
            '“It’s surprising to find a purple-skinned man so far in the North.”' if not iason_about_inn_bonus1:
                $ iason_about_inn_bonus1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s surprising to find a purple-skinned man so far in the North.”')
                jump peltnorthaboutpeltnorth02
            '“Is there a good story behind the inn’s name?”' if not iason_about_inn_bonus2:
                $ iason_about_inn_bonus2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there a good story behind the inn’s name?”')
                jump peltnorthaboutpeltnorth03
            'I return to my other questions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my other questions.')
                jump peltnorthregularquestionsv02
    else:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About your inn...”')
        menu:
            '“It’s still here.”
            '
            '“It’s surprising to find a purple-skinned man so far in the North.”' if not iason_about_inn_bonus1:
                $ iason_about_inn_bonus1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s surprising to find a purple-skinned man so far in the North.”')
                jump peltnorthaboutpeltnorth02
            '“Is there a good story behind the inn’s name?”' if not iason_about_inn_bonus2:
                $ iason_about_inn_bonus2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there a good story behind the inn’s name?”')
                jump peltnorthaboutpeltnorth03
            'I return to my other questions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my other questions.')
                jump peltnorthregularquestionsv02

    label peltnorthaboutpeltnorth02:
        $ iason_name = "Iason"
        $ description_iason03 = "His purple skin combined with the clean, city accent implies that he might have been born into slavery."
        menu:
            '“I ain’t seen a soul looking like this since my ma died,” he shrugs. “It’s not a fascinating tale. Let’s just say I wasn’t a part of the invasion... Yet I’m glad it freed all those who were chained by The Cities and their corsairs.”
            \n\nHe looks at the wall.
            \n\n“I’m {color=#f6d6bd}Iason{/color}, by the way. But I rarely hear the name.”
            '
            '“It’s surprising to find a purple-skinned man so far in the North.”' if not iason_about_inn_bonus1:
                $ iason_about_inn_bonus1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s surprising to find a purple-skinned man so far in the North.”')
                jump peltnorthaboutpeltnorth02
            '“Is there a good story behind the inn’s name?”' if not iason_about_inn_bonus2:
                $ iason_about_inn_bonus2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there a good story behind the inn’s name?”')
                jump peltnorthaboutpeltnorth03
            'I return to my other questions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my other questions.')
                jump peltnorthregularquestionsv02

    label peltnorthaboutpeltnorth03:
        menu:
            '“I mean, there’s {i}a{/i} story, but not a good one.” He clears his throat. “For years I wanted to have an inn called {i}Pelt{/i}, but in my city it would be in bad taste. Taverns and inns named with a single word were cheap, had a nasty reputation. There was the {i}Claw{/i}, and {i}Mugger{/i}, {i}Basilisk{/i}, and {i}Blissful{/i}, I think. The {i}good{/i} places used at least two words. {i}Empty Barrel{/i}, {i}A Rose and a Helmet{/i}, {i}Empress’ Smile{/i}. {i}Pig Head{/i} was the exception, it was a real dive,” he chuckles.
            \n\n“In my soul it’s still just a {color=#f6d6bd}Pelt{/color}. Pelts are what we came here for, and what will make us reach our goals.”
            '
            '“It’s surprising to find a purple-skinned man so far in the North.”' if not iason_about_inn_bonus1:
                $ iason_about_inn_bonus1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s surprising to find a purple-skinned man so far in the North.”')
                jump peltnorthaboutpeltnorth02
            '“Is there a good story behind the inn’s name?”' if not iason_about_inn_bonus2:
                $ iason_about_inn_bonus2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there a good story behind the inn’s name?”')
                jump peltnorthaboutpeltnorth03
            'I return to my other questions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my other questions.')
                jump peltnorthregularquestionsv02

##########################

label peltnorthaskingforjob01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Need anything done? I could use a job.”')
    $ banditshideout_bandits_pchearedabout = 1
    menu:
        '“I assume you mean a job for a roadwarden. Tell you what.” He looks you in the eyes. “There are brigands in the woods. Our place is a stronghold, so I’m not afraid of an open strike, but they’ve gotten more active in the last two years. One day, they {i}may{/i} steal our furs, and I’ve no doubt they’re the reason why merchants come here only once. Having bandits around gets expensive.”
        \n\nHe rubs his hands together, camouflaging his pause. “I want you to reach {color=#f6d6bd}Howler’s Dell{/color}, northwest from here. It’s the largest settlement around, I’m sure you’ll get there sooner or later. Ask {color=#f6d6bd}Thais{/color}, the mayor, about {color=#f6d6bd}Glaucia{/color}, that bloodthirsty wolf of a woman. I’ve heard rumors about a raid in the North. If {color=#f6d6bd}Glaucia’s{/color} ready to break the truce with the locals, I’m willing to join forces with them to get rid of her band.”
        \n\nHe looks at a nearby dragon bone. “Not too difficult, right? Just do it when you have a chance, a couple of days won’t make much of a difference. I’ll pay you two coins when you get back with the news. Fine?”
        '
        'I nod.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
            $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me two dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
            $ quest_intelforpeltnorth_rewardvalue = 2
            $ quest_intelforpeltnorth = 1
            $ renpy.notify("New entry: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
            jump peltnorthregularquestionsv05
        '“Three.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Three.”')
            if iason_friendship > 0:
                $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me three dragons if I get in touch with the mayor of Howler’s Dell, and bring him her response."
                $ quest_intelforpeltnorth_rewardvalue = 3
                $ quest_intelforpeltnorth = 1
                $ renpy.notify("New entry: Glaucia’s Band")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He nods with a smile. “What else do you need?”
                    '
                    '(iason1 set)':
                        pass
            else:
                $ quest_intelforpeltnorth_description01 = "According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me two dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
                $ quest_intelforpeltnorth_rewardvalue = 2
                $ quest_intelforpeltnorth = 1
                $ renpy.notify("New entry: Glaucia’s Band")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Glaucia’s Band{/i}')
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He observes you for a moment. “Two,” he growls.
                    '
                    '(iason1 set)':
                        pass

label peltnorthaskingforjob02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Glaucia’s{/color} band...”')
    menu:
        'He freezes, observing your hands silently.
        '
        'He wants me to get the answer from the mayor of Howler’s Dell. (disabled)' if not quest_intelforpeltnorth_description05 and not quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description06:
            pass
        '“{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her.”' if quest_intelforpeltnorth_description05 and not quest_intelforpeltnorth_description03 and not quest_intelforpeltnorth_description08 and not iason_about_quest_glaucia_thais:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her.”')
            jump peltnorthaskingforjob02a
        '“{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her. I heard that they mostly hurt the people of {color=#f6d6bd}White Marshes{/color}.”' if quest_intelforpeltnorth_description05 and quest_intelforpeltnorth_description03 and not quest_intelforpeltnorth_description08 and not iason_about_quest_glaucia_thais:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her. I heard that they mostly hurt the people of {color=#f6d6bd}White Marshes{/color}.”')
            jump peltnorthaskingforjob02b
        '“From what I found, they mostly hurt those who live in {color=#f6d6bd}White Marshes{/color}.”' if quest_intelforpeltnorth_description03 and not quest_intelforpeltnorth_description08 and iason_about_quest_glaucia_thais:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “From what I found, they mostly hurt those who live in {color=#f6d6bd}White Marshes{/color}.”')
            jump peltnorthaskingforjob02c
        '“{color=#f6d6bd}Thais{/color} has sent me to other villages. The bandits are focused on {color=#f6d6bd}White Marshes{/color}, so she’s not interested in your deal.”' if quest_intelforpeltnorth_description06 and not quest_intelforpeltnorth_description08 and not iason_about_quest_glaucia_thais:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} has sent me to other villages. The bandits are focused on {color=#f6d6bd}White Marshes{/color}, so she’s not interested in your deal.”')
            jump peltnorthaskingforjob02d
        'He wants me to find Glaucia. (disabled)' if quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10 and not banditshideout_banned:
            pass
        '“I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”' if quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10 and banditshideout_banned:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”')
            jump peltnorthaskingforjob02ffail
        '“I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”' if quest_intelforpeltnorth_description08 and quest_intelforpeltnorth_description10:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”')
            jump peltnorthaskingforjob02f
        '“I’m on it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m on it.”')
            jump peltnorthregularquestionsv05

    label peltnorthaskingforjob02a: #“{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her.”
        $ quest_intelforpeltnorth_description02b = "I need to find out where the bandits have been active in the recent past."
        show screen notifyimage( "Journal updated: Glaucia’s Band.\n+%s" %quest_intelforpeltnorth_rewardvalue, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band. +%s {image=cointest}{/i}' %quest_intelforpeltnorth_rewardvalue)
        $ coins += quest_intelforpeltnorth_rewardvalue
        $ iason_about_quest_glaucia_thais = 1
        $ iason_stance = "behindcounter"
        menu:
            'He puts your payment on the counter, approaches a window, opens it, and looks outside.
            \n\n“I was afraid it might be like that. Times will get rough, yet there may never be a threat large enough to unite this bunch of anarchists.” He rests his hand on the windowsill. “I was hoping you would learn something more about this issue, roadwarden. Come back if you ever find any details. Like {i}if{/i} and {i}where{/i} {color=#f6d6bd}Glaucia’s band{/color} strikes. Who knows how close she really is.”
            '
            '“I’ll let you know if I learn anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if I learn anything.”')
                jump peltnorthregularquestionsv05

    label peltnorthaskingforjob02b: #“{color=#f6d6bd}Thais{/color} is not interested in further talks. The bandits don’t bother her. I heard that they mostly hurt the people of {color=#f6d6bd}White Marshes{/color}.”
        $ quest_intelforpeltnorth_description08 = "The innkeeper wants me to find the bandit’s camp and speak with {color=#f6d6bd}Glaucia{/color} herself."
        show screen notifyimage( "Journal updated: Glaucia’s Band.\n+%s" %quest_intelforpeltnorth_rewardvalue, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band. +%s {image=cointest}{/i}' %quest_intelforpeltnorth_rewardvalue)
        $ coins += quest_intelforpeltnorth_rewardvalue
        $ iason_shop_crossbow_discount += 2
        $ iason_friendship += 1
        if not iason_shop_crossbow_bought:
            $ custom1 = ", then glances at your nose. “I still have the crossbow to sell, so let’s say we’ll lower its price a bit. Just for you.” He walks toward the window, opens it, and looks outside"
        else:
            $ custom1 = ", then walks toward the window, opens it, and looks outside"
        $ iason_stance = "behindcounter"
        menu:
            'Without a word, he puts your payment on the counter[custom1].
            \n\n“I was afraid it might be like that. Times will get rough, yet there may never be a threat large enough to unite this bunch of anarchists.” He rests his hand on the windowsill. “I have another job, if you’re interested. I’ll pay you ten coins for finding out what {color=#f6d6bd}Glaucia{/color} really wants. Ideally not by a direct question, but if there’s no other way...” He shrugs.
            \n\nHe turns back to you, and for a few words, looks into your eyes. “And better act before she marks you as her next prey, being a lonely traveler and all. Work with me, and I’ll do my best to keep you safe if you ever decide to hide behind our walls.”
            '
            '“I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”' if quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10 and banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”')
                jump peltnorthaskingforjob02ffail
            '“I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”' if quest_intelforpeltnorth_description10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”')
                jump peltnorthaskingforjob02f
            '“Let’s say I find her. Any tips on how I can get on her good side?”' if not quest_intelforpeltnorth_description10 and not glaucia_metwith:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I find her. Any tips on how I can get on her good side?”')
                jump peltnorthaskingforjob02e
            '“I’m on it.”' if not quest_intelforpeltnorth_description10 and not banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m on it.”')
                jump peltnorthregularquestionsv05

    label peltnorthaskingforjob02c: #“For what I found, they focus those who live in {color=#f6d6bd}White Marshes{/color}.”
        $ quest_intelforpeltnorth_description08 = "The keeper wants me to find the bandit’s camp and speak with {color=#f6d6bd}Glaucia{/color} herself."
        $ renpy.notify("Journal updated: Glaucia’s Band")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ iason_shop_crossbow_discount += 2
        $ iason_friendship += 1
        if not iason_shop_crossbow_bought:
            $ custom1 = "He nods, then glances at your nose. “I still have the crossbow to sell, so let’s say we’ll lower its price a bit. Just for you. "
        else:
            $ custom1 = "“"
        menu:
            '[custom1]I’m glad you’ve kept your ears clean. Now, I’ll pay you ten coins for finding out what {color=#f6d6bd}Glaucia{/color} really wants. Ideally not by a direct question, but if there’s no other way...” He shrugs. For a few words, he looks into your eyes. “And better act before she marks you as her next prey, being a lonely traveler and all. Work with me, and I’ll do my best to keep you safe if you ever decide to hide behind our walls.”
            '
            '“I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”' if quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10 and banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”')
                jump peltnorthaskingforjob02ffail
            '“I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”' if quest_intelforpeltnorth_description10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”')
                jump peltnorthaskingforjob02f
            '“Let’s say I find her. Any tips on how I can get on her good side?”' if not quest_intelforpeltnorth_description10 and not glaucia_metwith:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I find her. Any tips on how I can get on her good side?”')
                jump peltnorthaskingforjob02e
            '“I’m on it.”' if not quest_intelforpeltnorth_description10 and not banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m on it.”')
                jump peltnorthregularquestionsv05

    label peltnorthaskingforjob02d: #“{color=#f6d6bd}Thais{/color} has sent me to other villages. The bandits are completely focused on {color=#f6d6bd}White Marshes{/color}, so she’s not interested in your deal.”
        $ quest_intelforpeltnorth_description08 = "The innkeeper wants me to find the bandit’s camp and speak with {color=#f6d6bd}Glaucia{/color} herself."
        show screen notifyimage( "Journal updated: Glaucia’s Band.\n+%s" %quest_intelforpeltnorth_rewardvalue, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band. +%s {image=cointest}{/i}' %quest_intelforpeltnorth_rewardvalue)
        $ coins += quest_intelforpeltnorth_rewardvalue
        $ iason_shop_crossbow_discount += 4
        $ iason_friendship += 2
        if not iason_shop_crossbow_bought:
            $ custom1 = ", then glances at your nose. “I appreciate that you’ve been so thorough. You’ve already done more than I’ve asked for. I still have the crossbow to sell, so let’s say we’ll lower its price. Just for you. Keep up the good work.” He walks toward the window, opens it, and looks outside"
        else:
            $ custom1 = ", then walks toward the window, opens it, and looks outside"
        menu:
            'Without a word, he puts your payment on the counter[custom1].
            \n\n“I was afraid it might be like that. Times will get rough, yet there may never be a threat large enough to unite this bunch of anarchists.” He rests his hand on the windowsill. “I have another job, if you’re interested. I’ll pay you ten coins for finding out what {color=#f6d6bd}Glaucia{/color} really wants. Ideally not by a direct question, but if there’s no other way...” He shrugs.
            \n\nHe turns back to you, and for a few words, looks into your eyes. “And better act before she marks you as her next prey, being a lonely traveler and all. Work with me, and I’ll do my best to keep you safe if you ever decide to hide behind our walls.”
            '
            '“I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”' if quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10 and banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Glaucia{/color} is, but she’ll kill me on sight. I can’t learn from her anything else.”')
                jump peltnorthaskingforjob02ffail
            '“I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”' if quest_intelforpeltnorth_description10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m bringing good news, I guess. {color=#f6d6bd}Glaucia{/color} has only one target right for now, and it’s the necromancers of {color=#f6d6bd}White Marshes{/color}. You have nothing to worry about, at least when it comes to her.”')
                jump peltnorthaskingforjob02f
            '“Let’s say I find her. Any tips on how I can get on her good side?”' if not quest_intelforpeltnorth_description10 and not glaucia_metwith:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I find her. Any tips on how I can get on her good side?”')
                jump peltnorthaskingforjob02e
            '“I’m on it.”' if not quest_intelforpeltnorth_description10 and not banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m on it.”')
                jump peltnorthregularquestionsv05

    label peltnorthaskingforjob02e: #Let’s say I find her. Any tips on how I can get on her good side?
        $ description_glaucia05 = "According to the {color=#f6d6bd}Pelt’s innkeep{/color}, Glaucia is more favorable toward those who don’t show their fear."
        if iason_stance == "behindcounter":
            $ custom1 = "? "
        else:
            $ custom1 = ",” he gets behind the counter. “"
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            '“Assuming she has one[custom1]I only have one tip for you. If she sees that you can be broken, she won’t hesitate to make it happen.”
            '
            '(iason1 set)':
                pass

    label peltnorthaskingforjob02ffail:
        $ quest_intelforpeltnorth_description11 = "I received my last payment for the job."
        $ quest_intelforpeltnorth = 3
        show screen notifyimage( "Quest completed: Glaucia’s Band.\n+2", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Glaucia’s Band. +2 {image=cointest}{/i}')
        $ coins += 2
        $ iason_shop_crossbow_discount += 1
        $ iason_friendship += 1
        $ minutes += 5
        # $ dalit_friendship += 1
        $ questionpreset = "iason1"
        menu:
            'He frowns in disbelief, asking you a few questions about what you’ve seen in her hideout. Before you finish with the last answer, he reaches for a pouch, but pulls out only two dragons. “You didn’t do what I hired you for, but at least I’ve learned {i}something{/i}, thanks to you.” He puts them in front of you. “Roadwardens keep being much less useful then I was hoping them to be, I must say.”
            '
            '(iason1 set)':
                pass

    label peltnorthaskingforjob02f:
        $ quest_intelforpeltnorth_description11 = "I received my last payment for the job."
        $ quest_intelforpeltnorth = 2
        show screen notifyimage( "Quest completed: Glaucia’s Band.\n+10", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Glaucia’s Band. +10 {image=cointest}{/i}')
        $ coins += 10
        $ iason_shop_crossbow_discount += 4
        $ iason_friendship += 2
        $ minutes += 5
        # $ dalit_friendship += 1
        menu:
            'He frowns in disbelief, asking you a few questions about what you’ve seen in her hideout. Before you finish with the last answer, he empties an already-prepared pouch. His gestures are impatient, but the amount of dragon bones matches his promise.
            \n\n“You did what I asked for, so these are yours now. We’ll try to hunt in the north before fall, see if you were correct.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthregularquestionsv05
            '“Something worries you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something worries you?”')
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He observes the floor for a bit, but finally waves your question off. “Their camp sounds like a well-protected place, and hidden in a dangerous spot,” he raises his eyes, though only for a moment. “If you’re wrong, we won’t get to them easily. But that’s just a thought of mine.”
                    '
                    '(iason1 set)':
                        pass
            '“You were never expecting them to strike, did you? You just wanted an unaware spy to tell you where to find them.”' if description_glaucia01c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You were never expecting them to strike, did you? You just wanted an unaware spy to tell you where to find them.”')
                $ iason_friendship += 1
                $ can_items = 1
                $ questionpreset = "iason1"
                $ description_iason08 = "He was willing to keep me in a long lie for his own gain."
                menu:
                    'He observes the floor for a bit, but finally meets your eyes. While his shoulders are tense and the fingers rub the nearby wall angrily, there’s a new sort of respect hidden in his humble smile. “{color=#f6d6bd}Asterion{/color} never told me about the hamlet, kept it a secret. I’d rather have the band in a less guarded place, and not in such a dangerous spot.” His voice is like poisonous honey. “But don’t forget where you are. You’re at my mercy, and I hope to see you as an ally, not a cunning goblin.”
                    '
                    '(iason1 set)':
                        pass

#####################################

label peltnorthquestionsplague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”')
    $ minutes += 5
    $ iason_friendship += 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "iason1"
    $ oldpagos_plague_warnedplaces += 1
    if iason_stance == "behindcounter":
        $ custom1 = "counter"
    elif iason_stance == "sittingatstove":
        $ custom1 = "fire"
    elif iason_stance == "sittingattable":
        $ custom1 = "table"
    else:
        $ custom1 = "floor"
    menu:
        'He sighs and puts his muscled arm on his head, then asks you about the state of the village and the symptoms you know of. After a short conversation, he observes the [custom1].
        \n\n“I was planning to get in touch with those stonecutters. Thank you for bringing me the news. Let’s hope they can make it until spring.”
        '
        '(iason1 set)':
            pass

label peltnorth_iason_about_workforquintus01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s this gatekeeper, {color=#f6d6bd}Quintus{/color}...”')
    if iason_stance == "behindcounter":
        $ custom1 = "at a mug"
    elif iason_stance == "sittingatstove":
        $ custom1 = "into the fire"
    elif iason_stance == "sittingattable":
        $ custom1 = "at a mug"
    else:
        $ custom1 = "at the window"
    menu:
        'He looks [custom1], listening to your tale. “So what do you expect me to do with him, once he’s here?”
        '
        '“He can handle some easy tasks. Ask him to be on the lookout for the beasts and travelers.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He can handle some easy tasks. Ask him to be on the lookout for the beasts and travelers.”')
            $ iason_about_workforquintus = "guard"
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                '“The hunters can do this and much more, and they don’t drink as much,” he glances at the stairs and rubs his arm gently, “but I guess they won’t refuse some looser hours. Bring him here. I offer him gruel and a corner to sleep, but I won’t pay him until he proves himself.”
                '
                '(iason1 set)':
                    pass
        '“He’s a brave, strong soul. He could assist your hunters on their trips.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s a brave, strong soul. He could assist your hunters on their trips.”')
            $ iason_about_workforquintus = "hunter"
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "iason1"
            menu:
                '“We use our wits and traps, not so much brute force, but I guess you’re right. A fierce fighter may be of use.” He rubs his arm and reaches for a piece of roasted lizard. “Bring him here. I offer him gruel and a corner to sleep, and I’ll pay him once he helps us catch some worthy game.”
                '
                '(iason1 set)':
                    pass

#####################################
label peltnorthrumors01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to ask about someone.”')
    if iason_friendship < iason_rumors_threshold: # (iason_friendship+appearance_charisma) < iason_rumors_threshold:
        $ iason_rumors_introduction = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        menu:
            'He crosses his arms. “I don’t like to talk about people who ain’t nearby. Show me first that you’re someone worth changing habit for.”
            '
            '(iason1 set)':
                pass
    else:
        $ iason_rumors_introduction = 2
        menu:
            'He crosses his arms. “I don’t like to talk about people who ain’t nearby... But you know what you’re doing. Who are you wondering about?”
            '
            '“Tell me about...”':
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("Who are you asking about? (example: empress)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                $ tutorial_input = 2
                jump peltnorthrumors02

label peltnorthrumors01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any rumors worth sharing?”')
    if iason_about_hava == 1 and iason_friendship >= 10:
        $ iason_about_hava = 2
        menu:
            '“You know what... I may be ready to speak with you about {color=#f6d6bd}Old Hava{/color} again.”
            '
            '“Tell me about...”':
                python:
                    search = renpy.input("Who are you asking about? (example: empress)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
    elif iason_friendship >= 4 and not iason_about_pagans_hunterdruid and iason_about_pagans and not iason_about_pagans_encourages:
        $ iason_about_pagans_encourages = 1
        menu:
            '“Let me think... Remember how you asked me about the pagans? I’ve got something to say about the druids.”
            '
            '“Tell me about...”':
                python:
                    search = renpy.input("Who are you asking about? (example: empress)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
    else:
        if iason_rumors_introduction == 0:
            $ iason_rumors_introduction = 2
            menu:
                'He crosses his arms. “I don’t like to talk about people who ain’t nearby... But you know what you’re doing. Who are you wondering about?”
                '
                '“Tell me about...”':
                    if not tutorial_input:
                        $ tutorial_input = 1
                    python:
                        search = renpy.input("Who are you asking about? (example: empress)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    $ tutorial_input = 2
                    jump peltnorthrumors02
        elif iason_rumors_introduction == 1:
            $ iason_rumors_introduction = 2
            menu:
                'He sighs and looks out a window. “Fine. You know what you’re doing. Who are you wondering about?”
                '
                '“Tell me about...”':
                    if not tutorial_input:
                        $ tutorial_input = 1
                    python:
                        search = renpy.input("Who are you asking about? (example: empress)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    $ tutorial_input = 2
                    jump peltnorthrumors02
        else:
            $ custom1 = renpy.random.choice(['“Who are you thinking about?”', '“Just ask.”', 'He sighs.', 'Without a word, he looks at his boots.'])
            python:
                search = renpy.input("%s" %custom1, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "no one"
            $ tutorial_input = 2
            jump peltnorthrumors02

    label peltnorthrumors02:
    #EASTER EGGS
    if search == "noone" or search == "nobody" or search == "anyone" or search == "whatever" or search == "" or search == " " or search == "no shell" or search == "someone" or search == "shell" or search == "soul" or search == "nosoul":
        menu:
            '“Don’t waste my time.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "deity" or search == "thedeity" or search == "wright" or search == "thewright" or search == "god" or search == "divine" or search == "planescapetorment" or search == "planescape":
        menu:
            'He smirks and glances at the ceiling. “I don’t know them that well. If you want to hunt down a beast, you need to know where it sleeps. But where’s Wright’s bed? And how many blades can they swallow before they die?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "empress" or search == "emperor":
        menu:
            '“What do you mean? Are you trying to find her, after all these years?” He chuckles. “The empress is gone. And she will never be back. She’s as dead as shit.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "pokemon":
        menu:
            '“Don’t ruin the mood.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "me" or search == "myself" or search == "i" or search == "newroadwarden" or search == pcname_reduced:
        menu:
            '“Don’t get awkward, roadwarden.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "giant" or search == "giants" or search == "agiant" or search == "thegiant" or search == "thegiants":
        menu:
            '“I don’t have space in my soul to memorize such old tales. There are no giants, there never were, who cares?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag" or search == "bitch" or search == "whore" or search == "cunt":
        python:
            search = renpy.input("...Let’s try this again. Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
            search = search.strip().lower().replace(" ", "")
            if not search:
                search = "nothing"
        jump peltnorthrumors02
    ##### REAL ANSWERS
    elif search == "aegidia" or search == "aegida" or search == "thaislostdaughter" or search == "thaisslostdaughter":
        menu:
            '“Ah. She was a tearful girl, but had a good eye. It was sad news, her death. There ain’t many people willing to spend years with a bow. One day, she would have made a fine huntress.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "aeli":
        $ description_aeli01 = "According to"
        menu:
            '“I only know what I’ve heard. An important alchemist, but all the monks are the same, they think they’re smarter than everyone else. In his youth he used to be a thief of sorts, or maybe a bandit? But it was before the war. You’ll find him in {color=#f6d6bd}the monastery{/color}, or in {color=#f6d6bd}Old Págos{/color}.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "akakios" or search == "howlersdelltrader" or search == "traderfromhowlersdell" or search == "howlersdellmerchant" or search == "merchantfromhowlersdell" or search == "howlerstrader" or search == "traderfromhowlers" or search == "dellmerchant" or search == "merchantfromhowlers":
        if not iason_about_akakios:
            $ description_akakios02 = "According to"
            menu:
                '“The big guy, right? We barter in {color=#f6d6bd}Howler’s{/color} with him. We get coins, food supplies, and linen, so don’t expect him to give you any good prices for furs and trophies.”
                '
                '“{i}Big guy{/i}, you say? He actually lost a lot of weight.”' if howlersdell_akakios_firsttime:
                    $ iason_friendship += 1
                    menu:
                        '“That’s good to hear,” he smiles. “It’s better for the heart and legs. And soul, also.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            # He pauses and looks at something beneath the counter. “But he’s always interested in whatever has magic in it, blades, wands. Things like that.”
            menu:
                '“We barter in {color=#f6d6bd}Howler’s{/color} with him. We get coins, food supplies, and linen, so don’t expect him to give you any good prices for furs and trophies.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "armorer" or search == "thearmorer" or search == "oldarmorer" or search == "mutearmorer" or search == "mute":
        menu:
            '“He used to be able to speak. A sad fate, and a {i}painful{/i} one. One day he ate an undercooked slice of meat on his journey South, and after a few weeks he realized that something was biting his tongue. Something was living in it, like a worm in an apple. We tried to kill it with fire and hard drinks, but it was too late. The flesh started to rot, we had to amputate it. He can’t help other hunters without speaking or shouting, so he’s learning a new trade now.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "armorersstudent" or search == "armorersboy" or search == "youngarmorer" or search == "theyoungarmorer" or search == "armorersapprentice" or search == "boy" or search == "theboy" or search == "youngster" or search == "theyoungster":
        menu:
            '“Well, he works, so he can stay, at least until he gets older, then he’ll have to prove himself. We found him on the road in the South not so long ago, lost his entire family to trolls. Since the armorer needed someone to help him, we gave him a chance.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "asterion" or search == "previousroadwarden" or search == "roadwarden" or search == "oldroadwarden":
        if not iason_about_asterion_found:
            $ description_asterion03 = "According to"
            $ description_asterion03b = ", {color=#f6d6bd}Asterion{/color} tried to stay impartial and didn’t tie himself to any village, so there’s a good chance that he’s already dead. It’s possible that someone knows exactly what happened to him, or even set him up."
            menu:
                '“Well, not a large man, though broad-shouldered. Red hair and beard. I don’t know what to say.” He raises a muscled arm and places a hand on the back of his head. “He was a fine fellow, but I doubt he’s alive. He always tried to... stay away from things, let’s say. People knew him, but he didn’t really have allies. Maybe the locals know what happened to him, yet decided not to help him. Or they wanted to get rid of him.”
                \n\nHe leans forward, looks at his boots. “{color=#f6d6bd}Asterion{/color} was a fine man. A quiet one, but not dumb. He aided me many times, not for free, of course. And when he couldn’t finish the job, it was for damn good reasons. And you know what?” He looks you in the eyes. “He was scrupulous. Patient. I’d be shocked if he died because of some mistake of his. Maybe the bandits got to him, why not?”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            if not description_asterion03b:
                $ description_asterion03 = "According to"
                $ description_asterion03b = ", {color=#f6d6bd}Asterion{/color} tried to stay impartial and didn’t tie himself to any village."
            menu:
                '“Well, you already know what happened to him.” He shrugs. “He used to be a short man, though broad-shouldered. Red hair and beard. He always tried to... stay away from things, let’s say. People knew him, but he didn’t really have allies. And we can see where it led him.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "baldy":
        menu:
            '“He’s been with us from the beginning. His family carries power in their blood, he’s the unfortunate one that struggles with the simplest spells. Only after he joined us did we realize how sharp his senses are, like a wolf’s. Turns out he still has the talent, it just moved from his will and hands to his eyes and ears.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "beholder" or search == "thebeholder":
        menu:
            'He scratches his head. “Is this a soul carrier? A shaman? Ah, wait!” He crosses his arms. “It’s that large tree, the one that drinks blood. I saw it, but I don’t need some dark powers to protect me. I don’t care what the druids teach.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "bion" or search == "howlersdelltailor" or search == "tailorfromhowlersdell" or search == "howlerstailor" or search == "tailorfromhowlers" or search == "delltailor":
        menu:
            '“{color=#f6d6bd}Bion{/color} the tailor? A quiet one. Everything we wear is from her, this included.” He grabs the bottom part of his tunic and stretches it a bit. “Looks good, don’t you think? Most of the clothes we brought from home got ruined after several years, and our gambesons need a lot of repairs.” He suddenly lets go of his outfit. “Know what? {color=#f6d6bd}Bion{/color} has asked us to bring her any spider silk we find. If you ever get some threads, sell them to her.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "boar" or search == "pig" or search == "yourboar":
        menu:
            '“It’s... Just a boar,” he glances at you without understanding. “It eats whatever it finds, and since {color=#f6d6bd}Dalit{/color} wants it to stay with us, all it’s good for is dropping manure. But even that’s shitty,” he hesitates, “and by that I mean it’s not as good as mouflons’. We use it as a bait behind the wall.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "caius" or search == "onehandsoldier" or search == "onearmsoldier" or search == "deserter" or search == "thedeserter":
        $ foragers_caius_heardabout += 1
        menu:
            'He pauses. “{color=#f6d6bd}Caius{/color}... That’s {color=#f6d6bd}Tulia’s{/color} soldier who lost his hand, right?” He waits for your confirmation “He asked me for work, but was speaking like a mad man. I lent him a bed, and after a long sleep and a good meal he was still of no worth to us, and I don’t run a house for hobos. Told him to go north, but he went east instead. I’m surprised he’s not dead, but have no clue why {color=#f6d6bd}Foggy{/color} would keep him around.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "dalit" or search == "girlinyellowarmor" or search == "yellowarmor" or search == "theguardinyellowarmor" or search == "thewomaninyellowarmor" or search == "guardinyellowarmor" or search == "womaninyellowarmor" or search == "redhead" or search == "girlinyellowjacket" or search == "yellowjacket" or search == "guardinyellowjacket" or search == "womaninyellowjacket" or search == "womanwithredhair" or search == "redhairwoman" or search == "redhairedwoman" or search == "girlinyelowarmor" or search == "yelowarmor" or search == "theguardinyelowarmor" or search == "thewomaninyelowarmor" or search == "guardinyelowarmor" or search == "womaninyelowarmor" or search == "redhead" or search == "girlinyelowjacket" or search == "yelowjacket" or search == "guardinyelowjacket" or search == "womaninyelowjacket" or search == "girlinyellowgambeson" or search == "yellowgambeson" or search == "theguardinyellowgambeson" or search == "thewomaninyellowgambeson" or search == "guardinyellowgambeson" or search == "womaninyellowgambeson" or search == "girlinyelowgambeson" or search == "yelowgambeson" or search == "theguardinyelowgambeson" or search == "thewomaninyelowgambeson" or search == "guardinyelowgambeson" or search == "womaninyelowgambeson" or search == "yelowjacket" or search == "hunterinyelowjacket" or search == "huntressinyelowjacket" or search == "girlinyellowgambeson" or search == "yellowgambeson" or search == "thehunterinyellowgambeson" or search == "thehuntressinyellowgambeson" or search == "hunterinyellowgambeson" or search == "huntressinyellowgambeson" or search == "girlinyelowgambeson" or search == "yelowgambeson" or search == "thehunterinyelowgambeson" or search == "thehuntressinyelowgambeson" or search == "hunterinyelowgambeson" or search == "huntressinyelowgambeson" or search == "thehunterinyellowarmor" or search == "thehuntressinyellowarmor" or search == "hunterinyellowarmor" or search == "huntressinyellowarmor":
        $ dalit_name = "Dalit"
        $ description_dalit02 = "According to"
        $ description_dalit02b = ", she’s a master of the crossbow. He’s known her since she was a child."
        menu:
            '“Ah, {i}our{/i} {color=#f6d6bd}Dalit{/color}? Why do you ask? I’ve known her since she was a girl, so you’d better not bother her. If you’re looking for a master of the crossbow, she’s an obvious pick.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "decima":
        menu:
            '“I don’t know who that is. I’ve heard about some sorceress of this name, someone from the West. I’m sure she wasn’t here.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "elpis":
        if not quest_ruins_10yclue03 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue03 = "{color=#f6d6bd}Elpis{/color} became the leader of the druids in {color=#f6d6bd}Howler’s Dell{/color}."
        menu:
            '“I ain’t met her, the priests don’t want to speak with strangers. But I’ve heard this and that. More of a sorceress than a fighter. She’s been the leader of the druids for about ten years now, I believe. She’s...” He looks around and leans closer to you. “I heard that as the years go by, the druids are turning {i}wilder{/i}, less human, you see? And I’ve heard she’s already halfway there.” He nods, then straightens up. “There must be a reason why Wright’s folks were fighting the druids. Their blood gets bad.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "elah" or search == "ellah":
        $ elah_efren_siblings = 1
        $ description_elah_efren01 = "{color=#f6d6bd}Elah{/color} tries to carry a big burden, being one of the very few people in his tribe willing to plan for the future."
        menu:
            '“He ain’t like his brother, {color=#f6d6bd}Efren{/color}. He doesn’t fight, and was here only once, simply to introduce himself to me. {color=#f6d6bd}Elah{/color} may be only twenty... something, but he carries a soul twice his age, and that’s a good thing. You know, in {color=#f6d6bd}Creeks{/color} there are either elders, or kids, they lack those who would put together plans for the years to come. That’s a big burden to carry in a village where every adult has a right to vote, but most of them don’t care about anything that won’t land in their bowls or beds.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "eulalia" or search == "ireneus" or search == "eudocia_parents" or search == "eudociasparents" or search == "parentsofeudocia" or search == "eulaliaandireneus" or search == "ireneusandeulalia":
        if iason_about_eudocia_parents:
            menu:
                '“You know what happened to them. They were artists from {color=#f6d6bd}Old Págos{/color}, a couple. {color=#f6d6bd}Eulalia{/color} and {color=#f6d6bd}Ireneus{/color}. They’ve never been here, but I’ve heard about their works for the monastery. Ambitious people, with strong arms despite their age. They were hoping to sell some sculptures in the South.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            menu:
                '“They’re those artists from {color=#f6d6bd}Old Págos{/color}, am I right? {color=#f6d6bd}Eulalia{/color} and {color=#f6d6bd}Ireneus{/color}, a couple. They’re old, they’ve never been here, but I’ve heard about their works for the monastery. Ambitious people. They still have strong arms and were hoping to sell some sculptures in the South. We plan to meet with them and discuss it.”
                '
                '“I bring sad news about these two.”' if oldpagos_about_eudocia_parents:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring sad news about these two.”')
                    if not iason_shop_crossbow_bought and not item_crossbow:
                        $ iason_shop_crossbow_price -= 2
                    elif not iason_shop_shield_bought and iason_shop_shield_price:
                        $ iason_shop_shield_price -= 1
                    $ iason_friendship += 1
                    $ iason_about_eudocia_parents = 1
                    menu:
                        'You explain what happened to them, and he looks through you. “Too bad. At least we’ll know to give up on our plans, without wasting any more time.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "eudocia" or search == "crafter" or search == "magiccrafter" or search == "enchantress" or search == "enchanter":
        $ eudocia_name = "Eudocia"
        $ description_eudocia01 = "According to"
        $ description_eudocia01b = ", she’s insane and lives alone, {i}skinny and dirty{/i}, protected by her golems. She “never cries and never smiles”."
        menu:
            '“Oh, {color=#f6d6bd}Eudocia{/color} is {i}crazy{/i}. She lives in a lonely house all by herself, skinny and dirty like a corpse eater, surrounded by golems. Never smiles, never cries, one of those. She never leaves her home and if you see it from far away, it looks abandoned. Few times a year people travel to her and trade barrels of food for magical items.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "eryx" or search == "apealeinnkeeper" or search == "aleapeinnkeeper" or search == "thaishusband" or search == "thaisshusband" or search == "otherinnkeeper" or search == "otherinnkeep":
        menu:
            '“Let me think...{color=#f6d6bd}Thais’{/color} husband? I’ve barely talked to him, ever. He stays inside, cooking. And spends a lot of time with their children, or in the garden. I admire people who take care of orphans, especially if they treat them like their own, not just as a free hand to plow the field.” He tilts his head to the right and frowns gently. “But I also don’t think he’s much of an innkeeper.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "foggy" or search == "othertavernkeeper" or search == "tavernkeeper" or search == "tavernkeep":
        $ description_foggy01 = "According to"
        $ description_foggy01b = ", she often organizes large feasts and likes to drink a lot. She appreciates those who are promising allies in trade."
        menu:
            '“You mean {color=#f6d6bd}Foggy the tavernkeeper{/color}, I assume. You’ll find her on the northern road, far from here. Truth be told, I don’t know much about her. Tavern and inn owners don’t have many opportunities to see each other.” He chuckles. “But she’s a fun one. Drinks a lot, makes feasts, ain’t as scared of beasts as most people. Looks like there’s some good coin to be made in her scrap of the peninsula.” He looks away. “Who’d have guessed? Or maybe she just has a nose for coins.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "banditleader" or search == "glaucia" or search == "leaderofbandits" or search == "theleaderofbandits":
        $ description_glaucia01 = "According to"
        $ description_glaucia01b = ", she’s tanned, wrinkled by age. Charismatic, {i}strong{/i}, {i}scary{/i}. He heard that she was born in one of the northern villages. He claims that she wanted to move into {color=#f6d6bd}Pelt of the North{/color}."
        $ banditshideout_bandits_pchearedabout = 1
        menu:
            '“I’ve met her more than once. She’s older than me, wrinkled. Tanned. I don’t know how she has survived for so long. I’ve heard she’s from the coast. I don’t really know her story.”
            \n\n“She’s strong, though, and convincing. She wanted to move her band to {color=#f6d6bd}Pelt{/color}, make huts in the courtyard. When I told her to leave, she didn’t make a scene or anything. But her face... It was chilling.” He looks at the stove. “And she may want revenge. {color=#f6d6bd}Glaucia{/color} is a cruel soul in a scary shell.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "bandits" or search == "bandit" or search == "highwaymen" or search == "highwayman" or search == "brigands" or search == "brigand":
        $ banditshideout_bandits_pchearedabout = 1
        menu:
            '“I don’t know much about them, just that they’ve been here for a long time now. {color=#f6d6bd}Glaucia{/color} leads them. Ah, and there was another band in the camp, south from here, but they’re gone now, thanks to the previous lieutenant.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "yourself" or search == "iason" or search == "you":
        $ iason_name = "Iason"
        menu:
            '“There’s nothing you need to know about me to survive on the road. I’m {color=#f6d6bd}Iason{/color}. I’ve been in a city, now I’m here.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "illan" or search == "ilan" or search == "tzvi" or search == "zvi" or search == "cvi" or search == "foggysforagers" or search == "foggyforagers" or search == "foggylakeforagers":
        $ description_creeks04 = "“Simple, but honest people... They drink a fair bit, but you wouldn’t believe how much they eat. And not just groats, but meats. They have no druids around, but none would want to live with them. They are a well without a bottom.”"
        menu:
            '“The foragers? They were here a few times with the trading band from {color=#f6d6bd}Creeks{/color}. Simple, but honest ones, just like the rest of their village. Too clumsy to hunt, especially {color=#f6d6bd}Ilan{/color}, but they know how to handle themselves.” Lost in his thoughts, he goes on without looking at you. “They drink a fair bit, but you wouldn’t believe how much they eat. And not just groats, but meats. They have no druids around, but none would want to live with them. They are like a well without a bottom. And {color=#f6d6bd}Tzvi{/color}...” He glances at you and shakes his head slightly. “Let’s just say a trail of nasty rumors follows him.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "oldlieutenant" or search == "previouslieutenant":
        menu:
            '“A decent man, a bit of a talker. Open for a challenge. He had his secrets, and I didn’t have a reason to pressure him.”
            \n\nAfter a brief pause, he sighs. “He didn’t tell me about his plans to attack the bandits. He was afraid we would betray him. If I had known, we would have assisted the squad with our crossbows. Such a pointless death.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "nalia" or search == "gargoyleslayer":
        $ description_nalia01 = "She is known as {color=#f6d6bd}Nalia, the Gargoyleslayer{/color}."
        menu:
            '“Not sure who you’re talking about. Is she a farmer? Oh, {color=#f6d6bd}Nalia, the Gargoyleslayer{/color}? I know the tales, of course, but I don’t know why you think she may be in the North. Are you sure she’s still alive?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    # elif search == "nalia" or search == "Gargoyleslayer" or search == "gargoyleslayer":
    #     if iason_about_nalia:
    #         $ description_nalia01 = "She is known as {color=#f6d6bd}Nalia, the Gargoyleslayer{/color}."
    #         menu:
    #             '”{color=#f6d6bd}The Gargoyleslayer{/color}? I don’t know much more about her, and unlike you, I’ve never met her. I bet the tales about her are fulsome, but I must say, they’ve sparked my curiosity. Shooting down a gargoyle with a ballista, in the middle of {color=#f6d6bd}Hovlavan{/color}? Not a plan I’d expect from a mercenary.”
    #             '
    #             '“How about...”':
    #                 python:
    #                     search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                     search = search.strip().lower().replace(" ", "")
    #                     if not search:
    #                         search = "no one"
    #                 jump peltnorthrumors02
    #             '“Let’s change the topic.”':
    #                 jump peltnorthregularquestionsv04
    #     else:
    #         $ description_nalia01 = "She is known as {color=#f6d6bd}Nalia, the Gargoyleslayer{/color}."
    #         menu:
    #             '“I’m, not sure who you’re talking about. Is she a farmer? Oh, {color=#f6d6bd}Nalia, the Gargoyleslayer{/color}? I know the tales, of course, but I don’t know why you think she may be in the North. Are you sure she’s still alive?”
    #             '
    #             '“Actually, she’s here, in the peninsula. She’s staying at {color=#f6d6bd}Foggy’s{/color} place.”' if description_nalia03:
    #                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, she’s here, in the peninsula. She’s staying at {color=#f6d6bd}Foggy’s{/color} place.”')
    #                 $ iason_about_nalia = 1
    #                 if not iason_shop_crossbow_bought and not item_crossbow:
    #                     $ iason_shop_crossbow_price -= 2
    #                 elif not iason_shop_shield_bought and iason_shop_shield_price:
    #                     $ iason_shop_shield_price -= 1
    #                 $ iason_friendship += 1
    #                 menu:
    #                     'He frowns. “Truly? Meeting her would be quite something. I bet the tales about her are fulsome, but I must say, they’ve sparked my curiosity. Shooting down a gargoyle with a ballista, in the middle of {color=#f6d6bd}Hovlavan{/color}? Not a plan I’d expect from a mercenary.”
    #                     \n\n
    #                     '
    #                     '“How about...”':
    #                         python:
    #                             search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                             search = search.strip().lower().replace(" ", "")
    #                             if not search:
    #                                 search = "no one"
    #                         jump peltnorthrumors02
    #                     '“Let’s change the topic.”':
    #                         jump peltnorthregularquestionsv04
    #             '“How about...”':
    #                 python:
    #                     search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                     search = search.strip().lower().replace(" ", "")
    #                     if not search:
    #                         search = "no one"
    #                 jump peltnorthrumors02
    #             '“Let’s change the topic.”':
    #                 jump peltnorthregularquestionsv04
    elif search == "navica" or search == "galerocksboatmaker" or search == "galerockboatmaker":
        $ iason_about_navica = 1
        menu:
            '“She’s from {color=#f6d6bd}Gale Rocks{/color}, ain’t she? One of the sea folk, a boat maker. I heard that she got mauled by a dragonling, almost died. Ever since, she’s all about work, and gets shaky if anyone raises their voice around her, or even laughs too loudly.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "team" or search == "yourteam" or search == "yourpals" or search == "hunter" or search == "hunters" or search == "guards" or search == "staff" or search == "yourfriends" or search == "biggamehunters" or search == "gamehunters":
        $ description_bighunters01 = "They are led by"
        $ description_bighunters02 = "According to"
        $ description_bighunters02b = ", they are cautious and value teamwork above all else."
        $ description_bighunters03 = "Most of them came here from the South, but some were born in the peninsula."
        $ description_iason02 = "The leader of a team of big-game hunters."
        menu:
            '“My team is more than a dozen people strong,” he says with confidence. “And all of them are experienced hunters. They work for coins, sure, but we put our lives first, I don’t allow any recklessness. Over the past ten years only four of us have died, and two of them from sickness. With the kids from the villages who have joined us, we’re doing better than fine.”
            \n\nHe looks around and leans toward you. “A crappy warrior in the forests gives only worries, and I’m the one who decides who’s in. They train, learn how to understand one another in the middle of chaos, about monsters and traps. Teamwork, that’s the key. With our walls and a bunch such as this, it’s the safest place in the North. At least as long as the dragons stay away.” He chuckles.
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "pyrrhos" or search == "pyrros" or search == "scavenger":
        if not pyrrhos_peltnorth:
            menu:
                '“First time I’ve heard of them.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        if pyrrhos_peltnorth and pyrrhos_peltnorth_counter == day:
            menu:
                '“I just met him. Seems like a handy guy.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        if pyrrhos_peltnorth and pyrrhos_peltnorth_counter != day:
            menu:
                '“I don’t understand people who choose to be vagabonds, but I do grasp that some can’t bear the sight of their {i}home{/i}, they just have to leave it. I just think one should do their best creating their own place, or finding people to whom they belong. I don’t see a point in wandering like an outlaw.”
                \n\n“He knows a thing or two, I must admit. Though he’s slacking off.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "tulia" or search == "lieutenant" or search == "soldier" or search == "soldiers":
        if tulia_pelt_inside and not tulia_pelt_left:
            menu:
                'He glances at her. “The potions are serving her well.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            $ description_tulia02 = "She didn’t expect to become a lieutenant and most members of her squad are already dead."
            $ description_tulia03 = "According to"
            $ description_tulia03b = ", she’s more efficient when she has someone to order her around."
            menu:
                '“I ain’t seen {color=#f6d6bd}Tulia{/color} in quite some time. Since her squad vanished in the fogs, she’s been careful. Glad to know she’s still alive. She’s too inexperienced to lead others to battle, I think.” He shrugs. “Like most people, she needs to follow others, but she already knows that. There’s nothing worse than a fighter too stupid to limit their ambitions.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "monastery" or search == "monks" or search == "monk":
        $ description_monastery01 = "the monastery has unusual teachings, and the monks are experienced alchemists."
        menu:
            '“The monks are... Unusual. I’ve heard they live in isolation, locked in their mountain like prisoners. My team saw wagons from {color=#f6d6bd}Old Págos{/color} that were carrying wood and stone to the monastery, but I don’t what for.”
            \n\nHe scratches his head. “We were also invited to a wedding that took place in the village, and they were reciting lines from Wright’s Tablets. Didn’t feel like some forbidden heresy, you feel me?”
            \n\n“At least the monks know a lot about alchemy. Their potions play a big part during our hunting trips.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "necromancer" or search == "necromancers" or search == "necromancy" or search == "druid" or search == "druids" or search == "pagan" or search == "pagans" or search == "bloodmagicians" or search == "bloodmagic" or search == "bloodsorcerers" or search == "bloodsorcerer":
        if iason_friendship >= 4 or iason_about_pagans_hunterdruid == 1:
            $ iason_about_pagans = 1
            $ iason_about_pagans_hunterdruid = 1
            $ iason_about_pagans_encourages = 1
            $ description_druids03 = "According to"
            $ description_druids03b = ", one of the hunters who lives in his inn shares a {i}past{/i} with the local druids."
            menu:
                'When he crosses his arms, the room gets a bit colder. “I’m a city man, roadwarden. I’ve seen dozens of priests and monks saying the craziest shit for the sake of coin, dominance, and obsessions. Pagans, druids, necromancers... I don’t care about any of it, as long as they keep to themselves. The locals ain’t hostile, and I won’t repay them by spreading rumors about them.”
                \n\n“However... You may want to talk with my team about the druids. One of the boys shares a bit of a... past with them.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            $ iason_about_pagans = 1
            menu:
                'When he crosses his arms, the room gets a bit colder. “I’m a city man, roadwarden. I’ve seen dozens of priests and monks saying the craziest shit for the sake of coin, dominance, and obsessions. Pagans, druids, necromancers... I don’t care about any of it, as long as they keep to themselves. The locals ain’t hostile, and I won’t repay them by spreading rumors about them.”
                '
                'He doesn’t trust me enough to tell me more. (disabled)' if iason_friendship < 4:
                    pass
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "archdruid" or search == "thearchdruid" or search == "olddruid" or search == "theolddruid" or search == "oldforestspeaker" or search == "elpisfather" or search == "theelpisfather" or search == "elpisparent" or search == "theelpisparent" or search == "elpisdad" or search == "theelpisdad" or search == "altarwarden" or search == "thealtarwarden" or search == "altardruid" or search == "thealtardruid" or search == "thehermit" or search == "hermitincave" or search == "hermitinacave" or search == "hermitinthecave" or search == "thehermitincave" or search == "thehermitinacave" or search == "thehermitinthecave":
        menu:
            '“I’ve heard about him, yes, he even crossed this road once or twice, but never entered. The father of the current archdruidess, {color=#f6d6bd}Elpis{/color}. Years surrounded with pneuma and visions - can’t be healthy for you.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "thyrsusparents" or search == "thyrsussparents" or search == "thethyrsusparents":
        menu:
            '“No such couple ever visited. Folks from {color=#f6d6bd}White Marshes{/color} rarely do.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "thetalldruid" or search == "druidguard" or search == "guardofdruids":
        menu:
            '“That one, right. Looks more like a fighter, than a druid, correct? I’ve heard about him, but nothing interesting. Just that he’s always around, giving people looks.”
            \n\n
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "jocasta" or search == "iocasta" or search == "jokasta":
        menu:
            '“Never heard this name.”
            '
            '“She’s a forager. Lives in {color=#f6d6bd}Howler’s{/color}.”' if elpis_about_thyrsusgift_name_asked and not iason_about_jocasta:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s a forager. Lives in {color=#f6d6bd}Howler’s{/color}.”')
                $ iason_about_jocasta = 1
                menu:
                    '“Alright,” he quickly loses interest.
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump peltnorthrumors02
                    '“Let’s change the topic.”':
                        jump peltnorthregularquestionsv04
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "hava" or search == "havva" or search == "oldhava" or search == "oldhavva" or search == "erith" or search == "olderith":
        if description_creeks08 or iason_about_hava == 2:
            label iasononoldhava:
                $ description_creeks08 = "{color=#f6d6bd}Old Hava{/color} used to be an infamous highwaywoman. Some of the {i}mysterious{/i} disappearances that brought a bad name on the peninsula were tied to bounty hunters who were chasing after her."
                menu:
                    'He tells everyone inside to leave the room for a few minutes, then leans closer to you, almost whispering. He smells of hops and soil. “Her previous name was Erith, {color=#f6d6bd}Erith the highwaywoman{/color}.” He makes sure you’re listening. “She went to {color=#f6d6bd}Creeks{/color} as a settler, but after a few years the first group of adventurers came for her head. Then another one, and then one more. It was long before my group arrived here, but I’ve no doubt not {i}all{/i} of them were eaten by trolls and wolves, you see?” He looks out the windows, still speaking. “I’ve heard from a trusted source that she’s not killing people left and right all by herself. Her tribe keeps her safe. They {i}all{/i} know.”
                    \n\nHe leans away, waving for the hunters to come back. “But these are all old tales. She’s harmless now.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump peltnorthrumors02
                    '“Let’s change the topic.”':
                        jump peltnorthregularquestionsv04
        else:
            if not iason_about_hava:
                $ iason_about_hava = 1
            menu:
                'He freezes. “I...” He looks at the door. “It ain’t my story to tell, roadwarden. And you may be wiser to not ask for it.”
                '
                '“Don’t you think I’ve done enough to gain your trust?”' if iason_friendship >= 10:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you think I’ve done enough to gain your trust?”')
                    jump iasononoldhava
                'He doesn’t trust me enough to tell me more. (disabled)' if iason_friendship < 10:
                    pass
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "younghava" or search == "younghavva":
        menu:
            '“From {color=#f6d6bd}Creeks{/color}? Didn’t she get squashed by a troll club years ago?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "erastos" or search == "erastes" or search == "erostes" or search == "erastas" or search == "cassia" or search == "casia" or search == "cassio" or search == "casio" or search == "erastosandcassia" or search == "cassiaanderastos":
        if quest_recruitahunter == 2:
            menu:
                '“I’ve heard it’s {i}you{/i} who should be asked about them.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            $ quest_recruitahunter_spokento_iason = 1
            menu:
                '“{color=#f6d6bd}Dalit{/color} told me she’d like to learn more about {color=#f6d6bd}Erastos{/color} and {color=#f6d6bd}Cassia{/color}, true, but I don’t know much about either. The locals don’t enjoy badmouthing their neighbors in front of strangers. May be easier to ask someone from the outside.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "orentius" or search == "orientus" or search == "theprophet" or search == "prophet" or search == "thepriestofwhitemarshes" or search == "priestofwhitemarshes" or search == "priestwhitemarshes" or search == "priestfromwhitemarshes" or search == "theprophetofwhitemarshes" or search == "prophetofwhitemarshes" or search == "prophetwhitemarshes" or search == "prophetfromwhitemarshes":
        if iason_about_whitemarshes_destroyed:
            menu:
                'He crosses his arms. “Let the dead fade in peace.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            if not description_orentius00:
                $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright."
            $ description_orentius01 = "I heard that he won’t meet with people who are not trusted in his fellowship."
            $ description_orentius03 = "he’s “greater in thought than he is in heart.”"
            menu:
                'He avoids your eyes, thinking about the answer for a good few breaths. “I shouldn’t talk about {color=#f6d6bd}Orentius{/color}, and you won’t have a chance to meet with him anyway. Ever since he leads {color=#f6d6bd}White Marshes{/color}, only the trusted allies of the village can hear his teachings.”
                \n\nHe lets out a quiet grunt, almost a chuckle. “I’m not sure how he got so {i}beloved{/i} in the first place. He’s greater in thought than he is in heart. Not a {i}people person{/i}, you know.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "helvius" or search == "helvus" or search == "themayorofwhitemarshes" or search == "mayorofwhitemarshes" or search == "mayorwhitemarshes" or search == "mayorfromwhitemarshes":
        if iason_about_whitemarshes_destroyed:
            menu:
                'He crosses his arms. “Let the dead fade in peace.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            $ description_whitemarshes_helvius01 = "The mayor of the village is known as {color=#f6d6bd}Helvius{/color}."
            $ description_whitemarshes_helvius02 = "“like all brutes, he understands only strength, and hates those who challenge him.”"
            menu:
                '“That angry kid? I had to meet him, true. He’s a {i}mayor{/i} only in name, with loyalty greater than talent. Like all brutes, {color=#f6d6bd}Helvius{/color} understands only strength, and hates those who challenge him.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "thyrsus" or search == "warlock" or search == "peatwarden" or search == "mayorofwhitemarshes" or search == "mayorwhitemarshes" or search == "mayorfromwhitemarshes":
        if iason_about_whitemarshes_destroyed:
            menu:
                'He crosses his arms. “Let the dead fade in peace.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            $ description_thyrsus04 = "He was taught his unusual magic by the druids of {color=#f6d6bd}Howler’s Dell{/color}."
            $ description_thyrsus05 = "He seems to be bothered by the undead of {color=#f6d6bd}White Marshes{/color}."
            $ description_thyrsus06 = "He got into an argument with his tribe over the security of his family."
            menu:
                '“The peat mage taught by druids of {color=#f6d6bd}Howler’s{/color}? He may be a loon, but knows enough about herbs to help with some gentler ills. I haven’t spoken with him myself, he never leaves the bogs, especially since he moved away from the walls of {color=#f6d6bd}White Marshes{/color}.”
                \n\nYou ask why he lives by himself, but the innkeep scratches his ear. “He got into some argument with the priest? Some death in the family, I think, and he refused to put the others at risk. I don’t know, it sounds {i}personal{/i}.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "phoibe" or search == "pheibe" or search == "phoeibe" or search == "photiosgirl" or search == "photioslas" or search == "photiosdaughter" or search == "photiossgirl" or search == "photiosslas" or search == "photiossdaughter":
        menu:
            '“{color=#f6d6bd}Photios’{/color} girl? I don’t know a thing about her. She’s still a kid.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "photios" or search == "galerocksfisher" or search == "galerockfisher":
        menu:
            '“A seafolk from {color=#f6d6bd}Gale Rocks{/color}, correct? He was here with the fish trading crew, but didn’t do much of the talking. Had a wife once, but apes got to her on the road. She saved their little girl, though.”
            \n\nHe rubs down a stain on a wooden bowl. “Back then he was a kind man, if a quiet one. I’ve heard he’s changed a lot since. {color=#f6d6bd}Asterion{/color} mentioned he was doing some work for him, but every sage or shaman told him to abandon it, even {color=#f6d6bd}Thyrsus{/color} of {color=#f6d6bd}White Marshes{/color}.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "theprelate" or search == "prelate" or search == "prisca" or search == "monasteryleader" or search == "themonasteryleader":
        if iason_about_prelate:
            menu:
                '“You know more about them than I do. I now wonder if it’s better to keep all you’ve told me between the two of us, or ask the monks directly. Maybe they’ll deny everything, but maybe it’s a chance to get a foot in the door.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            menu:
                '“Does the monastery even have a prelate? I thought {color=#f6d6bd}Aeli{/color} is the one who speaks for the monks.”
                '
                '“He does, but I met the actual prelate. Quite the character.”' if monastery_cave_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He does, but I met the actual prelate. Quite the character.”')
                    if not iason_shop_crossbow_bought and not item_crossbow:
                        $ iason_shop_crossbow_price -= 2
                    elif not iason_shop_shield_bought and iason_shop_shield_price:
                        $ iason_shop_shield_price -= 1
                    $ iason_friendship += 1
                    $ iason_about_prelate = 1
                    $ minutes += 5
                    menu:
                        'During your story, he’s unconvinced, but he listens to you with curious eyes. “If that’s a lie, I must say, it’s an elaborate one.” He looks at the ceiling. “I wonder why they care so much about staying hidden. I doubt there’s that many assassins in the North.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "tertia" or search == "darkeyedwomanfromoldpagos" or search == "darkskinnedwomanfromoldpagos" or search == "darkeyedwomanfromoldpágos" or search == "darkskinned womanfromoldpágos":
        $ description_tertia01 = "According to"
        $ iason_about_tertia = 1
        menu:
            '“Right, {color=#f6d6bd}Tertia{/color}... Have you seen her with a spear? She’s a natural, and still young. It’s those eyes of a hunter that she’s got, I know a bit about that.” He blinks a few times. “She was meant to enter the monastery as an armed monk, like the temple wardens of The United Church, but something happened, who knows. Still has a stick up her ass, praying and scolding the {i}sinners{/i},” he chuckles, “but she’s a kind gal. Maybe {color=#f6d6bd}Aeli{/color} had something against her.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "thais" or search == "howlerdellmayor" or search == "howlersdellmayor" or search == "howlersdellmayor" or search == "mayorofhowlersdell" or search == "mayorofhowlers" or search == "themayorofhowlersdell" or search == "themayorofhowlers":
        $ description_thais04 = " doesn’t like her and admits that “she may be frivolous, but isn’t stupid.” According to him, she was born into wealth."
        menu:
            '“Eh. People say she’s a good mayor, but she’s rich from birth, so also careless. She doesn’t know the struggle, the hunger and dirt, so fancies her clothes more than one should. She thinks she keeps her village safe, even though it’s the druids who do all the work.”
            \n\nHe looks down, but finally speaks again. “She may be frivolous, but isn’t stupid. If you’re smart, better keep your eyes open.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "quintus" or search == "the gatekeeper" or search == "gatekeeper":
        $ quintus_friendswithdalit = 1
        $ description_quintus02 = "According to"
        $ description_howlersdell08a = " I’ve heard in {color=#f6d6bd}Pelt{/color} that their prices are “absurd”."
        $ description_whitemarshes09 = "I’ve heard in {color=#f6d6bd}Pelt{/color} that “their Order doesn’t look kindly on hard drinks. They say it {i}clouds one’s judgment{/i}.”"
        if quintus_pelt_firsttime and not quintus_pelt_left:
            $ custom1 = "Well, you can just speak with him, there?"
        else:
            $ custom1 = "{color=#f6d6bd}Quintus{/color} the gatekeeper?"
        menu:
            '“[custom1] One of our best and only clients. Can chug more mugs of ale than there are ideas in his head.” He smiles gently. “But he’s brave, that one. Has even trained with my team, practiced how to skin a large ape and how to find food in the woods. Too compliant to be a hunter, but could be a fine soldier.”
            \n\nHe points toward the wooden mugs. “In {color=#f6d6bd}White Marshes{/color} they doen’t look kindly on hard drinks, imagine that. They say it {i}clouds one’s judgment{/i}. And {color=#f6d6bd}Ape Ale’s{/color} prices are absurd, who knows why. Discord keeps people away from {color=#f6d6bd}Howler’s{/color}, but if they end up here, it’s only better for me.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "efren" or search == "effren" or search == "efrren":
        $ elah_efren_siblings = 1
        $ description_elah_efren06 = "{color=#f6d6bd}Efren{/color} is more of a pathfinder than a fighter, and was invited to stay at {color=#f6d6bd}Pelt of the North{/color} as a ranger."
        menu:
            '“When the people of {color=#f6d6bd}Creeks{/color} send a trading band to us, it’s with {color=#f6d6bd}Efren{/color} in the front. He’s not so much of a fighter as he is a pathfinder, but he’s killed enough beasts that I invited him to be our ranger, too bad he loves his home too much,” he says with the tone of someone who describes a completely alien experience. “Unlike his brother, {color=#f6d6bd}Elah{/color}, he’s a man of action, not of layered schemes.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "younghava" or search == "younghavva":
        menu:
            '“From {color=#f6d6bd}Creeks{/color}? Didn’t she die long time ago?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "valens" or search == "valenss" or search == "valen" or search == "walens" or search == "walenss" or search == "walen":
        $ iason_about_valens = 1
        if quest_readtheletter and item_letterwhitemarshes_read:
            $ renpy.notify("Journal updated: Read the Letter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Read the Letter{/i}')
        menu:
            '“{color=#f6d6bd}Valens{/color} is the farmer from {color=#f6d6bd}White Marshes{/color}? I had a job for his husband, what’s his face? No matter, he failed. Joined my crew on the trip for pelts, returned with no eye and no left arm. Taught me a lesson about hiring mercenaries. Anyway, he then paid us for delivering a letter to this... {color=#f6d6bd}Valens{/color}, you said?, and left south. Told me he won’t be another burden for his tribe.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "admon" or search == "dalia" or search == "daliya" or search == "vaschel" or search == "vashel" or search == "vachel" or search == "missinghunters" or search == "missinghunter" or search == "missinghunters":
        if iason_about_missinghunters:
            menu:
                '“You know more about them than I do.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            menu:
                '“Let me think... Some friend of {color=#f6d6bd}Efren’s{/color} from {color=#f6d6bd}Creeks{/color}?”
                '
                '“Three hunters, {color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Dalia{/color}, and {color=#f6d6bd}Vaschel{/color}. They’re missing.”' if quest_missinghunters == 1:
                    $ iason_about_missinghunters = 1
                    $ iason_friendship += 1
                    menu:
                        '“All three of them? That’s bad news for us. I’m quite glad knowing there’s pressure in the North, and that beasts are being pushed toward our forests. Thanks to you, we may adjust our plans for spring.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                '“Three hunters, {color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Dalia{/color}, and {color=#f6d6bd}Vaschel{/color}. They recently died.”' if quest_missinghunters == 2:
                    $ iason_about_missinghunters = 1
                    $ iason_friendship += 1
                    menu:
                        '“All three of them? That must be a big hit to the village. It’s bad news for us as well. Though I am quite glad to know there’s pressure in the North, and that beasts were being pushed toward our forests. Thanks to you, we may adjust our plans for spring.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                'I don’t know enough about them. (disabled)' if quest_missinghunters == 0 or quest_missinghunters == 3:
                    pass
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "aquila" or search == "aquilla" or search == "galerocksbathman" or search == "aguila" or search == "aguilla":
        menu:
            '“I know not of such a man, but I heard that their river is too wild for them to use. There were some deaths of bathing kids, drunken elders, or tired washpeople. No surprise that they’d rather use tubs and buckets.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "albus" or search == "galerocksalter" or search == "galerockssalter":
        menu:
            '“The white-skinned man, am I right?” After you confirm that’s the one, he asks you for a moment to think. “He’s visiting us with {color=#f6d6bd}Gale Rocks’{/color} caravan, knows his trade better than anyone in the city, and can talk about his salt as if it’s sugar. He always gets here wearing a heavy cloak, no matter the weather, and works under the roof to avoid direct sunlight, but he’s a cheerful fellow. No gloom in his soul.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "domitia" or search == "domita" or search == "galerockscooper" or search == "galerockcooper" or search == "galerockscarpenter" or search == "galerockcarpenter":
        menu:
            '“I’ve heard there was some accident and that {color=#f6d6bd}Gale Rocks{/color} has a new head cooper now, but I don’t know her at all.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "severina" or search == "sewerina" or search == "galerocksheadwoman" or search == "galerocksmayor" or search == "galerockheadwoman" or search == "galerockmayor" or search == "galerockschief" or search == "galerockchief":
        $ iason_about_severina = 1
        menu:
            '“Remember to call her {color=#f6d6bd}the headwoman{/color} whenever you address her. The villagers are mad at any {i}outsider{/i} who gives her another title, go figure,” he shrugs, “or comes to her without showing {i}respect{/i}. You know, smelly, drunk.” He observes you for a moment, and suddenly smiles. “Treat her as if she’s a city official. Be brief, don’t ask for favors, don’t threaten. Say what you have to, don’t argue for long.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "porcia" or search == "portia" or search == "galerockscook" or search == "galerockcook":
        menu:
            '“Well, her job ain’t so different from mine,” he grunts with a smile, “but I’ve heard her group cooks for the {i}entire{/i} village. No wonder she never came here to trade or anything.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "galerocksgateguard" or search == "galerocksguard" or search == "galerockgateguard" or search == "galerockguard":
        menu:
            '“I think I’ve heard of him. That job is his reward. I mean, how many travelers does he have to meet each year?” He spares you a slight smile. “He got it after he saved {color=#f6d6bd}the headwoman’s{/color} life, risking his own.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "tatius" or search == "tacius" or search == "galerocksarmorer" or search == "galerockarmorer":
        menu:
            '“Correct me if I’m wrong... He’s teaching the youth and looking after the armory?” You nod, but the innkeep struggles to describe him after that. “That side of their village is a bit of a mystery to me. They don’t work much on weapons and armors, rather buy some fine equipment. But it’s not like in some villages, where fighters are free of exhausting labor. They all train and fight, and only a few of them guard the village at all times, but that’s a reward for their brave deeds, rather than a trade. I think {color=#f6d6bd}Tatius{/color} has no such tales to share, but was recognized as the best fighter in the village, and a talented instructor.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "rufina" or search == "galerocktailor" or search == "galerockstailor":
        menu:
            '“I ain’t even sure she can be called a {i}tailor{/i}, more like a... patcher. Seafolk have a different shape,” he raises and rubs his arm, pretending to stretch it. “So most pieces of clothing don’t fit them, unless they make them on their own. But you’ve seen their days, they work hard and all day long, they don’t doll up often. So they buy any piece of clothing they can, and {color=#f6d6bd}Rufina{/color} sews them all together into something new.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "fulvia" or search == "fulva" or search == "galerocksroomkeeper" or search == "galerockroomkeeper" or search == "galerocksroomkeep" or search == "galerockroomkeep":
        $ galerocks_fulvia_secret_knowsabout = 1
        $ shortcut_pcknowsabout = 1
        menu:
            '“Give me a moment,” he puts a hand on his dark forehead, looking at the ceiling as he thinks. “You know, I’ve heard of her, but only once, and around ten years ago, when the first group from {color=#f6d6bd}Gale Rocks{/color} paid us a visit. They were telling us about the road leading through the heart of the woods, and mentioned that {i}only her{/i}, that’s right, {i}only{/i}, was good enough to get safely through it, even during nights. Yet The Wright took away her pride, together with her eyes.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "petronius" or search == "patronius" or search == "petronus" or search == "patronus" or search == "galerocksgossip" or search == "galerocksgossiper" or search == "galerockgossip" or search == "galerockgossiper":
        menu:
            'He looks at the window, frowning. When he answers, he speaks slowly. “And you say he’s an adult from {color=#f6d6bd}Gale Rocks{/color}? I’ve never heard of him.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "iuno" or search == "juno" or search == "galerocksbuilder" or search == "galerocksdigger" or search == "galerockbuilder" or search == "galerockdigger":
        menu:
            '“{color=#f6d6bd}Iuno{/color} is too old to travel, but her people mention her whenever they speak of something they plan to construct. They told me her hand moved every rock and building log that’s in their village, and even hollowed one of the caves.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "florus" or search == "florius" or search == "galerocksfletcher" or search == "galerockfletcher" or search == "galerocksarrowmaker" or search == "galerockarrowmaker":
        menu:
            '“We tried to get some arrows from {color=#f6d6bd}Helvios{/color}, but that ain’t something his headwoman will depart with cheaply. He makes so many of them that every spring the hunters take a few filled quivers and just shoot at any harpy they can find between the rocks, as if they are some crop-digging boars.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "glauciaparents" or search == "glauciafamily" or search == "glauciamother" or search == "glauciamom" or search == "glauciafather" or search == "glauciadad" or search == "vitaandvalerius" or search == "vitavalerius" or search == "glauciasibling" or search == "glauciasiblings" or search == "glauciasparents" or search == "glauciasfamily" or search == "glauciasmother" or search == "glauciasmom" or search == "glauciasfather" or search == "glauciasdad" or search == "vita" or search == "valerius" or search == "glauciassibling" or search == "glauciassiblings" or search == "glauciasancestors" or search == "glauciaancestors":
        $ description_glaucia02 = "I heard that she was raised by her family in the village of {color=#f6d6bd}Gale Rocks{/color}."
        menu:
            '“Oh, you can tell by her accent. “{color=#f6d6bd}Glaucia’s family{/color} comes from {color=#f6d6bd}Gale Rocks{/color}, though I think there isn’t much of it left.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "marina" or search == "maryna":
        menu:
            '“I only know of the time when she and her family were looking for this priest, her partner, I think? He was foraging around {color=#f6d6bd}Gale Rocks{/color}, left his group for a few minutes. Left {color=#f6d6bd}Marina{/color} pregnant and alone, but that ain’t so bad at their village. She would struggle in the city, but here her people care for them both.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "paulus" or search == "pavlus" or search == "pavlvs":
        menu:
            '“That’s some kid from {color=#f6d6bd}Gale Rocks{/color}, I think? He hasn’t been here yet.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "timo" or search == "teemo":
        if not iason_about_timo:
            menu:
                '“I met her at {color=#f6d6bd}Howler’s{/color} a few years back, she was close to her adulthood. She seemed strong... I wonder if she can fight.”
                '
                '“I doubt it. She’s a washwoman now, and hoping to marry soon.”' if howlersdell_timo_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I doubt it. She’s a washwoman now, and hoping to marry soon.”')
                    $ iason_friendship += 1
                    $ iason_about_timo = 1
                    menu:
                        '“Pity. Thank you for saving me some time.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump peltnorthrumors02
                        '“Let’s change the topic.”':
                            jump peltnorthregularquestionsv04
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            menu:
                '“I haven’t been in {color=#f6d6bd}Howler’s{/color} recently. Maybe in fall.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "shoshi" or search == "shosi" or search == "shoshanna" or search == "shoshana" or search == "shoshinna" or search == "shoshina":
        $ shoshi_namebig = "{color=#f6d6bd}Shoshi{/color}"
        $ shoshi_namesmall = "{color=#f6d6bd}Shoshi{/color}"
        if quest_recruitahunter_spokento_shoshi_recruited:
            menu:
                '“Sounds like I judged her well when she was here a few years back, with those strong arms of her,” he lets out a satisfied grunt. “I hope {color=#f6d6bd}Dalit{/color} will find some wits in her, too.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
        else:
            menu:
                '“That singing woodcutter? Last she was here I was hoping she’d agree to work for us, but we have no use for someone who ain’t going to fight. Shame, with those strong arms of her. Weird that she haven’t left {color=#f6d6bd}Creeks{/color} yet. A calm place, like {color=#f6d6bd}Gale Rocks{/color}, would fit her.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "thetribeofthegreenmountain" or search == "tribeofthegreenmountain" or search == "thetribeofgreenmountain" or search == "tribeofgreenmountain" or search == "tribeofgreenmountain" or search == "tribegreenmountain" or search == "thegreenmountaintribe" or search == "greenmountaintribe" or search == "greenmountainpeople" or search == "hiddenvillage" or search == "hiddentribe" or search == "greenmountain" or search == "hiddenpagans" or search == "thetribeofthegreenmountain" or search == "thetribethegreenmountain" or search == "thetribegreenmountain" or search == "thetribeofthegreenmountains" or search == "thetribethegreenmountains" or search == "thetribegreenmountains":
        if iason_about_greenmountaintribe:
            jump peltnorthiasonaboutgreenmountaintribe2
        $ quest_reachthepaganvillage_description01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
        $ description_greenmountaintribe01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
        $ description_greenmountaintribe02 = "I heard that the brook leading to this village is dangerous, filled with flesh-eating fish."
        if not quest_reachthepaganvillage or quest_reachthepaganvillage == 1:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("New entry: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
        menu:
            'When he frowns, his words are quick and frustrated. “And how do you know about {color=#f6d6bd}The Green Mountain Tribe{/color}? Did you walk into them in a tavern?” He shrugs before you respond. “They’re loners, and I don’t send them any troubles. I’ve heard there’s a brook in the East that leads to their place, but it’s full of rockbites.” Seeing your look, he carries on. “Red-and-gray fish, larger than my hand.” He reaches in your direction with his pink, open palm. “They eat flesh. So... Stay away from the water, is what I’m saying.”
            '
            'I tell him about the things I saw there.' if cephasgaiane_available and not iason_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him about the things I saw there.')
                jump peltnorthiasonaboutgreenmountaintribe1
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    elif search == "gaiane" or search == "gaiana" or search == "cephas" or search == "cefas":
        if iason_about_greenmountaintribe:
            label peltnorthiasonaboutgreenmountaintribe2:
                menu:
                    '“Why do you ask me about? You know {color=#f6d6bd}The Tribe{/color} better than anyone on this side of {color=#f6d6bd}Hag Hills{/color}.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump peltnorthrumors02
                    '“Let’s change the topic.”':
                        jump peltnorthregularquestionsv04
        else:
            menu:
                '“These names are from the Old Speech, aren’t they? They sound like they’re from {color=#f6d6bd}Howler’s Dell{/color}.”
                '
                'I tell him about the leaders of {color=#f6d6bd}The Green Mountain Tribe{/color}.' if cephasgaiane_available and not iason_about_greenmountaintribe:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him about the leaders of {color=#f6d6bd}The Green Mountain Tribe{/color}.')
                    label peltnorthiasonaboutgreenmountaintribe1:
                        $ iason_about_greenmountaintribe = 1
                        $ iason_friendship += 1
                        $ quarters += 1
                        menu:
                            'He’s listening to your story patiently, and at occasion even stares in your eyes, as if he’s trying to spot a lie.
                            \n\n“I must say, you’ve been to some unusual places,” he responds after a longer pause. “I’ll keep what you told me to myself, but at least now I know I {i}could{/i} get to meet them, with a gift at hand...” He glances at the casks beneath the stairs, lost in his thoughts. “Though it may be easier to get through the young shaman, than that {i}chief{/i}.”
                            '
                            '“How about...”':
                                python:
                                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                    search = search.strip().lower().replace(" ", "")
                                    if not search:
                                        search = "no one"
                                jump peltnorthrumors02
                            '“Let’s change the topic.”':
                                jump peltnorthregularquestionsv04
                '“How about...”':
                    python:
                        search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump peltnorthrumors02
                '“Let’s change the topic.”':
                    jump peltnorthregularquestionsv04
    elif search == "thesaurianrider" or search == "asaurianrider" or search == "saurianrider" or search == "thelizardrider" or search == "alizardrider" or search == "lizardrider":
        if iason_about_greenmountaintribe:
            jump peltnorthiasonaboutgreenmountaintribe2
        menu:
            '“Who do you mean by that? {color=#f6d6bd}Asterion{/color}?”
            '
            'I tell him about the things I saw in {color=#f6d6bd}The Green Mountain Tribe{/color}.' if cephasgaiane_available and not iason_about_greenmountaintribe:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him about the things I saw in {color=#f6d6bd}The Green Mountain Tribe{/color}.')
                jump peltnorthiasonaboutgreenmountaintribe1
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04
    # elif search == "" or search == "" or search == "":
    #     menu:
    #         '“{color=#f6d6bd}{/color} {color=#f6d6bd}Gale Rocks{/color}”
    #         '
    #         '“How about...”':
    #             python:
    #                 search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                 search = search.strip().lower().replace(" ", "")
    #                 if not search:
    #                     search = "no one"
    #             jump peltnorthrumors02
    #         '“Let’s change the topic.”':
    #             jump peltnorthregularquestionsv04
    else:
        menu:
            '“I don’t know them.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Who are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump peltnorthrumors02
            '“Let’s change the topic.”':
                jump peltnorthregularquestionsv04

###########################

label peltnorthquest_orentius_thais_description01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a message from {color=#f6d6bd}Thais{/color}. It’s about {color=#f6d6bd}Orentius{/color}.”')
    $ questionpreset = "iason1"
    $ can_rest = 1
    $ can_items = 1
    $ quest_orentius_thais_description03a01 = "The hunters from {color=#f6d6bd}Pelt of the North{/color} are going to support {color=#f6d6bd}Thais’{/color} cause."
    $ renpy.notify("Journal updated: Orentius, the Necromancer")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
    $ quarters += 1
    if iason_stance == "sittingattable":
        $ custom1 = "moves in his chair an clears his throat, then stands up, fills up two mugs behind the counter, and returns to you"
    else:
        $ custom1 = "gestures for you to sit at the table. He walks behind the counter, fills up two mugs, and sits down with you"
    menu:
        'You explain the matter, and when you mention necromancy, the innkeep [custom1]. The beer he offers you is full of hops, yellow, thick, and cloudy. The smell alone makes you think of sweet and sour fruits from the distant South.
        \n\nThe man has plenty of questions and doubts. You describe {color=#f6d6bd}White Marshes{/color} and its deeds, the undead, {color=#f6d6bd}Orentius’{/color} leadership, {color=#f6d6bd}Thais’{/color} plans. It goes on for quite a while, with you doing most of the talking. In the meantime, a couple of hunters gather in the room, and listen to your conversation in silence, keenly observing you. Your thoughts run toward your axe.
        \n\nOnce {color=#f6d6bd}[iason_name]{/color} is done with his questions, he spends a good minute observing the contents of his mug. “Fine,” his eyes steadily observe his mug. “A couple of us will arrive at {color=#f6d6bd}Howler’s{/color} soon. They’ll join you when you move on the {color=#f6d6bd}Marshes{/color}.” He nods to his companions and asks you if there’s anything else.
        '
        '(iason1 preset)':
            pass

label peltnorthaboutnomoreundeadALL:
    label peltnorthaboutnomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead of {color=#f6d6bd}White Marshes{/color} are gone, and the village suffered no losses. I thought you should know.”')
        $ iason_about_nomoreundead = 1
        $ iason_friendship += 1
        $ minutes += 5
        $ questionpreset = "iason1"
        menu:
            '“Thanks,” he says slowly. “But what happened, exactly?”
            \n\nYour story isn’t long, though the innkeep also asks you about {color=#f6d6bd}Helvius{/color} and {color=#f6d6bd}Thyrsus{/color}. “So that’s how it is. Well, Nice job,” he gives you an encouraging nod. “Though I doubt {color=#f6d6bd}Orentius{/color} will keep his word. I hope I’m wrong.”
            '
            '(iason1 set)':
                pass

    label peltnorthaboutnomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead of {color=#f6d6bd}White Marshes{/color} are gone, but I don’t think the village will take any traders in the near future. I thought you should know.”')
        $ iason_about_nomoreundead = 1
        $ iason_friendship += 2
        $ minutes += 5
        $ questionpreset = "iason1"
        menu:
            '“Thanks,” he says slowly. “But what happened, exactly?”
            \n\nYour story isn’t long, though the innkeep also asks you about {color=#f6d6bd}Helvius{/color} and {color=#f6d6bd}Thyrsus{/color}. “So that’s how it is. Well, great job,” his smile disappears as quickly as it showed up. “Having {color=#f6d6bd}Orentius{/color} away from the village means we don’t have to worry about him. Just the way I like it.”
            '
            '(iason1 set)':
                pass

    label peltnorthaboutnomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The undead of {color=#f6d6bd}White Marshes{/color} may soon leave the bogs, and there’s no one there to control them. I recommend avoiding these territories.”')
        $ iason_about_nomoreundead = 1
        $ iason_friendship += 1
        $ minutes += 5
        $ questionpreset = "iason1"
        menu:
            '“Explains the smoke we saw from our tower,” he looks at your ear, frowning slightly. “What happened?”
            \n\nYour story isn’t long, though the innkeep asks you about a few of the now-gone souls - {color=#f6d6bd}Helvius{/color}, {color=#f6d6bd}Thyrsus{/color}, and especially - {color=#f6d6bd}Orentius{/color}. “Shame to see all of them gone, but you did a nice job,” he gives you an encouraging nod. “Having fewer people to trade with and more monsters against us will give us a rough couple of years, but it’s better than fighting off a power-hungry necromancer.”
            '
            '(iason1 set)':
                pass

label peltnorthfoggymessage01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Foggy{/color} has a message for you.”')
    $ quest_foggy2iason_description01 = "{color=#f6d6bd}Iason{/color} is unable to keep his side of the bargain, but wants me to lie in his name. It seems to me like he made a decision a long time ago."
    menu:
        'The innkeeper listens to {color=#f6d6bd}Foggy’s{/color} words patiently, then crosses his arms and leans back, lost in his thoughts. “Seems like she won’t be played so easily.”
        \n\nAfter you mention the answer, he tells you to relax. “You’ll have it soon. See, I’ve lost her first share. {color=#f6d6bd}Asterion{/color} was meant to deliver it to her, never happened. I don’t want to waste more. But {i}she{/i} doesn’t need to know it.” He raises a bowl that sits nearby and reveals a few dragon bones. He counts off five of them. “Tell her this. {i}Asterion lost your coin, I’m now in debt. Let’s be partners for now, I’ll send you more once I have it. But I don’t {i}promise{/i} anything.{/i}”
        \n\nHe pushes the coins toward you, observing them like a hawk. “They are yours, just help me keep the charade going, now and later. It’s important to me.”
        '
        '“Why even bother?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why even bother?”')
            menu:
                'He makes a nervous hiss as he breathes through his teeth. “I plan to sell furs to her in the late autumn, and I hope she’ll keep sending people here whenever they stop at her place. I want to stay on her good side, you see. She doesn’t get {i}hurt{/i} in any way, bah, I’ll spread a good word about her if it comes to it, until I head back home. And if the winds change and the cityfolk start trading here once the roads get safer,” he meets your eyes, “I may return to our deal.”
                '
                'I take the coins. “I’ll cover for you.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the coins. “I’ll cover for you.”')
                    $ iason_friendship += 2
                    $ coins += 5
                    $ iason_friendship_moneybonus_points += 5
                    $ quest_foggy2iason_description02 = "I told {color=#f6d6bd}Iason{/color} I’ll fulfill his wish."
                    $ questionpreset = "iason1"
                    $ can_rest = 1
                    show screen notifyimage( "Journal updated: Check on Iason.\n+5", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason. +5 {image=cointest}{/i}')
                    menu:
                        'He smiles gently. “Good. Good.”
                        '
                        '(iason1 preset)':
                            pass
                '(lie) I take the coins. “Fine.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I take the coins. “Fine.”')
                    $ iason_friendship += 2
                    $ coins += 5
                    $ iason_friendship_moneybonus_points += 2
                    $ quest_foggy2iason_description02a = "I lied to {color=#f6d6bd}Iason{/color} that I’d fulfill his wish."
                    $ pc_lies += 1
                    $ questionpreset = "iason1"
                    $ can_rest = 1
                    $ can_items = 1
                    show screen notifyimage( "Journal updated: Check on Iason.\n+5", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason. +5 {image=cointest}{/i}')
                    menu:
                        'He smiles gently. “Good. Good.”
                        '
                        '(iason1 preset)':
                            pass
                '“I won’t lie to her.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t lie to her.”')
                    $ iason_friendship -= 2
                    $ questionpreset = "iason1"
                    $ can_rest = 1
                    $ can_items = 1
                    $ renpy.notify("Journal updated: Check on Iason")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason{/i}')
                    menu:
                        'He grabs the coins. “As you wish. But don’t expect you’ll be rewarded by her.”
                        '
                        '(iason1 preset)':
                            pass
        'I take the coins. “I’ll cover for you.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the coins. “I’ll cover for you.”')
            $ iason_friendship += 2
            $ coins += 5
            $ iason_friendship_moneybonus_points += 5
            $ quest_foggy2iason_description02 = "I told {color=#f6d6bd}Iason{/color} I’ll fulfill his wish."
            $ questionpreset = "iason1"
            $ can_rest = 1
            $ can_items = 1
            show screen notifyimage( "Journal updated: Check on Iason.\n+5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason. +5 {image=cointest}{/i}')
            menu:
                'He smiles gently. “Good. Good.”
                '
                '(iason1 preset)':
                    pass
        '(lie) I take the coins. “Fine.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I take the coins. “Fine.”')
            $ iason_friendship += 2
            $ coins += 5
            $ iason_friendship_moneybonus_points += 2
            $ quest_foggy2iason_description02a = "I lied to {color=#f6d6bd}Iason{/color} that I’d fulfill his wish."
            $ pc_lies += 1
            $ questionpreset = "iason1"
            $ can_rest = 1
            $ can_items = 1
            show screen notifyimage( "Journal updated: Check on Iason. +5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason. +5 {image=cointest}{/i}')
            menu:
                'He smiles gently. “Good. Good.”
                '
                '(iason1 preset)':
                    pass
        '“I won’t lie to her.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t lie to her.”')
            $ iason_friendship -= 2
            $ questionpreset = "iason1"
            $ can_rest = 1
            $ can_items = 1
            $ renpy.notify("Journal updated: Check on Iason")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Check on Iason{/i}')
            menu:
                'He grabs the coins. “As you wish. But don’t expect you’ll be rewarded by her.”
                '
                '(iason1 preset)':
                    pass

label iason_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about {color=#f6d6bd}High Island{/color}?”')
    $ can_rest = 1
    $ can_items = 1
    $ iason_about_highisland = 1
    $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
    $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
    $ questionpreset = "iason1"
    menu:
        '“Hm? I’ve heard this name somewhere, let me think,” he looks around, then picks up a mug and tilts it to peek inside. “Oh, right. It’s the savage wilds around the volcano? I asked the locals what’s with the smoke that can be seen from time to time, but they don’t know much about the place either. I’d ask some sailors if I were you.
        '
        '(iason1 set)':
            pass

label peltnorthquestionssteephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk. You and your group arrived to the peninsula not long before the village in the west was ruined.”')
    $ iason_about_steephouse_gray = 1
    if iason_stance == "sittingatstove":
        $ custom1 = "He reaches for a poker and stokes the fire, avoiding your eyes. His fingers go pale from clutching."
    elif iason_stance == "behindcounter":
        $ custom1 = "He glances at your weapon, then turns away from you, moving a few jars on the shelf, but without achieving anything specific."
    elif iason_stance == "sweeping":
        $ custom1 = "The motions he makes slow down slightly as he glances toward your weapon."
    elif iason_stance == "sittingattable":
        $ custom1 = "His eyes run to the entrance, then to your weapon. His fingers alternately spread and make fists, as if he’s warming them up."
    menu:
        '[custom1] “No, I don’t think so. I may be in need of a roadwarden’s services, but not of their nosiness.”
        \n\n“I’m not dropping it so easily,” you start, and the man lets out an unusually loud chuckle. You notice movement at the entrance, and the man’s gestures suddenly get more confident.
        \n\n“Is that so? So why can’t you figure out what happened to that place by yourself?”
        '
        '“It was raided by humans.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was raided by humans.”')
            jump peltnorthquestionssteephouse01fail
        '“It was destroyed during the wrath of the herds.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was destroyed during the wrath of the herds.”')
            jump peltnorthquestionssteephouse01fail
        '“It was pillaged by humans, then destroyed by monsters.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was pillaged by humans, then destroyed by monsters.”')
            $ iason_about_steephouse_price_base -= 10
            $ iason_about_steephouse_price = iason_about_steephouse_price_base
            $ iason_about_steephouse_price -= (appearance_price*2)
            $ iason_about_steephouse_price -= ((iason_friendship+dalit_friendship)/3)
            if iason_about_steephouse_price < 10:
                $ iason_about_steephouse_price = 10
            menu:
                'He makes an annoyed click with his tongue. “That’s one way to put it,” he takes a deep breath, getting even larger. “Fine, I’ll give you that. But I’ve no interest in changing things as they are, and helping you now may cut a branch on which I sit.”
                \n\nYou ask him what he wants in return, and he runs his fingers through his blueish hair. “Oh, nothing fancy. Just pay me.” He sizes you up. “Considering everything, how about... [iason_about_steephouse_price] coins.”
                '
                'I sigh and reach for my pouch.' if coins >= iason_about_steephouse_price:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it.”')
                    jump peltnorthquestionssteephouse02
                'I don’t have enough. (disabled)' if coins < iason_about_steephouse_price:
                    pass
                '“That’s too much.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s too much.”')
                    $ questionpreset = "iason1"
                    $ can_rest = 1
                    $ can_items = 1
                    menu:
                        '“Let’s agree to disagree.”
                        '
                        '(iason1 preset)':
                            pass
        '“It was attacked by beasts, then finished off by humans.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was attacked by beasts, then finished off by humans.”')
            jump peltnorthquestionssteephouse01fail
        '“Humans used monsters to destroy it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Humans used monsters to destroy it.”')
            jump peltnorthquestionssteephouse01fail

    label peltnorthquestionssteephouse01fail:
        $ iason_about_steephouse_price = iason_about_steephouse_price_base
        $ iason_about_steephouse_price -= (appearance_price*2)
        $ iason_about_steephouse_price -= ((iason_friendship+dalit_friendship)/3)
        if iason_about_steephouse_price < 10:
            $ iason_about_steephouse_price = 10
        menu:
            'He scoffs. “So not only do you {i}not{/i} know, you want me to do your entire job, and cut a branch on which I sit? I’ve no interest in changing things as they are, thank you very much.”
            \n\nYou ask him what he wants in return, and he runs his fingers through his blueish hair. “Oh, nothing fancy. Just pay me.” He sizes you up. “Considering everything, how about... [iason_about_steephouse_price] coins.”
            '
            'I sigh and reach for my pouch.' if coins >= iason_about_steephouse_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it.”')
                jump peltnorthquestionssteephouse02
            'I don’t have enough. (disabled)' if coins < iason_about_steephouse_price:
                pass
            '“That’s too much.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s too much.”')
                $ questionpreset = "iason1"
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“Let’s agree to disagree.”
                    '
                    '(iason1 preset)':
                        pass

    label peltnorthaboutruinedvillage01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn what happened to the ruined village. Let’s talk the price.”')
        $ iason_about_steephouse_price = iason_about_steephouse_price_base
        $ iason_about_steephouse_price += (appearance_price*2)
        $ iason_about_steephouse_price -= ((iason_friendship+dalit_friendship)/3)
        if iason_about_steephouse_price < 10:
            $ iason_about_steephouse_price = 10
        menu:
            '“This again,” he sighs. “Fine. [iason_about_steephouse_price] coins and the {i}truth{/i} is yours,” he says without hiding his contempt.
            '
            'I sigh and reach for my pouch.' if coins >= iason_about_steephouse_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it.”')
                jump peltnorthquestionssteephouse02
            'I don’t have enough. (disabled)' if coins < iason_about_steephouse_price:
                pass
            '“That’s too much.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s too much.”')
                $ questionpreset = "iason1"
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“Your loss, {i}roadwarden{/i}.”
                    '
                    '(iason1 preset)':
                        pass

    label peltnorthquestionssteephouse02:
        $ iason_about_steephouse = 1
        $ ruinedvillage_truth = 1
        $ ruinedvillage_name = "Steep House"
        $ iason_friendship_moneybonus_points += 10
        $ quest_ruins_description_truestory = "The crew of {color=#f6d6bd}Pelt of the North{/color} assisted the people of {color=#f6d6bd}Howler’s Dell{/color} in their destruction of {color=#f6d6bd}Steep House{/color}. According to the innkeep’s story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
        $ quest_ruins_description_peltparticipated = "{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew helped {color=#f6d6bd}Thais{/color} during the raid."
        $ description_bighunters10 = "{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew helped {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."
        $ description_iason10 = "He admitted that his crew hekoed {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."
        $ description_ruinedvillage02 = "The crew of {color=#f6d6bd}Pelt of the North{/color} assisted the people of {color=#f6d6bd}Howler’s Dell{/color} in their destruction of {color=#f6d6bd}Steep House{/color}. According to the innkeep’s story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
        $ description_thais06 = "{color=#f6d6bd}Pelt’s{/color} innkeep assisted her in destroying the southern village."
        $ coins -= iason_about_steephouse_price
        show screen notifyimage( "-%s" %iason_about_steephouse_price, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-[iason_about_steephouse_price] {image=cointest}{/i}')
        if iason_stance == "sittingatstove":
            $ custom1 = "He reaches out to you, palm up, and waits for you to count down the bones. With a nod, he drops them all in a wooden bowl, then places them on top of the stove."
            $ custom2 = "He stands up and takes his new coins behind the counter, where he takes a sip from his mug."
        elif iason_stance == "behindcounter":
            $ custom1 = "He knocks on the countertop and waits for you to count down the bones. With a nod, he drops them all in a wooden mug, then places them on the shelf."
            $ custom2 = "He takes a sip from his mug."
        elif iason_stance == "sweeping":
            $ custom1 = "He puts away the broom and invites you to the counter, where you count down the bones. With a nod, he drops them all in a wooden mug, then places them on the shelf."
            $ custom2 = "He takes a sip from his mug."
        elif iason_stance == "sittingattable":
            $ custom1 = "He stands up and takes his new coins behind the counter, where he takes a sip from his mug."
            $ custom2 = "He stands up and takes his new coins behind the counter, where he takes a sip from his mug."
        $ iason_stance = "behindcounter"
        menu:
            '“Wait, are you serious?” [custom1] “I was half-joking, why would you care about a pile of rot and ashes? But a deal is a deal.” Without looking at you, he puts a finger on his lips and gathers his thoughts, but once he starts his tale, he sounds confident, even absent, as if he has had plenty of time to memorize everything there is to say.
            \n\n“After we had cleared this building of ooze, rats, and spiders, we needed some quick supplies, as well as timber and stone. We knew a bit about {color=#f6d6bd}Steep House{/color}, that’s the ruins now, and {color=#f6d6bd}Howler’s Dell{/color}, but {color=#f6d6bd}Thais{/color} was more willing to open her people’s storehouse for us. And she was willing to do so for no dragons, just one evening of work.”
            \n\nHe clears his throat, preparing himself to tread through his words carefully. “Her plan was to unite the tribes of the peninsula under her command. Taxes for protection. Some hesitated, but only one said {i}no{/i}. Maybe she wouldn’t punish any other villages as roughly as she did {color=#f6d6bd}Steep House{/color}, but, you see, they were of the same tribe, and she was making it clear to everyone what it means to {i}betray{/i} her.”
            '
            'I stare at his face, looking for lies.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare at his face, looking for lies.')
                $ quest_ruins_description_truestory = "The crew of {color=#f6d6bd}Pelt of the North{/color} assisted the people of {color=#f6d6bd}Howler’s Dell{/color} in their destruction of {color=#f6d6bd}Steep House{/color}. According to the innkeep’s story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                $ quest_ruins_description_peltparticipated = "{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew helped {color=#f6d6bd}Thais{/color} during the raid."
                $ description_bighunters10 = "{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew helped {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."
                $ description_iason10 = "He admitted that his crew helped {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."
                $ description_ruinedvillage02 = "The crew of {color=#f6d6bd}Pelt of the North{/color} assisted the people of {color=#f6d6bd}Howler’s Dell{/color} in their destruction of {color=#f6d6bd}Steep House{/color}. According to the innkeep’s story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                $ description_thais06 = "{color=#f6d6bd}Pelt’s{/color} innkeep assisted her in destroying the southern village."
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                menu:
                    'He glances at the entrance, making sure his crew is at hand. “She raided them, like in the old days. Not to destroy, just to weaken them, but her people were a bit... {i}too{/i} eager. Some bad, old blood between them, I don’t know.” He pauses. “My people and I were keeping watch at the southern pastures. We took the animals and were meant to turn the refugees back so they wouldn’t regroup, but we didn’t have much work to do.”
                    \n\n“Still, that ain’t how the village fell. Have you noticed all the tree stumps next to it? It used to be their forest garden, but they had to cut it all, almost at once, and get to repairing their walls and houses, and gather all the food from nearby branches and shrubs. Animals did {i}not{/i} like it, and the village wasn’t ready for their wrath.” [custom2] “And that’s the whole story. Not one that would make me proud, but you know how it goes. Every year brings down another village. That’s how things go.”
                    '
                    '“Don’t you dare shrug it off. You’re responsible for many deaths.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you dare shrug it off. You’re responsible for many deaths.”')
                        if peltnorth_firsttime_day <= 5 and peltnorth_firsttime_day < day:
                            $ custom1 = "\n\nAs you look into his contemptuous eyes, you find not a hint of the shy, straightforward man you met at the beginning of your journey."
                        else:
                            $ custom1 = ""
                        $ can_rest = 1
                        $ can_items = 1
                        $ iason_friendship -= 2
                        $ dalit_friendship -= 1
                        $ questionpreset = "iason1"
                        menu:
                            'He meets your eyes, “I’m responsible for the stolen mouflons and for keeping a few kids from getting to the edge of the forest. I saved them, roadwarden. Did I do so intentionally? No. But did I intend to burn their griffin-shit homes? No. Don’t!” He shouts at the door, where you see a few people reaching for their weapons. “The roadwarden won’t hurt us, not even with the army’s help.” There’s a victorious smile hiding in the edge of his lips. “Without us and our {color=#f6d6bd}Pelt{/color}, the peninsula is as good as gone. We can’t be touched.”
                            \n\nHis hunters step away, but you know he might be right.
                            \n\n“You’ve made me much richer today, [pcname]. Now tell me if you need anything, or go out there and bring me something worth buying.”[custom1]
                            '
                            '(iason1 preset)':
                                pass
                    '“Indeed. Sooner or later, everyone’s life crumbles.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Indeed. Sooner or later, everyone’s life crumbles.”')
                        if peltnorth_firsttime_day <= 5 and peltnorth_firsttime_day < day:
                            $ custom1 = "As you look into his contemptuous eyes, you find not a hint of the shy, straightforward man you met at the beginning of your journey."
                        else:
                            $ custom1 = ""
                        $ can_rest = 1
                        $ can_items = 1
                        $ iason_friendship -= 2
                        $ dalit_friendship -= 1
                        $ questionpreset = "iason1"
                        menu:
                            '“No argument there, [pcname]. All we can do is try our best to keep our families and friends safe... And pick our battles {i}wisely{/i},” his voice suddenly gets as cold as the middle of the night. [custom1]
                            '
                            '(iason1 preset)':
                                pass
                    'I nod. “Thanks for the tale. Let’s change the topic.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you dare shrug it off. You’re responsible for many deaths.”')
                        $ can_rest = 1
                        $ can_items = 1
                        $ iason_friendship += 1
                        $ questionpreset = "iason1"
                        menu:
                            'He frowns, but then nods with a gentle smile. “Very well. Go on.”
                            '
                            '(iason1 preset)':
                                pass

label peltnorthpeltnorth_sellingrawfishALL:
    label peltnorth_sellingrawfish01:
        menu:
            '“Don’t put it on the counter, if you may.” He glances at your catch, then at the stove. “My crew doesn’t hunt for fish, the lakes and rivers are too far away, and they ain’t trained with all the weaving, worms, and rods. Sell me two at once and I’ll give you a coin. I ain’t wasting the firewood on just one.”
            '
            '“Deal.”' if item_rawfishtotalnumber >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold two fish.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold two fish. +1 {image=cointest}{/i}')
                $ iason_fish_delivered_current += 2
                $ iason_fish_delivered_total += 2
                if iason_fish_delivered_current >= iason_fish_frienship_level:
                    $ iason_friendship += 1
                    $ iason_fish_delivered_current = 0
                $ item_rawfishtotalnumber -= 2
                $ item_rawfish_losing = 2
                $ iason_friendship_moneybonus_points += 1
                $ coins += 1
                $ iason_about_fish = 1
                jump peltnorth_selling02
            'I only have a single fish. (disabled)' if item_rawfishtotalnumber < 2:
                pass
            '“That’s all.”':
                hide screen selling
                jump peltnorthregularquestionsv04

    label peltnorth_sellingrawfish02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have more fish to sell.”')
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "iason1"
        show screen notifyimage( "You sold two fish. +1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold two fish. +1 {image=cointest}{/i}')
        $ iason_fish_delivered_current += 2
        $ iason_fish_delivered_total += 2
        if iason_fish_delivered_current >= iason_fish_frienship_level:
            $ iason_friendship += 1
            $ iason_fish_delivered_current = 0
        $ item_rawfishtotalnumber -= 2
        $ item_rawfish_losing = 2
        $ iason_friendship_moneybonus_points += 1
        $ coins += 1
        menu:
            'He points behind you, then puts a dragon bone on the counter. “Thanks. Put them there, in the bucket.”
            '
            '(iason1 set)':
                pass
