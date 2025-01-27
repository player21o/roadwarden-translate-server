default foggy_friendship = 0
default foggy_friendship_tradepoints = 0
default foggy_friendship_tradepoints_threshold = 2
default foggy_response_fluff = ""
default foggy_response_fluff_old = ""
default foggy_response_rumors_fluff = ""
default foggy_response_rumors_fluff_old = ""
default foggy_food_meal = ""
default foggy_food_mealold = 0
default foggy_food_meals_available = 0
default foggy_food_meals_available_free = 0
default foggy_food_meals_available_free_lastmeal = 0 # day

default foggy_about_asterion = 0 # 1 - spytana, 2 - powiedziała o płaszczu
default foggy_about_questionsasterion1 = 0
default foggy_about_questionsasterion2 = 0
default foggy_about_questionsasterion3 = 0
default foggy_about_questionsasterion4 = 0
default foggy_about_questionsasterion5 = 0
default foggy_about_asterion_questions_max = 4
default foggy_about_asterion_questions = 0
default foggy_about_foundasterion = 0

default foggy_about_dolmen_quest = 0
default foggy_about_dolmen_underground_firsttime = 0
default foggy_about_trade = 0
default foggy_about_shelter = 0
default foggy_about_job = 0
default foggy_about_bandits = 0
default foggy_about_bandits_available = 0
default foggy_about_islands = 0
default foggy_about_plague = 0
default foggy_about_asterionwine = 0
default foggy_about_necromancers = 0
default foggy_about_hermagic = 0
default foggy_about_personalquestions = 0
default foggy_about_personalquestions_amount = 0
default foggy_about_personalquestions_amount_max = 9
default foggy_about_personalquestions_inquisitive = 0
default foggy_about_herself = 0
default foggy_about_herarm = 0
default foggy_about_beastsaround = 0
default foggy_about_hunting = 0
default foggy_about_hertavern = 0
default foggy_about_herplans = 0
default foggy_about_thename = 0
default foggy_about_fish = 0
default foggy_about_alcohol = 0
default foggy_about_goblins = 0
default foggy_about_missinghunters_dayreported = 0

default foggy_about_rumors = 0
default foggy_about_rumors_available = 0
default foggy_about_rumors_firsttime = 0

default foggy_about_detailsofquest2 = 0
default foggy_quest_iason_trade = 0
default foggy_quest_iason_bonustimer = 0
default foggy_quest_iason_relationship = 0 # liedto / neutral / mad
default foggy_quest_whitemarshes_details = 0
default foggy_about_whitemarshes_cancelled = 0

default foggy_about_peltnorth = 0
default foggy_about_whitemarshes = 0
default foggy_about_monastery = 0
default foggy_about_fallentree = 0
default foggy_about_cairn = 0
default foggy_about_militarycamp = 0
default foggy_about_howlerscreek = 0
default foggy_about_steephouse = 0
default foggy_about_rockslide = 0
default foggy_about_banditshideout = 0
default foggy_about_highisland = 0
default foggy_about_caius = 0
default foggy_about_oceannecklace = 0
default foggy_about_duskfoxesshelter = 0
default foggy_about_mushroomsinruinedshelter = 0
default foggy_about_nest = 0
default foggy_about_howlerslair = 0
default foggy_about_vines = 0
default foggy_about_oldtunnel_inside_opened = 0
default foggy_about_giantstatue = 0
default foggy_about_oldcamp = 0
default foggy_aboutnavica = 0
default foggy_aboutnavica_gray = 0
default foggy_about_nomoreundead = 0
default foggy_about_clearedstatue = 0
default foggy_about_ironingot = 0

default foggy_shop_asterionscloak = 0 #0 - nie może, 1 - mówi graczowi, że może, 2 - sprzedane
default foggy_shop_asterionscloak_price = 18
default foggy_shop_ironscraps = 0
default foggy_shop_ironscraps_price = 6
default foggy_shop_axe02alt_price = 8
default foggy_shop_axehead_price = 7
default foggy_shop_furlesswolftrophy_price = 7
default foggy_shop_linen_price = 13
default foggy_shop_asterionbow_price = 9
default foggy_shop_asterionwine_price = 40
default foggy_shop_asterionwine_bought = 0
default foggy_shop_griffonegg_price = 6
default foggy_shop_griffonegg_sold = 0
default foggy_shop_elkfur_price = 0
default foggy_shop_sealskin_price = 0
default foggy_shop_cidercask_returned = 0
default foggy_shop_cidercask_bought = 0

label foggylakefoggyafterinteraction01: # po pytaniu
    label foggy_response_fluffloop:
        $ foggylake_firsttime_afterdrink = 1
        $ foggy_response_fluff = ""
        $ foggy_response_fluff = renpy.random.choice(['Her scarred lips form a grimace of a smile.', 'She gestures for you to go on.', 'She smiles. “Hwat else, dear?”', 'She asks if you have everything you need.', 'She grabs a cloth and starts to wipe the table.', '{color=#f6d6bd}Foggy{/color} grabs the dirty dishes and puts them near the bucket.', 'She tilts a window shutter by just looking at it.'])
        if foggy_response_fluff_old == foggy_response_fluff:
            jump foggy_response_fluffloop
        else:
            $ foggy_response_fluff_old = foggy_response_fluff
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    menu:
        '[foggy_response_fluff]
        '
        '(preset foggy1)':
            pass

label foggylakeregularquestionseatingALL:
    label foggylakeregularquestionseating01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to eat.”')
        $ pc_food = limit_pc_food(pc_food+2)
        show plus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        $ foggy_food_meals_available -= 1
        $ quarters += 2
        if quarters >= (world_daylength-12):
            $ custom1 = "It’s already late, so you devour everything that’s in front of you. {color=#f6d6bd}Foggy{/color}"
        else:
            $ custom1 = "Once you’re done, {color=#f6d6bd}Foggy{/color} packs the leftovers for you as a snack for the rest of the day and"
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        label foggy_food_mealloop4:
            $ foggy_food_meal = ""
            $ foggy_food_meal = renpy.random.choice(['a bowl of simple gruel, two roasted bird thighs, and a mug of acorn brew', 'a bowl of berries, two fresh, though cold, roasted perches and a cup of chamomile tisane', 'old rye bread, a fistful of nuts, a roasted rat, and a mug of acorn brew', 'old, toasted acorn bread, a large slice of mouflon cheese, and a piece of roasted pike', 'a nettle tisane and a simple root stew with plenty of meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a soft-boiled egg', 'some monster meat you can’t identify, a couple of apples, and a cup of birch sap', 'a baked, cold pheasant and a raw eggplant', 'roasted badger meat with mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water', 'a large mug of cold mint tisane and a bit stale scraps of roasted squirrel', 'two bowls, one with roasted ants and crickets and one with a warm stew'])
            if foggy_food_mealold == foggy_food_meal:
                jump foggy_food_mealloop4
            else:
                $ foggy_food_mealold = foggy_food_meal
        menu:
            'She stretches out her arm and grabs a bowl. “Give me a moment.”
            \n\nYou sit down at the clean table. After a moment, the keeper brings you [foggy_food_meal].
            \n\n[custom1] mentions that you’ve already paid for another [foggy_food_meals_available] meals.
            '
            '(preset foggy1)':
                pass

    label foggylakeregularquestionseating02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like my free meal.”')
        $ pc_food = limit_pc_food(pc_food+2)
        show plus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        $ quarters += 2
        if quarters >= (world_daylength-12):
            $ custom1 = "It’s already late, so you devour everything that’s in front of you."
        else:
            $ custom1 = "Once you’re done, {color=#f6d6bd}Foggy{/color} packs the leftovers for you as a snack for the rest of the day."
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        label foggy_food_mealloop5:
            $ foggy_food_meal = ""
            $ foggy_food_meal = renpy.random.choice(['a bowl of simple gruel, two roasted bird thighs, and a mug of acorn brew', 'a bowl of berries, two fresh, though cold, roasted perches and a cup of chamomile tisane', 'old rye bread, a fistful of nuts, a roasted rat, and a mug of acorn brew', 'old, toasted acorn bread, a large slice of mouflon cheese, and a piece of roasted pike', 'a nettle tisane and a simple root stew with plenty of meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a soft-boiled egg', 'some monster meat you can’t identify, a couple of apples, and a cup of birch sap', 'a baked, cold pheasant and a raw eggplant', 'roasted badger meat with mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water', 'a large mug of cold mint tisane and a bit stale scraps of roasted squirrel', 'two bowls, one with roasted ants and crickets and one with a warm stew'])
            if foggy_food_mealold == foggy_food_meal:
                jump foggy_food_mealloop5
            else:
                $ foggy_food_mealold = foggy_food_meal
        $ foggy_food_meals_available_free_lastmeal = day
        menu:
            'She stretches out her arm and grabs a bowl. “Give me a moment.”
            \n\nYou sit down at the clean table. After a moment, the keeper brings you [foggy_food_meal].
            \n\n[custom1]
            '
            '(preset foggy1)':
                pass

label foggylakeregularquestionsfoundasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
    $ foggy_about_foundasterion = 1
    $ minutes += 5
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    menu:
        'After your story, she lets out a chuckle. “So that’s what he’s been up to? Going there all by himself? Hwat a dumb boy.”
        \n\nShe sees your look and shrugs. “Hwat can I say, love? He wasn’t of much use. I wish I could get the head of his lizard, it would look plenty fine, oh, there.” She points at the bug’s trophy with her broad chin.
        '
        '(preset foggy1)':
            pass

label foggylakeregularquestionsasterionALL:
    label foggylakeregularquestionsasterion01: # “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”
        $ foggy_about_asterion = 1
        menu:
            'She looks at you for a longer moment, without the slightest movement. “And hwy d’you think he’s here?”
            '
            '“I’m not saying that I do. But maybe you know where I can find him?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not saying that I do. But maybe you know where I can find him?”')
                $ custom5 = "“Ah, I misunderstood you,” she shakes her head and leans on the table. “I don’t know his whereabouts. He didn’t tell me a thing more than I needed to hear.”"
                jump foggylakeregularquestionsasterion02
            '“{i}Is{/i} he here?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Is{/i} he here?”')
                $ foggy_friendship -= 1
                menu:
                    'Her face darkens as she scratches her knee. “Don’t upset me.”
                    '
                    '“All I’m saying is that he might have been here. Wounded, or ill. I’m not trying to lure you into a game.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “All I’m saying is that he might have been here. Wounded, or ill. I’m not trying to lure you into a game.”')
                        $ custom5 = "“Every soul’s got a game, though some are not ready to admit it. But no, I don’t think he was struggling with health last time I saw him.”"
                        jump foggylakeregularquestionsasterion02
                    '“Right now I suspect everyone. But I’m still looking for clues.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Right now I suspect everyone. But I’m still looking for clues.”')
                        $ custom5 = "“{i}Clues{/i}, aye. Ask me your questions, then. I don’t promise any answers, dear.”"
                        jump foggylakeregularquestionsasterion02
                    '“He could have been swallowed by a toad for all I know. I’m just asking for help.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He could have been swallowed by a toad for all I know. I’m just asking for help.”')
                        $ custom5 = "While her voice remains calm, her thin eyes get distrustful. “You’ve scared me a li’l bit. I don’t want any nasty rumors. Sure, some of those who travel through {color=#f6d6bd}Foggy’s{/color} disappear on the road, but it’s a safe place. We don’t hold slaves.” She waves toward the trapdoor. “You can check and see.”"
                        jump foggylakeregularquestionsasterion02
            '“I’m just asking around.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m just asking around.”')
                $ custom5 = "While her voice remains calm, her thin eyes get distrustful. “You’ve scared me a li’l bit. I don’t want any nasty rumors. Sure, some of those who travel through {color=#f6d6bd}Foggy’s{/color} disappear on the road, but it’s a safe place. We don’t hold slaves.” She waves toward the trapdoor. “You can check and see.”"
                jump foggylakeregularquestionsasterion02

    label foggylakeregularquestionsasterion02:
        menu:
            '[custom5]
            '
            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                jump foggylakeregularquestionsasterion03question04
            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                jump foggylakeregularquestionsasterion03question01
            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                jump foggylakeregularquestionsasterion03question02
            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                jump foggylakeregularquestionsasterion03question03
            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                jump foggylakeregularquestionsasterion03question05
            '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff {color=#f6d6bd}Asterion{/color} brought you.”')
                jump foggylakeregularquestionsasterion03question06
            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question04: # “What can you tell me about him?”
        $ foggy_about_questionsasterion4 = 1
        $ foggy_about_asterion_questions += 1
        $ minutes += 2
        menu:
            'She rests her only hand across her stomach, which you identify as her version of crossing her arms. “A customer and an errand runner, hwat’s there to say?”
            \n\nYour additional questions don’t get many more answers. She brings up the man’s looks and equipment, without adding much to what you’ve already learned from {color=#f6d6bd}Tulia{/color}.
            \n\n“He was paying with dragons, rarely bartered,” she adds. “That’s hwat cityfolk do, aye? Seeking riches, then locking themselves in a chamber, prisoners of their might.”
            '
            'I smile. “Well said.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Well said.”')
                menu:
                    'Her chuckle makes you think of a wolf’s growl.
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            'I frown. “It’s not really what I’m aiming for.”' if pc_goal != "iwantmoney":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown. “It’s not really what I’m aiming for.”')
                menu:
                    '“We’ll see, love. We’ll see.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            '(lie) I frown. “It’s not really what I’m aiming for.”' if pc_goal == "iwantmoney":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I frown. “It’s not really what I’m aiming for.”')
                $ pc_lies += 1
                menu:
                    '“We’ll see, love. We’ll see.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            'I shrug. “I see no problem with that.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “I see no problem with that.”')
                menu:
                    '“Sure you don’t. You can hide away from the awoken and the beasts, but having a {i}safe{/i} life is the dream of the fools. The next plague, the next war, the next dragon will come. There’s nowhere we can hide, but a pyre.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question01: # “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”
        $ foggy_about_questionsasterion1 = 1
        $ foggy_about_asterion_questions += 1
        menu:
            'She glances at a window. “Same as the others, in the late days of spring. We were waiting for his return, me and all the villages, then moved on. I’ve no idea where he went.”
            '
            '“{i}All{/i} of the villages, you say?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}All{/i} of the villages, you say?”')
                menu:
                    'She turns toward you with the fierceness of a bear. “That’s hwat I said.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                jump foggylakeregularquestionsasterion03question04
            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                jump foggylakeregularquestionsasterion03question01
            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                jump foggylakeregularquestionsasterion03question02
            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                jump foggylakeregularquestionsasterion03question03
            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                jump foggylakeregularquestionsasterion03question05
            '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                jump foggylakeregularquestionsasterion03question06
            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question02: # “Did he do any jobs for you?”
        $ foggy_about_questionsasterion2 = 2
        $ foggy_about_asterion_questions += 1
        menu:
            'She presses her tongue against her cheek and lips. “Well, I’m not sure. He was bringing me news, or delivering my messages. Sold me some stuff, sometimes bought a thing or two. His life wasn’t really {i}that{/i} riveting. Just another mug guzzler, sitting in the corner, patching his clothes.”
            '
            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                jump foggylakeregularquestionsasterion03question04
            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                jump foggylakeregularquestionsasterion03question01
            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                jump foggylakeregularquestionsasterion03question02
            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                jump foggylakeregularquestionsasterion03question03
            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                jump foggylakeregularquestionsasterion03question05
            '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                jump foggylakeregularquestionsasterion03question06
            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question03: # “Did he sell you anything unusual?”
        $ foggy_about_questionsasterion3 = 1
        $ foggy_about_asterion_questions += 1
        menu:
            'She stares at you without blinking. “Such’s hwat?”
            '
            '“Something that hints to where he went.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something that hints to where he went.”')
                menu:
                    'She frowns. “I’ll tell you if I think of anything.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            '“Something he found in a weird place.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something he found in a weird place.”')
                menu:
                    '“Such tales stay between me and my guests.” She nods toward the wall that separates you from the lake. “This place may be open, maybe too open, but it guards secrets just fine.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03
            '“Something useful. Maybe I could buy it back.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something useful. Maybe I could buy it back.”')
                $ foggy_friendship_tradepoints += 1
                menu:
                    'The scar on her lips distorts her smile. “It just so happens...” She hesitates. “I promised to keep it around for some time. Ask me later, maybe after you’ve shown us what you’re made of. I’ll see what I can offer.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakeregularquestionsasterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakeregularquestionsasterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakeregularquestionsasterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakeregularquestionsasterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakeregularquestionsasterion03question05
                    '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                        jump foggylakeregularquestionsasterion03question06
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question05: # “You don’t sound especially bothered by his disappearance.”
        $ foggy_about_questionsasterion5 = 1
        menu:
            '“You see me as someone eager to make friends with a vagabond? I’ll take it as a compliment to my skills as a tavernkeep. Folks come and go, their faces disappear, friends die in my arms,” she pauses, “families fade away. There was a different roadwarden years ago, and there is another one now. But there’s only one {color=#f6d6bd}Foggy{/color} in the North, and one {color=#f6d6bd}Ilan{/color}, that slow son of mine, and one {color=#f6d6bd}Creeks{/color}. I have only so many tears to spare.”
            '
            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                jump foggylakeregularquestionsasterion03question04
            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                jump foggylakeregularquestionsasterion03question01
            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                jump foggylakeregularquestionsasterion03question02
            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                jump foggylakeregularquestionsasterion03question03
            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                jump foggylakeregularquestionsasterion03question05
            '“I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”')
                jump foggylakeregularquestionsasterion03question06
            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                jump foggylakeregularquestionsasterion03

    label foggylakeregularquestionsasterion03question06: # “I think I’ve done enough to earn your trust. Tell me more about the stuff he brought you.”
        $ foggy_about_asterion = 2
        $ foggy_shop_asterionscloak = 1
        menu:
            'She observes you with the patience of a statue, then sends the one-handed man outside with a nod. After a minute, she brings from the basement a simple package covered with wax, tied together with a couple of cords. She removes them in silence, the scent of honey fills the air.
            \n\nShe raises a dark cloak, green like trees covered by shadows. The shapes of leaves are embroidered on the surface with a silver-like thread, from the hood to the very bottom. They are the size of your hand, spread sparsely, elegant. Each one is different.
            \n\nIt’s heavy, most likely rainproof, but the inner layer is downy, made from lambswool. Every scrap of this garment was touched by a master.
            \n\n“There’s magic in it.” {color=#f6d6bd}Foggy’s{/color} voice is solemn. “Keeps you warm at night, without a fireplace. Makes rocks feel like fur.”
            '
            '“Why did he sell it to you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why did he sell it to you?”')
                $ renpy.notify("You can now trade for a new item.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
                menu:
                    '“He {i}needed{/i} dragon bones. Was planning to travel somewhere, needed coins for a boat.” She folds the cloak and packs it again, tying the cords with her thoughts. “I told him to look for it in {color=#f6d6bd}Gale Rocks{/color}.”
                    \n\nYou wait for her to go on, but she changes the topic. “I wanted to sell it for fifty dragons, but if you’re interested, we’ll see. I won’t ask for a fortune from a friend.”
                    '
                    '“Where was he heading, {color=#f6d6bd}Foggy{/color}?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where was he heading, {color=#f6d6bd}Foggy{/color}?”')
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ asterion_highisland_clues += 1
                        if quest_asterion == 1 and not asterion_found:
                            $ renpy.notify("Journal updated: Find the Roadwarden")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ description_asterion12 = "According to {color=#f6d6bd}Foggy{/color}, Asterion sold her a unique, magical cloak to purchase a boat."
                        $ quest_asterion_description10 = "According to {color=#f6d6bd}Foggy{/color}, Asterion was seen purchasing a boat in {color=#f6d6bd}Gale Rocks{/color}."
                        menu:
                            '“I told you everything I know, love.” She holds the package with her elbow. “Take it from here on your own.”
                            '
                            '(preset foggy1)':
                                pass

    label foggylakeregularquestionsasterion03:
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        $ quarters += 1
        $ minutes += 10
        menu:
            '“Maybe, maybe. Once our souls are too restless to stay quiet.”
            '
            '(preset foggy1)':
                pass

