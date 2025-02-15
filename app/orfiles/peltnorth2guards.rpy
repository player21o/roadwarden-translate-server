default dalit_friendship = 0
default dalit_firstattitude = 0
default dalit_friendship_comment = 0
default dalit_friendship_tier2 = 15
default dalit_friendship_tier3 = 25
default dalit_name = "the guard in yellow armor"
default dalit_about_name = 0
default dalit_about_name_gray = 0
default dalit_firsttime = 0
default dalit_dayofvisit = 0

default dalit_about_highisland_recruitment = 0
default dalit_about_highisland_recruitment_done = 0
default dalit_highisland_joined = 0
default dalit_about_highisland_payment_threshold = 0
default dalit_about_highisland_payment_threshold_base = 40

default dalit_bestiary_bugs = 0
default dalit_bestiary_beastfolk = 0
default dalit_bestiary_dragonlings = 0
default dalit_bestiary_dragon = 0
default dalit_bestiary_ghouls = 0
default dalit_bestiary_gargoyles = 0
default dalit_bestiary_goblins = 0
default dalit_bestiary_golems = 0
default dalit_bestiary_griffons = 0
default dalit_bestiary_harpies = 0
default dalit_bestiary_howlers = 0
default dalit_bestiary_pebblers = 0
default dalit_bestiary_spiders = 0
default dalit_bestiary_trolls = 0
default dalit_bestiary_undead = 0
default dalit_bestiary_undead_light = 0
default dalit_bestiary_huntlords = 0
default dalit_bestiary_birds = 0
default dalit_bestiary_treants = 0
default dalit_bestiary_wolves = 0
default dalit_bestiary_apes = 0
default dalit_bestiary_largecats = 0
default dalit_bestiary_fisheater = 0
default dalit_bestiary_howlersandmeat = 0
default dalit_bestiary_mediumcritters = 0
default dalit_bestiary_saurians = 0
default dalit_bestiary_unicorns = 0

default dalit_dice = 0
default dalit_dice_never = 0
default dalit_axes = 0
default dalit_pc_debt = 0
default dalit_pc_debt_timer = 0
default dalit_pc_tools = 0
default dalit_about_goblins = 0
default dalit_about_goblins_timer = 0
default dalit_about_goblins_timer_display = 0
default dalit_about_goblins_price_base = 15
default dalit_about_goblins_price = 0
default dalit_about_goblins_participation = 0
default dalit_about_berries = 0
default dalit_about_druids = 0
default dalit_about_pyrrhos = 0
default dalit_about_tulia = 0
default dalit_about_ilan = 0
default dalit_about_shortcut = 0
default dalit_about_highisland = 0
default dalit_about_missinghunters = 0
default dalit_about_fish = 0
default dalit_about_arrow = 0

default dalit_about_quintus = 0
default dalit_about_quintus2 = 0

default dalit_about_wildcreatures = 0
default dalit_beastiary_unlocked = 0
default dalit_beastiary_discount = 0
default dalit_beastiary_discount_ilan = 0
default dalit_beastiary_price_base = 15
default dalit_beastiary_price = 15

default dalit_about_minorquestionALL = 0
default dalit_about_tower = 0
default dalit_about_creatures = 0
default dalit_about_hunting = 0
default dalit_about_north = 0
default dalit_about_necromancers = 0
default dalit_about_boar = 0

label dalit_firsttimeALL:
    label dalit_firsttime01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ dalit_dayofvisit = day
        menu:
            '{color=#f6d6bd}The woman in yellow armor{/color} is kneeling next to a brown, hairy boar, which is resting on its side. The beast is not as large as the dark ones from the forests. It responds to the touch of the human’s hand and brush with grateful grunting and rapid twitches of a hind hoof. No matter how friendly it appears, it’s still tethered to the well, and you have no doubts that its charge would leave {color=#f6d6bd}[horsename]{/color} dead in a breath.
            \n\nWhen the woman notices you, she steps forward, to the boar’s disappointment. “So, the new roadwarden?” She points at a window with her chin, forestalling the question. “We don’t need anything now, but when we travel with our furs, we can use some assistance.”
            \n\nShe may be around thirty, but her warm voice and bright smile are camouflaging the touch of time on her unpowdered face. Like many red-haired people with freckles, her skin is unhealthily pale.
            \n\nThe boar runs up to her, observing your boots and fruitlessly sniffing for food beneath the beaten ground. She pats its back, but maintains her focus. “How about a game or two? We have a bit of time and can talk a bit about this and that, maybe you’ll get a couple of coins. Or lose one.” She winks. “We could play dice, or throw axes at a target.”
            '
            '{image=d6} “Sure, let’s play some dice.”' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Sure, let’s play some dice.”')
                $ quarters += 1
                $ dalit_friendship += 1
                $ dalit_dice = day
                jump dalit_firsttime01diceA
            '{image=d6} “Axe throwing? Show me what you’ve got.”' if coins and pc_hp >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Axe throwing? Show me what you’ve got.”')
                $ quarters += 1
                $ dalit_friendship += 1
                jump sdalit_firsttime01axeA
            'I’m too tired to throw axes for half an hour. (Required vitality: 2) (disabled)' if pc_hp <= 1:
                pass
            'I have no coins. (disabled)' if not coins:
                pass
            '“I don’t really have time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t really have time.”')
                $ questionpreset = "dalit1"
                menu:
                    '“Right, I kind of thought so,” her smile disappears. She returns to the other guards. “Roadwardens are always busy, ain’t they? Better hope you’ll have a day of rest sometime.”
                    '
                    '(dalit1 set)':
                        pass
            '“I don’t gamble.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t gamble.”')
                $ dalit_dice_never = 1
                $ questionpreset = "dalit1"
                menu:
                    '“Oh, I wouldn’t call it gambling, just a couple of games,” her smile disappears. She returns to the other guards. “Finding anything fun to do in this hole ain’t easy. Last time I saw a bard from the South... I don’t remember when it was.”
                    '
                    '(dalit1 set)':
                        pass

    label dalit_firsttime01diceA:
        if creeks_youth_gambling < 2:
            $ custom1 = "The game is new to you, but in no way baffling. Four people can play at once. The wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
        else:
            $ custom1 = "The game has similar rules to the one you’ve played in {color=#f6d6bd}Creeks{/color}, but this time four people can play at once, and the wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
        menu:
            'Your arrival, and especially the dragon bone you pull out, are cheerfully welcomed. Two of the guards bring a table from the inn, another one prepares a couple of stools and chairs. There are also spectators, and you’re told that the other hunters are either sleeping, or have duty on the tower. “Remember, no magic,” says one of the players. His face is deadly serious.
            \n\n[custom1]
            '
            'I blend in with the group.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blend in with the group.')
                $ at = 0
                if pc_class == "scholar":
                    $ at_unlock_knowledge = 1
                menu:
                    'You share casual jokes, memories, and views on luck and optimal strategies. {color=#f6d6bd}[horsename]{/color} and {color=#f6d6bd}Tulia’s{/color} camp are also brought up, but when you ask about the roads or the locals, their stories are vague.
                    \n\nThe drinks are here. It’s a poor beer made from the leftovers after the regular brewing. It’s cold, sweet, and doesn’t reach your head, but you try to avoid the smell. “Just don’t spill anything, the boar may get sick,” says your bald opponent.
                    \n\nIn just a few minutes you get two points, which are now represented by smooth pebbles. You don’t really know how you got them. Either you don’t get the strategy, or it’s just pure luck.
                    '
                    '{image=d6} Let’s see how lucky I am.' ( condition="at != 'knowledge'" ):
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        $ at = 0
                        $ at_unlock_knowledge = 0
                        $ quarters += 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Let’s see how lucky I am.')
                        jump dalit_firsttime01diceB
                    '{image=d6} There’s a strategy to this game, I can see it. I can’t be sure I’ll win, but I can play better than they expect.' ( condition="at == 'knowledge'"):
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        $ pc_gamblingxp += 15
                        $ pc_gamblingxp_scholarbonus = 1
                        $ at = 0
                        $ at_unlock_knowledge = 0
                        $ quarters += 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} There’s a strategy to this game, I can see it. I can’t be sure I’ll win, but I can play better than they expect.')
                        jump dalit_firsttime01diceB

    label dalit_firsttime01diceB:
        $ iason_friendship_moneybonus_points += 1
        $ questionpreset = "dalit1"
        if d100roll-pc_gamblingxp > 75:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_gamblingxp += 3
            menu:
                'Your score is the lowest. You move a dragon bone to the bold, quiet man with wide nostrils, who has the grin of a wolf. After the table and the chairs are moved back into the building, {color=#f6d6bd}[dalit_name]{/color} asks if she can help you with anything.
                '
                '(dalit1 set)':
                    pass
        elif d100roll-pc_gamblingxp > 50:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_gamblingxp += 3
            menu:
                'After a long series of bad rolls you finish with two points, the second-lowest score. You put a dragon bone in front of {color=#f6d6bd}[dalit_name]{/color}, whose comically exaggerated thanks are met with laughter. After the table and the chairs are moved back into the building, she asks if you need anything.
                '
                '(dalit1 set)':
                    pass
        elif d100roll-pc_gamblingxp > 25:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_gamblingxp += 3
            menu:
                'Your score is second-best. “Nice one,” you hear from the man with a fancily braided beard, who reaches to pick up your dragon bone. As the table and the chairs are carried back into the building, {color=#f6d6bd}[dalit_name]{/color} looks at you with a smile.
                '
                '(dalit1 set)':
                    pass
        else:
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_gamblingxp += 5
            menu:
                'During the final round you get ahead of everyone, and the spectators playfully comment on your moves. The winner takes all - three dragons are placed on the table and you put them into your pouch quickly.
                \n\nThe table and chairs are moved back into the building and {color=#f6d6bd}[dalit_name]{/color} thanks you for playing. “Is there anything you need?”
                '
                '(dalit1 set)':
                    pass

    label sdalit_firsttime01axeA:
        $ iason_friendship_moneybonus_points += 1
        menu:
            'Your arrival, and especially the dragon bone you pull out, are cheerfully welcomed. The guards prepare a couple of wooden planks, which are leaned against the wall. There are also spectators, and you’re told that the other hunters are either sleeping, or have duty on the tower. “Remember, no magic,” says one of the players. His face is deadly serious.
            \n\nThere’s going to be four participants and eight rounds. You aim at the target drawn with charcoal. The person whose axe lands the closest to the center of the circle gets a point. Axes that fail to stay in the plank don’t count. The person who has the most points at the end of the last turn becomes the winner.
            '
            'I blend in with the group.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blend in with the group.')
                $ at = 0
                if pc_class == "warrior":
                    $ at_unlock_force = 1
                menu:
                    'You talk a lot, but also don’t say much. You share casual jokes, memories, and views on luck and optimal strategies. {color=#f6d6bd}[horsename]{/color} and {color=#f6d6bd}Tulia’s{/color} camp are also brought up, but when you ask about the roads or the locals, their stories are vague.
                    \n\nThe drinks are here. It’s a poor beer made from the leftovers after the regular brewing. It’s cold, sweet, and doesn’t reach your head, but you try to avoid the smell. “Just don’t spill anything, the boar may get sick,” says the opponent with one arm.
                    \n\nAs a guest, you start with the first throw. Your axe flies well, hitting the very middle of the painted target and piercing the plank with a pleasant thud, which makes it really difficult for the other players to outperform you. A minute later, you’ve won the first round, but you can’t expect to be that lucky every time.
                    '
                    '{image=d6} All I can do is try my best.' ( condition="at != 'force'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} All I can do is try my best.')
                        $ at = 0
                        $ at_unlock_force = 0
                        $ quarters += 1
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        if pc_hp >= 4:
                            $ d100roll -= 15
                        elif pc_hp == 3:
                            $ d100roll -= 5
                        elif pc_hp <= 1:
                            $ d100roll += 10
                        if not pc_food:
                            $ d100roll += 5
                        if pc_food == 3:
                            $ d100roll -= 5
                        if pc_food == 4:
                            $ d100roll -= 15
                        if item_axe03:
                            $ d100roll -= 15
                        elif item_axe02 or item_axe02alt:
                            $ d100roll -= 5
                        $ custom6 = (pc_throwingxp*3)
                        if custom6 > 30:
                            $ custom6 = 30
                        $ d100roll -= custom6
                        jump dalit_firsttime01axethrow
                    '{image=d6} I’ve trained in axe throwing for years. I’ve got this.' ( condition="at == 'force'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve trained in axe throwing for years. I’ve got this.')
                        $ at = 0
                        $ at_unlock_force = 0
                        $ quarters += 1
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 80)
                        if pc_hp >= 4:
                            $ d100roll -= 15
                        elif pc_hp == 3:
                            $ d100roll -= 5
                        elif pc_hp <= 1:
                            $ d100roll += 10
                        if not pc_food:
                            $ d100roll += 5
                        if pc_food == 3:
                            $ d100roll -= 5
                        if pc_food == 4:
                            $ d100roll -= 15
                        if item_axe03:
                            $ d100roll -= 15
                        elif item_axe02 or item_axe02alt:
                            $ d100roll -= 5
                        $ custom6 = (pc_throwingxp*3)
                        if custom6 > 30:
                            $ custom6 = 30
                        $ d100roll -= custom6
                        jump dalit_firsttime01axethrow

    label dalit_firsttime01axethrow:
        $ iason_friendship_moneybonus_points += 1
        $ dalit_axes = day
        $ questionpreset = "dalit1"
        if d100roll > 75:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'You finish with only one point. You cast a dragon bone at a massive woman, who stops her winning dance only briefly, surrounded by the rhythmic clapping of her crew. You’re approached by {color=#f6d6bd}[dalit_name]{/color} and her wholehearted laughter.
                '
                '(dalit1 set)':
                    pass
        elif d100roll > 50:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'After a long series of misses you finish with one point, the second-last place. You give the gasping winner your dragon bone. “Cheers,” he says, but doesn’t make a big deal out of it. The light-hearted comments of the other losers lighten up the mood, and {color=#f6d6bd}[dalit_name]{/color} approaches you with a smile.
                '
                '(dalit1 set)':
                    pass
        elif d100roll > 25:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'Even though you get two points, {color=#f6d6bd}[dalit_name]{/color} gets one more. “Yes!” She raises her fist and nods to the spectators, who chuckle at her cheeky pride. After you give her your coin, she looks you in the eyes with a smile.
                '
                '(dalit1 set)':
                    pass
        else:
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_throwingxp += 2
            menu:
                'After getting your fourth point, the other players nod with respect. “Quite a score,” you hear from {color=#f6d6bd}[dalit_name]{/color} as she hands you your dragon bones. The other participants carry away the remaining planks.
                '
                '(dalit1 set)':
                    pass

####################################################
label peltnorthtalkingwithguards01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ questionpreset = "dalit1"
    if dalit_dayofvisit != day:
        $ dalit_dayofvisit = day
        if quintus_pelt_firsttime and not quintus_pelt_left and not dalit_about_quintus2:
            $ dalit_about_quintus2 = 1
            menu:
                'The boar greets you with an oink, making {color=#f6d6bd}[dalit_name]{/color} giggle. “So it’s you who brought that stubborn ibex here? You saved his life, [pcname]. Now what {i}we’ve{/i} got to do is convince him to use more soap.” She covers her nose exaggeratedly. “These are not {i}the wilds{/i} anymore,” she mimics his {color=#f6d6bd}Quintus’{/color} accent.
                '
                '(dalit1 set)':
                    pass
        elif tulia_pelt_inside and not tulia_pelt_left and not dalit_about_tulia:
            $ dalit_about_tulia = 1
            menu:
                'The boar is resting on the ground, demanding {color=#f6d6bd}[dalit_name]’s{/color} patting. The huntress looks gives you a sad glance. “The trolls are back,” she states simply, and you run your eyes over her companions. They are unusually quiet.
                '
                '(dalit1 set)':
                    pass
        elif dalit_about_pyrrhos and not pyrrhos_peltnorth:
            $ dalit_about_pyrrhos = 1
            $ dalit_friendship += 1
            menu:
                'The boar gets closer, followed by {color=#f6d6bd}[dalit_name]{/color}. “I’m glad you helped that vagabond. He’s silly, but he trades and has a job for us. Cheers, [pcname]. Boss would thank you as well, if his tongue weren’t burnt whenever it carries a warm word.”
                '
                '(dalit1 set)':
                    pass
        elif iason_fish_delivered_total >= 12 and not dalit_about_fish:
            $ dalit_about_fish = 1
            $ iason_friendship_moneybonus_points += 1
            menu:
                'One of the guards is playing with fishbones, arranging them into a picture of a large ape. “Thanks for these, roadwarden,” he shouts at you as a greeting. {color=#f6d6bd}[dalit_name]{/color} steps forward with a kind smile. “I mean, they ain’t as tasty as game meat, but they’re different, and that matters. We may spend a part of winter learning how to make our own baskets.”
                '
                '(dalit1 set)':
                    pass
        elif iason_friendship_moneybonus_level2_given and not dalit_friendship_moneybonus_level2_reaction:
            $ dalit_friendship_moneybonus_level2_reaction = 1
            menu:
                'The hunters warmly greet you, and {color=#f6d6bd}[dalit_name]{/color} welcomes you with a shining smile. “Hi there! Our savings keep looking better the more often you visit us. So, you should do so every day!”
                '
                '(dalit1 set)':
                    pass
        elif iason_friendship_moneybonus_level4_given and not dalit_friendship_moneybonus_level4_reaction:
            $ dalit_friendship_moneybonus_level4_reaction = 1
            menu:
                'The boar rests on its side, pet by two of the guards, and your arrival is greeted by the entire group with kind calls. When {color=#f6d6bd}[dalit_name]{/color} shows up, she makes a comically exaggerated bow. “Our benefactor has arrived! Not satisfied with securing our purses yet?”
                '
                '(dalit1 set)':
                    pass
        elif dalit_friendship <= 1:
            menu:
                'The busy guards pay you no attention. You’re approached by {color=#f6d6bd}[dalit_name]{/color}, who keenly observes you and asks if you’re looking for someone.
                '
                '(dalit1 set)':
                    pass
        elif dalit_friendship <= 10:
            menu:
                'The guards greet you with polite nods or a casual {i}hello{/i}. When {color=#f6d6bd}[dalit_name]{/color} gets closer to you with a smile, the brown boar follows her steps. “What brings you to us?”
                '
                '(dalit1 set)':
                    pass
        else:
            $ quarters += 1
            menu:
                'The guards greet you enthusiastically by calling you by your name. A few of them join {color=#f6d6bd}[dalit_name]{/color} and the boar to gossip with you for a few minutes.
                '
                '(dalit1 set)':
                    pass
    else:
        menu:
            'You return to {color=#f6d6bd}[dalit_name]{/color}.
            '
            '(dalit1 set)':
                pass

label peltnorthtalkingwithguardsafterquestions:
    $ questionpreset = "dalit1"
    if dalit_name == "Dalit" and dalit_about_name:
        menu:
            '{color=#f6d6bd}[dalit_name]{/color} hooks a thumb behind her belt and smiles gently.
            '
            '(dalit1 set)':
                pass
    elif dalit_name == "Dalit" and not dalit_about_name:
        menu:
            '{color=#f6d6bd}[dalit_name]{/color} observes you with a hand casually resting on her hip.
            '
            '(dalit1 set)':
                pass
    else:
        menu:
            'She observes you with a hand casually resting on her hip.
            '
            '(dalit1 set)':
                pass

label peltnorthtalkingwithguardsdalit_namea:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
    $ custom1 = "She brushes away the hair from her forehead. The tangled chaos all over her scalp cares not for her efforts. “I’m {color=#f6d6bd}Dalit{/color}. Half my life ago I was living on crops, but I bet I’ve shot down more monsters than you’ve broken eggs. Are you much of a fighter?”"
    jump peltnorthtalkingwithguardsdalit_nameafter
    label peltnorthtalkingwithguardsdalit_nameaa:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to know more about you.”')
        $ custom1 = "She brushes away the hair from her forehead. The tangled chaos all over her scalp cares not for her efforts. “I’m {color=#f6d6bd}Dalit{/color}. Half my life ago I was living on crops, but I bet I’ve shot down more monsters than you’ve broken eggs. Are you much of a fighter?”"
        jump peltnorthtalkingwithguardsdalit_nameafter
    label peltnorthtalkingwithguardsdalit_nameb:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalit{/color}, right?”')
        $ custom1 = "She brushes away the hair from her forehead. The tangled chaos all over her scalp cares not for her efforts. “Well, yeah. Half my life ago I was living on crops, but I bet I’ve shot down more monsters than you’ve broken eggs. Are you much of a fighter?”"
        jump peltnorthtalkingwithguardsdalit_nameafter_after
    label peltnorthtalkingwithguardsdalit_nameafter:
        if (dalit_friendship+appearance_charisma) > 3:
            label peltnorthtalkingwithguardsdalit_nameafter_after:
                $ dalit_about_name = 1
                $ dalit_name = "Dalit"
                menu:
                    '“Oh?” She giggles to cover her confusion. “Are you asking me out? I ain’t interested in any silliness.”
                    \n\n[custom1]
                    \n\nMany more eyes turn toward you.
                    '
                    '“I don’t fight when I don’t have to.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t fight when I don’t have to.”')
                        $ questionpreset = "dalit1"
                        menu:
                            'While {color=#f6d6bd}Dalit{/color} starts to look around, the guards get back to their own affairs.
                            \n\n“I can’t say I see many folks seeking blood, but who knows what are good reasons to kill. Self-defense, filled belly, coins for medicine? If you don’t have the will to fight, I don’t think the roads here are good for you.”
                            \n\nAfter a short pause, she steps toward the noisy boar. “These roads are for loons. Loons and deerlegs.”
                            '
                            '(dalit1 set)':
                                pass
                    '“Hard to say. I’d rather have friendly blades on my side.”':
                        $ dalit_friendship += 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hard to say. I’d rather have friendly blades on my side.”')
                        $ questionpreset = "dalit1"
                        menu:
                            '“Same here,” says a man with a large scar on his cheek, while the rest of the group nods. One of the women mutters something you can’t hear, which the others welcome with a chuckle.
                            \n\n{color=#f6d6bd}Dalit{/color} glances at them, then smiles at you. “I never leave home without these goblinheads. No soul has told me to find {i}glory{/i} in killing, even if bards so often natter about it. I’ll take being alive any day, and a good team is of greater value than the best crossbow.”
                            '
                            '(dalit1 set)':
                                pass
                    '“If you live as a traveler, you face enemies. Not really an option.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you live as a traveler, you face enemies. Not really an option.”')
                        $ questionpreset = "dalit1"
                        menu:
                            'While {color=#f6d6bd}Dalit{/color} pats the boar, the guards get back to their own affairs.
                            \n\n“I guess. But there’s alway {i}an{/i} option. To stop the journey. One should always look for a new home.”
                            '
                            '(dalit1 set)':
                                pass
                    '“I fight to protect others. That’s my job.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I fight to protect others. That’s my job.”')
                        $ questionpreset = "dalit1"
                        menu:
                            'While {color=#f6d6bd}Dalit{/color} pats the boar, the guards get back to their own affairs.
                            \n\n“Hero material, huh? Ain’t something I’m going to be jealous about, this trade of yours. I had a cousin who tried to get rich as a roadwarden. She kept it together for maybe half a year. Was lucky enough to die in a village, not in the middle of nowhere. At least she han’t woken up, the good folk burned her on a proper pyre.”
                            '
                            '(dalit1 set)':
                                pass
                    '“There’s something... pleasing in triumph.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s something... pleasing in triumph.”')
                        $ questionpreset = "dalit1"
                        menu:
                            'The guards look at each other, then get back to their own affairs. {color=#f6d6bd}Dalit{/color} speaks slowly, weighing her words.
                            \n\n“I feel like it burns out, that rapture. When you practice the same steps, the same strikes for years and years, when you go on your fiftieth hunt... The blood turns dim, the screams get muffled. Probably what the large cats feel when they hunt. They ain’t ferocious, just efficient.”
                            '
                            '(dalit1 set)':
                                pass
        else:
            $ questionpreset = "dalit1"
            $ dalit_about_name_gray = 1
            menu:
                '“Oh, what was that?” After a brief giggle, her voice gets cold and serious. “Nah, roadwarden. We use names and stories among friends, you ain’t one. Don’t make me tempt curses.”
                '
                '(dalit1 set)':
                    pass

