# Glaucia - green gambeson, emerald eyes - one healthy and one scarred, shiny "jangling" mail, likes to put her hands on her sides, or on her back. "She raises her healthy eyebrow", has massive/heavy boots with buckles she likes to adjust, Taps the hilt of her sickle-sword

default glaucia_fluff = ""
default glaucia_fluff_old = ""

default glaucia_metwith = 0
default glaucia_firstattitude = 0
default glaucia_friendship = 0
default glaucia_friendship_tier = 0
default glaucia_annoyed = 0
default glaucia_dayoflastvisit = 0
default glaucia_questionstoday = 0

default glaucia_about_nomoreundead = 0

default glaucia_about_vote = 0
default glaucia_about_galerocksdecision = 0
default glaucia_about_galerocksdecision_liedto = 0
default glaucia_about_returningtoparents = 0
default glaucia_willreturntogalerocks = 0
default glaucia_woundedpc = 0

default glaucia_spices_available = 0
default glaucia_spices_bought = 0
default glaucia_spices_price_base = 30
default glaucia_spices_price = 0

default glaucia_about_iason1 = 0
default glaucia_about_iason2 = 0

default glaucia_about_herself = 0
default glaucia_about_protectingthewoods = 0
default glaucia_about_attackingpeople = 0
default glaucia_about_pastbandits = 0
default glaucia_about_cityinfluence = 0
default glaucia_about_shortcut = 0
default glaucia_about_dolmen_underground_firsttime = 0
default glaucia_about_dolmen_underground_firsttime_refused = 0

default glaucia_about_runaway = 0
default glaucia_about_runaway_bonusquestion1 = 0
default glaucia_about_runaway_bonusquestion2 = 0
default glaucia_about_runaway_bonusquestion3 = 0
default glaucia_about_runaway_bonusquestion4 = 0
default glaucia_about_runaway_bonusquestion5 = 0
default glaucia_about_runaway_bonusquestion6 = 0

default glaucia_about_spyonnecromancers_negativereaction = 0
default glaucia_about_spyonnecromancers = 0
default glaucia_about_spyonnecromancers_bonusquestion1 = 0
default glaucia_about_spyonnecromancers_bonusquestion2 = 0
default glaucia_about_spyonnecromancers_bonusquestion3 = 0
default glaucia_about_spyonnecromancers_bonusquestion4 = 0
default glaucia_about_spyonnecromancers_bonusquestion5 = 0
default glaucia_about_spyonnecromancers_bonusquestion6 = 0

default glaucia_about_abandonedwagon = 0
default glaucia_about_lostmerchants = 0
default glaucia_about_lostmerchants_trail = 0
default glaucia_about_arrow = 0

default glaucia_about_plague = 0
default glaucia_about_undead = 0
default glaucia_about_necklace = 0
default glaucia_about_beach = 0

default glaucia_about_vendetta_whitemarshes_friendshiplevel = 8
default glaucia_about_vendetta_whitemarshes_gray = 0
default glaucia_about_vendetta_whitemarshes = 0
default glaucia_about_pasttragedy = 0

default glaucia_about_vendetta_howlers = 0
default glaucia_about_orentius = 0

default glaucia_about_steephouse1 = 0
default glaucia_about_steephouse2_friendshiplevel = 6
default glaucia_about_steephouse2_gray = 0
default glaucia_about_steephouse2 = 0 # description_glaucia12 = 0 #"I’ve learned that many years ago she found a husband in the south - in the village of {color=#f6d6bd}Steep House{/color}."
default glaucia_about_steephouse3 = 0

default glaucia_about_asterion1 = 0 # ogólne pytanie
default glaucia_about_asterion2 = 0 # description_glaucia11 = 0 #"According to {color=#f6d6bd}Elah{/color}, she was involved with {color=#f6d6bd}Asterion’s{/color} disappearance."
default glaucia_about_highhisland = 0 # (asterion_highisland_knowsabout and not cephasgaiane_about_highisland and options_cephasgaiane_highisland) or (description_highisland00 and not cephasgaiane_about_highisland and options_cephasgaiane_highisland)
default glaucia_about_asterion3 = 0 # spilling the beans
default glaucia_about_asterion3_bonusquestion1 = 0
default glaucia_about_asterion3_bonusquestion2 = 0
default glaucia_about_asterion3_bonusquestion3 = 0
default glaucia_about_asterion3_bonusquestion4 = 0
default glaucia_about_asterion3_bonusquestion5 = 0
default glaucia_about_asterion4 = 0 # found

default glaucia_invitingtojoin = 0
default glaucia_invitingtojoin_discarded = 0

