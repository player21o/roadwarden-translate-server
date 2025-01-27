###################### Pelt of the North
default peltnorth_firsttime = 0
default peltnorth_firsttime_day = 0
default peltnorth_ban_temp = 0
default peltnorth_ban_perm = 0
default peltnorth_ban_perm_past = 0
default peltnorth_bonusnpcs = 0

default peltnorth_guards_fluff = ""
default peltnorth_guards_fluff_old = ""
default peltnorth_horsename_fluff = ""
default peltnorth_horsename_fluff_old = 0
default peltnorth_iason_fluff = ""
default peltnorth_iason_fluff_old = ""
default peltnorth_relaxing_fluff = ""
default peltnorth_relaxing_fluff_old = ""
default peltnorth_resting = 0
default peltnorth_selling = 0

default iason_friendship_moneybonus_points = 0
default iason_friendship_moneybonus_level1 = 10
default iason_friendship_moneybonus_level1_given = 0
default iason_friendship_moneybonus_level1_reaction = 0
default dalit_friendship_moneybonus_level1_reaction = 0
default iason_friendship_moneybonus_level2 = 20
default iason_friendship_moneybonus_level2_given = 0
default iason_friendship_moneybonus_level2_reaction = 0
default dalit_friendship_moneybonus_level2_reaction = 0
default iason_friendship_moneybonus_level3 = 35
default iason_friendship_moneybonus_level3_given = 0
default iason_friendship_moneybonus_level3_reaction = 0
default dalit_friendship_moneybonus_level3_reaction = 0
default iason_friendship_moneybonus_level4 = 50
default iason_friendship_moneybonus_level4_given = 0
default iason_friendship_moneybonus_level4_reaction = 0
default dalit_friendship_moneybonus_level4_reaction = 0
default iason_friendship_moneybonus_level5 = 70
default iason_friendship_moneybonus_level5_given = 0
default iason_friendship_moneybonus_level5_reaction = 0
default dalit_friendship_moneybonus_level5_reaction = 0