#################################################################
label peltnorthtalkingwithguardsberries:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The innkeep has asked me to forage for berries...”')
    $ dalit_about_berries = 1
    $ description_bighunters01 = "They are led by"
    $ description_iason04 = "According to"
    $ description_iason04b = ", he likes to give strangers small tasks to find out if they’re useful. And hates thieves."
    $ description_iason02 = "The leader of a team of big-game hunters."
    $ questionpreset = "dalit1"
    menu:
        'She chuckles. “Oh, don’t worry about it! Usually we forage by ourselves, but he wouldn’t ask you for a dragon for a meal. He gives small jobs to people all the time, just to see who agrees to do them. Wants to judge who’s of use and who’s too proud for their own good. If you’ve agreed, just be sure to get those berries today. And don’t try to take his tools away! He hates thieves.”
        '
        '(dalit1 set)':
            pass
    label peltnorthtalkingwithguardsberriesalt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was foraging for berries for the innkeep...”')
        $ dalit_about_berries = 1
        $ description_bighunters01 = "They are led by"
        $ description_iason04 = "According to"
        $ description_iason04b = ", he likes to give strangers small tasks to find out if they’re useful. And hates thieves."
        $ description_iason02 = "The leader of a team of big-game hunters."
        $ questionpreset = "dalit1"
        menu:
            'She chuckles. “So I’ve heard! Don’t worry about it. Usually we forage by ourselves, but he wouldn’t ask you for a dragon for a meal. He gives small jobs to people all the time, just to see who agrees to do them. Wants to judge who’s of use and who’s too proud for their own good.”
            '
            '(dalit1 set)':
                pass

#################################################################