label banditshideoutglauciaregular01:
    if (whitemarshes_attacked and not glaucia_about_nomoreundead) or (whitemarshes_destroyed and not glaucia_about_nomoreundead) or (whitemarshes_nomoreundead and not glaucia_about_nomoreundead):
        $ glaucia_about_nomoreundead = 1
        $ glaucia_questionstoday += 1
        $ glaucia_dayoflastvisit = day
        if not whitemarshes_attack_companion_bandits:
            if orentius_spared:
                $ glaucia_questionstoday = 0
                $ glaucia_friendship -= 2
                if whitemarshes_attacked and quest_spyonwhitemarshes == 1:
                    $ quest_spyonwhitemarshes = 3
                    $ renpy.notify("Quest completed: Spy on White Marshes")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
                $ questionpreset = "glaucia1"
                menu:
                    'She frowns at the sight of you, narrowing her healthy eye, then stalks away. “You’re brave to return here after your failure at {color=#f6d6bd}Marshes{/color}. Too bad you didn’t seek my help before. Somehow, all them roadwardens keep putting {i}more{/i} work on my shoulders.” She takes a deep breath. “How do you want to waste my time now? You need a broom to sweep a road?”
                    '
                    '(glaucia1 set)':
                        pass
            elif quest_spyonwhitemarshes == 1:
                if whitemarshes_destroyed:
                    $ custom6 = "Our watchers saw the commotion. The price you paid to set us free from the necromancers was high, but the risk you defeated was greater. I applaud your judgment, I merely wish I was there to see it happen."
                    $ glaucia_friendship += 3
                elif orentius_banished:
                    $ custom6 = "Our watchers saw the commotion. I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. Good job, warden."
                    $ glaucia_friendship += 2
                elif orentius_convinced:
                    $ custom6 = "Our watchers saw the commotion. I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. I would merely prefer to not put {i}hope{/i} into your judgment."
                    $ glaucia_friendship += 1
                $ glaucia_friendship_tier += 1
                $ quest_spyonwhitemarshes = 2
                $ renpy.notify("Quest completed: Spy on White Marshes")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
                menu:
                    'She welcomes you with a grin. “So I’ve heard you pushed your {i}spying{/i} quite far!” She pats your elbow and leads you deeper into the hamlet. “[custom6] Now, I was meant to give you something back, wasn’t I? What do you want? Twelve coins, or two healing potions?”
                    '
                    '“Potions, obviously.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Potions, obviously.”')
                        $ quest_spyonwhitemarshes_description02 = "I received my reward."
                        $ quest_spyonwhitemarshes = 2
                        $ renpy.notify("Quest completed: Spy on White Marshes.\nYou received two healing potions.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. You received two healing potions.{/i}')
                        $ item_generichealingpotion += 2
                        $ quest_runaway_description01 = "I received my reward."
                        $ questionpreset = "glaucia1"
                        menu:
                            'She glances at one of the guards. He stalks toward you and hands you a small box engraved with the shapes of leaves, but after you put it under your arm, he clears his throat. “I need it,” he grouses, and you take out the fragile, earthenware bottles, returning the box to him. {color=#f6d6bd}Glaucia{/color} ignores the exchange. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                            '
                            '(glaucia1 set)':
                                pass
                    '“Dragons are always useful.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragons are always useful.”')
                        $ quest_spyonwhitemarshes_description02 = "I received my reward."
                        $ quest_spyonwhitemarshes = 2
                        show screen notifyimage( "Quest completed: Spy on White Marshes.\n+12", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. +12 {image=cointest}{/i}')
                        $ coins += 12
                        $ quest_runaway_description01 = "I received my reward."
                        $ questionpreset = "glaucia1"
                        menu:
                            'She glances at one of the guards. He throws you a small pouch, and you toss it upward a few times. Should be enough.
                            \n\n{color=#f6d6bd}Glaucia{/color}, making enough noise of her own, ignores the rattling coins. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                            '
                            '(glaucia1 set)':
                                pass
            else:
                if whitemarshes_destroyed:
                    $ custom6 = "Our watchers saw the commotion. The price you paid to set us free from the necromancers was high, but the risk you defeated was greater. I applaud your judgment, I merely wish I was there to see it happen."
                    $ glaucia_friendship += 3
                elif orentius_banished:
                    $ custom6 = "Our watchers saw the commotion. I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. Good job, warden."
                    $ glaucia_friendship += 2
                elif orentius_convinced:
                    $ custom6 = "Our watchers saw the commotion. I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. I would merely prefer to not put {i}hope{/i} into your judgment."
                    $ glaucia_friendship += 1
                $ questionpreset = "glaucia1"
                menu:
                    'She welcomes you with a grin, and leads you deeper into the hamlet.“[custom6]”
                    '
                    '(glaucia1 set)':
                        pass
        else:
            if quest_spyonwhitemarshes == 1:
                if whitemarshes_destroyed:
                    $ custom6 = "The price we paid was great, but better this than the necromancer being a thorn in our sides."
                    $ glaucia_friendship += 3
                elif orentius_banished:
                    $ custom6 = "I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land."
                    $ glaucia_friendship += 2
                elif orentius_convinced:
                    $ custom6 = "I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. I would merely prefer to not put {i}hope{/i} into your judgment."
                    $ glaucia_friendship += 1
                $ glaucia_friendship_tier += 1
                if whitemarshes_attack_glauciathreatened:
                    $ custom1 = "with a polite nod. “I assume you’re here to celebrate our triumph, and not to keep throwing vain threats around."
                elif whitemarshes_attack_glauciaattackedpc:
                    $ custom1 = "with a kind nod. “How’s your head?"
                else:
                    $ custom1 = "with a kind nod. “Here to celebrate our triumph?"
                $ quest_spyonwhitemarshes = 2
                $ renpy.notify("Quest completed: Spy on White Marshes")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
                menu:
                    'She welcomes you [custom1] [custom6]” After a short pause, she taps her side, as if she’s looking for something in invisible pockets. “I was meant to give you something back for the spying, and I believe you fulfilled your duties. What do you want? Twelve coins, or two healing potions? [custom3]”
                    '
                    '“Potions, obviously.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Potions, obviously.”')
                        $ quest_spyonwhitemarshes_description02 = "I received my reward."
                        $ quest_spyonwhitemarshes = 2
                        $ renpy.notify("Quest completed: Spy on White Marshes.\nYou received two healing potions.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. You received two healing potions.{/i}')
                        $ item_generichealingpotion += 2
                        $ quest_runaway_description01 = "I received my reward."
                        $ questionpreset = "glaucia1"
                        menu:
                            'She glances at one of the guards. He stalks toward you and hands you a small box engraved with the shapes of leaves, but after you put it under your arm, he clears his throat. “I need it,” he grouses, and you take out the fragile, earthenware bottles, returning the box to him. {color=#f6d6bd}Glaucia{/color} ignores the commotion. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                            '
                            '(glaucia1 set)':
                                pass
                    '“Dragons are always useful.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragons are always useful.”')
                        $ quest_spyonwhitemarshes_description02 = "I received my reward."
                        $ quest_spyonwhitemarshes = 2
                        show screen notifyimage( "Quest completed: Spy on White Marshes.\n+12", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. +12 {image=cointest}{/i}')
                        $ coins += 12
                        $ quest_runaway_description01 = "I received my reward."
                        $ questionpreset = "glaucia1"
                        menu:
                            'She glances at one of the guards. He throws you a small pouch, and you toss it upward a few times. Should be enough.
                            \n\n{color=#f6d6bd}Glaucia{/color}, making enough noise of her own, ignores the rattling of the coins. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                            '
                            '(glaucia1 set)':
                                pass
            else:
                if whitemarshes_destroyed:
                    $ custom6 = "The price we paid was great, but better this than the necromancer being a thorn in our sides."
                    $ glaucia_friendship += 3
                elif orentius_banished:
                    $ custom6 = "I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land."
                    $ glaucia_friendship += 2
                elif orentius_convinced:
                    $ custom6 = "I’d rather see the necromancer pay the price for his deeds... But at least he’s away from my land. I would merely prefer to not put {i}hope{/i} into your judgment."
                    $ glaucia_friendship += 1
                $ glaucia_friendship_tier += 1
                if whitemarshes_attack_glauciathreatened:
                    $ custom1 = "with a polite nod. “I assume you’re here to celebrate our triumph, and not to keep throwing vain threats around."
                elif whitemarshes_attack_glauciaattackedpc:
                    $ custom1 = "with a kind nod. “How’s your head?"
                else:
                    $ custom1 = "with a kind nod. “Here to celebrate our triumph?"
                $ questionpreset = "glaucia1"
                menu:
                    'She welcomes you [custom1] [custom6]” After a short pause, she nods for you to join her in her stroll.
                    '
                    '(glaucia1 set)':
                        pass
    elif glaucia_dayoflastvisit != day:
        $ glaucia_dayoflastvisit = day
        $ glaucia_questionstoday = 0
        label glaucia_fluffloop:
            $ glaucia_fluff = ""
            $ glaucia_fluff = renpy.random.choice(['{color=#f6d6bd}Glaucia{/color} is walking around the shelter, lost in her thoughts.', 'You’re told to wait, since {color=#f6d6bd}Glaucia{/color} is wandering outside the hamlet with a few of her men. You hear a loud whistle, then another, and after a few minutes, the entire group is back. Their leader gestures for you to join her on her walk.', '{color=#f6d6bd}Glaucia{/color} is standing with the only other woman who belongs to her band, laughing about something she’s said. She then walks toward you and gestures for you to walk with her, while the other person steps away, observing you distrustfully.', '{color=#f6d6bd}Glaucia{/color} is sitting on a bench, eating dried bread loudly. After you get closer, she covers it with a linen sheet, and gestures for you to walk with her.', '{color=#f6d6bd}Glaucia{/color} is observing her mail, which seems to be even more polished than usual.', '{color=#f6d6bd}Glaucia{/color} is standing next to a tree stump, washing her heavy boots with a wet cloth. Seeing your arrival, she adjusts the buckles, and gestures for you to walk with her around the shelter.'])
            if glaucia_fluff_old == glaucia_fluff:
                jump glaucia_fluffloop
            else:
                $ glaucia_fluff_old = glaucia_fluff
        $ questionpreset = "glaucia1"
        menu:
            '[glaucia_fluff]
            '
            '(glaucia1 set)':
                pass
    else:
        $ questionpreset = "glaucia1"
        menu:
            'She frowns at the sight of you, but doesn’t stop her stroll.
            '
            '(glaucia1 set)':
                pass

label banditshideoutglauciaafterinteraction01:
    $ questionpreset = "glaucia1"
    menu:
        'You walk forward, listening to {color=#f6d6bd}Glaucia’s{/color} heavy boots and jangling mail.
        '
        '(glaucia1 set)':
            pass

label banditshideoutglauciapersonalquestionsALL:
    label banditshideoutglaucia_about_herself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about you.”')
        if (glaucia_friendship+appearance_charisma) < 4:
            $ glaucia_about_herself = 1
            $ questionpreset = "glaucia1"
            menu:
                'She doesn’t even stop. “Hire yourself a bard,” she growls.
                '
                '(glaucia1 set)':
                    pass
        else:
            $ glaucia_about_herself = 2
            if not quest_ruins_10yclue11 and quest_ruins == 1 and quest_ruins_description01:
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
            $ quest_ruins_10yclue11 = "{color=#f6d6bd}Glaucia{/color} became a bandit."
            $ questionpreset = "glaucia1"
            menu:
                'She stops, smirking as she rubs a large nettle leaf between her fingers. “Are there no bards who would sing you to sleep? There ain’t much story in me to share. As a young lass, I was taught to sew for food, and planned to start a family with a kind cobbler.”
                \n\nHer voice weakens, and she looks down at her boots. “I had to leave my family, but I accepted it. On my way to the wedding, them awoken shells took my closest friend, my face, and the hand I worked with, but I accepted it. The Wright gave me no kids, but I accepted it.”
                \n\nShe then runs her eyes over the nearby guards, raising her voice almost to a shout. “But after them {i}monsters{/i} hit my home and shattered everything I had built or loved, I would {i}not{/i} accept it. With or without The Wright, I’ll make those butchers pay!” Her wounded eye, far from being free of the pain it has seen, looks at you with determination. “I’ve been here for ten years now, and I’ll be here as long as it takes. By myself, if I must.”
                \n\nTapping the hilt of her sword, she moves forward.
                '
                '(glaucia1 set)':
                    pass
        label banditshideoutglaucia_about_herself02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about you.”')
            $ glaucia_about_herself = 2
            if not quest_ruins_10yclue11 and quest_ruins == 1 and quest_ruins_description01:
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
            $ quest_ruins_10yclue11 = "{color=#f6d6bd}Glaucia{/color} became a bandit."
            $ questionpreset = "glaucia1"
            menu:
                'She stops, and rubs a large nettle leaf between her fingers. “There ain’t much story in me to share. As a young lass, I was taught to sew for food, and planned to start a family with a kind cobbler.” Her voice weakens, and she looks down at her boots. “I had to leave my family, and I accepted it. On my way to the wedding, them awoken shells took my closest friend, my face, and the hand I worked with, and I accepted it. The Wright gave me no kids, and I accepted it.”
                \n\nShe then runs her eyes over the nearby guards, raising her voice almost to a shout. “But after them {i}monsters{/i} hit my home and shattered everything I had built or loved, I would {i}not{/i} accept it. With or without The Wright, I’ll make those butchers pay!” Her wounded eye, far from being free of the pain it has seen, looks at you with determination. “I’ve been here for ten years now, and I’ll be here as long as it takes. By myself, if I must.”
                \n\nTapping the hilt of her sword, she moves forward.
                '
                '(glaucia1 set)':
                    pass

    label banditshideoutglaucia_about_pasttragedy01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Foggy{/color} mentioned some dark days pushed you into becoming a bandit.”')
        label banditshideoutglaucia_about_pasttragedy02:
            $ glaucia_about_pasttragedy = 1
            $ glaucia_about_vendetta_whitemarshes_friendshiplevel -= 2
            $ glaucia_about_steephouse2_friendshiplevel -= 2
            $ ruinedvillage_name = "Steep House"
            $ description_bandits06 = "According to {color=#f6d6bd}Glaucia{/color}, every member of her band has been {i}wronged by this land{/i}."
            if not glaucia_about_steephouse2:
                $ custom1 = "the long-gone village of "
            else:
                $ custom1 = ""
            $ questionpreset = "glaucia1"
            menu:
                '“More of them than you can count. Or did you think people leave their warm homes to pick easy coins? We have survivors from [custom1]{color=#f6d6bd}Steep House{/color}; a lad forced into marriage by some old pricks with long beards; a cooper whose daughter poisoned herself with a {i}daffodil pie{/i}; a hunter whose home was lost to a fire; a shepherd who took an oath to clean these woods of wolves; a hungry thief who chose to run away, instead of losing their arm.”
                \n\nThe guards are now more numerous. Some of them look down, casting you shameful glances, while others meet your eyes, keeping their backs straight. “We were all wronged by this land,” {color=#f6d6bd}Glaucia{/color} carries on, and as her steps grow springy, her mail becomes annoyingly loud. “And our {i}work{/i} will give us our pride back.”
                '
                '(glaucia1 set)':
                    pass

        label banditshideoutglaucia_about_pasttragedy01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Foggy{/color} mentioned that the other members of your group were also pushed into becoming bandits by some dark events.”')
            jump banditshideoutglaucia_about_pasttragedy02

    label banditshideoutglaucia_about_shortcut01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “After spending a few days on these roads, I’m surprised your band hasn’t been mauled to death yet.”')
        $ glaucia_about_shortcut = 1
        $ description_shortcut10 = "According to {color=#f6d6bd}Glaucia{/color}: “There ain’t anything free in the woods. A lost bone, rotten apple, shiny pebble, a cave. Everything will be eaten or taken away, and if it’s laying there all by itself, you better wonder why.”"
        $ questionpreset = "glaucia1"
        menu:
            'She looks at a man who’s missing an eye. “We’ve been marked in many ways,” she starts carefully, “and we’ve burnt our share of shells. Not all of us were here from the beginning, you see.”
            \n\nAfter you ask her for any tips on how to survive on the road, she shrugs, then moves her hands behind her back, still turned away from you. “Not for a rider, I don’t. When we move in a strong group, smaller monsters stay away, and {i}you{/i} can’t fight the packs numerous enough to attack {i}us{/i}.” Her pause is long enough that you consider changing the topic, but she then carries on. “What you need to learn is that there ain’t anything free in the woods. A lost bone, rotten apple, shiny pebble, a cave. Everything will be eaten or taken away, and if it’s laying there all by itself, you better wonder why.”
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_protectingthewoods01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why don’t you try to secure these roads?”')
        $ glaucia_about_protectingthewoods = 1
        $ description_glaucia15 = "She seems to be fine with the local roads growing more dangerous."
        $ questionpreset = "glaucia1"
        menu:
            'She kicks away a small rock, one of many you step upon. “The roads are fine as they are.”
            \n\nYou ask her for any thoughts on how people see them as dangerous, too much so for maintaining any trade, but she chuckles in response. “Some of them will do better by never leaving their homes.”
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_attackingpeople01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who are you even robbing on these roads?”')
        $ glaucia_about_attackingpeople = 1
        $ questionpreset = "glaucia1"
        menu:
            '“You don’t understand our path, stranger,” her voice is harsh, but carries no grudge. “Yes, we took a few things from the settlements, or forced some merchants to pay us for {i}escorting{/i} them,” she says with amusement, “but we ain’t some bloodthirsty robbers. We cut our own firewood, hunt to fill our bellies, trade if we need to. You’d be surprised,” she turns around and takes a few steps backwards, gazing into your eyes, “how little work one needs when you have strong arms, no {i}taxes{/i}, and no young or old mouths to feed.”
            \n\nYou glance at the massive hole in the southern part of the wall. Her lips tighten, and she turns away again. “We won’t stay in this place for much longer.”
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_pastbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re lucky that the soldiers from {color=#f6d6bd}Hovlavan{/color} took care of the band dwelling in {color=#f6d6bd}Hag Hills{/color}.”')
        $ glaucia_about_pastbandits = 1
        $ description_tulia05 = "It seems like {color=#f6d6bd}Glaucia{/color} was collaborating with {color=#f6d6bd}Tulia{/color} in the past."
        $ questionpreset = "glaucia1"
        menu:
            'She walks without a word for a good few heartbeats. Three rooks are searching for food in the grass, ignoring her heavy steps and mail, yet toddling away once you approach them. “I had {i}different opinions{/i} on the range of their territory,” she looks at her guards with pride. “They had enough muscle to become a threat, but were careless, and had no {i}purpose{/i}, merely hunger. We were around long before them. They’re gone, but we remain. Such is Wright’s will for us.”
            \n\nBefore she resumes her stroll, she meets your eyes and nod slowly. “Right, we were lucky. Say {i}hi{/i} to {color=#f6d6bd}Tulia{/color} from me. I’ll see her soon.” She responds to your frown with a smirk, then turns away.
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_dolmen_underground_firsttime01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider telling her about the secret trapdoor from the dolmen.')
        menu:
            'You wander behind her, under the keen eyes of the other members of her band. Their harsh looks can’t hide their unrest.
            \n\nGiving them yet another hideout could save their lives during difficult journeys, but they could just as well use it to {i}practice their trade{/i}, so to speak.
            '
            'I tell her everything. Her trust is worth it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Her trust is worth it.')
                $ glaucia_about_dolmen_underground_firsttime = 1
                $ glaucia_friendship += 1
                $ minutes += 1
                $ questionpreset = "glaucia1"
                menu:
                    'Their leader doesn’t interrupt you, nor slows down her pace. After you’re done, she says without a hint of emotion, but you notice the unnatural pause. “Of course,” she tries to maintain her composure, “but if you’re trying to impress me, you need to try harder.”
                    \n\nYou look at the surprised glances of the others, and try to hide your smile. You got them.
                    '
                    '(glaucia1 set)':
                        pass
            'Maybe I can’t stop them on my own, but I won’t aid them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I can’t stop them on my own, but I won’t aid them.')
                $ glaucia_about_dolmen_underground_firsttime_refused = 1
                $ minutes += 1
                $ questionpreset = "glaucia1"
                menu:
                    'You keep walking, but find the strength in you to answer the tense looks of others.
                    '
                    '(glaucia1 set)':
                        pass
            'I need to think about it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to think about it.')
                $ questionpreset = "glaucia1"
                menu:
                    'Though you say nothing, the clinking armor offers you not a moment of silence.
                    '
                    '(glaucia1 set)':
                        pass

label banditshideoutglauciaglaucia_spices_available01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you still have the spices you {i}took{/i} from the merchants? I need some to get on the good side of {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”')
    $ renpy.notify("New trader unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
    $ glaucia_spices_available = 1
    $ glaucia_spices_price = (glaucia_spices_price_base-glaucia_friendship+appearance_price)
    menu:
        '“This again? You’re in luck, we sell our wares sparsely to make sure everyone needs them.” She turns toward you and runs her eyes over you, then pats your arm with her strong hand. “I’ll give you a box with many different sacks for [glaucia_spices_price] coins. I give discounts to helpful allies.”
        '
        '“[glaucia_spices_price]... Very well.”' if coins >= glaucia_spices_price and not item_spices:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “%s... Very well.”' %glaucia_spices_price)
            $ item_spices = 1
            $ coins -= glaucia_spices_price
            $ glaucia_friendship += 1
            $ glaucia_questionstoday += 1
            $ glaucia_spices_bought = day
            show screen notifyimage( "You bought the spices.\n-%s" %glaucia_spices_price, "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the spices. -%s {image=cointest}{/i}' %glaucia_spices_price)
            jump banditshideoutglauciaafterinteraction01
        'I can’t afford them. (disabled)' if coins < glaucia_spices_price and not item_spices:
            pass
        'I already have some spices. (disabled)' if item_spices:
            pass
        '“I’ll think about it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
            jump banditshideoutglauciaafterinteraction01

label banditshideoutglauciaglaucia_spices_available02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About those spices...”')
    $ shop = "glaucia"
    show screen shopscreen with dissolve
    $ questionpreset = "glaucia1"
    menu:
        'She gives you an annoyed glance and mentions her price.
        '
        '(glaucia1 set)':
            pass

label banditshideoutglaucia_about_plague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may want to stay away from {color=#f6d6bd}Old Págos{/color}. It’s been struggling with a plague.”')
    $ glaucia_about_plague = 1
    $ questionpreset = "glaucia1"
    menu:
        'She glances at you with her unmarked eyebrow raised, making the difference between the sizes of her eyes even more jarring. “You think I don’t know what’s happening in my land? I don’t need your rumors.”
        '
        '(glaucia1 set)':
            pass

label banditshideoutglaucia_about_undead01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about the undead in the North?”')
    $ glaucia_about_undead = 1
    menu:
        'Her armor clinks so loudly that a nearby rook flutters its wings, dashing to the wall. “They are... around.” She meets your eyes, tapping the hilt of her sword. “Why do you ask?”
        '
        '“They need to be dealt with, of course.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They need to be dealt with, of course.”')
            $ glaucia_friendship += 1
            $ glaucia_questionstoday += 1
            $ description_whitemarshes12 = "According to {color=#f6d6bd}Glaucia{/color}, the villagers are using more than just their own dead - they are willing to seek corpses in the wilderness."
            $ description_glaucia16 = "She feels deep hatred toward the undead of {color=#f6d6bd}White Marshes{/color}."
            $ questionpreset = "glaucia1"
            menu:
                'She stares at you, then nods vigorously and turns away, carrying on with her walk. “You’ve got a clear eye. There are some undead in the darkest thickets and caves, but they ain’t anything more than a gentle rash on a shell filled with poison. {color=#f6d6bd}White Marshes{/color}, with their dark arts and crazy warlocks, are the real danger, and a part of our {i}work{/i} is taking any bone we can get away from them.”
                \n\nYou ask her to say something more and she slows down. “They ain’t merely using their own dead, outsider. They seek the shells in the woods, they scavenge for them, like,” she waves at one of the rooks, which opens its mouth in objection. “Shame on the villages that let them do so, may The Wright drown them all.”
                '
                '(glaucia1 set)':
                    pass
        '“I wonder if you see them as a threat.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder if you see them as a threat.”')
            $ description_whitemarshes12 = "According to {color=#f6d6bd}Glaucia{/color}, the villagers are using more than just their own dead - they are willing to seek corpses in the wilderness."
            $ description_glaucia16 = "She feels deep hatred toward the undead of {color=#f6d6bd}White Marshes{/color}."
            $ glaucia_friendship -= 1
            $ questionpreset = "glaucia1"
            menu:
                'Her eyes are filled with fury. “What do you think? Those fuckers at {color=#f6d6bd}White Marshes{/color} wake up more shells with every season, no matter where they find them. Deep woods, the swamps, their own beds. If they could,” her hand soars toward your neck, causing you to step away. She stops herself before reaching you, but makes a gesture suggesting a blade making a cut. “They would kill us all in our sleep.”
                \n\nShe strides away and you try to catch up. After a pause, she raises her voice. “Shame on the villages that let them do so, may The Wright drown them all.”
                '
                '(glaucia1 set)':
                    pass
        '“I’d rather be prepared for anything.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather be prepared for anything.”')
            $ description_whitemarshes12 = "According to {color=#f6d6bd}Glaucia{/color}, the villagers are using more than just their own dead - they are willing to seek corpses in the wilderness."
            $ description_glaucia16 = "She feels deep hatred toward the undead of {color=#f6d6bd}White Marshes{/color}."
            $ questionpreset = "glaucia1"
            menu:
                'She stares at you, then turns away slowly, carrying on with her walk. “There are some undead in the darkest thickets and caves, but they ain’t anything more than a gentle rash on a shell filled with poison. {color=#f6d6bd}White Marshes{/color}, with their dark arts and crazy warlocks, are the real danger, and a part of our {i}work{/i} is taking away any bone we can get from them.”
                \n\nYou ask her to say something more and she slows down. “They ain’t merely using their own dead, outsider. They seek the shells in the woods, they scavenge for them, like,” she waves at one of the rooks, which opens its mouth in objection. “Shame on the villages that let them do so, may The Wright drown them all.”
                '
                '(glaucia1 set)':
                    pass

label banditshideoutglaucia_about_necklace01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the pouch with a necklace. “I think this belongs to you.”')
    $ glaucia_about_necklace = 1
    $ glaucia_questionstoday += 1
    $ item_oceannecklace = 0
    $ renpy.notify("You gave away the ocean necklace.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the ocean necklace.{/i}')
    if glaucia_friendship >= 6:
        $ custom1 = "She turns toward you, observing your hands with curiosity, but once she sees the trinket, she stands still with an open mouth. After a few heartbeats, she smiles awkwardly and reaches toward you with an open, four-fingered palm."
    else:
        $ custom1 = "Hearing you reach for something, she leaps away and turns toward you rapidly, but seeing the trinket, she stands still with an open mouth. After a few heartbeats, she clears her throat and reaches toward you with an open, four-fingered palm."
    menu:
        '[custom1] “So it is, stranger, but I ain’t one to keep around sentimental rubbish.” She glances at her boots. “Cheers, I guess.”
        '
        'I smile and toss it to her. “Also, {color=#f6d6bd}Rufina{/color} will make you a new one next time you get {i}home{/i}. And she’ll kick your teeth out.”' if galerocks_rufina_about_necklace:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile and toss it to her. “Also, {color=#f6d6bd}Rufina{/color} will make you a new one next time you get {i}home{/i}. And she’ll kick your teeth out.”')
            $ glaucia_friendship += 1
            $ glaucia_about_necklace = 2
            if glaucia_about_returningtoparents:
                $ glaucia_willreturntogalerocks = 1
                $ pc_goal_iwanttohelppoints += 1
            $ questionpreset = "glaucia1"
            menu:
                'She observes the necklace in silence, then glances at the nettles, as if it should find its rest with them. Finally, she puts it in a sack at her side, and her mouth is torn between a smile and remaining tightlipped. “I ain’t sure I like your nosiness,” she speaks slowly, “but I admit I’d like to see {color=#f6d6bd}Rufina’s{/color} kicks in those fancy togs of hers.”
                \n\nHer steps seem a bit lighter than usual.
                '
                '(glaucia1 set)':
                    pass
        'I hold the necklace a bit longer than necessary. “It was at the western beach. Looking for ways to broaden your trade?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hold the necklace a bit longer than necessary. “It was at the western beach. Looking for ways to broaden your trade?”')
            $ glaucia_friendship += 0
            $ glaucia_about_beach = 1
            $ questionpreset = "glaucia1"
            menu:
                'She looks at the necklace in silence, then throws it into the nettles. “And if so? If you plan to keep your ugly nose,” she turns away without so much as a scowl, “you should also look for some {i}safer{/i} opportunities.”
                '
                '(glaucia1 set)':
                    pass

label banditshideoutglaucia_about_orentius01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} wants to deal with {color=#f6d6bd}Orentius{/color} and could use your band’s help.”')
    $ glaucia_about_orentius = 1
    $ glaucia_friendship += 1
    $ glaucia_questionstoday += 1
    $ renpy.notify("Journal updated: Orentius, the Necromancer")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
    $ quest_orentius_thais_description03a07 = "{color=#f6d6bd}Glaucia{/color} and her band are going to join {color=#f6d6bd}Thais{/color} in her efforts."
    $ questionpreset = "glaucia1"
    menu:
        'She slows down, with every step raising her eyes, then clasps her hands behind her back. “From all the bloody souls in the North, this troll cunt is the one who tries to do the {i}right{/i} thing?” She sighs, then turns toward you with narrowed eyes. “Tell her I’ll be at her home soon, but I’m {i}not{/i} putting away my blade at the gate.”
        \n\nYou nod in silence, and as she shares the news with the rest of her band, they react with angry grunts, but not a single word of disobedience.
        '
        '(glaucia1 set)':
            pass

label banditshideoutglaucia_about_lostmerchantsALL:
    label banditshideoutglaucia_about_abandonedwagon01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found an abandoned cart on the eastern trail...”')
        $ glaucia_about_abandonedwagon = 1
        menu:
            'She keeps her pace, forcing you to stare at her hair, then steps outside of the gate, looking around.
            '
            '“And your boots left quite a trail.”' if shortcut_cairn_tracks and quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And your boots left quite a trail.”')
                jump banditshideoutglaucia_about_lostmerchants_trail01alt
            '“And you dropped this arrow there.”' if item_arrow and galerocks_florus_about_arrow and not glaucia_about_arrow:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you dropped this arrow there.”')
                jump banditshideoutglaucia_about_arrow01alt
            '“What do you think about that?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think about that?”')
                $ questionpreset = "glaucia1"
                menu:
                    '“I think you found it indeed,” she walks down the slope, speaking slowly as she takes careful steps. “And whoever used to own it, they have vanished in the fogs, they did.”
                    '
                    '(glaucia1 set)':
                        pass

    label banditshideoutglaucia_about_lostmerchants01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard in {color=#f6d6bd}Gale Rocks{/color} that the villagers are awaiting some spice merchants.”')
        $ glaucia_about_lostmerchants = 1
        $ questionpreset = "glaucia1"
        menu:
            'She doesn’t say a thing, waiting for you to go on.
            \n\n“Do you know anything about it?”
            \n\nShe shrugs. “Nothing you need to hear.”
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_lostmerchants_trail01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I followed the trail leading from the abandoned cart. And here I am.”')
        label banditshideoutglaucia_about_lostmerchants_trail01alt:
            $ glaucia_about_lostmerchants_trail = 1
            $ glaucia_questionstoday += 1
            if quest_fallentree == 1 and quest_lostmerchants == 1:
                $ renpy.notify("Journal updated: Fallen Tree,\nLost Merchants")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Fallen Tree,\nLost Merchants{/i}')
            elif quest_fallentree == 1:
                $ renpy.notify("Journal updated: The Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Fallen Tree{/i}')
            elif quest_lostmerchants == 1:
                $ renpy.notify("Journal updated: The Lost Merchants")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Lost Merchants{/i}')
            $ quest_fallentree_description04 = "I’ve no doubt it was {color=#f6d6bd}Glaucia{/color} and her band who took the people from the wagon at the fallen tree."
            $ quest_lostmerchants_description01 = "I’ve learned that {color=#f6d6bd}Glaucia{/color} and her band attacked the traders. I should report this to {color=#f6d6bd}Severina{/color}."
            ################
            $ custom2 = "She freezes, then turns around slowly, scowling at you. You notice how the slow twist of her wrist makes one of the guards step back, hiding his already drawn blade. “I ain’t going to explain myself to you. We needed tools and wares to sell, so we took them. The merchants are back in their homes, with their skin untouched and togs on their backs. They knew the risk and took it.”\n\nYou flinch when she reaches for your shoulder, but someone is already behind you, keeping you in her range. Her strong hand squeezes your flesh. “Do we have a problem here?”"
            jump banditshideoutglaucia_about_lostmerchants_trail02

    label banditshideoutglaucia_about_arrow01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You dropped this arrow at the abandoned cart.”')
        label banditshideoutglaucia_about_arrow01alt:
            $ glaucia_about_lostmerchants_trail = 1
            $ glaucia_questionstoday += 1
            $ item_arrow -= 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the arrow.{/i}')
            if quest_fallentree == 1 and quest_lostmerchants == 1:
                $ renpy.notify("Journal updated: Fallen Tree,\nLost Merchants.\nYou lost the arrow.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Fallen Tree, Lost Merchants. You lost the arrow.{/i}')
            elif quest_fallentree == 1:
                $ renpy.notify("Journal updated: The Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Fallen Tree. You lost the arrow.{/i}')
            elif quest_lostmerchants == 1:
                $ renpy.notify("Journal updated: The Lost Merchants")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Lost Merchants. You lost the arrow.{/i}')
            $ quest_fallentree_description04 = "I’ve no doubt it was {color=#f6d6bd}Glaucia{/color} and her band who took the people from the wagon at the fallen tree."
            $ quest_lostmerchants_description01 = "I’ve learned that {color=#f6d6bd}Glaucia{/color} and her band attacked the traders. I should report this to {color=#f6d6bd}Severina{/color}."
            ################
            $ custom2 = "She freezes, then turns around too quickly for you to notice how it ends up in her hand. Your fingers are aching for the next few minutes. “{i}Cheers{/i} for returning it to me,” she scowls at you and throws the arrow to one of her guards. “I ain’t going to explain myself to you. We needed tools and wares to sell, so we took them. The merchants are back in their homes, with their skin untouched and togs on their backs. They knew the risk and took it.”\n\nYou flinch when she reaches for your shoulder, but someone is already behind you, keeping you in her range. Her strong hand squeezes your flesh. “Do we have a problem here?”"
            jump banditshideoutglaucia_about_lostmerchants_trail02

        label banditshideoutglaucia_about_lostmerchants_trail02:
            menu:
                '[custom2]
                '
                'I clear my throat. “No problem, {color=#f6d6bd}Glaucia{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “No problem, {color=#f6d6bd}Glaucia{/color}.”')
                    $ minutes += 5
                    $ glaucia_friendship -= 1
                    if pc_hp >= 2:
                        $ custom1 = ", but stay on your feet"
                    else:
                        $ custom1 = " and fall on your butt"
                    $ questionpreset = "glaucia1"
                    menu:
                        'She scoffs at your weak voice and pushes you away. You stumble[custom1]. “So I thought.”
                        \n\nShe adjusts her mail and swaggers away, then pauses to let you keep up with her. “What else?”
                        '
                        '(glaucia1 set)':
                            pass
                'I shake my head slowly. “I needed to know the truth, that’s all.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake my head slowly. “I needed to know the truth, that’s all.”')
                    $ minutes += 5
                    $ questionpreset = "glaucia1"
                    menu:
                        '“You {i}needed{/i}, did you?” You sigh with relief when she releases your shoulder, but then her strong fingers start to pat the front of your neck. “And {i}I{/i} need you to know your place.” Her hand forms a fist and hits your chest gently. “Don’t be a kid. Some questions are better left unanswered.”
                        \n\nHer emerald eyes weigh on you heavier than her touch. She walks away slowly, gesturing for you to follow. “What else?”
                        '
                        '(glaucia1 set)':
                            pass
                'I try to shake her hand off me. “I’m responsible for these roads. Don’t make me your enemy.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to shake her hand off me. “I’m responsible for these roads. Don’t make me your enemy.”')
                    $ minutes += 5
                    $ glaucia_friendship -= 1
                    if armor >= 3:
                        $ custom1 = ", though you feel little pain thanks to your fine armor"
                    else:
                        $ custom1 = ", with your side aching from the fall"
                    $ glaucia_annoyed = day
                    $ can_items = 1
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    menu:
                        '“You can choke on your {i}responsibilities{/i}, for all I care,” you sigh with relief when she releases your shoulder, but then her strong fingers start to pat the front of your neck. “{i}My{/i} enemy, ehm? And what would you do?” The sudden grasp makes you choke, then you land on the ground[custom1]. {color=#f6d6bd}Glaucia{/color} crouches next to you, patting your face. “Scat and think about your tongue. See me another day, if you’ll have something worth saying.”
                        \n\nShe stands up and crosses the gate. Her steps are heavier than usual.
                        '
                        'I get back on my feet and travel to the cairn.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back on my feet and travel to the cairn.')
                            $ travel_destination_shortcut = "cairn"
                            $ pc_area = "shortcut-cairn"
                            $ quarters += 1
                            $ can_leave = 0
                            $ can_rest = 0
                            $ can_items = 0
                            nvl clear
                            $ shortcut_pcknowsabout = 1
                            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                                play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
                            stop nature fadeout 4.0
                            jump cairn01
                '{image=d6} Without a word, I try to withstand her gaze.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Without a word, I try to withstand her gaze.')
                    $ questionpreset = "glaucia1"
                    $ minutes += 5
                    if pc_hp >= 4 or (pc_hp >= 3 and glaucia_firstattitude == "intimidating"):
                        $ glaucia_friendship += 1
                        $ custom1 = "She looks away after a few long breaths, then frowns, her healthy eye showing her surprise, before glancing back at you. “We said what we needed to. What else do you have for me?”\n\nAs she heads for the gate, her steps are heavier than usual."
                    else:
                        $ custom1 = "You look away after a few long breaths, and she smirks with satisfaction, then pushes you away. You stumble, but stay on your feet. “So I thought.”\n\nShe adjusts her mail and swaggers away, then pauses to let you keep up with her. “What else?”"
                    menu:
                        '[custom1]
                        '
                        '(glaucia1 set)':
                            pass

label banditshideoutglaucia_about_iason101:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You made {color=#f6d6bd}%s{/color} quite worried with your recent moves.”' %iason_name)
    $ glaucia_about_iason1 = 1
    $ glaucia_questionstoday += 1
    $ iason_name = "Iason"
    menu:
        'She slows down. The two of you approach the old animal pen, though right now it’s inhabited only by rooks and worms. She leans against the soggy fence, which moans in protest. Her emerald eyes don’t hide her surprise, or perfectly imitate it. “I suppose I should have expected {color=#f6d6bd}Iason’s{/color} boar eyes on me, but what does he want you to get from me, exactly?”
        '
        '“He wanted to be sure you won’t try to target his hunters.”' if quest_intelforpeltnorth_description10:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To learn what you’re trying to achieve. Are you planning to attack his hunters?”')
            if whitemarshes_destroyed or whitemarshes_attacked:
                $ custom1 = "It takes her unusually long to answer. “Alright. You already know it’s the necromancers of {color=#f6d6bd}White Marshes{/color} I wanted. They may be gone, but there are still awoken in these woods, and I need to take care of them. I think of {color=#f6d6bd}Pelt{/color} only so far as our common goals take us.”"
            else:
                $ custom1 = "It takes her unusually long to answer. “Alright. You already know it’s the necromancers of {color=#f6d6bd}White Marshes{/color} I want. I only think of {color=#f6d6bd}Pelt{/color} so far as our common goals take us.”"
            jump banditshideoutglaucia_about_iason102
        '“To learn what you’re trying to achieve. Are you planning to attack his hunters?”' if not quest_intelforpeltnorth_description10:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To learn what you’re trying to achieve. Are you planning to attack his hunters?”')
            if whitemarshes_destroyed or whitemarshes_attacked:
                $ custom1 = "It takes her unusually long to answer. “Alright. Tell him this, stranger: {i}Don’t sweat, {color=#f6d6bd}White Marshes{/color} has fallen, but there are still awoken I need to torch. Also, bed with an ibex.{/i}”"
            else:
                $ custom1 = "It takes her unusually long to answer. “Alright. Tell him this, stranger: {i}Don’t sweat, The Wright leads my blade and dreams against the necromancers of {color=#f6d6bd}White Marshes{/color}. Also, bed with an ibex.{/i}”"
            jump banditshideoutglaucia_about_iason102
        '“I see nothing surprising in an innkeeper who’s worried about bandits.”' if not quest_intelforpeltnorth_description10:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see nothing surprising in an innkeeper who’s worried about bandits.”')
            if whitemarshes_destroyed or whitemarshes_attacked:
                $ custom1 = "Her wide, mirthless grin, more akin to a scowl, makes you think of a dragonling. “You would, if you knew the deeds that tie our pasts. Tell him this, stranger: {i}Don’t sweat, {color=#f6d6bd}White Marshes{/color} has fallen, but there are still awoken I need to torch. Also, bed with an ibex.{/i}”"
            else:
                $ custom1 = "Her wide, mirthless grin, more akin to a scowl, makes you think of a dragonling. “You would, if you knew the deeds that tie our pasts. Tell him this, stranger: {i}Don’t sweat, The Wright leads my blade and dreams against the necromancers of {color=#f6d6bd}White Marshes{/color}. Also, bed with an ibex.{/i}”"
            jump banditshideoutglaucia_about_iason102

    label banditshideoutglaucia_about_iason102:
        if quest_intelforpeltnorth == 1 and quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ quest_intelforpeltnorth_description10 = "I’ve learned that {color=#f6d6bd}Glaucia{/color} is trying to destroy the necromancers of {color=#f6d6bd}White Marshes{/color}. I should bring the news to the keeper."
        $ questionpreset = "glaucia1"
        menu:
            '[custom1]
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_iason201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You speak of {color=#f6d6bd}Iason{/color} as if you work together, but he didn’t agree to let your band move into {color=#f6d6bd}Pelt{/color}, am I wrong?”')
        $ glaucia_about_iason2 = 1
        $ description_glaucia01c = "She implied that {color=#f6d6bd}Iason{/color} lied to me when he mentioned the whole {i}moving to {color=#f6d6bd}Pelt{/color}{/i} dispute."
        $ questionpreset = "glaucia1"
        menu:
            '“Oh, that old quarrel?” She blinks a few times, with her wounded eyelid moving noticeably slower. “I offered him to join our forces some years back, but I almost forgot about it.”
            \n\nSeeing your surprised look, she scoffs, and confidently moves forward, increasing the pace. “In your place, I’d consider where you put your trust, stranger.”
            '
            '(glaucia1 set)':
                pass

label banditshideoutglaucia_about_vendetta_whitemarshesALL:
    label banditshideoutglaucia_about_vendetta_whitemarshes01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you target {color=#f6d6bd}White Marshes{/color}?”')
        menu:
            '“And why don’t you?” She turns just her head, giving you an annoyed glance. “What good is a roadwarden for if there are armies of awoken shells right under their nose?”
            '
            '“I can’t force an entire village to obey the laws of a faraway city.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t force an entire village to obey the laws of a faraway city.”')
                if (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    $ custom1 = "She looks away. “I’d rather see you stand on the side of righteousness, not {i}laws{/i}. These spells have been forbidden since the days before The Ten Cities, and the way the settlements are looking away, their... {i}laziness{/i},” her tone is full of disgust, “their seperation from all them rights written on our souls by The Wright... It lets the beasts devour the last shreds of what we, as humans, deserve.”\n\nShe ambles forward, without looking at you. “I have nothing to gain from telling you some stories. Fight for what’s right, or fall with all the others.”"
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01fail
                else:
                    $ custom1 = "She looks away. “I’d rather see you stand on the side of righteousness, not {i}laws{/i}. These spells have been forbidden since the days before The Ten Cities, and the way the settlements are looking away, their... {i}laziness{/i},” her tone is full of disgust, “their seperation from all them rights written on our souls by The Wright... It lets the beasts devour the last shreds of what we, as humans, deserve.”\n\nShe kicks away a piece of the roof that has fallen on the ground and, without stopping, turns full circle. Maybe it’s her stride that helps her maintain the angry tone, hiding any trace of melancholy."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01part2
            '“I’ll put the necromancers’ rule to an end, I just need to find a way.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll put the necromancers’ rule to an end, I just need to find a way.”')
                $ glaucia_friendship += 1
                if (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    $ custom1 = "Her emerald eyes pierce through your skull. “Good. Now let’s see if you have deeds to stand on, not words. For now, I have nothing to gain from telling you some stories. Fight for what’s right, or fall with all the others.” She spares you a nod and ambles forward."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01fail
                else:
                    $ custom1 = "Her emerald eyes pierce through your skull. “Good. Now let’s see if you have deeds to stand on, not words.”\n\nShe moves forward, and kicks away a piece of the roof that has fallen on the ground and, without stopping, turns full circle. Maybe it’s her stride that helps her maintain the angry tone, hiding any trace of melancholy."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01part2
            '“They aren’t hurting anyone, really.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They aren’t hurting anyone, really.”')
                if pc_religion == "pagan":
                    $ pc_faithpoints += 1
                elif pc_religion == "theunitedchurch":
                    $ pc_faithpoints -= 2
                elif pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ pc_faithpoints -= 1
                $ glaucia_friendship -= 1
                if (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    $ custom1 = "She stops in place, lowers her head for a moment, and once your eyes meet again, her disgust flows through your veins. “Lazy piece of shit, more proof of what cityfolk are good for. They take what’s not theirs, they put all our lives at risk. They build walls from our skulls, even if they are to collect them later.”\n\nShe ambles forward, without looking at you. “I have nothing to gain from telling you some stories. Fight for what’s right, or fall with all the others.”"
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01fail
                else:
                    $ custom1 = "She stops in place, lowers her head for a moment, and once your eyes meet again, her disgust flows through your veins. “Lazy piece of shit, more proof of what cityfolk are good for. They take what’s not theirs, they put all our lives at risk. They build walls from our skulls, even if they are to collect them later.”\n\nShe takes a long step away from you, kicks away a piece of the roof that has fallen on the ground, and, without stopping, turns full circle. Maybe it’s her stride that helps her maintain the angry tone, hiding any trace of melancholy."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01part2
            '“Let me understand the situation better so I can do something about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me understand the situation better so I can do something about it.”')
                if (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    $ custom1 = "The brow over her healthy eye furrows with her frown. “Are you that blind? There are necromancers in our land, what else is there to tell? These spells have been forbidden since the days before The Ten Cities, and the way the settlements are looking away, their... {i}laziness{/i},” her tone is full of disgust, “their seperation from all them rights written on our souls by The Wright... It lets the beasts devour the last shreds of what we, as humans, deserve.”\n\nShe ambles forward, without looking at you. “I have nothing to gain from telling you some stories. Fight for what’s right, or fall with all the others.”"
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01fail
                else:
                    $ custom1 = "The brow over her healthy eye furrows with her frown. “Are you that blind? There are necromancers in our land, what else is there to tell? These spells have been forbidden since the days before The Ten Cities, and the way the settlements are looking away, their... {i}laziness{/i},” her tone is full of disgust, “their seperation from all them rights written on our souls by The Wright... It lets the beasts devour the last shreds of what we, as humans, deserve.”\n\nShe kicks away a piece of the roof that has fallen on the ground and, without stopping, turns full circle. Maybe it’s her stride that helps her maintain the angry tone, hiding any trace of melancholy."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01part2

    label banditshideoutglaucia_about_vendetta_whitemarshes01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why did you target {color=#f6d6bd}White Marshes{/color}?”')
        menu:
            '“And why shouldn’t I?” She turns just her head, giving you an annoyed glance. “Would you rather have me observe their undead army grow?”
            '
            '“No other reason at all, huh?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No other reason at all, huh?”')
                if (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    $ custom1 = "She ambles forward, without looking at you. “I have nothing to gain from telling you some stories. You fought for what’s right. Don’t stop now.”"
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01fail
                else:
                    $ custom1 = "She ambles forward, without looking at you. “You fought for what’s right. And so did I.” A long pause."
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01part2

    label banditshideoutglaucia_about_vendetta_whitemarshes01fail:
        $ glaucia_about_vendetta_whitemarshes_gray = 1
        $ questionpreset = "glaucia1"
        menu:
            '[custom1]
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_vendetta_whitemarshes02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What did {color=#f6d6bd}White Marshes{/color} do to you?”')
        $ custom1 = "She kicks away a piece of the roof that has fallen on the ground and, without stopping, turns full circle. Maybe it’s her stride that helps her maintain the angry tone, hiding any trace of melancholy."
        jump banditshideoutglaucia_about_vendetta_whitemarshes01part2

    label banditshideoutglaucia_about_vendetta_whitemarshes01part2:
        $ glaucia_about_vendetta_whitemarshes = 1
        $ glaucia_questionstoday += 1
        $ ruinedvillage_name = "Steep House"
        $ minutes += 5
        if quest_intelforpeltnorth == 1 and quest_intelforpeltnorth_description08 and not quest_intelforpeltnorth_description10:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ quest_intelforpeltnorth_description10 = "I’ve learned that {color=#f6d6bd}Glaucia{/color} is trying to destroy the necromancers of {color=#f6d6bd}White Marshes{/color}. I should bring the news to the keeper."
        $ description_glaucia06 = "I’ve learned that she plans to take down the necromancers from {color=#f6d6bd}White Marshes{/color}, who have turned the deceased members of her family into undead."
        menu:
            '[custom1] “After the fall of {color=#f6d6bd}Steep House{/color}, I returned there a few days later, to torch any neighbor left behind by the scavengers. Me,” she glances at a few of her men, whose eyes are focused on the nearby grasses and nettles, “and a few others, who were hiding with me in a cave, with raw meat and bark in our stomachs, rags on our backs, and sharpened flints in our hands.”
            \n\nA rook tries to rest on a wooden post next to her, but as it struggles to stay upright, it rescues itself with a wing flap, then lands on {color=#f6d6bd}Glaucia’s{/color} shoulder, though only for a few heartbeats. Once she carries on, her words flow slowly, dim and flat.
            \n\n“We pushed the ashes aside, dug in the soft ground, even jumped into the stream, but there were no shells awaiting us. {i}Ghouls{/i}, we thought, {i}runners, or goblins{/i}. We traveled far those days, to warn our last few friends. {i}Awoken will strike{/i}, we told them, {i}make clubs, dig moats{/i}. And we waited, in this very hamlet, seeking them and preparing ourselves.”
            \n\n“A year went by, then another. We saw the first enslaved shells in {color=#f6d6bd}White Marshes{/color}. The deeds of {color=#f6d6bd}Orentius{/color}, the priest. We thought little of it, not the first sin of our lifetimes, until we realized. It wasn’t merely {i}their{/i} dead who they’d awoken,” her voice cracks, but she manages to keep her composure. “They had taken my husband, his parents, and many others. {i}Wagons{/i} of dead flesh.”
            \n\nYou spend a good minute in silence. “We’re but a band of workers. We can’t storm walls, or send an army of beasts to punish evil acts. But our work bears fruits, and we’ll find a way to get rid of the necromancers. Or to make their lives so dire they’ll leave their homes on their own.”
            '
            '“I’m sorry you faced such a hardship.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry you faced such a hardship.”')
                $ questionpreset = "glaucia1"
                menu:
                    'She adjusts a buckle on her boot, then reaches for a waterskin. “I don’t ask for pity,” she takes a sip. “Either cut off the rotting limb of the awoken, or shut your face.”
                    '
                    '(glaucia1 set)':
                        pass
            '“They will regret what they did to you, to everyone.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They will regret what they did to you, to everyone.”')
                $ glaucia_friendship += 1
                $ questionpreset = "glaucia1"
                menu:
                    '“Don’t make me laugh,” her tone is as somber as ever. “{i}Regret{/i} is good for a cook who took a bite out of another’s chicken, or a hunter who missed a shot. They’ll {i}pay{/i} for the decision they’ve made. I’ll listen to no excuses.” Without another word she reaches for a waterskin and moves forward.
                    '
                    '(glaucia1 set)':
                        pass
            'I walk in silence.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk in silence.')
                $ questionpreset = "glaucia1"
                menu:
                    'The air is heavy. She takes a sip from a waterskin, with her testimony weighing on her shoulders.
                    '
                    '(glaucia1 set)':
                        pass

label banditshideoutglauciaaboutsteephouseALL:
    label banditshideoutglaucia_about_steephouse101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the ruins at the southern road?”')
        $ glaucia_about_steephouse1 = 1
        $ questionpreset = "glaucia1"
        menu:
            'A long pause. “A lot. But there ain’t anything you can do about them.”
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_steephouse201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You were there when {color=#f6d6bd}Steep House{/color} fell, weren’t you?”')
        if (glaucia_friendship+appearance_charisma) < glaucia_about_steephouse2_friendshiplevel:
            $ questionpreset = "glaucia1"
            $ glaucia_about_steephouse2_gray = 1
            $ glaucia_about_steephouse1 = 1
            menu:
                'She stops and turns around. When she places a hand on her side the mail clinks. “I was, alright, but those memories are for me alone.” You look at each other in silence, then move forward.
                '
                '(glaucia1 set)':
                    pass
        else:
            $ glaucia_about_steephouse2 = 1
            $ glaucia_about_steephouse1 = 1
            label banditshideoutglaucia_about_steephouse203:
                $ glaucia_about_steephouse2 = 1
                $ glaucia_questionstoday += 1
                $ description_glaucia18 = "She’s a survivor of the massacre in {color=#f6d6bd}Steep House{/color}."
                menu:
                    'She stops and turns around. When she places a hand on her side, the mail clinks. “I saw it all, alright. {color=#f6d6bd}Thais’{/color} threats, the torches and bows of her people, the druids in clean robes with curses on their tongues. I helped the others add logs to our broken wall, but when the herds got in through the breach, all I could do was run. So I did.”
                    \n\nShe closes her eyes, but her wounded hand instantly moves to the scabbard of her blade, just in case. “I still remember two young men, no, boys, fighting each other by the flames of my house, and a head hitting a tree. My husband, screaming from pain in our bed, poisoned by the well, not knowing he would never fall asleep, nor wake up. And a werebear grasping my friend, then tearing her shell in half. I, and a few others, carry it all,” her absent eyes glance at one of her guards, a man with a face eaten by fire. “And will never forget.”
                    '
                    'I stare at her. “So... {color=#f6d6bd}Howler’s Dell{/color} was behind all this?”' if not ruinedvillage_truth:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare at her. “So... {color=#f6d6bd}Howler’s Dell{/color} was behind all this?”')
                        $ ruinedvillage_truth = 1
                        if not quest_ruins_description_truestory:
                            $ quest_ruins_description_truestory = "{color=#f6d6bd}Glaucia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                        $ quest_ruins_description_origins = "The village was located by the people of {color=#f6d6bd}Howler’s Dell{/color}, and was a part of their tribe."
                        $ quest_ruins_description_glauciasperspective = "{color=#f6d6bd}Glaucia{/color} claims that {color=#f6d6bd}Steep House{/color} was getting very rich because of its location, causing great anger in {color=#f6d6bd}Howler’s{/color}, which demanded a share of the village’s income - even though they were a part of the same tribe."
                        if not description_ruinedvillage02:
                            $ description_ruinedvillage02 = "{color=#f6d6bd}Glaucia{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to her story, {color=#f6d6bd}Thais{/color} tried to make an example out of the villagers when they refused to join her covenant."
                        if not description_thais06:
                            $ description_thais06 = "{color=#f6d6bd}Glaucia{/color} blames her for destroying the southern village."
                        $ renpy.notify("Journal updated: The Ruined Village")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                        menu:
                            '“The tribes have hidden this {i}little secret{/i} of ours quite well, I see,” she glances at you with a sad smirk. “Like you said. Ten years ago she offered every settlement to enter a covenant with her people. Taxes for her guards. We at {color=#f6d6bd}Steep House{/color} refused, and she decided to start a raid, like {i}a bandit{/i},” her voice swings from sadness to a bitter amusement.
                            \n\n“We surrendered, we did, but she wanted bloodshed, and she got it. Her people torched our houses, cut the forest garden, ended lives. We tried to recover, many said we should bow to her if it meant we could keep our home, but nature was merciless. The beasts attacked us soon after.”
                            \n\nShe falls quiet and puts her left boot on a nearby log, adjusting its buckles. “And that’s it. {color=#f6d6bd}Steep House{/color} was no more, killed by two different monsters.”
                            '
                            '“But why were the people of {color=#f6d6bd}Howler’s{/color} willing to go so far?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But why were the people of {color=#f6d6bd}Howler’s{/color} willing to go so far?”')
                                jump banditshideoutglaucia_about_steephouse204
                    '“I know {color=#f6d6bd}Thais{/color} was angry about the thing with the covenant... But why were the people of {color=#f6d6bd}Howler’s{/color} willing to do all this?”' if ruinedvillage_truth:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know {color=#f6d6bd}Thais{/color} was angry about the thing with the covenant... But why were the people of {color=#f6d6bd}Howler’s{/color} willing to do all this?”')
                        label banditshideoutglaucia_about_steephouse204:
                            $ glaucia_questionstoday += 1
                            $ quest_ruins_description_origins = "The village was located by the people of {color=#f6d6bd}Howler’s Dell{/color}, and was a part of their tribe."
                            $ quest_ruins_description_glauciasperspective = "{color=#f6d6bd}Glaucia{/color} claims that {color=#f6d6bd}Steep House{/color} was getting very rich because of its location, causing great anger in {color=#f6d6bd}Howler’s{/color}, which demanded a share of the village’s income - even though they were a part of the same tribe."
                            $ questionpreset = "glaucia1"
                            menu:
                                '“{i}They{/i} would say {i}we{/i} were asking for it. I spent not even fifteen years in {color=#f6d6bd}Steep House{/color}, but I saw my share of quarrels between the two villages. Did you know they were both the same tribe? It’s true,” she emphasizes, even though her eyes are focused on the roaming rooks. She must have told this story many times already. “{color=#f6d6bd}Howler’s{/color} started a fishing hamlet at the stream bank, and it sprouted into a new village.”
                                \n\n“In a few generations {color=#f6d6bd}Steep House{/color} grew strong enough to prosper without {color=#f6d6bd}Howler’s{/color} help, and decided to cut ties. We pretty much paid taxes, you see, and got little in return, chiefly since {i}we{/i} were placed closer to the hill pass, and many traders turned around soon after they entered our gates. My neighbors had riches, alright, good food and pretty homes,” she pauses, and you’re not sure if these words make her at all proud. “But respected their land, woods, and stream. The only greed we faced was that brought to us with violence.”
                                \n\nHer furious eyes look away and she strides forward.
                                '
                                '(glaucia1 set)':
                                    pass

    label banditshideoutglaucia_about_steephouse202:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me, {color=#f6d6bd}Glaucia{/color}. What did you see in {color=#f6d6bd}Steep House{/color}?”')
        jump banditshideoutglaucia_about_steephouse203

    label banditshideoutglauciaglaucia_about_steephouse301:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So now you aim your rage at {color=#f6d6bd}White Marshes{/color}... Is {color=#f6d6bd}Howler’s Dell{/color} next?”')
        $ description_glaucia17 = "Once the undead are gone, she will likely use her band to wound the people of {color=#f6d6bd}Howler’s Dell{/color}."
        $ glaucia_about_steephouse3 = 1
        $ questionpreset = "glaucia1"
        menu:
            'The smirk of her scarred lips sends shivers down your spine. “Maybe, maybe.”
            '
            '(glaucia1 set)':
                pass

label banditshideoutglaucia_about_highhisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard anything about {color=#f6d6bd}High Island{/color}?”')
    $ glaucia_about_highhisland = 1
    $ questionpreset = "glaucia1"
    if quest_runaway == 3 or quest_spyonwhitemarshes == 3 or quest_glauciasupport == 3 or quest_glauciasupport == 4: # or quest_spyonwhitemarshes == 4
        menu:
            '“You’re wasting my time, stranger. And not for the first time.”
            '
            '(glaucia1 set)':
                pass
    else:
        $ asterion_highisland_clues += 1
        if glaucia_about_asterion2:
            menu:
                '“Stop bothering me with this nonsense,” her response is as quick as a whip. “I ain’t got a reason to guide you around. If you want me to help you find {color=#f6d6bd}Asterion{/color}, be useful.”
                '
                '(glaucia1 set)':
                    pass
        else:
            menu:
                '“This again? Is that some lair of roadwardens?” Her response is as quick as a whip. “Don’t waste my time. If you want me to help you find {color=#f6d6bd}Asterion{/color}, be useful.”
                '
                '(glaucia1 set)':
                    pass

label glaucia_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}?”')
    $ quest_recruitahunter_spokento_glaucia = 1
    $ quest_recruitahunter_cassia_points += 1
    if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify2:
        $ quest_recruitahunter_cassia_points_notify2 = 1
        $ quest_recruitahunter_cassia_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    elif quest_recruitahunter_cassia_points >= 3 and not quest_recruitahunter_cassia_points_notify1:
        $ quest_recruitahunter_cassia_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    $ questionpreset = "glaucia1"
    menu:
        'She sends an angry look toward a surprised rook. “That good-for-nothing? Why, she’s offering you a job?” After you mention that you just try to learn more about her character, she walks in silence for a good minute. “Let’s merely say I’m not {i}convinced{/i} she’s capable of keeping her word, even though she promises a lot, and loudly so.”
        '
        '(glaucia1 set)':
            pass

label banditshideoutglauciaaboutasterionALL:
    label banditshideoutglaucia_about_asterion101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find out what happened to {color=#f6d6bd}Asterion{/color}.”')
        $ glaucia_about_asterion1 = 1
        if quest_runaway == 3 or quest_spyonwhitemarshes == 3 or quest_glauciasupport == 3 or quest_glauciasupport == 4:
            $ questionpreset = "glaucia1"
            menu:
                '“After you’ve proven that you’re not willing to do what I ask you for? You’re really testing my patience, stranger.”
                '
                '(glaucia1 set)':
                    pass
        # elif quest_spyonwhitemarshes == 4:
        #     $ questionpreset = "glaucia1"
        #     menu:
        #         '“After you’ve proven that you’re not willing to do what I ask you for? You’re really testing my patience, stranger.”
        #         '
        #         '(glaucia1 set)':
        #             pass
        else:
            menu:
                'She doesn’t spare you a glance. “So?”
                '
                '“There are... {i}some{/i} who are convinced that you had something to do with his disappearance.”' if description_glaucia11 and not glaucia_about_asterion2:
                    jump banditshideoutglaucia_about_asterion201
                '“Can you help me?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you help me?”')
                    $ questionpreset = "glaucia1"
                    menu:
                        '“Why would I?” She doesn’t wait for your answer. “I need nothing that you could fit in your saddles. Do me a few favors, and we’ll see.”
                        '
                        '(glaucia1 set)':
                            pass
                '“So tell me what you know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So tell me what you know.”')
                    $ questionpreset = "glaucia1"
                    menu:
                        'You hear an annoyed grunt. “Right, no. He and I shared a few goals, and if I was to tell you about {i}my{/i} plans, I would need to know it won’t stab me in the back.”
                        '
                        '(glaucia1 set)':
                            pass
                'I let out a loud sigh. “What do you want?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let out a loud sigh. “What do you want?”')
                    $ questionpreset = "glaucia1"
                    menu:
                        'You hear something between a grunt and a chuckle. “Scratch my back, I’ll scratch yours.”
                        '
                        '(glaucia1 set)':
                            pass

    label banditshideoutglaucia_about_asterion201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There are... {i}some{/i} who are convinced that you had something to do with {color=#f6d6bd}Asterion’s{/color} disappearance.”')
        $ glaucia_about_asterion2 = 1
        menu:
            'She stops in place and her heavy hand rests on your shoulder, pulling you down. You catch the weak scent of myrtle, a flower that grows in warmer lands and is often delivered by ships to {color=#f6d6bd}Hovlavan{/color}. A bit like a sour fruit, a bit like mint.
            \n\n“And who are those {i}some{/i}?” You notice that two of her front teeth are missing.
            '
            '“{color=#f6d6bd}Elah{/color} of {color=#f6d6bd}Creeks{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elah{/color} of {color=#f6d6bd}Creeks{/color}.”')
                $ glaucia_friendship += 1
                $ glaucia_questionstoday += 1
                $ questionpreset = "glaucia1"
                menu:
                    'She takes her hand off you and continues her walk. “I had something to discuss with him anyway. I’ll use the opportunity to make him remember the value of silence.”
                    '
                    '(glaucia1 set)':
                        pass
            'I just smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile.')
                $ questionpreset = "glaucia1"
                menu:
                    'She waits for a few more breaths, piercing through you with her emerald eyes, then pushes you away and continues her walk. “Let them talk. People will ascribe to me every misdeed or bad dream they have, but I had no roadwarden in my stew... yet.”
                    '
                    '(glaucia1 set)':
                        pass

    label banditshideoutglaucia_about_asterion401:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color} is dead.”')
        $ glaucia_about_asterion4 = 1
        $ glaucia_questionstoday += 1
        if glaucia_about_asterion3:
            $ minutes += 5
            $ glaucia_friendship += 1
            $ glaucia_friendship_tier += 1
            menu:
                'She turns around. “Did he reach {color=#f6d6bd}High Island{/color}? How did you find him?” After she makes sure that you keep your tale short, she puts her hands on her sides, observing her boots. “So there’s no {i}treasure{/i} left. Merely wasted effort, coins, and souls. I was wrong to trust him.”
                \n\nShe then meets your eyes, and the charming smile on her scarred lips would fit that of an old, caring aunt. “At least this time I was better at picking my allies.” She reaches out her hand.
                '
                'I accept.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I accept.')
                    $ questionpreset = "glaucia1"
                    $ glaucia_friendship += 1
                    $ glaucia_friendship_tier += 1
                    menu:
                        'Her broad fingers offer a strong squeeze, even without a thumb. The handshake is quick and firm.
                        \n\nAfter one more nod, she pulls you so that you stand side by side with her, moving forward as equals, though only so far as the narrow paths of the hamlet allow you to.
                        '
                        '(glaucia1 set)':
                            pass
                'I raise my eyebrow. “I decided you ought to know the truth, that’s all.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my eyebrow. “I decided you ought to know the truth, that’s all.”')
                    $ questionpreset = "glaucia1"
                    menu:
                        'Her hand returns on her side, and this time she raises her chin even higher, letting out dishonest laughter. “And now I know! Let’s not waste any more time.”
                        \n\nWithout another word, she continues her stroll, and her guards follow.
                        '
                        '(glaucia1 set)':
                            pass
        else:
            $ questionpreset = "glaucia1"
            menu:
                'She turns around. “At {color=#f6d6bd}High Island{/color}, I assume?” Seeing your slow nod, she looks at the rooks on the wall, and reaches to her heart, not noticing that she scratches only her mail. “He turned his back on all his allies, and ended up killed by his own cockiness.”
                \n\nYou try to describe how you have found him, but she is already continuing her stroll. “I don’t care.”
                '
                '(glaucia1 set)':
                    pass

    label banditshideoutglaucia_about_asterion301:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I did enough for you already. Help me find {color=#f6d6bd}Asterion{/color}.”')
        $ glaucia_about_asterion3 = 1
        $ asterion_highisland_knowsabout = 1
        $ asterion_highisland_clues += 5
        $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
        menu:
            '“And you’re still hoping he’s alive?” She turns around, sizing you up. “Alright then. I hope you washed your ears.”
            \n\nShe’s standing sideways to you, with a proudly raised chin and a hand on her side. “He was meant to bring me the treasure from {color=#f6d6bd}High Island{/color}, the largest scrap of land within range of a boat. It’s northwest from the coast, covered with a jungle. He’s gone, [pcname].”
            \n\nShe strides forward, as if there’s nothing else to say.
            '
            '“What {i}treasure{/i}?”' if not glaucia_about_asterion3_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What {i}treasure{/i}?”')
                $ glaucia_about_asterion3_bonusquestion1 = 1
                if not quest_reachthepaganvillage:
                    $ quest_reachthepaganvillage = 1
                    $ renpy.notify("New entry: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
                $ custom1 = "She takes a moment before speaking, her mail jangling loudly. “Dozens of blades, some enchanted, some not. Left behind by the smiths of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, long before we were born. They had refused to throw them into the sea, they did, and hid them in a cave, at the foot of the volcano.”"
                jump banditshideoutglaucia_about_asterion304
            '“What was your role in all of this?”' if glaucia_about_asterion3_bonusquestion1 and not glaucia_about_asterion3_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your role in all of this?”')
                $ glaucia_about_asterion3_bonusquestion2 = 1
                $ custom1 = "“Are you serious?” While you can’t see her face, her smirk alters her voice. “It would be a priceless find. I put him in touch with a few old friends of mine, gave him a few healing potions and a crossbow, helped him with a few tasks that were pinning him to the land. All for my fair half of what he would bring.” She glances at your boots. “But it was all for nothing. I can’t afford another bet like that.”"
                jump banditshideoutglaucia_about_asterion304
            '“How do I reach this island?”' if not glaucia_about_asterion3_bonusquestion3 and not highisland_howtoreach_pcknows:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do I reach this island?”')
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime, through a waterfall."
                $ glaucia_about_asterion3_bonusquestion3 = 1
                $ custom1 = "“Assuming you don’t have a ship? With a boat. But you need to get there with the night tide, and reach the cave hidden by a... waterfall on the eastern shore,” she speaks slowly, searching for lost memories. “But it’s an old tale. The villages are forbidden to land there, and there are no guides to that place.”"
                jump banditshideoutglaucia_about_asterion304
            '“I need to know more about that place.”' if not glaucia_about_asterion3_bonusquestion4 and highisland_howtoreach_pcknows:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to know more about that place.”')
                $ glaucia_about_asterion3_bonusquestion4 = 1
                $ custom1 = "“Do you, now,” she stops for a moment, crossing her armored arms. “Well, your {i}friend by trade{/i} kept me in the fog, told me he won’t let me get the treasure on my own. You know as much as I do.”"
                jump banditshideoutglaucia_about_asterion304
            '“But {i}why{/i} did he want to find it in the first place?”' if not glaucia_about_asterion3_bonusquestion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But {i}why{/i} did he want to find it in the first place?”')
                $ glaucia_about_asterion3_bonusquestion5 = 1
                $ description_asterion16 = "As far as I understand, he was obsessed with some sort of treasure."
                if pc_goal == "ineedmoney":
                    $ custom1 = "“Who can know for sure? He told me something about {i}a sick daughter{/i},” she says with mockery, “but he said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwantmoney":
                    $ custom1 = "“Who can know for sure? He told me he planned to save a fortune for the rest of his life, but he was one of those who always had a scheme on the side.” A short pause. “I wouldn’t trust a word of his.”"
                elif pc_goal == "iwanttoberemembered":
                    $ custom1 = "“Who can know for sure? He told me something about {i}changing the North{/i}, {i}healing the land{/i} and suchlike. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwanttohelp":
                    $ custom1 = "“Who can know for sure? He told me something about {i}helping people{/i} with these weapons, teaching them how to defend themselves, things like that. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwanttostartanewlife":
                    $ custom1 = "“Who can know for sure? He told me something about the sins of his past, people he needed to apologize to, bad blood to clean, all the usual nonsense. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwantstatus":
                    $ custom1 = "“Who can know for sure? He told me something about becoming a merchant, the city council, plans for better roads, I hardly listened. He said all that merely to get a better share, I ain’t trusting his talk.”"
                jump banditshideoutglaucia_about_asterion304
            '“That’s all.”' if glaucia_about_asterion3_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all.”')
                if not quest_asterion_description14:
                    $ quest_asterion_description14 = "{color=#f6d6bd}Glaucia{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to find a treasure left behind in a cave by {color=#f6d6bd}The Tribe of The Green Mountain{/color} on {color=#f6d6bd}High Island{/color}, at the foot of the volcano."
                    $ renpy.notify("Journal updated: Find the Roadwarden")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Journal updated: Find the Roadwarden')
                    $ questionpreset = "glaucia1"
                    menu:
                        '“I didn’t expect anyone to give a shit about this lad,” her steps are slower, hands on her back. “If you find him after all, hiding in the bushes with some {i}Spear of Immortality{/i}, I’d appreciate your tale. But even more so the spear,” she chuckles.
                        '
                        '(glaucia1 set)':
                            pass
                else:
                    jump banditshideoutglauciaafterinteraction01

    label banditshideoutglaucia_about_asterion302:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have more questions about {color=#f6d6bd}Asterion’s{/color} journey.”')
        $ custom1 = "She keeps walking, leaving you staring at the back of her head."
        jump banditshideoutglaucia_about_asterion304

    label banditshideoutglaucia_about_asterion304:
        menu:
            '[custom1]
            '
            '“What {i}treasure{/i}?”' if not glaucia_about_asterion3_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What {i}treasure{/i}?”')
                $ glaucia_about_asterion3_bonusquestion1 = 1
                if not quest_reachthepaganvillage:
                    $ quest_reachthepaganvillage = 1
                    $ renpy.notify("New entry: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
                $ custom1 = "She takes a moment before speaking, her mail jangling loudly. “Dozens of blades, some enchanted, some not. Left behind by the smiths of {color=#f6d6bd}The Tribe of The Green Mountain{/color}, long before we were born. They had refused to throw them into the sea, they did, and hid them in a cave, at the foot of the volcano.”"
                jump banditshideoutglaucia_about_asterion304
            '“What was your role in all of this?”' if glaucia_about_asterion3_bonusquestion1 and not glaucia_about_asterion3_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your role in all of this?”')
                $ glaucia_about_asterion3_bonusquestion2 = 1
                $ custom1 = "“Are you serious?” While you can’t see her face, her smirk alters her voice. “It would be a priceless find. I put him in touch with a few old friends of mine, gave him a few healing potions and a crossbow, helped him with a few tasks that were pinning him to the land. All for my fair half of what he would bring.” She glances at your boots. “But it was all for nothing. I can’t afford another bet like that.”"
                jump banditshideoutglaucia_about_asterion304
            '“How do I reach this island?”' if not glaucia_about_asterion3_bonusquestion3 and not highisland_howtoreach_pcknows:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do I reach this island?”')
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime, through a waterfall."
                $ glaucia_about_asterion3_bonusquestion3 = 1
                $ custom1 = "“Assuming you don’t have a ship? With a boat. But you need to get there with the night tide, and reach the cave hidden by a... waterfall on the eastern shore,” she speaks slowly, searching for lost memories. “But it’s an old tale. The villages are forbidden to land there, and there are no guides to that place.”"
                jump banditshideoutglaucia_about_asterion304
            '“I need to know more about that place.”' if not glaucia_about_asterion3_bonusquestion4 and highisland_howtoreach_pcknows:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to know more about that place.”')
                $ glaucia_about_asterion3_bonusquestion4 = 1
                $ custom1 = "“Do you, now,” she stops for a moment, crossing her armored arms. “Well, your {i}friend by trade{/i} kept me in the fog, told me he won’t let me get the treasure on my own. You know as much as I do.”"
                jump banditshideoutglaucia_about_asterion304
            '“But {i}why{/i} did he want to find it in the first place?”' if not glaucia_about_asterion3_bonusquestion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But {i}why{/i} did he want to find it in the first place?”')
                $ glaucia_about_asterion3_bonusquestion5 = 1
                $ description_asterion16 = "As far as I understand, he was obsessed with some sort of treasure."
                if pc_goal == "ineedmoney":
                    $ custom1 = "“Who can know for sure? He told me something about {i}a sick daughter{/i},” she says with mockery, “but he said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwantmoney":
                    $ custom1 = "“Who can know for sure? He told me he planned to save a fortune for the rest of his life, but he was one of those who always had a scheme on the side.” A short pause. “I wouldn’t trust a word of his.”"
                elif pc_goal == "iwanttoberemembered":
                    $ custom1 = "“Who can know for sure? He told me something about {i}changing the North{/i}, {i}healing the land{/i} and suchlike. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwanttohelp":
                    $ custom1 = "“Who can know for sure? He told me something about {i}helping people{/i} with these weapons, teaching them how to defend themselves, things like that. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwanttostartanewlife":
                    $ custom1 = "“Who can know for sure? He told me something about the sins of his past, people he needed to apologize to, bad blood to clean, all the usual nonsense. He said all that merely to get a better share, I ain’t trusting his talk.”"
                elif pc_goal == "iwantstatus":
                    $ custom1 = "“Who can know for sure? He told me something about becoming a merchant, the city council, plans for better roads, I hardly listened. He said all that merely to get a better share, I ain’t trusting his talk.”"
                jump banditshideoutglaucia_about_asterion304
            '“That’s all.”' if glaucia_about_asterion3_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all.”')
                if not quest_asterion_description14:
                    $ quest_asterion_description14 = "{color=#f6d6bd}Glaucia{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to find a treasure left behind in a cave by {color=#f6d6bd}The Tribe of The Green Mountain{/color} on {color=#f6d6bd}High Island{/color}, at the foot of the volcano."
                    $ renpy.notify("Journal updated: Find the Roadwarden")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Journal updated: Find the Roadwarden')
                    $ questionpreset = "glaucia1"
                    menu:
                        '“I didn’t expect anyone to give a shit about this lad,” her steps are slower, shoulders hunched. “If you find him after all, hiding in the bushes with some {i}Spear of Immortality{/i}, I’d appreciate your tale. But even more so the spear,” she chuckles.
                        '
                        '(glaucia1 set)':
                            pass
                else:
                    jump banditshideoutglauciaafterinteraction01

label banditshideoutglaucia_about_runawayALL:
    label banditshideoutglaucia_about_runaway01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need any assistance?”')
        $ glaucia_about_runaway = 1
        $ glaucia_questionstoday += 1
        menu:
            'She stops in place, then gestures at a soggy bench. Both of you sit down, but your eyes don’t meet - instead, you observe the dark birds that are pushing and pecking each other over old gruel spread among the nettles. “And why would a roadwarden want to help me?”
            '
            '“To avoid harm.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To avoid harm.”')
                $ custom1 = "She grunts. “You don’t need to do anything to {i}earn{/i} such a luxury. The opposite is true - don’t get in my way, and I won’t cut myself a steak out of your palfrey. Simple as that.”\n\nShe leans back and looks at the clouds. “But you can do some small things for me, and not for free. "
                jump banditshideoutglaucia_about_runaway02
            '“To be rewarded.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To be rewarded.”')
                $ custom1 = "She gives you a puzzled look, then nods. “So I’ve met two from your trade this year, and both of them are but mercenaries with a mount? I’d expect as much from the cityfolk. Alright. I’ll have a few things to offer you.”\n\nShe leans back and looks at the clouds. “"
                jump banditshideoutglaucia_about_runaway02
            '“So you can help me find {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found and not glaucia_about_asterion1 and not glaucia_about_asterion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you can help me find {color=#f6d6bd}Asterion{/color}.”')
                $ glaucia_about_asterion1 = 1
                $ custom1 = "She frowns. “Don’t you mean his dead shell? Very well. Do a few small tasks for me, and I’ll tell you all that I know. And I know {i}exactly{/i} where he went.”\n\nShe leans back and looks at the clouds. “But you won’t work for nothing, I have a few things to spare. "
                jump banditshideoutglaucia_about_runaway02
            'I smile. “We all need friends, don’t we?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “We all need friends, don’t we?”')
                $ custom1 = "She takes a few heartbeats to respond. “No. What I {i}have{/i} is a family.” She glances at the men who observe you from a distance. “And I trust them more than I would any stranger.”\n\nShe leans back and looks at the clouds. “But you can do some small things for me, and not for free. "
                jump banditshideoutglaucia_about_runaway02

    label banditshideoutglaucia_about_runaway02:
        $ quest_runaway = 1
        $ renpy.notify("New entry: The Runaway")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Runaway{/i}')
        menu:
            '[custom1]One of my lads has abandoned his post, and had taken something {i}very{/i} valuable to me. He wants to start his life anew, so he won’t use his name, but you’ll recognize him. Speaks like someone from my village, {i}he does{/i},” while her tone is sarcastic, her eyes remain serious. “Young, strong, with the pretty face and blue eyes of a beaten cub. Shaves often. The last tog he had on his back was our black gambeson, matching his short hair, but if he has any wits, he sold it somewhere already.”
            \n\nWhen she crosses one leg with the other, her mail clinks so loudly it makes you flinch. She reaches for her boot, adjusting it with her broad fingers. “He doesn’t want to be found, but he may need a roadwarden’s help. If so, merely tell me where he hides, and I will find him, alright.” She straightens up and rises to her feet, as if the conversation reached its conclusion. “I’ll drop you a few coins for trouble. Four, maybe? Or I can give you a handful of arrows for a crossbow, I don’t need them, really.”
            '
            '“What did he take from you?”' if not glaucia_about_runaway_bonusquestion6:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What did he take from you?”')
                $ glaucia_about_runaway_bonusquestion6 = 1
                $ custom1 = "“A small supply of black powder I was saving for a {i}special{/i} occasion, for one thing. I’d be ready to forgive him, but betraying my trust and taking our secrets outside is beyond excuses.”"
                jump banditshideoutglaucia_about_runaway04
            '“Why did he leave your band?”' if not glaucia_about_runaway_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why did he leave your band?”')
                $ glaucia_about_runaway_bonusquestion1 = 1
                $ custom1 = "She thinks about it for a few heartbeats. “He’s weak,” she states, but after seeing your frown, she puts hands behind her back. “He joined us not that long ago. He didn’t have any drive, was merely bored with his old life, but was good enough with his knives to impress me. Turns out he wasn’t ready for the change he took upon himself, and he left before he paid his debt to me.”"
                jump banditshideoutglaucia_about_runaway04
            '“What will you do with him once you find him?”' if glaucia_about_runaway_bonusquestion1 and not glaucia_about_runaway_bonusquestion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do with him once you find him?”')
                $ glaucia_about_runaway_bonusquestion4 = 1
                $ custom1 = "She frowns, narrowing her healthy eye, as if it’s too obvious to be worthy of an answer. “What he deserves.”"
                jump banditshideoutglaucia_about_runaway04
            '“You have nothing to gain in all this. You could just let him walk away.”' if glaucia_about_runaway_bonusquestion4 and not glaucia_about_runaway_bonusquestion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You have nothing to gain in all this. You could just let him walk away.”')
                $ glaucia_about_runaway_bonusquestion5 = 1
                $ custom1 = "She rests her hand on her weapon. “Stop trying to anger me, outsider. Whatever you think of me, I ain’t a hothead. When I draw my blade,” she pauses, rubbing the hilt with her finger. “I do so with conviction.”"
                jump banditshideoutglaucia_about_runaway04
            '“Any tips where to start?”' if not glaucia_about_runaway_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips where to start?”')
                $ glaucia_about_runaway_bonusquestion2 = 1
                $ custom1 = "“If I knew how to answer that, I’d have gone after him already. He was cautious, left our hunting group to take a leak, then sneaked away. The band assumed he got caught by a cat, but I told them to search our supplies. I doubt he took them for a walk, alright.”"
                jump banditshideoutglaucia_about_runaway04
            '“What if I can’t find him?”' if glaucia_about_runaway_bonusquestion2 and not glaucia_about_runaway_bonusquestion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if I can’t find him?”')
                $ glaucia_about_runaway_bonusquestion3 = 1
                $ custom1 = "“Why, he’s most likely dead already. Killing lone travelers is what the woods are best for. If you can’t find him, let me know. No answers, no pay, but also no hard feelings.”"
                jump banditshideoutglaucia_about_runaway04
            '“I think I saw him hiding in a cave, not so far away from here.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit and not shortcut_darkforest_bandit_talkedto:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I saw him hiding in a cave, not so far away from here.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him hiding in a cave, not so far away from here.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and not shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him hiding in a cave, not so far away from here.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him in a cave, not so far away from here, but he fled after I mentioned your name. Who knows where he is now.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him in a cave, not so far away from here, but he fled after I mentioned your name. Who knows where he is now.”')
                $ glaucia_friendship -= 1
                $ custom1 = "She turns toward you and puts hands on her sides. “So he’s alive, but can’t you hold your tongue? That moves me not an inch closer to him. Wasted effort.” She then continues her stroll. The sound of her heels and mail ruffles the nearby rooks."
                jump banditshideoutglaucia_about_runaway05halfsuccess
            '“I found him in a cave, not so far away from here, but he will soon leave to the cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_toldabouthuntercabin == day and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him in a cave, not so far away from here, but he will soon leave to the cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him. He should be in the old cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_toldabouthuntercabin < day and not shortcut_darkforest_bandit_huntercabin_firsttime and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him. He should be in the old cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“Last time I saw him, he was in the old cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_huntercabin_firsttime and not shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Last time I saw him, he was in the old cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“Last time I saw him, he was in {color=#f6d6bd}Pelt{/color}.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Last time I saw him, he was in {color=#f6d6bd}Pelt{/color}.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '(lie) “I found a shell in the woods that matches the description you gave me. Mauled to death by beasts.”' if shortcut_darkforest_furlesswolf:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I found a shell in the woods that matches the description you gave me. Mauled to death by beasts.”')
                $ custom1 = "“And you’re sure I won’t find him prowling around? It would make me {i}very{/i} angry, it would.” After you describe how she can still find his blood among the grasses east of the stone cairn, she scoffs. “That’s what happens when a wolf leaves its pack,” she turns away and continues her stroll. The sound of her heels and mail ruffles the nearby rooks."
                jump banditshideoutglaucia_about_runaway05halfsuccess
            '“He already left the peninsula.”' if shortcut_darkforest_bandit_leftthepeninsula:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He already left the peninsula.”')
                jump banditshideoutglaucia_about_runaway05doubt
            '“I don’t like this. I’m not going to help you.”' if not shortcut_darkforest_bandit_leftthepeninsula and glaucia_about_runaway_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like this. I’m not going to help you.”')
                jump banditshideoutglaucia_about_runaway05fail
            '“I’ll tell you once I learn anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you once I learn anything.”')
                jump banditshideoutglauciaafterinteraction01

    label banditshideoutglaucia_about_runaway03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the man you’re looking for...”')
        $ custom1 = "“What is it?”"
        jump banditshideoutglaucia_about_runaway04

    label banditshideoutglaucia_about_runaway04:
        menu:
            '[custom1]
            '
            '“What did he take from you?”' if not glaucia_about_runaway_bonusquestion6:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What did he take from you?”')
                $ glaucia_about_runaway_bonusquestion6 = 1
                $ custom1 = "“A small supply of black powder I was saving for a {i}special{/i} occasion, for one thing. I’d be ready to forgive him, but betraying my trust and taking our secrets outside is way beyond excuses.”"
                jump banditshideoutglaucia_about_runaway04
            '“Why did he leave your band?”' if not glaucia_about_runaway_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why did he leave your band?”')
                $ glaucia_about_runaway_bonusquestion1 = 1
                $ custom1 = "She thinks about it for a few heartbeats. “He’s weak,” she states, but after seeing your frown, she puts hands behind her back. “He joined us not that long ago. He didn’t have any drive, was merely bored with his old life, but was good enough with his knives to impress me. Turns out he wasn’t ready for the change he took upon himself, and he left before he paid his debt to me.”"
                jump banditshideoutglaucia_about_runaway04
            '“What will you do with him once you find him?”' if glaucia_about_runaway_bonusquestion1 and not glaucia_about_runaway_bonusquestion4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do with him once you find him?”')
                $ glaucia_about_runaway_bonusquestion4 = 1
                $ custom1 = "She frowns, narrowing her healthy eye, as if it’s too obvious to be worthy of an answer. “What he deserves.”"
                jump banditshideoutglaucia_about_runaway04
            '“You have nothing to gain in all this. You could just let him walk away.”' if glaucia_about_runaway_bonusquestion4 and not glaucia_about_runaway_bonusquestion5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You have nothing to gain in all this. You could just let him walk away.”')
                $ glaucia_about_runaway_bonusquestion5 = 1
                $ custom1 = "She rests her hand on her weapon. “Stop trying to anger me, outsider. Whatever you think of me, I ain’t a hothead. When I draw my blade,” she pauses, rubbing the hilt with her finger. “I do so with conviction.”"
                jump banditshideoutglaucia_about_runaway04
            '“Any tips where to start?”' if not glaucia_about_runaway_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips where to start?”')
                $ glaucia_about_runaway_bonusquestion2 = 1
                $ custom1 = "“If I knew how to answer that, I’d have gone after him already. He was cautious, left our hunting group to take a leak, then sneaked away. The band assumed he got caught by a cat, but I told them to search our supplies. I doubt he took them for a walk, alright.”"
                jump banditshideoutglaucia_about_runaway04
            '“What if I can’t find him?”' if glaucia_about_runaway_bonusquestion2 and not glaucia_about_runaway_bonusquestion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if I can’t find him?”')
                $ glaucia_about_runaway_bonusquestion3 = 1
                $ custom1 = "“Why, he’s most likely dead already. Killing lone travelers is what the woods are best for. If you can’t find him, let me know. No answers, no pay, but also no hard feelings.”"
                jump banditshideoutglaucia_about_runaway04
            '“I think I saw him hiding in a cave, not so far away from here.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit and not shortcut_darkforest_bandit_talkedto:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I saw him hiding in a cave, not so far away from here.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him hiding in a cave, not so far away from here.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and not shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him hiding in a cave, not so far away from here.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him in a cave, not so far away from here, but he fled after I mentioned your name. Who knows where he is now.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him in a cave, not so far away from here, but he fled after I mentioned your name. Who knows where he is now.”')
                $ glaucia_friendship -= 1
                $ custom1 = "She turns toward you and puts hands on her sides. “So he’s alive, but you can’t hold your tongue? That moves me not an inch closer to him. Wasted effort.” She then continues her stroll. The sound of her heels and mail ruffles the nearby rooks."
                jump banditshideoutglaucia_about_runaway05halfsuccess
            '“I found him in a cave, not so far away from here, but he will soon leave to the cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_toldabouthuntercabin == day and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him in a cave, not so far away from here, but he will soon leave to the cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“I found him. He should be in the old cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_talkedto and shortcut_darkforest_bandit_toldabouthuntercabin < day and not shortcut_darkforest_bandit_huntercabin_firsttime and not shortcut_darkforest_bandit_fled:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found him. He should be in the old cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“Last time I saw him, he was in the old cabin on the eastern path.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_huntercabin_firsttime and not shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Last time I saw him, he was in the old cabin on the eastern path.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '“Last time I saw him, he was in {color=#f6d6bd}Pelt{/color}.”' if not shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_leftthepeninsula and shortcut_darkforest_bandit_inpeltnorthpcknowsabout:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Last time I saw him, he was in {color=#f6d6bd}Pelt{/color}.”')
                jump banditshideoutglaucia_about_runaway05fullsuccess
            '(lie) “I found a shell in the woods that matches the description you gave me. Mauled to death by beasts.”' if shortcut_darkforest_furlesswolf:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I found a shell in the woods that matches the description you gave me. Mauled to death by beasts.”')
                $ custom1 = "“And you’re sure I won’t find him prowling around? It would make me {i}very{/i} angry, it would.” After you describe how she can still find his blood among the grasses east of the stone cairn, she scoffs. “That’s what happens when a wolf leaves its pack,” she turns away and continues her stroll. The sound of her heels and mail ruffles the nearby rooks."
                jump banditshideoutglaucia_about_runaway05halfsuccess
            '“He already left the peninsula.”' if shortcut_darkforest_bandit_leftthepeninsula:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He already left the peninsula.”')
                jump banditshideoutglaucia_about_runaway05doubt
            '“I don’t like this. I’m not going to help you.”' if not shortcut_darkforest_bandit_leftthepeninsula and glaucia_about_runaway_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like this. I’m not going to help you.”')
                jump banditshideoutglaucia_about_runaway05fail
            '“I’ll tell you once I learn anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you once I learn anything.”')
                jump banditshideoutglauciaafterinteraction01

    label banditshideoutglaucia_about_runaway05doubt:
        menu:
            'She gives you a long look. Her voice is chillingly quiet.
            \n\n“And did you have anything to do with his {i}departure{/i}?”
            '
            '(lie) “I just asked around. People have seen him.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I just asked around. People have seen him.”')
                $ custom1 = "“So, gone for good,” she turns away and continues her stroll. “I applaud his decision.” The sound of her heels and mail ruffles the nearby rooks."
                jump banditshideoutglaucia_about_runaway05halfsuccess
            '“I did.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I did.”')
                jump banditshideoutglaucia_about_runaway05fail

    label banditshideoutglaucia_about_runaway05fullsuccess:
        $ glaucia_friendship += 2
        $ glaucia_questionstoday += 1
        $ quest_runaway = 2
        $ shortcut_darkforest_bandit_killed = day
        menu:
            'She steps toward you and pats your shoulder, a bit too roughly. The smirk of her scarred lips is brief, but telling.
            \n\n“Alright. We may still have time to get to him. What do you want? Four coins, or six arrows?”
            '
            '“Quarrels are good.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Quarrels are good.”')
                $ item_crossbowquarrels += 6
                $ renpy.notify("Quest completed: The Runaway.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Runaway. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                $ quest_runaway_description01 = "I received my reward."
                $ questionpreset = "glaucia1"
                $ minutes += 5
                menu:
                    '“Don’t make us wait,” she orders a guard, who heads to the building’s entrance. For the next minute or two, you wander forward, and even after the boar-skin quiver is passed to you, {color=#f6d6bd}Glaucia{/color} says nothing. Her steps are light, and not as loud.
                    '
                    '(glaucia1 set)':
                        pass
            '“I’ll take the dragon bones.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take the dragon bones.”')
                show screen notifyimage( "Quest completed: The Runaway.\n+4", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Runaway. +4 {image=cointest}{/i}')
                $ coins += 4
                $ quest_runaway_description01 = "I received my reward."
                $ questionpreset = "glaucia1"
                $ minutes += 5
                menu:
                    '“Don’t make us wait,” she orders a guard, who heads to the building’s entrance. For the next minute or two, you wander forward, and even after the coins enter your hand, {color=#f6d6bd}Glaucia{/color} says nothing. Her steps are light, and not as loud.
                    '
                    '(glaucia1 set)':
                        pass

    label banditshideoutglaucia_about_runaway05halfsuccess:
        $ glaucia_friendship += 1
        $ glaucia_questionstoday += 1
        $ pc_lies += 1
        $ quest_runaway = 2
        $ quest_runaway_description02 = "I decided to lie to her, sacrificing my reward."
        $ renpy.notify("Quest completed: The Runaway")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Runaway{/i}')
        $ questionpreset = "glaucia1"
        menu:
            '[custom1]
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_runaway05fail:
        $ glaucia_friendship -= 3
        $ quest_runaway = 3
        $ renpy.notify("Quest completed: The Runaway")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Runaway{/i}')
        $ glaucia_annoyed = day
        $ can_items = 1
        menu:
            'Her fist flies toward your abdomen, but retracts before it lands - and before you manage to block it. “You’re a piece of shit, waste of air,” she steps away, turns around, and vaguely waves in your direction. Whatever message was intended, it causes her guards to approach you. “Don’t show up again before you have something of worth to say.”
            \n\nThe blunt edge of a guard’s spear pushes you toward {color=#f6d6bd}[horsename]{/color}.
            '
            'I climb into the saddle and travel back to the cairn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb into the saddle and travel back to the cairn.')
                $ travel_destination_shortcut = "cairn"
                $ pc_area = "shortcut-cairn"
                $ quarters += 1
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                nvl clear
                $ shortcut_pcknowsabout = 1
                if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                    play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
                stop nature fadeout 4.0
                jump cairn01

label banditshideoutglaucia_about_spyonnecromancers01ALL:
    label banditshideoutglaucia_about_spyonnecromancers01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What else do you want me to do?”')
        $ glaucia_about_spyonnecromancers = 1
        if whitemarshes_destroyed or orentius_banished or orentius_convinced:
            $ quest_spyonwhitemarshes = 2
            $ glaucia_friendship_tier += 1
            $ questionpreset = "glaucia1"
            menu:
                'She maintains her pace. “I was planning to ask you for help with the necromancers, but I guess we’re already over that. Didn’t expect to find a cityfolk ready to take such dire matters into their own hands, but I’ll take what I can get.”
                '
                '(glaucia1 set)':
                    pass
        elif whitemarshes_attacked:
            $ quest_spyonwhitemarshes = 3
            $ questionpreset = "glaucia1"
            menu:
                'She maintains her pace. “I was planning to ask you for help with the necromancers, but I doubt you’ll ever be let inside. I’ve no use for you, stranger.”
                '
                '(glaucia1 set)':
                    pass
        else:
            $ glaucia_questionstoday += 1
            $ quest_spyonwhitemarshes = 1
            $ renpy.notify("New entry: Spy on White Marshes")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Spy on White Marshes{/i}')
            $ quest_spyonwhitemarshes_description01 = "I was asked by {color=#f6d6bd}Glaucia{/color} to gather as much information as I can about the defenses of the village of {color=#f6d6bd}White Marshes{/color}."
            menu:
                'She gestures for you to sit down on a bench, though its age makes it look more like a rotten log. With hands on her sides, she looks across the hamlet. “This will be easier for you, though it will take you into a fetid place. Those cowards from {color=#f6d6bd}White Marshes{/color} won’t let us in, not that I blame them. But they may welcome you, if you have any charm at all.”
                \n\nStaring in your eyes, she speaks slowly, as if she’s giving orders to a child. “Get there, through the bogs spread by the western road, and look around. Count the awoken, or see which side of the village is poorly guarded. What weapons they have, and what they’re made of.” She sits down next to you, and her arm burdens your shoulders. She pulls you closer to her, and you lean down. The delightful scent of myrtle doesn’t make you any more comfortable. “I don’t care about your trade. I need you as a spy, [pcname]. Someone who can shut their lips when they speak to my enemies.”
                \n\nShe springs up, her mail jangling. “I’ll have a small pouch ready for your return. Or two healing potions, always useful,” she sizes you up, “to a traveler.”
                '
                '“Why do you target {color=#f6d6bd}White Marshes{/color}?”' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and not glaucia_about_vendetta_whitemarshes and not glaucia_about_vendetta_whitemarshes_gray:
                    jump banditshideoutglaucia_about_vendetta_whitemarshes01
                '“What did {color=#f6d6bd}White Marshes{/color} do to you?”' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) >= glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    jump banditshideoutglaucia_about_vendetta_whitemarshes02
                'She’s not willing to tell me the truth about White Marshes. (disabled)' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                    pass
                '“Any advice on how I can get on the locals’ good side?”' if not glaucia_about_spyonnecromancers_bonusquestion1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any advice on how I can get on the locals’ good side?”')
                    $ glaucia_about_spyonnecromancers_bonusquestion1 = 1
                    $ description_whitemarshes13 = "According to {color=#f6d6bd}Glaucia{/color}, they are a harsh tribe that “will listen only to the strong and the gritty.”"
                    $ description_thyrsus03 = "According to {color=#f6d6bd}Glaucia{/color}, he has “a soul as firm as a shield. No threat nor begging will move him an inch.”"
                    $ whitemarshes_opposition += 1
                    $ description_thyrsus05 = "He seems to be bothered by the undead of {color=#f6d6bd}White Marshes{/color}."
                    $ custom1 = "She rests her hands on her knees, looking ahead in silence. “Right... They’re a harsh tribe, with hardship and hungry years behind them. They will listen only to the strong and the gritty, unless...” She once again hesitates, and carries on as if she’s surprised to hear her own voice. “Not all of them {i}agree{/i} with their necromancer, {color=#f6d6bd}Orentius{/color}. Their warlock, {color=#f6d6bd}Thyrsus{/color}, lives in the peat field, divided with his people, with a soul as firm as a shield. No threat nor begging will move him an inch.”"
                    jump banditshideoutglaucia_about_spyonnecromancers03
                '“I can’t enter {color=#f6d6bd}White Marshes{/color} anymore. I can’t help you.”' if whitemarshes_attacked and not whitemarshes_spying_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t enter {color=#f6d6bd}White Marshes{/color} anymore. I can’t help you.”')
                    jump banditshideoutglaucia_about_spyonnecromancers04ban
                '“I’ve a lot to say.”' if whitemarshes_spying_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a lot to say.”')
                    jump banditshideoutglaucia_about_spyonnecromancers04fullsuccess
                '“You’re asking for too much. It would be wrong to do this.”' if not whitemarshes_attacked or (whitemarshes_spying_completed and whitemarshes_attacked):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for too much. It would be wrong to do this.”')
                    jump banditshideoutglaucia_about_spyonnecromancers04fail
                '“I’ll get it done.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll get it done.”')
                    jump banditshideoutglauciaafterinteraction01

    label banditshideoutglaucia_about_spyonnecromancers02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the spying you wanted me to do...”')
        $ custom1 = "“What did you see?”"
        jump banditshideoutglaucia_about_spyonnecromancers03

    label banditshideoutglaucia_about_spyonnecromancers03:
        menu:
            '[custom1]
            '
            '“Why do you target {color=#f6d6bd}White Marshes{/color}?”' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and not glaucia_about_vendetta_whitemarshes and not glaucia_about_vendetta_whitemarshes_gray:
                jump banditshideoutglaucia_about_vendetta_whitemarshes01
            '“What did {color=#f6d6bd}White Marshes{/color} do to you?”' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) >= glaucia_about_vendetta_whitemarshes_friendshiplevel:
                jump banditshideoutglaucia_about_vendetta_whitemarshes02
            'She’s not willing to tell me the truth about White Marshes. (disabled)' if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime and glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                pass
            '“Any advice on how I can get on the locals’ good side?”' if not glaucia_about_spyonnecromancers_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any advice on how I can get on the locals’ good side?”')
                $ glaucia_about_spyonnecromancers_bonusquestion1 = 1
                $ description_whitemarshes13 = "According to {color=#f6d6bd}Glaucia{/color}, they are a harsh tribe that “will listen only to the strong and the gritty.”"
                $ description_thyrsus03 = "According to {color=#f6d6bd}Glaucia{/color}, he has “a soul as firm as a shield. No threat nor begging will move him an inch.”"
                $ whitemarshes_opposition += 1
                $ description_thyrsus05 = "He seems to be bothered by the undead of {color=#f6d6bd}White Marshes{/color}."
                $ custom1 = "She rests her hands on her knees, looking ahead in silence. “Right... They’re a harsh tribe, with hardship and hungry years behind them. They will listen only to the strong and the gritty, unless...” She once again hesitates, and carries on as if she’s surprised to hear her own voice. “Not all of them {i}agree{/i} with their necromancer, {color=#f6d6bd}Orentius{/color}. Their warlock, {color=#f6d6bd}Thyrsus{/color}, lives in the peat field, divided with his people, with a soul as firm as a shield. No threat nor begging will move him an inch.”"
                jump banditshideoutglaucia_about_spyonnecromancers03
            '“I can’t enter {color=#f6d6bd}White Marshes{/color} anymore. I can’t help you.”' if whitemarshes_attacked and not whitemarshes_spying_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t enter {color=#f6d6bd}White Marshes{/color} anymore. I can’t help you.”')
                jump banditshideoutglaucia_about_spyonnecromancers04ban
            '“I’ve a lot to say.”' if whitemarshes_spying_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a lot to say.”')
                jump banditshideoutglaucia_about_spyonnecromancers04fullsuccess
            '“You’re asking for too much. It would be wrong to do this.”' if not whitemarshes_attacked or (whitemarshes_spying_completed and whitemarshes_attacked):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for too much. It would be wrong to do this.”')
                jump banditshideoutglaucia_about_spyonnecromancers04fail
            '“I’ll get it done.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll get it done.”')
                jump banditshideoutglauciaafterinteraction01

    label banditshideoutglaucia_about_spyonnecromancers04ban:
        $ glaucia_friendship -= 1
        $ quest_spyonwhitemarshes = 3
        $ renpy.notify("Quest completed: Spy on White Marshes")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
        $ quest_spyonwhitemarshes_description04 = "I couldn’t finish the job."
        $ questionpreset = "glaucia1"
        menu:
            'She looks at you in silence, then continues with her walk among the nettles.
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_spyonnecromancers04fullsuccess:
        $ glaucia_friendship += 3
        $ glaucia_friendship_tier += 1
        $ quarters += 1
        menu:
            'She nods for you to follow her outside the gate, then to the pond bridge, but since it turns out to be occupied by a few orange frogs - each one as long as your forearm - you instead enter the woodlands behind the palisade. Her guards are nearby.
            '
            'I try to stay calm, thinking about the dagger in my boot.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to stay calm, thinking about the dagger in my boot.')
                $ custom1 = "With every passing minute, you glance more and more often toward the gate, thinking you may never see your mount again, nor all the belongings you’ve gathered in the bundles on its back.\n\nYou speak quickly, describing the walls and dwellers of {color=#f6d6bd}White Marshes{/color}, as well as the grounds surrounding the village. The questions don’t stop, why are there so many of them? After a few good minutes, you are told to get back to the hamlet. You’re breathing heavily, ready to run - yet there’s a short man in your way. Should you stab him, or just push him aside...?\n\n“I said {i}you did well{/i},” {color=#f6d6bd}Glaucia’s{/color} voice brings you back. “What do you want? Twelve coins, or two healing potions?”"
                jump banditshideoutglaucia_about_spyonnecromancers04fullsuccess02
            'Nah, she wouldn’t hurt me. I’m too valuable to her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Nah, she wouldn’t hurt me. I’m too valuable to her.')
                $ custom1 = "The saunter is slow. You describe the walls and dwellers of {color=#f6d6bd}White Marshes{/color}, as well as the grounds surrounding the village, and every question you receive is straight-forward and brief. After a few good minutes, you walk back to the hamlet. No one pushes you, or even steps close enough to make you worry.\n\n“You did well, you did. So, what do you want? Twelve coins, or two healing potions?”"
                jump banditshideoutglaucia_about_spyonnecromancers04fullsuccess02

        label banditshideoutglaucia_about_spyonnecromancers04fullsuccess02:
            menu:
                '[custom1]
                '
                '“Potions, obviously.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Potions, obviously.”')
                    $ quest_spyonwhitemarshes_description02 = "I received my reward."
                    $ quest_spyonwhitemarshes = 2
                    $ renpy.notify("Quest completed: Spy on White Marshes.\nYou received two healing potions.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. You received two healing potions.{/i}')
                    $ item_generichealingpotion += 2
                    $ quest_runaway_description01 = "I received my reward."
                    $ questionpreset = "glaucia1"
                    menu:
                        'She glances at one of the guards. He stalks toward you and hands you a small box engraved with the shapes of leaves, but after you put it under your arm, he clears his throat. “I need it,” he grouses, and you take out the fragile, earthenware bottles, returning the box to him. {color=#f6d6bd}Glaucia{/color} ignores the commotion. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                        '
                        '(glaucia1 set)':
                            pass
                '“Dragons are always useful.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Dragons are always useful.”')
                    $ quest_spyonwhitemarshes_description02 = "I received my reward."
                    $ quest_spyonwhitemarshes = 2
                    show screen notifyimage( "Quest completed: Spy on White Marshes.\n+12", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes. +12 {image=cointest}{/i}')
                    $ coins += 12
                    $ quest_runaway_description01 = "I received my reward."
                    $ questionpreset = "glaucia1"
                    menu:
                        'She glances at one of the guards. He throws you a small pouch, and you toss it upward a few times. Should be enough.
                        \n\n{color=#f6d6bd}Glaucia{/color}, making enough noise of her own, ignores the rattling of the coins. “I now have to plan my next steps. Maybe I’ll have something more for you in autumn. I have big plans for it.” Her wide grin alters her voice.
                        '
                        '(glaucia1 set)':
                            pass

    label banditshideoutglaucia_about_spyonnecromancers04fail:
        $ glaucia_friendship -= 3
        $ quest_spyonwhitemarshes = 3
        $ renpy.notify("Quest completed: Spy on White Marshes")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
        $ quest_spyonwhitemarshes_description03 = "I rejected her offer... Though she wasn’t happy about it."
        $ glaucia_annoyed = day
        $ can_items = 1
        menu:
            'Her fist flies toward your abdomen, but retracts before it lands - and before you manage to block it. “And you carried such a promise. You’re a piece of shit, waste of air,” she steps away, turns around, and vaguely waves in your direction. Her guards approach you. “Don’t show up again before you have something of worth to say.”
            \n\nThe blunt edge of a guard’s spear pushes you toward {color=#f6d6bd}[horsename]{/color}.
            '
            'I climb into the saddle and travel back to the cairn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb into the saddle and travel back to the cairn.')
                $ travel_destination_shortcut = "cairn"
                $ pc_area = "shortcut-cairn"
                $ quarters += 1
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                nvl clear
                $ shortcut_pcknowsabout = 1
                if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                    play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
                stop nature fadeout 4.0
                jump cairn01

label banditshideoutglaucia_about_voteALL:
    label banditshideoutglaucia_about_vote01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The council of {color=#f6d6bd}Gale Rocks{/color} is planning to hold a meeting about cutting ties with your band.”')
        $ glaucia_about_vote = 1
        $ glaucia_questionstoday += 1
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        if cleanliness_clothes_blood:
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        else:
            $ cleanliness_clothes_blood = 1
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        menu:
            'She freezes, then dashes toward you, pushing you against the wall. Your cheek scratches against the moldy logs, and you try to move your hands, but to no avail - the guards emerge out of thin air, holding you from both sides. {color=#f6d6bd}Glaucia’s{/color} dagger and fingers are at your neck, and you try to hold your breath.
            \n\n“They’re {i}planning{/i}, are they,” she gasps, “and not at all because of you? I don’t know what you told them,” the blade cuts through your skin, and the warm, dense blood leaks down the front of your gambeson, “but you’re going to fix it.”
            \n\nYou’re on the ground, held by her massive boot. “That’s why you’re here, ain’t you? To hear {i}my{/i}, offer. Too slimy to do something out of your own conviction.”
            \n\nShe takes her leg off you, and you can breathe again. “Show me you heard me. {i}You’re going to fix this{/i},” she drawls.
            '
            'I nod, waiting for her to step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod, waiting for her to step away.')
                $ custom1 = "She answers your gesture with a brief smile. “Then listen. "
                jump banditshideoutglaucia_about_vote02
            'Without a word, I try to get up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a word, I try to get up.')
                $ custom1 = "A kick into your jaw sends you back on the ground. You hiss, but no one stops you from touching your face - you rub it, hoping it will ease the pain. “I have your attention now,” {color=#f6d6bd}Glaucia{/color} announces. “"
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                jump banditshideoutglaucia_about_vote02

    label banditshideoutglaucia_about_vote02:
        $ quest_glauciasupport = 1
        $ renpy.notify("New entry: The Support of Bandits")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Bandits{/i}')
        $ glaucia_annoyed = day
        $ can_items = 1
        if glaucia_about_asterion1 and not asterion_found and not glaucia_about_asterion3 and quest_runaway != 3 and quest_spyonwhitemarshes != 3 and quest_glauciasupport != 3:
            if quest_spyonwhitemarshes == 2:
                $ custom2 = "And if you’re still interested in finding {color=#f6d6bd}Asterion{/color},” she turns toward you, with hands on her sides, “I’ll tell you where you’ll find him.”"
                $ quest_glauciasupport_description00 = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but will help me learn more about the peninsula."
            else:
                $ custom2 = "And if you’re still interested in finding {color=#f6d6bd}Asterion{/color},” she turns toward you, with hands on her sides, “do some more work for me, and I’ll tell you where you’ll find him.”"
                $ quest_glauciasupport_description00 = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but will help me learn more about the peninsula."
        else:
            $ custom2 = "But most importantly,” she turns toward you, with hands on her sides, “I’ll let you live.”"
            $ quest_glauciasupport_description00alt = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but would keep me safer in the future seasons... If I care for it."
        menu:
            '[custom1]Take part in this meeting, say a thing or two, merely don’t be {i}too{/i} convincing. Let them conclude it was a bad idea in the first place, but not that you wasted their time.”
            \n\nThe loud call of a rook makes her turn away from you, and it returns her stare with its beak parted in surprise. “Play nice, and I’ll play with you. If you plan to stay in this peninsula for the next few seasons or so, I’ll be ready to make some concessions for your sake, as well as share our future earnings with you. [custom2]
            \n\nHer eyes size you up, yet you notice that her look is absent. Soon after, she heads to the shelter’s entrance loudly. “Scat, outsider. And don’t fuck this up.” The door closes behind her, but the guards remain close to you, with little patience in their gaze.
            '
            'Speaking to no one, I ride south.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Speaking to no one, I ride south.')
                $ travel_destination_shortcut = "cairn"
                $ pc_area = "shortcut-cairn"
                $ quarters += 1
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                nvl clear
                $ shortcut_pcknowsabout = 1
                if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                    play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
                stop nature fadeout 4.0
                jump cairn01

        ### BACKUP - should sickle sword be a reward?
        # if glaucia_about_asterion1 and not asterion_found and not glaucia_about_asterion3 and quest_runaway != 3 and quest_spyonwhitemarshes != 3 and quest_glauciasupport != 3:
        #     if quest_spyonwhitemarshes == 2:
        #         $ custom2 = "“And if you’re still interested in finding {color=#f6d6bd}Asterion{/color},” she turns toward you, with hands on her sides, “I’ll tell you where you’ll find him.”"
        #         $ quest_glauciasupport_description00 = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but will help me learn more about the peninsula, and I’ll receive a handy sickle sword."
        #     else:
        #         $ custom2 = "“And if you’re still interested in finding {color=#f6d6bd}Asterion{/color},” she turns toward you, with hands on her sides, “do some more work for me, and I’ll tell you where you’ll find him.”"
        #         $ quest_glauciasupport_description00 = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but will help me learn more about the peninsula, and I’ll receive a handy sickle sword."
        # else:
        #     $ custom2 = "“But most importantly,” she turns toward you, with hands on her sides, “I’ll let you live.”"
        #     $ quest_glauciasupport_description00alt = "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but would keep me safer in the future seasons... If I care for it. I’ll also receive a handy sickle sword."
        # menu:
        #     '[custom1]Take part in this meeting, say a thing or two, just don’t be {i}too{/i} convincing. Let them conclude it was a bad idea in the first place, but not that you wasted their time.”
        #     \n\nThe loud call of a rook makes her turn away from you, and it returns her stare with its beak parted in surprise. “Play nice, and I’ll play with you. If you plan to stay in this peninsula for the next few seasons or so, I’ll be ready to make some concessions for your sake, as well as share our earnings with you. Starting with this,” she pats her sheated sickle sword, by itself worth twenty dragon bones, if not more. [custom2]
        #     \n\nHer eyes size you up, yet you notice that her look is absent. Soon after, she heads to the shelter’s entrance loudly. “Scat, outsider. And don’t fuck this up.” The door closes behind her, but the guards remain close to you, with little patience in their gaze.
        #     '