label peltnorth01:
    $ renpy.music.play("audio/track_07peltnorth.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    nvl clear
    label peltnorth_guards_fluffloop:
        $ peltnorth_guards_fluff = renpy.random.choice(['playing with their boar, patting its side and feeding it', 'spread across the wall, observing the area', 'training with spears and staffs in the courtyard', 'training with wooden swords and blunt axes in the courtyard', 'sitting at a table and on the stairs, gossiping with mugs of beer in their hands', 'practicing archery and fixing their equipment in the courtyard', 'are by the well, arguing with each other', 'sitting at a table, gambling for apples', 'splitting firewood and weeding the garden patches'])
        if peltnorth_guards_fluff_old == peltnorth_guards_fluff:
            jump peltnorth_guards_fluffloop
        else:
            $ peltnorth_guards_fluff_old = peltnorth_guards_fluff
    label peltnorth_horsename_fluffloop1:
        $ peltnorth_horsename_fluff = renpy.random.choice(['enjoying some old hay', 'napping', 'looking around', 'moving around slowly, as far as its cord allows', 'pawing the ground', 'fighting off flies with its tail', 'lazily looking around'])
        if peltnorth_horsename_fluff_old == peltnorth_horsename_fluff:
            jump peltnorth_horsename_fluffloop1
        else:
            $ peltnorth_horsename_fluff_old = peltnorth_horsename_fluff
    label peltnorth_iason_fluffloop:
        if quarters < 36:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, but the counter is lit with candles.', 'The weak fire in the stove hardly lightens up the hall.', 'The windows are locked, and several guards are sleeping in a corner.'])
            $ iason_stance = "sittingatstove"
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sitting at the stove, cleaning a set of metal tools and ladles.', 'Several guards are eating gruel and talking with {color=#f6d6bd}the innkeeper{/color} at the stove.', '{color=#f6d6bd}The innkeeper{/color} is sitting on a stool, looking at the flames in the stove and holding a carrot and a knife without using them.', '{color=#f6d6bd}The innkeeper{/color} is mixing something in a pot at the stove.'])
        elif quarters < 48:
            $ peltnorthroomdescription = renpy.random.choice(['Some of the windows are open, revealing the dust dancing in the sunbeams.', 'The open windows fill the hall with refreshing air.', 'Two guards are looking through an open window, embracing each other. They don’t spare you a look.'])
            $ iason_stance = "behindcounter"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is dusting the counter and the shelves with a cloth.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, contemplating an empty mug.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, cutting vegetables.', '{color=#f6d6bd}The innkeeper{/color} is standing behind the counter, preparing a set of mugs.', '{color=#f6d6bd}The innkeeper{/color} is leaning on the counter, dividing a small pile of dragon bones.'])
        elif quarters < (world_daylength-60):
            $ peltnorthroomdescription = renpy.random.choice(['The windows are open, but the heat of the burning stove makes the room warm.', 'Most of the windows are open, and the smell of fresh chamomile tisane fills up the hall.', 'The windows are open, and a couple of guards are gossiping in the corner, eating gruel from wooden bowls.'])
            $ iason_stance = "swiping"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sweeping the floor with gentle, even lazy, movements, as if he’s lost in his thoughts.', '{color=#f6d6bd}The innkeeper{/color} is leaning on a broom, having a quiet conversation with an armored guard.', '{color=#f6d6bd}The innkeeper{/color} uses a broom to remove the spiderwebs from the corners of the hall.', '{color=#f6d6bd}The innkeeper{/color} holds a broom in one hand and a dusting cloth in another.'])
        elif quarters < world_daylength:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are open, and while there’s a few guards eating and drinking, the hall is clean.', 'The open windows fill the hall with refreshing air and the sounds of conversation.', 'Sitting beneath an open window, three guards are arguing about something, but then ease the tension with friendly banter.'])
            $ iason_stance = "behindcounter"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is dusting the counter and the shelves with a cloth.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, contemplating an empty mug.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, cutting vegetables.', '{color=#f6d6bd}The innkeeper{/color} is standing behind the counter, preparing a set of mugs.', '{color=#f6d6bd}The innkeeper{/color} is leaning on the counter, dividing a small pile of dragon bones.'])
        else:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, and both the counter and the tables are lit with candles.', 'The strong fire in the stove lightens up the hall, though the whispers between the guards are tense.', 'All windows but one are closed, and one of the guards is looking outside nervously.'])
            $ iason_stance = "swiping"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sweeping the floor with gentle, even lazy, movements, as if he’s lost in his thoughts.', '{color=#f6d6bd}The innkeeper{/color} is leaning on a broom, having a quiet conversation with an armored guard.', '{color=#f6d6bd}The innkeeper{/color} uses a broom to remove the spiderwebs from the corners of the hall.', '{color=#f6d6bd}The innkeeper{/color} holds a broom in one hand and a dusting cloth in another.'])
        if peltnorth_iason_fluff_old == peltnorth_iason_fluff:
            jump peltnorth_iason_fluffloop
        else:
            $ peltnorth_iason_fluff_old = peltnorth_iason_fluff
    $ randommeal = renpy.random.choice(['a bowl of simple gruel and a mug of ale', 'fresh rye bread and an old grain beer with an intense smell of yeast', 'old rye bread, a fistful of nuts, and a fresh grain beer', 'old, toasted bread and a large slice of mouflon cheese', 'a nettle tisane and a simple root stew with hardly any meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a slice of rye bread', 'bacon, an apple, and a cup of birch sap', 'flatbread with butter and an herbal dip sauce', 'a baked, cold pheasant breast and a raw eggplant', 'a roasted rat with a mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water'])
    $ randomgoodmeal = renpy.random.choice(['fresh rye bread, a sausage, a bowl of berries, and a mug of malty beer', 'a decent stew with white bread to dip', 'a fried salmon in sorrel sauce and a bowl of gruel', 'two boiled eggs, a cup of buttermilk, and some ibex offals', 'a bowl of oatmeal based on ibex milk, with berries, nuts, and honey', 'a fresh pie with deer meat, onions, and coriander', 'baked artichokes with a weird, but tasty, roasted lizard', 'an eggplant soup, a bowl of pears, and some crumbly biscuits', 'a raw cabbage head, a smoked quail wing, and a cup of yogurt', 'a pie with hare and cabbage, a bowl of plums and grapes, and a cup of mouflon milk', 'a cup of mint tisane, three duck eggs, and baked duck meat', 'fried, breaded mushrooms with gravy and chamomile tisane', 'a warm mutton stew and a cold yogurt'])
    if pyrrhos_peltnorth == 1:
        label pyrrhos_peltnorth_fluffloop:
            if description_pyrrhos01:
                $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with {color=#f6d6bd}the innkeeper{/color}. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
            else:
                $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with {color=#f6d6bd}the innkeeper{/color}. ', '{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}The scavenger{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
            if pyrrhos_peltnorth_fluff_old == pyrrhos_peltnorth_fluff:
                jump pyrrhos_peltnorth_fluffloop
            else:
                $ pyrrhos_peltnorth_fluff_old = pyrrhos_peltnorth_fluff
    else:
        $ pyrrhos_peltnorth_fluff = ""
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        label shortcut_bandit_peltnorth_fluffloop:
            $ shortcut_bandit_peltnorth_fluff = ""
            $ shortcut_bandit_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The man without a name{/color} is sharpening a curved dagger used for shaving. ', '{color=#f6d6bd}The man without a name{/color} is plucking the feathers from a dead pigeon. ', '{color=#f6d6bd}The man without a name{/color} is washing his gambeson. ', '{color=#f6d6bd}The man without a name{/color} is sitting at the stove, lost in his thoughts. When he glances at you, his eyes are absent. ', '{color=#f6d6bd}The man without a name{/color} is sitting next to a couple of empty mugs, smiling to himself. ', '{color=#f6d6bd}The man without a name{/color} is washing his boots. '])
            if shortcut_bandit_peltnorth_fluff_old == shortcut_bandit_peltnorth_fluff:
                jump shortcut_bandit_peltnorth_fluffloop
            else:
                $ shortcut_bandit_peltnorth_fluff_old = shortcut_bandit_peltnorth_fluff
    else:
        $ shortcut_bandit_peltnorth_fluff = ""
    if quintus_left_gate and quintus_left_gate < day and not quintus_pelt_firsttime:
        $ quintus_pelt_firsttime = 1
        $ iason_friendship_moneybonus_points += 5
        $ peltnorth_bonusnpcs += 1
        $ iason_friendship += 1
        $ dalit_friendship += 1
        $ description_quintus05 = "For now, he hides at {color=#f6d6bd}Pelt of the North{/color}."
    if quintus_pelt_firsttime and not quintus_pelt_left:
        label quintus_peltnorth_fluffloop:
            $ quintus_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Quintus{/color} is playing with an empty mug. ', '{color=#f6d6bd}Quintus{/color} smiles at you from above a mug. ', '{color=#f6d6bd}Quintus{/color} is trying to fix a shirt with a crude bone needle. ', '{color=#f6d6bd}Quintus{/color} is washing his black gambeson, humming to himself. He glances at you with a smile. ', '{color=#f6d6bd}Quintus{/color} casts sad glances toward a hunter who’s eating a fresh roast. ', '{color=#f6d6bd}Quintus{/color} is napping in the corner. '])
            if quintus_peltnorth_fluff_old == quintus_peltnorth_fluff:
                jump quintus_peltnorth_fluffloop
            else:
                $ quintus_peltnorth_fluff_old = quintus_peltnorth_fluff
    else:
        $ quintus_peltnorth_fluff = ""
    if tulia_pelt_inside and not tulia_pelt_left:
        label tulia_peltnorth_fluffloop:
            $ tulia_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Tulia{/color} is sitting in the corner, flinching at every loud noise. ', '{color=#f6d6bd}Tulia{/color} is chopping vegetables, from time to time taking them to the innkeep. ', '{color=#f6d6bd}Tulia{/color} is keeping her sword on the top of the table, spinning it in place. ', '{color=#f6d6bd}Tulia{/color} glances at you from a corner as she’s inspecting her sparse possessions. ', '{color=#f6d6bd}Tulia{/color} exchanges a few words with one of the hunters. Her voice carries sadness, but she’s standing upright. ', '{color=#f6d6bd}Tulia{/color} is looking through a window. ', '{color=#f6d6bd}Tulia{/color} is observing her sparse hair in the mirror - or rather, the back of a plate. '])
            if tulia_peltnorth_fluff_old == tulia_peltnorth_fluff:
                jump tulia_peltnorth_fluffloop
            else:
                $ tulia_peltnorth_fluff_old = tulia_peltnorth_fluff
    else:
        $ tulia_peltnorth_fluff = ""

    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if (iason_shop_furbought and not iason_shop_shield) or (iason_shop_crossbow_bought and not iason_shop_shield):
        $ iason_shop_shield_announced = 1
    if day >= militarycamp_destroyed_day and not militarycamp_destroyed_firsttime_tulia:
        show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        $ ruinedvillage_unlocked = 1
    elif not peltnorth_firsttime:
        $ ruinedvillage_unlocked = 1
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
    else:
        if quarters <= (world_daylength-5):
            show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        else:
            show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
    if world_endmode:
        show areapicture peltnorth01inside at basicfade
        hide peltnorthbronzerod
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if iason_food_day != day:
        $ iason_food_day = day
        $ iason_food_roll = 0
        $ iason_food_roll = renpy.random.randint(1, 100)
    if day >= militarycamp_destroyed_day and not militarycamp_destroyed_firsttime_tulia:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        $ militarycamp_destroyed_firsttime_tulia = 1
        $ militarycamp_destroyed = 1
        $ tulia_pelt_dayofvisit = day
        $ peltnorth_bonusnpcs += 1
        $ tulia_pelt_inside = 1
        $ tulia_peltnorth_fluff = "{color=#f6d6bd}Tulia{/color} is sitting in the corner, flinching at every loud noise. "
        if not peltnorth_firsttime:
            $ world_known_areas += 1
            $ world_known_npcs += 2 # 1 for guards, 1 for innkeeper
            $ peltnorth_firsttime += 1
            $ peltnorth_firsttime_day = day
            $ renpy.force_autosave(take_screenshot=False, block=True)
            jump peltnorth_tulia_meeting_firsttime01
        else:
            $ renpy.force_autosave(take_screenshot=False, block=True)
            jump peltnorth_tulia_meeting01
    elif world_endmode:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture peltnorth01inside at basicfade
        hide peltnorthbronzerod
        if tulia_about_highisland_narration:
            $ tulia_about_highisland_narration = 0
            $ custom1 = "{color=#f6d6bd}Tulia{/color} flops onto the bench by the window and starts to take off her boots. “I’m not going anywhere before I get to wash myself in the well.”"
        elif tulia_friendship >= 10:
            $ custom1 = "{color=#f6d6bd}Tulia{/color} is waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a smile. “I’m sure glad I don’t have to leave by myself.”"
        else:
            $ custom1 = "{color=#f6d6bd}Tulia{/color} is waiting for you by the window, having her possessions rolled in orderly bundles and the sword by her side. She greets you with a kind nod. “Today is the day, I believe.”"
        $ renpy.force_autosave(take_screenshot=False, block=True)
        jump peltnorth_tulia01regularquestionsafter
    if not peltnorth_firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        jump peltnorthfirstvisit01
    else:
        if pyrrhos_quest_escorting == 1:
            $ pyrrhos_quest_escorting = 0
            $ pc_battlecounter += 1
            $ pyrrhos_peltnorth_counter = day
            $ pyrrhos_peltnorth = 1
            $ peltnorth_bonusnpcs += 1
            $ iason_friendship += 1
            if description_pyrrhos01 and pyrrhos_quest_escorting == 1:
                $ pyrrhos_peltnorth_fluff = "{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with {color=#f6d6bd}the innkeeper{/color}. "
            else:
                $ pyrrhos_peltnorth_fluff = "{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with {color=#f6d6bd}the innkeeper{/color}. "
            jump pyrrhospeltnorth01arrival
        $ can_leave = 1
        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        jump peltnorthregularvisit01

label peltnorthregularvisit01:
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_killed < day:
        $ shortcut_darkforest_bandit_inpeltnorth = 0
        $ shortcut_bandit_peltnorth_fluff = ""
        $ peltnorth_bonusnpcs -= 1
        $ quarters += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'After you enter the yard, the scent of burning flesh comes to you from the grounds behind the inn. You ask what’s this about, and one of the guards shrugs. “Know the guy in the black jacket? His band was here. Called him a traitor, chopped his head off. But we ain’t having his shell roaming in the woods, you know.”
            '
            'I get off my horse and enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off my horse and enter the inn.')
                jump peltnorth01inside
            'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
                if dalit_firsttime:
                    jump peltnorthtalkingwithguards01
                else:
                    $ dalit_firsttime = 1
                    jump dalit_firsttime01
            'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
                if peltnorth_armorer_firsttime:
                    jump peltnorthtalkingwitharmorer01
                else:
                    $ peltnorth_armorer_firsttime = 1
                    jump peltnorthtalkingwitharmorerfirsttime01
            'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                pass
            'I go to the well.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
                jump peltnorthwell01
            'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
                jump peltnorthleftoversquestforberries02
            'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                pass
            'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                pass
    if iason_food_berries_day != day and iason_food_berries == 1:
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'You hear the gate closing. The guards are watching you from the wall - some of them hold spears, others seem more curious than hostile.
            \n\n“Roadwarden,” you hear the familiar, but firm voice of {color=#f6d6bd}[dalit_name]{/color}. “You ain’t walking inside.”
            '
            '“Is this about the berries?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is this about the berries?”')
                $ dalit_pc_tools = 1
                $ iason_food_berries = 3
                $ iason_friendship -= 1
                menu:
                    '“If you wish so, you can be a liar and a thief, but not in our house. Return the tools and pay a coin for being a bother.”
                    \n\nYou can’t see if her crossbow is loaded.
                    '
                    'I dismount and put all the tools on the ground, then throw a coin in the bucket. “Fine, here they are.”' if item_peltnorthberrytools and coins:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and put all the tools on the ground, then throw a coin in the bucket. “Fine, here they are.”')
                        $ item_peltnorthberrytools = 0
                        $ item_peltnorthberries = 0
                        $ coins -= 1
                        $ renpy.notify("You lost the hook, the bucket, and a coin.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook, the bucket, and a coin.{/i}')
                        $ can_leave = 1
                        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
                            $ can_rest = 1
                        else:
                            $ can_rest = 0
                        $ can_items = 1
                        menu:
                            'You lead {color=#f6d6bd}[horsename]{/color} through the now-open gate, where a couple of people observe you with unfriendly smirks. You head to the stable, while {color=#f6d6bd}[dalit_name]{/color} climbs down the wall. Another woman gives her the things you prepared, and after she takes a brief look, she smiles.
                            \n\n“See? That wasn’t so hard. Next time, don’t muck around.” She turns around and goes toward the shed. “We’ll watch your hands.”
                            '
                            'I enter the inn.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                                jump peltnorth01inside
                    'I dismount and put the claw and the other tools on the ground, then throw a coin in the bucket. “Fine, here they are.”' if item_peltnorthberryclaw and coins:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and put the claw and the other tools on the ground, then throw a coin in the bucket. “Fine, here they are.”')
                        $ item_peltnorthberrytools = 0
                        $ item_peltnorthberries = 0
                        $ coins -= 1
                        $ dalit_friendship -= 1
                        show screen notifyimage( "You lost the claw and the bucket.\n-1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the claw and the bucket. -1 {image=cointest}{/i}')
                        $ can_leave = 1
                        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
                            $ can_rest = 1
                        else:
                            $ can_rest = 0
                        $ can_items = 1
                        menu:
                            'You lead {color=#f6d6bd}[horsename]{/color} through the now-open gate, where a couple of people observe you with unfriendly smirks. You head to the stable, while {color=#f6d6bd}[dalit_name]{/color} climbs down the wall. Another woman gives her the things you prepared, and after she sees the detached claw, her eyes widen.
                            \n\n“What spirit made you do this? That’s just silly,” she heads toward the shed. “We’ll watch your hands from now on, {i}roadwarden{/i}.”
                            '
                            'I enter the inn.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                                jump peltnorth01inside
                    '“I have the tools, but I’m broke. I can’t pay you.” I dismount and put all the tools on the ground.' if (item_peltnorthberrytools and coins <= 0) or (item_peltnorthberryclaw and coins <= 0):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have the tools, but I’m broke. I can’t pay you.” I dismount and put all the tools on the ground.')
                        jump peltnorthrberriesban02e
                    '(lie) “I have the tools, but I’m broke. I can’t pay you.” I dismount and put all the tools on the ground.' if (item_peltnorthberrytools and coins) or (item_peltnorthberryclaw and coins):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I have the tools, but I’m broke. I can’t pay you.” I dismount and put all the tools on the ground.')
                        $ pc_lies += 1
                        label peltnorthrberriesban02e:
                            $ renpy.notify("You lost the hook and the bucket.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the hook and the bucket.{/i}')
                            $ dalit_pc_debt = 1
                            $ item_peltnorthberrytools = 0
                            $ item_peltnorthberryclaw = 0
                            $ item_peltnorthberries = 0
                            $ dalit_friendship -= 2
                            $ can_leave = 1
                            if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
                                $ can_rest = 1
                            else:
                                $ can_rest = 0
                            $ can_items = 1
                            menu:
                                '“Really, {i}that{/i} broke?” There’s honest surprise in her voice. She consults with her companions, who then open the gate. You lead {color=#f6d6bd}[horsename]{/color} inside, where a couple of people observe you with unfriendly smirks. One of them giggles. You head to the stable, while {color=#f6d6bd}[dalit_name]{/color} climbs down the wall. Another woman gives her the things you’ve prepared, and after she takes a brief look, she sighs.
                                \n\n“See? That wasn’t so hard. But you won’t get away with this so easily. We’ll {i}wait{/i} for your damn coin.” She heads toward the shed. “And stop being such a fool. We’ll watch your hands.”
                                '
                                'I enter the inn.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                                    jump peltnorth01inside
                    '“I don’t have the tools anymore. How about I pay you back?”' if not item_peltnorthberrytools and not item_peltnorthberryclaw:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have the tools anymore. How about I pay you back?”')
                        jump peltnorthrberriesban02g
                    '(lie) “I don’t have the tools anymore. How about I pay you back?”' if item_peltnorthberrytools or item_peltnorthberryclaw:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “(lie) I don’t have the tools anymore. How about I pay you back?”')
                        $ pc_lies += 1
                        label peltnorthrberriesban02g:
                            $ dalit_friendship -= 3
                            $ iason_friendship -= 1
                            menu:
                                '“Are you serious?” As you stay silent, she starts to discuss something with her companions. Finally, they open the gate. You lead {color=#f6d6bd}[horsename]{/color} inside, where a couple of people observe you with unfriendly smirks. One of them giggles. You head to the stable, while {color=#f6d6bd}[dalit_name]{/color} climbs down the wall quickly. Her red hair is like a forest fire.
                                \n\n“You’re a damn fool if you think you’ll get away with this. Better bring us three dragons soon, or you’ll find a locked gate. You have three days.”
                                '
                                'I reach for my pouch. “Here, I can pay you right away.”' if coins >= 3:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for my pouch. “Here, I can pay you right away.”')
                                    $ can_leave = 1
                                    if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
                                        $ can_rest = 1
                                    else:
                                        $ can_rest = 0
                                    $ can_items = 1
                                    $ dalit_friendship += 1
                                    $ dalit_pc_debt_timer = 0
                                    $ dalit_pc_debt = 0
                                    menu:
                                        'She nods, but her eyes are far from friendly. “M-hm. Good. See, that wasn’t so hard.” Shaking her head, she walks away. “But stop being such a fool. We’ll watch your hands.”
                                        '
                                        'I enter the inn.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                                            jump peltnorth01inside
                                'I don’t have enough. (disabled)' if coins < 3:
                                    pass
                                '“Don’t worry. Three dragons, three days.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry. Three dragons, three days.”')
                                    $ can_leave = 1
                                    if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
                                        $ can_rest = 1
                                    else:
                                        $ can_rest = 0
                                    $ can_items = 1
                                    $ dalit_pc_debt_timer = (day+3)
                                    $ dalit_pc_debt = 3
                                    menu:
                                        'She shakes her head and walks away. “And stop being such a fool. We’ll watch your hands.”
                                        '
                                        'I enter the inn.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                                            jump peltnorth01inside
    if dalit_pc_debt_timer > 0 and dalit_pc_debt_timer < day and day < militarycamp_destroyed_day:
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
        $ can_leave = 1
        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        $ peltnorth_ban_perm = 1
        if quest_intelforpeltnorth == 1 and quest_recruitahunter == 1:
            $ quest_intelforpeltnorth = 3
            $ renpy.notify("Journal updated: Glaucia’s Band,\nRecruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band, Recruit a Hunter{/i}')
            $ quest_recruitahunter_possible = 0
            $ quest_recruitahunter = 3
        elif quest_intelforpeltnorth == 1:
            $ quest_intelforpeltnorth = 3
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        elif quest_recruitahunter == 1:
            $ quest_recruitahunter_possible = 0
            $ quest_recruitahunter = 3
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'The gate is closed. The guards are on the wall, and {color=#f6d6bd}[dalit_name]{/color} holds a raised crossbow.
            \n\n“Get out.”
            '
            'I nod and ride away. (disabled)':
                pass
    elif quarters <= (world_daylength-5):
        $ renpy.force_autosave(take_screenshot=False, block=True)
        if dalit_friendship > 5:
            $ custom1 = "welcomes you with a nod"
        else:
            $ custom1 = "ignores your arrival"
        if quarters >= 32 and quarters < (world_daylength-12):
            $ peltnorth_armorer_description = "You hear the clinking of tools coming from the armorer’s workshop."
        else:
            $ peltnorth_armorer_description = "At this hour, the armorer’s workshop is closed."
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        menu:
            'The guard [custom1]. As you ride in, the other hunters [peltnorth_guards_fluff]. [peltnorth_armorer_description]
            '
            'I get off my horse and enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off my horse and enter the inn.')
                jump peltnorth01inside
            'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
                if dalit_firsttime:
                    jump peltnorthtalkingwithguards01
                else:
                    $ dalit_firsttime = 1
                    jump dalit_firsttime01
            'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                pass
            'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
                if peltnorth_armorer_firsttime:
                    jump peltnorthtalkingwitharmorer01
                else:
                    $ peltnorth_armorer_firsttime = 1
                    jump peltnorthtalkingwitharmorerfirsttime01
            'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                pass
            'I go to the well.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
                jump peltnorthwell01
            'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
                jump peltnorthleftoversquestforberries02
            'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                pass
            'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                pass
    elif quarters == (world_daylength-4):
        $ renpy.force_autosave(take_screenshot=False, block=True)
        if dalit_friendship > 5:
            $ custom1 = "concern"
        else:
            $ custom1 = "curiosity"
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        menu:
            'The guards are close to the gate, looking at you with [custom1]. One of them speaks:
            \n\n“We’re closing, roadwarden. Better come inside.”
            '
            'I get off my horse and enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off my horse and enter the inn.')
                jump peltnorth01inside
            'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                pass
            'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                pass
            'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                pass
    elif quarters <= world_daylength:
        $ renpy.force_autosave(take_screenshot=False, block=True)
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        menu:
            'The lights are promising a refuge. The guards have bows and spears in their hands, and some rush to the gate, only to close it again right after you ride inside.
            \n\n“Bored with life, roadwarden?” One of them grumbles. “Han’t you noticed it’s almost dark?”
            '
            'I get off my horse and enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off my horse and enter the inn.')
                jump peltnorth01inside
            'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                pass
            'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                pass
            'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                pass
    else:
        $ renpy.force_autosave(take_screenshot=False, block=True)
        $ quarters += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        menu:
            'The lights are promising a refuge. The guards have bows and spears in their hands, and ask if there are any monsters behind you. They tell you to wait, observing the area, then open the gate carefully, only to close it right after you ride inside.
            \n\n“Bored with life, roadwarden?” One of them grumbles. “Han’t you noticed it’s already dark?”
            '
            'I get off my horse and apologize to them. I enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off my horse and apologize to them. I enter the inn.')
                jump peltnorth01inside
            'I ignore them. I get off my horse and enter the inn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore them. I get off my horse and enter the inn.')
                jump peltnorth01inside
            'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                pass
            'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                pass
            'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                pass

label leavingthepeltnorth:
    if ((iason_friendship+appearance_charisma) >= iason_alliance_threshold and not iason_alliance and quest_intelforpeltnorth == 2 and quest_foggy2iason_description02) or ((iason_friendship+appearance_charisma) >= iason_alliance_threshold and not iason_alliance and quest_intelforpeltnorth == 2 and quest_foggy2iason_description02a):
        $ iason_freeroom = 1
        $ iason_alliance = 1
        if quest_foggy2iason_description02:
            $ custom1 = ""
            if pc_goal == "iwantstatus":
                $ pc_goal_iwantstatuspoints += 1
            if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ custom1 = "\n\nYou frown. Knowing how you lied to him about your deal with {color=#f6d6bd}Foggy{/color}, you realize you can’t count on {color=#f6d6bd}the innkeep{/color} too much. Otherwise, he may pay you back with his own stab in the back."
        menu:
            'Before you leave the room, {color=#f6d6bd}[iason_name]{/color} knocks on the counter, drawing your eyes. “So far, you’ve been rather useful,” he looks into your eyes, though shortly. “You may indeed make this place a bit crowdier. If you ever need a room, just go upstairs, and save your pouch.”[custom1]
            '
            '“I appreciate it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I appreciate it.”')
                jump leavingthepeltnorth
            'I nod to him, then push the door.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to him, then push the door.')
                jump leavingthepeltnorth
    $ can_leave = 1
    if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if quarters <= (world_daylength-5):
        show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
    else:
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
    if eudocia_bronzerod_rodin_peltnorth:
        show peltnorthbronzerod at basicfade
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    if quarters >= 32 and quarters < (world_daylength-12):
        $ peltnorth_armorer_description = "You hear the clinking of tools coming from the armorer’s workshop."
    else:
        $ peltnorth_armorer_description = "At this hour, the armorer’s workshop is closed."
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
        $ iason_friendship_moneybonus_level1_given = 1
        $ dalit_friendship += 1
        $ iason_friendship += 1
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
        $ iason_friendship_moneybonus_level2_given = 1
        $ dalit_friendship += 2
        $ iason_friendship += 2
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
        $ iason_friendship_moneybonus_level3_given = 1
        $ dalit_friendship += 3
        $ iason_friendship += 3
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
        $ iason_friendship_moneybonus_level4_given = 1
        $ dalit_friendship += 4
        $ iason_friendship += 4
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
        $ iason_friendship_moneybonus_level5_given = 1
        $ dalit_friendship += 5
        $ iason_friendship += 5
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    menu:
        'You step outside. {color=#f6d6bd}[horsename]{/color} is [peltnorth_horsename_fluff]. [peltnorth_armorer_description]
        '
        'I enter the inn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
            jump peltnorth01inside
        'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
            if dalit_firsttime:
                jump peltnorthtalkingwithguards01
            else:
                $ dalit_firsttime = 1
                jump dalit_firsttime01
        'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
            pass
        'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
            if peltnorth_armorer_firsttime:
                jump peltnorthtalkingwitharmorer01
            else:
                $ peltnorth_armorer_firsttime = 1
                jump peltnorthtalkingwitharmorerfirsttime01
        'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
            pass
        'I go to the well.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
            jump peltnorthwell01
        'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
            jump peltnorthleftoversquestforberries02
        'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
            pass
        'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
            pass

label leavingthepeltnorth02:
    $ can_leave = 1
    if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if quarters <= (world_daylength-5):
        show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
    else:
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
    if eudocia_bronzerod_rodin_peltnorth:
        show peltnorthbronzerod at basicfade
    if quarters >= 32 and quarters < (world_daylength-12):
        $ peltnorth_armorer_description = "You hear the clinking of tools coming from the armorer’s workshop."
    else:
        $ peltnorth_armorer_description = "At this hour, the armorer’s workshop is closed."
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
        $ iason_friendship_moneybonus_level1_given = 1
        $ dalit_friendship += 1
        $ iason_friendship += 1
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
        $ iason_friendship_moneybonus_level2_given = 1
        $ dalit_friendship += 2
        $ iason_friendship += 2
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
        $ iason_friendship_moneybonus_level3_given = 1
        $ dalit_friendship += 3
        $ iason_friendship += 3
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
        $ iason_friendship_moneybonus_level4_given = 1
        $ dalit_friendship += 4
        $ iason_friendship += 4
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
        $ iason_friendship_moneybonus_level5_given = 1
        $ dalit_friendship += 5
        $ iason_friendship += 5
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    menu:
        'You return to the courtyard. [peltnorth_armorer_description]
        '
        'I enter the inn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
            jump peltnorth01inside
        'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
            if dalit_firsttime:
                jump peltnorthtalkingwithguards01
            else:
                $ dalit_firsttime = 1
                jump dalit_firsttime01
        'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
            pass
        'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
            if peltnorth_armorer_firsttime:
                jump peltnorthtalkingwitharmorer01
            else:
                $ peltnorth_armorer_firsttime = 1
                jump peltnorthtalkingwitharmorerfirsttime01
        'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
            pass
        'I go to the well.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
            jump peltnorthwell01
        'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
            jump peltnorthleftoversquestforberries02
        'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
            pass
        'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
            pass

##############################################

label peltnorthfirstvisit01:
    $ world_known_areas += 1
    $ world_known_npcs += 2 # 1 for guards, 1 for innkeeper
    $ peltnorth_firsttime += 1
    $ peltnorth_firsttime_day = day
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'Inns like this one fit the regions traveled by merchants, but you wouldn’t expect a place of this size in a forsaken peninsula. The stone and lumber must have been transported from far away, and the workers, guarded by expensive mercenaries, surely lived for many seasons in a primitive hamlet, subsisting on salted supplies.
        \n\nThere are seemingly no cracks in the wall, and the building was whitewashed only a few years back. The road is wide and beaten. Dozens of souls could hide if not in the buildings, then at least in the yard. The expenses and labor put into this fortress were worth many trading ships.
        \n\nThree armed people are on the ramparts, though you only see what’s above their waistline. They’re leaning on the parapet, right next to the gate, and you think you notice a glimpse of a smile. They wear gambesons, each one of them dyed differently - yellow, green, and linen-gray.
        '
        'I approach the gate.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the gate.')
            $ at_activate = 1
            $ at = 0
            menu:
                '{color=#f6d6bd}A woman in yellow armor{/color} leans forward. She has long, curly, disorderly red hair, pointing in every possible direction. This combination of colors doesn’t work at all - in the woods, one would have to shout to draw this much attention.
                \n\nThere’s still a fair distance between the two of you, but she speaks loudly. “I han’t seen a horse for years now! I just said that it’s weird to see such a large jackass, huh!” Her voice is young and strong, with an accent that reminds you of the villages spread around {color=#f6d6bd}Hovlavan{/color}. “But no jackass would wear a saddle, I’d say.”
                \n\nShe exchanges a few words with a male guard wearing green, giving you time to move closer. “Well, this one here says there really {i}are{/i} donkey saddles. Say, traveler, how hard is it to ride a horse?”
                '
                ' (disabled)' ( condition="at == 0" ):
                    pass
                '“How about you give it a try?”' ( condition="at == 'friendly'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “How about you give it a try?”')
                    $ at_activate = 0
                    $ at = 0
                    $ dalit_firstattitude = "friendly"
                    $ dalit_friendship += 2
                    show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
                    menu:
                        'She gasps. “Seriously? Just a moment!” She disappears behind the wall and soon after that, the gate is opened. While you dismount next to the wood splitting spot, a couple of people surround you, pointing at your mount and commenting on its appearance, though they step away whenever {color=#f6d6bd}[horsename]{/color} makes a rapid movement.
                        \n\n{color=#f6d6bd}The guard in the yellow armor{/color} is the only one who steps forward. She raises her hands, as if to pet your palfrey, but doesn’t touch it. “It looked smaller from above,” she whispers loudly. “How do I even get up there?”
                        '
                        '“It’s not easy when you lack confidence. Better use a stool. Or I can help you.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s not easy when you lack confidence. Better use a stool. Or I can help you.”')
                            $ quarters += 1
                            menu:
                                'She touches the animal, which pays no attention to her presence. “Now I’m {i}really{/i} scared,” she contradicts her words with a gentle smile and shining eyes. “Maybe I should wear something lighter?”
                                \n\nYou nod and engage in a bit of a chit-chat with the entire group, discussing what it takes to take care of a horse. Finally, {color=#f6d6bd}the red-haired woman{/color} leads you under the roof where your palfrey can rest, tethered with a cord to a wooden post, near some old hay. “Once you’re ready, go inside, speak with our boss. Maybe you’re hungry?”
                                \n\nThe other guards return to various chores. They peek at your mount every now and then as they’re splitting firewood, cleaning their clothes, weeding the garden patches, and moving chairs. Two of them are making a rope. You head toward the inn, hearing the piercing scream of a boar from the other side of the yard.
                                '
                                'I open the door.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the door.')
                                    jump peltnorthfirstvisit04
                'I laugh. “You wouldn’t believe it! The lessons were a pain.”' ( condition="at == 'playful'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I laugh. “You wouldn’t believe it! The lessons were a real pain.”')
                    $ at_activate = 0
                    $ at = 0
                    show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
                    $ dalit_friendship += 1
                    $ dalit_firstattitude = "playful"
                    $ minutes += 10
                    menu:
                        'You get off your horse and imitate the silly walk from the day that followed your first long journey, when your whole shell was crying. You illustrate the pain as you move your hand from your back to hips, then thighs. In return, the guards tell you about that time when they had to carry their friend with bitten-off legs for three days straight, through the heart of the woods. Meanwhile, the other guards open the gate.
                        \n\n“You may be in a good mood,” {color=#f6d6bd}the woman in the yellow jacket{/color} smiles at you. “But don’t get so noisy when you talk to our boss. The man never smiles - he has the world’s suffering sculpted on his face.”
                        \n\nShe leads you under the roof under which your palfrey can rest, tethered with a cord to a wooden post, near some old hay. “Once you’re ready, go inside, speak with our boss. Maybe you’re hungry?”
                        \n\nThe other guards take care of various chores. They peek at your mount every now and then as they’re splitting firewood, cleaning their clothes, weeding the garden patches, and moving chairs. Two of them are making a rope. You head toward the inn, hearing the piercing scream of a boar from the other side of the yard.
                        '
                        'I open the door.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the door.')
                            jump peltnorthfirstvisit04
                '“It’s easy to learn the basics, but it’s tiring. You train different muscles than those for combat.”' ( condition="at == 'distanced'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “It’s easy to learn the basics, but it’s tiring. You train different muscles than those for combat.”')
                    $ at_activate = 0
                    $ at = 0
                    $ dalit_firstattitude = "distanced"
                    show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
                    $ minutes += 5
                    menu:
                        '“You don’t say?” She gestures for the other soldier to take care of the gate. “What sort of muscles?”
                        \n\nYou climb down, staying concise and to the point. You point at your back, hips, and thighs, then speak about the training routine that a rider follows to stay in the saddle for more than two days.
                        \n\nAs you enter the yard, the woman also uses a ladder to get off the wall, then leads you under the roof where your palfrey can rest, tethered with a cord to a wooden post, near some old hay. “Once you’re ready, go inside, speak with our boss,” she says with a shadow of a smile. “He has time, there aren’t any travelers around.”
                        \n\nThe other guards take care of various chores. They peek at your mount every now and then as they’re splitting firewood, cleaning their clothes, weeding the garden patches, and moving chairs. Two of them are making a rope. You head toward the inn, hearing the piercing scream of a boar from the other side of the yard.
                        '
                        'I open the door.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the door.')
                            jump peltnorthfirstvisit04
                'I don’t answer her. “It’s an inn, isn’t it? Open the gate!”' ( condition="at == 'intimidating'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I don’t answer her. “It’s an inn, isn’t it? Open the gate!”')
                    $ at_activate = 0
                    $ at = 0
                    $ dalit_firstattitude = "intimidating"
                    show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
                    $ dalit_friendship -= 1
                    menu:
                        '“Ah, bugger off,” she shrugs and climbs down. After just a moment, the other guards help her open the gate and let you in.
                        \n\nYou get off your horse and ask where you can leave it. {color=#f6d6bd}The guard in the yellow gambeson{/color} leads you under the roof with a wooden post for a tethering cord, near some old hay. When she speaks, her tone is harsh.
                        \n\n“This place is a haven, but also our house, stranger. You better show our boss due respect. One word from him,” she turns back and walks away. “And we’ll chop you to pieces, no questions asked.”
                        \n\nThe other guards take care of various chores. They peek at your mount every now and then as they’re splitting firewood, cleaning their clothes, weeding the garden patches, and moving chairs. Two of them are making a rope, and some others are holding weapons. You head toward the inn.
                        '
                        'I open the door.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the door.')
                            jump peltnorthfirstvisit04
                '“Quite hard, honestly. Some days are still rough on me.”' ( condition="at == 'vulnerable'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Quite hard, honestly. Some days are still rough on me.”')
                    $ at_activate = 0
                    $ at = 0
                    $ dalit_firstattitude = "vulnerable"
                    show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
                    menu:
                        '“How come?” She gestures for the other soldiers to take care of the gate. “It looks like you’re just sitting there?”
                        \n\nAs you climb down, you vaguely gesture at your back, hips, and thighs. The lessons and first journeys were filled with pain, but as time went on, it got easier.
                        \n\nYou enter the yard, and the woman uses a ladder to get off the wall, then leads you under the roof where your palfrey can rest, tethered with a cord to a wooden post, near some old hay. “Once you’re ready, go inside, speak with our boss,” she says with a shadow of a smile. “You sound like someone who needs to rest.”
                        \n\nThe other guards take care of various chores. They peek at your mount every now and then as they’re splitting firewood, cleaning their clothes, weeding the garden patches, and moving chairs. Two of them are making a rope. You head toward the inn, hearing the piercing scream of a boar from the other side of the yard.
                        '
                        'I open the door.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the door.')
                            jump peltnorthfirstvisit04

####################################################

label peltnorth01inside:
    show areapicture peltnorth01inside at basicfade
    hide peltnorthbronzerod
    $ shop = "peltnorth"
    $ can_leave = 0
    $ can_items = 1
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
        $ iason_friendship_moneybonus_level1_given = 1
        $ dalit_friendship += 1
        $ iason_friendship += 1
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
        $ iason_friendship_moneybonus_level2_given = 1
        $ dalit_friendship += 2
        $ iason_friendship += 2
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
        $ iason_friendship_moneybonus_level3_given = 1
        $ dalit_friendship += 3
        $ iason_friendship += 3
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
        $ iason_friendship_moneybonus_level4_given = 1
        $ dalit_friendship += 4
        $ iason_friendship += 4
    if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
        $ iason_friendship_moneybonus_level5_given = 1
        $ dalit_friendship += 5
        $ iason_friendship += 5
    label peltnorth_iason_fluffloop2:
        $ peltnorth_iason_fluff = ""
        if quarters < 36:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, but the counter is lit with candles.', 'The weak fire in the stove hardly lightens up the hall.', 'The windows are locked, and several guards are sleeping in a corner.'])
            $ iason_stance = "sittingatstove"
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sitting at the stove, cleaning a set of metal tools and ladles.', 'Several guards are eating gruel and talking with {color=#f6d6bd}the innkeeper{/color} at the stove.', '{color=#f6d6bd}The innkeeper{/color} is sitting on a stool, looking at the flames in the stove and holding a carrot and a knife without using them.', '{color=#f6d6bd}The innkeeper{/color} is mixing something in a pot at the stove.'])
        elif quarters < 48:
            $ peltnorthroomdescription = renpy.random.choice(['Some of the windows are open, revealing the dust dancing in the sunbeams.', 'The open windows fill the hall with refreshing air.', 'Two guards are looking through an open window, embracing each other. They don’t spare you a look.'])
            $ iason_stance = "behindcounter"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is dusting the counter and the shelves with a cloth.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, contemplating an empty mug.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, cutting vegetables.', '{color=#f6d6bd}The innkeeper{/color} is standing behind the counter, preparing a set of mugs.', '{color=#f6d6bd}The innkeeper{/color} is leaning on the counter, dividing a small pile of dragon bones.'])
        elif quarters < (world_daylength-60):
            $ peltnorthroomdescription = renpy.random.choice(['The windows are open, but the heat of the burning stove makes the room warm.', 'Most of the windows are open, and the smell of fresh chamomile tisane fills up the hall.', 'The windows are open, and a couple of guards are gossiping in the corner, eating gruel from wooden bowls.'])
            $ iason_stance = "swiping"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sweeping the floor with gentle, even lazy, movements, as if he’s lost in his thoughts.', '{color=#f6d6bd}The innkeeper{/color} is leaning on a broom, having a quiet conversation with an armored guard.', '{color=#f6d6bd}The innkeeper{/color} uses a broom to remove the spiderwebs from the corners of the hall.', '{color=#f6d6bd}The innkeeper{/color} holds a broom in one hand and a dusting cloth in another.'])
        elif quarters < world_daylength:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are open, and while there’s a few guards eating and drinking, the hall is clean.', 'The open windows fill the hall with refreshing air and the sounds of conversation.', 'Sitting beneath an open window, three guards are arguing about something, but then ease the tension with friendly banter.'])
            $ iason_stance = "behindcounter"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is dusting the counter and the shelves with a cloth.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, contemplating an empty mug.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, cutting vegetables.', '{color=#f6d6bd}The innkeeper{/color} is standing behind the counter, preparing a set of mugs.', '{color=#f6d6bd}The innkeeper{/color} is leaning on the counter, dividing a small pile of dragon bones.'])
        else:
            $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, and both the counter and the tables are lit with candles.', 'The strong fire in the stove lightens up the hall, though the whispers between the guards are tense.', 'All windows but one are closed, and one of the guards is looking outside nervously.'])
            $ iason_stance = "swiping"
            $ peltnorth_iason_fluff = ""
            $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sweeping the floor with gentle, even lazy, movements, as if he’s lost in his thoughts.', '{color=#f6d6bd}The innkeeper{/color} is leaning on a broom, having a quiet conversation with an armored guard.', '{color=#f6d6bd}The innkeeper{/color} uses a broom to remove the spiderwebs from the corners of the hall.', '{color=#f6d6bd}The innkeeper{/color} holds a broom in one hand and a dusting cloth in another.'])
        if peltnorth_iason_fluff_old == peltnorth_iason_fluff:
            jump peltnorth_iason_fluffloop2
        else:
            $ peltnorth_iason_fluff_old = peltnorth_iason_fluff
    if peltnorth_bonusnpcs:
        jump peltnorth01insidechoosenpc
    else:
        jump peltnorth01insidetalkingwithiason

label peltnorth01insidechoosenpc:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
    $ can_rest = 1
    $ can_leave = 0
    $ can_items = 1
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
        $ shortcut_darkforest_bandit_inpeltnorthpcknowsabout = 1
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    menu:
        '[peltnorthroomdescription] [peltnorth_iason_fluff] [pyrrhos_peltnorth_fluff][quintus_peltnorth_fluff][shortcut_bandit_peltnorth_fluff][tulia_peltnorth_fluff]
        '
        'I go to {color=#f6d6bd}the innkeeper{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the innkeeper{/color}.')
            jump peltnorth01insidetalkingwithiasonalt
        'I join {color=#f6d6bd}Tulia{/color}.' if tulia_pelt_inside and not tulia_pelt_left:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I join {color=#f6d6bd}Tulia{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithtulia01
        'I approach {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_peltnorth == 1 and description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithpyrrhos
        'I approach {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_peltnorth == 1 and not description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithpyrrhos
        'I speak to {color=#f6d6bd}the man without a name{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and not shortcut_bandit_identity:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the man without a name{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithbandit
        'I speak to {color=#f6d6bd}the bandit{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and shortcut_bandit_identity:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the bandit{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithbandit
        'I step toward {color=#f6d6bd}Quintus{/color}.' if quintus_pelt_firsttime and not quintus_pelt_left:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step toward {color=#f6d6bd}Quintus{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithquintus01
        'I go outside.':
            $ can_rest = 0
            $ can_items = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump leavingthepeltnorth

label peltnorthaftersleepfloor:
    nvl clear
    show areapicture peltnorth01inside at basicfade
    hide peltnorthbronzerod
    $ peltnorth_guards_fluff = ""
    $ peltnorth_guards_fluff = renpy.random.choice(['playing with their boar, patting its side and feeding it', 'spread across the wall, observing the area', 'training with spears and staffs in the courtyard', 'training with wooden swords and blunt axes in the courtyard', 'sitting at a table and on the stairs, gossiping with mugs of beer in their hands', 'practicing archery and fixing their equipment in the courtyard', 'are by the well, arguing with each other', 'sitting at a table, gambling for apples', 'splitting firewood and weeding the garden patches'])
    $ peltnorth_guards_fluff_old = peltnorth_guards_fluff
    $ peltnorth_horsename_fluff = renpy.random.choice(['enjoying some old hay', 'napping', 'looking around', 'moving around slowly, as far as its cord allows', 'pawing the ground', 'fighting off flies with its tail', 'lazily looking around'])
    $ peltnorth_iason_fluff = ""
    $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, but the counter is lit with candles.', 'The weak fire in the stove hardly lightens up the hall.', 'The windows are locked, and several guards are sleeping in a corner.'])
    $ iason_stance = "sittingatstove"
    $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sitting at the stove, cleaning a set of metal tools and ladles.', 'Several guards are eating gruel and talking with {color=#f6d6bd}the innkeeper{/color} at the stove.', '{color=#f6d6bd}The innkeeper{/color} is sitting on a stool, looking at the flames in the stove and holding a carrot and a knife without using them.', '{color=#f6d6bd}The innkeeper{/color} is mixing something in a pot at the stove.'])
    $ peltnorth_iason_fluff_old = peltnorth_iason_fluff
    if pyrrhos_peltnorth == 1:
        if description_pyrrhos01:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
        else:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}The scavenger{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
    else:
        $ pyrrhos_peltnorth_fluff = ""
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ shortcut_bandit_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The man without a name{/color} is sharpening a curved dagger used for shaving. ', '{color=#f6d6bd}The man without a name{/color} is plucking the feathers from a dead pigeon. ', '{color=#f6d6bd}The man without a name{/color} is washing his gambeson. ', '{color=#f6d6bd}The man without a name{/color} is sitting at the stove, lost in his thoughts. When he glances at you, his eyes are absent. ', '{color=#f6d6bd}The man without a name{/color} is sitting next to a couple of empty mugs, smiling to himself. ', '{color=#f6d6bd}The man without a name{/color} is washing his boots. '])
    else:
        $ shortcut_bandit_peltnorth_fluff = ""
    if quintus_pelt_firsttime and not quintus_pelt_left:
        $ quintus_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Quintus{/color} is playing with an empty mug. ', '{color=#f6d6bd}Quintus{/color} smiles at you from above a mug. ', '{color=#f6d6bd}Quintus{/color} is trying to fix a shirt with a crude bone needle. ', '{color=#f6d6bd}Quintus{/color} is washing his black gambeson, humming to himself. He glances at you with a smile. ', '{color=#f6d6bd}Quintus{/color} casts sad glances toward a hunter who’s eating a fresh roast. ', '{color=#f6d6bd}Quintus{/color} is napping in the corner. '])
    else:
        $ quintus_peltnorth_fluff = ""
    if tulia_pelt_inside and not tulia_pelt_left:
        $ tulia_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Tulia{/color} is sitting in the corner, flinching at every loud noise. ', '{color=#f6d6bd}Tulia{/color} is chopping vegetables, from time to time taking them to the innkeep. ', '{color=#f6d6bd}Tulia{/color} is keeping her sword on the top of the table, spinning it in place. ', '{color=#f6d6bd}Tulia{/color} glances at you from a corner as she’s inspecting her sparse possessions. ', '{color=#f6d6bd}Tulia{/color} exchanges a few words with one of the hunters. Her voice carries sadness, but she’s standing upright. ', '{color=#f6d6bd}Tulia{/color} is looking through a window. ', '{color=#f6d6bd}Tulia{/color} is observing her sparse hair in the mirror - or rather, the back of a plate. '])
    else:
        $ tulia_peltnorth_fluff = ""
    if iason_food_day != day:
        $ iason_food_day = day
        $ iason_food_roll = 0
        $ iason_food_roll = renpy.random.randint(1, 100)
    $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ renpy.music.play("audio/track_07peltnorth.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ questionpreset = "iason1"
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if shortcut_darkforest_bandit_inpeltnorth and not iason_about_shortcut_bandit and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ iason_about_shortcut_bandit = 1
        $ shortcut_bandit_identity = 1
        $ iason_friendship += 1
        $ iason_friendship_moneybonus_points += 3
        $ banditshideout_bandits_pchearedabout = 1
        menu:
            'The uncomfortable sleeping spot and the sounds of conversation and closing doors wake you up a few times during the night. Nevertheless, your back survives. The morning air here is stuffy and {color=#f6d6bd}the innkeeper{/color} looking toward {color=#f6d6bd}the man you found at the shortcut{/color}. His voice is thoughtful.
            \n\n“Weird times, hm? I was hoping to learn more about the bandits, and now one of them is right here, drinking my ale. Too bad he doesn’t talk,” he glances toward you. “He said he knows you, that you faced some beasts... I mean, coin is coin, but couldn’t you bring me some merchants instead?”
            '
            '(iason1 set)':
                pass
    else:
        menu:
            'The uncomfortable sleeping spot and the sounds of conversation and closing doors wake you up a few times during the night. Nevertheless, your back survives. The morning air here is stuffy and {color=#f6d6bd}the innkeeper{/color} is already starting a fire in the stove. He asks if you need anything.
            '
            '(iason1 set)':
                pass

label peltnorthaftersleeproom:
    nvl clear
    show areapicture peltnorth01inside at basicfade
    hide peltnorthbronzerod
    $ peltnorth_guards_fluff = renpy.random.choice(['playing with their boar, patting its side and feeding it', 'spread across the wall, observing the area', 'training with spears and staffs in the courtyard', 'training with wooden swords and blunt axes in the courtyard', 'sitting at a table and on the stairs, gossiping with mugs of beer in their hands', 'practicing archery and fixing their equipment in the courtyard', 'are by the well, arguing with each other', 'sitting at a table, gambling for apples', 'splitting firewood and weeding the garden patches'])
    $ peltnorth_guards_fluff_old = peltnorth_guards_fluff
    $ peltnorth_horsename_fluff = renpy.random.choice(['enjoying some old hay', 'napping', 'looking around', 'moving around slowly, as far as its cord allows', 'pawing the ground', 'fighting off flies with its tail', 'lazily looking around'])
    $ peltnorthroomdescription = renpy.random.choice(['The windows are locked, but the counter is lit with candles.', 'The weak fire in the stove hardly lightens up the hall.', 'The windows are locked, and several guards are sleeping in a corner.'])
    $ iason_stance = "sittingatstove"
    $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is sitting at the stove, cleaning a set of metal tools and ladles.', 'Several guards are eating gruel and talking with {color=#f6d6bd}the innkeeper{/color} at the stove.', '{color=#f6d6bd}The innkeeper{/color} is sitting on a stool, looking at the flames in the stove and holding a carrot and a knife without using them.', '{color=#f6d6bd}The innkeeper{/color} is mixing something in a pot at the stove.'])
    $ peltnorth_iason_fluff_old = peltnorth_iason_fluff
    $ randommeal = renpy.random.choice(['a bowl of simple gruel and a mug of ale', 'fresh rye bread and an old grain beer with an intense smell of yeast', 'old rye bread, a fistful of nuts, and a fresh grain beer', 'old, toasted bread and a large slice of mouflon cheese', 'a nettle tisane and a simple root stew with hardly any meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a slice of rye bread', 'bacon, an apple, and a cup of birch sap', 'flatbread with butter and an herbal dip sauce', 'a baked, cold pheasant breast and a raw eggplant', 'a roasted rat with a mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water'])
    $ randomgoodmeal = renpy.random.choice(['fresh rye bread, a sausage, a bowl of berries, and a mug of malty beer', 'a decent stew with white bread to dip', 'a fried salmon in sorrel sauce and a bowl of gruel', 'two boiled eggs, a cup of buttermilk, and some ibex offals', 'a bowl of oatmeal based on ibex milk, with berries, nuts, and honey', 'a fresh pie with deer meat, onions, and coriander', 'baked artichokes with a weird, but tasty, roasted lizard', 'an eggplant soup, a bowl of pears, and some crumbly biscuits', 'a raw cabbage head, a smoked quail wing, and a cup of yogurt', 'a pie with hare and cabbage, a bowl of plums and grapes, and a cup of mouflon milk', 'a cup of mint tisane, three duck eggs, and baked duck meat', 'fried, breaded mushrooms with gravy and chamomile tisane', 'a warm mutton stew and a cold yogurt'])
    if pyrrhos_peltnorth == 1:
        if description_pyrrhos01:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
        else:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}The scavenger{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
    else:
        $ pyrrhos_peltnorth_fluff = ""
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ shortcut_bandit_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The man without a name{/color} is sharpening a curved dagger used for shaving. ', '{color=#f6d6bd}The man without a name{/color} is plucking the feathers from a dead pigeon. ', '{color=#f6d6bd}The man without a name{/color} is washing his gambeson. ', '{color=#f6d6bd}The man without a name{/color} is sitting at the stove, lost in his thoughts. When he glances at you, his eyes are absent. ', '{color=#f6d6bd}The man without a name{/color} is sitting next to a couple of empty mugs, smiling to himself. ', '{color=#f6d6bd}The man without a name{/color} is washing his boots. '])
    else:
        $ shortcut_bandit_peltnorth_fluff = ""
    if quintus_pelt_firsttime and not quintus_pelt_left:
        $ quintus_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Quintus{/color} is playing with an empty mug. ', '{color=#f6d6bd}Quintus{/color} smiles at you from above a mug. ', '{color=#f6d6bd}Quintus{/color} is trying to fix a shirt with a crude bone needle. ', '{color=#f6d6bd}Quintus{/color} is washing his black gambeson, humming to himself. He glances at you with a smile. ', '{color=#f6d6bd}Quintus{/color} casts sad glances toward a hunter who’s eating a fresh roast. ', '{color=#f6d6bd}Quintus{/color} is napping in the corner. '])
    else:
        $ quintus_peltnorth_fluff = ""
    if tulia_pelt_inside and not tulia_pelt_left:
        $ tulia_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Tulia{/color} is sitting in the corner, flinching at every loud noise. ', '{color=#f6d6bd}Tulia{/color} is chopping vegetables, from time to time taking them to the innkeep. ', '{color=#f6d6bd}Tulia{/color} is keeping her sword on the top of the table, spinning it in place. ', '{color=#f6d6bd}Tulia{/color} glances at you from a corner as she’s inspecting her sparse possessions. ', '{color=#f6d6bd}Tulia{/color} exchanges a few words with one of the hunters. Her voice carries sadness, but she’s standing upright. ', '{color=#f6d6bd}Tulia{/color} is looking through a window. ', '{color=#f6d6bd}Tulia{/color} is observing her sparse hair in the mirror - or rather, the back of a plate. '])
    else:
        $ tulia_peltnorth_fluff = ""
    if iason_food_day != day:
        $ iason_food_day = day
        $ iason_food_roll = 0
        $ iason_food_roll = renpy.random.randint(1, 100)
    $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ renpy.music.play("audio/track_07peltnorth.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    $ questionpreset = "iason1"
    if shortcut_darkforest_bandit_inpeltnorth and not iason_about_shortcut_bandit and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ iason_about_shortcut_bandit = 1
        $ shortcut_bandit_identity = 1
        $ iason_friendship += 1
        $ iason_friendship_moneybonus_points += 3
        $ banditshideout_bandits_pchearedabout = 1
        menu:
            'The small room is quiet and far away from unwanted eyes. You take a calm bath, rest on a soft mattress, look through the window, and enjoy the minutes of safety.
            \n\nIn the morning, you find a stool with a large, wooden plate, bearing an aromatic breakfast - [randomgoodmeal]. Downstairs, {color=#f6d6bd}the innkeeper{/color} is looking toward {color=#f6d6bd}the man you found at the shortcut{/color}. His voice is thoughtful.
            \n\n“Weird times, hm? I was hoping to learn more about the bandits, and now one of them is right here, drinking my ale. Too bad he doesn’t talk,” he glances toward you. “He said he knows you, that you faced some beasts... I mean, coin is coin, but couldn’t you bring me some merchants instead?”
            '
            '(iason1 set)':
                pass
    else:
        menu:
            'The small room is quiet and far away from unwanted eyes. You take a calm bath, rest on a soft mattress, look through the window, and enjoy the minutes of safety.
            \n\nIn the morning, you find a stool with a large, wooden plate, bearing an aromatic breakfast - [randomgoodmeal]. Downstairs, {color=#f6d6bd}the innkeeper{/color} is putting firewood into the stove. He asks if you need anything.
            '
            '(iason1 set)':
                pass

label peltnorthafterrelaxing01:
    nvl clear
    show areapicture peltnorth01inside at basicfade
    hide peltnorthbronzerod
    $ peltnorth_guards_fluff = renpy.random.choice(['playing with their boar, patting its side and feeding it', 'spread across the wall, observing the area', 'training with spears and staffs in the courtyard', 'training with wooden swords and blunt axes in the courtyard', 'sitting at a table and on the stairs, gossiping with mugs of beer in their hands', 'practicing archery and fixing their equipment in the courtyard', 'are by the well, arguing with each other', 'sitting at a table, gambling for apples', 'splitting firewood and weeding the garden patches'])
    $ peltnorth_guards_fluff_old = peltnorth_guards_fluff
    $ peltnorth_horsename_fluff = renpy.random.choice(['enjoying some old hay', 'napping', 'looking around', 'moving around slowly, as far as its cord allows', 'pawing the ground', 'fighting off flies with its tail', 'lazily looking around'])
    $ peltnorthroomdescription = renpy.random.choice(['The windows are open, and while there’s a few guards eating and drinking, the hall is clean.', 'The open windows fill the hall with refreshing air and the sounds of conversation.', 'Sitting beneath an open window, three guards are arguing about something, but then ease the tension with friendly banter.'])
    $ iason_stance = "behindcounter"
    $ peltnorth_iason_fluff = renpy.random.choice(['{color=#f6d6bd}The innkeeper{/color} is dusting the counter and the shelves with a cloth.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, contemplating an empty mug.', '{color=#f6d6bd}The innkeeper{/color} is sitting behind the counter, cutting vegetables.', '{color=#f6d6bd}The innkeeper{/color} is standing behind the counter, preparing a set of mugs.', '{color=#f6d6bd}The innkeeper{/color} is leaning on the counter, dividing a small pile of dragon bones.'])
    $ peltnorth_iason_fluff_old = peltnorth_iason_fluff
    if pyrrhos_peltnorth == 1:
        if description_pyrrhos01:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
        else:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}The scavenger{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
    else:
        $ pyrrhos_peltnorth_fluff = ""
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
        $ shortcut_darkforest_bandit_inpeltnorthpcknowsabout = 1
    if shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll:
        $ shortcut_bandit_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The man without a name{/color} is sharpening a curved dagger used for shaving. ', '{color=#f6d6bd}The man without a name{/color} is plucking the feathers from a dead pigeon. ', '{color=#f6d6bd}The man without a name{/color} is washing his gambeson. ', '{color=#f6d6bd}The man without a name{/color} is sitting at the stove, lost in his thoughts. When he glances at you, his eyes are absent. ', '{color=#f6d6bd}The man without a name{/color} is sitting next to a couple of empty mugs, smiling to himself. ', '{color=#f6d6bd}The man without a name{/color} is washing his boots. '])
    else:
        $ shortcut_bandit_peltnorth_fluff = ""
    if quintus_pelt_firsttime and not quintus_pelt_left:
        $ quintus_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Quintus{/color} is playing with an empty mug. ', '{color=#f6d6bd}Quintus{/color} smiles at you from above a mug. ', '{color=#f6d6bd}Quintus{/color} is trying to fix a shirt with a crude bone needle. ', '{color=#f6d6bd}Quintus{/color} is washing his black gambeson, humming to himself. He glances at you with a smile. ', '{color=#f6d6bd}Quintus{/color} casts sad glances toward a hunter who’s eating a fresh roast. ', '{color=#f6d6bd}Quintus{/color} is napping in the corner. '])
    else:
        $ quintus_peltnorth_fluff = ""
    if tulia_pelt_inside and not tulia_pelt_left:
        $ tulia_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Tulia{/color} is sitting in the corner, flinching at every loud noise. ', '{color=#f6d6bd}Tulia{/color} is chopping vegetables, from time to time taking them to the innkeep. ', '{color=#f6d6bd}Tulia{/color} is keeping her sword on the top of the table, spinning it in place. ', '{color=#f6d6bd}Tulia{/color} glances at you from a corner as she’s inspecting her sparse possessions. ', '{color=#f6d6bd}Tulia{/color} exchanges a few words with one of the hunters. Her voice carries sadness, but she’s standing upright. ', '{color=#f6d6bd}Tulia{/color} is looking through a window. ', '{color=#f6d6bd}Tulia{/color} is observing her sparse hair in the mirror - or rather, the back of a plate. '])
    else:
        $ tulia_peltnorth_fluff = ""
    if iason_food_day != day:
        $ iason_food_day = day
        $ iason_food_roll = 0
        $ iason_food_roll = renpy.random.randint(1, 100)
    $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    if pc_relax_dayof < (day-8):
        $ pc_relax_fluff = "Turns out the rest was much more necessary than you’d expected. Your belongings are a mess, the sacks and the blanket have too many holes to count, and you spend a good hour brushing and cleaning your mount. At the end of the day, you’re still a bit tired, but at least you feel prepared."
    elif pc_relax_dayof < (day-4):
        $ pc_relax_fluff = "You were pretty busy today, but not exhaustingly so. Taking care of your mount, as well as all the patches, scratches, bandages, and the general mess among your possessions took some reorganizing, but at the end of the day your muscles are grateful for not spending hours on riding."
    elif pc_relax_dayof < (day-2):
        $ pc_relax_fluff = "It’s been a relaxing day, but free of boredom. You spent almost an hour looking after your mount, but at least it’s now clean and cheerful. You patch holes in your bundles to the soothing sounds of a late summer drizzle."
    else:
        $ pc_relax_fluff = "It’s been a lazy day. Repairing your equipment and taking care of your mount didn’t take nearly as much time as you'd expected, and you instead enjoy some refreshing water, observe your surroundings with a clear head, wander about, and stretch out. After a few hours, you feel rather bored, but at least you have an opportunity to gather your thoughts."
    $ pc_relax_dayof = day
    label peltnorth_relaxing_fluffloop:
        $ peltnorth_relaxing_fluff = ""
        $ peltnorth_relaxing_fluff = renpy.random.choice(['Some of the hunters occupied the watchtower, while the rest of the group went after some big game beyond the walls.', 'Every now and then, the hunters invited you to a friendly chit-chat, asking you for stories from the wide world.', 'At one point, the innkeep invited you for a drink, asking you about the news.', 'At one point, you were invited to some friendly combat practice with the hunters, and you made sure to not take it too easy.'])
        if peltnorth_relaxing_fluff_old == peltnorth_relaxing_fluff:
            jump peltnorth_relaxing_fluffloop
        else:
            $ peltnorth_relaxing_fluff_old = peltnorth_relaxing_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    menu:
        '[pc_relax_fluff] [peltnorth_relaxing_fluff]
        \n\n[peltnorthroomdescription] [peltnorth_iason_fluff] [pyrrhos_peltnorth_fluff][quintus_peltnorth_fluff][shortcut_bandit_peltnorth_fluff][tulia_peltnorth_fluff]
        '
        'I go to {color=#f6d6bd}the innkeeper{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the innkeeper{/color}.')
            jump peltnorth01insidetalkingwithiasonalt
        'I join {color=#f6d6bd}Tulia{/color}.' if tulia_pelt_inside and not tulia_pelt_left:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I join {color=#f6d6bd}Tulia{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithtulia01
        'I approach {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_peltnorth == 1 and description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithpyrrhos
        'I approach {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_peltnorth == 1 and not description_pyrrhos01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithpyrrhos
        'I speak to {color=#f6d6bd}the man without a name{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and not shortcut_bandit_identity:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the man without a name{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithbandit
        'I speak to {color=#f6d6bd}the bandit{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and shortcut_bandit_identity:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the bandit{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithbandit
        'I step toward {color=#f6d6bd}Quintus{/color}.' if quintus_pelt_firsttime and not quintus_pelt_left:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step toward {color=#f6d6bd}Quintus{/color}.')
            $ can_rest = 0
            jump peltnorth01insidetalkingwithquintus01
        'I go outside.':
            $ can_rest = 0
            $ can_items = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump leavingthepeltnorth

label peltnorthleftoversquestforberries02:
    if quarters <= (world_daylength-5):
        show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
    else:
        show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
    if eudocia_bronzerod_rodin_peltnorth:
        show peltnorthbronzerod at basicfade
    $ peltnorth_guards_fluff = renpy.random.choice(['playing with their boar, patting its side and feeding it', 'spread across the wall, observing the area', 'training with spears and staffs in the courtyard', 'training with wooden swords and blunt axes in the courtyard', 'sitting at a table and on the stairs, gossiping with mugs of beer in their hands', 'practicing archery and fixing their equipment in the courtyard', 'are by the well, arguing with each other', 'sitting at a table, gambling for apples', 'splitting firewood and weeding the garden patches'])
    $ peltnorth_guards_fluff_old = peltnorth_guards_fluff
    $ peltnorth_horsename_fluff = renpy.random.choice(['enjoying some old hay', 'napping', 'looking around', 'moving around slowly, as far as its cord allows', 'pawing the ground', 'fighting off flies with its tail', 'lazily looking around'])
    if pyrrhos_peltnorth == 1:
        $ pyrrhos_peltnorth_fluff = ""
        if description_pyrrhos01:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}Pyrrhos{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}Pyrrhos{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}Pyrrhos{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
        else:
            $ pyrrhos_peltnorth_fluff = renpy.random.choice(['{color=#f6d6bd}The scavenger{/color} is nearby, talking quietly with the innkeeper. ', '{color=#f6d6bd}The scavenger{/color} is sitting on a stool, using his knife to turn a log of wood into a new cup. ', '{color=#f6d6bd}The scavenger{/color} is sitting in a corner, napping, though he winks at you when you look toward him. ', '{color=#f6d6bd}The scavenger{/color} is sitting at a table, eating something from a bowl. ', '{color=#f6d6bd}The scavenger{/color} is leaning against a wall, with arms crossed, though he nods toward you when you enter. '])
    $ quarters += 3
    $ can_items = 0
    $ can_leave = 0
    $ can_rest = 0
    $ at = 0
    if pc_class == "scholar":
        $ at_unlock_knowledge = 1
    menu:
        '{color=#f6d6bd}The innkeeper{/color} knew what he was talking about. You put on the gloves and look through the bushes from a safe distance. It doesn’t take long before you notice the first serpent lying on a rock somewhere in the thicket. The creatures are not that large, and even if some of them hiss at you or slither closer, the jabs of the hook keep them at a distance.
        \n\nYou don’t know much about these berries. They are round and reddish - you wouldn’t trust such a color even if you were looking for food in the wilderness. The plants don’t have thorns, but the leaves are harsh, so you make sure to thoroughly cover your skin with your clothes. You have to look through many bushes to fill the bucket, but the presence of insects and snakes doesn’t allow you to relax.
        '
        'I gather the berries and go back to the inn.' ( condition="at != 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather the berries and go back to the inn.')
            $ at_unlock_knowledge = 0
            jump peltnorthleftoversquestforberries03
        'I notice a shrub that’s not like the others.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I notice a shrub that’s not like the others.')
            $ at_unlock_knowledge = 0
            $ at = 0
            $ item_marshbules += 1
            $ renpy.notify("You added marshbules to your bag of ingredients.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added marshbules to your bag of ingredients.{/i}')
            menu:
                'One of the bushes in the back has more berries than the others. They’re purple, and as you squeeze one of them, you recognize that these are marshbules. In small amounts, they are added to pies, sauces, and beverages, known for their delicate sourness and sweetness, unique, but not intrusive. Still, eating a cup of them will make one sick, if not poisoned. You’re surprised to see them in a meadow, far away from a wetland.
                \n\nYou could use them at an alchemy table, if you can find it. For now, you put a fistful into one of your jars. The others are still a bit greenish.
                '
                'I gather the berries and return to the gate.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather the berries and return to the gate.')
                    jump peltnorthleftoversquestforberries03

    label peltnorthleftoversquestforberries03:
        $ can_leave = 1
        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        $ at_unlock_knowledge = 0
        if quarters <= (world_daylength-5):
            show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        else:
            show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
        $ item_peltnorthberries = 1
        $ renpy.notify("You’ve gathered a bucketful of berries.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve gathered a bucketful of berries.{/i}')
        menu:
            'You’ve returned to the courtyard. Two of the guards are participating in a friendly skirmish. Their wrestling is accompanied by a crowd.
            '
            'I enter the inn.':
                show areapicture peltnorth01inside at basicfade
                hide peltnorthbronzerod
                $ shop = "peltnorth"
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                jump peltnorth01insidetalkingwithiason

label peltnorthwell01:
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
        'The recently renovated wooden roof covers the well from rain and birds. One of the guards is enjoying the cold drink he drew with a bucket, and tells you to use only as much water as is necessary.
        \n\n[custom1][custom2]
        '
        'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
            jump peltnorthwellwashing01
        'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump peltnorthwellwashing01
        'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
            jump peltnorthwellwashing01
        'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.' if cleanliness_clothes_blood:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.')
            jump peltnorthwelllaundry01
        'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump leavingthepeltnorth02

    label peltnorthwellwashing01:
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
            'Splashing yourself with cold water from a bucket won’t take away your smell, but it’s enough to remove the tallow and sweat from your skin, or mud stains from your clothes.
            '
            'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
                jump peltnorthwellwashing01
            'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump peltnorthwellwashing01
            'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump peltnorthwellwashing01
            'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.')
                jump peltnorthwelllaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump leavingthepeltnorth02

    label peltnorthwelllaundry01:
        $ cleanliness_clothes_blood = 0
        $ quarters += 8
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'Soaking, pounding, and rubbing the fabric while you hold it above the dusty ground takes a lot of effort, especially without flowing water.
            '
            'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
                jump peltnorthwellwashing01
            'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump peltnorthwellwashing01
            'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
                jump peltnorthwellwashing01
            'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.' if cleanliness_clothes_blood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not a convenient spot, but in two hours I can remove the blood stains from my clothes.')
                jump peltnorthwelllaundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump leavingthepeltnorth02