label peltnorthtalkingwithguardsaboutpeltnorthALL:
    label peltnorthtalkingwithguardsaboutpeltnorth:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about this place.”')
        menu:
            '“Not much to tell, honestly. There are many beasts around, both wild game and dangerous monsters. We spend our time surrounded by these walls, leaving only to hunt, forage, or trade.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth01:
        menu:
            '“Like in {color=#f6d6bd}Hovlavan{/color}? Fair! But it ain’t here to protect the gate. This stronghold was built long before we moved in, and not to fight off humans. The tower was meant to be used by those who observe the deep forest. We look out for fires, dragons, and any winged creatures that are looking to roost on the roof.”
            \n\n“Baldy,” she nods toward a man who, indeed, is completely bald. “Has a great eye, and sees well even in darkness.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth02:
        $ description_dalit01 = "It looks like she could teach me quite a bit about the monsters that live in this peninsula."
        menu:
            '“Ha! Here? Everything lives here!” She flips her hair. “I swear, we saw a few dragons, a unicorn family, a battle between trolls and goblins, faced two beastmen, oh, and a gargoyle, and a hunting queen shouts all the time. I could tell you all about them... But I won’t.” She winks and pats the boar on its head. “You know, hunters have their secrets.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth03:
        menu:
            '“Anything we can eat or sell. If there’s a partridge, a squirrel, or a rat, we don’t complain. But when we move as a group, we look for something larger. Deers and aurochs are delicious, but we don’t always look for taste alone. There’s value in bones, antlers, claws, tusks. Things people use to make tools or sculptures. We use some of them to make tools and spears, you can {i}never{/i} have enough spears.” She pauses and looks at a strand of her hair, then suddenly speaks up again. “And we look for furs, of course.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth04:
        $ description_oldpagos02 = "It’s connected strongly with the nearby Order of Truth."
        $ description_oldpagos05 = "“as long as you don’t mock their Order and act nice, they’ll also be kind. My boss says they’re too serious for him to stand them, but at least they don’t bite without a reason.”"
        $ description_bighunters04 = "They arrived here about ten years ago."
        if not quest_ruins_10yclue02 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue02 = "Newcomers arrived at {color=#f6d6bd}Pelt of the North{/color}."
        menu:
            '“I’m sorry, we don’t really go to those regions. We stay close to home, only sometimes move south or west, to {color=#f6d6bd}Howler’s Dell{/color}, but only to trade. They’re fine with buying more than they need, since they then take wares to the coast.”
            \n\nShe takes a long breath, twirling her hair and gathering her thoughts. “You know what? I’ve never even seen a beach! And I’ve been living here for how many, more than ten years now!” She giggles. “The only part of the sea I’ve seen was from {color=#f6d6bd}Old Págos{/color}, which is placed on a hill. I’ve never put a toe in salt water!” She looks toward another huntress who confirms that her experience is the same.
            \n\n“But {color=#f6d6bd}Old Págos{/color} is a good place. As long as you don’t mock their Order and act nice, they’ll also be kind. Boss says they’re too serious for him to stand them, but at least they don’t bite without a reason.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth05:
        $ description_whitemarshes03 = "Some of the locals decided to leave their homes once the village had started to awaken the dead."
        $ whitemarshes_opposition += 1
        menu:
            '“It’s something new,” her voice lowers to a whisper. “I’ve never been to {color=#f6d6bd}White Marshes{/color}, but over the years we’ve seen people moving away from there, south. They told us that the place has changed too much. A priest died, I think? An’ the new one awakens the dead. Sorry, roadwarden, that’s all I know.”
            \n\nIf she’s hiding something, she sounds convincing.
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaboutpeltnorth06:
        menu:
            '“How could you not be?” She crouches and raises the boar’s head, but it steps away and squeals as if someone’s murdering it. “It came with us from the city, just in case. We had no clue how our first winter would go, so we needed some backup meat. And it works, too! Cleans the dirt.” She reaches out to the beast again, but it trots away. The woman straightens up with a pleased sigh.
            \n\n“We haven’t needed to eat it so far, but it’s also funny. I learned in my home village that the farm boars are getting a bit smaller and more cuddly, kind of like ibexes, so it’s not such a wild, dangerous beast. But we don’t let it get close to other animals. Or children.”
            '
            '“That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”' if not dalit_about_tower:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_tower += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s an unusual tower. I’d expect it’d be closer to the gate. And shorter.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth01
            '“Any interesting creatures living nearby?”' if not dalit_about_creatures:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_creatures += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any interesting creatures living nearby?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth02
            '“Your group seems to be quite attached to this boar.”' if not dalit_about_boar:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_boar += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group seems to be quite attached to this boar.”')
                jump peltnorthtalkingwithguardsaboutpeltnorth06
            '“What do you usually hunt for?”' if not dalit_about_hunting:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_hunting += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you usually hunt for?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth03
            '“What can I find north from here?”' if not dalit_about_north:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_north += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I find north from here?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth04
            '“Have you heard anything about the necromancers?”' if not dalit_about_necromancers:
                $ dalit_about_minorquestionALL += 1
                $ dalit_about_necromancers += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about the necromancers?”')
                jump peltnorthtalkingwithguardsaboutpeltnorth05
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump peltnorthtalkingwithguardsafterquestions

###############################################################

label peltnorthtalkingwithguardsaboutdruids:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that one of you could tell me something about the local druids.”')
    $ dalit_about_druids = 1
    menu:
        'The group gets quiet. After a moment, you hear a sigh, and a tall man steps forward. He doesn’t look more than twenty, and you’d barely noticed his presence before. His hair is blond, skin tanned, clothes well-kept. “Come, I wanted to take a look at your horse anyway.”
        \n\nDuring your conversation, he grows confident enough to pet {color=#f6d6bd}[horsename]’s{/color} head, then lets it peacefully munch hay. His accent is a bit thick, but he speaks slowly enough for you to catch up.
        \n\nWhen he was growing up in {color=#f6d6bd}Howler’s Dell{/color}, he wanted to learn more about animals. He tried to become a druid. “Do ne think of them as some evildoers. For the cityfolk they may be pagans, but for ma home they’re saviors. They tame the beasts, keep them in the woods, beg the spirits to spare us on the road. Can’t deal with all creatures, surely, but their teachings have lived in our village for centuries.”
        '
        'I tell him that many people would call me a pagan and I don’t see druids as evil.' if pc_religion == "pagan" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him that many people would call me a pagan and I don’t see druids as evil.')
            $ dalit_friendship += 1
            jump peltnorthtalkingwithguardsaboutdruids02A
        '(lie) I tell him that many people would call me a pagan and I don’t see druids as evil.' if pc_religion != "pagan":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I tell him that many people would call me a pagan and I don’t see druids as evil.')
            $ dalit_friendship += 1
            $ pc_lies += 1
            $ pc_faithpoints -= 1
            label peltnorthtalkingwithguardsaboutdruids02A:
                $ knowsabouthowlerdellpagans = 1
                $ description_druids02 = "I can find the local druids in the village of {color=#f6d6bd}Howler’s Dell{/color}, along the western road."
                $ description_druids05 = "According to one of the hunters from {color=#f6d6bd}Pelt{/color}, the local druids aren’t as interested in philosophy as they are in protecting the villagers. They teach how to respect the {i}laws of the forests{/i} and are ready to turn away anyone who dares to break their strict code."
                $ description_bighunters03 = "Most of them came here from the South, but some were born in the peninsula."
                $ description_howlersdell05 = "The locals are following the teachings of a group of druids."
                menu:
                    'His tone shifts from kindness to friendliness. “Would ne expect it, surely ne from a roadwarden,” he whispers enthusiastically. “Some people here are a bit, you know. Ne too happy talking about the deeds of our grandparents. But all you need to do is show the druids that you accept our ways, unlike the city madfolk.”
                    \n\nThe man explains that minor details related to faith aren’t as important to the local druids. They see humans as a part of nature and want to protect them from harm. They teach villagers how to respect the laws of the forests, and to avoid undue foraging and hunting. They don’t mingle much with the laws of humans, and use magic to separate the wilderness from the weak.
                    \n\n“They’re strict en have rules they will ne break, no matter what. That’s why I did ne stay around. You shall never disobey the elders, you know, but I just could ne handle it. They told me to stay still when I needed to act, when I tried to help my family. I can ne make such choices. At least now I share my knowledge with the hunters, make sure they do ne make more harm than necessary.”
                    '
                    '“Any suggestions on how I can get on their good side?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any suggestions on how I can get on their good side?”')
                        jump peltnorthtalkingwithguardsaboutdruids03
        'I let him continue.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let him continue.')
            $ description_druids05 = "According to one of the hunters from {color=#f6d6bd}Pelt{/color}, the local druids aren’t as interested in philosophy as they are in protecting the villagers. They teach how to respect the {i}laws of the forests{/i} and are ready to turn away anyone who dares to break their strict code."
            menu:
                'The man explains that minor details related to faith aren’t as important to the local druids. They see humans as a part of nature and want to protect them from harm. They teach villagers how to respect the laws of the forests, and to avoid unduly foraging and hunting. They don’t mingle much with the laws of humans, and use magic to separate the wilderness from the weak.
                \n\n“They’re strict en have rules they will ne break, no matter what. That’s why I did ne stay around. You shall never disobey the elders, you know, but I just could ne handle it. They told me to stay still when I needed to act, when I tried to help my family. I can ne make such choices. At least now I share my knowledge with the hunters, make sure they do ne make more harm than necessary.”
                '
                '“Any suggestions on how I can get on their good side?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any suggestions on how I can get on their good side?”')
                    jump peltnorthtalkingwithguardsaboutdruids03

    label peltnorthtalkingwithguardsaboutdruids03:
        $ description_druids04 = "To show them due respect, one should be humble and penitent, respect their efforts, and address them as {i}forest speakers{/i}."
        menu:
            '“Their good side, you say... Well, they’re protectors of humans, you know? You shall honor their work en sacrifice. Be honest, but look at the ground en don’t waste their time. Act as if there’s a burden on you en you {i}need them{/i} to help you. En remember to call them {i}forest speakers{/i}! ‘Tis a sign of respect. A simple {i}greetings, forest speaker{/i} will be enough.”
            \n\nHe points west. “To find them, just stay on the road. You’ll get to a large tree. From there, the road goes north, but there’s a small path south, to a cave. This is where you can find the elder druids, there’s two of them. The others are in {color=#f6d6bd}Howler’s{/color}.”
            '
            'I thank him for his help and head toward {color=#f6d6bd}[dalit_name]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank him for his help and head toward {color=#f6d6bd}%s{/color}.' %dalit_name)
                jump peltnorthtalkingwithguardsafterquestions
            'I nod and head toward {color=#f6d6bd}[dalit_name]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and head toward {color=#f6d6bd}%s{/color}.' %dalit_name)
                jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardsbeasts01:
    $ dalit_about_wildcreatures = 1
    if not dalit_beastiary_discount:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for knowledge about wild creatures.”')
        menu:
            '“Well... I told you our knowledge is valuable. I don’t know.” She looks at the boar, which seems to be obsessed with a clump of grass growing next to the wall. “Fifteen dragons, no less.”
            '
            'I don’t have enough. (disabled)' if coins < dalit_beastiary_price_base:
                pass
            'I give her fifteen coins. “Fine.”' if coins >= dalit_beastiary_price_base:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her fifteen coins. “Fine.”')
                $ dalit_beastiary_unlocked = 1
                $ bestiary = 1
                show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                jump peltnorthtalkingwithguardsbeastsparserspaid
            '“Is there any discount for friends?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there any discount for friends?”')
                jump peltnorthtalkingwithguardshagglingonprice
            '“Never mind.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                jump peltnorthtalkingwithguardsafterquestions
    else:
        $ dalit_beastiary_price = (dalit_beastiary_price_base-((dalit_friendship+appearance_charisma)/2))
        if dalit_beastiary_discount_ilan:
            $ dalit_beastiary_price -= 2
        if dalit_beastiary_price > 15:
            $ dalit_beastiary_price = 15
        if dalit_beastiary_price < 5:
            $ dalit_beastiary_price = 5
        if dalit_beastiary_price >= 15:
            menu:
                '“You know how it is. Fifteen.”
                '
                'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
                    pass
                'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
                    jump peltnorthtalkingwithguardshagglingonpriceilan
                'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
                    $ dalit_beastiary_unlocked = 1
                    $ bestiary = 1
                    show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                    jump peltnorthtalkingwithguardsbeastsparserspaid
                '“Never mind.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                    jump peltnorthtalkingwithguardsafterquestions
        elif dalit_beastiary_price == 5:
            menu:
                '“Well, [pcname],” she chuckles. “For you, it’s five dragons. I won’t go any lower, the others would give me weird looks.”
                '
                'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
                    pass
                'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
                    jump peltnorthtalkingwithguardshagglingonpriceilan
                'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
                    $ dalit_beastiary_unlocked = 1
                    $ bestiary = 1
                    show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                    jump peltnorthtalkingwithguardsbeastsparserspaid
                '“Never mind.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                    jump peltnorthtalkingwithguardsafterquestions
        else:
            menu:
                '“I see... You know how it is, [pcname]. For you, it’s [dalit_beastiary_price].”
                '
                'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
                    pass
                'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
                    jump peltnorthtalkingwithguardshagglingonpriceilan
                'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
                    $ dalit_beastiary_unlocked = 1
                    $ bestiary = 1
                    show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                    jump peltnorthtalkingwithguardsbeastsparserspaid
                '“Never mind.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                    jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardsbeastsparserspaid:
    $ coins -= dalit_beastiary_price
    $ iason_friendship_moneybonus_points += 2
    menu:
        'She takes the coins with a smile. “We can start whenever you want.”
        '
        '“That’s all I need to know.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
            jump peltnorthtalkingwithguardsafterquestions
        '“I’ve learnt something new about howlers. I saw them ignoring meat that was brought right into the heart of their lair. They only eat leaves and fruits.”' if howlerslair_corpse_predator and dalit_bestiary_howlers and not dalit_bestiary_howlersandmeat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve learnt something new about howlers. I saw them ignoring meat that was brought right into the heart of their lair. They only eat leaves and fruits.”')
            jump peltnorthtalkingwithguardsbeasthowlerstrivia
        '“I’ve been in the watchtower northeast from here and it’s crawling with bugs.”' if not dalit_bestiary_bugs and quest_explorepeninsula_description05:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been in the watchtower northeast from here and it’s crawling with bugs.”')
            $ dalit_bestiary_bugs = 1
            jump peltnorthdalitonbugs
        '“Should I be afraid of the local apes?”' if not dalit_bestiary_apes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I be afraid of the local apes?”')
            $ dalit_bestiary_apes = 1
            jump peltnorthdalitonbeastapes
        '“Apes and monkeys.”' if dalit_bestiary_apes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Apes and monkeys.”')
            jump peltnorthdalitonbeastapes
        '“Are there many beastfolk around?”' if not dalit_bestiary_beastfolk:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are there many beastfolk around?”')
            $ dalit_bestiary_beastfolk = 1
            jump peltnorthdalitonbeastfolk
        '“Beastfolk.”' if dalit_bestiary_beastfolk:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Beastfolk.”')
            jump peltnorthdalitonbeastfolk
        '“I can’t always run away from dragonlings. How do you deal with them?”' if not dalit_bestiary_dragonlings:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t always run away from dragonlings. How do you deal with them?”')
            $ dalit_bestiary_dragonlings = 1
            jump peltnorthdalitondragonlings
        '“Dragonlings.”' if dalit_bestiary_dragonlings:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragonlings.”')
            jump peltnorthdalitondragonlings
        '“Have you ever hunted down a dragon?”' if not dalit_bestiary_dragon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever hunted down a dragon?”')
            $ dalit_bestiary_dragon = 1
            jump peltnorthdalitondragon
        '“Dragons.”' if dalit_bestiary_dragon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragons.”')
            jump peltnorthdalitondragon
        '“I don’t expect to find a lot of people who live in caves here... Should I expect any corpse eaters?”' if not dalit_bestiary_ghouls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect to find a lot of people who live in caves here... Should I expect any corpse eaters?”')
            $ dalit_bestiary_ghouls = 1
            jump peltnorthdalitonghouls
        '“Corpse eaters.”' if dalit_bestiary_ghouls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Corpse eaters.”')
            jump peltnorthdalitonghouls
        '“Any weird critters getting close to the settlements?”' if not dalit_bestiary_mediumcritters:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any weird critters getting close to the settlements?”')
            $ dalit_bestiary_mediumcritters = 1
            jump peltnorthdalitonmediumcritters
        '“Foxes and such.”' if dalit_bestiary_mediumcritters:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Foxes and such.”')
            jump peltnorthdalitonmediumcritters
        '“Are there any gargoyles lurking around?”' if not dalit_bestiary_gargoyles:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are there any gargoyles lurking around?”')
            $ dalit_bestiary_gargoyles = 1
            jump peltnorthdalitongargoyles
        '“Gargoyles.”' if dalit_bestiary_gargoyles:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gargoyles.”')
            jump peltnorthdalitongargoyles
        '“Any goblin packs I should be aware of?”' if not dalit_bestiary_goblins:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any goblin packs I should be aware of?”')
            $ dalit_bestiary_goblins = 1
            jump peltnorthdalitongoblins
        '“Goblins.”' if dalit_bestiary_goblins:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Goblins.”')
            jump peltnorthdalitongoblins
        '“Maybe you know something about the golems? How does one {i}kill{/i} a magical being?”' if not dalit_bestiary_golems:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you know something about the golems? How does one {i}kill{/i} a magical being?”')
            $ dalit_bestiary_golems = 1
            $ quest_studyingthegolems_description04 = "According to"
            $ quest_studyingthegolems_description04b = "golems get confused when they move away from their owners. Trying to crush their shells won’t do much good, but if properly trapped, their limbs can be pulled apart, weakening the magic that keeps them in one piece."
            if quest_studyingthegolems == 1 and not aeli_golems_learned04b:
                $ renpy.notify("Journal updated: Studying the Golems")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
            jump peltnorthdalitongolems
        '“Golems.”' if dalit_bestiary_golems:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Golems.”')
            jump peltnorthdalitongolems
        '“I met a bunch of annoying griffons on my way here.”' if not dalit_bestiary_griffons:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met a bunch of annoying griffons on my way here.”')
            $ dalit_bestiary_griffons = 1
            jump peltnorthdalitongriffons
        '“Griffons.”' if dalit_bestiary_griffons:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Griffons.”')
            jump peltnorthdalitongriffons
        '“May harpies pose any problem?”' if not dalit_bestiary_harpies:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “May harpies pose any problem?”')
            $ dalit_bestiary_harpies = 1
            jump peltnorthdalitonharpies
        '“Harpies.”' if dalit_bestiary_harpies:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Harpies.”')
            jump peltnorthdalitonharpies
        '“What can you tell me about howlers?”' if not dalit_bestiary_howlers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about howlers?”')
            $ dalit_bestiary_howlers = 1
            jump peltnorthdalitonhowlers
        '“Howlers.”' if dalit_bestiary_howlers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Howlers.”')
            jump peltnorthdalitonhowlers
        '“What do you know about the local huntlords and huntqueens? Is there any ruler yet?”' if not dalit_bestiary_huntlords:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the local huntlords and huntqueens? Is there any ruler yet?”')
            $ dalit_bestiary_huntlords = 1
            jump peltnorthdalitonhuntlords
        '“Huntlords.”' if dalit_bestiary_huntlords:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Huntlords.”')
            jump peltnorthdalitonhuntlords
        '“How should I handle the runners? They keep sneaking among the trees, waiting for me to get off {color=#f6d6bd}[horsename]{/color}.”' if not dalit_bestiary_birds:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How should I handle the runners? They keep sneaking among the trees, waiting for me to get off {color=#f6d6bd}%s{/color}.”' %horsename)
            $ dalit_bestiary_birds = 1
            jump peltnorthdalitonbirds
        '“Runners.”' if dalit_bestiary_birds:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Runners.”')
            jump peltnorthdalitonbirds
        '“What can I do about large cats?”' if not dalit_bestiary_largecats:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I do about large cats?”')
            $ dalit_bestiary_largecats = 1
            jump peltnorthdalitonlargecats
        '“Large cats.”' if dalit_bestiary_largecats:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Large cats.”')
            jump peltnorthdalitonlargecats
        '“Do many locals have issues with pebblers?”' if not dalit_bestiary_pebblers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do many locals have issues with pebblers?”')
            $ dalit_bestiary_pebblers = 1
            jump peltnorthdalitonpebblers
        '“Pebblers.”' if dalit_bestiary_pebblers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pebblers.”')
            jump peltnorthdalitonpebblers
        '“How do you prepare for saurians when they come in so many shapes and sizes?”' if not dalit_bestiary_saurians:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you prepare for saurians when they come in so many shapes and sizes?”')
            $ dalit_bestiary_saurians = 1
            jump peltnorthdalitonsaurians
        '“Saurians.”' if dalit_bestiary_saurians:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Saurians.”')
            jump peltnorthdalitonsaurians
        '“I’m sure I’m going to find a spider or two in some of the local ruins.”' if not dalit_bestiary_spiders:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure I’m going to find a spider or two in some of the local ruins.”')
            $ dalit_bestiary_spiders = 1
            jump peltnorthdalitonspiders
        '“Spiders.”' if dalit_bestiary_spiders:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Spiders.”')
            jump peltnorthdalitonspiders
        '“Where can I expect to encounter treants? Among the swamps, in the heart of the forest?”' if not dalit_bestiary_treants:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where can I expect to encounter treants? Among the swamps, in the heart of the forest?”')
            $ dalit_bestiary_treants = 1
            jump peltnorthdalitontreants
        '“Treants.”' if dalit_bestiary_treants:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Treants.”')
            jump peltnorthdalitontreants
        '“How many trolls can I find here?”' if not dalit_bestiary_trolls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How many trolls can I find here?”')
            $ dalit_bestiary_trolls = 1
            jump peltnorthdalitontrolls
        '“Trolls.”' if dalit_bestiary_trolls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Trolls.”')
            jump peltnorthdalitontrolls
        '“What would you do with an undead? Or maybe a group of them?”' if not dalit_bestiary_undead:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do with an undead? Or maybe a group of them?”')
            $ dalit_bestiary_undead = 1
            jump peltnorthdalitonundead
        '“Undead.”' if dalit_bestiary_undead:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Undead.”')
            jump peltnorthdalitonundead
        '“You know I have to ask about unicorns.”' if not dalit_bestiary_unicorns:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know I have to ask about unicorns.”')
            $ dalit_bestiary_unicorns = 1
            jump peltnorthdalitonunicorns
        '“Unicorns.”' if dalit_bestiary_unicorns:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Unicorns.”')
            jump peltnorthdalitonunicorns
        '“What about wolves? Are there any unusual breeds around here?”' if not dalit_bestiary_wolves:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about wolves? Are there any unusual breeds around here?”')
            $ dalit_bestiary_wolves = 1
            jump peltnorthdalitonwolves
        '“Wolves.”' if dalit_bestiary_wolves:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wolves.”')
            jump peltnorthdalitonwolves

label peltnorthtalkingwithguardshagglingonprice:
    $ dalit_beastiary_discount = 1
    $ dalit_beastiary_price = (dalit_beastiary_price_base-((dalit_friendship+appearance_charisma)/2))
    if dalit_beastiary_discount_ilan:
        $ dalit_beastiary_price -= 2
    if dalit_beastiary_price > 20:
        $ dalit_beastiary_price = 20
    if dalit_beastiary_price < 5:
        $ dalit_beastiary_price = 5
    if dalit_dice_never:
        $ dalit_dice_never = 0
    if dalit_beastiary_price >= 20:
        menu:
            '“I mean... There is. But I don’t think it’s relevant here. If it’s too much for you, maybe ask me after you spend some time around, show us what you’re capable of. Or play dice with us when you have an hour to spare. These folks here,” she starts to whisper and points with her thumb at the guards behind. “They {i}crave{/i} gossip.”
            '
            'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
                pass
            'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
                jump peltnorthtalkingwithguardshagglingonpriceilan
            'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
                $ dalit_beastiary_unlocked = 1
                $ bestiary = 1
                show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                jump peltnorthtalkingwithguardsbeastsparserspaid
            '“Never mind.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                jump peltnorthtalkingwithguardsafterquestions
    else:
        menu:
            '“Well... Depending on the friend.” She gives you a radiant smile. “Let’s say [dalit_beastiary_price]. If it’s too much for you, maybe ask me after you spend some time around, show us what you’re capable of. Or play dice with us when you have an hour to spare. These folks here,” she starts to whisper and points with her thumb at the guards behind. “They {i}crave{/i} gossip.”
            '
            'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
                pass
            'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
                jump peltnorthtalkingwithguardshagglingonpriceilan
            'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
                $ dalit_beastiary_unlocked = 1
                $ bestiary = 1
                show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
                jump peltnorthtalkingwithguardsbeastsparserspaid
            '“Never mind.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
                jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardshagglingonpriceilan:
    $ dalit_beastiary_discount_ilan = 1
    $ dalit_beastiary_price = (dalit_beastiary_price_base-((dalit_friendship+appearance_charisma)/2))
    if dalit_beastiary_discount_ilan:
        $ dalit_beastiary_price -= 2
    if dalit_beastiary_price > 20:
        $ dalit_beastiary_price = 20
    if dalit_beastiary_price < 5:
        $ dalit_beastiary_price = 5
    menu:
        'She giggles. “Oh, don’t you say such a thing! You make me sound like an old lady. I’m still a hunter, not a talker!” She winks at you. “Fine. [dalit_beastiary_price].”
        '
        'I don’t have enough. (disabled)' if coins < dalit_beastiary_price:
            pass
        'I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”' if description_dalit04 and not dalit_beastiary_discount_ilan:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Come on, it will be fun. {color=#f6d6bd}Ilan{/color} told me you love to talk about beasts.”')
            jump peltnorthtalkingwithguardshagglingonpriceilan
        'I give her [dalit_beastiary_price] dragons. “Fine.”' if coins >= dalit_beastiary_price:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her %s dragons. “Fine.”' %dalit_beastiary_price)
            $ dalit_beastiary_unlocked = 1
            $ bestiary = 1
            show screen notifyimage( "The entire bestiary has been updated.\n-%s" %dalit_beastiary_price, "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The entire bestiary has been updated. -%s {image=cointest}{/i}' %dalit_beastiary_price)
            jump peltnorthtalkingwithguardsbeastsparserspaid
        '“Never mind.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Never mind.”')
            jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardsbeastsparsers:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for knowledge about wild creatures.”')
    $ custom1 = renpy.random.choice(['She nods. “Go ahead.”', '“Which one?”', '“You need to be more specific.”', 'She smiles and rests her hand on her waist.'])
    menu:
        '[custom1]
        '
        '“That’s all I need to know.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
            jump peltnorthtalkingwithguardsafterquestions
        '“I’ve learnt something new about howlers. I saw them ignoring meat that was brought right into the heart of their lair. They only eat leaves and fruits.”' if howlerslair_corpse_predator and dalit_bestiary_howlers and not dalit_bestiary_howlersandmeat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve learnt something new about howlers. I saw them ignoring meat that was brought right into the heart of their lair. They only eat leaves and fruits.”')
            jump peltnorthtalkingwithguardsbeasthowlerstrivia
        '“I’ve been in the watchtower northeast from here and it’s crawling with bugs.”' if not dalit_bestiary_bugs and quest_explorepeninsula_description05:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been in the watchtower northeast from here and it’s crawling with bugs.”')
            $ dalit_bestiary_bugs = 1
            jump peltnorthdalitonbugs
        '“Should I be afraid of the local apes?”' if not dalit_bestiary_apes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I be afraid of the local apes?”')
            $ dalit_bestiary_apes = 1
            jump peltnorthdalitonbeastapes
        '“Apes and monkeys.”' if dalit_bestiary_apes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Apes and monkeys.”')
            jump peltnorthdalitonbeastapes
        '“Are there many beastfolk around?”' if not dalit_bestiary_beastfolk:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are there many beastfolk around?”')
            $ dalit_bestiary_beastfolk = 1
            jump peltnorthdalitonbeastfolk
        '“Beastfolk.”' if dalit_bestiary_beastfolk:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Beastfolk.”')
            jump peltnorthdalitonbeastfolk
        '“I can’t always run away from dragonlings. How do you deal with them?”' if not dalit_bestiary_dragonlings:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t always run away from dragonlings. How do you deal with them?”')
            $ dalit_bestiary_dragonlings = 1
            jump peltnorthdalitondragonlings
        '“Dragonlings.”' if dalit_bestiary_dragonlings:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragonlings.”')
            jump peltnorthdalitondragonlings
        '“Have you ever hunt down a dragon?”' if not dalit_bestiary_dragon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever hunt down a dragon?”')
            $ dalit_bestiary_dragon = 1
            jump peltnorthdalitondragon
        '“Dragons.”' if dalit_bestiary_dragon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragons.”')
            jump peltnorthdalitondragon
        '“I don’t expect to find a lot of people who live in caves here... Should I expect any corpse eaters?”' if not dalit_bestiary_ghouls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect to find a lot of people who live in caves here... Should I expect any corpse eaters?”')
            $ dalit_bestiary_ghouls = 1
            jump peltnorthdalitonghouls
        '“Corpse eaters.”' if dalit_bestiary_ghouls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Corpse eaters.”')
            jump peltnorthdalitonghouls
        '“Any weird critters getting close to the settlements?”' if not dalit_bestiary_mediumcritters:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any weird critters getting close to the settlements?”')
            $ dalit_bestiary_mediumcritters = 1
            jump peltnorthdalitonmediumcritters
        '“Foxes and such.”' if dalit_bestiary_mediumcritters:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Foxes and such.”')
            jump peltnorthdalitonmediumcritters
        '“Are there any gargoyles lurking around?”' if not dalit_bestiary_gargoyles:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are there any gargoyles lurking around?”')
            $ dalit_bestiary_gargoyles = 1
            jump peltnorthdalitongargoyles
        '“Gargoyles.”' if dalit_bestiary_gargoyles:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gargoyles.”')
            jump peltnorthdalitongargoyles
        '“Any goblin packs I should be aware of?”' if not dalit_bestiary_goblins:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any goblin packs I should be aware of?”')
            $ dalit_bestiary_goblins = 1
            jump peltnorthdalitongoblins
        '“Goblins.”' if dalit_bestiary_goblins:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Goblins.”')
            jump peltnorthdalitongoblins
        '“Maybe you know something about the golems? How does one {i}kill{/i} a magical being?”' if not dalit_bestiary_golems:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you know something about the golems? How does one {i}kill{/i} a magical being?”')
            $ dalit_bestiary_golems = 1
            $ quest_studyingthegolems_description04 = "According to"
            $ quest_studyingthegolems_description04b = "golems get confused when they move away from their owners. Trying to crush their shells won’t do much good, but if properly trapped, their limbs can be pulled apart, weakening the magic that keeps them in one piece."
            if quest_studyingthegolems == 1 and not aeli_golems_learned04b:
                $ renpy.notify("Journal updated: Studying the Golems")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
            jump peltnorthdalitongolems
        '“Golems.”' if dalit_bestiary_golems:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Golems.”')
            jump peltnorthdalitongolems
        '“I met a bunch of annoying griffons on my way here.”' if not dalit_bestiary_griffons:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met a bunch of annoying griffons on my way here.”')
            $ dalit_bestiary_griffons = 1
            jump peltnorthdalitongriffons
        '“Griffons.”' if dalit_bestiary_griffons:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Griffons.”')
            jump peltnorthdalitongriffons
        '“May harpies pose any problem?”' if not dalit_bestiary_harpies:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “May harpies pose any problem?”')
            $ dalit_bestiary_harpies = 1
            jump peltnorthdalitonharpies
        '“Harpies.”' if dalit_bestiary_harpies:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Harpies.”')
            jump peltnorthdalitonharpies
        '“What can you tell me about howlers?”' if not dalit_bestiary_howlers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about howlers?”')
            $ dalit_bestiary_howlers = 1
            jump peltnorthdalitonhowlers
        '“Howlers.”' if dalit_bestiary_howlers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Howlers.”')
            jump peltnorthdalitonhowlers
        '“What do you know about the local huntlords and huntqueens? Is there any ruler yet?”' if not dalit_bestiary_huntlords:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the local huntlords and huntqueens? Is there any ruler yet?”')
            $ dalit_bestiary_huntlords = 1
            jump peltnorthdalitonhuntlords
        '“Huntlords.”' if dalit_bestiary_huntlords:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Huntlords.”')
            jump peltnorthdalitonhuntlords
        '“How should I handle the runners? They keep sneaking among the trees, waiting for me to get off {color=#f6d6bd}[horsename]{/color}.”' if not dalit_bestiary_birds:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How should I handle the runners? They keep sneaking among the trees, waiting for me to get off {color=#f6d6bd}%s{/color}.”' %horsename)
            $ dalit_bestiary_birds = 1
            jump peltnorthdalitonbirds
        '“Runners.”' if dalit_bestiary_birds:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Runners.”')
            jump peltnorthdalitonbirds
        '“What can I do about large cats?”' if not dalit_bestiary_largecats:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can I do about large cats?”')
            $ dalit_bestiary_largecats = 1
            jump peltnorthdalitonlargecats
        '“Large cats.”' if dalit_bestiary_largecats:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Large cats.”')
            jump peltnorthdalitonlargecats
        '“Do many locals have issues with pebblers?”' if not dalit_bestiary_pebblers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do many locals have issues with pebblers?”')
            $ dalit_bestiary_pebblers = 1
            jump peltnorthdalitonpebblers
        '“Pebblers.”' if dalit_bestiary_pebblers:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pebblers.”')
            jump peltnorthdalitonpebblers
        '“How do you prepare for saurians when they come in so many shapes and sizes?”' if not dalit_bestiary_saurians:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you prepare for saurians when they come in so many shapes and sizes?”')
            $ dalit_bestiary_saurians = 1
            jump peltnorthdalitonsaurians
        '“Saurians.”' if dalit_bestiary_saurians:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Saurians.”')
            jump peltnorthdalitonsaurians
        '“I’m sure I’m going to find a spider or two in some of the local ruins.”' if not dalit_bestiary_spiders:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure I’m going to find a spider or two in some of the local ruins.”')
            $ dalit_bestiary_spiders = 1
            jump peltnorthdalitonspiders
        '“Spiders.”' if dalit_bestiary_spiders:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Spiders.”')
            jump peltnorthdalitonspiders
        '“Where can I expect to encounter treants? Among the swamps, in the heart of the forest?”' if not dalit_bestiary_treants:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where can I expect to encounter treants? Among the swamps, in the heart of the forest?”')
            $ dalit_bestiary_treants = 1
            jump peltnorthdalitontreants
        '“Treants.”' if dalit_bestiary_treants:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Treants.”')
            jump peltnorthdalitontreants
        '“How many trolls can I find here?”' if not dalit_bestiary_trolls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How many trolls can I find here?”')
            $ dalit_bestiary_trolls = 1
            jump peltnorthdalitontrolls
        '“Trolls.”' if dalit_bestiary_trolls:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Trolls.”')
            jump peltnorthdalitontrolls
        '“What would you do with an undead? Or maybe a group of them?”' if not dalit_bestiary_undead:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do with an undead? Or maybe a group of them?”')
            $ dalit_bestiary_undead = 1
            jump peltnorthdalitonundead
        '“Undead.”' if dalit_bestiary_undead:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Undead.”')
            jump peltnorthdalitonundead
        '“You know I have to ask about unicorns.”' if not dalit_bestiary_unicorns:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know I have to ask about unicorns.”')
            $ dalit_bestiary_unicorns = 1
            jump peltnorthdalitonunicorns
        '“Unicorns.”' if dalit_bestiary_unicorns:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Unicorns.”')
            jump peltnorthdalitonunicorns
        '“What about wolves? Are there any unusual breeds around here?”' if not dalit_bestiary_wolves:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What about wolves? Are there any unusual breeds around here?”')
            $ dalit_bestiary_wolves = 1
            jump peltnorthdalitonwolves
        '“Wolves.”' if dalit_bestiary_wolves:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wolves.”')
            jump peltnorthdalitonwolves

    label peltnorthdalitonbugs:
        menu:
            '“Sure thing, they follow abandoned food. I hate the fat roaches, they give me the creeps.” She twirls her hair nervously. “They don’t like smoke, so they stay away if people live in a place during spring and autumn, but they’re also scared of some herbs. Maybe ask in {color=#f6d6bd}White Marshes{/color} for a balm? The worst thing that can happen is that you’ll find one of the hundred-legged ones, those larger than your boot. But they mostly stay near tall grasses, maybe they won’t get inside.”
            '
            '“I have another creature on my mind.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonbeastfolk:
        menu:
            '“Ah,” she lets out a hiss. “Ain’t gonna lie... They’re too weird, each one is different. Two of them, one deerhead and one bearfolk, tried to steal a rabbit from our trap. We outnumbered them, so they just grunted for a bit and withdrew. But you know the old tales. Bring the offerings, meat and whatnot, and {i}maybe{/i} they’ll be {i}kind{/i} to you. Something they won’t find in the woods. Or food touched with pneuma.”
            \n\n“And if you were asking just about the gnolls... Who cares about them, they could barely bite your hand. You see a dozen of them? Run before they knock you down. You see two? Just chop their heads off. They ain’t magical, that I can tell you for sure. And they’re dumber than wolves.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitondragonlings:
        menu:
            'She chuckles. “Put your horse to use and flee! Most of them are west of here, they stay away when we move in large groups. But oh, do they lurk around! If you {i}really{/i} have to fight them... They attack all at once, so you won’t make it when outnumbered, and you won’t outrun them on foot. Hide up a tree if you’re alone, and if not, be sure that everyone in your group has a decent weapon. Getting through their skin is tough. Unless you find kobolds, you know. Those that are knee-high. They’re not too dangerous, they won’t try to hunt down a human. Maybe if they’re starving.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitondragon:
        menu:
            '“Eh, we han’t tried to get close enough to any of them, not once. Bones are fine and all, but you know what’s better? Staying in one piece. As long as they don’t storm our inn, I’m just fine watching them cross the sky, listening to their roars. They don’t care about humans all that much. We’re too small for their jaws, and it’s not easy for them to get through our clothes and equipment. But they do destroy villages if they feel like it.”
            \n\n“I wish I could have a voice like they do. Whenever they roar, birds take off, and the wild game either flees or plays dead. Could be a handy little trick. You know, like this.” She looks around, then opens and closes her mouth a couple of times, as if she’s considering making a roar of her own. Finally, she glances at her companions and gestures for you to go on.
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonghouls:
        menu:
            '“They’re not around. There ain’t many travelers and settlements here, so they can’t feast on humans alone. Last time I saw their claw marks, when was it? A year ago or so, when we placed traps in the northeast, near the old watchtower. They stay away from the heart of the forest, so all that remains is the far east.”
            \n\n“At least they don’t move in large packs,” {color=#f6d6bd}[dalit_name]{/color} seems to be lost in her thoughts, when suddenly she points at your blade. “You can handle at least one of them, with that axe of yours. Just give it all, right away. Hurt the beast even slightly, cut its arm or something, and it’s going to run in panic. They’re deadly cowards.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonmediumcritters:
        menu:
            '“I can’t say for the villages, but none of them come to our walls. The badgers, foxes, wolverines, and others like that stay in their burrows, or in the ruins if there are no goblins around. You don’t hunt for furs, I expect?” Seeing your shrug, she goes on. “If they bother you, you can bother them back from time to time. Scare them off, you see? Show them their home ain’t safe anymore, and they’ll look for another one. Much less bloody than a fight with a whole pack at once.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitongargoyles:
        menu:
            '“They stay where the trees and shrubs are the thickest. In the heart of the forest, most likely. Waiting for something to get close, then they jump, ready to bite off their prey’s heads. The oldest one I’ve seen looked like a small dragon. It could swallow you whole.”
            \n\n“What you need to do is keep an eye on the tree crowns, or maybe the thicket next to the road. When a gargoyle prepares to strike, their eyes get red, almost shiny. That’s when you need to take a damn crossbow and shoot right into it. Don’t use spells, though. They won’t do any good.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitongoblins:
        menu:
            '“We’ve finished off some of the packs, but they travel all around, and move their camps every now and then. Expect them anywhere. If you see a single creature, turn back, its family is just nearby. If you really want to hurt them, take care of their home. Sink it, ruin it, burn it. Whatever you do with it, they’ll move away. They need to hide from monsters, just like we do, so they won’t stay around.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitongolems:
        menu:
            '“Well... They protect their owners, so it ain’t really something I’d {i}hunt{/i} down, you know?” She brushes away the hair from her forehead. “Oh, you ain’t playing around. Well, let me think. They ain’t a single whole.” She puts her left arm on her right shoulder and pulls it. “I don’t understand it fully, but I think it’s a bit like with the undead. The more parts of the shell you remove, even for a time, the more magic gets to waste, as if... It returns to the air?” She shrugs and returns to her previous stance. “Make a trap, try to hold it, then pull, a rope may work. Don’t try to stab it or smash it with a hammer. You can’t {i}harm{/i} them.”
            \n\nShe looks at the boar. “Or maybe... You could just kill their owner. Or move them far away. It’s impossible to order golems around from a great distance. It confuses them.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitongriffons:
        menu:
            '“The noble griffins? But they don’t live here, it’s too close to the ocean. They can’t compete with the flying beasts, so they only hunt at dawn. Oh, or do you mean the scrubs? Those are everywhere. Try to scare them off, like from a large distance, or by wounding them before they get into position. In a place like this one they won’t starve, there’s a lot of game around. I wouldn’t expect them to hunt for human flesh.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonharpies:
        menu:
            '“Are you even going to find them? There should be none in these woods, the thicket is much too dense. And, you know, they’re cowards,” she simultaneously smiles and shrugs. “How much of a threat can they be? If you have to travel where they live, just be sure to have a few guards with you. They won’t attack a group of humans. Or take a crossbow. Or spells.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonhowlers:
        menu:
            '“I han’t heard about someone studying them, you know? Those shouts,” she cups her hands around her mouth, “are like spells, and will make you sick. All it takes is what, a minute or so. Maybe a single one won’t be a threat, but they’re never alone. You’ll see packs of them in the north, and you better stay away from them, or be sure to have as many ways to keep them scared of you as you can. If they ain’t afraid, they ain’t going to let you live, and will devour you right after they deafen you.”
            '
            '“I know for a fact they eat only plants. I saw them ignoring meat that was brought right into the heart of their lair.”' if howlerslair_corpse_predator and not dalit_bestiary_howlersandmeat:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know for a fact they eat only plants. I saw them ignoring meat that was brought right into the heart of their lair.”')
                jump peltnorthtalkingwithguardsbeasthowlerstrivia
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsbeasthowlerstrivia:
        $ dalit_bestiary_howlersandmeat = 1
        menu:
            '“What are you talking about?” Her eyes widen, but then she purses her lips. “Sounds like a crazy tale.”
            '
            '“I don’t have time for this. Just trust me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have time for this. Just trust me.”')
                $ dalit_friendship += 1
                menu:
                    '“Well, I’d rather keep an eye on them if I see any. Thanks.”
                    '
                    '“Let’s talk about another beast.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                        jump peltnorthtalkingwithguardsbeastsparsers
                    '“That’s all I need to know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                        jump peltnorthtalkingwithguardsafterquestions
            'I tell her about everything that happened.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her about everything that happened.')
                $ dalit_friendship += 2
                $ quarters += 2
                menu:
                    'The entire group joins her to listen, asking you for the details of your trek. They burst into laughter as you describe your encounters with the pack, and insightfully discuss the looks of the lair, and the decisions that helped you survive. As you glance at {color=#f6d6bd}[dalit_name]{/color}, she’s unusually quiet, and chips in only after the conversation ends.
                    \n\n“Well, I’m glad I didn’t put any dragons on this.” She covers her mouth and giggles. “I thought them to be bloodthirsty, but maybe they’re just really, {i}really{/i} obsessed about their land.” She thoughtfully looks at another huntress, who nods back to her. “That’s helpful to know, [pcname]. Thank you.”
                    '
                    '“Let’s talk about another beast.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                        jump peltnorthtalkingwithguardsbeastsparsers
                    '“That’s all I need to know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                        jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonhuntlords:
        menu:
            '“Yeah, they don’t fight anymore. The latest queen has ruled for maybe five years now. Our watchmen saw it a couple of times, it’s tall and has red and silver fur. I’d recognize its howling anywhere. But please don’t tell me you plan to look for it,” she looks at you with worry. “No human can harm such a being. If it decides it wants you, the best you can do is abandon your palfrey and hope it looks tasty. But huntlords rarely strike before dusk, so who cares? Stay in the sunlight, like the rest of us.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonsaurians:
        menu:
            '“At least not all of them eat meat!” She spreads her arms. “Those longer than this are the worst, but that’s why you keep away from the ponds and lakes. They stay just at the bank, jump at whatever gets close. You try to wash your hands, whoosh!” She clasps her hands loudly. “Snapped. Even worse with a horse, it will grab it by the leg... And you know how fragile they are, as good as gone. Those all-gray are the big problem, all of them eat humans. And look at their tails. If they are thin and swing left and right, they can break your ribs.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonspiders:
        menu:
            '“Most of them are in the ruins and the very lush forests. They sit, all by themselves, in their webs, waiting for critters that have lost their way. If you face them, watch out. Their bites are... Well, maybe not {i}venomous{/i}, but they do something weird, I can’t describe it. It {i}melts{/i} your skin. And their legs are pointy, like tiny spears. There’s no point in fighting them, unless you’re looking for spider silk.”
            \n\nAfter you ask her how to get rid of such a creature, she struggles to find an answer. “A really large one? Without a crossbow? A bow should do fine as well, but aim at the abdomen. A spear would be a good choice and when it gets too close, switch to an axe, or a mace. Or do you mean the smaller ones, like head-size big?” She measures an invisible spider with her hands. “They often, I don’t know, spit at their targets, or something. You do not want to get hit with it, this {i}web{/i}. Dodge it, or get blinded. Maybe jump away. Then you can smash it with whatever you have at hand.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitontrolls:
        if not tulia_pelt_inside and not dalit_about_tulia:
            menu:
                'She puts a hand on her chest, close to her heart. “There should be none of them left. Those fatheads were causing utter chaos across the entire peninsula, especially near the coast. Once they ate a forager from the tavern, we were hired to get rid of them. And so we did.”
                '
                '“Let’s talk about another beast.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                    jump peltnorthtalkingwithguardsbeastsparsers
                '“That’s all I need to know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                    jump peltnorthtalkingwithguardsafterquestions
        else:
            menu:
                'She looks down. “Those fatheads were causing utter chaos across the entire peninsula, especially near the coast. Once they ate a forager from the tavern, we were hired to get rid of them. I thought they were gone for good.”
                '
                '“Let’s talk about another beast.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                    jump peltnorthtalkingwithguardsbeastsparsers
                '“That’s all I need to know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                    jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonundead:
        menu:
            'She sighs. “Yeah, I don’t have any tricks for you. Chop them as many times as you can, like the priests and soldiers say. Crush their bones, cut off their limbs. Surround them, outnumber them. Only the dumbest ones, those barely touched by the fogs, can fall into a simple trap. But if you {i}hurt{/i} them enough, the pneuma leaves them. Don’t ask me how that works, I don’t drink with necromancers.”
            \n\nWhen you ask where you can find them, she points north. “Well, in {color=#f6d6bd}White Marshes{/color}, probably. But also in the deep woods, surely looking to form a new band. Don’t worry, though, they won’t catch {color=#f6d6bd}[horsename]{/color}.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonbirds:
        menu:
            '“Well, they ain’t as bad as dragonlings, you know? At least you can make a roast out of them. You’ll outrun them on a palfrey, but if you’re on foot, don’t even try. Don’t hide up a tree, they jump way too high. Wings, you know,” she waves her arms, imitating a flying bird. “And remember, they strike with their beaks. If they miss, it takes time for them to try again. Be fast, be decisive. Or...” She hesitates. “You can try to buy time by throwing some meat at it. But only if there’s one of them, no more.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitontreants:
        menu:
            '“Just like you said, mostly in the swamps. Do you know how to spot them? They have no leaves and their branches are wide and long, they catch birds and animals that get close to them. They use their food to bait other creatures. There may be some in the deep woods, but I don’t think {color=#f6d6bd}[horsename]{/color} is going to take you there anyway.”
            \n\n“If one of them catches you after all, play dead. Don’t try to free yourself, just wait, or it’s going to choke you, or tear off your limbs. I know it sounds bad,” her voice stays serious, despite her smile. “But stay calm. It’ll put you into its mouth, only then should you strike. Its inside is smooth, hit it with a blade, it may panic, then drop you. May. That’s your moment to run. It happened to me once, you see,” she puts one hand on her chest and another one on her side, as if posing for a sculptor. “And I’m still here. But you know, it’s better to stay as far away as you can.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonwolves:
        menu:
            '“Ha, there’s a lovely pack of red ones, those that jump really far and once they bite you, they never let go. Also some blue wolves, they spend their time spread around, but howl to one another when they find good prey. Trust me, don’t ever try to fight a pack. Their furs are valuable, even the gray ones, but the only way to hurt them is setting up a trap. They abandon those that can’t be helped... But not the spotted wolves. They always try to help their wounded.”
            \n\nAfter a brief moment, she carries on. “But the furless wolves... Those are the worst. They live alone, but are as dangerous as an entire group. Once you find one, you can’t run away from it, you can’t scare it off if it’s not bleeding. You must stay brave, especially when it charges at you. It’s going to jump, oh, this high” she raises her hand to her neck. “Duck beneath it, as quickly as you can.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonbeastapes:
        menu:
            'She takes a deep breath, shifts her weight to her left leg, and puts her right hand on her waist. “Oh, could I tell you stories!” A short chuckle. “It ain’t as bad now as it used to be. What’s left are mostly the monkeys. They’re not much of a threat if you stay away from their land, but they throw things at whatever they’re afraid of. Once they get used to you, they’ll leave you alone, at least one of the many families that live in these forests.”
            \n\nShe twirls her hair, thinking. “There’s a couple of dangerous apes, though. They ain’t to be ignored. We’ve seen at least one frightape, you know what it is? The gray one, with muscles this big,” she makes vague gestures around her arms covered by a gambeson. “If it attacks you, it knows it can easily squeeze you to death. You can’t fight it, [pcname]. All you can do is run away.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonlargecats:
        menu:
            '“You ain’t going to do much about them,” she shrugs with a smile. “The cats won’t let you see them. They stalk their prey, and jump when you least expect it. Like, slash, and its claws are in your neck. And have you seen how big they can get? A venemus gets twice as long as your horse!”
            \n\nAfter you ask her if she’s sure that there’s nothing you can do to protect yourself, she twirls her hair. “You could do something if it’s right in front of you. Like, if it ain’t hunting. If you were smart, you’d stay away, wait for the cat to move. But if you have to... I don’t know. Be calm? Scare it away? Pretend you’re large?” She chuckles. “But what are the chances you’ll ever be in such a situation?”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonpebblers:
        menu:
            '“There ain’t that many forest gardens here, in the North, so they sometimes show up out west. The druids get rid of them, and the people of {color=#f6d6bd}Old Págos{/color} have a pile of mails and iron spearheads, so they know how to fight them off. I’d say there ain’t much point in hunting them. You can’t eat them, or get a good pelt. And their bones are so hard you ain’t going to sharpen one after even a day of work. Dragging their corpse away will take you hours and dozens of hands, so it’s all a big waste of time. Better to just discourage them, or scare them away.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorthdalitonunicorns:
        menu:
            '“I... Doubt you’ll face one anytime soon!” There’s a worry in her voice as she glances at the wall. “I only saw them a few times, from very far away. We don’t hunt such large beasts, you know.” You ask her to think if there’s anything interesting she noticed, and she takes a few breaths before she comes up with something. “I han’t seen more than one of them at once, I think?” She asks a few other hunters, and while most of them agree, two people mention that unicorns mate in early spring, but even then they “don’t hang around much.”
            \n\n“You know what people say. The unicorns crave flesh filled with pneuma, but rarely hunt humans, and are only afraid of the largest beasts... Just the usual tales.”
            '
            '“Let’s talk about another beast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about another beast.”')
                jump peltnorthtalkingwithguardsbeastsparsers
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump peltnorthtalkingwithguardsafterquestions

label peltnorthpayingbackthedebt:
    $ dalit_friendship += 1
    $ dalit_pc_debt_timer = 0
    $ questionpreset = "dalit1"
    if dalit_pc_debt == 1:
        $ custom1 = "dragon bone"
    else:
        $ custom1 = "dragon bones"
    $ coins -= dalit_pc_debt
    show screen notifyimage( "-%s" %dalit_pc_debt, "gui/coin2.png")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %dalit_pc_debt)
    $ dalit_pc_debt = 0
    menu:
        'She smiles when you hand her the [custom1]. “Feels good, doesn’t it? Honesty, that is.”
        '
        '(dalit1 set)':
            pass

label peltnorthtalkingwithguardsplayingdiceALL:
    label peltnorthtalkingwithguardsplayingdice00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “If you have coin, I could throw some dice.”')
        $ d100roll = 0
        if dalit_pc_debt:
            $ questionpreset = "dalit1"
            menu:
                'She frowns. “How about you pay what you owe us first.”
                '
                '(dalit1 set)':
                    pass
        else:
            menu:
                '“Surely! But we’re doing it the right way. All ten rounds, so it’s going to take us half an hour or so. Four players, each one bets a coin. The winner takes all. Still in?”
                '
                '{image=d6} “I’m ready when you are.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I’m ready when you are.”')
                    $ dalit_friendship += 1
                    if not dalit_dice:
                        $ dalit_dice = day
                        $ quarters += 1
                        jump peltnorthtalkingwithguardsplayingdicefirsttimebutafterfirstmeeting01A
                    else:
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        $ dalit_dice = day
                        $ quarters += 2
                        jump peltnorthtalkingwithguardsplayingdiceregular01
                '“Maybe some other time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some other time.”')
                    jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsplayingdicefirsttimebutafterfirstmeeting01A:
        $ at = 0
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
        if not dalit_axes:
            if creeks_youth_gambling < 2:
                $ custom1 = "The game is new to you, but in no way baffling. Four people can play at once. The wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
            else:
                $ custom1 = "The game has similar rules to the one you’ve played in {color=#f6d6bd}Creeks{/color}, but this time four people can play at once, and the wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
            menu:
                'Your words and, especially the dragon bone you pull out, are cheerfully welcomed. Two of the guards bring a table from the inn, another one prepares a couple of stools and chairs. There are also spectators, and you’re told that the other hunters are either sleeping, or have duty on the tower. “Remember, no magic,” says one of the players. His face is deadly serious.
                \n\n[custom1]
                \n\nYou share casual jokes, memories, and views on luck and optimal strategies. {color=#f6d6bd}[horsename]{/color} and {color=#f6d6bd}Tulia’s{/color} camp are also brought up, but when you ask about the roads or the locals, their stories are vague.
                \n\nThe drinks are here. It’s a poor beer made from the leftovers after the regular brewing. It’s cold, sweet, and doesn’t reach your head, but you try to avoid the smell. “Just don’t spill anything, the boar may get sick,” says your bald opponent.
                \n\nIn just a few minutes you get two points, which are now represented by smooth pebbles. You don’t really know how you got them. Either you don’t get the strategy, or it’s just pure luck.
                '
                '{image=d6} Let’s see how lucky I am.' ( condition="at != 'knowledge'" ):
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ at = 0
                    $ at_unlock_knowledge = 0
                    $ quarters += 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Let’s see how lucky I am.')
                    jump peltnorthtalkingwithguardsplayingdiceregular01
                '{image=d6} There’s a strategy to this game, I can see it. I can’t be sure that I’ll win, but I can play better than they expect.' ( condition="at == 'knowledge'"):
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ pc_gamblingxp += 15
                    $ pc_gamblingxp_scholarbonus = 1
                    $ at = 0
                    $ at_unlock_knowledge = 0
                    $ quarters += 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} There’s a strategy to this game, I can see it. I can’t be sure I’ll win, but I can play better than they expect.')
                    jump peltnorthtalkingwithguardsplayingdiceregular01
        else:
            if creeks_youth_gambling < 2:
                $ custom1 = "The game is new to you, but in no way baffling. Four people can play at once. The wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
            else:
                $ custom1 = "The game has similar rules to the one you’ve played in {color=#f6d6bd}Creeks{/color}, but this time four people can play at once, and the wooden dice are long, with only four dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
            menu:
                '[custom1]
                \n\nIn just a few minutes you get two points, which are now represented by smooth pebbles. You don’t really know how you got them. Either you don’t get the strategy, or it’s just pure luck.
                '
                '{image=d6} Let’s see how lucky I am.' ( condition="at != 'knowledge'" ):
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ at = 0
                    $ at_unlock_knowledge = 0
                    $ quarters += 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Let’s see how lucky I am.')
                    jump peltnorthtalkingwithguardsplayingdiceregular01
                '{image=d6} There’s a strategy to this game, I can see it. I can’t be sure that I’ll win, but I can play better than they expect.' ( condition="at == 'knowledge'"):
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ pc_gamblingxp += 15
                    $ pc_gamblingxp_scholarbonus = 1
                    $ at = 0
                    $ at_unlock_knowledge = 0
                    $ quarters += 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s a strategy to this game, I can see it. I can’t be sure I’ll win, but I can play better than they expect.')
                    jump peltnorthtalkingwithguardsplayingdiceregular01

    label peltnorthtalkingwithguardsplayingdiceregular01:
        $ iason_friendship_moneybonus_points += 1
        $ questionpreset = "dalit1"
        if d100roll-pc_gamblingxp > 75:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            if pc_gamblingxp <= 50:
                $ pc_gamblingxp += 3
            menu:
                'Time goes by, filled with light-hearted jokes and chit-chat. Your score is the lowest. You move a dragon bone to the bold, quiet man with wide nostrils, who has the grin of a wolf. After the table and the chairs are moved back into the building, {color=#f6d6bd}[dalit_name]{/color} asks if she can help you with anything.
                '
                '(dalit1 set)':
                    pass
        elif d100roll-pc_gamblingxp > 50:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            if pc_gamblingxp <= 50:
                $ pc_gamblingxp += 3
            menu:
                'Time goes by, filled with light-hearted jokes and chit-chat. After a long series of bad rolls you finish with two points, the second-lowest score. You put a dragon bone in front of {color=#f6d6bd}[dalit_name]{/color}, who’s comically exaggerated thanks are met with laughter. After the table and the chairs are moved back into the building, she asks if you need anything.
                '
                '(dalit1 set)':
                    pass
        elif d100roll-pc_gamblingxp > 25:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            if pc_gamblingxp <= 50:
                $ pc_gamblingxp += 3
            menu:
                'Time goes by, filled with light-hearted jokes and chit-chat. Your score is second-best. “Nice one,” you hear from the man with a fancily braided beard, who reaches to pick up your dragon bone. As the table and the chairs are carried back into the building, {color=#f6d6bd}[dalit_name]{/color} looks at you with a smile.
                '
                '(dalit1 set)':
                    pass
        else:
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            if pc_gamblingxp < 40:
                $ pc_gamblingxp += 5
            elif pc_gamblingxp <= 50:
                $ pc_gamblingxp += 3
            $ questionpreset = "dalit1"
            menu:
                'Time goes by, filled with light-hearted jokes and chit-chat. During the final round you get ahead of everyone, and the spectators playfully comment on your moves. The winner takes all - three dragons are placed on the table and you put them into your pouch quickly.
                \n\nThe table and chairs are moved back into the building and {color=#f6d6bd}[dalit_name]{/color} thanks you for playing. “Is there anything you need?”
                '
                '(dalit1 set)':
                    pass

label peltnorthtalkingwithguardsaxethrowingALL:
    label peltnorthtalkingwithguardsaxethrowing00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “How about some axe throwing?”')
        $ d100roll = 0
        if dalit_pc_debt:
            $ questionpreset = "dalit1"
            menu:
                'She frowns. “How about you pay what you owe us first.”
                '
                '(dalit1 set)':
                    pass
        else:
            menu:
                '“If you think you can handle it! We’ll throw eight times, so it’s going to take us half an hour or so. Four players, each one bets a coin. The winner takes all. Still in?”
                '
                '{image=d6} “I’m ready when you are.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I’m ready when you are.”')
                    $ dalit_friendship += 1
                    if not dalit_axes:
                        $ dalit_axes = day
                        $ quarters += 1
                        jump peltnorthtalkingwithguardsaxethrowingfirsttimebutafterfirstmeeting01A
                    else:
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        $ dalit_axes = day
                        $ quarters += 2
                        if pc_hp >= 4:
                            $ d100roll -= 15
                        elif pc_hp == 3:
                            $ d100roll -= 5
                        elif pc_hp <= 1:
                            $ d100roll += 10
                        if not pc_food:
                            $ d100roll += 5
                        if pc_food == 3:
                            $ d100roll -= 5
                        if pc_food == 4:
                            $ d100roll -= 15
                        if item_axe03:
                            $ d100roll -= 15
                        elif item_axe02 or item_axe02alt:
                            $ d100roll -= 5
                        $ custom6 = (pc_throwingxp*3)
                        if custom6 > 30:
                            $ custom6 = 30
                        $ d100roll -= custom6
                        if pc_class == "warrior":
                            $ d100roll -= 15
                        jump peltnorthtalkingwithguardsaxethrowingregular01
                '“Maybe some other time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some other time.”')
                    jump peltnorthtalkingwithguardsafterquestions

    label peltnorthtalkingwithguardsaxethrowingfirsttimebutafterfirstmeeting01A:
        $ at = 0
        if pc_class == "warrior":
            $ at_unlock_force = 1
        if not dalit_dice:
            menu:
                'Your words, and especially the dragon bone you pull out, are cheerfully welcomed. The guards prepare a couple of wooden planks, which are leaned against the wall. There are also spectators, and you’re told that the other hunters are either sleeping, or have duty on the tower. “Remember, no magic,” says one of the players. His face is deadly serious.
                \n\nYou’re meant to aim at the target drawn with charcoal. The person whose axe lands the closest to the center of the circle gets a point. Axes that fail to stay in the plank don’t count. The person who has the most points at the end of the last turn becomes the winner.
                \n\nYou talk a lot, but also don’t say much. You share casual jokes, memories, and views on luck and optimal strategies. {color=#f6d6bd}[horsename]{/color} and {color=#f6d6bd}Tulia’s{/color} camp are also brought up, but when you ask about the roads or the locals, their stories are vague.
                \n\nThe drinks are here. It’s a poor beer made from the leftovers after the regular brewing. It’s cold, sweet, and doesn’t reach your head, but you try to avoid the smell. “Just don’t spill anything, the boar may get sick,” says the opponent with one arm.
                \n\nAs a guest, you start with the first throw. Your axe flies well, hitting the very middle of the painted target and piercing the plank with a pleasant thud, which makes it really difficult for the other players to outperform you. A minute later, you’ve won the first round, but you can’t expect to be that lucky every time.
                '
                '{image=d6} All I can do is try my best.' ( condition="at != 'force'" ):
                    $ at = 0
                    $ at_unlock_force = 0
                    $ quarters += 1
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if pc_hp >= 4:
                        $ d100roll -= 15
                    elif pc_hp == 3:
                        $ d100roll -= 5
                    elif pc_hp <= 1:
                        $ d100roll += 10
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 15
                    if item_axe03:
                        $ d100roll -= 15
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 5
                    $ custom6 = (pc_throwingxp*3)
                    if custom6 > 30:
                        $ custom6 = 30
                    $ d100roll -= custom6
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} All I can do is try my best.')
                    jump dalit_firsttime01axethrow
                '{image=d6} I’ve trained in axe throwing for years. I’ve got this.' ( condition="at == 'force'" ):
                    $ at = 0
                    $ at_unlock_force = 0
                    $ quarters += 1
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 80)
                    if pc_hp >= 4:
                        $ d100roll -= 15
                    elif pc_hp == 3:
                        $ d100roll -= 5
                    elif pc_hp <= 1:
                        $ d100roll += 10
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 15
                    if item_axe03:
                        $ d100roll -= 15
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 5
                    $ custom6 = (pc_throwingxp*3)
                    if custom6 > 30:
                        $ custom6 = 30
                    $ d100roll -= custom6
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve trained in axe throwing for years. I’ve got this.')
                    jump dalit_firsttime01axethrow
        else:
            menu:
                'You’re meant to aim at the target drawn with charcoal. The person whose axe lands the closest to the center of the circle gets a point. Axes that fail to stay in the plank don’t count. The person who has the most points at the end of the last turn becomes the winner.
                \n\nAs a guest, you start with the first throw. Your axe flies well, hitting the very middle of the painted target and piercing the plank with a pleasant thud, which makes it really difficult for the other players to outperform you. A minute later, you’ve won the first round, but you can’t expect to be that lucky every time.
                '
                '{image=d6} All I can do is try my best.' ( condition="at != 'force'" ):
                    $ at = 0
                    $ at_unlock_force = 0
                    $ quarters += 1
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if pc_hp >= 4:
                        $ d100roll -= 15
                    elif pc_hp == 3:
                        $ d100roll -= 5
                    elif pc_hp <= 1:
                        $ d100roll += 10
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 15
                    if item_axe03:
                        $ d100roll -= 15
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 5
                    $ custom6 = (pc_throwingxp*3)
                    if custom6 > 30:
                        $ custom6 = 30
                    $ d100roll -= custom6
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} All I can do is try my best.')
                    jump dalit_firsttime01axethrow
                '{image=d6} I’ve trained in axe throwing for years. I’ve got this.' ( condition="at == 'force'" ):
                    $ at = 0
                    $ at_unlock_force = 0
                    $ quarters += 1
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 80)
                    if pc_hp >= 4:
                        $ d100roll -= 15
                    elif pc_hp == 3:
                        $ d100roll -= 5
                    elif pc_hp <= 1:
                        $ d100roll += 10
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 15
                    if item_axe03:
                        $ d100roll -= 15
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 5
                    $ custom6 = (pc_throwingxp*3)
                    if custom6 > 30:
                        $ custom6 = 30
                    $ d100roll -= custom6
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve trained in axe throwing for years. I’ve got this.')
                    jump dalit_firsttime01axethrow

    label peltnorthtalkingwithguardsaxethrowingregular01:
        $ iason_friendship_moneybonus_points += 1
        $ questionpreset = "dalit1"
        if d100roll > 75:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'Between the thudding of the axes, there’s plenty of time for casual gossip. You finish with only one point. You cast a dragon bone at a massive woman, who stops her winning dance only briefly, surrounded by the rhythmic clapping of her crew. You’re approached by {color=#f6d6bd}[dalit_name]{/color} and her wholehearted laughter.
                '
                '(dalit1 set)':
                    pass
        elif d100roll > 50:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'Between the thudding of the axes, there’s plenty of time for casual gossip. After a long series of misses you finish with one point, the second-last place. You give the gasping winner your dragon bone. “Cheers,” he says, but doesn’t make a big deal out of it. The light-hearted comments of the other losers lighten up the mood, and {color=#f6d6bd}[dalit_name]{/color} approaches you with a smile.
                '
                '(dalit1 set)':
                    pass
        elif d100roll > 25:
            $ coins -= 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            $ pc_throwingxp += 1
            menu:
                'Between the thudding of the axes, there’s plenty of time for casual gossip. Even though you get two points, {color=#f6d6bd}[dalit_name]{/color} gets one more. “Yes!” She raises her fist and nods to the spectators, who chuckle at her cheeky pride. After you give her your coin, she looks you in the eyes with a smile.
                '
                '(dalit1 set)':
                    pass
        else:
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_throwingxp += 2
            menu:
                'Between the thudding of the axes, there’s plenty of time for casual gossip. After getting the fourth point, the other players nod with respect. “Quite a score,” you hear from {color=#f6d6bd}[dalit_name]{/color} as she hands you your dragon bones. The other participants carry away the remaining planks.
                '
                '(dalit1 set)':
                    pass