label banditshideoutglaucia_about_galerocksdecisionALL:
    label banditshideoutglaucia_about_galerocksdecision01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The council has come to a decision.”')
        $ glaucia_about_galerocksdecision = 1
        $ glaucia_questionstoday += 1
        menu:
            'You keep moving forward, but her steps are heavier, and the guards move closer to you, no longer leaning against the palisade.
            '
            '“I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”' if quest_galerockssupport == 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”')
                $ glaucia_friendship += 5
                $ quest_glauciasupport_description01 = "I told her about my success, and she was grateful - in her own way."
                $ custom1 = "She turns toward you and pats your elbow. “Well done. You had me worried there for a moment, but I guess my position in the village is now stronger than it has been in a long time. I’ll pay them a visit soon, and I’ll return your favor, one way or the other. Let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02
            '“I didn’t do a good job as a speaker, but still, they decided to support you, for now.”' if quest_galerockssupport == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t do a good job as a speaker, but still, they decided to support you, for now.”')
                $ glaucia_friendship += 2
                $ quest_glauciasupport_description01 = "I told her about my success, and she was grateful - in her own way."
                $ custom1 = "She turns toward you, lets out a sigh, but then waves it off and continues her walk. “I’ll pay them a visit soon, maybe it will fix your mess. For now, let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02
            '(lie) “I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”' if quest_galerockssupport == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”')
                $ glaucia_friendship += 5
                $ pc_lies += 1
                $ quest_glauciasupport_description01 = "I told her about my success, and she was grateful - in her own way."
                $ custom1 = "She turns toward you and pats your elbow. “Well done. You had me worried there for a moment, but I guess my position in the village is now stronger than it has been in a long time. I’ll pay them a visit soon, and I’ll return your favor, one way or the other. Let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02
            '“From now on, don’t count on the help of the people of {color=#f6d6bd}Gale Rocks{/color}. You are advised to disband.”' if quest_galerockssupport == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “From now on, don’t count on the help of the people of {color=#f6d6bd}Gale Rocks{/color}. You are advised to disband.”')
                $ quest_glauciasupport_description03 = "I told her the truth, and she was far from happy."
                jump banditshideoutglaucia_about_galerocksdecision03
            '(lie) “I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”' if quest_galerockssupport == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I was quite convincing, but they plan to stay on their path. You have nothing to worry about.”')
                $ glaucia_friendship += 5
                $ pc_lies += 4
                $ glaucia_about_galerocksdecision_liedto += 1
                $ quest_glauciasupport_description02 = "I lied to her. Let’s hope she won’t learn the truth while I’m around."
                $ custom1 = "She turns toward you and pats your elbow. “Well done. You had me worried there for a moment, but I guess my position in the village is now stronger than it has been in a long time. I’ll pay them a visit soon, and I’ll return your favor, one way or the other. Let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02

    label banditshideoutglaucia_about_galerocksdecision02:
        $ quest_glauciasupport = 2
        $ glaucia_friendship_tier += 1
        if pc_goal == "iwantstatus":
            $ pc_goal_iwantstatuspoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwantstatus" and not glaucia_about_galerocksdecision_liedto:
            $ renpy.notify("Quest completed: The Support of Bandits,\nJournal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Bandits, Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ renpy.notify("Quest completed: The Support of Bandits")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Bandits{/i}')
        $ questionpreset = "glaucia1"
        menu:
            '[custom1]
            '
            '(glaucia1 set)':
                pass

    label banditshideoutglaucia_about_galerocksdecision03:
        $ quest_glauciasupport = 3
        $ renpy.notify("Quest completed: The Support of Bandits")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Bandits{/i}')
        if glaucia_friendship+appearance_charisma >= 8:
            $ glaucia_friendship -= 5
            menu:
                'She raises her eyes and puts on a glove. “Brave of you to bring me the news in person, I appreciate that,” she clenches her fist a few times, then glances at the other woman from her band... then at you again, and lets out a sigh. “I should kill you, outsider. You lowered my guard, and now I’m further away from my goal than I was last spring.”
                \n\nShe steps closer, looks at the palm of her four-fingered hand, now covered with leather, and after a few heartbeats, turns around. “Don’t ever get in our way again. I’ll break your neck on sight.”
                '
                '“Farewell, {color=#f6d6bd}Glaucia{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell, {color=#f6d6bd}Glaucia{/color}.”')
                    $ banditshideout_banned = 1
                    $ glaucia_annoyed = day
                    if quest_runaway == 1:
                        $ quest_runaway = 3
                        $ renpy.notify("Quest completed: The Runaway")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Runaway{/i}')
                    if quest_spyonwhitemarshes == 1:
                        $ quest_spyonwhitemarshes = 3
                        $ renpy.notify("Quest completed: Spy on White Marshes")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Spy on White Marshes{/i}')
                        $ quest_spyonwhitemarshes_description04 = "I couldn’t finish the job."
                    $ can_items = 0
                    menu:
                        '“Fuck off,” she growls. Her heavy steps, accompanied by the constant sound of her heels and mail, follow her to the pond.
                        \n\nOne of her men grabs the collar of your gambeson, pushing you toward the gate.
                        '
                        'I approach {color=#f6d6bd}[horsename]{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}%s{/color}.' %horsename)
                            $ travel_destination_shortcut = "cairn"
                            $ pc_area = "shortcut-cairn"
                            $ quarters += 1
                            $ can_leave = 0
                            $ can_rest = 0
                            $ can_items = 0
                            nvl clear
                            $ shortcut_pcknowsabout = 1
                            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                                play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
                            stop nature fadeout 4.0
                            jump cairn01
                '“You can still hide your blade. Go see {color=#f6d6bd}your parents{/color}. They’re sick, but they miss you. Your tribe would be stronger with you.”' if description_glaucia13:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can still hide your blade. Go see {color=#f6d6bd}your parents{/color}. They’re sick, but they miss you. Your tribe would be stronger with you.”')
                    $ glaucia_about_returningtoparents = 1
                    if glaucia_about_necklace == 2:
                        $ glaucia_willreturntogalerocks = 1
                        $ pc_goal_iwanttohelppoints += 1
                    $ questionpreset = "glaucia1"
                    menu:
                        'You’re met with silence, then her hands go behind her back. “You ain’t merely walking on the edge of my patience, you’re {i}dancing{/i} on it. Can’t you see that my work needs me? That I already went too far?”
                        \n\nYou try to find some supportive words, maybe a quote from an ancient song, but she once again meets your eyes. Her voice cracks. “What else do you want from me, [pcname]?”
                        '
                        '(glaucia1 set)':
                            pass
        else:
            $ banditshideout_banned = 1
            $ glaucia_annoyed = day
            $ glaucia_friendship = -10
            if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
                play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
            menu:
                'She raises her eyes, then, with a sigh, puts on a glove. “Brave of you to bring me the news in person, I appreciate that,” she clenches her fist a few times, then glances at the other woman from her band. “Let’s get to work.”
                \n\nSomething hard hits the back of your head, you land on your knees, then your face hits the ground. Your hand touches the nettle leaves.
                '
                'I order them to let me go.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I order them to let me go.')
                    jump banditshideoutglaucia_about_galerocksdecision03post
                'I try to kick them away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to kick them away.')
                    jump banditshideoutglaucia_about_galerocksdecision03post
                'I beg for her forgiveness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I beg for her forgiveness.')
                    jump banditshideoutglaucia_about_galerocksdecision03post

        label banditshideoutglaucia_about_galerocksdecision03post:
            $ travel_destination_shortcut = "cairn"
            $ pc_area = "shortcut-cairn"
            $ glaucia_woundedpc = 1
            $ quarters += 1
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            nvl clear
            $ shortcut_pcknowsabout = 1
            stop nature fadeout 4.0
            jump cairn01

    label banditshideoutglaucia_about_galerocksdecision01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The council of {color=#f6d6bd}Gale Rocks{/color} held a meeting about cutting ties with your band.”')
        $ glaucia_about_galerocksdecision = 1
        $ glaucia_questionstoday += 1
        $ minutes += 5
        menu:
            'She freezes, then looks at you with a puzzled frown creasing her healthy eye. “A {i}meeting{/i}? What are you talking about?”
            \n\nYou summarize the situation, and she looks at her boots, with hands on her sides. “You’re treading on shaky ground if you think I can’t connect this whole thing to your recent arrival. You’re {i}responsible{/i} for what’s going on.” She meets your eyes, and the fury you find in her look makes you step back. “So, why are you here? To beg for my forgiveness, or to bring the good news?”
            '
            '“They decided to support you, for now.”' if quest_galerockssupport == 3 or quest_galerockssupport == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They decided to support you, for now.”')
                $ glaucia_friendship += 2
                $ quest_glauciasupport_description01 = "I told her about my success, and she was grateful - in her own way."
                $ custom1 = "She turns toward you, lets out a sigh, but then waves it off and continues her walk. “I’ll pay them a visit soon, maybe it will fix your mess. Let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02
            '“From now on, don’t count on the help of the people of {color=#f6d6bd}Gale Rocks{/color}. You are advised to disband.”' if quest_galerockssupport == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “From now on, don’t count on the help of the people of {color=#f6d6bd}Gale Rocks{/color}. You are advised to disband.”')
                $ quest_glauciasupport_description03 = "I told her the truth, and she was far from happy."
                jump banditshideoutglaucia_about_galerocksdecision03
            '(lie) “They decided to support you, for now.”' if quest_galerockssupport == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “They decided to support you, for now.”')
                $ glaucia_friendship += 2
                $ pc_lies += 4
                $ glaucia_about_galerocksdecision_liedto += 1
                $ quest_glauciasupport_description02 = "I lied to her. Let’s hope she won’t learn the truth while I’m around."
                $ custom1 = "She turns toward you, lets out a sigh, but then waves it off and continues her walk. “I’ll pay them a visit soon, maybe it will fix your mess. Let’s forget the whole thing.”"
                jump banditshideoutglaucia_about_galerocksdecision02