label foggylakeregularquestionsshelter01: # “Could I spend a night or two under your roof?”
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could I spend a night or two under your roof?”')
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    $ minutes += 5
    $ foggy_about_shelter = 1
    $ renpy.notify("New shelter unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
    # if foggy_friendship < 10:
    #     $ custom1 = ""
    # else:
    #     $ custom1 = "“I guess we can make an exception for you, love. You seem to be quite useful.”"
    menu:
        'She approaches a window above the table and looks outside. “Your beast won’t make it easy for us, dear.” She places her hand on the shutters. “It’s not a city inn, I don’t cook for a smile, I don’t work to feel noble. I allow folks to lie down there for free,” she points to the bear fur with her broad chin, “but that’s ‘bout it. If your horse stays outside, it’ll lure the beasts to us, but if we move it here, upstairs, it’ll leave its droppings on my floor.” She gets annoyed even by the idea of it happening. “If you want to rest here, love, be ready either to pay with a coin or some food rations, or to spend the night keeping your mount quiet. And clean after it in the morning, will you?” She steps away.
        '
        '(preset foggy1)':
            pass

label foggylakeregularquestionstradeALL:
    label foggylakeregularquestionstrade01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What do you have for sale?”')
        $ foggy_about_trade = 1
        $ renpy.notify("New trader unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
        menu:
            '“Now you’re talking,” she grins. “Well, I could serve you some of my cooking. Not food rations, mind you, need hwat we can save for the winter season. Let’s say you give me a dragon, and in return I’ll cook for you four times. You just need to ride up when you’re hungry. And other than that... You won’t take any wood or stone, are you?” Seeing your shrug, she waves it off and heads toward the trapdoor.
            \n\nAfter a minute, she shows up with a sack that clangs after every step. “I can sell you some scraps.” She pulls out a couple of iron clasps, nails, and a broken steel blade. A value trash. “We found them hwile foraging. We don’t have a furnace in {color=#f6d6bd}Creeks{/color}, but you could sell these bits and pieces to someone else.” She observes you for a moment, then shrugs. “Let’s discuss the price?”
            '
            '“Let me take a look first.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me take a look first.”')
                $ shop = "foggylakefoggy"
                show screen shopscreen with dissolve
                $ minutes += 5
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'You discuss the prices.
                    '
                    '(preset foggy1)':
                        pass

    label foggylakeregularquestionstrade02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to buy something.”')
        $ shop = "foggylakefoggy"
        show screen shopscreen with dissolve
        $ minutes += 5
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        menu:
            'She mentions her sparse supplies.
            '
            '(preset foggy1)':
                pass

label foggylakeregularquestionssellingALL:
    label foggylakeregularquestionsselling01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some things I’m willing to part with.”')
        $ shop = "foggylakefoggy"
        $ thingstosell = 0
        if item_axe02alt or item_axehead or item_axeset:
            $ thingstosell += 1
        if item_furlesswolftrophy:
            $ thingstosell += 1
        if item_ironingot and not foggy_about_ironingot:
            $ thingstosell += 1
        if item_linen:
            $ thingstosell += 1
        if item_trollurine:
            $ thingstosell += 1
        if item_peltnorthberryclaw:
            $ thingstosell += 1
        if item_rawfishtotalnumber and not foggy_about_fish:
            $ thingstosell += 1
        if item_peltnorthberrytools:
            $ thingstosell += 1
        if item_elkfur:
            $ thingstosell += 1
        if item_sealskin:
            $ thingstosell += 1
        if item_dragonlingclaws:
            $ thingstosell += 1
        if item_asterionbow:
            $ thingstosell += 1
        if item_asterionspear:
            $ thingstosell += 1
        if item_asterionwine and item_asterionwine_pcknows_1 and item_asterionwine_pcknows_2:
            $ thingstosell += 1
        if item_asterionwine and item_asterionwine_pcknows_1 and not item_asterionwine_pcknows_2:
            $ thingstosell += 1
        if item_stoat:
            $ thingstosell += 1
        if item_boartusks:
            $ thingstosell += 1
        if item_goblinspear:
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
            menu:
                '“And I {i}may{/i} be willing to buy them, love.”
                '
                '“Forget it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        else:
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            hide screen selling
            menu:
                'You show her what you have for sale, but she waves her hand. “Nah, love. Come back with something I could sell at a profit, or maybe hang on the wall.” You collect your belongings.
                '
                '(preset foggy1)':
                    pass

    label foggylakeselligALL_ITEMS:
        label foggylakesellingaxe02alt:
            $ foggy_shop_axe02alt_price = (8-appearance_price)
            menu:
                '“It could be older than my parents.” She holds the bronze head under her nose, examining the blade. “Aye, not bad. Steel stays sharp longer, you know,” she glances at you. “But bronze survives waves and rains. I’ll take it for {color=#f6d6bd}[foggy_shop_axe02alt_price] dragons{/color}, my son would enjoy it.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the bronze axe.\n+%s" %foggy_shop_axe02alt_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bronze axe. +%s {image=cointest}{/i}' %foggy_shop_axe02alt_price)
                    $ item_axe02alt = 0
                    $ coins += foggy_shop_axe02alt_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingaxehead:
            $ foggy_shop_axehead_price = (7-appearance_price)
            menu:
                '“It could be older than my parents.” She holds the bronze head under her nose, examining the blade. “Aye, not bad. Steel stays sharp longer, you know,” she glances at you. “But bronze survives waves and rains. I’ll take it for {color=#f6d6bd}[foggy_shop_axehead_price] dragons{/color}, my son would enjoy it.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the axe head.\n+%s" %foggy_shop_axehead_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the axe head. +%s {image=cointest}{/i}' %foggy_shop_axehead_price)
                    $ item_axehead = 0
                    $ item_axeset = 0
                    $ coins += foggy_shop_axehead_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingfurlesswolftrophy:
            $ foggy_shop_furlesswolftrophy_price = (8-appearance_price)
            menu:
                'You lead her outside and reveal the head attached to your saddle. {color=#f6d6bd}Foggy’s{/color} eyes are wide open, and her grin turns into laughter. She grabs the head and moves it closer to her scarred face, looking deeply into its dead eyes. Next to her, the monster would be tiny.
                \n\n“You brought me a treat, love!” Her voice is so loud that {color=#f6d6bd}[horsename]{/color}, already disturbed by the smell of blood, steps away. “It’ll look plenty fine on my wall. {color=#f6d6bd}[foggy_shop_furlesswolftrophy_price] dragons{/color}!” She looks at you with a smile. “No soul in the North will give you more, and it will soon turn into a stinking pulp.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the head of a beast.\n+%s" %foggy_shop_furlesswolftrophy_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the head of a beast. +%s {image=cointest}{/i}' %foggy_shop_furlesswolftrophy_price)
                    $ item_furlesswolftrophy = 0
                    $ coins += foggy_shop_furlesswolftrophy_price
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 2
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellinglinen:
            $ foggy_shop_linen_price = (14-appearance_price)
            menu:
                '“You brought this here from {color=#f6d6bd}Howler’s{/color}?” She runs her fingers over the unpacked stack of fabric, then grins. “I want it!” She announces. “I won’t get something like this in {color=#f6d6bd}Creeks{/color}, and I could use a proper dress. I’ll give you {color=#f6d6bd}[foggy_shop_linen_price] dragons{/color} for it, take them, or I’m going to buy me another sack from {color=#f6d6bd}Akakios{/color}.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the stack of linen fabric.\n+%s" %foggy_shop_linen_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the stack of linen fabric. +%s {image=cointest}{/i}' %foggy_shop_linen_price)
                    $ item_linen -= 1
                    $ coins += foggy_shop_linen_price
                    $ foggy_friendship += 1
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingtrollurine:
            menu:
                'She narrows her eyes. “Well, don’t open it. I’ve seen it before, in the hands of that wayfarer.” She waves her hand. “I’ll give you {color=#f6d6bd}four dragons{/color}, no more. Goblins are pests, but they stick to the South.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the jar.\n+4", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the jar. +4 {image=cointest}{/i}')
                    $ item_trollurine -= 1
                    $ coins += 4
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingpeltnorthberryclaw:
            menu:
                '“That’s a nice one,” she raises the pebbler’s claw to a beam of light. “Pebbler’s? It must have lost it in the woods. I’d put it... maybe there,” she points at a shelf with her chin. “{color=#f6d6bd}Three dragons{/color}, more than fair.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the pebbler’s claw.\n+3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the pebbler’s claw. +3 {image=cointest}{/i}')
                    $ item_peltnorthberryclaw = 0
                    $ coins += 3
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingpeltnorthberrytools:
            menu:
                '“I don’t need this, but that’s a nice claw,” she raises it to the beam of light. “Pebbler’s? It must have lost it in the woods. I’d put it... maybe there,” she points at a shelf with her chin. “{color=#f6d6bd}Three dragons{/color}, more than fair.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the hook with a claw.\n+3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the hook with a claw. +3 {image=cointest}{/i}')
                    $ item_peltnorthberrytools = 0
                    $ coins += 3
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingfurlesswolfironingot:
            $ foggy_about_ironingot = 1
            $ galerocks_pastrobbery = 1
            menu:
                'She gives it a long look, then meets your eyes. “I don’t know hwere you got it, but I’d take it to {color=#f6d6bd}Severina{/color}, the headwoman of {color=#f6d6bd}Gale Rocks{/color}. The folks from there were asking me ‘bout a stolen ingot.”
                '
                '“Interesting.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Interesting.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingrawfish:
            $ foggy_about_fish = 1
            menu:
                '“You know we’re by the lake, aye?” She laughs and gestures for you to take your catch away. “There are fresh fish in {color=#f6d6bd}Creeks{/color}, salty ones in {color=#f6d6bd}Gale Rocks{/color}... Maybe try in the {color=#f6d6bd}Ape Ale{/color} inn, in {color=#f6d6bd}Howler’s{/color}? Or in {color=#f6d6bd}Pelt of the North{/color}?”
                '
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingelkfur:
            if foggy_friendship < 5:
                $ foggy_shop_elkfur_price = (20-appearance_price)
                $ custom1 = "Better prices are reserved to my regulars."
            elif foggy_friendship < 10:
                $ foggy_shop_elkfur_price = (21-appearance_price)
                $ custom1 = "You’re a dear, but it’s already a fair offer. I give better ones only to my regulars."
            elif foggy_friendship < 15:
                $ foggy_shop_elkfur_price = (22-appearance_price)
                $ custom1 = "You’re a love, but it’s already more than a fair offer."
            else:
                $ foggy_shop_elkfur_price = (23-appearance_price)
                $ custom1 = "It’s the best I can offer."
            menu:
                'You unfold the elk fur and she presses it with her open palm. “Soft enough, large... Very good for my attic, dear.” She examines it carefully, and the imperfections she points out sound to you rather minuscule.
                \n\nShe sizes you up. “I’ll give you {color=#f6d6bd}[foggy_shop_elkfur_price] dragon bones{/color},” she gives you no space to haggle. “[custom1]”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the elk fur.\n+%s" %foggy_shop_elkfur_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the elk fur. +%s {image=cointest}{/i}' %foggy_shop_elkfur_price)
                    $ item_elkfur -= 1
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 1
                    $ coins += foggy_shop_elkfur_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingsealskin:
            if foggy_friendship < 5:
                $ foggy_shop_sealskin_price = (10-appearance_price)
                $ custom1 = "Better prices are reserved to my regulars."
            elif foggy_friendship < 10:
                $ foggy_shop_sealskin_price = (11-appearance_price)
                $ custom1 = "You’re a dear, but it’s already a fair offer. I give better ones only to my regulars."
            elif foggy_friendship < 15:
                $ foggy_shop_sealskin_price = (13-appearance_price)
                $ custom1 = "You’re a love, but it’s already more than a fair offer."
            else:
                $ foggy_shop_sealskin_price = (15-appearance_price)
                $ custom1 = "It’s the best I can offer."
            menu:
                'You hold the sealskin, allowing {color=#f6d6bd}Foggy{/color} to measure it with her forearm. “A greenhorn’s work, aye?” She points at the flaws in the pelt, and you must admit they’re hard to ignore. “Not good for a wall, but at my home we’ll turn it into a fluffy trimming for a few cloaks.”
                \n\nShe sizes you up. “{color=#f6d6bd}[foggy_shop_sealskin_price] dragon bones{/color} should be enough,” she says in a way that makes it clear she’s not willing to haggle. “[custom1]”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the sealskin.\n+%s" %foggy_shop_sealskin_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the sealskin. +%s {image=cointest}{/i}' %foggy_shop_sealskin_price)
                    $ item_sealskin -= 1
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 1
                    $ coins += foggy_shop_sealskin_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingdragonlingclaws:
            menu:
                '“Pointy,” she touches the tip of a claw with her finger. “From a runner?” After you correct her, she nods with approval. “A full set from a saurian’s paw... It would look plenty fine on a table at a feast, with some berries between them.” You spot a hint of a smile behind her scar. “{color=#f6d6bd}Three dragons{/color}.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the dragonling claws.\n+3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the dragonling claws. +3 {image=cointest}{/i}')
                    $ item_dragonlingclaws -= 1
                    $ coins += 3
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingasterionbow:
            $ foggy_shop_asterionbow_price = (9-appearance_price)
            menu:
                '“A friend of mine in {color=#f6d6bd}Creeks{/color} will want this,” she weighs Asterion’s bow in her hand. “It’s better than ours. {color=#f6d6bd}[foggy_shop_asterionbow_price] dragon bones{/color}, let’s say, for this and the string. We don’t need any arrows.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold Asterion’s bow.\n+%s" %foggy_shop_asterionbow_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold Asterion’s bow. +%s {image=cointest}{/i}' %foggy_shop_asterionbow_price)
                    $ item_asterionbow -= 1
                    $ foggy_friendship += 1
                    $ coins += foggy_shop_asterionbow_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingasterionspear:
            menu:
                '“A plenty fine weapon, especially the head,” she nods while holding Asterion’s spear. “The boys outside could practice with it in winter, I don’t trust their daggers and clubs. But I won’t give you more than {color=#f6d6bd}six dragons{/color}.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold Asterion’s spear.\n+6", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold Asterion’s spear. +6 {image=cointest}{/i}')
                    $ item_asterionspear -= 1
                    $ foggy_friendship_tradepoints += 2
                    $ coins += 6
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01


        label foggylakesellingstoat:
            if item_stoat == 1:
                menu:
                    '“Not the cleanest game, won’t get too much out of the pelt,” she takes a good look at the dead stoat. “Better sell it while it doesn’t smell. I’ll free you of it for {color=#f6d6bd}four dragons{/color}.”
                    '
                    '“Deal.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        show screen notifyimage( "You sold the dead stoat.\n+4", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the dead stoat. +4 {image=cointest}{/i}')
                        $ item_stoat = 0
                        $ coins += 4
                        $ foggy_friendship_tradepoints += 1
                        jump foggylakeregularquestionsselling02
                    '“Maybe later.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                        hide screen selling
                        jump foggylakefoggyafterinteraction01
            if item_stoat == 2:
                menu:
                    '“Good job with the clean kill, I see no wounds on it.” She takes a good look at the dead stoat. “Better sell it while it doesn’t smell. I’ll free you of it for {color=#f6d6bd}six dragons{/color}.”
                    '
                    '“Deal.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                        show screen notifyimage( "You sold the dead stoat.\n+6", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the dead stoat. +6 {image=cointest}{/i}')
                        $ item_stoat = 0
                        $ coins += 6
                        $ foggy_friendship_tradepoints += 2
                        jump foggylakeregularquestionsselling02
                    '“Maybe later.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                        hide screen selling
                        jump foggylakefoggyafterinteraction01
        label foggylakesellingboartusks:
            menu:
                '“These are large, dear, but every now and then we also hunt down a boar or two.” She places the tusks on the table, making a circle. “I may sell them to a traveler one day, the cityfolk like to show their friends hwat mighty hunters they are. I’ll give you {color=#f6d6bd}a dragon, and dinner{/color} later on.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the boar tusks\nfor a meal and +1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the boar tusks for a meal and +1 {image=cointest}{/i}')
                    $ item_boartusks -= 1
                    $ coins += 1
                    $ foggy_food_meals_available += 1
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellinggoblinspear:
            menu:
                '“What an eyesore. Did {i}you{/i} make this?” After you mention the goblins, her curiosity grows. “Could one of them really shape the tip like this? Or did it find a kid’s toy at the edge of a village?” She scoffs. “Not too impressive of a trophy, I won’t display it in the hall. But I’ll gladly store it in my cellar. I’ll give you {color=#f6d6bd}two meals{/color} for it. You can eat them here once you’re hungry.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    $ renpy.notify("You sold the goblin spear for two meals.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the goblin spear for two meals.{/i}')
                    $ item_goblinspear -= 1
                    $ foggy_food_meals_available += 2
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellinggriffonegg:
            $ foggy_shop_griffonegg_price = (6-appearance_price)
            menu:
                '“Oh dear!” She covers the egg with her massive hand, but sighs after noticing the unusual lightness. “Won’t even press a cloth on a table. I could, let me think, make a stand for it, a piece of wood here and here...” She illustrates how it would work with her fingers, then looks back at you only after you clear your throat. “I like it {color=#f6d6bd}[foggy_shop_griffonegg_price] dragons{/color} strong, love.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the griffon egg.\n+%s" %foggy_shop_griffonegg_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the griffon egg. +%s {image=cointest}{/i}' %foggy_shop_griffonegg_price)
                    $ item_griffonegg -= 1
                    $ foggy_friendship += 1
                    $ foggy_shop_griffonegg_sold = 1
                    $ coins += foggy_shop_griffonegg_price
                    jump foggylakeregularquestionsselling02
                '“Forget it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingasterionwine01:
            $ foggy_shop_asterionwine_price = (40-(appearance_price*2))
            menu:
                'Her eyes widen once you mention the Night’s Bane. You share what you’ve learned about it, and she listens without interruptions.
                \n\n“I’ve met a folk or two who used to say that this wine is sought after like hardly any. Made of grapes, but finer than those we have in the north. And the new bottles may never come, not since the cityfolk stopped robbing The Southern Realms,” she says with an undisguised satisfaction. “If it’s the real deal... I can give you {color=#f6d6bd}[foggy_shop_asterionwine_price] dragons{/color}. Better take it before I get smarter.”
                \n\nYou try to haggle, but she interrupts you. “But I can’t be sure it’s really hwat you say, aye? Could someone fill the bottle with a sailor’s piss? That’s already too much of a risk.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the bottle of Night’s Bane.\n+%s" %foggy_shop_asterionwine_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bottle of Night’s Bane. +%s {image=cointest}{/i}' %foggy_shop_asterionwine_price)
                    $ item_asterionwine -= 1
                    $ foggy_friendship += 4
                    $ coins += foggy_shop_asterionwine_price
                    menu:
                        'She returns from the basement with a small sack filled with rattling coins. She scatters them on the table, all sorts of larger and smaller bone-made disks in many colors, from gray, through cream, to white. She counts down the agreed amount, then asks you to do the same.
                        \n\nOnce you’re done, she takes a deep breath, pushes the pile toward you, then shoves the rest back into the bag.
                        \n\n“Let’s not talk ‘bout it,” she grunts. “There’s a good chance it’s {i}you{/i} who’s doing {i}me{/i} a favor. We’ll see, dear.”
                        '
                        'I nod. “How about this?”':
                            jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        label foggylakesellingasterionwine02:
            $ foggy_shop_asterionwine_price = (15-appearance_price)
            menu:
                '“You’re saying it’s from grapes? I’ll take a sniff, aye?” She puts the bottle under her nose and lets out a pleased sigh. “I don’t know much ‘bout these, but this one smells plenty fine. It must be rare. {color=#f6d6bd}[foggy_shop_asterionwine_price] dragons{/color}? I’d add it to my collection.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold Asterion’s wine.\n+%s" %foggy_shop_asterionwine_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold Asterion’s wine. +%s {image=cointest}{/i}' %foggy_shop_asterionwine_price)
                    $ item_asterionwine -= 1
                    $ foggy_friendship += 2
                    $ coins += foggy_shop_asterionwine_price
                    jump foggylakeregularquestionsselling02
                '“Maybe later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe later.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01

    label foggylakeregularquestionsselling02:
        if not tutorial_selling:
            $ tutorial_selling = 1
        $ thingstosell = 0
        if item_axe02alt or item_axehead or item_axeset:
            $ thingstosell += 1
        if item_furlesswolftrophy:
            $ thingstosell += 1
        if item_ironingot and not foggy_about_ironingot:
            $ thingstosell += 1
        if item_linen:
            $ thingstosell += 1
        if item_trollurine:
            $ thingstosell += 1
        if item_peltnorthberryclaw:
            $ thingstosell += 1
        if item_rawfishtotalnumber and not foggy_about_fish:
            $ thingstosell += 1
        if item_peltnorthberrytools:
            $ thingstosell += 1
        if item_elkfur:
            $ thingstosell += 1
        if item_sealskin:
            $ thingstosell += 1
        if item_dragonlingclaws:
            $ thingstosell += 1
        if item_asterionbow:
            $ thingstosell += 1
        if item_asterionspear:
            $ thingstosell += 1
        if item_asterionwine and item_asterionwine_pcknows_1 and item_asterionwine_pcknows_2:
            $ thingstosell += 1
        if item_asterionwine and item_asterionwine_pcknows_1 and not item_asterionwine_pcknows_2:
            $ thingstosell += 1
        if item_stoat:
            $ thingstosell += 1
        if item_boartusks:
            $ thingstosell += 1
        if item_goblinspear:
            $ thingstosell += 1
        if item_griffonegg:
            $ thingstosell += 1
        if thingstosell:
            show screen selling()
            menu:
                '“I still may have a bone or two, love.”
                '
                '“Forget it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                    hide screen selling
                    jump foggylakefoggyafterinteraction01
        else:
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            hide screen selling
            menu:
                '“Come back with something I could sell at a profit, or maybe hang on the wall.” You collect your belongings.
                '
                '(preset foggy1)':
                    pass

label foggylakeregularquestionsoceannecklace01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the ocean necklace. “Any ideas where this comes from?”')
    $ minutes += 3
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    $ foggy_about_oceannecklace = 1
    menu:
        'She doesn’t reach out for it. “Ah, one of those that shine in the sun. The folks from {color=#f6d6bd}Gale Rocks{/color} make them from the shells and dead sharks they find on the coast.”
        \n\nYou ask about a probable owner, but she lets out a puff. “Could be anyone.”
        '
        '(preset foggy1)':
            pass

label foggylakeregularquestionsbandits01ALT:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard there are some bandits in the North.”')
    jump foggylakeregularquestionsbandits01AFTER
    label foggylakeregularquestionsbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve mentioned bandits?”')
        jump foggylakeregularquestionsbandits01AFTER
        label foggylakeregularquestionsbandits01AFTER:
            $ minutes += 4
            $ foggy_about_bandits = 1
            $ description_bandits01 = "According to {color=#f6d6bd}Foggy{/color}, the highwaymen sometimes eat at her place, but they don’t bother them. Seems like they’ve made a pact."
            $ description_glaucia08 = "According to {color=#f6d6bd}Foggy{/color}, she became the leader of the local bandits after they faced some sort of a tragedy."
            menu:
                'She makes an annoyed grimace. “Hwat can I tell you, dear? You know how it goes. Lost souls need a new path after an awfulness finds them, but the years go by, and it doesn’t get any easier. One day they take a pile of firewood, another one some bread and clothes. After they start hurting folks, there’s no way back, even if they’re not at all cruel.”
                \n\nYou ask her some more, but she’s reluctant to give you straightforward answers. “You don’t have to worry ‘bout {color=#f6d6bd}Glaucia’s{/color} band. They hunt, sometimes take this or that, scavenge after folks who get jumped by beasts. But she never tried to threaten my place. You’re safe here, and hwy would they try to bother a roadwarden?”
                '
                'She may be right. Some {i}bandits{/i} are just desperate.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- She may be right. Some {i}bandits{/i} are just desperate.')
                    jump foggylakefoggyafterinteraction01
                'I frown, but bite my tongue. If {color=#f6d6bd}Hovlavan{/color} sends its soldiers here, she may face consequences for supporting the outlaws.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown, but bite my tongue. If {color=#f6d6bd}Hovlavan{/color} sends its soldiers here, she may face consequences for supporting the outlaws.')
                    jump foggylakefoggyafterinteraction01