label peltnorthtalkingwithguardsaboutbronzerod:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to place this rod on your watchtower for {color=#f6d6bd}Eudocia{/color}, the enchantress.”')
    if (dalit_friendship+appearance_charisma) >= 4:
        $ questionpreset = "dalit1"
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ eudocia_bronzerod_rodin_peltnorth = 1
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
            'She moves it close to her face, observing it with widened eyes. “Is this some sort of magic thing?” After your reassuring words, she pauses. “I mean, if it’s nothing dangerous... Fine. I’ll tie it somewhere during my watch, don’t you worry.”
            '
            '(dalit1 set)':
                pass
    elif iason_friendship >= 6:
        $ questionpreset = "dalit1"
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ eudocia_bronzerod_rodin_peltnorth = 1
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
            'She moves it close to her face, observing it with widened eyes. “Is this some sort of magic thing?” After your reassuring words, she pauses. “I mean, if it’s nothing dangerous... Fine, our boss trusts you. I’ll tie it somewhere during my watch, don’t you worry.”
            '
            '(dalit1 set)':
                pass
    else:
        if dalit_dice_never:
            $ dalit_dice_never = 0
        menu:
            'She moves it close to her face, observing it with widened eyes. “Is this some sort of magic thing?” After your reassuring words, she’s unconvinced. “I don’t know, I ain’t fired-up to do such favors. Maybe ask me after you spend some time around, show us what you’re capable of. Or play dice with us when you have an hour to spare. These folks here,” she starts to whisper and points with her thumb at the guards behind. “They {i}crave{/i} gossip.”
            '
            '“...What if I give you a coin?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...What if I give you a coin?”')
                $ questionpreset = "dalit1"
                $ renpy.notify("Journal updated: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                $ coins -= 1
                $ iason_friendship_moneybonus_points += 1
                $ eudocia_bronzerod_rodin_peltnorth = 1
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
                    'She laughs. “Sure, or that!” She reaches out to you, palm up. You give her a dragon bone, then a rod. “We’ll tie it somewhere, don’t you worry.”
                    '
                    '(dalit1 set)':
                        pass
            '“Fine. Maybe.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Maybe.”')
                jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardsaboutquintus01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met {color=#f6d6bd}Quintus{/color}, the one who trained with your team. He may need your help.”')
    $ dalit_friendship += 2
    $ dalit_about_quintus = day
    $ questionpreset = "dalit1"
    $ minutes += 5
    menu:
        'You explain the difficult situation he finds himself in, putting emphasis on his wounds and food issues. Listening to your conversation, the nearby guards surround you, forming a circle together with the boar, and ask you if {color=#f6d6bd}Quintus{/color} is in one piece. Your tale causes the tension to give way to jokes. “He’s so scared of the wrath of the herds that he’ll sooner eat his bloody crossbow than learn how to use it,” says one of the older women.
        \n\n“Let’s give the poor guy a break,” {color=#f6d6bd}[dalit_name]{/color} interrupts, which is not welcomed by a one-eyed man, who comments that “he’s not even here!”
        \n\nAfter another minute, she grins at you. “Thanks for telling us. We’ll change some plans and get in touch with him during our next trip.”
        \n\n“Come on, not that,” the same man chips in, but quiets down under the redhead’s stare.
        '
        '(dalit1 set)':
            pass

label peltnorthtalkingwithguardsaboutarrow01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the arrow I found near the fallen tree. “Did any of you drop this?”')
    $ dalit_about_arrow = 1
    $ questionpreset = "dalit1"
    menu:
        'She returns it without hesitation. “Nah. We get ours from the villages in the south, and they don’t use pheasant feathers. The locals ask too much for their arrows, as if they’re filled with pneuma or something.”
        '
        '(dalit1 set)':
            pass

label peltnorthtalkingwithguardsaboutgoblins01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a job for your crew. There are some goblins in the nearby ruins that pose a danger on the road.”')
    $ dalit_about_goblins = 1
    $ dalit_about_goblins_price = (dalit_about_goblins_price_base-dalit_friendship+appearance_charisma)
    if dalit_about_goblins_price < 10:
        $ dalit_about_goblins_price = 10
    menu:
        '“As long as it involves someone paying for it, I’m ready to listen. What do you know about the pack?” Without interruptions, you tell as much as you can.
        \n\n“Getting rid of them will do the trick, sure, but as long as those buildings ain’t razed to the ground, new beasts will move in, sooner or later. Though I ain’t one to stop you from reaching into your pouch,” a brief smile quirks her lips. “Now, you need to take care of some things first. Hunters or not, we won’t raid a lair blindly.”
        '
        '“What do you want me to do?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to do?”')
            menu:
                'She lists your tasks one by one, in the meantime bending forward to brush the boar. “Make sure you’ve looked around the entire village. My crew will get mad if it turns out that yet another lair is just behind the corner. Then, be sure there’s no soul around. When we fight, we don’t do rescue jobs, and if we do, they cost {i}a lot{/i}.” The boar grunts and turns around, leading her to its other side. “Speaking of which. For you it’s going to be...” She squints her eyes a bit. “[dalit_about_goblins_price] coins. But we’ll take some of the loot we find. We won’t let go of magic swords and rings just because. Not that I expect any,” she straightens up. “But who knows.”
                '
                '“I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”' if (coins >= dalit_about_goblins_price and quest_escortpyrrhos > 1 and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_peltnorth and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_howlersdell and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_dead and ruinedvillage_explored):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”')
                    jump peltnorthtalkingwithguardsaboutgoblins03
                '“Just so you know, I’ll bring an axe with me.”' if not dalit_about_goblins_participation:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just so you know, I’ll bring an axe with me.”')
                    $ dalit_about_goblins_participation = 1
                    menu:
                        'She looks at you as if you’re a lunatic. “We won’t take you with us, [pcname]. If you can kill a goblin, good. But we have a team. Our own words, knowledge of our strong and weak sides. We don’t need you around. Just give us two or three days after you pay us and we’ll take care of it.”
                        '
                        '“I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”' if (coins >= dalit_about_goblins_price and quest_escortpyrrhos > 1 and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_peltnorth and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_howlersdell and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_dead and ruinedvillage_explored):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”')
                            jump peltnorthtalkingwithguardsaboutgoblins03
                        'I don’t have the [dalit_about_goblins_price] dragons that she’s asked me for. (disabled)' if coins < dalit_about_goblins_price:
                            pass
                        'As far as I know, the scavenger is still in the ruins. (disabled)' if quest_escortpyrrhos == 1 and not quest_escortpyrrhos_description05 and not pyrrhos_dead:
                            pass
                        'I haven’t fully explored the ruins yet. (disabled)' if not ruinedvillage_explored:
                            pass
                        '“We’ll return to it later.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to it later.”')
                            jump peltnorthtalkingwithguardsafterquestions
                'I don’t have the [dalit_about_goblins_price] dragons that she’s asked me for. (disabled)' if coins < dalit_about_goblins_price:
                    pass
                'As far as I know, the scavenger is still in the ruins. (disabled)' if quest_escortpyrrhos == 1 and not quest_escortpyrrhos_description05 and not pyrrhos_dead:
                    pass
                'I haven’t fully explored the ruins yet. (disabled)' if not ruinedvillage_explored:
                    pass
                '“We’ll return to it later.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to it later.”')
                    jump peltnorthtalkingwithguardsafterquestions

label peltnorthtalkingwithguardsaboutgoblins02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the goblins...”')
    if not dalit_about_goblins_timer:
        $ dalit_about_goblins_price = (dalit_about_goblins_price_base-dalit_friendship+appearance_charisma)
        if dalit_about_goblins_price < 10:
            $ dalit_about_goblins_price = 10
        menu:
            '“Shoot. The price is [dalit_about_goblins_price].”
            '
            '“I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”' if (coins >= dalit_about_goblins_price and quest_escortpyrrhos > 1 and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_peltnorth and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_howlersdell and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_dead and ruinedvillage_explored):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”')
                jump peltnorthtalkingwithguardsaboutgoblins03
            '“Just so you know, I’ll bring an axe with me.”' if not dalit_about_goblins_participation:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just so you know, I’ll bring an axe with me.”')
                $ dalit_about_goblins_participation = 1
                menu:
                    'She looks at you as if you’re a lunatic. “We won’t take you with us, [pcname]. If you can kill a goblin, good. But we have a team. Our own words, knowledge of our strong and weak sides. We don’t need you around. Just give us two or three days after you pay us and we’ll take care of it.”
                    '
                    '“I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”' if (coins >= dalit_about_goblins_price and quest_escortpyrrhos > 1 and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_peltnorth and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_howlersdell and ruinedvillage_explored) or (coins >= dalit_about_goblins_price and pyrrhos_dead and ruinedvillage_explored):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have your dragons, and there’s no soul in the entire ruins. Let’s get to it.”')
                        jump peltnorthtalkingwithguardsaboutgoblins03
                    'I don’t have the [dalit_about_goblins_price] dragons that she’s asked me for. (disabled)' if coins < dalit_about_goblins_price:
                        pass
                    'As far as I know, the scavenger is still in the ruins. (disabled)' if quest_escortpyrrhos == 1 and not quest_escortpyrrhos_description05 and not pyrrhos_dead:
                        pass
                    'I haven’t fully explored the ruins yet. (disabled)' if not ruinedvillage_explored:
                        pass
                    '“We’ll return to it later.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to it later.”')
                        jump peltnorthtalkingwithguardsafterquestions
            'I don’t have the [dalit_about_goblins_price] dragons that she’s asked me for. (disabled)' if coins < dalit_about_goblins_price:
                pass
            'As far as I know, the scavenger is still in the ruins. (disabled)' if quest_escortpyrrhos == 1 and not quest_escortpyrrhos_description05 and not pyrrhos_dead:
                pass
            'I haven’t fully explored the ruins yet. (disabled)' if not ruinedvillage_explored:
                pass
            '“We’ll return to it later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to it later.”')
                jump peltnorthtalkingwithguardsafterquestions
    elif dalit_about_goblins_timer >= day:
        $ custom1 = (dalit_about_goblins_timer-day+1)
        $ questionpreset = "dalit1"
        if custom1 == 1:
            $ custom2 = "day"
        else:
            $ custom2 = "days"
        menu:
            '“We’ll get to it soon, we just need to prepare a bit, and hunt down some game while most of us are unwounded. Give us [custom1] [custom2] and we’ll be done with it.”
            '
            '(dalit1 set)':
                pass
    else:
        $ dalit_about_goblins = 2
        $ questionpreset = "dalit1"
        $ dalit_friendship += 2
        menu:
            '“It’s done. Most of the goblins are dead, some are back in the forest. The loot wasn’t that great,” she sighs, ”though maybe we missed something under all the feces they left behind. Well, thanks to some magic, our wounded are fine,” she pushes her hair away from her neck. “But I still think the place should be burned.”
            '
            '(dalit1 set)':
                pass