label foggylakeregularquestionsnecromancers01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about necromancers here in the North?”')
    $ foggy_about_necromancers = 1
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    $ description_whitemarshes05 = "I heard that the locals had to stop selling their lumber because {color=#f6d6bd}Howler’s Dell{/color} started offering their own supplies for much better prices. Because of that, the village fell into poverty."
    $ description_orentius06 = "According to {color=#f6d6bd}Foggy{/color}: “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”"
    menu:
        'She rubs her chin. “I don’t like what they’re doing one bit, but I can’t blame them. The folks at {color=#f6d6bd}Hwite Marshes{/color} struggle, and they don’t know how to protect their kids, their elders. {color=#f6d6bd}Orentius{/color}, their priest...” She cracks her shoulders. “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”
        \n\nShe opens the door with a wave of her hand, letting in some fresh air. She looks at the lake. “They used to trade in lumber, those from {color=#f6d6bd}Marshes{/color}, until {color=#f6d6bd}Howler’s Dell{/color} started selling their own trees for better prices. The trade to {color=#f6d6bd}Marshes{/color} died, and so came the hunger.” She looks at you with an unclear grimace on her lips. “You may judge them, but at least their preacher gave them hope, even if it’s tied to black magic.”
        '
        '(preset foggy1)':
            pass

label foggylakeregularquestionsalchemyset01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I take a look at your brewing set? I’m a bit of an alchemist.”')
    $ minutes += 5
    $ foggylake_alchemytable_firsttime = 1
    menu:
        'She frowns, but gestures for you to follow her. “Don’t touch anything. I’ve no toys here,” she gasps as she squeezes through the trapdoor. Downstairs, she has to lower her head to avoid the beams beneath the ceiling.
        \n\nThe humid scent of over a dozen wooden barrels is free of putridity. Your eyes run over the trophies - claws, bones, jaws, and tusks are gathered in piles, while the staffed heads of various creatures observe you with their fake eyes.
        \n\n{color=#f6d6bd}Foggy{/color} lights a candle with the help of a tinder box and leads you to a table in the furthest corner. The instruments made of glass, gold, and copper would allow you to brew even advanced potions. Bottles, scales, knives, alembics, mortars, a crucible... The jars on a shelf contain simple, but useful ingredients.
        '
        '“I could put this table to good use, {color=#f6d6bd}Foggy{/color}.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could put this table to good use, {color=#f6d6bd}Foggy{/color}.”')
            $ minutes += 5
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            menu:
                '“Could you, now,” her voice is playful, but her face is covered with shadows. “You could also set the place on fire, or spill my stuff, or break this... glass thingy.” She waves at one of the alembics and heads back to the stairs. “We’ll see how trustworthy you are, dear. We’ll see.”
                \n\nShe suddenly turns back and gives you a harsh look. “Don’t you think I’ll give you my stuff for nothing. We’re in the middle of nowhere, ingredients are expensive. You brew, you pay. And if I don’t like the way you walk around here, you pay more. The rule of the tavern.”
                '
                '(preset foggy1)':
                    pass

label foggylakeregularquestionscaius01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with {color=#f6d6bd}Caius{/color}. I wonder why you agreed to keep him around.”')
    $ foggy_about_caius = 1
    $ foggy_friendship_tradepoints += 1
    $ questionpreset = "foggy1"
    if foggy_about_shelter == 1:
        $ can_rest = 1
    menu:
        '“Ha! Do I {i}need{/i} a reason?” Her amused eyes get thoughtful as she looks at the ceiling. “He came here as a poor soul in need, taught only how to use a spear and a shield. I {i}know{/i} how it feels, to have all that you’re good at taken away from you.”
        \n\nShe straightens up and hits her chest with her fist. “But so I know that new paths await us, with or without the help of others! {color=#f6d6bd}Caius{/color} legs may be buried in despair, but I’m ready to throw him a shovel, once he asks for it.” She pauses, then looks through the window. “Though these fantasies of his won’t help him ask anytime soon. They swallow his thoughts.”
        '
        '(preset foggy1)':
            pass

label foggy_about_navicaALL:
    label foggy_about_navica01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Try to remember. Maybe there’s someone you know of who’s been to {color=#f6d6bd}High Island{/color}?”')
        $ foggy_aboutnavica_gray = 1
        if (foggy_friendship+appearance_charisma) < 10:
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            menu:
                'She scratches her knee. “How could I, dear. It’s such’ dangerous place, and there are... folks who’d be upset with those reaching it without their permission.”
                '
                '(preset foggy1)':
                    pass
        else:
            jump foggy_about_navica03

    label foggy_about_navica02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Help me, {color=#f6d6bd}Foggy{/color}. I need to find someone who knows more about {color=#f6d6bd}High Island{/color}.”')
        jump foggy_about_navica03

    label foggy_about_navica03:
        $ galerocks_navica_pcknowsabout_highisland = 1
        $ foggy_aboutnavica = 1
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        menu:
            'She rolls her eyes. “Dear, dear... You’re putting your fingers into the wrong stew.“ You’re ready to change the topic, but she sighs loudly, then almost whispers. “Ask {color=#f6d6bd}Navica{/color} from {color=#f6d6bd}Gale Rocks{/color}.”
            '
            '(preset foggy1)':
                pass

label foggylakeregularquesaboutnomoreundeadALL:
    label foggylakeregularquesaboutnomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} won’t be overtaken by its undead. {color=#f6d6bd}Orentius{/color} agreed to abandon dark magic.”')
        $ foggy_about_nomoreundead = 1
        $ foggy_friendship += 3
        $ quarters += 1
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        if foggylake_firsttime_pcdrinks == 1 or foggylake_firsttime_pcdrinks == 2:
            $ custom1 = "pour both of you a cup of dense mead"
        else:
            $ custom1 = "pour herself a cup of dense mead, while you get a mug of birch sap with honey"
        menu:
            '“He did?” She waits for your nod, then bursts into laughter. “Splendid! Tell me everything, love!”
            \n\nRight when you start, she gestures for you to sit down at the table, and uses her hand and spells to [custom1]. She listens patiently, then leans away, scratching her chin with her wrist.
            \n\n“When I was younger, we had it easier than you do now,” her wide grin carries more charm than playfulness. “Before the war, there were all these patrols, wardens, monks... Not many folks were eager to solve their issues with force. We, adventurers, only asked for a target and the pay. No one asked us to judge human hearts. I don’t envy you,” she points at you with her cup, “trying to hold both an axe, and your wits, but I’m glad you do well with them both.”
            '
            '(foggy1 set)':
                pass

    label foggylakeregularquesaboutnomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} won’t be overtaken by its undead, but the locals will most likely cut their ties to the other settlements.”')
        $ foggy_about_nomoreundead = 1
        $ foggy_friendship += 1
        $ minutes += 5
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        menu:
            '“Are you sure?” She waits for your nod, then lets out a sigh. “How did it come to this?”
            \n\nShe listens patiently, mixing the stew in the cauldron. “Necromancers or not, I wish them the best,” her voice is raised, yet sullen. “Maybe you had no other options, I can’t tell,” she glances at you, “but there are now even more wounds to heal. Wounds that can tear this land apart.”
            '
            '(foggy1 set)':
                pass

    label foggylakeregularquesaboutnomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} is no more, and its undead may soon come here. I don’t believe your wall and foragers will be enough to keep you safe.”')
        $ foggy_about_nomoreundead = 1
        $ foggy_friendship -= 5
        $ minutes += 5
        $ questionpreset = "foggy1"
        if foggy_about_shelter == 1:
            $ can_rest = 1
        menu:
            'She stares into your eyes. “Say that again.”
            \n\nYou start to describe what happened in the village, but {color=#f6d6bd}Foggy{/color} doesn’t let you finish. She springs to her feet, steps away, grabs a chair and throws it at the wall - its loud shatter makes {color=#f6d6bd}the foragers{/color} look inside.
            \n\n{color=#f6d6bd}The keeper{/color} gasps for air, buried underneath the many decades she has seen. “Bring another,” she tells her son, and he obediently heads toward the trapdoor. She kicks away the chair’s leg and moves back to you. “You did this. How?”
            \n\nYou tell her as little as you can, but she waves it all off. “Forget it. I’d rather listen to one of your victims, if there are any left.”
            '
            '(foggy1 set)':
                pass

label foggyallquests:
    label foggylakeregularquestionsjob1ALL:
        label foggylakeregularquestionsjob101:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for work.”')
            $ foggy_about_job = 1
            $ quest_foggy1oldpagos = 1
            $ renpy.notify("New entry: Check on Old Págos")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Old Págos{/i}')
            menu:
                'She grins. “I somehow doubt you’re here to forage for me, love. Not that I have any room for another soul. Let me think.” She runs her eyes over the shelves and the trophies, but it’s the rocks surrounding the fireplace that catch her attention.
                \n\n“The folks at {color=#f6d6bd}Old Págos{/color} are weirdly quiet. They were supposed to drop two wagons of rocks at my place. Can you check on them? Just find out if they’re fine.”
                \n\nYou mention the payment. “It won’t take much work from a rider. You can get there and back in less than a day, just ride west of here until the road takes you south, to the crossroads. Turn west again, and you’ll find the village. I’ll give you, let’s say, a dragon bone?”
                \n\nYou say that it’s not much, but she waves it off. “A roadwarden should get familiar with all the villages anyway, right? Just do it when you have a chance. I’ll have more coins for you once you prove you can be trusted with the simpler tasks.”
                '
                '“What can you tell me about {color=#f6d6bd}Old Págos{/color}?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Old Págos{/color}?”')
                    $ description_oldpagos01 = "A western village settled on barren soil. The locals exchange the stones from their quarries for supplies."
                    $ description_oldpagos02 = "It’s connected strongly with the nearby Order of Truth."
                    $ description_oldpagos06 = "It may be one of the oldest settlements in the North."
                    $ description_oldpagos08 = "According to {color=#f6d6bd}Foggy{/color}, “they don’t look kindly on those who don’t follow the Orders of Truth”, but “are true believers” and “fine folks”."
                    menu:
                        '“It may be one of the oldest villages in the North, but even if not, it’s safe, with strong walls and safe roads. Their crops are weak, but for generations now they’ve been cutting stone and building for other tribes in exchange for supplies. Some time ago they tied themselves to the monks, and now they don’t look kindly on those who don’t follow the Orders of Truth,” she pauses, twisting her lips to one side, choosing her words carefully, “but they’re plenty fine folks. True believers. Something lost in the city. Not ones to deal in slave trading and pillage.”
                        '
                        '“I bring news from {color=#f6d6bd}Old Págos{/color}. They’re not good.”' if oldpagos_plague_known:
                            jump foggylakeregularquestionsjob102
                        '“I’ll let you know if I learn anything.”' if not oldpagos_plague_known:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if I learn anything.”')
                            jump foggylakefoggyafterinteraction01
                '“I bring news from {color=#f6d6bd}Old Págos{/color}. They’re not good.”' if oldpagos_plague_known:
                    jump foggylakeregularquestionsjob102
                '“I’ll let you know if I learn anything.”' if not oldpagos_plague_known:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know if I learn anything.”')
                    jump foggylakefoggyafterinteraction01

        label foggylakeregularquestionsjob102:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news from {color=#f6d6bd}Old Págos{/color}. They’re not good.”')
            $ foggy_about_plague = 1
            $ oldpagos_plague_warnedplaces += 1
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            $ foggy_friendship += 1
            if quest_foggy1oldpagos:
                $ quest_foggy1oldpagos = 2
                $ quest_foggy1oldpagos_description01 = "I collected my reward."
                show screen notifyimage( "Quest completed: Check on Old Págos.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Old Págos. +1 {image=cointest}{/i}')
                $ coins += 1
                menu:
                    'Listening to your tale, she rubs her forehead. “Well, not what I was hoping to hear, love, but I’m glad you went there. Better warn the other settlements, folks should know before they send their own messengers. It’s going to be a rough few seasons for all of us.”
                    \n\nShe pulls out a dragon bone from her pocket and tosses it in your direction. “Here. Good job.” She steps toward the ajar door and looks at the lake.
                    '
                    '(preset foggy1)':
                        pass
            else:
                $ quest_foggy1oldpagos = 2
                $ quest_foggy1oldpagos_description01 = "I brought the news to {color=#f6d6bd}Foggy{/color}."
                menu:
                    '“Well, shit. I was ‘bout to ask you to check on them.” Listening to your tale, she rubs her forehead. “Well, not what I was hoping to hear, love, but I’m glad you went there. Better warn the other settlements, folks should know before they send their own messengers. It’s going to be a rough few seasons for all of us.”
                    '
                    '(preset foggy1)':
                        pass

    label foggylakeregularquestionsjob201ALL:
        label foggylakeregularquestionsjob201a:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Want me to do anything else?”')
            $ foggy_about_job = 2
            if foggy_friendship < 5:
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'She scratches the stump of her missing arm. Her powerful voice carries a hint of a threat. “I need a soul who can handle a delicate task. And I’m not sure it’s you, dear.”
                    '
                    '(preset foggy1)':
                        pass
            else:
                $ iason_name = "Iason"
                menu:
                    '“Very much so. I have a message to {color=#f6d6bd}Iason{/color}, the innkeeper of {color=#f6d6bd}Pelt of the North{/color}. His place is in the far South, a huge bother for us to get there. A bother worth, let’s say, three dragons.”
                    \n\nShe sits down on a stool and looks you in the eyes. The scars and wrinkles on her thoughtful face could belong to a statue. “Tell him, {i}are we still trading? I’m running out of patience{/i}. Remember it well, aye? Bring me the answer, only then you’ll get paid.”
                    '
                    '“It may be better for you to tell me what this is all about.”' if not foggy_about_detailsofquest2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to tell me what this is all about.”')
                        jump foggylakeregularquestionsjob201details01
                    '“You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”' if not foggy_quest_iason_bonustimer and not peltnorth_ban_perm:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”')
                        jump foggylakeregularquestionsjob201details02
                    '“Tell me about {color=#f6d6bd}Pelt{/color}.”' if not foggy_about_peltnorth:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Pelt{/color}.”')
                        jump foggylakeregularquestionsjob201details03
                    '“I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”' if peltnorth_ban_perm:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”')
                        jump foggylakeregularquestionsjob203ALT
                    '“I’ll do it.”' if not peltnorth_ban_perm:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do it.”')
                        $ quest_foggy2iason = 1
                        $ renpy.notify("New entry: Check on Iason")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Iason{/i}')
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            'She just nods.
                            '
                            '(preset foggy1)':
                                pass
        label foggylakeregularquestionsjob201details01:
            $ foggy_about_detailsofquest2 = 1
            $ foggy_quest_iason_trade = 1
            $ description_iason06 = "He was planning to purchase the {color=#f6d6bd}Foggy Lake{/color} tavern."
            menu:
                'She frowns. “I don’t ask you to negotiate in my name... Though I guess it won’t hurt to tell you. {color=#f6d6bd}Iason{/color} and I were thinking ‘bout working together. He’d invest in my place, and would get his share of profits in the future, and a shelter for his hunters. He was meant to send me the first pouch of dragons, but has fallen silent. I want to know where we stand.”
                '
                '“It may be better for you to tell me what this is all about.”' if not foggy_about_detailsofquest2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to tell me what this is all about.”')
                    jump foggylakeregularquestionsjob201details01
                '“You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”' if not foggy_quest_iason_bonustimer and not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”')
                    jump foggylakeregularquestionsjob201details02
                '“Tell me about {color=#f6d6bd}Pelt{/color}.”' if not foggy_about_peltnorth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Pelt{/color}.”')
                    jump foggylakeregularquestionsjob201details03
                '“I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”' if peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”')
                    jump foggylakeregularquestionsjob203ALT
                '“I’ll do it.”' if not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do it.”')
                    $ quest_foggy2iason = 1
                    $ renpy.notify("New entry: Check on Iason")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Iason{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She just nods.
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob201details02:
            if quarters <= world_daylength-12:
                $ custom1 = "tomorrow"
                $ foggy_quest_iason_bonustimer = (day+1)
            else:
                $ custom1 = "in two days"
                $ foggy_quest_iason_bonustimer = (day+2)
            menu:
                'She waves her hand. “Riding around, talking with folks, isn’t that hwat you’re meant to do anyway? But fine. Bring me the answer [custom1] and I’ll add a dragon to the pile.”
                '
                '“It may be better for you to tell me what this is all about.”' if not foggy_about_detailsofquest2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to tell me what this is all about.”')
                    jump foggylakeregularquestionsjob201details01
                '“You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”' if not foggy_quest_iason_bonustimer and not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”')
                    jump foggylakeregularquestionsjob201details02
                '“Tell me about {color=#f6d6bd}Pelt{/color}.”' if not foggy_about_peltnorth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Pelt{/color}.”')
                    jump foggylakeregularquestionsjob201details03
                '“I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”' if peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”')
                    jump foggylakeregularquestionsjob203ALT
                '“I’ll do it.”' if not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do it.”')
                    $ quest_foggy2iason = 1
                    $ renpy.notify("New entry: Check on Iason")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Iason{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She just nods.
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob201details03:
            $ foggy_about_peltnorth = 1
            $ description_iason02 = "The leader of a team of big-game hunters."
            $ description_iason02a = "He arrived here more than ten years ago."
            $ iason_name = "Iason"
            $ description_bighunters01 = "They are led by "
            $ description_bighunters04 = "They arrived here about ten years ago."
            $ description_bighunters05 = "According to {color=#f6d6bd}Foggy{/color}, “they can be a lot of fun if he’s not around.”"
            menu:
                '“It’s placed in what used to be an outpost of dragon hunters. Older than mine, but finely renewed. Far away, near the pass that leads through {color=#f6d6bd}Hag Hills{/color}. An inn, so you can rest there, or buy yourself some food. {color=#f6d6bd}Iason{/color}, the innkeeper, leads a group of {color=#f6d6bd}big game hunters{/color}, though when they’re together, he’s like a cloud above them. Otherwise, they can be a lot of fun. They haven’t been here long, must be not much more than ten years, and they mostly keep to themselves.”
                '
                '“It may be better for you to tell me what this is all about.”' if not foggy_about_detailsofquest2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to tell me what this is all about.”')
                    jump foggylakeregularquestionsjob201details01
                '“You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”' if not foggy_quest_iason_bonustimer and not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”')
                    jump foggylakeregularquestionsjob201details02
                '“Tell me about {color=#f6d6bd}Pelt{/color}.”' if not foggy_about_peltnorth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Pelt{/color}.”')
                    jump foggylakeregularquestionsjob201details03
                '“I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”' if peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”')
                    jump foggylakeregularquestionsjob203ALT
                '“I’ll do it.”' if not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do it.”')
                    $ quest_foggy2iason = 1
                    $ renpy.notify("New entry: Check on Iason")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Iason{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She just nods.
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob201b:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So. The next job.”')
            $ iason_name = "Iason"
            menu:
                '“Still interested? I have a message to {color=#f6d6bd}Iason{/color}, the innkeeper of {color=#f6d6bd}Pelt of the North{/color}. His place is in the far South, a huge bother for us to get there. A bother worth, let’s say, three dragons.”
                \n\nShe sits down on a stool and looks you in the eyes. The scars and wrinkles on her thoughtful face could belong to a statue. “Tell him, {i}are we still trading? I’m running out of patience{/i}. Remember it well, aye? Bring me the answer, only then you’ll get paid.”
                '
                '“It may be better for you to tell me what this is all about.”' if not foggy_about_detailsofquest2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to tell me what this is all about.”')
                    jump foggylakeregularquestionsjob201details01
                '“You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”' if not foggy_quest_iason_bonustimer and not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t pay me well enough, {color=#f6d6bd}Foggy{/color}.”')
                    jump foggylakeregularquestionsjob201details02
                '“Tell me about {color=#f6d6bd}Pelt{/color}.”' if not foggy_about_peltnorth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Pelt{/color}.”')
                    jump foggylakeregularquestionsjob201details03
                '“I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”' if peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t deliver this message, {color=#f6d6bd}Foggy{/color}. They won’t let me in.”')
                    jump foggylakeregularquestionsjob203ALT
                '“I’ll do it.”' if not peltnorth_ban_perm:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll do it.”')
                    $ quest_foggy2iason = 1
                    $ renpy.notify("New entry: Check on Iason")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Check on Iason{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She just nods.
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob202:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had a talk with {color=#f6d6bd}Iason{/color}.”')
            $ foggy_friendship += 1
            menu:
                'She encourages you with a smile. “And hwat did he say, love?”
                '
                '(lie) I cover up for him.' if quest_foggy2iason_description02 or quest_foggy2iason_description02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I cover up for him.')
                    $ foggy_quest_iason_relationship = "liedto"
                    $ quest_foggy2iason_description03 = "I lied to {color=#f6d6bd}Foggy{/color}. I collected my reward."
                    $ pc_lies += 1
                    if day <= foggy_quest_iason_bonustimer:
                        $ coins += 4
                        $ custom1 = "Three for the job, one for finishing it in fine time."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+4", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+4 {image=cointest}{/i}')
                    elif not foggy_quest_iason_bonustimer:
                        $ coins += 3
                        $ custom1 = "Here are your dragons."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    else:
                        $ coins += 3
                        $ custom1 = "Here, three dragons. It took you a while."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'After your tale, she scratches her knee. “So you’re saying {color=#f6d6bd}Asterion{/color} is to blame... Fine. Though I’d rather hear ‘bout it from the hunters themselves, without waiting for them to wake up. Thanks,” she pats your shoulder. “That’s a big help.”
                        \n\nShe hands you the cold pieces of bone. “[custom1]”
                        '
                        '(preset foggy1)':
                            pass
                'I tell her that the deal is off.' if not quest_foggy2iason_description02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her the truth.')
                    $ foggy_quest_iason_relationship = "neutral"
                    $ quest_foggy2iason_description04 = "I brought {color=#f6d6bd}Foggy{/color} her answer. I collected my reward."
                    if day <= foggy_quest_iason_bonustimer:
                        $ coins += 4
                        $ custom1 = "Three for the job, one for finishing it in fine time."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+4", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+4 {image=cointest}{/i}')
                    elif not foggy_quest_iason_bonustimer:
                        $ coins += 3
                        $ custom1 = "Here are your dragons."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    else:
                        $ coins += 3
                        $ custom1 = "Here, three dragons. It took you a while."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        '“And he made me wait for this long? With a group of fighters in that tower of his, couldn’t he be bothered to send three or four?” She soaks a cloth in the bucket of water, then slaps it on the table. A few droplets land on you. “Forgive me,” she says without conviction and turns back. Her angry look makes you lean away, but she simply hands you the cold pieces of bone. “[custom1] Thanks, dear.”
                        '
                        '(preset foggy1)':
                            pass
                'I mention that he wanted me to lie to her.' if not quest_foggy2iason_description02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I mention that he wanted me to lie to her.')
                    $ foggy_quest_iason_relationship = "mad"
                    $ quest_foggy2iason_description04 = "I told {color=#f6d6bd}Foggy{/color} the truth. I collected my reward."
                    $ foggy_friendship += 1
                    if day <= foggy_quest_iason_bonustimer:
                        $ coins += 4
                        $ custom1 = "Three for the job, one for finishing it in fine time."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+4", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+4 {image=cointest}{/i}')
                    elif not foggy_quest_iason_bonustimer:
                        $ coins += 3
                        $ custom1 = "Here are your dragons."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    else:
                        $ coins += 3
                        $ custom1 = "Here, three dragons. It took you a while."
                        $ quest_foggy2iason = 2
                        show screen notifyimage( "Quest completed: Check on Iason.\n+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason.\n+3 {image=cointest}{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She walks around the hearth like a bear in a cavern, dusting the shelves with a wet cloth. She keeps silent for a minute or two, then throws the rag into some jars, knocking them on the ground. Her loud words cover the cracking sound.
                        \n\n“So that’s how it is,” her tone remains in control. She puts her hand on your shoulder, looking into your eyes. “I appreciate your honesty, [pcname].” She hands you the cold pieces of bone. “[custom1]”
                        \n\nShe steps away, looking through the window shutters. “There will be consequences,” she announces, lowering her voice.
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob203:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t be able to deliver your message to {color=#f6d6bd}Pelt{/color}.”')
            $ renpy.notify("Quest completed: Check on Iason")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Check on Iason{/i}')
            label foggylakeregularquestionsjob203ALT:
                $ quest_foggy2iason = 3
                $ foggy_friendship -= 1
                menu:
                    'She stands still for a few heartbeats, then raises her voice. “Hwy?”
                    '
                    'I tell her the truth.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her the truth.')
                        $ foggy_friendship -=1
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ minutes += 5
                        menu:
                            'Speechless, she scratches her knee. Her voice is tired. “Such’ dumb way to turn an ally into a stranger, if not an enemy. Well, I won’t help you here.”
                            '
                            '(preset foggy1)':
                                pass
                    '...“It’s between me and them.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...“It’s between me and them.”')
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            'Even though she’s still towering over you, she sounds tired. “Fine. Forget it.”
                            '
                            '(preset foggy1)':
                                pass

    label foggylakeregularquestionsjob3ALL:
        label foggylakeregularquestionsjob301a:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me know if you have anything else for me to do.”')
            $ foggy_about_job = 3
            if foggy_about_nomoreundead:
                jump foggylakeregularquestionsjob301cancelled
            elif foggy_friendship < 8:
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'She scratches the stump of her missing arm. Her powerful voice carries a hint of a threat. “I need a soul who I know won’t steal from me. And I’m still not sure it’s you, dear.”
                    '
                    '(preset foggy1)':
                        pass
            else:
                label foggylakeregularquestionsjob301c:
                    if whitemarshes_nomoreundead or whitemarshes_destroyed or whitemarshes_attacked:
                        jump foggylakeregularquestionsjob301cancelled02
                    $ renpy.notify("You received a cask of cider.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a cask of cider.{/i}')
                    $ item_cidercask += 1
                    menu:
                        '“Aye, I’ve already prepared hwat I need you to take care of.” She nods toward a wooden cask that’s under the table. It’s not larger than your stomach. “It’s a mighty fine strong cider. Brewed it myself. The folks at {color=#f6d6bd}Hwite Marshes{/color} paid for it many days ago, it was meant to be a wedding gift. But no soul came to pick it up. Take it to them, dear. I know it’s heavy and I bet you’re not eager to go there.” She chuckles. “But three coins is going to be plenty fine for you. It’s not that far from here. Just don’t {i}lose{/i} it at a trader’s stall,” she cracks her knuckles just by making a fist. “It’s not so valuable that you’d want to sell it behind my back.”
                        \n\nYou ask who exactly is meant to receive the delivery, but she just waves her hand. “Just ask for the mayor, {color=#f6d6bd}Helvius{/color}.”
                        '
                        '“And what if they won’t take it at all? Am I to bring it back?”' if not foggy_quest_whitemarshes_details:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if they won’t take it at all? Am I to bring it back?”')
                            jump foggylakeregularquestionsjob301adetail01
                        '“Tell me about {color=#f6d6bd}White Marshes{/color}.”' if not foggy_about_whitemarshes and not foggy_about_necromancers:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}White Marshes{/color}.”')
                            jump foggylakeregularquestionsjob301adetail02
                        '“Consider it done.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Consider it done.”')
                            $ quest_foggy3whitemarshes = 1
                            $ renpy.notify("New entry: Cask of Cider")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Cask of Cider{/i}')
                            $ questionpreset = "foggy1"
                            if foggy_about_shelter == 1:
                                $ can_rest = 1
                            menu:
                                'She nods. “I will, love.”
                                '
                                '(preset foggy1)':
                                    pass
        label foggylakeregularquestionsjob301b:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, the next job.”')
            if foggy_about_nomoreundead:
                jump foggylakeregularquestionsjob301cancelled
            jump foggylakeregularquestionsjob301c
        label foggylakeregularquestionsjob301adetail01:
            $ foggy_quest_whitemarshes_details = 1
            menu:
                '“Hwy wouldn’t they?” She waves it off. “But aye, let me know ‘bout it. I can sell it back to you for a good price.”
                '
                '“And what if they won’t take it at all? Am I to bring it back?”' if not foggy_quest_whitemarshes_details:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if they won’t take it at all? Am I to bring it back?”')
                    jump foggylakeregularquestionsjob301adetail01
                '“Tell me about {color=#f6d6bd}White Marshes{/color}.”' if not foggy_about_whitemarshes and not foggy_about_necromancers:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}White Marshes{/color}.”')
                    jump foggylakeregularquestionsjob301adetail02
                '“Consider it done.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Consider it done.”')
                    $ quest_foggy3whitemarshes = 1
                    $ renpy.notify("New entry: Cask of Cider")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Cask of Cider{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She nods. “I will, love.”
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob301adetail02:
            $ foggy_about_whitemarshes = 1
            $ foggy_about_necromancers = 1
            $ description_whitemarshes05 = "I heard that the locals had to stop selling their lumber because {color=#f6d6bd}Howler’s Dell{/color} started offering their own supplies for much better prices. Because of that, the village fell into poverty."
            $ description_orentius06 = "According to {color=#f6d6bd}Foggy{/color}: “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”"
            menu:
                '“It’s an old village, placed among the bogs in the west. Not so far from here, but the road there leads around the woods, so it takes a good hwile.” She rubs her chin. “I’m sure you already know ‘bout the awoken. I don’t like what the folks there are doing, not one bit, but I can’t blame them. They struggle, and they don’t know how to protect their kids, their elders. {color=#f6d6bd}Orentius{/color}, their priest...” She cracks her shoulders. “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”
                \n\nShe opens the door with a wave of her hand, letting in some fresh air. She looks at the lake. “They used to trade in lumber, those from {color=#f6d6bd}Marshes{/color}, until {color=#f6d6bd}Howler’s Dell{/color} started selling their own trees for better prices. The trade to {color=#f6d6bd}Marshes{/color} died, and so came the hunger.” She looks at you with an unclear grimace on her lips. “You may judge them, but at least their preacher gave them hope, even if it’s tied to black magic.”
                '
                '“And what if they won’t take it at all? Am I to bring it back?”' if not foggy_quest_whitemarshes_details:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what if they won’t take it at all? Am I to bring it back?”')
                    jump foggylakeregularquestionsjob301adetail01
                '“Tell me about {color=#f6d6bd}White Marshes{/color}.”' if not foggy_about_whitemarshes and not foggy_about_necromancers:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}White Marshes{/color}.”')
                    jump foggylakeregularquestionsjob301adetail02
                '“Consider it done.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Consider it done.”')
                    $ quest_foggy3whitemarshes = 1
                    $ renpy.notify("New entry: Cask of Cider")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Cask of Cider{/i}')
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    menu:
                        'She nods. “I will, love.”
                        '
                        '(preset foggy1)':
                            pass
        label foggylakeregularquestionsjob302:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I took care of the cask with cider.”')
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            menu:
                'She pats your back with her huge hand and leads you toward the three coins lying on the table. “And hwat happened to it, dear?”
                '
                '“{color=#f6d6bd}Helvius{/color} was afraid to take it, but I left it with the warlock, {color=#f6d6bd}Thyrsus{/color}.”' if quest_foggy3whitemarshes_description02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Helvius{/color} was afraid to take it, but I left it with the warlock, {color=#f6d6bd}Thyrsus{/color}.”')
                    $ quest_foggy3whitemarshes = 2
                    $ quest_foggy3whitemarshes_description03 = "I collected my reward."
                    $ renpy.notify("Quest completed: Cask of Cider")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Cask of Cider{/i}')
                    $ custom1 = "Fair enough! Let them handle this the way they like"
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 3
                    jump foggylakeregularquestionsjob302success01
                '(lie) “I left it with {color=#f6d6bd}Helvius{/color}, though it took some convincing.”' if not quest_foggy3whitemarshes_description02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I left it with {color=#f6d6bd}Helvius{/color}, though it took some convincing.”')
                    $ pc_lies += 1
                    $ quest_foggy3whitemarshes = 3
                    $ quest_foggy3whitemarshes_description05 = "I’ve decided to keep the cask to myself. I lied to {color=#f6d6bd}Foggy{/color} about it and received my reward."
                    $ renpy.notify("Quest completed: Cask of Cider")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Cask of Cider{/i}')
                    $ custom1 = "You could have just brought it back here"
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 3
                    jump foggylakeregularquestionsjob302success01
                '“They don’t need hard drinks anymore. You can tell your men to unpack the barrel.”' if item_cidercask:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They don’t need hard drinks anymore. You can tell your men to unpack the barrel.”')
                    $ quest_foggy3whitemarshes = 2
                    $ quest_foggy3whitemarshes_description05 = "I told the truth about it to {color=#f6d6bd}Foggy{/color} and she’s decided to break our deal."
                    $ foggy_shop_cidercask_returned = 1
                    $ item_cidercask -= 1
                    $ renpy.notify("Quest completed: Cask of Cider. You can now trade for a new item.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Cask of Cider. You can now trade for a new item.{/i}')
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 1
                    jump foggylakeregularquestionsjob302success02
            label foggylakeregularquestionsjob302success01:
                if quest_foggy1oldpagos == 2 and quest_foggy2iason == 2:
                    $ foggy_food_meals_available_free = 1
                    menu:
                        'You share a story of what it took for you to deliver the cask, causing her hearty chuckle. “[custom1],” she says with a smirk. “But I see you speak with deeds. You’ve done a lot for me, and I want you to feel welcome at {color=#f6d6bd}Foggy Lake{/color}.” She nods toward the cauldron in the middle of the room. “From now on, you don’t have to pay for the first meal you’ll eat at this place every day. I’ll always have something for you on the side.”
                        '
                        '“Thanks, {color=#f6d6bd}Foggy{/color}. I appreciate it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks, {color=#f6d6bd}Foggy{/color}. I appreciate it.”')
                            $ questionpreset = "foggy1"
                            if foggy_about_shelter == 1:
                                $ can_rest = 1
                            menu:
                                'She laughs. “But you’re plenty welcome, love. Whatever you need.”
                                '
                                '(preset foggy1)':
                                    pass
                        'I nod. “I’ll tell you if I need anything.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I’ll tell you if I need anything.”')
                            $ questionpreset = "foggy1"
                            if foggy_about_shelter == 1:
                                $ can_rest = 1
                            menu:
                                'She takes a deep breath. “Aye, do so.”
                                '
                                '(preset foggy1)':
                                    pass
                else:
                    $ coins += 1
                    show screen notifyimage( "Quest completed: Cask of Cider.\n+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Cask of Cider. +1 {image=cointest}{/i}')
                    menu:
                        'You share a story of what it took for you to deliver the cask, causing her hearty chuckle. “[custom1],” she says with a smirk. “But I see you speak with deeds. Here,” she reaches to her pocket. “One extra bone. You deserve it.”
                        '
                        '“Thanks, {color=#f6d6bd}Foggy{/color}. I appreciate it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks, {color=#f6d6bd}Foggy{/color}. I appreciate it.”')
                            $ questionpreset = "foggy1"
                            if foggy_about_shelter == 1:
                                $ can_rest = 1
                            menu:
                                'She laughs. “But you’re plenty welcome, love. Let me know if you need anything.”
                                '
                                '(preset foggy1)':
                                    pass
                        'I nod and hide the coin.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and hide the coin.')
                            $ questionpreset = "foggy1"
                            if foggy_about_shelter == 1:
                                $ can_rest = 1
                            menu:
                                'She observes you in silence.
                                '
                                '(preset foggy1)':
                                    pass
            label foggylakeregularquestionsjob302success02:
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ minutes += 5
                menu:
                    'After you describe the situation, she rubs her ear. “Well, not something I was hoping to hear. The more water drinkers there are around, the fewer coins will flow into my {color=#f6d6bd}Lake{/color}.” She wipes her hand off her stomach. “Let me know if you want to buy the cask from me. It won’t last long, maybe until the winter, but I’m sure someone will take it.”
                    '
                    '(preset foggy1)':
                        pass

            label foggylakeregularquestionsjob301cancelled:
                $ foggy_about_whitemarshes_cancelled = 1
                $ quest_foggy3whitemarshes = 4
                $ renpy.notify("You can now trade for a new item.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ minutes += 5
                menu:
                    'She sighs and nods toward a wooden cask that’s under the table. It’s not larger than your stomach. “I was planning to ask you to take it to {color=#f6d6bd}Hwite Marshes{/color}, but I guess that won’t happen now. It’s a mighty fine strong cider. Brewed it myself. If you wish so, I can sell it to you for, well, maybe four dragons? It’s worth more, but won’t last long. Until the winter, at best. You could try selling it somewhere else.”
                    '
                    '(preset foggy1)':
                        pass

        label foggylakeregularquestionsjob301cancelled02ALL:
            label foggylakeregularquestionsjob301cancelled02:
                $ quest_foggy3whitemarshes = 4
                menu:
                    '“Aye, I’ve already prepared hwat I need you to take care of.” She nods toward a wooden cask that’s under the table. It’s not larger than your stomach. “It’s a mighty fine strong cider. Brewed it myself. The folks at {color=#f6d6bd}Hwite Marshes{/color} paid for it many days ago, it was meant to be a wedding gift. But no soul came to pick it up. Take it to them, dear. Ask for the mayor, {color=#f6d6bd}Helvius{/color}.”
                    '
                    '“I don’t think he’s going to speak with me.” I tell her about my meeting with {color=#f6d6bd}Orentius{/color}.' if orentius_convinced:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think he’s going to speak with me.” I tell her about my meeting with {color=#f6d6bd}Orentius{/color}.')
                        jump cidercask_foggylakeregularquesaboutnomoreundead01
                    '“I don’t think I’ll be let into the village anytime soon.” I tell her about the way we captured {color=#f6d6bd}Orentius{/color}.' if orentius_banished:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think I’ll be let into the village anytime soon.” I tell her about the way we captured {color=#f6d6bd}Orentius{/color}.')
                        jump cidercask_foggylakeregularquesaboutnomoreundead02
                    '“I’m afraid this won’t happen...”' if whitemarshes_destroyed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m afraid this won’t happen...”')
                        jump cidercask_foggylakeregularquesaboutnomoreundead03
                    '“I don’t think I’ll be let into the village anytime soon.” I tell her about the way we attacked the village.' if whitemarshes_attacked and not whitemarshes_nomoreundead:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think I’ll be let into the village anytime soon.” I tell her about the way we attacked the village.')
                        jump cidercask_foggylakeregularquesaboutnomoreundead04
            label cidercask_foggylakeregularquesaboutnomoreundead01:
                $ foggy_about_nomoreundead = 1
                $ foggy_friendship += 3
                $ quarters += 1
                if foggylake_firsttime_pcdrinks == 1 or foggylake_firsttime_pcdrinks == 2:
                    $ custom1 = "pour both of you a cup of dense mead"
                else:
                    $ custom1 = "pour herself a cup of dense mead, while you get a mug of birch sap with honey"
                menu:
                    'After you mention the end of the awoken, she bursts into laughter. “Splendid! Tell me everything, love!”
                    \n\nRight when you start, she gestures for you to sit down at the table, and uses her hand and spells to [custom1]. She listens patiently, then leans away, scratching her chin with her wrist.
                    \n\n“When I was younger, we had it easier than you do now,” her wide grin carries more charm than playfulness. “Before the war, there were all these patrols, wardens, monks... Not many folks were eager to solve their issues with force. We, adventurers, only asked for a target and the pay. No one asked us to judge human hearts. I don’t envy you,” she points at you with her cup, “trying to hold both an axe, and your wits, but I’m glad you do well with them both.”
                    '
                    'I nod and finish my drink.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and finish my drink.')
                        $ foggy_about_whitemarshes_cancelled = 1
                        $ renpy.notify("You can now trade for a new item.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ minutes += 5
                        menu:
                            '“Well, hwat I have here is a mighty fine strong cider. Brewed it myself. If you wish so, I can sell it to you for, well, maybe four dragons? It’s worth more, but won’t last long. Until the winter, at best. You could try selling it somewhere else.”
                            '
                            '(preset foggy1)':
                                pass
            label cidercask_foggylakeregularquesaboutnomoreundead02:
                $ foggy_about_nomoreundead = 1
                $ foggy_friendship += 1
                $ minutes += 5
                menu:
                    'She lets out a sigh. “How did it come to this?”
                    \n\nShe listens patiently, mixing the stew in the cauldron. “Necromancers or not, I wish them the best,” her voice is raised, yet sullen. “Maybe you had no other options, I can’t tell,” she glances at you, “but there are now even more wounds to heal. Wounds that can tear this land apart.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        $ foggy_about_whitemarshes_cancelled = 1
                        $ renpy.notify("You can now trade for a new item.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You can now trade for a new item.{/i}')
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ minutes += 5
                        menu:
                            '“Well, hwat I have here is a mighty fine strong cider. Brewed it myself. If you wish so, I can sell it to you for, well, maybe four dragons? It’s worth more, but won’t last long. Until the winter, at best. You could try selling it somewhere else.”
                            '
                            '(preset foggy1)':
                                pass
            label cidercask_foggylakeregularquesaboutnomoreundead03:
                $ foggy_about_nomoreundead = 1
                $ foggy_friendship -= 5
                $ minutes += 5
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'You start carefully, and her gaze gets unbearable. After just mention the attack of the undead, she springs to her feet, steps away, grabs a chair and throws it at the wall - its loud shatter makes {color=#f6d6bd}the foragers{/color} look inside.
                    \n\n{color=#f6d6bd}The keeper{/color} gasps for air, buried underneath the many decades she has seen. “Bring another,” she tells her son, and he obediently heads toward the trapdoor. She kicks away the chair’s leg and moves back to you. “You did this. How?”
                    \n\nYou tell her as little as you can, but she waves it all off. “Forget it. I’d rather listen to one of your victims, if there are any left.”
                    '
                    '(foggy1 set)':
                        pass
            label cidercask_foggylakeregularquesaboutnomoreundead04:
                $ foggy_about_nomoreundead = 4
                $ foggy_friendship -= 1
                $ minutes += 5
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'She lets out a sigh. “How did it come to this?”
                    \n\nShe listens patiently, mixing the stew in the cauldron. “Necromancers or not, I wish them the best,” her voice is raised, yet sullen. “Maybe you had no other options, I can’t tell,” she glances at you, “but there are now even more wounds to heal. Wounds that can tear this land apart.”
                    '
                    '(foggy1 set)':
                        pass

        label foggylakeregularquestionsjob301cancelled02ALT:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the cider...”')
            $ quest_foggy3whitemarshes = 3
            $ renpy.notify("Quest completed: Cask of Cider")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Cask of Cider{/i}')
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            menu:
                'She waves her hand. “Yeah, I know. Hwatever happened to it, doesn’t matter now.”
                '
                '(foggy1 set)':
                    pass

label foggylakeallpersonalquestions:
    label foggylakeregularquestionspersonalquestions01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about your tavern.”')
        $ foggy_about_personalquestions = 1
        if (foggy_friendship+appearance_charisma) < 5:
            $ questionpreset = "foggy1"
            if foggy_about_shelter == 1:
                $ can_rest = 1
            menu:
                'Her fingers tap on her chest loudly. “Nah. I find no pleasure in talks that serve no reason.”
                '
                '(preset foggy1)':
                    pass
        else:
            $ questionpreset = "foggy2"
            menu:
                '“Hwat burdens your soul?”
                '
                '(preset foggy2)':
                    pass

    label foggylakepersonalquestionsaboutthetavern01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s the story behind this place? It can’t be more than a few years old.”')
        $ minutes += 5
        $ foggy_about_hertavern = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = ""
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She observes the mead in her cup."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "As she observes the mead in her cup, you reach for your meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "As she observes the mead in her cup, you reach for a snack."
        else: # nic nie ma
            $ custom1 = ""
        menu:
            '“It’s our third summer under the roof of {color=#f6d6bd}Foggy Lake{/color}, but the palisade is older. Used to be a camping spot for the bird catchers from {color=#f6d6bd}Creeks{/color}, and there are fish here that don’t swim in our streams. When we were but newcomers in the North these lands were hard to bend, but the beasts got used to us with time.” A melancholy crawls into her eyes. [custom1]
            \n\n“Every year or so we added something new. The rocks for a campfire, some stools, a fence, a firewood shed, a boat. At one point we brought the lumber from {color=#f6d6bd}Hwite Marshes{/color} and built a cabin, like the one at the eastern road. More folks started resting here, even traders from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Old Págos{/color}. A plenty fine spot for an inn, aye?”
            \n\nHer smile is warm. “I’m building my home from nothing, you could say, and not for the first time. How ‘bout you? Does any of it sound tempting?”
            '
            '“That’s the dream. A place far away from {color=#f6d6bd}Hovlavan{/color}, somewhere where I can rest after a day of work without an aching back.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the dream. A place far away from {color=#f6d6bd}Hovlavan{/color}, somewhere where I can rest after a day of work without an aching back.”')
                $ questionpreset = "foggy2"
                menu:
                    '“You speak my own words, love, my own words. We have a good home here, in the North. Not a safe one, not a fun one. But there’s plenty of food, and plenty of things to build. I’m already luckier than most.” She looks at the place where her missing arm used to be.
                    '
                    '(preset foggy2)':
                        pass
            '“My home is wherever I can find kind people.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My home is wherever I can find kind people.”')
                $ questionpreset = "foggy2"
                menu:
                    'She chuckles. “You can always find {i}some{/i} folks who are {i}somehwat{/i} kind {i}some{/i} of the time. But all of them have their limits or bad days. Without a place to return to, you’re missing out on souls and their stories.” She looks you in the eyes with motherly concern. “Or who knows. Maybe you’re different.”
                    '
                    '(preset foggy2)':
                        pass
            '“That’s something I can ask myself after I’ve saved some dragon bones.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s something I can ask myself after I’ve saved some dragon bones.”')
                $ questionpreset = "foggy2"
                menu:
                    '“I used to be like that, waiting with decisions until I had no other option. But when nights are colder, it’s good to think you’re getting closer to your goal, to something you can name.” Her eyes turn absent.
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsaboutbeastsaround01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you stay safe from the beasts? You’re completely open from the lake.”')
        $ minutes += 5
        $ foggy_about_beastsaround = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = ""
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = " and takes another sip"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = " and takes another sip"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = " and reaches for a dried plum"
        else: # nic nie ma
            $ custom1 = ""
        menu:
            '“Quick legs, love!” Her brief, yet thunderous laughter makes you flinch. “We don’t leave any food outside, but our cauldron smells. Every now and then something scary shows up. We lock ourselves in here, for days, if we have to. Our windows help us keep an eye on the yard. Better that than leaving the hamlet to goblins.”
            \n\nYou mention that having no wall from the lake side is quite a risk. She nods in agreement[custom1]. “We don’t bring children and old folks around, but this part of the peninsula is not so bad, at least in sunlight. Not much food growing or running around, unless you can live on fish and birds. And the folks of {color=#f6d6bd}Creeks{/color} are great hunters, the greatest around. But isn’t there a harbor in the city as well? How d’you keep the creatures away?”
            '
            '“They’re used to avoiding {color=#f6d6bd}Hovlavan{/color}. The guards and sailors make it too dangerous for them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They’re used to avoiding {color=#f6d6bd}Hovlavan{/color}. The guards and sailors make it too dangerous for them.”')
                $ questionpreset = "foggy2"
                $ bestiary_seamonsters_city = "creaturesstayaway"
                menu:
                    '“See, that’s what I hope for. With enough time and crossbows, walls can only get safer. I just have to play it smart, and take some risks. So far, it’s working.”
                    '
                    '(preset foggy2)':
                        pass
            '“They mostly stay in the water, waiting for trash or drunkards to fall off of a bridge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They mostly stay in the water, waiting for trash or drunkards to fall off of a bridge.”')
                $ questionpreset = "foggy2"
                $ bestiary_seamonsters_city = "creaturesattackdrunkards"
                menu:
                    '“Chilling! One day we had such’ thing here, during our first summer. Two adventurers got drunk and went to watch the lake after dark. {i}We’ll hide if anything shows up{/i}, they were saying. In the morning, the water was red, and their rags were covering the rocks.”
                    '
                    '(preset foggy2)':
                        pass
            '“Every now and then, something large shows up between the boats, or even enters the streets. People learn to run away and leave it to the soldiers, but from time to time there are casualties.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every now and then, something large shows up between the boats. People learn to run away and leave it to the soldiers.”')
                $ questionpreset = "foggy2"
                $ bestiary_seamonsters_city = "creaturesgetontheland"
                menu:
                    'She asks you to tell her more, then taps her chin. “Still safer than living in villages, I’d say. Every other season a hunter or a farmer lands on a pyre, or disappears into the fogs. But... A place of this size should have a way to stay stronger. I lived in the capital before the invasion. Having things in such’ state would make folks revolt.”
                    '
                    '(preset foggy2)':
                        pass
            '“It’s actually the flying beasts that bother us.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s actually the flying beasts that bother us.”')
                $ questionpreset = "foggy2"
                $ bestiary_seamonsters_city = "flyingmonsters"
                menu:
                    'You describe the harpies and other creatures, and how the cityfolk do their chores with spears by their side. “The kids are told to stay inside unless they’re supervised,” you finish your tale.
                    \n\n{color=#f6d6bd}Foggy{/color} gives you a long look. “So that’s how the cities are when there’s no iron for bolts and crossbows. I now wonder hwat the capital looks like. I mean, it’s not that important anymore. Not without the emperors.”
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsabouthunting01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting beasts you hunt for?”')
        $ foggy_about_hunting = 1
        menu:
            '“Oh, {i}I{/i} hunt for nothing,” she smirks. “Not since I lost my arm. And the boys outside are not made for it either. They’ve no drive to fight, you see, and grew up to be wimps. They sometimes club down a hare, but we’re all ‘bout foraging and bird traps now.”
            \n\n“The folks in {color=#f6d6bd}Creeks{/color} do the real hunting,” she adds after a pause. “Runners, mouflons, rats, sometimes a buffalo or a saurian. We have no soil for fields, so game meat is all we have left.”
            \n\nShe stretches out, getting even taller. “D’you hunt often?”
            '
            '“If I’m about to starve. I don’t enjoy killing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If I’m about to starve. I don’t enjoy killing.”')
                $ questionpreset = "foggy2"
                menu:
                    '“You’ve picked a rough trade for yourself, then. I used to like it. Hunting, sure, but even more so crushing the undead. I even cut down a few bandits for a good pay. But now, when my dumb ape of a son goes on a longer trip, my heart pounds like a hammer.” She thuds her clenched fist against her chest. “I couldn’t go on like this. Bandits also have mothers, aye?”
                    '
                    '(preset foggy2)':
                        pass
            '“Sometimes I set up traps. I don’t risk facing big game.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sometimes I set up traps. I don’t risk facing big game.”')
                $ questionpreset = "foggy2"
                menu:
                    '“That’s hardly a hunt, is it?” She leans forward, chuckling. “Picking up a dead bird from a loop is not the same as pushing away a warm corpse that was just pinning you down to the ground.” She looks toward the open window shutters. “Not the same... But probably smarter. A friend of mine was a {i}real{/i} huntress. For a year or so.”
                    '
                    '(preset foggy2)':
                        pass
            '“In {color=#f6d6bd}Hovlavan{/color} you won’t find much game aside from rats and pigeons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In {color=#f6d6bd}Hovlavan{/color} you won’t find much game aside from rats and pigeons.”')
                $ questionpreset = "foggy2"
                menu:
                    '“It used to be the same in the capital. Kids taught one another how to hit them with rocks. And we still eat those around here. Not much glory in easy kills, but they’re better than bark.”
                    '
                    '(preset foggy2)':
                        pass
            '“I do. Making a monster bleed makes me feel alive.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I do. Making a monster bleed makes me feel alive.”')
                $ questionpreset = "foggy2"
                menu:
                    'She laughs. “I used to be the same. I loved the hunts, sure, but even more so crushing the undead. I even cut down a few bandits for a good pay. But now, when my dumb ape of a son goes on a longer trip, my heart pounds like a hammer.” She thuds her clenched fist against her chest. “I couldn’t go on like this. Bandits also have mothers, aye?”
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsaboutherself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What brought you North? You don’t look like someone who planned to spend their life cleaning tables.”')
        $ minutes += 5
        $ foggy_about_herself = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = "she leans back and relaxes, smiling"
                $ custom2 = "Her eyes are absent."
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "she leans forward and takes another look at her bottle, sealing it with an approving nod"
                $ custom2 = "She smells the mead in her cup, but doesn’t take a sip."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "she leans forward and takes another look at her bottle, sealing it with an approving nod"
                $ custom2 = "She looks at your bowl, lost in her thoughts."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "she leans forward and takes another look at her bottle, sealing it with an approving nod"
                $ custom2 = "She smells the mead in her cup, but doesn’t take a sip."
        else: # nic nie ma
            $ custom1 = "she leans back and relaxes, smiling"
            $ custom2 = "Her eyes are absent."
        $ questionpreset = "foggy2"
        menu:
            '“Once you burn enough dead friends and relatives, clean tables start to look plenty tempting,” [custom1]. “My ma and pa were both big, big and strong. One time, they saw me sitting on this kid, twisting his arm, so they started to teach me. Staff duels, running, lifting barrels and rocks. Thankfully, the army chieftain said I wasn’t {i}disciplined{/i} enough.” She rubs the scars on her forehead. “So I did a lot of things. Escorted some merchants, joined a group of adventurers, hunted for bounties, guarded a village temple,” the last memory makes her voice gloomy. “Not all of these things make me proud of myself.”
            \n\n[custom2] “I moved here only after I lost my arm, when the folks were fleeing the invasion. I took my {color=#f6d6bd}Ilan{/color}, a casket of dragons, and joined a more organized group. Arm or not, I still have a fierce punch,” she lets out a pleased grunt, “I was worth keeping around.”
            \n\nHer voice can’t hide that she’s delighted to carry on with her tale. “Now that the years are catching up with me, and even more so with my back, I need to build myself a decent shelter. I crave no adventures, but I’m happy to hear stories from other restless souls. In the meantime, I’ll practice this li’l trick.” She points at the cauldron in the middle of the room and starts to make circles with her finger. The ladle mimics the movement, mixing the stew for another minute or two. “That’s also good for my back.”
            '
            '(preset foggy2)':
                pass

    label foggylakepersonalquestionsaboutthename01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your name’s {color=#f6d6bd}Foggy{/color}, and this is {color=#f6d6bd}Foggy Lake{/color}... Is the tavern named after you, or after the lake?”')
        $ foggy_about_thename = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = "she playfully raises her chin. Her voice is warm."
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "she moves her cup away and leans forward, resting her elbow on the table. Her voice is playful, warm."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "she moves her cup away and leans forward, resting her elbow on the table. Her voice is playful, warm."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "she moves her cup away and leans forward, resting her elbow on the table. Her voice is playful, warm."
        else: # nic nie ma
            $ custom1 = "she playfully raises her chin. Her voice is warm."
        menu:
            '“Ah, the lake has no name,” [custom1] “{i}Yet{/i}, I mean. But there will be stories ‘bout this place, believe me, and ‘bout passing by the lake hwile getting to {color=#f6d6bd}Foggy’s{/color}. I may not be a dragonslayer or a holy woman, but one way or another, my soul will live on in my name, tied to these walls.” She looks at you in silence, then bursts into laughter. You could swear she makes the jars shake. “I’m plenty fine being vain.”
            '
            '“We all want to be remembered, I think.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We all want to be remembered, I think.”')
                $ questionpreset = "foggy2"
                menu:
                    '“My pa used to say memories of ours live in the blood of our children. But guess hwat, kids die as well. All my brothers and sisters, gone.” She pauses, but there’s no sadness in her eyes. “Stories have a better reach, aye? We can tell each other ‘bout strangers who lived centuries ago. There’s {i}magic{/i} in that.”
                    '
                    '(preset foggy2)':
                        pass
            '“Not everything that’s {i}vain{/i} is {i}wrong{/i}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not everything that’s {i}vain{/i} is {i}wrong{/i}.”')
                $ questionpreset = "foggy2"
                menu:
                    'She observes you in silence, then lets out a chuckle. “Very true! Eating tidbits may be dumb, but, in fair shares, keeps our souls stronger.”
                    '
                    '(preset foggy2)':
                        pass
            '“It’s probably better to stay humble.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s probably better to stay humble.”')
                $ questionpreset = "foggy2"
                $ foggy_friendship -= 1
                menu:
                    '“Better for whom, I wonder? For my {i}eternal soul{/i}? For the empress? For priests who used to chain slaves to the altars? All I have and care ‘bout is my family, here and in {color=#f6d6bd}Creeks{/color}. Other than that, I just want to be happy.”
                    '
                    '(preset foggy2)':
                        pass
            'I just smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile.')
                $ questionpreset = "foggy2"
                menu:
                    'After an awkward pause, {color=#f6d6bd}Foggy{/color} smiles back at you.
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsaboutherarm01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod toward the spot where her right arm should be. “Any story there?”')
        $ foggy_about_herarm = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = "Her wink turns into an awkward blink."
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She grabs her cup. Her wink turns into an awkward blink."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "She grabs her cup. Her wink turns into an awkward blink."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She grabs her cup. Her wink turns into an awkward blink."
        else: # nic nie ma
            $ custom1 = "Her wink turns into an awkward blink."
        $ questionpreset = "foggy2"
        menu:
            'She leans back, moving her shoulders and chest up and down as if she’s having a soundless chuckle. “Not one I’m going to share with a newcomer, dear. Stay alive until next autumn, I’ll open a cask of cold cider and tell you quite a tale. It has treason, treasure, monsters, and dark spells. But I’m way too sober for it now.” [custom1]
            '
            '(preset foggy2)':
                pass

    label foggylakepersonalquestionsabouthermagic01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... You can move things with your thoughts.”')
        $ foggy_about_hermagic = 1
        menu:
            'She chuckles. “Hwy, can’t you?”
            '
            '“I know some tricks, but not that one.” I tell her about my amulets.' if pc_class == "mage":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know some tricks, but not that one.” I tell her about my amulets.')
                $ questionpreset = "foggy2"
                $ foggy_friendship += 1
                $ quarters += 1
                if not foggylake_firsttime_afterdrink:
                    if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                        $ custom1 = "She examines her fingernails. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom1 = "She examines her cup."
                else: # nic nie ma
                    $ custom1 = "She examines her fingernails."
                menu:
                    'She pays great attention to the ways you’ve obtained your talismans and how they affect your spellcasting. “In my family, it was nothing like that,” she says after a good couple of minutes. “My grandparents used to be great mages, but not great enough to survive The Plague.” Her scarred lips form a grimace. “And my ma got no talent from them. After a year of training, she was hardly able to push a feather from a distance of a foot. I always knew I had a strong soul in my blood, but there was no soul there to teach me how to use it.”
                    \n\n[custom1] “Now I try to figure it out, all by myself, but without a teacher, I may not have enough summers left to become a master.”
                    '
                    '(preset foggy2)':
                        pass
            '“I don’t know much about magic.”' if pc_class != "mage":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know much about magic.”')
                $ minutes += 5
                $ questionpreset = "foggy2"
                if not foggylake_firsttime_afterdrink:
                    if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                        $ custom1 = "She examines her fingernails. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom1 = "She examines her cup."
                else: # nic nie ma
                    $ custom1 = "She examines her fingernails."
                menu:
                    '“Without a teacher, there’s not much you can do. My grandparents used to be great mages, but not great enough to survive The Plague,” her scarred lips form a grimace. “My ma got no talent from them. After a year of training, she was hardly able to move a feather by a foot. I always knew I had a strong pneuma in my blood, but there was no soul there to teach me how to use it.”
                    \n\n[custom1] “I’m trying to figure it out by myself, but I may not have enough summers left.”
                    '
                    '(preset foggy2)':
                        pass
            '(lie) “I know some tricks, but not that one.”' if pc_class != "mage":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I know some tricks, but not that one.”')
                $ minutes += 5
                $ questionpreset = "foggy2"
                $ pc_lies += 1
                if not foggylake_firsttime_afterdrink:
                    if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                        $ custom1 = "She examines her fingernails. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom1 = "She examines her cup."
                else: # nic nie ma
                    $ custom1 = "She examines her fingernails."
                menu:
                    'Seeing that you have nothing to add to this, she shrugs. “My grandparents used to be great mages, but not great enough to survive The Plague,” her scarred lips form a grimace. “My ma got no talent from them. After a year of training, she was hardly able to move a feather by a foot. I always knew I had a strong pneuma in my blood, but there was no soul there to teach me how to use it.”
                    \n\n[custom1] “I’m trying to figure it out by myself, but without a teacher, I may not have enough summers left.”
                    '
                    '(preset foggy2)':
                        pass
            '(lie) “I don’t know much about magic.”' if pc_class == "mage":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I don’t know much about magic.”')
                $ minutes += 5
                $ pc_lies += 1
                $ questionpreset = "foggy2"
                if not foggylake_firsttime_afterdrink:
                    if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                        $ custom1 = "She examines her fingernails. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom1 = "She examines her cup. The ladle stops moving."
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom1 = "She examines her cup."
                else: # nic nie ma
                    $ custom1 = "She examines her fingernails."
                menu:
                    '“Without a teacher, there’s not much you can do. My grandparents used to be great mages, but not great enough to survive The Plague,” her scarred lips form a grimace. “My ma got no talent from them. After a year of training, she was hardly able to move a feather by a foot. I always knew I had a strong pneuma in my blood, but there was no soul there to teach me how to use it.”
                    \n\n[custom1] “I’m trying to figure it out by myself, but I may not have enough summers left.”
                    '
                    '(preset foggy2)':
                        pass
            'I smile. “Now, {i}that’s{/i} a mystery.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Now, {i}that’s{/i} a mystery.”')
                $ questionpreset = "foggy2"
                menu:
                    'She chuckles. “Aye, let’s hope you won’t need to use it on your journeys... Or that winter will never come, or that wolves will cuddle with mouflons.”
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsaboutherplans01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s going to happen next? Will you build a real wall?”')
        $ minutes += 3
        $ foggy_about_herplans = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = "She nods toward you."
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She sips from her cup, looking at you."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "She sips from her cup, looking at you."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She sips from her cup, looking at you."
        else: # nic nie ma
            $ custom1 = "She nods toward you."
        if not quest_easternpath:
            $ quest_easternpath = 1
            $ quest_easternpath_description_teaser = "{color=#f6d6bd}Foggy{/color}, the keeper of the local tavern, claims that the people from {color=#f6d6bd}Creeks{/color}, a hunting village in the far North, have some issues with maintaining their roads."
            $ renpy.notify("New entry: Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Eastern Path{/i}')
        menu:
            '“Why not! Then grow my connections in the villages, buy more hard drinks, build another shed, a cabin, even, and hire a private warden for these roads, you know, for my guests...” [custom1] “But it’s all in the distant future. We, at {color=#f6d6bd}Creeks{/color}, need to take care of the eastern route, clear it for the traders. Without trade, all I have is the locals, and they don’t even {i}use{/i} dragon bones. But hwy d’you care, dear? Are you planning to stay around?”
            '
            '“At least for a few years.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “At least for a few years.”')
                $ questionpreset = "foggy2"
                $ pc_futureplans = "liveinpeninsula"
                $ foggy_friendship_tradepoints += 2
                $ creeks_reputation += 1
                menu:
                    'Her smile would suit a bear. “If you know how to use that axe of yours you’ll be more than welcomed. On this side of {color=#f6d6bd}Hag Hills{/color} we need folks who can handle themselves, no matter if they’re roadwardens, mercenaries, or guards. Just not soldiers,” she chuckles.
                    '
                    '(preset foggy2)':
                        pass
            '“I hope to spend a longer time in {color=#f6d6bd}Hovlavan{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope to spend a longer time in {color=#f6d6bd}Hovlavan{/color}.”')
                $ questionpreset = "foggy2"
                $ pc_futureplans = "stayincity"
                menu:
                    'She lets out a fake, long sigh. “Earning hwat dragons you can and returning behind the walls, are you? A smart plan, at least as smart as it goes for someone willing to even start a journey.”
                    '
                    '(preset foggy2)':
                        pass
            '“I hope to stay on the road. Visit other parts of The Dragonwoods.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope to stay on the road. Visit other parts of The Dragonwoods.”')
                $ questionpreset = "foggy2"
                $ pc_futureplans = "travel"
                menu:
                    '“Is that so? All the tales I’ve heard make me glad I now have a place of my own. The trails grow green and thorny, the villages turn empty, the cities lose their reach.” She leans forward and stares into your eyes. “If that’s really your plan, it won’t end well for you. Hwat will you do without roads?”
                    '
                    '(preset foggy2)':
                        pass
            '“I’ll see what the future brings.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see what the future brings.”')
                $ questionpreset = "foggy2"
                menu:
                    'She nods. “As we all will.”
                    '
                    '(preset foggy2)':
                        pass

    label foggylakepersonalquestionsaboutheralcohols01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You seem to be into some expensive drinks.”')
        $ minutes += 3
        $ foggy_about_alcohol = 1
        if not foggylake_firsttime_afterdrink:
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ custom1 = "She glances at the trapdoor."
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She tilts her cup."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom1 = "She tilts her cup."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She tilts her cup and grabs a purple carrot from the snack plate."
        else: # nic nie ma
            $ custom1 = "She glances at the trapdoor."
        $ questionpreset = "foggy2"
        $ description_foggy03 = "She has her own set of alchemical tools, necessary to brew ciders and distill hard drinks."
        if not foggylake_alchemytable_firsttime:
            menu:
                '“The pricey ones are gifts I received, or treasures I found when I was young. I also bought a few, aye. I like to offer something unusual to the wealthier... Or more {i}promising{/i} guests.” [custom1] “I dabbled with some recipes myself, I’ve plenty of brewing tools, though I can name maybe half of them. Still, from ales to hard drinks, I had some successes.”
                '
                '(preset foggy2)':
                    pass
        else:
            menu:
                'The pricey ones are gifts I received, or treasures I found when I was young. I also bought a few, aye. I like to offer something unusual to the wealthier... Or more {i}promising{/i} guests.” [custom1] “You saw my brewing set. I don’t even know how some of these tools work. Still, from ales to hard drinks, I had some successes.”
                '
                '(preset foggy2)':
                    pass

label foggylakefoggyafterinteraction01allpersonalquestions:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
    if (foggy_about_personalquestions_amount >= foggy_about_personalquestions_amount_max) and not foggy_about_personalquestions_inquisitive:
        $ foggy_about_personalquestions_inquisitive = 1
        $ minutes += 5
        menu:
            '“I must say, love, I rarely meet folks with that many questions,” she gives you a warm look. “Hwat hides beneath them?”
            '
            '“Nothing. Just getting to know you better.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nothing. Just getting to know you better.”')
                $ foggylake_firsttime_afterdrink = 1
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'Her scarred lips make an unclear grimace. “Words can only get you so far. You won’t {i}know{/i} someone by meeting them once every few seasons. You need to stay around, see others’ deeds, listen to their coughs and cries. Travelers don’t know folks, just stories.”
                    \n\nHer voice gets somber. “Trust my years when I say so.”
                    '
                    '(preset foggy1)':
                        pass
            '“I was hoping to learn something useful.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping to learn something useful.”')
                $ foggy_friendship += 1
                if not foggylake_firsttime_afterdrink:
                    if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                        $ custom1 = "She looks at the trapdoor with a smirk."
                    elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom1 = "She looks at your cup with a smirk."
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom1 = "She looks at her cup with a smirk."
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom1 = "She looks at her cup with a smirk."
                else: # nic nie ma
                    $ custom1 = "She looks at the trapdoor with a smirk."
                menu:
                    'She bursts into laughter. “Can’t say now if you’re more of a trader, seeking a chance hwerever they are, or one down-to-earth traveler.”
                    '
                    '“The former. All the things I learn may help me find a good opportunity.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The former. All the things I learn may help me find a good opportunity.”')
                        $ foggylake_firsttime_afterdrink = 1
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            '“Aye, some folks don’t know how to keep their mouth shut.” [custom1] “But some of us are plenty fine at it.”
                            '
                            '(preset foggy1)':
                                pass
                    '“The latter. Every scrap of knowledge may help me survive.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The latter. Every scrap of knowledge may help me survive.”')
                        $ foggylake_firsttime_afterdrink = 1
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            'She nods. “Very true, dear. Even the strongest ox needs to keep their ears clean.”
                            '
                            '(preset foggy1)':
                                pass
                    '“A little bit of both, most likely.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A little bit of both, most likely.”')
                        $ foggylake_firsttime_afterdrink = 1
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            'Her grin is worthy of a wolf. “Safety and risk don’t go hand in hand, I’d say, but I look forward to seeing your results.”
                            '
                            '(preset foggy1)':
                                pass
            '“We all need friends, don’t we?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We all need friends, don’t we?”')
                $ foggylake_firsttime_afterdrink = 1
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'She rests her hand on her stomach. “We do, but some of us need them more than the others. I’d say it’s better for me to have a peek into a roadwarden’s head. A good one could shake things up a fair bit. The bad ones... Well, they die quickly.”
                    '
                    '(preset foggy1)':
                        pass
            '“I was bored, that’s all.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was bored, that’s all.”')
                $ foggylake_firsttime_afterdrink = 1
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ foggy_friendship -= 1
                menu:
                    'Her scars bent beneath her frown. “I’d expect a roadwarden would have plenty of things to do. Don’t you know? Autumn isn’t far away.”
                    '
                    '(preset foggy1)':
                        pass
    else:
        jump foggylakefoggyafterinteraction01