label peltnorthtalkingwithguardsaboutgoblins03:
    $ coins -= dalit_about_goblins_price
    $ iason_friendship_moneybonus_points += 4
    show screen notifyimage( "-%s" %dalit_about_goblins_price, "gui/coin2.png")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %dalit_about_goblins_price)
    if quarters >= (world_daylength-24):
        $ dalit_about_goblins_timer = (day+2)
    else:
        $ dalit_about_goblins_timer = (day+1)
    $ custom1 = (dalit_about_goblins_timer-day+1)
    $ dalit_friendship += 1
    if custom1 == 1:
        $ custom2 = "day"
    else:
        $ custom2 = "days"
    $ questionpreset = "dalit1"
    menu:
        'She reaches out for the coins and hides them without counting. “Cheers, [pcname].” She looks at the sun. “Give us [custom1] [custom2] to prepare for the raid. We’ll handle it with a small team.” There’s a different kind of confidence in her voice, and her stance is more like a leader’s. “Better stay away from the ruins until then, or you may get a random quarrel between your ears.”
        '
        '(dalit1 set)':
            pass

label peltnorthdalitonfisheater:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw a weird, human-like creature with gray skin, eating a raw fish at the pond in the heart of the woods. Any clue what that could be?”')
    $ questionpreset = "dalit1"
    $ dalit_friendship += 1
    $ dalit_bestiary_fisheater = 1
    menu:
        'She asks you about the appearance and actions of the creature, and after a pause, she looks at the boar, as if she’s asking it for help. “I han’t ever heard about such a beast,” her voice turns into a whisper. “It may be a bad sign.”
        '
        '(dalit1 set)':
            pass

label peltnorthdalitonundead_light:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you know there are undead that use light?”')
    $ questionpreset = "dalit1"
    $ dalit_friendship += 1
    $ dalit_bestiary_undead_light = 1
    menu:
        '“Kind of?” She gives you an unconvinced smile. “I know they grow more human-like the older they get. I think they don’t {i}need{/i} light, they just {i}want{/i} it. Like when they put on clothes or take trinkets from those they kill.”
        '
        '(dalit1 set)':
            pass

label peltnorthtalkingwithguardsaboutilan01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met {color=#f6d6bd}Ilan{/color}. He says hi.”')
    $ dalit_friendship += 1
    $ dalit_about_ilan = 1
    menu:
        'She looks up, twirling her hair as she thinks. “I’m sorry... Who?”
        '
        '“{color=#f6d6bd}Foggy’s{/color} son.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Foggy’s{/color} son.”')
            jump peltnorthtalkingwithguardsaboutilan02
        '“The big forager from the north.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The big forager from the north.”')
            label peltnorthtalkingwithguardsaboutilan02:
                $ quarters += 1
                $ questionpreset = "dalit1"
                menu:
                    'She gives you a beaming smile “Ah, so that’s his name! His accent is so thick I kind of misheard it, forgive me. How’s he doing?” You gossip about the man and his companion, and a couple of the hunters join your conversation, asking about the eastern road, the tavern, and traveling in general. A good couple of minutes is spent on discussing fashion in {color=#f6d6bd}Creeks{/color}. Some of the hunters regret not being used to wearing leather and furs, while others are convinced that linen is more convenient. “And if you’re cold, just put on a cloak,” says a woman with a bandage on her neck.
                    \n\nAfter some time, the guards walk away, leaving you with {color=#f6d6bd}[dalit_name]{/color} and the napping boar.
                    '
                    '(dalit1 set)':
                        pass

label peltnorthdalitabouthighisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know anything about {color=#f6d6bd}High Island{/color}?”')
    $ dalit_about_highisland = 1
    $ questionpreset = "dalit1"
    menu:
        'She looks at the other guards, but is met with silence. “‘Tis just an island,” says one of them. “No soul swims there no more. It’s too green, too many beasts. Unicorns, I heard.”
        '
        '(dalit1 set)':
            pass

label dalit_about_highisland_recruitmentALL:
    label dalit_about_highisland_recruitment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use a skillful hunter on my short journey to {color=#f6d6bd}High Island{/color}.”')
        $ dalit_about_highisland_recruitment = 1
        $ minutes += 5
        menu:
            '“What?” She chuckles, but then matches your serious look. “Tell me more.”
            \n\nYou share the gist of your plans as she’s spreading the old stew on the ground, to her boar’s great joy. “I put safety above adventure,” she finally responds, “but there {i}is{/i} a way you could convince me.”
            '
            '“What’s your price?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your price?”')
                label dalit_about_highisland_recruitment01a:
                    $ dalit_about_highisland_payment_threshold = dalit_about_highisland_payment_threshold_base
                    if peltnorth_ban_perm_past:
                        $ dalit_about_highisland_payment_threshold += 10
                    if iason_friendship_moneybonus_level5:
                        $ dalit_about_highisland_payment_threshold -= 10
                    elif iason_friendship_moneybonus_level4:
                        $ dalit_about_highisland_payment_threshold -= 8
                    elif iason_friendship_moneybonus_level3:
                        $ dalit_about_highisland_payment_threshold -= 6
                    elif iason_friendship_moneybonus_level2:
                        $ dalit_about_highisland_payment_threshold -= 4
                    elif iason_friendship_moneybonus_level1:
                        $ dalit_about_highisland_payment_threshold -= 2
                    $ dalit_about_highisland_payment_threshold -= (dalit_friendship+appearance_charisma)
                    if dalit_about_highisland_payment_threshold <= 5:
                        $ dalit_about_highisland_payment_threshold = 5
                    if dalit_about_highisland_payment_threshold <= 10:
                        $ custom1 = "And a few minutes in the saddle.”\n\nSeeing your look, she giggles. “What! I was about to ask you for forty bones, but you’re a friend of the inn. You know what you’re doing, and I can look after myself.”"
                    elif dalit_about_highisland_payment_threshold <= 20:
                        $ custom1 = "You seem to know what you’re doing, and I can look after myself. Good patrons get good prices.”"
                    elif dalit_about_highisland_payment_threshold <= 30:
                        $ custom1 = "Better prices are for inn’s friends only.”"
                    elif dalit_about_highisland_payment_threshold <= 40:
                        $ custom1 = "I won’t put my life at risk for less, not after I spent so many years training with a crossbow.”"
                    else:
                        $ custom1 = "And pay upfront. You’re a stranger, and I won’t put my life at risk for less."
                    menu:
                        '“{color=#f6d6bd}[dalit_about_highisland_payment_threshold]{/color} dragons. [custom1]
                        '
                        'I don’t have enough. (disabled)' if coins < dalit_about_highisland_payment_threshold:
                            pass
                        '“[dalit_about_highisland_payment_threshold]... Here you go.”' if coins >= dalit_about_highisland_payment_threshold:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “%s... Here you go.”' %dalit_about_highisland_payment_threshold)
                            show screen notifyimage( "-%s" %dalit_about_highisland_payment_threshold, "gui/coin2.png")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %dalit_about_highisland_payment_threshold)
                            $ coins -= dalit_about_highisland_payment_threshold
                            $ dalit_about_highisland_recruitment_done = 1
                            $ iason_friendship_moneybonus_points += 2
                            if dalit_about_highisland_payment_threshold <= 10:
                                $ quarters += 1
                                $ dalit_name = "Dalit"
                                menu:
                                    'She pays little attention to the few bones you hand her, and approaches the beast quickly - her short posture only emphasizes its enormous size. You clasp your hands to form a step, letting her get into the saddle, and preparing her to walk around the yard.
                                    \n\nIn actuality, it’s you who’s holding the lead. {color=#f6d6bd}[horsename]{/color}, disoriented by the rider’s unconvinced touch and her anxious gasps, welcomes having you by its side.
                                    \n\nAs the hunters gather on the walls, observing these events and drawing {color=#f6d6bd}[dalit_name]’s{/color} attention by calling her name and jokingly commenting on her transparent fear, their cheer makes you think of the market square. The worried, but honest laughter of your companion is like a child’s, for a few moments unbothered by the events of the outside world.
                                    \n\nFinally, you help {color=#f6d6bd}the guard{/color} get down. She’s sweating, but her smile is as radiant as always. She spreads her arms.
                                    '
                                    'I embrace her.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I embrace her.')
                                        $ dalit_friendship += 3
                                        $ questionpreset = "dalit1"
                                        menu:
                                            'Her arms are strong. She smells of water from the local well, but also of mud. Before she steps away, she pats your back a few times.
                                            '
                                            '(dalit1 set)':
                                                pass
                                    'I nod and lead {color=#f6d6bd}[horsename]{/color} to its usual spot.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and lead {color=#f6d6bd}%s{/color}, to its usual spot.' %horsename)
                                        $ dalit_friendship += 1
                                        $ questionpreset = "dalit1"
                                        menu:
                                            'After a few moments, you met again. “Well! Let me know when you need me.”
                                            '
                                            '(dalit1 set)':
                                                pass
                            else:
                                $ questionpreset = "dalit1"
                                menu:
                                    'She weighs the pouch in her hand, then places it on the table. “Pleasure! Let me know when you need me.”
                                    '
                                    '(dalit1 set)':
                                        pass
                        '“We can return to this later.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We can return to this later.”')
                            jump peltnorthtalkingwithguardsafterquestions

        label dalit_about_highisland_recruitment01b:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- We negotiate the price of her help at {color=#f6d6bd}High Island{/color}.')
            jump dalit_about_highisland_recruitment01a

label dalit_about_missinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a few hunters from {color=#f6d6bd}Creeks{/color}. {color=#f6d6bd}Vaschel{/color}, {color=#f6d6bd}Dalia{/color}, {color=#f6d6bd}Admon{/color}. Were they here?”')
    $ dalit_about_missinghunters = 1
    menu:
        '“I don’t know those names,” she looks at her companions and while there’s someone who claims to have met them, he has nothing to say about them. She then glances at the boar, which is now very interested in the smell of your boots, and giggles. “It’s a long way from here to {color=#f6d6bd}Creeks{/color}, I mostly spoke with {color=#f6d6bd}Efren{/color}. Have you met him?”
        '
        '“Sure. He’s a nice guy.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. He’s a nice guy.”')
            $ dalit_friendship += 1
            $ questionpreset = "dalit1"
            menu:
                'She starts to laugh. “Well, maybe I wouldn’t say {i}nice{/i}, but there’s charm to his vigor!”
                '
                '(dalit1 set)':
                    pass
        '“I don’t really trust him. He’s a bit weird.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t really trust him. He’s a bit weird.”')
            $ questionpreset = "dalit1"
            menu:
                'She raises an eyebrow. “You really don’t spend much time with hunters, [pcname]. When it comes to people, {i}weird{/i} is one of our words for {i}good{/i},” she smiles. “If all of us had the same eye, tongue, and ear, we wouldn’t be ready for all the crazy shit that comes after us in the woods.”
                '
                '(dalit1 set)':
                    pass
        '“I think he’s crazy, and I mean it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think he’s crazy, and I mean it.”')
            $ dalit_friendship += 1
            $ questionpreset = "dalit1"
            menu:
                'She bites her bottom lip, stopping her laughter, and points at the top of her head. “You mean that because of... The wolf-thingy?” When you mention it’s just a start, she nods with resignation. “There’s something broken in his soul, but he stays alive and healthy. So, crazy, or...” She points behind her with her thumb and it takes you a moment before you realize she means the wilderness behind the wall. “Ready for what’s to come?”
                '
                '(dalit1 set)':
                    pass

label dalit_about_shortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the heart of the woods?”')
    $ dalit_about_shortcut = 1
    $ questionpreset = "dalit1"
    $ description_shortcut09 = "“There are treants there, and wolves, even the furless ones. And if you have to go through the tall grasses, watch out for what’s on the ground. There ain’t many archers in the trees, but there are all too many worms, even larger than a water leech.”"
    menu:
        '“We sometimes hunt south from there, there are good hunting grounds in the western half. The second one is too overgrown, maybe the soil is different?” She shrugs, then moves the hair away from her forehead. “But it’s a risky spot. There are treants there, and wolves, even the furless ones. And if you have to go through the tall grasses, watch out for what’s on the ground. There ain’t many archers in the trees,” she smiles as if it’s a joke, “but there are all too many worms, even larger than a water leech.”
        '
        '(dalit1 set)':
            pass

label peltnorthtalkingwithguardsabouttraps01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to place some traps in an old tunnel in the far north. Any ideas?”')
    $ oldtunnel_exploration_knowledge = 1
    $ minutes += 20
    $ quest_closedtunnel_description01a = "The tunnel hides a group of undead. To have a better chance at fighting them, I could construct some simple traps."
    $ renpy.notify("Journal updated: The Closed Tunnel")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
    $ questionpreset = "dalit1"
    menu:
        '“Oh, I’ve never been there. What’s the place like?” You describe what you’ve seen of the tunnel and its inhabitants. In the meantime, she throws the boar a snack, observing how it brutally murders an apple. “That’s not easy, they aren’t like, stupid. You want something not {i}too{/i} obvious. Maybe deadfalls above entrances, ones made of wood and rocks. And pointy whip traps in spots that would mask the trigger cords... Are there any corridors, sharp turns?”
        \n\nYou speak with her for the next few minutes, then she leads you up a ladder, to the wall walk. She points at a few branches, telling you about the {i}whips{/i} then draws on the wall with a piece of charcoal, explaining how to build some simple traps. “Some really good ones can hold creatures in place, but unless you have a crossbow or something like it, it won’t help much. You dig a hole in some soft ground, then surround it with sticks, maybe camouflage it. A {i}foothold trap{/i}, you see.”
        \n\nShe offers to show you how to make one, then repeats her previous instructions. You nod with gratitude.
        '
        '(dalit1 set)':
            pass