################################################# RUMORS - SEARCH
label foggylakeregularquestionsrumors00ALT:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting rumors?”')
    jump foggylakeregularquestionsrumors00AFTER
    label foggylakeregularquestionsrumors00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the peninsula?”')
        jump foggylakeregularquestionsrumors00AFTER
        label foggylakeregularquestionsrumors00AFTER:
            $ foggy_about_rumors = 1
            if foggy_friendship < 0 and not foggy_about_rumors_available: # (foggy_friendship+appearance_charisma) < 3
                $ questionpreset = "foggy1"
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                menu:
                    'She frowns. “I’m not one to spread tales among strangers. First show me hwat you’re made of.”
                    '
                    '(preset foggy1)':
                        pass
            else:
                $ foggy_about_rumors_firsttime = 1
                menu:
                    'She nods. “I know this and that. Which place?”
                    '
                    '“What can you tell me about...”':
                        if not tutorial_input:
                            $ tutorial_input = 1
                        python:
                            search = renpy.input("Which place are you asking about? (example: tulias camp)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        $ tutorial_input = 2
                        jump foggylakeregularquestionsrumors02
                    '“Forget it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it.”')
                        jump foggylakefoggyafterinteraction01

label foggylakeregularquestionsrumors01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
    if not foggy_about_rumors_firsttime:
        $ foggy_about_rumors_firsttime = 1
        menu:
            'She nods. “Which place?”
            '
            '“What can you tell me about...”':
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("Which place are you asking about? (example: tulias camp)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                $ tutorial_input = 2
                jump foggylakeregularquestionsrumors02
    else:
        $ custom1 = renpy.random.choice(['“Which place, dear?”', '“Aye?”', 'She frowns.', '“Go ahead, dear.”'])
        python:
            search = renpy.input("[custom1]", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
            search = search.strip().lower().replace(" ", "")
            if not search:
                search = "no one"
        $ tutorial_input = 2
        jump foggylakeregularquestionsrumors02

label foggylakeregularquestionsrumors02:
    if search == "none" or search == "nothing" or search == "anyplace" or search == "anyplace" or search == "place" or search == "any" or search == "whatever" or search == " " or search == "":
        menu:
            '“Hwat?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag" or search == "bitch" or search == "whore" or search == "cunt":
        python:
            search = renpy.input("...Let’s try this again.", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
            search = search.strip().lower().replace(" ", "")
            if not search:
                search = "nothing"
        jump foggylakeregularquestionsrumors02
    elif search == "north" or search == "thenorth" or search == "peninsula" or search == "thissideofthehills":
        menu:
            'She raises an eyebrow. “It’s a large place, dear. You want a tale ‘bout every single tree that grows here?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "theruins" or search == "ruins" or search == "camps" or search == "thecamp" or search == "camp" or search == "village" or search == "thevillage" or search == "ruin" or search == "lake" or search == "settlement" or search == "hamlet" or search == "roads" or search == "theroad" or search == "road" or search == "roads" or search == "fishingvillage" or search == "mountainpass" or search == "forestroad" or search == "forest" or search == "forests" or search == "woods" or search == "house" or search == "thehouse" or search == "ahouse" or search == "cave" or search == "cavern" or search == "acave" or search == "acavern" or search == "astatue" or search == "thestatue" or search == "statue" or search == "bridge" or search == "river" or search == "brook" or search == "stream" or search == "creek" or search == "pond" or search == "valley" or search == "meadow" or search == "tree" or search == "trap" or search == "abandonedplace" or search == "lair" or search == "den" or search == "garden" or search == "forestgarden":
        menu:
            '“There are many places you could call that, dear.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "island" or search == "islands" or search == "theisland" or search == "anisland" or search == "aisland" or search == "anyisland" or search == "anyislands" or search == "someisland" or search == "someislands" or search == "isle" or search == "anisle" or search == "someisle":
        $ foggy_about_islands = 1
        menu:
            '“There are more of them than you can count, dear, most of them too small for a tree to take root. Strange tribes live on the larger ones, in the east and west. Here, the rocks stop any ships, boats, even. {color=#f6d6bd}High Island{/color} may be big and rich, but its volcano is too much of a threat for any settlers.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "wasteland" or search == "wastelands" or search == "thewasteland" or search == "thewastelands" or search == "southernrealm" or search == "southernrealms" or search == "thesouthernrealm" or search == "thesouthernrealms" or search == "southernrealm" or search == "southernrealms" or search == "thesouthernrealm" or search == "thesouthernrealms" or search == "southerntribe" or search == "southerntribes" or search == "thesoutherntribe" or search == "thesoutherntribes":
        menu:
            '“I never reached The Growing Mountains, even less so The Southern Realms. It’s a different world for me, but any folks from there are welcome at my place, no matter their tongue or looks. I mean, they are already among {i}our{/i} tribes, not as invaders, but as farmers and hunters. We’ve no right to bear them ill will after the emperors pillaged their lands for centuries.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "middlemountains" or search == "middlemountain" or search == "themiddlemountains" or search == "themiddlemountain" or search == "growingmountains" or search == "growingmountain" or search == "thegrowingmountains" or search == "thegrowingmountain":
        menu:
            '“I’ve never tried to reach the southern borders. Folks say the peaks there disappear into the clouds, and it takes strong lungs to cross even the gentle passes. There are tales I’ve heard in the capital and on my journeys, but no soul talks ‘bout The Growing Mountains now, not since the war. The clans stay hwere they always have been, and so does our forest.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "theland" or search == "land" or search == "continent" or search == "thiscontinent" or search == "thecontinent":
        menu:
            '“I’ve seen only a small part of it, and there are not many journeys left in these bones!” She chuckles and points at her legs. “I don’t even know how large The Land is.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "empire" or search == "theempire" or search == "ourcountry" or search == "ourempire" or search == "ourfatherland" or search == "ourmotherland" or search == "thetencities" or search == "tencities" or search == "thecities" or search == "cities":
        menu:
            'She scratches her thick neck. “I guess we’re going to keep calling this realm {i}The Ten Cities{/i}, aye? Hear my words, there’s no such place to be saved. The provinces are drifting apart, the emperors are gone, and no soul can hold the mask for long. And so be it,” she laughs, “we need no army, we need no corsairs, or pagan hunters, or tax collectors. The folks ought to rule themselves.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "ocean" or search == "theocean" or search == "sea" or search == "thesea" or search == "asea":
        menu:
            '“Not much to say ‘bout it, aye? I was never on a ship, I only know hwat I’ve seen from the shore. A lot of blue, plenty of rocks and drifting beams, and who can count all the beasts in the water and the sky. There are no joyful tales ‘bout the water. Hard to believe there are those who hope to build colonies in distant lands.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "colonies" or search == "colony" or search == "thecolonies" or search == "acolony":
        menu:
            '“You know I came here as a refugee, aye? In the days of the invasion. There were plenty of us. A half tried to settle down, the others wanted to cross the sea, join those on the other side. With the help of the locals they built a ship, imagine, but it didn’t get far. Rocks. At least the planks drifted back to the shore, so we had enough wood to burn the dead ones.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "coast" or search == "thecoast" or search == "shore" or search == "theshore" or search == "asea" or search == "beach" or search == "beaches" or search == "harbor" or search == "thebeach" or search == "abeach" or search == "beach":
        menu:
            '“The coasts here are all steep, it’s easier to break your neck falling down from a cliff than to find a beach. And the rocks are like razors, they shred ships to pieces. I only know of two places good enough for a boat. The pier in the north, behind {color=#f6d6bd}Gale Rocks{/color}, and the old fishing hamlet in the far west.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "apeale" or search == "apealeinn" or search == "apealetavern" or search == "aleape":
        menu:
            '“It’s more of an alehouse for the folks living at {color=#f6d6bd}Howler’s{/color} than a real inn. The innkeep’s prices are high, unless one’s on {color=#f6d6bd}Thais’{/color} good side.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "howlerscreek" or search == "creekofhowlersdell" or search == "creekofhowlers" or search == "howlercreek" or search == "creekofhowlers" or search == "creekofhowlersdell" or search == "thehowlerscreek":
        $ foggy_about_howlerscreek = 1
        menu:
            '“It’s this gentle stream that flows from the mountains in the west and ends up in the wetlands. There are still plenty of howlers around, screaming for any and no reason. I was told that long, long ago a young woman got lost in the forest, and started to {i}sing{/i} with the monkeys. They heard their words in her voice, and took care of her. She then made a hut by the creek, and became the mother of {color=#f6d6bd}Howler’s Dell{/color}. Don’t ask me,” she shrugs. “The druids have some wild dreams.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "capital" or search == "capitalcity" or search == "thecapital" or search == "thecapitaloftheempire" or search == "thecapitalofthetencities" or search == "thecapitaloftencities" or search == "themaincity":
        menu:
            'She hits her chest with her fist. “Aye, that’s hwere I was born and raised, though I may not sound like it any more. I wanted my {color=#f6d6bd}Ilan{/color} to speak like a boy from here, so I’ve practiced my tongue,” her sullen eyes betray her chuckle. “My ma and pa weren’t poor, so I had it easier than the other kids, but I don’t have many fond memories of the place. The slaves and beggars had to give way to rich pricks and cunts, unless they wanted to end up in the gutter, with their noses broken.” A long pause. “I wanted to leave it even before the war. Such places hold you in chains, take away your breath.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "city" or search == "thecity" or search == "acity" or search == "hovlavan" or search == "thehovlavan" or search == "hovlavancity" or search == "thehovlavancity" or search == "provincecapital" or search == "town" or search == "thetown":
        $ description_hovlavan09 = "During The Southern Invasion, the city kept many asylum seekers outside the walls, unable to provide shelter to the great number of people who reached this place from the southern provinces. The way these refugees disturbed the forests has provoked a dragon attack, and brought doom on many of them."
        menu:
            '“Nah, I wasn’t let in,” she bursts into laughter, “and tried only once, when I was seeking asylum. Too many folks did the same, it was as far away from the frontline as possible. Still, not far enough. I didn’t want to sit at the gate, waiting for folks inside to die and make space. I headed to the peninsula with the rest of my group, and I’d say we got lucky. A few days later, the dragon burnt a hundred souls, if not more, and many others were lost to the nights and hunger.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "easternroad" or search == "eastroad" or search == "roadintheeast" or search == "eastroad" or search == "roadintheeast" or search == "theeasternroad":
        $ quest_ruins_10yclue05 = "I heard that the trade between the villages has slowed down."
        $ foggy_about_goblins = 1
        menu:
            '“It used to be just another path, but now folks stay away from it. Once the war began, the soldiers left the watchtower to the locals. The trade has slowed down. Ten years ago or so, folks used to travel from here to {color=#f6d6bd}Eudocia’s{/color} place, {color=#f6d6bd}Pelt of the North{/color}, and {color=#f6d6bd}Steep House{/color}. Now, there isn’t much point. It’s easier to just head west, to {color=#f6d6bd}Howler’s Dell{/color} and back.”
            \n\n“So, fewer folks travel, the road hardly ever gets cleared, gnolls and other beasts stop worrying ‘bout blades. Even the goblins are getting too clever. They surround you from two sides, one gets loud, others sneaks by you...” She jabs the air with her fist. “Bam, they get you from the back.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "westernroad" or search == "westroad" or search == "roadinthewest" or search == "thewesternroad":
        menu:
            '“It’s not too dangerous, especially for a rider. The path from here leads between the bogs and the forest, with mountains on the horizon. You’ll get to a ford, then the western crossroads. The turn west leads to {color=#f6d6bd}Old Págos{/color}, or you can keep riding ahead, to {color=#f6d6bd}Howler’s Dell{/color}. They’re both large villages, and they keep their parts of the wilderness safe. Just don’t turn east. That’s how you enter the heart of the forest, but no soul uses that route anymore. Better to forget ‘bout it.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "northernroad" or search == "thenorthernroad" or search == "northroad" or search == "roadinthenorth":
        menu:
            '“That’s hwere we are,” she waves her hand as if she’s inviting you to enter a new room. “You can keep riding west and south to get to the crossroad that leads into the bogs. It will take you to {color=#f6d6bd}Hwite Marshes{/color}. Other than that, you can either ride north, to {color=#f6d6bd}Gale Rocks{/color}, or north and east, to {color=#f6d6bd}Creeks{/color}. We still trade a bunch, so the paths there are the safest corner on this side of {color=#f6d6bd}Hag Hills{/color}. Not many beasts hiding by the lake, and my tribesfolk got rid of the wolf packs.”
            '
            '“I spot a large lair of howlers by the lake.”' if not foggy_about_howlerslair and howlerslair_unlocked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spot a large lair of howlers by the lake.”')
                $ foggy_about_howlerslair += 1
                $ foggy_friendship_tradepoints += 1
                $ minutes += 3
                menu:
                    'She thanks you for the tale, but says that her son avoids the forests anyway. “And it’s not hard to spot hwere the {i}howlers{/i} dwell,” she emphasizes with a chuckle.
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "howlerslair" or search == "howlerlair" or search == "lairofhowlers" or search == "thehowlerslair" or search == "thehowlerlair" or search == "thelairofhowlers":
        if not foggy_about_howlerslair:
            menu:
                '“Hwy, just follow their howls and you’ll find them soon enough, dear.”
                '
                '“I spot a large lair at the northern road.” I describe the place her crew should avoid.' if not foggy_about_howlerslair and howlerslair_unlocked:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spot a large lair at the northern road.” I describe the place her crew should avoid.')
                    $ foggy_about_howlerslair += 1
                    $ foggy_friendship_tradepoints += 1
                    $ minutes += 3
                    menu:
                        'She thanks you for the tale, but says that her son avoids the forests anyway. “And it’s not hard to spot hwere the {i}howlers{/i} dwell,” she emphasizes with a chuckle.
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "southernroad" or search == "southroad" or search == "roadinthesouth" or search == "thesouthernroad":
        menu:
            '“You must have crossed the mountain pass leading through {color=#f6d6bd}Hag Hills{/color}, aye? The old dolmen is in the east, {color=#f6d6bd}Pelt of the North{/color} and the ruins of {color=#f6d6bd}Steep House{/color} in the west. From there, it’s a long road to {color=#f6d6bd}Howler’s Dell{/color}.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "haghills" or search == "thehaghills" or search == "hags" or search == "thehags":
        if not quest_explorepeninsula_description10c:
            $ quest_explorepeninsula_description10c = "The old mine set in {color=#f6d6bd}Hag Hills{/color} is flooded. There’s no point in trying to restore it."
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        menu:
            '“Honestly, we’re done with {color=#f6d6bd}Hag Hills{/color}, at least from this side. The old mine by the western road is flooded, and there are no plans to build a new quarry hamlet. {color=#f6d6bd}Old Págos{/color} cuts better blocks of stone anyway.”
            \n\nShe looks through the window at the lake. “The river that flows by the southern road is wide and strong, with no bridges, or settlements... If there’s anything behind it, no soul has found it yet.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "militarycamp" or search == "tuliascamp" or search == "tuliacamp" or search == "campoftulia" or search == "soldierscamp" or search == "soldiercamp" or search == "guardcamp" or search == "themilitarycamp" or search == "thearmycamp":
        if foggy_about_oldcamp:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        $ foggy_about_militarycamp = 1
        menu:
            '“A mystery, aye? That it’s still standing at all. There were always bad tales ‘bout the place. Folks disappearing, or getting sick. Highwaymen taking over. Weird screams, and nightmares. {color=#f6d6bd}Caius{/color}, the one without a hand?” She points toward his whereabouts with her thumb. “He had a vision one night there, something that turned his soul wicked. That’s hwat {color=#f6d6bd}Hag Hills{/color} do to folks.”
            '
            '“The camp is gone.”' if militarycamp_destroyed and not foggy_about_oldcamp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The camp is gone.”')
                label foggy_about_oldcamp01:
                    $ foggy_about_oldcamp = 1
                    $ foggy_friendship += 1
                    menu:
                        '“Another troll...” She concludes your brief tale and scratches her knee. “These soldiers must have carried quite a collection of curses, aye? Now the traders will have one less reason to even cross the valley.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "oldcamp" or search == "destroyedcamp" or search == "oldtuliacamp" or search == "oldmilitarycamp" or search == "theoldcamp" or search == "thedestroyedcamp" or search == "theoldtuliacamp" or search == "theoldmilitarycamp":
        if foggy_about_oldcamp:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“Never heard of it.”
                '
                '“The military camp in {color=#f6d6bd}Hag Hills{/color} is gone.”' if militarycamp_destroyed and not foggy_about_oldcamp:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The military camp in {color=#f6d6bd}Hag Hills{/color} is gone.”')
                    jump foggy_about_oldcamp01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "southerncrossroad" or search == "southerncrossroads" or search == "southcrossroads" or search == "southcrossroad" or search == "crossroadsinsouth" or search == "crossroadsinthesouth" or search == "thecrossroadsinthesouth" or search == "thesoutherncrossroads":
        $ pcknowsaobutdolmen = 1
        menu:
            '“Is our signpost still standing? Our hunters carried it there a few years back. We wanted to warn folks to move through {color=#f6d6bd}Howler’s{/color}, but it felt {i}wrong{/i}, you know, like bowing your head, admitting you lost your home. The eastern road used to be ours, and now...” She scratches her knee. “Even the roadside dolmen is nothing more but a racoon house.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "easterncrossroads" or search == "easterncrossroad" or search == "eastcrossroads" or search == "eastcrossroad" or search == "crossroadsineast" or search == "crossroadsintheeast" or search == "thecrossroadsintheeast" or search == "theeasterncrossroads" or search == "thewatchtower" or search == "watchtower" or search == "theabandonedwatchtower" or search == "abandonedwatchtower" or search == "theruinedwatchtower" or search == "ruinedwatchtower":
        $ galerocks_watchtowerkey_knows = 1
        $ shortcut_pcknowsabout = 1
        menu:
            '“The watchtower used to be a safe shelter,” she looks through the door. “Its walls could stop even the larger beasts. Well, maybe not a dragon. But there are no soldiers around here, and without traders - also no mercenaries. We asked adventurers to occupy it, but all they ever did was grab hwat they could, hunt for a bit, then went away.”
            \n\n“{color=#f6d6bd}Eudocia{/color}, the enchantress, said she cares not ‘bout keeping the tower in one piece. We don’t even have a key to the main door, it’s in {color=#f6d6bd}Gale Rocks{/color}. We can only wait and see how many years it will take before it turns into a ruin.”
            \n\nYou ask her what you can find near the watchtower. “{color=#f6d6bd}Eudocia{/color} is to the east, the road through the heart of the forest to the west. Far away to the south you’ll find a dolmen, but no soul looks after it anymore. The road north leads here, through the stone bridge and foraging grounds.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "westerncrossroads" or search == "westerncrossroad" or search == "westcrossroads" or search == "westcrossroad" or search == "crossroadsinwest" or search == "crossroadsinthewest" or search == "thecrossroadsinthewest" or search == "thewesterncrossroads":
        menu:
            '“With Howler’s Creek flowing by it, it’s a charming path. A safe one, too. There’s {color=#f6d6bd}Howler’s Dell{/color} to the south and {color=#f6d6bd}Old Págos{/color} to the west, so it’s important for trade. The folks from all the villages place signs to show hwat they have to offer. A custom older than {color=#f6d6bd}Creeks{/color},” she says with a smile. “In the east you’ll find this large gate that keeps away the monsters of the deep woods.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "northerncrossroads" or search == "northerncrossroad" or search == "northcrossroads" or search == "northcrossroad" or search == "crossroadsinnorth" or search == "crossroadsinthenorth" or search == "thecrossroadsinthenorth" or search == "thenortherncrossroads":
        menu:
            '“If there were such’ place, we would be it. You have two crossroads nearby, the one leading north, to {color=#f6d6bd}Gale Rocks{/color}, and the other leading either to {color=#f6d6bd}Creeks{/color}. If you ride south, you’ll get to the statue of The Wanderer, and if west - to the ruined shelter.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "alchemytable" or search == "alchemyset" or search == "alchemytools" or search == "alchemy":
        $ description_foggy03 = "She has her own set of alchemical tools, necessary to brew ciders and distill hard drinks."
        menu:
            'She points at the trapdoor with her chin. “I dabbled with some recipes for drinks. I’ve plenty of brewing tools, though I can name maybe half of them. Still, from ales to hard drinks, I had some successes.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "pelt" or search == "peltnorth" or search == "thepeltnorth" or search == "thepeltofnorth" or search == "thepeltofthenorth" or search == "peltofnorth" or search == "peltofthenorth" or search == "thepeltnorthtavern" or search == "peltnorthtavern" or search == "peltnorthinn" or search == "iasontavern" or search == "iasonsplace" or search == "thepeltnorthinn" or search == "peltnorthinn" or search == "peltnorthinn" or search == "iasoninn":
        $ foggy_about_peltnorth = 1
        $ description_iason02 = "The leader of a team of big-game hunters."
        $ description_iason02a = "He arrived here more than ten years ago."
        $ iason_name = "Iason"
        $ description_bighunters01 = "They are led by "
        $ description_bighunters04 = "They arrived here about ten years ago."
        $ description_bighunters05 = "According to {color=#f6d6bd}Foggy{/color}, “they can be a lot of fun if he’s not around.”"
        menu:
            '“It’s placed in what used to be an outpost of dragon hunters. Older than mine, but finely renewed. Far away, near the pass that leads through {color=#f6d6bd}Hag Hills{/color}. An inn, so you can rest there, or buy yourself some food. {color=#f6d6bd}Iason{/color}, the innkeeper, leads a group of {color=#f6d6bd}big game hunters{/color}, though when they’re together, he’s like a cloud above them. Otherwise, they can be a lot of fun. They haven’t been here long, must be not much more than ten years, and they mostly keep to themselves.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "steephouse" or search == "thesteephouse" or search == "theruinedvillage" or search == "ruinedvillage" or search == "southernvillage" or search == "thesouthernvillage" or search == "theruinsinthesouth" or search == "southruins" or search == "thesouthernruins" or search == "southernruins":
        $ ruinedvillage_name = "Steep House"
        $ foggy_about_steephouse = 1
        if quest_ruins == 1 and not quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
        menu:
            '“{color=#f6d6bd}Steep House{/color}... Aye, it keeps coming back to me, the poor li’l place. Those ruins used to be the richest village in the North, placed so close to the pass through {color=#f6d6bd}Hag Hills{/color}. Perfect for traders and travelers.”
            \n\nHer eyes show sorrow. “They cared ‘bout the southern road, unlike the hunters from {color=#f6d6bd}Pelt{/color}. They farmed, looked after their forest garden, and yet...” She looks away and puts a thumb on her scarred lips. “They would have done better spending their dragons on a proper wall, not that pitiful palisade of theirs. They were {i}inviting{/i} monsters.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "largetree" or search == "thelargetree" or search == "beholder" or search == "treeinaswamp" or search == "bigtree" or search == "thebigtree" or search == "thebeholder" or search == "creepytree" or search == "swamptree" or search == "spookytree" or search == "treealtar" or search == "swampaltar" or search == "stonealtar":
        $ beholder_name_known = 1
        $ description_druids08 = "According to {color=#f6d6bd}Foggy{/color}, the large tree from the swamps is kept under their protection. It’s older than their ring, and it “eats their souls”."
        menu:
            'Her broad shoulders form a straight line. “It’s a dark thing, this {color=#f6d6bd}Beholder{/color}. Gives me chills. The druids told us it’s been here longer than any human, but I don’t know hwy they keep such dark magic around. I heard that it {i}eats{/i} souls, but you know. Gossip gets cruel when it’s ‘bout {i}pagans{/i}.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "elderscave" or search == "druidcave" or search == "thedruidcave" or search == "theelderscave" or search == "caveofdruids" or search == "caveofelders" or search == "theoldmine" or search == "oldmine" or search == "caveoftheelders" or search == "thecaveoftheelders":
        if not quest_explorepeninsula_description10c:
            $ quest_explorepeninsula_description10c = "The old mine set in {color=#f6d6bd}Hag Hills{/color} is flooded. There’s no point in trying to restore it."
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        $ description_druids04a = "According to {color=#f6d6bd}Foggy{/color}: “It’s the same as it is with the priests of Unites, dear. You keep your eyes low, nod without a word, then let them go and do your own thing.”"
        menu:
            '“Aye, there are druids there, in the old, flooded mine. I don’t know much ‘bout them. They keep close to {color=#f6d6bd}Howler’s Dell{/color}, helping with animals and plants. Only two of them ever came to {color=#f6d6bd}Creeks{/color}, soon after we built our first palisade. My {color=#f6d6bd}Ilan{/color} was but a baby.”
            \n\nYou ask her what they said, and she puts her fist to her forehead. “Let me... They had no guards, no weapons, not even a wolf. Were older than I am now, but were walking down these roads as if they owned them. And came to warn us, the shamanic twaddle you can hear everywhere. That we are to stay {i}humble{/i} and {i}respect their woods{/i}. It’s the same as it is with the priests of Unites, dear. You keep your eyes low, nod without a word, then let them go and do your own thing.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "howlersdell" or search == "howlerdell" or search == "howlers" or search == "thehowlersdell" or search == "howlersdell" or search == "howlerdell" or search == "biggestvillage" or search == "thebiggestvillage":
        $ description_thais01 = "{color=#f6d6bd}Foggy{/color} seems to be afraid of her, and encouraged me to “laugh at her jokes”."
        if howlersdell_firsttime:
            $ custom1 = "You recall your memories of {color=#f6d6bd}Thais{/color}, a thin, smiling woman who likes expensive dresses. {color=#f6d6bd}Foggy’s{/color} could squash her in a blink of an eye."
        else:
            $ custom1 = "You wonder how this {color=#f6d6bd}Thais{/color} looks like. You imagine that {color=#f6d6bd}Foggy{/color} should be able to squash most humans in a blink of an eye."
        menu:
            '“Well, there’s a lot to say ‘bout {color=#f6d6bd}Howler’s Dell{/color}, dear.” Her eyes dart around, and you have to press her before she says anything of note. “It’s in the middle of the western road, among the safer lands, and has a large forest garden. Its folks eat and dress well, and have plenty of guards, and the strong spells of their druids.” She scratches her knee, measuring every word. “Whatever you do... Remember to laugh at the mayor’s jokes. Her name’s {color=#f6d6bd}Thais{/color}. Don’t get in her way.” Her voice is as grim as her eyes are serious.
            \n\n[custom1]
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "rockslide" or search == "therockslide" or search == "landslide" or search == "landslide" or search == "roadtofishinghamlet" or search == "fishinghamletroad":
        if foggy_about_rockslide:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“Let me think... That’s the road in the far west, aye? The one between {color=#f6d6bd}Howler’s Dell{/color} and their fishing hamlet? The rocks blocked it over a decade ago.”
                '
                '“Actually, the road has been cleared.”' if rockslide_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, the road has been cleared.”')
                    $ foggy_about_rockslide = 1
                    $ foggy_friendship_tradepoints += 2
                    menu:
                        '“Is that right!” She scratches her broad chin. “I wonder hwat will happen now. {color=#f6d6bd}Gale Rocks{/color} is going to struggle if {color=#f6d6bd}Howler’s{/color} won’t spare dragons on their salted fish.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "fishinghamlet" or search == "thefishinghamlet" or search == "fishhamlet" or search == "thefishhamlet" or search == "howlers hamlet":
        menu:
            '“I’ve never been there. I’ve heard it’s just a couple of buildings and a weak wall. There used to be more hamlets on this side of {color=#f6d6bd}Hag Hills{/color}, like the lumberjack one, but as the fear of the woods grows, folks don’t dare to live in such li’l groups. The soldiers’ camp in the far south is the last one I can think of, and it’s hardly safe.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "oldpágos" or search == "oldpagos" or search == "theoldpagos" or search == "oldpagosvillage":
        $ description_oldpagos01 = "A western village settled on barren soil. The locals exchange the stones from their quarries for supplies."
        $ description_oldpagos02 = "It’s connected strongly with the nearby Order of Truth."
        $ description_oldpagos06 = "It may be one of the oldest settlements in the North."
        $ description_oldpagos08 = "According to {color=#f6d6bd}Foggy{/color}, “they don’t look kindly on those who don’t follow the Orders of Truth”, but “are true believers” and “fine folks”."
        menu:
            '“You’ll do good visiting that place, dear. It may be one of the oldest villages in the North, but even if not, it’s safe, with strong walls and safe roads. Their crops are weak, but for generations now they’ve been cutting stone and building for other tribes in exchange for supplies. Some time ago they tied themselves to the monks, and now they don’t look kindly on those who don’t follow the Orders of Truth,” she pauses, twisting her lips to one side, choosing her words carefully, “but they’re plenty fine folks. True believers. Something lost in the city. Not ones to deal in slave trading and pillage.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "oldpagostemple" or search == "monastery" or search == "themonastery" or search == "templeinmountain" or search == "mountaintemple" or search == "monkstemple" or search == "monkshouse":
        $ description_monastery02 = "According to {color=#f6d6bd}Foggy{/color}, her old friend used to say that sleeping in the monastery helps him with casting spells."
        menu:
            '“Do I look like a pious woman to you?” She moves her bent arm up and down, flexing her muscles. “The monks came to the mountain long before I got here, taking over the old pagan caves, trading their crafts for food with {color=#f6d6bd}Old Págos{/color}. Now, the entire village follows their teachings, and those who live in the monastery can stay inside as long as they want. A friend of mine needed to talk with them, so she called them with... Something like a bell? And then she stood by the gate for an hour, waiting for anyone to speak with her.”
            \n\nYou ask her for any interesting rumors, but she apologizes with a shrug. “It’s a place of secrets. There was this late fire mage from {color=#f6d6bd}Gale Rocks{/color}, truly a dear. He told me that whenever he slept there, he felt as if his soul was stronger. {i}Fingers lighter, spells brighter{/i}, he used to say. Well, the howlers got him anyway.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "highcaves":
        $ description_monastery02 = "According to {color=#f6d6bd}Foggy{/color}, her old friend used to say that sleeping in the monastery helps him with casting spells."
        menu:
            '“You mean the monastery? That’s a name no soul uses anymore. But hwy are you asking me? Do I look like a pious woman to you?” She moves her bent arm up and down, flexing her muscles. “The monks came to the mountain long before I got here, taking over the old pagan caves, trading their crafts for food with {color=#f6d6bd}Old Págos{/color}. Now, the entire village follows their teachings, and those who live in the monastery can stay inside as long as they want. A friend of mine needed to talk with them, so she called them with... Something like a bell? And then she stood by the gate for an hour, waiting for anyone to speak with her.”
            \n\nYou ask her for any interesting rumors, but she apologizes with a shrug. “It’s a place of secrets. There was this late fire mage from {color=#f6d6bd}Gale Rocks{/color}, truly a dear. He told me that whenever he slept there, he felt as if his soul was stronger. {i}Fingers lighter, spells brighter{/i}, he used to say. Well, the howlers got him anyway.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "libraryinstone" or search == "librarystone" or search == "libraryinsidestone" or search == "libraryinstone":
        if monastery_name == "Library in Stone":
            if not foggy_about_monastery:
                menu:
                    '“Never heard of it.”
                    '
                    '“It’s what the prelate calls the monastery.”':
                        $ foggy_about_monastery = 1
                        $ description_monastery02 = "According to {color=#f6d6bd}Foggy{/color}, her old friend used to say that sleeping in the monastery helps him with casting spells."
                        $ foggy_friendship += 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s what the prelate calls the monastery.”')
                        menu:
                            'She bursts into laughter. “Are you serious, love? Hwat a silly name. But hwy are you asking me? Do I look like a pious woman to you?” She moves her bent arm up and down, flexing her muscles. “The monks came to the mountain long before I got here, taking over the old pagan caves, trading their crafts for food with {color=#f6d6bd}Old Págos{/color}. Now, the entire village follows their teachings, and those who live in the monastery can stay inside as long as they want. A friend of mine needed to talk with them, so she called them with... Something like a bell? And then she stood by the gate for an hour, waiting for anyone to speak with her.”
                            \n\nYou ask her for any interesting rumors, but she apologizes with a shrug. “It’s a place of secrets. There was this late fire mage from {color=#f6d6bd}Gale Rocks{/color}, truly a dear. He told me that whenever he slept there, he felt as if his soul was stronger. {i}Fingers lighter, spells brighter{/i}, he used to say. Well, the howlers got him anyway.”
                            '
                            '“How about...”':
                                python:
                                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                    search = search.strip().lower().replace(" ", "")
                                    if not search:
                                        search = "no one"
                                jump foggylakeregularquestionsrumors02
                            '“Thanks.”':
                                jump foggylakefoggyafterinteraction01
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            else:
                $ description_monastery02 = "According to {color=#f6d6bd}Foggy{/color}, her old friend used to say that sleeping in the monastery helps him with casting spells."
                menu:
                    '“You know more ‘bout this place than I do, love. The monks came to the mountain long before I got here, taking over the old pagan caves, trading their crafts for food with {color=#f6d6bd}Old Págos{/color}. Now, the entire village follows their teachings, and those who live in the monastery can stay inside as long as they want. A friend of mine needed to talk with them, so she called them with... Something like a bell? And then she stood by the gate for an hour, waiting for anyone to speak with her.”
                    \n\nYou ask her for any interesting rumors, but she apologizes with a shrug. “It’s a place of secrets. There was this late fire mage from {color=#f6d6bd}Gale Rocks{/color}, truly a dear. He told me that whenever he slept there, he felt as if his soul was stronger. {i}Fingers lighter, spells brighter{/i}, he used to say. Well, the howlers got him anyway.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“Never heard of it.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "thegate" or search == "westgate" or search == "thewestgate" or search == "thewesterngate" or search == "westernforestedge" or search == "westernforestentrance" or search == "largegate" or search == "biggate" or search == "thelargegate" or search == "thebiggate" or search == "stonegate" or search == "thestonegate":
        menu:
            '“Aye, let’s be grateful to {color=#f6d6bd}Old Págos{/color} that the gate is still standing. They build it all on their own decades ago, and it keeps the wingless monsters away from the western road. It’s too bad that the route beyond it has overgrown.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "shortcut" or search == "heartoftheforest" or search == "centerofthewoods" or search == "heartofthewoods" or search == "centerofthewood" or search == "heartofthewood" or search == "heartwoods" or search == "heartforest" or search == "centerofpeninsula" or search == "woodland" or search == "centeroftheforest" or search == "hearthwood":
        $ description_shortcut00 = "A shortcut leading through the center of the peninsula."
        $ description_shortcut01 = "I heard that it connects the western villages to the watchtower in the east."
        $ description_shortcut03 = "The locals claim that this place is abandoned, neglected, and unusually dangerous."
        $ description_shortcut04 = "I was advised to use it only when healthy, ideally with fine equipment at hand."
        $ description_shortcut05 = "According to {color=#f6d6bd}Foggy{/color}: “Stay as close to the road as you can. You may find parts that seem safe, but nothing ‘bout the woods is. Sooner or later, something flesh-chasing will show up. Don’t get yourself killed for a couple of sour apples. The cairn in the middle of the road may seem safer, but there are some nasty beasts living in the grass. You won’t return with a twisted ankle.”"
        $ shortcut_pcknowsabout = 1
        menu:
            '“No soul uses it anymore. It used to tie the watchtower to the villages in the west. Forget ‘bout it,” she waves her hand with resignation. “The few hours it’s going to save you are not worth the risk.”
            \n\nAfter a few more questions, she gives up. “Fine. It’s the darkest road in the North, so find yourself a plenty fine weapon and armor, and don’t travel there in late hours, or with a weak shell.” She straightens up and walks around the hearth, like a leader describing a plan to a team of adventurers. “Stay as close to the road as you can. You may find parts that seem safe, but nothing ‘bout the woods is. Sooner or later, something flesh-chasing will show up. Don’t get yourself killed for a couple of sour apples. The cairn in the middle of the road may seem safer, but there are some nasty beasts living in the grass. You won’t return with a twisted ankle.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "cairn" or search == "forestcairn" or search == "rockcairn" or search == "stonecairn":
        if foggy_about_cairn:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“I remember it from the few times I’ve been to the heart of the woods. I was told it’s ancient, older than the road or the druids from {color=#f6d6bd}Howler’s{/color}, and that it protects travelers from... {i}evil{/i}, was it? Or just {i}danger{/i}? I’m not sure, but I saw too many folks who ended up dying there to think it’s true.”
                '
                '“I know a ritual that helps me spot magic. There’s a trace of an old spell attached to the cairn, though I’m not sure what was its purpose.”' if shortcut_cairn_interacted == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know a ritual that helps me spot magic. There’s a trace of an old spell attached to the cairn, though I’m not sure what was its purpose.”')
                    $ foggy_about_cairn += 1
                    $ foggy_friendship += 1
                    menu:
                        'She gives you a curious glance. “So you’re saying that there {i}is{/i} a story there. I’ll ask some spellcasters ‘bout it, if any will come here.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "dolmen" or search == "stonechapel" or search == "thedolmen" or search == "thedolmen" or search == "stonechapel":
        menu:
            '“At the southern road, aye? It must be centuries old, but I’d rather spend a night in a young inn, thank you. I know hunters used to make campfires there, but I bet it leaves sticky soot on the walls. Isn’t it weird that there are no other chapels in the North? Maybe they were all dismantled. Stone has its price, after all. ”
            '
            'I show her the key I got from {color=#f6d6bd}Akakios{/color}. “Do you know anything about a secret spot in there? Something with a lock?”' if not dolmen_inside_trapdoor and quest_healingpotion and not foggy_about_dolmen_quest:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This one is important. It blocks the road in the southeast corner. No wagon is going to ride through anytime soon.”')
                $ foggy_about_dolmen_quest += 1
                $ quest_healingpotion_description00d_alt2 = "{color=#f6d6bd}Foggy{/color} told me to dig, and mentioned the dolmen’s walls may be covered in soot."
                if quest_healingpotion == 1:
                    $ renpy.notify("Journal updated: Merchant’s Medicament")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Merchant’s Medicament{/i}')
                $ minutes += 1
                menu:
                    'She raises it to her eye, as if the hole in its bow is about to reveal the hidden entrance. “Centuries old,” her half-whisper remains sonorous and confident, “but not as ancient as the chapel itself. Try digging.” As she returns the key, it looks laughably small in the palm of her hand. “Maybe you’ll find a clue where to dig {i}exactly{/i}.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            '“Funny thing. I found a trapdoor inside the dolmen. It leads to a hidden basement.”' if dolmen_underground_firsttime and not foggy_about_dolmen_underground_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Funny thing. I found a trapdoor inside the dolmen. It leads to a hidden basement.”')
                $ foggy_about_dolmen_underground_firsttime += 1
                $ foggy_friendship_tradepoints += 1
                $ minutes += 1
                menu:
                    'You tell her what you found inside and her grimace, puzzled at first, turns into a chuckle as she scratches her wide neck. “So it’s, hwat, an old bandits’ hideout? A warehouse?” Your empty guesses don’t bring you any closer to an answer. “Let’s just be glad it’s not a cursed altar covered in blood. But who knows, maybe some traders could use this {i}chamber{/i} to pace out their deliveries,” she gives you an encouraging smile. “A plenty fine find, dear.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "riversideturn" or search == "theriversideturn":
        menu:
            '“Just a part of the southern road. Let’s hope that beavers won’t flood it.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "fallentree" or search == "thefallentree":
        if fallentree_cleared:
            menu:
                '“You know more ‘bout this place than I do, love. I’m glad you took care of it.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        elif foggy_about_fallentree:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“Fallen trees are everyhwere, dear.”
                '
                '“This one is important. It blocks the road in the southeast corner. No wagon is going to ride through anytime soon.”' if fallentree_firsttime and not foggy_about_fallentree:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This one is important. It blocks the road in the southeast corner. No wagon is going to ride through anytime soon.”')
                    $ foggy_about_fallentree += 1
                    $ foggy_friendship_tradepoints += 1
                    menu:
                        '“Shit, more and more to deal with. Better take the news to {color=#f6d6bd}Elah{/color} in {color=#f6d6bd}Creeks{/color}. He may be able to deal with it.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "secludedresidence" or search == "thesecludedresidence" or search == "asecludedresidence" or search == "eudociahouse" or search == "theeudociahouse" or search == "aeudociahouse" or search == "eudociashouse" or search == "eudociashouse" or search == "theeudociashouse" or search == "aeudociashouse" or search == "eudocia" or search == "eudocias" or search == "crafterhouse" or search == "thecrafterhouse" or search == "acrafterhouse" or search == "craftershouse" or search == "thecraftershouse" or search == "acraftershouse" or search == "magiccrafterhouse" or search == "themagiccrafterhouse" or search == "amagiccrafterhouse" or search == "themagiccraftershouse" or search == "enchantresshouse" or search == "theenchantresshouse" or search == "aenchantresshouse" or search == "enchantressshouse" or search == "theenchantressshouse" or search == "aenchantressshouse" or search == "magicenchantresshouse" or search == "themagicenchantresshouse" or search == "amagicenchantresshouse" or search == "themagicenchantressshouse" or search == "enchanterhouse" or search == "theenchanterhouse" or search == "aenchanterhouse" or search == "enchantershouse" or search == "theenchantershouse" or search == "aenchantershouse" or search == "magicenchanterhouse" or search == "themagicenchanterhouse" or search == "amagicenchanterhouse" or search == "themagicenchantershouse":
        $ description_eudocia05 = "According to {color=#f6d6bd}Foggy{/color}, she doesn’t look for friendship, and may already be crazy."
        menu:
            '“I know a fair bit ‘bout that house, it’s not more than a few years old. It’s east of the watchtower, surrounded with a wall. My {color=#f6d6bd}Ilan{/color} helped build it, {color=#f6d6bd}Tzvi{/color} as well, as did many souls from {color=#f6d6bd}Gale Rocks{/color}. {color=#f6d6bd}Eudocia{/color} enchanted things for all the tribes for years, that’s how she got enough savings and trust to get the stone and wood she needed. She slept alongside the workers in the watchtower for months. {i}I can’t trust they’ll build it right{/i}, she told me.”
            \n\n“Now she doesn’t leave her home at all, just surrounds herself with walking rocks. She doesn’t seek friends among the tribes. Maybe she’s lonely. Or maybe crazy. A witch.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "stonebridge" or search == "oldbridge" or search == "astonebridge" or search == "aoldbridge" or search == "theoldbridge" or search == "thestonebridge" or search == "thebridgeofstone" or search == "thebridgemadeofstone" or search == "dolmenbridge" or search == "oldbridgemadeofstone" or search == "oldstonebridge" or search == "anoldstonebridge" or search == "aoldstonebridge" or search == "theoldstonebridge":
        menu:
            '“It must be centuries old, this slab, and will stay there longer than any of us.” She smiles.
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "woodlandedge" or search == "thewoodlandedge" or search == "awoodlandedge" or search == "stonesign" or search == "easternforestetrance":
        menu:
            '“You mean the stone we placed at the entrance to the heart of the woods? We did so five years ago, after a group of traders entered the woods and never returned. They tried to walk around the spotted wolves, but instead entered a true dragons’ lair.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "smallcave" or search == "asmallcave" or search == "thesmallcave" or search == "ghoulcave":
        menu:
            '“Caves standing in the middle of nohwere aren’t safe. Even kids know that.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "cabin" or search == "thecabin" or search == "acabin" or search == "huntercabin" or search == "ahuntercabin" or search == "thehuntercabin" or search == "hunterscabin" or search == "ahunterscabin" or search == "thehunterscabin" or search == "woodencabin" or search == "woodencabin" or search == "thewoodencabin" or search == "awoodencabin":
        menu:
            '“My tribesfolk from {color=#f6d6bd}Creeks{/color} built it for hunters years back, a damn mistake of ours. Runners ate two of my friends before we finished construction. We should have waited for a few more years, let the animals get used to us, but now the roads are not much better.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "foragingground" or search == "theforagingground" or search == "aforagingground" or search == "foragingarea" or search == "theforagingarea" or search == "aforagingarea" or search == "foraginggrounds" or search == "theforaginggrounds" or search == "aforagingground":
        menu:
            '“That’s the furthest spot to the south where the foragers of {color=#f6d6bd}Creeks{/color} go. Such’n open area offers li’l to no hideouts, so larger beasts avoid it. Now that there isn’t much food for humans left, {color=#f6d6bd}Ilan{/color} and {color=#f6d6bd}Tzvi{/color} stay closer to the tavern.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "wanderer" or search == "thewanderer" or search == "statueofawoman" or search == "statueofwoman" or search == "thestatueofawoman" or search == "astatueofawoman" or search == "statuewoman" or search == "womanstatue" or search == "statueofalady" or search == "statueoflady" or search == "thestatueofalady" or search == "astatueofalady" or search == "statuelady" or search == "ladystatue" or search == "statueofafemale" or search == "statueoffemale" or search == "thestatueofafemale" or search == "astatueofafemale" or search == "statuefemale" or search == "femalestatue":
        $ wanderer_name = "The Wanderer"
        menu:
            '“That old {i}gal{/i} from {color=#f6d6bd}Gale Rocks{/color} told me it’s {color=#f6d6bd}The Wanderer{/color}, a spirit who looks after travelers. She’s centuries old, the spirit, not the statue, and needs gifts, just a bit of this and that, to pay for her own food and shelter. At her feet, one should spare an apple, a dragon bone, even a pretty pebble. Those who skimp on her will one day be in need, and will see a woman with a staff on the horizon, too busy with her own struggles to help them.”
            \n\n{color=#f6d6bd}Foggy{/color} frowns, moving the scars on her forehead. “But how do we know hwat these travelers saw? Beats me!”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "foggylake" or search == "thisplace" or search == "foggys" or search == "yourplace" or search == "foggyslake" or search == "here":
        menu:
            '“It’s our third summer under the roof of {color=#f6d6bd}Foggy Lake{/color}, but the palisade is older. Used to be a camping spot for the bird catchers from {color=#f6d6bd}Creeks{/color}, and there are fish here that don’t swim in our streams. When we were but newcomers in the North these lands were hard to bend, but the beasts got used to us with time.” A melancholy crawls into her eyes. [custom1]
            \n\n“Every year or so we added something new. The rocks for a campfire, some stools, a fence, a firewood shed, a boat. At one point we brought the lumber from {color=#f6d6bd}Hwite Marshes{/color} and built a cabin, like the one at the eastern road. More folks started resting here, even traders from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Old Págos{/color}. A plenty fine spot for an inn, aye?”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "giantstatue" or search == "divinestatue" or search == "giantstatue" or search == "agiantstatue" or search == "thegiantstatue" or search == "agiantstatue" or search == "statueofaspirit" or search == "statueofagod" or search == "thegiant" or search == "giant" or search == "spiritstatue" or search == "agiant":
        $ foggy_about_giantstatue = 1
        menu:
            '“I saw it myself, two decades ago. Crude like a dolmen, aye? We were seeking help from {color=#f6d6bd}The Tribe of The Green Mountain{/color}, and I’ve seen a druid from {color=#f6d6bd}Howler’s{/color} kneeling in front of the statue, for minutes. Like we would do to the empress, back in the capitol. But I saw no spells, it’s just a big piece of ugly rock.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "oldforestgarden" or search == "oldgarden" or search == "theoldforestgarden" or search == "theoldgarden" or search == "anoldforestgarden" or search == "anoldgarden" or search == "bogentrance" or search == "thebogentrance" or search == "abogentrance":
        $ whitemarshes_forestgardenabandoned = 1
        menu:
            '“That place... The air there resembles the bogs. It used to be a green and healthy forest, but took a lot of work, and brought li’l fruit. Wrong soil. Last I heard, the folks from {color=#f6d6bd}Hwite Marshes{/color} wanted to let it grow wild, see what happens to it.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "creeks" or search == "creek" or search == "thecreeks" or search == "thecreek" or search == "smallestvillage" or search == "thesmallestvillage" or search == "yourhome" or search == "home":
        $ description_creeks01 = "A village of fishers, hunters, and woodcutters in the far North."
        $ description_creeks01a = "They plan to focus more on woodcutting and carpentry."
        $ description_creeks02 = "I heard that the locals are lighthearted and eager to have fun, and appreciate those who approach them with a smile."
        $ description_creeks05 = "According to {color=#f6d6bd}Foggy{/color}, the village is still very young, and almost the entire generation of its original settlers was lost to the fogs."
        menu:
            '“{color=#f6d6bd}Creeks{/color} is my home. It’s younger than {color=#f6d6bd}Ilan{/color} by over a year. It may be small, but I’ve felt better with the folks there than I ever did at the capital.” She takes a big breath. “We used to live on wild game, fish, and foraged goods, and after some years, we chased the larger animals out of the forest. Now our youths learn carpentry. They make barrels, planks, tools. If trade ever comes back here, we’ll have things to sell. There used to be only struggle, now there’s hope, and laughter. We may be poor, but it’s the last joyful place in the North.”
            \n\nHer eyes get gloomy as she reaches for one of the bottles from a shelf. “Aye, there were struggles. I’m among our oldests. Those who came here with me...” She pauses, then puts the bottle away. “But now their children have a real home.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "galerocks" or search == "galerock" or search == "galesrock":
        $ description_galerocks01 = "A large fishing village near the northern shore."
        $ description_galerocks02 = "During sunny days, the locals go to the shores to hunt the fish and birds that live there. When it gets dark, they hide behind the walls, boiling water for salt."
        $ description_galerocks05 = "According to {color=#f6d6bd}Foggy{/color}, harsh lives turned them into harsh people."
        $ description_galerocks08 = "According to {color=#f6d6bd}Foggy{/color}, they lose many folks during their trading trips."
        menu:
            '“Not the nicest bunch of fishers, are they?” She chuckles, but there’s motherly concern in her eyes. “Harsh lives give birth to harsh folks, dear. They spend every sunny day on their fishing boats, then cut the seafish all night long to place them in barrels, or hang them in the smokery. They don’t have crops, no lumber, or iron. The coastal birds and rock squabs are their only game meat. It’s not too dangerous, being a fisher, but all they get comes from trading... Well, you can tell that’s not good news. They try to be their own merchants, take the wares south, and with every year they need to burn more pyres.”
            \n\nShe scratches her broad chin. “Hard to believe {color=#f6d6bd}Gale Rocks{/color} is as old as it is. And that they stick to it, no matter how difficult their lives get.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "pier" or search == "thepier" or search == "galerocksbeach":
        menu:
            '“The one behind {color=#f6d6bd}Gale Rocks{/color}? Not much to say ‘bout it. That’s where the fishers work in the daytime, but they leave that place before eve. Have you ever taken a bath in the sea water? Not too fun,” she chuckles, “once it dries out, you’ve salt {i}everywhere{/i}.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "highisland" or search == "highislands" or search == "thehighisland" or search == "ahighisland" or search == "volcano" or search == "largeisland" or search == "largestisland" or search == "alargeisland" or search == "thelargestisland" or search == "bigisland" or search == "bigestisland" or search == "abigisland" or search == "thebigestisland":
        if not foggy_about_highisland:
            $ foggy_about_highisland = 1
            $ asterion_highisland_clues += 1
        $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
        $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
        $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
        $ description_highisland04 = "According to {color=#f6d6bd}Foggy{/color}, the people of {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Howler’s Dell{/color} may know more about the place."
        menu:
            'She leans forward, but her voice seems to be incapable of a whisper. “You don’t plan to swim there, d’ye? You won’t get there without a boat. And {i}with{/i} a boat it’s still a dice roll, There’s always a drunk or two in {color=#f6d6bd}Rocks{/color} and {color=#f6d6bd}Howler’s{/color} who says they’ve been there, but it’s all rubbish, they hardly touched the island’s wall.”
            \n\nYou try to pressure her a bit, but don’t learn much. She claims that it’s high above the sea, on the top of a wall-like steep cliff, and “a rope may not be enough for one to get to the top”. From time to time, a pillar of smoke flies out of the volcano in the center of the island. “The whole place is green, with animals as great as dragons. Could it store treasures, like the folks say? Maybe. But no soul knows where to look for them. For all I know, some child started a tale and played with everyone’s desperate dreams.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "whitemarshes" or search == "thewhitemarshes" or search == "themarshes" or search == "whitemarsh" or search == "necromancervillage" or search == "hwitemarshes" or search == "thehwitemarshes" or search == "themarshes" or search == "hwitemarsh":
        $ foggy_about_whitemarshes = 1
        $ foggy_about_necromancers = 1
        $ description_whitemarshes05 = "I heard that the locals had to stop selling their lumber because {color=#f6d6bd}Howler’s Dell{/color} started offering their own supplies for much better prices. Because of that, the village fell into poverty."
        $ description_orentius06 = "According to {color=#f6d6bd}Foggy{/color}: “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”"
        menu:
            '“It’s an old village, placed among the bogs in the west. Not so far from here, but the road there leads around the woods, so it takes a good hwile.” She rubs her chin. “I’m sure you already know ‘bout the awoken. I don’t like what the folks there are doing, not one bit, but I can’t blame them. They struggle, and they don’t know how to protect their kids, their elders. {color=#f6d6bd}Orentius{/color}, their priest...” She cracks her shoulders. “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”
            \n\nShe opens the door with a wave of her hand, letting in some fresh air. She looks at the lake. “They used to trade in lumber, those from {color=#f6d6bd}Marshes{/color}, until {color=#f6d6bd}Howler’s Dell{/color} started selling their own trees for better prices. The trade to {color=#f6d6bd}Marshes{/color} died, and so came the hunger.” She looks at you with an unclear grimace on her lips. “You may judge them, but at least their preacher gave them hope, even if it’s tied to black magic.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "banditcamp" or search == "banditscamp" or search == "campofbandits" or search == "bandithamlet" or search == "banditshamlet" or search == "hamletofbandits" or search == "hideoutofbandits" or search == "bandithideout" or search == "banditshideout" or search == "bandits" or search == "hideout" or search == "glauciacamp" or search == "glauciascamp" or search == "campofglaucias" or search == "glauciacamp" or search == "glauciascamp" or search == "glauciahamlet" or search == "glauciashamlet" or search == "hamlet ofglaucias" or search == "glauciahamlet" or search == "glauciashamlet" or search == "glauciahideout" or search == "glauciashideout" or search == "hideoutofglaucias" or search == "glaucias":
        if foggy_about_banditshideout:
            menu:
                'She gestures for you to stop. “Not another word. I don’t care.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                'She puts her hand on her side, pushing her chest out. “Hwy would I know hwere the bandits are hiding? Better watch your words.”
                '
                '“I know how to find the hideout.”' if banditshideout_pcknowswhere:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know how to find the hideout.”')
                    if banditshideout_knowsaboutlumberjackcamp and banditshideout_pcknowswhere:
                        $ banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp = 1
                    $ foggy_about_banditshideout = 1
                    menu:
                        'You mention a camp near the cairn, but she frowns and gestures for you to stop. “Not another word. I don’t care.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "lumberjackcamp" or search == "lumberjackhamlet" or search == "woodcuttercamp" or search == "woodcutterscamp" or search == "campofwoodcutters" or search == "thecampofwoodcutters" or search == "lumberjackhamlet" or search == "lumberjackhamlet" or search == "woodcutterhamlet" or search == "woodcuttershamlet" or search == "hamletofwoodcutters" or search == "thehamletofwoodcutters":
        $ banditshideout_knowsaboutlumberjackcamp += 1
        if banditshideout_knowsaboutlumberjackcamp and banditshideout_pcknowswhere:
            $ banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp = 1
        menu:
            '“Woodcutters used to have a camp close to the heart of the woods, north from the cairn that’s just halfway through the shortcut. They were gathering logs for {color=#f6d6bd}Creeks{/color} and {color=#f6d6bd}Gale Rocks{/color}, but animals didn’t like it, not one bit. Once the summer started, it got too dangerous. We left the hamlet to itself, at least while we had {i}some{/i} of our limbs left,” she makes a wide grin.
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "greenmountaintribe" or search == "greenmountain" or search == "villageofgreenmountaintribe" or search == "villageofthegreenmountaintribe" or search == "thegreenmountaintribe" or search == "thegreenmountain" or search == "tribegreenmountain" or search == "thetribeofthegreemnountain" or search == "tribeofthegreemnountain" or search == "villagegreenmountaintribe" or search == "greenmountaintribevillage" or search == "greenmountaintribehome" or search == "greenmountaintribecave" or search == "greenmountaintribehideout" or search == "hiddenvillage" or search == "thehiddenvillage" or search == "secretpaganvillage" or search == "thesecretvillage" or search == "hiddentribe" or search == "thehiddentribe" or search == "secrettribe" or search == "thesecrettribe" or search == "thepaganvillage" or search == "paganvillage" or search == "thetribeofthegreenmountain" or search == "thetribethegreenmountain" or search == "thetribegreenmountain" or search == "thetribeofthegreenmountains" or search == "thetribethegreenmountains" or search == "thetribegreenmountains" or search == "secretvillage" or search == "secrettribe" or search == "tribeofthegreenmountain" or search == "tribethegreenmountain" or search == "tribeofthegreenmountains" or search == "tribethegreenmountains" or search == "tribegreenmountains":
        $ quest_reachthepaganvillage_description01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
        $ description_greenmountaintribe01 = "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
        if not quest_reachthepaganvillage:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("New entry: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
        $ description_greenmountaintribe06 = "According to {color=#f6d6bd}Foggy{/color}, they cut off contact with other villages almost ten years ago."
        $ description_greenmountaintribe07 = "Apparently they try to stay away from the cityfolk, afraid of persecution from the hands of The United Church."
        $ quest_ruins_10yclue06 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} cut off contact with other villages."
        menu:
            'She looks at you in silence, then suddenly bursts into laughter. “Was it me who told you ‘bout {color=#f6d6bd}The Tribe of The Green Mountain{/color}? Shameful!” Her shaking chest is like a running beast. “Oh love, they won’t be happy to see you. They live in a cave, far from here, on the mountainside in the far east. They try to stay away from hwat happens in the lowlands, but they don’t even want to trade with us any more, not since...” She waves her hand. “Since almost a decade, I’d say.”
            \n\nWhen you ask her why their presence is such a secret, she scratches her knee. “It’s their will, and we seek no conflict with their weird shamans. They know of the monks from the monastery, and they’re afraid of hwat they’ll face once the Unites arrive. You know hwat the {i}Church{/i} does to {i}pagans{/i}.” Both of these words are dripping with disgust. “If you have to bother them, ride south, to the old bridge, then turn east, until you reach a game trail. Just stay on the northern side of the brook... And be sure you can get through the thicket, somehow.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "ford" or search == "theford":
        if not ford_firsttime:
            menu:
                '“There are many places you could call that, dear.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                'After you describe the ford close to the western crossroads, she scratches her shoulder, then her back. “Flies and mosquitos, well. I’m not a bug sage, you know. The fog would keep them on the ground, but unless you have dozens of leaves-heavy torches, don’t try to scare them with fire. Maybe ask around in {color=#f6d6bd}Hwite Marshes{/color}? Living in the bogs, they must have some ways to keep their blood inside.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "bog" or search == "thebog" or search == "abog" or search == "bogs" or search == "thebogs":
        if not foggy_about_vines:
            menu:
                '“You must mean {color=#f6d6bd}Hwite Marshes{/color} and their peat fields. It’s been years since I’ve been to that place, but places like this don’t change much. If you must ride so far, dear, leave those parts long before dusk. The hunting beasts aren’t as afraid of sunlight.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“You know more ‘bout the bogs than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "vine" or search == "thevine" or search == "avine" or search == "vines" or search == "thevines":
        if not vines_firsttime:
            menu:
                '“This tells me nothing, dear.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            if not foggy_about_vines:
                $ foggy_friendship += 1 # $ foggy_friendship_tradepoints += 2
                $ foggy_about_vines = 1
                menu:
                    'After you tell her about the gate of plants, she lets out a deep sigh. “Never heard of it. It wasn’t meant for beasts, was it. It’s for the outsiders.” She scratches her knee and gives you a grateful nod.
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            else:
                menu:
                    '“You know more ‘bout this place than I do, love.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
    elif search == "peatfield" or search == "thepeatfield" or search == "apeatfield" or search == "turffield" or search == "theturffield" or search == "aturffield" or search == "peatfields" or search == "thepeatfields" or search == "apeatfields" or search == "turffields" or search == "theturffields" or search == "aturffields":
        if not quest_explorepeninsula_description17:
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
            $ quest_explorepeninsula_description17 = "The western bogs are a good spot for peat harvesting - as long as the locals are friendly to the outsiders, they may be willing to trade for it."
        menu:
            '“It used to be just a bit brighter part of the bogs, with a small clearing, aye? The folks were cutting a wagon or two of peat every year, for farmers and smokers, but those were different times. Now the field widens so much that beasts may grow angry, losing their homes and all.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "theruinedshelter" or search == "aruinedshelter" or search == "ruinedshelter":
        $ quest_ruins_10yclue05p2 = "That’s also when the locals stopped caring about the shelter at the northern road."
        if not quest_ruins_10yclue05p2 and quest_ruins_10yclue05 and quest_ruins_description01 and quest_ruins == 1:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            '“It used to be a fine spot for folks moving heavy wares with them, be it in bags or on wagons. Even draft beasts need to rest after walking uphill, aye? Not this beast, of course,” she flexes her arm, then bursts into laughter. “Just kidding! No shame on hard workers. That shelter is not all that safe, but a good spot to spend an hour or so in the middle of the day while moving from {color=#f6d6bd}Gale Rocks{/color} to {color=#f6d6bd}Old Págos{/color}. Say, to eat dinner. But no soul looks after it anymore. Don’t know why. It’s been maybe ten years since the last time someone bothered with fixing the gate.”
            '
            '“There’s a lot of mushrooms to find there. Bugs, too. Better tell your foragers.”' if ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a lot of mushrooms to find there. Bugs, too. Better tell your foragers.')
                $ foggy_about_mushroomsinruinedshelter += 1
                $ foggy_friendship_tradepoints += 3
                $ foragers_friendship += 1
                menu:
                    'You start to describe what you saw, but she gestures for you to relax. “I’ll tell them, don’t you worry. We’ll need some mushrooms for the cold months. Thanks, dear.”
                    '
                    '“How about...”':
                        python:
                            search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "no one"
                        jump foggylakeregularquestionsrumors02
                    '“Thanks.”':
                        jump foggylakefoggyafterinteraction01
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
    elif search == "theduskfoxesshelter" or search == "aduskfoxesshelter" or search == "duskfoxesshelter" or search == "thefoxesshelter" or search == "afoxesshelter" or search == "foxesshelter" or search == "thenightfoxshelter" or search == "anightfoxshelter" or search == "nightfoxshelter" or search == "fox shelter" or search == "thefoxshelter" or search == "afoxshelter" or search == "foxshelter":
        if ruinedshelter_name != "Dusk Foxes’ Shelter":
            menu:
                '“Hwat? Never heard of it.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        elif not foggy_about_duskfoxesshelter:
            menu:
                '“Hwat? Never heard of it.”
                '
                '“The ruined shelter in the west. It’s now a home to a family of dusk foxes.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The ruined shelter in the west. It’s now a home to a family of dusk foxes.”')
                    $ foggy_about_duskfoxesshelter = 1
                    $ foggy_friendship_tradepoints += 2
                    menu:
                        'She raises an eyebrow, but listening to your tale, starts to laugh and taps your shoulders. “Li’l pups, you say? How do they look?” Even after a few minutes of chit-chat, she doesn’t hide her grin. “Well, hwat’s the worst that can happen. They’ll get eaten by a bear, or a cat, or a wolf, or a bird. I wouldn’t mind a fur or two as well. Dusk foxes may not be the prettiest of the beasts, but they’re plenty funny.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            $ search = "ruined shelter"
            jump foggylakeregularquestionsrumors02
    elif search == "theoldtunnel" or search == "anoldtunnel" or search == "aoldtunnel" or search == "oldtunnel" or search == "thetunnel" or search == "antunnel" or search == "atunnel" or search == "tunnel":
        if not foggy_about_oldtunnel_inside_opened:
            menu:
                '“There’s nothing to find there, dear. The sea-side entrance was sealed for two years, now...” She pauses, then pretends to wipe her forehead. “Or make it three! Oof! Time sure doesn’t wait.”
                \n\nYou encourage her to go on. “Other than the tunnel, there’s a few chambers there, some made by beasts, others by folks from {color=#f6d6bd}Gale Rocks{/color}. The guards needed a place to stay around, and ways to get rid of bears and such. Chambers for sleep and food and to store supplies. {color=#f6d6bd}Iuno{/color}, the digger from {color=#f6d6bd}Rocks{/color}, used to know all ‘bout those corridors.”
                \n\nYou ask about anything unusual that could be left by the previous dwellers, but she frowns. “Possessed by an adventurous spirit, love? Nah, I doubt you’ll find any {i}treasures{/i}, even if you had a lantern with you. Just watch out for the pointy rocks hanging from the ceilings. They’re brittle, but heavy enough weight to crack your skull.”
                '
                '“Actually, the tunnel is clean now. Took some effort, but it should be easy to get from here to the other side.”' if oldtunnel_inside_opened and not foggy_about_oldtunnel_inside_opened:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, the tunnel is clean now. Took some effort, but it should be easy to get from here to the other side.”')
                    $ foggy_about_oldtunnel_inside_opened = 1
                    $ foggy_friendship += 1
                    $ foggy_friendship_tradepoints += 2
                    $ quarters += 1
                    menu:
                        'You share with her the entire story, and she lets out a tired sigh. “Undead... Too many of them show up around, and I have no strong walls for them.” She scratches her knee and pauses. “You’re bringing me quite relieving news, love. I’m glad you’re safe.”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            menu:
                '“You know more ‘bout this place than I do, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    elif search == "nest" or search == "thenest" or search == "anest" or search == "griffonnest" or search == "thegriffonnest" or search == "agriffonnest":
        if not mountainroad_firsttime:
            menu:
                '“Hwat? Never heard of it.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        elif not foggy_about_nest and foggy_shop_griffonegg_sold:
            $ foggy_about_nest = 1
            $ foggy_friendship += 1
            menu:
                '“So that’s hwere you brought me the egg from... For a roadwarden, you sure do deviate from the route, love.”
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        elif not foggy_about_nest and not foggy_shop_griffonegg_sold:
            menu:
                '“Hwat? Never heard of it.”
                '
                '“It’s set at the mountain road leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.” I tell her all about it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s set at the mountain road leading to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.” I tell her all about it.')
                    $ foggy_about_nest = 1
                    $ foggy_friendship += 1
                    menu:
                        'She taps her lips with two of her sausage-like fingers. “Who knew such beasts live so close... Not that I want to go there. But an egg, that would be something to see, aye?”
                        '
                        '“How about...”':
                            python:
                                search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "no one"
                            jump foggylakeregularquestionsrumors02
                        '“Thanks.”':
                            jump foggylakefoggyafterinteraction01
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
        else:
            if foggy_shop_griffonegg_sold:
                $ custom1 = "“You know more ‘bout this place than I do, love. But I do love the egg you brought me.”"
            else:
                $ custom1 = "“You know more ‘bout this place than I do, love. Are you sure that egg can’t be reached?”"
            menu:
                '[custom1]
                '
                '“How about...”':
                    python:
                        search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "no one"
                    jump foggylakeregularquestionsrumors02
                '“Thanks.”':
                    jump foggylakefoggyafterinteraction01
    # elif search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "" or search == "":
    #     menu:
    #         ' “” “”
    #         '
    #         '“How about...”':
    #             python:
    #                 search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                 search = search.strip().lower().replace(" ", "")
    #                 if not search:
    #                     search = "no one"
    #             jump foggylakeregularquestionsrumors02
    #         '“Thanks.”':
    #             jump foggylakefoggyafterinteraction01
    else:
        menu:
            '“I haven’t heard of such’ place.”
            '
            '“How about...”':
                python:
                    search = renpy.input("Which place are you asking about?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "no one"
                jump foggylakeregularquestionsrumors02
            '“Thanks.”':
                jump foggylakefoggyafterinteraction01