label peltnorth_dalit_recruitahunterALL:
    label peltnorth_dalit_recruitahunter00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
        menu:
            '“Just a moment!” She runs in front of you, cutting your way with her wide grin. “Want to help us out? I spoke with our boss, and I kind of need a rider.”
            '
            '“What do you need?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you need?”')
                menu:
                    '“We could use another pair of hands here, someone who knows their way around the woods.” You start to explain that you’d rather stick to the saddle, but she waves it off. “So help me find a better soul! There are two people I’ve heard of who would like to join us. {color=#f6d6bd}Erastos{/color} from {color=#f6d6bd}Howler’s Dell{/color} and {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}.”
                    \n\nShe rubs the side of her boar, then pushes it away gently, as if she’s asking a child to play by itself for a few minutes. “The thing is we already have hunters who used to live in these places, and they told me they ain’t all too eager to welcome them here. I’d like you to speak with them both, and to ask the folks from their tribes about them. Before I make a decision whom should I invite, I need to be sure they can handle the job.”
                    '
                    '“So whom are you going to hire?”' if quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted:
                        jump peltnorth_dalit_recruitahunter03
                    '“What’s in it for me?”' if not quest_recruitahunter_dalit_about_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s in it for me?”')
                        $ quest_recruitahunter_dalit_about_reward = 1
                        $ custom1 = "“Coins, duh,” she giggles. “How about five? I’ll give you a few more if you {i}amaze me{/i} with all the news you’ll bring.”"
                        jump peltnorth_dalit_recruitahunter02
                    '“Why not hire {color=#f6d6bd}Quintus{/color}?”' if not quest_recruitahunter_dalit_about_quintus and dalit_about_quintus:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why not hire {color=#f6d6bd}Quintus{/color}?”')
                        $ quest_recruitahunter_dalit_about_quintus = 1
                        $ description_quintus07 = "According to {color=#f6d6bd}Dalit{/color}, he’s a bit dumb."
                        $ custom1 = "Your question sparks playful comments from her companions. “He’s a great friend,” she admits, “but he can’t be trusted with more {i}delicate{/i} tasks. When possible, we’d rather avoid using muscles alone. What matters the most is getting out of trouble with as few scratches as possible.”"
                        jump peltnorth_dalit_recruitahunter02
                    '“Who’s this {color=#f6d6bd}Erastos{/color}?”' if not quest_recruitahunter_dalit_about_erastos:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who’s this {color=#f6d6bd}Erastos{/color}?”')
                        $ quest_recruitahunter_dalit_about_erastos = 1
                        $ custom1 = "“A trapper. A few months ago, he told a passing-by caravan he wanted to leave his home, and asked them to bring us his message. One of his past neighbors told me he remembers {color=#f6d6bd}Erastos{/color} as a weak, quiet boy. I ain’t sure he knows how to fight, but we’d rather use traps anyway.”"
                        jump peltnorth_dalit_recruitahunter02
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if not quest_recruitahunter_dalit_about_cassia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        $ quest_recruitahunter_dalit_about_cassia = 1
                        $ custom1 = "“She mentioned to {color=#f6d6bd}Asterion{/color} she’d like to come here. She’s a guard, but I’ve heard she’s more of a talker, than a fighter. {color=#f6d6bd}Gale Rocks{/color} is so far away I’d really prefer to not travel there, but if she’s the {i}better{/i} choice, I may have no other option.”"
                        jump peltnorth_dalit_recruitahunter02
                    '“Any tips how to handle this?”' if not quest_recruitahunter_dalit_about_tips:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips how to handle this?”')
                        $ quest_recruitahunter_dalit_about_tips = 1
                        $ custom1 = "She glances at the other guards, and the one with a fancily braided beard clears his throat. “Ask as many people as you can. In small villages, you can never know who sleeps with whom.”"
                        jump peltnorth_dalit_recruitahunter02
                    'I still need to speak with Erastos. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_spokento_erastos:
                        pass
                    'I need to learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold:
                        pass
                    '“I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_dalit_about_erastos_completed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”')
                        if not quest_recruitahunter_dalit_about_erastos:
                            $ quest_recruitahunter_dalit_about_erastos = 2
                        $ quest_recruitahunter_dalit_about_erastos_completed = 1
                        $ minutes += 5
                        $ renpy.notify("Journal updated: Recruit a Hunter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                        if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2:
                            $ custom1 = "She hums a brief melody. “If what you’re saying is true, I’d say we’re better without him,” she glances at the others. “Here, we ain’t going to look after broken hearts. We need someone who can figure out their own shit.”"
                        else:
                            $ custom1 = "“Can’t say you dispelled my doubts,” she sighs. “I’d rather invite someone who knows how to fight when it comes to it, and won’t flee without an order.”"
                        jump peltnorth_dalit_recruitahunter02
                    'I could still learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_dalit_about_erastos_completed:
                        pass
                    'I still need to speak with Cassia. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_cassia_points:
                        pass
                    'I need to learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold:
                        pass
                    '“Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_dalit_about_cassia_completed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”')
                        if not quest_recruitahunter_dalit_about_cassia:
                            $ quest_recruitahunter_dalit_about_cassia = 2
                        $ quest_recruitahunter_dalit_about_cassia_completed = 1
                        $ minutes += 5
                        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2:
                            $ custom1 = "“It sounds like no matter her talents, or the lack thereof, she’s got a harpy of an attitude,” she summarizes your tale and tries to push aside the hair on her forehead. “May be better to spare ourselves the trouble after all.”"
                        else:
                            $ custom1 = "“Not the easiest attitude to deal with, you say,” she twirls her hair. “I ain’t so sure we need even more arguments around here.”"
                        $ renpy.notify("Journal updated: Recruit a Hunter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                        jump peltnorth_dalit_recruitahunter02
                    'I could still learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_dalit_about_cassia_completed:
                        pass
                    '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_about_reward and not quest_recruitahunter_dalit_started:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                        $ quest_recruitahunter_dalit_started = 1
                        $ quest_recruitahunter = 1
                        $ renpy.notify("New entry: Recruit a Hunter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Recruit a Hunter{/i}')
                        $ minutes += 5
                        jump leavingthepeltnorth02
                    '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_started and not (quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                        jump peltnorthtalkingwithguardsafterquestions

    label peltnorth_dalit_recruitahunter01:
        menu:
            'Her eyes light up.
            '
            '“So whom are you going to hire?”' if quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted:
                jump peltnorth_dalit_recruitahunter03
            '“What’s in it for me?”' if not quest_recruitahunter_dalit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s in it for me?”')
                $ quest_recruitahunter_dalit_about_reward = 1
                $ custom1 = "“Coins, duh,” she giggles. “How about five? I’ll give you a few more if you {i}amaze me{/i} with all the news you’ll bring.”"
                jump peltnorth_dalit_recruitahunter02
            '“Why not hire {color=#f6d6bd}Quintus{/color}?”' if not quest_recruitahunter_dalit_about_quintus and dalit_about_quintus:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why not hire {color=#f6d6bd}Quintus{/color}?”')
                $ quest_recruitahunter_dalit_about_quintus = 1
                $ description_quintus07 = "According to {color=#f6d6bd}Dalit{/color}, he’s a bit dumb."
                $ custom1 = "Your question sparks playful comments from her companions. “He’s a great friend,” she admits, “but he can’t be trusted with more {i}delicate{/i} tasks. When possible, we’d rather avoid using muscles alone. What matters the most is getting out of trouble with as few scratches as possible.”"
                jump peltnorth_dalit_recruitahunter02
            '“Who’s this {color=#f6d6bd}Erastos{/color}?”' if not quest_recruitahunter_dalit_about_erastos:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who’s this {color=#f6d6bd}Erastos{/color}?”')
                $ quest_recruitahunter_dalit_about_erastos = 1
                $ custom1 = "“A trapper. A few months ago, he told a passing-by caravan he wanted to leave his home, and asked them to bring us his message. One of his past neighbors told me he remembers {color=#f6d6bd}Erastos{/color} as a weak, quiet boy. I ain’t sure he knows how to fight, but we’d rather use traps anyway.”"
                jump peltnorth_dalit_recruitahunter02
            '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if not quest_recruitahunter_dalit_about_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                $ quest_recruitahunter_dalit_about_cassia = 1
                $ custom1 = "“She mentioned to {color=#f6d6bd}Asterion{/color} she’d like to come here. She’s a guard, but I’ve heard she’s more of a talker, than a fighter. {color=#f6d6bd}Gale Rocks{/color} is so far away I’d really prefer to not travel there, but if she’s the {i}better{/i} choice, I may have no other option.”"
                jump peltnorth_dalit_recruitahunter02
            '“Any tips how to handle this?”' if not quest_recruitahunter_dalit_about_tips:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips how to handle this?”')
                $ quest_recruitahunter_dalit_about_tips = 1
                $ custom1 = "She glances at the other guards, and the one with a fancily braided beard clears his throat. “Ask as many people as you can. In small villages, you can never know who sleeps with whom.”"
                jump peltnorth_dalit_recruitahunter02
            'I still need to speak with Erastos. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_spokento_erastos:
                pass
            'I need to learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold:
                pass
            '“I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_dalit_about_erastos_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”')
                if not quest_recruitahunter_dalit_about_erastos:
                    $ quest_recruitahunter_dalit_about_erastos = 2
                $ quest_recruitahunter_dalit_about_erastos_completed = 1
                $ minutes += 5
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2:
                    $ custom1 = "She hums a brief melody. “If what you’re saying is true, I’d say we’re better without him,” she glances at the others. “Here, we ain’t going to look after broken hearts. We need someone who can figure out their own shit.”"
                else:
                    $ custom1 = "“Can’t say you dispelled my doubts,” she sighs. “I’d rather invite someone who knows how to fight when it comes to it, and won’t flee without an order.”"
                jump peltnorth_dalit_recruitahunter02
            'I could still learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_dalit_about_erastos_completed:
                pass
            'I still need to speak with Cassia. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_cassia_points:
                pass
            'I need to learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold:
                pass
            '“Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”')
                if not quest_recruitahunter_dalit_about_cassia:
                    $ quest_recruitahunter_dalit_about_cassia = 2
                $ quest_recruitahunter_dalit_about_cassia_completed = 1
                $ minutes += 5
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2:
                    $ custom1 = "“It sounds like no matter her talents, or the lack thereof, she’s got a harpy of an attitude,” she summarizes your tale and tries to push aside the hair on her forehead. “May be better to spare ourselves the trouble after all.”"
                else:
                    $ custom1 = "“Not the easiest attitude to deal with, you say,” she twirls her hair. “I ain’t so sure we need even more arguments around here.”"
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                jump peltnorth_dalit_recruitahunter02
            'I could still learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_dalit_about_cassia_completed:
                pass
            '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_about_reward and not quest_recruitahunter_dalit_started:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                $ quest_recruitahunter_dalit_started = 1
                $ quest_recruitahunter = 1
                $ renpy.notify("New entry: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Recruit a Hunter{/i}')
                $ minutes += 5
                jump leavingthepeltnorth02
            '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_started and not (quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorth_dalit_recruitahunter02:
        menu:
            '[custom1]
            '
            '“So whom are you going to hire?”' if quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted:
                jump peltnorth_dalit_recruitahunter03
            '“What’s in it for me?”' if not quest_recruitahunter_dalit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s in it for me?”')
                $ quest_recruitahunter_dalit_about_reward = 1
                $ custom1 = "“Coins, duh,” she giggles. “How about five? I’ll give you a few more if you {i}amaze me{/i} with all the news you’ll bring.”"
                jump peltnorth_dalit_recruitahunter02
            '“Why not hire {color=#f6d6bd}Quintus{/color}?”' if not quest_recruitahunter_dalit_about_quintus and dalit_about_quintus:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why not hire {color=#f6d6bd}Quintus{/color}?”')
                $ quest_recruitahunter_dalit_about_quintus = 1
                $ description_quintus07 = "According to {color=#f6d6bd}Dalit{/color}, he’s a bit dumb."
                $ custom1 = "Your question sparks playful comments from her companions. “He’s a great friend,” she admits, “but he can’t be trusted with more {i}delicate{/i} tasks. When possible, we’d rather avoid using muscles alone. What matters the most is getting out of trouble with as few scratches as possible.”"
                jump peltnorth_dalit_recruitahunter02
            '“Who’s this {color=#f6d6bd}Erastos{/color}?”' if not quest_recruitahunter_dalit_about_erastos:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who’s this {color=#f6d6bd}Erastos{/color}?”')
                $ quest_recruitahunter_dalit_about_erastos = 1
                $ custom1 = "“A trapper. A few months ago, he told a passing-by caravan he wanted to leave his home, and asked them to bring us his message. One of his past neighbors told me he remembers {color=#f6d6bd}Erastos{/color} as a weak, quiet boy. I ain’t sure he knows how to fight, but we’d rather use traps anyway.”"
                jump peltnorth_dalit_recruitahunter02
            '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if not quest_recruitahunter_dalit_about_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                $ quest_recruitahunter_dalit_about_cassia = 1
                $ custom1 = "“She mentioned to {color=#f6d6bd}Asterion{/color} she’d like to come here. She’s a guard, but I’ve heard she’s more of a talker, than a fighter. {color=#f6d6bd}Gale Rocks{/color} is so far away I’d really prefer to not travel there, but if she’s the {i}better{/i} choice, I may have no other option.”"
                jump peltnorth_dalit_recruitahunter02
            '“Any tips how to handle this?”' if not quest_recruitahunter_dalit_about_tips:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips how to handle this?”')
                $ quest_recruitahunter_dalit_about_tips = 1
                $ custom1 = "She glances at the other guards, and the one with a fancily braided beard clears his throat. “Ask as many people as you can. In small villages, you can never know who sleeps with whom.”"
                jump peltnorth_dalit_recruitahunter02
            'I still need to speak with Erastos. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_spokento_erastos:
                pass
            'I need to learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold:
                pass
            '“I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_dalit_about_erastos_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I learned about {color=#f6d6bd}Erastos{/color}.”')
                if not quest_recruitahunter_dalit_about_erastos:
                    $ quest_recruitahunter_dalit_about_erastos = 2
                $ quest_recruitahunter_dalit_about_erastos_completed = 1
                $ minutes += 5
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2:
                    $ custom1 = "She hums a brief melody. “If what you’re saying is true, I’d say we’re better without him,” she glances at the others. “Here, we ain’t going to look after broken hearts. We need someone who can figure out their own shit.”"
                else:
                    $ custom1 = "“Can’t say you dispelled my doubts,” she sighs. “I’d rather invite someone who knows how to fight when it comes to it, and won’t flee without an order.”"
                jump peltnorth_dalit_recruitahunter02
            'I could still learn more about Erastos. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_dalit_about_erastos_completed:
                pass
            'I still need to speak with Cassia. (disabled)' if quest_recruitahunter_dalit_started and not quest_recruitahunter_cassia_points:
                pass
            'I need to learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold:
                pass
            '“Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here’s what I heard about {color=#f6d6bd}Cassia{/color}...”')
                if not quest_recruitahunter_dalit_about_cassia:
                    $ quest_recruitahunter_dalit_about_cassia = 2
                $ quest_recruitahunter_dalit_about_cassia_completed = 1
                $ minutes += 5
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2:
                    $ custom1 = "“It sounds like no matter her talents, or the lack thereof, she’s got a harpy of an attitude,” she summarizes your tale and tries to push aside the hair on her forehead. “May be better to spare ourselves the trouble after all.”"
                else:
                    $ custom1 = "“Not the easiest attitude to deal with, you say,” she twirls her hair. “I ain’t so sure we need even more arguments around here.”"
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                jump peltnorth_dalit_recruitahunter02
            'I could still learn more about Cassia. (disabled)' if quest_recruitahunter_dalit_started and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_dalit_about_cassia_completed:
                pass
            '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_about_reward and not quest_recruitahunter_dalit_started:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                $ quest_recruitahunter_dalit_started = 1
                $ quest_recruitahunter = 1
                $ renpy.notify("New entry: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Recruit a Hunter{/i}')
                $ minutes += 5
                jump leavingthepeltnorth02
            '“I’ll tell you if I learn anything.”' if quest_recruitahunter_dalit_started and not (quest_recruitahunter_dalit_about_erastos_completed and quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_dalit_about_reward_granted):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump peltnorthtalkingwithguardsafterquestions

    label peltnorth_dalit_recruitahunter03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So who are you going to hire?”')
        $ quest_recruitahunter_dalit_about_reward_granted = 1
        $ quest_recruitahunter = 2
        $ renpy.notify("Quest completed: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Recruit a Hunter{/i}')
        if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2 and quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2:
            $ quest_recruitahunter_noonerecruited = 1
            $ quest_recruitahunter_description02 = "{color=#f6d6bd}Dalit{/color} rejected both hunters. I received my reward, but she would like to know if I meet a trustworthy candidate."
            $ custom1 = (8-appearance_price)
            $ coins += custom1
            show screen notifyimage( "+%s" %custom1, "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+%s {image=cointest}{/i}' %custom1)
            $ dalit_friendship += 2
            $ iason_friendship_moneybonus_points += 4
            menu:
                '“With two {i}terrible{/i} choices, I’d rather wait another year,” she scoffs and prepares her pouch. “Thanks, [pcname], you saved us quite a journey. But let me know if you happen to meet someone who could use a risky, but good-paying job.” She counts down five rings, then sizes you up and pulls out a few more.
                '
                '“Maybe I’ll find someone.”' if not quest_recruitahunter_spokento_shoshi:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe I’ll find someone.”')
                    $ questionpreset = "dalit1"
                    menu:
                        '“Sure sounds like you’ve talent for meeting people!” She lets out a chuckle.
                        '
                        '(dalit1 set)':
                            pass
                '“I spoke with this strong lumberjack...”' if quest_recruitahunter_spokento_shoshi:
                    label peltnorth_dalit_recruitahunter_shoshi01:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with this strong lumberjack...”')
                        $ questionpreset = "dalit1"
                        $ quest_recruitahunter_spokento_shoshi_recruited = 1
                        $ dalit_friendship += 1
                        $ iason_friendship_moneybonus_points += 2
                        $ iason_friendship += 1
                        $ iason_shop_crossbow_discount += 5
                        menu:
                            'Your short tale is met with her wide smile. “But I do remember {color=#f6d6bd}Shoshi{/color}! She made quite the impression last time she was here... So she’s bored in {color=#f6d6bd}Creeks{/color}, you’re saying? I guess I {i}could{/i} speak with her.”
                            \n\nAs the rumor spreads through the rest of her guards, you notice {color=#f6d6bd}the smiling innkeep{/color} standing in the open door. He spares you a polite nod, then goes back inside.
                            '
                            '(dalit1 set)':
                                pass
        else:
            $ quest_recruitahunter_description01 = "I received my reward."
            $ questionpreset = "dalit1"
            $ coins += 5
            show screen notifyimage( "+5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+5 {image=cointest}{/i}')
            $ dalit_friendship += 1
            $ iason_friendship_moneybonus_points += 2
            if quest_recruitahunter_erastos_points < quest_recruitahunter_cassia_points:
                $ quest_recruitahunter_erastosrecruited = 1
                $ custom1 = "“I guess {color=#f6d6bd}Erastos{/color} ain’t hopeless, and as long as he’s going to focus on the traps, maybe he won’t ruin any hunts. We’ll go to {color=#f6d6bd}Howler’s{/color} before winter, speak with him ourselves.”"
            elif quest_recruitahunter_erastos_points == quest_recruitahunter_cassia_points:
                $ quest_recruitahunter_erastosrecruited = 1
                $ custom1 = "“I guess neither of them is much better than the other, but at least {color=#f6d6bd}Erastos{/color} lives closer. As long as he’s going to focus on the traps, maybe he won’t ruin any hunts. We’ll go to {color=#f6d6bd}Howler’s{/color} before winter, speak with him ourselves.”"
            else:
                $ quest_recruitahunter_cassiarecruited = 1
                $ custom1 = "“I guess {color=#f6d6bd}Cassia{/color} can land a few hits, maybe enough to keep the others safe. We’ll go to {color=#f6d6bd}Gale Rocks{/color} before winter, speak with her ourselves.”"
            menu:
                'She attempts to move her hair behind her shoulders. [custom1] She prepares her pouch and counts down five rings. “Thanks, [pcname].”
                '
                '(dalit1 set)':
                    pass
