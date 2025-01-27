default orentius_met = 0
default orentius_attitude = 0
default orentius_friendship = 0

default whitemarshes_attacked = 0
default whitemarshes_destroyed = 0
default whitemarshes_nomoreundead = 0 # day
default whitemarshes_nomoreundeadfirstsleepdescription = 0
default orentius_banished = 0
default orentius_spared = 0
default orentius_convinced = 0

default whitemarshes_attack_companion_bandits = 0
default whitemarshes_attack_companion_galerocks = 0
default whitemarshes_attack_companion_pelt = 0

default whitemarshes_attack_plan = 0 # "banish" # "convince" # "whateverittakes"

default whitemarshes_attack_numberofallies = 0
default whitemarshes_attack_glauciaattackedpc = 0
default whitemarshes_attack_glauciahelpedescape = 0
default whitemarshes_attack_glauciakilledorentius = 0
default whitemarshes_attack_glauciathreatened = 0
default whitemarshes_attack_numberofdead = 0

default whitemarshes_attack_question1 = 0
default whitemarshes_attack_question2 = 0
default whitemarshes_attack_question3 = 0
default whitemarshes_attack_question4 = 0
default whitemarshes_attack_question5 = 0
default whitemarshes_attack_question6 = 0
default whitemarshes_attack_question7 = 0
default whitemarshes_attack_question8 = 0
default whitemarshes_attack_question9 = 0

default orentius_dagger = 0

default orentius_arguments = 0
default orentius_arguments_needed = 6

default orentius_argument_undeadaredangerous = 0
default orentius_argument_aeliaboutundead = 0
default orentius_argument_eudocia_about_whitemarshes = 0
default orentius_argument_notjusttheirowndead = 0
default orentius_argument_fickleness = 0
default orentius_argument_orthodoxy = 0
default orentius_argument_trust = 0
default orentius_argument_caius = 0
default orentius_argument_sleepingritual = 0
default orentius_argument_empathy = 0
default orentius_argument_empathy_appearancepoints = 0

default orentius_argument_locals = 0
default orentius_argument_locals_helviusiscruel = 0
default orentius_argument_locals_helviusbreaksrules = 0
default orentius_argument_locals_trytoleave = 0
default orentius_argument_locals_thyrsusisoutsider = 0
default orentius_argument_locals_hunger = 0

label whitemarshes_attackedALL:
    label whitemarshes_attacked01:
        $ orentius_dagger = 1
        $ whitemarshes_attacked = 1
        $ whitemarshes_attack_numberofallies = 0
        if quest_orentius_thais_description03a01 and not peltnorth_ban_perm:
            $ whitemarshes_attack_numberofallies += 1
            $ whitemarshes_attack_companion_pelt = 1
        if quest_orentius_thais_description03a06:
            $ whitemarshes_attack_numberofallies += 1
            $ whitemarshes_attack_companion_galerocks = 1
        if quest_orentius_thais_description03a07 and not banditshideout_banned:
            $ whitemarshes_attack_numberofallies += 1
            $ whitemarshes_attack_companion_bandits = 1
        $ quarters = (world_daylength-4)
        show areapicture howlersdellfull at basicfade
        hide howlersdellsquareutensils
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/weloveindies_petrified_tenseloop.ogg":
            play music "<loop 8.0>audio/weloveindies_petrified_tenseloop.ogg" fadeout 1.0 fadein 3.0
        if helvius_about_oldtunnel_paid and helvius_about_oldtunnel_paid > day:
            $ helvius_about_oldtunnel_paid = 0
        with Fade(1.8, 1.5, 1.8, color="#0f2a3f")
        if quest_hiddenpurse == 1 and quest_readtheletter == 1:
            $ quest_hiddenpurse = 3
            $ quest_readtheletter = 3
            $ renpy.notify("Quests completed: A Hidden Pouch, Read the Letter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: A Hidden Pouch, Read the Letter{/i}')
        elif quest_hiddenpurse == 1:
            $ quest_hiddenpurse = 3
            $ renpy.notify("Quests completed: A Hidden Pouch")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: A Hidden Pouch{/i}')
        elif quest_readtheletter == 1:
            $ quest_readtheletter = 3
            $ renpy.notify("Quest completed: Read the Letter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Read the Letter{/i}')
        menu:
            'You observe the preparations. Twelve village guards, assisted by many more, inspect the straps and cords of their gambesons and the sharpness of their blades. A few of them were planning to take rations of food and water, but are now being told to leave them behind. “Whoever’s ne returning tonight,” grunts a man with a short reflex bow as he tests the strings, “is ne coming back at all.”
            \n\nThere’s quite a commotion, despite the cooling dusk air. Families and friends don’t spare best wishes and words of wisdom. Two brothers are crying as they embrace, while a spearwoman in her thirties promises her sons she’ll be with them when they wake up.
            \n\nFinally, the last group of fighters arrives at the village, and you head to the gate, ready to discuss the plan with your allies in the weak light of the lanterns. {color=#f6d6bd}Thais{/color} shows off her dress, powders, and rouges, with her deer-shaped buckle glimmering at the edge of darkness. When she speaks, others listen, when she makes a joke, they politely join her chuckle. People half her age look away in embarrassment when she catches them glancing at her elegantly spread hair, red lips, and revealed neck.
            '
            'I look at the hunters from {color=#f6d6bd}Pelt{/color}. “I see that {color=#f6d6bd}[dalit_name]{/color} isn’t with you.”' if whitemarshes_attack_companion_pelt and not whitemarshes_attack_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the hunters from {color=#f6d6bd}Pelt{/color}. “I see that {color=#f6d6bd}%s{/color} isn’t with you.”' %dalit_name)
                $ whitemarshes_attack_question1 = 1
                $ custom1 = "There’s six of them, but only five will join you - the last one got sick soon after he got stung by a bee, just outside the southern gate. “She wasn’t happy about this trip,” explains the bald man with wide nostrils. “But we ain’t going hunting anyway, we’ll do.”\n\nUnlike the locals, they look like a band of mercenaries. Each one of them has unique equipment made by various artisans from different materials. Their jackets are darker and thinner, more suitable for crawling in the woods, while their weapons are heavier and simpler, aside from the crossbows. They were meant to pierce animals, not gambesons."
                jump whitemarshes_attacked01a
            'I nod at the guards from {color=#f6d6bd}Gale Rocks{/color}. “Who’s going to lead your group?”' if whitemarshes_attack_companion_galerocks and not whitemarshes_attack_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at the guards from {color=#f6d6bd}Gale Rocks{/color}. “Who’s going to lead your group?”')
                $ whitemarshes_attack_question2 = 1
                if galerocks_tatius_firsttime:
                    $ custom1 = "The muscular man raises his hand, points at his chest with his thumb, then shrugs his shoulders. It takes you a moment before you recognize him - {color=#f6d6bd}Tatius{/color}, the instructor and armorer, looks strange when fully clothed. “I’m the one who’s going to be yelled at if anything goes wrong, alright, but I ain’t looking to be a hero. Once you tell us what to do, we’ll do it.”\n\nThe nine people who assist him are grouped a few steps away, eating dried fruits and paying little attention to the gathering. While they all carry similar equipment, looking like a proper squad of soldiers with shields, heavy jackets, and axes, the thin, long limbs of the seafolk and the unusual height of the locals make them look timid, especially since they’re already marked by the tiring journey."
                else:
                    $ custom1 = "The muscular man raises his hand, points at his chest with his thumb, then shrugs his shoulders. “I’m {color=#f6d6bd}Tatius{/color}, the one who’s going to be yelled at if anything goes wrong, alright, but I ain’t looking to be a hero. Once you tell us what to do, we’ll do it.”\n\nThe nine people who assist him are grouped a few steps away, eating dried fruits and paying little attention to the gathering. While they all carry similar equipment, looking like a proper squad of soldiers with shields, heavy jackets, and axes, the thin, long limbs of the seafolk and the unusual height of the locals make them look timid, especially since they’re already marked by the tiring journey."
                jump whitemarshes_attacked01a
            'I turn toward {color=#f6d6bd}Glaucia{/color}. “You seem more than ready.”' if whitemarshes_attack_companion_bandits and not whitemarshes_attack_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward {color=#f6d6bd}Glaucia{/color}. “You seem more than ready.”')
                $ whitemarshes_attack_question3 = 1
                $ custom1 = "One wouldn’t guess her trade just by looking at her. She smiles politely, looking around nervously and keeping her hands behind her back, like a tavern guard on their first evening, but her expensive armor makes her look like a foreign diplomat. Hearing your words, she raises her healthy eyebrow. “If I were younger, I’d already have grabbed your hood and be pulling you through the bogs. Let’s get this over with.”\n\nMost members of her band are right behind her, with the remaining three looking after the hideout. Their poor equipment is even more evident - some of them don’t have any armor, or carry simple, blunt weapons that don’t require much training. Yet they chat loudly with the rest of the gathering, describing enthusiastically what they’re going to do if any of “them awoken” try to stop them."
                jump whitemarshes_attacked01a
            '“Let’s get to it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get to it.”')
                jump whitemarshes_attacked02

    label whitemarshes_attacked01a:
        menu:
            '[custom1]
            '
            'I look at the hunters from {color=#f6d6bd}Pelt{/color}. “I see that {color=#f6d6bd}[dalit_name]{/color} isn’t with you.”' if whitemarshes_attack_companion_pelt and not whitemarshes_attack_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the hunters from {color=#f6d6bd}Pelt{/color}. “I see that {color=#f6d6bd}%s{/color} isn’t with you.”' %dalit_name)
                $ whitemarshes_attack_question1 = 1
                $ custom1 = "There’s six of them, but only five will join you - the last one got sick soon after he got stung by a bee, just outside the southern gate. “She wasn’t happy about this trip,” explains the bald man with wide nostrils. “But we ain’t going hunting anyway, we’ll do.”\n\nUnlike the locals, they look like a band of mercenaries. Each one of them has unique equipment made by various artisans from different materials. Their jackets are darker and thinner, more suitable for crawling in the woods, while their weapons are heavier and simpler, aside from the crossbows. They were meant to pierce animals, not gambesons."
                jump whitemarshes_attacked01a
            'I nod at the guards from {color=#f6d6bd}Gale Rocks{/color}. “Who’s going to lead your group?”' if whitemarshes_attack_companion_galerocks and not whitemarshes_attack_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at the guards from {color=#f6d6bd}Gale Rocks{/color}. “Who’s going to lead your group?”')
                $ whitemarshes_attack_question2 = 1
                if galerocks_tatius_firsttime:
                    $ custom1 = "The muscular man raises his hand, points at his chest with his thumb, then shrugs his shoulders. It takes you a moment before you recognize him - {color=#f6d6bd}Tatius{/color}, the instructor and armorer, looks strange when fully clothed. “I’m the one who’s going to be yelled at if anything goes wrong, alright, but I ain’t looking to be a hero. Once you tell us what to do, we’ll do it.”\n\nThe nine people who assist him are grouped a few steps away, eating dried fruits and paying little attention to the gathering. While they all carry similar equipment, looking like a proper squad of soldiers with shields, heavy jackets, and axes, the thin, long limbs of the seafolk and the unusual height of the locals make them look timid, especially since they’re already marked by the tiring journey."
                else:
                    $ custom1 = "The muscular man raises his hand, points at his chest with his thumb, then shrugs his shoulders. “I’m {color=#f6d6bd}Tatius{/color}, the one who’s going to be yelled at if anything goes wrong, alright, but I ain’t looking to be a hero. Once you tell us what to do, we’ll do it.”\n\nThe nine people who assist him are grouped a few steps away, eating dried fruits and paying little attention to the gathering. While they all carry similar equipment, looking like a proper squad of soldiers with shields, heavy jackets, and axes, the thin, long limbs of the seafolk and the unusual height of the locals make them look timid, especially since they’re already marked by the tiring journey."
                jump whitemarshes_attacked01a
            'I turn toward {color=#f6d6bd}Glaucia{/color}. “You seem more than ready.”' if whitemarshes_attack_companion_bandits and not whitemarshes_attack_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward {color=#f6d6bd}Glaucia{/color}. “You seem more than ready.”')
                $ whitemarshes_attack_question3 = 1
                $ custom1 = "One wouldn’t guess her trade just by looking at her. She smiles politely, looking around nervously and keeping her hands behind her back, like a tavern guard on their first evening, but her expensive armor makes her look like a foreign diplomat. Hearing your words, she raises her healthy eyebrow. “If I were younger, I’d already have grabbed your hood and be pulling you through the bogs. Let’s get this over with.”\n\nMost members of her band are right behind her, with the remaining three looking after the hideout. Their poor equipment is even more evident - some of them don’t have any armor, or carry simple, blunt weapons that don’t require much training. Yet they chat loudly with the rest of the gathering, describing enthusiastically what they’re going to do if any of “them awoken” try to stop them."
                jump whitemarshes_attacked01a
            '“Let’s get to it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get to it.”')
                jump whitemarshes_attacked02

    label whitemarshes_attacked02:
        if whitemarshes_attack_companion_pelt:
            $ custom1 = "A huntress clicks her tongue. “And what then? Do we...” She makes a neck-breaking gesture."
        else:
            $ custom1 = "Someone then clears his throat. “But what exactly do we want to get from that priest? Are we supposed to kill him?”"
        if whitemarshes_attack_companion_galerocks:
            $ custom2 = "“Not a laudable maneuver,” {color=#f6d6bd}Tatius{/color} from {color=#f6d6bd}Gale Rocks{/color} sighs, “but if it works, we’ll get what we want without bloodshed.”"
        else:
            $ custom2 = "“At least we won’t risk much that way,” adds one of her guards."
        menu:
            '“Very well,” {color=#f6d6bd}Thais{/color} clasps her hands on the stomach, and continues to use her cityfolk accent. “I’ve already spoken with [pcname] about the village’s defenses, and I recommend a simple deception,” she looks at you with an encouraging smile. “In the cover of darkness, you’ll beg at the gates for help, horseless and {i}wounded{/i}. Once they open,” she raises her palm, moving it slowly from right to left, vaguely gesturing at everyone around, “the others, who by that time will have been hidden beneath the wall with dark cloaks on their backs, will get to their feet and charge inside. Catch as many hostages as you can, and force the others to let you meet with {color=#f6d6bd}Orentius{/color}.”
            \n\n[custom2]
            \n\n[custom1]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess it’ll be the last time I’m ever let into that village.”')
        $ whitemarshes_attack_question4 = 1
        if whitemarshes_attack_companion_bandits:
            $ custom3 = "“More likely, it’s the last time they won’t shoot you the moment they see you,” {color=#f6d6bd}Glaucia{/color} rests her hands on her sides. “But so what? A roadwarden shouldn’t hang out with necromancers anyway.”"
        else:
            $ custom3 = "“I wouldn’t be so sure,” {color=#f6d6bd}Thais{/color} sighs. “Maybe for a few years, but sooner or later they must open their eyes. We’re doing the right thing.”"
        menu:
            '[custom3]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hostages?”')
        $ whitemarshes_attack_question5 = 1
        if whitemarshes_attack_companion_galerocks:
            $ custom2 = "The guards from {color=#f6d6bd}Gale Rocks{/color} scowl at her and share telling looks, but say nothing. “I’ve nothing better to propose, I don’t,” admits {color=#f6d6bd}Tatius{/color}."
        else:
            $ custom2 = "No one seems eager to argue with her."
        menu:
            '“The gate watch would be a start, but you’d do better getting into the nearest houses,” {color=#f6d6bd}Thais{/color} speaks gently, as if she’s a shepherd planning the future of her flock. “Catch a few foragers, or maybe some kids? They won’t throw themselves at you, and you won’t need to hurt them.”
            \n\n[custom2]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02c:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If they abandon the hostages and start a fight... Can we handle them?”')
        $ whitemarshes_attack_question6 = 1
        if whitemarshes_attack_companion_bandits:
            $ custom3 = "“The living, sure,” says a bandit. “But when pressured, they may send the awoken against us.” One of the {color=#f6d6bd}Howler’s{/color} guards nods in agreement. “Let’s hope no one will suffer tonight.”"
        else:
            $ custom3 = "After a long pause, one of the {color=#f6d6bd}Howler’s{/color} guards speaks up. “We’ve numbers to fight the armed folks, but we don’t know how far they can be pushed before they release the undead from their leash. Let’s avoid stepping too far, if possible.”"
        menu:
            '[custom3]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02d:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if they don’t let me in?”')
        $ whitemarshes_attack_question7 = 1
        if whitemarshes_attack_companion_bandits:
            $ custom3 = "“We turn back, alright,” {color=#f6d6bd}Glaucia{/color} looks around, and seeing that {color=#f6d6bd}the mayor{/color} nods in agreement, she carries on. “If they notice our approach, they’ll win. We can’t storm a village full of undead.”"
        else:
            $ custom3 = "“Then it means they know what’s going on, and you have to flee,” {color=#f6d6bd}the mayor{/color} meets your eyes. “Don’t storm the walls, or they’ll use the undead to fight you. Everything will be lost.”"
        menu:
            '[custom3]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02e:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We won’t have much time.”')
        $ whitemarshes_attack_question8 = 1
        if whitemarshes_attack_companion_pelt:
            $ custom1 = "“We’ll have enough, if we don’t hesitate,” says a hunter. “We can’t keep an eye on all of them, and given enough time, they’ll regroup. We have to follow the first hit, to the very end.”"
        else:
            $ custom1 = "“Tha’s why we can ne change our plans once we get there,” responds a guard. “Whatever the plan, we have to go with it, without second thoughts.”"
        menu:
            '[custom1]
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked02f:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”')
        $ whitemarshes_attack_question9 = 1
        menu:
            '“Tha’s why I’m coming,” says one of {color=#f6d6bd}Thais’{/color} men, “as I often go out with hunters. Our cloaks will be darker than the night, our steps will ne awake a mouse.”
            \n\nHis voice is calm, even bored. You give him another look. His gambeson is thinner and shorter than of the regular fighters, and he’s only equipped with a spear and a club. It takes a few moments before you recognize his bearded, but young face - you saw him a few times by the village square, always dressed in the long robe of a druid.
            '
            '“We won’t have much time.”' if not whitemarshes_attack_question8:
                jump whitemarshes_attacked02e
            '“What if they don’t let me in?”' if not whitemarshes_attack_question7:
                jump whitemarshes_attacked02d
            '“I guess it’ll be the last time I’m ever let into that village.”' if not whitemarshes_attack_question4:
                jump whitemarshes_attacked02a
            '“Hostages?”' if not whitemarshes_attack_question5:
                jump whitemarshes_attacked02b
            '“If they abandon the hostages and start a fight... Can we handle them?”' if whitemarshes_attack_question5 and not whitemarshes_attack_question6:
                jump whitemarshes_attacked02c
            '“Won’t the night watch see us sneaking up to the wall? We’re putting a lot of trust in luck.”' if not whitemarshes_attack_question9:
                jump whitemarshes_attacked02f
            '“Here’s what we’re going to do next...”':
                jump whitemarshes_attacked03

    label whitemarshes_attacked03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here’s what we’re going to do next...”')
        menu:
            'The gathering falls quiet. There will be no coming back from this.
            '
            '“We need to avoid risk. We’ll demand that the villagers hand {color=#f6d6bd}Orentius{/color} over. No disputes - or we’ll threaten to kidnap the hostages. Then, we’ll take him away, so he can’t turn back to necromancy.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We need to avoid risk. We’ll demand that the villagers hand {color=#f6d6bd}Orentius{/color} over. No disputes - or we’ll threaten to kidnap the hostages. Then, we’ll take him away, so he can’t turn back to necromancy.”')
                $ whitemarshes_attack_plan = "banish"
                $ thais_friendship += 1
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = "\n\n“We could take him south, to the valley,” says a hunter from {color=#f6d6bd}Pelt{/color}. “But it may be safer to just, you know, {i}send him into the woods{/i},” he gives the others telling looks, but {color=#f6d6bd}the mayor{/color} says it’s going to be a problem for later."
                else:
                    $ custom1 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ custom2 = "\n\n“It’s still quite a hit, if they already rely on the undead so strongly,” {color=#f6d6bd}Tatius{/color} looks at his guards, who give you distrustful scowls. “I won’t blame them if they decide to lock their gates for good after that.”"
                else:
                    $ custom2 = ""
                if whitemarshes_attack_companion_bandits:
                    $ custom3 = "\n\n“I’d rather see him dead, make him pay for what he’s done,” {color=#f6d6bd}Glaucia{/color} lets out an excessive sigh, but then nods in agreement. “But if this increases the chance we’ll all wake up tomorrow, I’ll follow.”"
                else:
                    $ custom3 = ""
                menu:
                    '{color=#f6d6bd}Thais{/color} breaks the silence with her titter, then rests a hand on your shoulder. “I was about to propose the very same thing. Get in, make your demands, and get out, before anyone rebels. Any objections,” she looks at the others, but her tone carries no hint of an actual question.[custom3][custom2][custom1]
                    '
                    'I raise my voice. “All you have to do is follow my lead. Let’s get to it!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my voice. “All you have to do is follow my lead. Let’s get to it!”')
                        jump whitemarshes_attacked04
                    'I look down. “Just remember, we’re not trying to start a war. We go there as rescuers, not robbers.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look down. “Just remember, we’re not trying to start a war. We go there as rescuers, not robbers.”')
                        jump whitemarshes_attacked04
                    'I smile. “Treat {color=#f6d6bd}[horsename]{/color} well while I’m away.”' if pc_likeshorsename:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Treat {color=#f6d6bd}%s{/color} well while I’m away.”' %horsename)
                        jump whitemarshes_attacked04
                    'I take a deep breath and head toward the gate, ready to go.' if not pc_likeshorsename:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and head toward the gate, ready to go.')
                        jump whitemarshes_attacked04
            '“I’ll meet with {color=#f6d6bd}Orentius{/color} and use what I’ve learned during my journeys to open his eyes. Having him give up on necromancy will convince his followers, and may save the bridge between them and the rest of the peninsula.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll meet with {color=#f6d6bd}Orentius{/color} and use what I’ve learned during my journeys to open his eyes. Having him give up on necromancy will convince his followers, and may save the bridge between them and the rest of the peninsula.”')
                menu:
                    '{color=#f6d6bd}Thais{/color} gives you a puzzled look. “The more time you spend in the village, the more opportunities you’ll give the locals to regroup. And what if he won’t listen to you? Once you lose the advantage, you’ll no longer be able to take him by force.”
                    '
                    '“If I fail, I fail. I’d rather take this chance than see {color=#f6d6bd}White Marshes{/color} sunk in blood.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If I fail, I fail. I’d rather take this chance than see {color=#f6d6bd}White Marshes{/color} sunk in blood.”')
                        $ whitemarshes_attack_plan = "convince"
                        $ thais_friendship -= 1
                        if whitemarshes_attack_companion_pelt:
                            $ custom1 = "\n\n“The more villages and traders there are, the safer the roads,” says one of the hunters from {color=#f6d6bd}Pelt{/color}. “Allowing them to remain strong would make our boss happy. I’m...” He looks behind, and his companions nod in agreement. “We’re in.”"
                        else:
                            $ custom1 = ""
                        if whitemarshes_attack_companion_galerocks:
                            $ galerocks_reputation += 1
                            $ custom2 = "\n\n“Sounds alright to me,” {color=#f6d6bd}Tatius{/color} glances at his guards, who look at you kindly. “If wounding the village may kill it, I’d rather not touch it at all.”"
                        else:
                            $ custom2 = ""
                        if whitemarshes_attack_companion_bandits:
                            $ glaucia_friendship -= 1
                            $ custom3 = "\n\nAfter a longer pause, {color=#f6d6bd}Glaucia{/color} starts to wander around the gathering. “I’ve no pity for the necromancers, I don’t,” her voice is cold, and her slow pace gives it an added confidence. “You want to have a chat with them, do so, outsider. But don’t think I’m going to scat empty-handed. We’re here to make the issue disappear, not poke it.” She returns to her original spot, and puts her hands on her sides. Her eyes leave you no doubt - she won’t take {i}no{/i} for an answer."
                        else:
                            $ custom3 = ""
                        menu:
                            'Her voice grows harsh. “If you fail, {i}our{/i} efforts will be wasted on your whim. I really hope you judge your talents well, [pcname].”[custom2][custom1][custom3]
                            '
                            '“Don’t worry, {color=#f6d6bd}Glaucia{/color}. I know what I’m doing.”' if whitemarshes_attack_companion_bandits:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry, {color=#f6d6bd}Glaucia{/color}. I know what I’m doing.”')
                                jump whitemarshes_attacked04
                            '“I know I’m asking you all for a lot of trust, but you won’t regret it. I can fix all of this.”' if not whitemarshes_attack_companion_bandits:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know I’m asking you all for a lot of trust, but you won’t regret it. I can fix all of this.”')
                                jump whitemarshes_attacked04
                            '“If we push too much, we may regret this for the rest of our lives. Let’s save ourselves with a bit of compassion.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If we push too much, we may regret this for the rest of our lives. Let’s save ourselves with a bit of compassion.”')
                                jump whitemarshes_attacked04
                            'I smile. “Treat {color=#f6d6bd}[horsename]{/color} well while I’m away.”' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Treat {color=#f6d6bd}%s{/color} well while I’m away.”' %horsename)
                                jump whitemarshes_attacked04
                            'I take a deep breath and head toward the gate, ready to go.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and head toward the gate, ready to go.')
                                jump whitemarshes_attacked04
                    'My voice is grim. “I’m ready to do whatever it takes to stop him.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My voice is grim. “I’m ready to do whatever it takes to stop him.”')
                        $ whitemarshes_attack_plan = "whateverittakes"
                        if whitemarshes_attack_companion_pelt:
                            $ custom1 = "\n\n“If anything, be sure to finish him quickly,” says one of the hunters from {color=#f6d6bd}Pelt{/color}. “He may curse you, or tell the undead to turn against us.”"
                        else:
                            $ custom1 = ""
                        if whitemarshes_attack_companion_galerocks:
                            $ galerocks_reputation -= 1
                            $ custom2 = "\n\n{color=#f6d6bd}Tatius{/color} emphatically shakes his head, and tells you to think straight. “We were meant to get rid of the undead, not murder Wright’s priests. I’d rather give up than start a war. In the name of {color=#f6d6bd}Gale Rocks{/color}, I ask you to reconsider.”"
                        else:
                            $ custom2 = ""
                        if whitemarshes_attack_companion_bandits:
                            $ glaucia_friendship += 1
                            $ custom3 = "\n\nAfter a longer pause, {color=#f6d6bd}Glaucia{/color} gives you a pat on the back. “I’ve nothing to add. Good call, outsider. If you weren’t ready to do this,” she pauses, “I would be.”"
                        else:
                            $ custom3 = ""
                        menu:
                            'She looks around, then nods slowly. “Well, someone had to say it. But the villagers may strike back if they notice such a loss. If you’re going to do this, get out of there fast, [pcname].”[custom2][custom1][custom3]
                            '
                            '“Don’t worry, {color=#f6d6bd}Glaucia{/color}. I know what I’m doing.”' if whitemarshes_attack_companion_bandits:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry, {color=#f6d6bd}Glaucia{/color}. I know what I’m doing.”')
                                jump whitemarshes_attacked04
                            '“It’s our only chance. We must be sure to use it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s our only chance. We must be sure to use it.”')
                                jump whitemarshes_attacked04
                            'I smile. “Treat {color=#f6d6bd}[horsename]{/color} well while I’m away.”' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Treat {color=#f6d6bd}%s{/color} well while I’m away.”' %horsename)
                                jump whitemarshes_attacked04
                            'I take a deep breath and head toward the gate, ready to go.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and head toward the gate, ready to go.')
                                jump whitemarshes_attacked04

    label whitemarshes_attacked04:
        $ quarters = 95
        show areapicture bogroadentirety at basicfade
        $ pc_area = "whitemarshes"
        if not renpy.music.get_playing(channel='music') == "<loop 5.0>audio/hinterheimfinnalylost_orentius_loop.ogg":
            play music "<loop 5.0>audio/hinterheimfinnalylost_orentius_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 2.0, 1.5, color="#0f2a3f")
        menu:
            'Things are going smoothly. The wild beasts, worried by your loud and large band, keep their distance. With the druid’s help, you find a somewhat safe, though wet, route around the creepers, and after observing the lantern-carrying wall patrols you manage to sneak up, hiding in the shallow moat. After all, the locals were meant to keep an eye on the creatures of the night, not invaders.
            \n\nWith a cold wind hitting your soaked boots, you’re at the gate, crying for help. The guards call to one another, afraid you may be in danger. “Open the gates! You’re safe now!” The last few words are aimed at you.
            '
            'I’m doing this for their own good.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m doing this for their own good.')
                jump whitemarshes_attacked05
            'I’m doing this for the peninsula.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m doing this for the peninsula.')
                jump whitemarshes_attacked05
            'I can’t believe it has come to this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t believe it has come to this.')
                jump whitemarshes_attacked05
            'It’s as if I’m stabbing them in their backs.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s as if I’m stabbing them in their backs.')
                jump whitemarshes_attacked05

    label whitemarshes_attacked05:
        show areapicture whitemarshes01night at basicfade
        if not whitemarshes_spying_completed:
            if whitemarshes_attack_numberofallies < 3:
                $ whitemarshes_attack_numberofdead += 1
                $ custom4 = "One of yours is already dead, surprised after he entered a dark alley by himself. The locals’ decision to forbid you to get a good look around the village has already caused difficulties."
            else:
                $ custom4 = "One of yours is already wounded, surprised after he entered a dark alley by himself. The locals’ decision to forbid you to get a good look around the village has already caused difficulties, but the sheer number of your allies has made your storm unstoppable."
        else:
            $ custom4 = "So far, there has been no real bloodshed - the spying you did for {color=#f6d6bd}Glaucia{/color} helped you organize your storm to avoid darker alleys and sheds."
        menu:
            'After a few long minutes you’re standing by the well, surrounded with chaos and weeping. The hostages are gathered in the center of the animal pen, guarded by your forces - most of them being defenseless children and elders, as well as a few workers with slim, weak shells. The guards, now disarmed, were squeezed into the nearby shed.
            \n\nYour band observes the walking corpses with a mixture of fear and disgust - the same way the locals look at you. [custom4] Now even more people gather at the edge of the light cast by your torches - too afraid to attack, too lost and terrified to abandon their loved ones.
            \n\nFour of your allies are leading {color=#f6d6bd}Helvius{/color} to the rest of hostages, unarmed, tied with ropes. His face carries red marks left by punches. He spits in your direction, but can’t do anything.
            '
            'I raise my voice. “The days of dark magic have come to an end. Don’t fight us, and we won’t hurt you.”' if whitemarshes_attack_plan == "banish":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my voice. “The days of dark magic have come to an end. Don’t fight us, and we won’t hurt you.”')
                jump whitemarshes_attacked06
            'I nod to my people. “Time for me to speak with {color=#f6d6bd}Orentius{/color}. Stay close.”' if whitemarshes_attack_plan != "banish":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to my people. “Time for me to speak with {color=#f6d6bd}Orentius{/color}. Stay close.”')
                jump whitemarshesorentius01

    label whitemarshes_attacked06:
        $ whitemarshes_nomoreundead = (day+1)
        if whitemarshes_attack_companion_bandits:
            $ custom3 = "{color=#f6d6bd}Glaucia’s{/color} gaze could kill an auroch, but after she notices your glance, she obediently nods. "
        else:
            $ custom3 = ""
        menu:
            'You point at the wooden cabin and tell your people to “bring the necromancer,” which takes them less than a minute. The elder doesn’t fight back - wearing old sandals and a worn robe, he leans against a walking stick. As he observes his tribe, there are tears of pain in his two-colored eyes. Some of his followers have already gathered by the pond, asking The Wright for protection loudly.
            \n\nHis yellowish skin resembles a piece of parchment, tightly stretched over his shell, which holds no trace of fat. The hair in his ears and on his ink-stained fingers is thick and neglected, while his shaved face and scalp make him resemble an ill infant. After every few breaths he squints his two-colored eyes.
            \n\n[custom3]When the man speaks, his voice crackles, like a falling branch in dry woods. “Don’t hurt my people.”
            '
            'I offer him one of the dark cloaks to keep him warm.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him one of the dark cloaks to keep him warm.')
                $ custom1 = "He accepts it, though with little enthusiasm. After you explain what will happen next, he doesn’t meet your eyes. “You’re pushing all these people to their deaths,” he whispers, “but I see your hearts are merciless.”"
                jump whitemarshes_attacked07
            '“Purge the undead, priest. I won’t ask again.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Purge the undead, priest. I won’t ask again.”')
                $ custom1 = "He doesn’t meet your eyes. “You’re pushing all these people to their deaths,” he whispers, “but I see your hearts are merciless.”"
                jump whitemarshes_attacked07

    label whitemarshes_attacked07:
        show areapicture whitemarshes01night at basicfade
        $ orentius_banished = 1
        $ achievement_pyrepoints += 1
        $ whitemarshes_nomoreundead = (day+1)
        if whitemarshes_attack_companion_galerocks:
            $ custom2 = " “Exhausted,” says a fighter from {color=#f6d6bd}Gale Rocks{/color}."
        else:
            $ custom2 = ""
        menu:
            '[custom1]
            \n\nThere’s no gesture, no ritual of blood, not even a word. The man’s eyes grow dimmer, and as he falls to the ground - caught just in time by one of your guards - you hear thudding coming from various directions. The undead, previously walking or standing in the back of the village, or even on top of the walls, all at once fall to the ground, with their shells offering no resistance. The bones of the skeletons turn into disjointed piles, with some of the skulls rolling away, until they sink in the mud.
            \n\nYour people exchange surprised glances, and so do the locals. In just a heartbeat, the army of awoken is no more.
            \n\nYou approach the mage. He’s asleep, breathing, but heavily.[custom2]
            '
            'I try to stay in control. “You’ll now burn the shells, as one should,” I order {color=#f6d6bd}the mayor{/color}. “We’re leaving.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to stay in control. “You’ll now burn the shells, as one should,” I order {color=#f6d6bd}the mayor{/color}. “We’re leaving.”')
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ custom2 = "The group from {color=#f6d6bd}Gale Rocks{/color}, who keep to themselves, scowl at the others, but say nothing."
                else:
                    $ custom2 = ""
                menu:
                    '“Fuck you, outsider,” he responds, but you know he has no other option. His tribe, crying and terrified, will have a heavy few days.
                    \n\nThe fighters let out relieved sighs and chuckles, leading you toward the gate. “Now let us grab our spoils en we can leave,” says a guard from {color=#f6d6bd}Howler’s{/color}. Without waiting for your answer, they unpack large sacks, fill them up with weapons you took from the locals, and head toward the humble houses and workshops. [custom1][custom2]
                    '
                    'I should have expected this. I say nothing.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have expected this. I say nothing.')
                        jump whitemarshesorentiusafterdisputebanished03attack01a
                    'It’s not the right time to get into an argument. We need to look strong.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not the right time to get into an argument. We need to look strong.')
                        label whitemarshesorentiusafterdisputebanished03attack01a:
                            show areapicture bogcrossroadstowhitemarshes at basicfade
                            if whitemarshes_attack_companion_galerocks:
                                $ custom2 = "{color=#f6d6bd}Tatius{/color} tells them to shut it - “you’ll spook all them beasts.”"
                            else:
                                $ custom2 = ""
                            menu:
                                'You spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows he found, together with a pretty mug made of an auroch’s horn.[custom2]
                                '
                                'Seems like I’ve been played after all.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                    jump whitemarshesorentiusafterdisputebanished03attack02
                                'Whatever I tried to accomplish... I’m now a pillager.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                    jump whitemarshesorentiusafterdisputebanished03attack02
                                'Such are the rules of war.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Such are the rules of war.')
                                    jump whitemarshesorentiusafterdisputebanished03attack02
                    'I point at the loot. “What’s going on here?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point at the loot. “What’s going on here?”')
                        if whitemarshes_attack_companion_pelt:
                            $ custom1 = "A hunter clears his throat. “I mean, we ain’t leaving empty-handed. We’ll grab no seeds, no food, they’ll be fine.”\n\nA guard looks at you like you’re an idiot. “{color=#f6d6bd}Thais{/color} let us.”"
                        else:
                            $ custom1 = "A guard looks at you like you’re an idiot. “Just the spoils. {color=#f6d6bd}Thais{/color} told us what we need. Ne much.”"
                        menu:
                            '[custom1]
                            '
                            '“No one discussed this with me.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No one discussed this with me.”')
                                if whitemarshes_attack_companion_bandits:
                                    $ custom1 = "She shrugs. “So? There was nae need.”\n\nOne of {color=#f6d6bd}Glaucia’s{/color} men shifts from one foot to the other. “Time to get to it, right? We’ve no time.”"
                                else:
                                    $ custom1 = "She shrugs. “So? There was nae need.”"
                                menu:
                                    '[custom1]
                                    '
                                    '“Fine. You deserve it, I guess.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                        $ howlersdell_reputation += 1
                                        if whitemarshes_attack_companion_pelt:
                                            $ iason_friendship += 1
                                        if whitemarshes_attack_companion_galerocks:
                                            $ galerocks_reputation -= 1
                                        if whitemarshes_attack_companion_bandits:
                                            $ glaucia_friendship += 1
                                        jump whitemarshesorentiusafterdisputebanished03attack01a
                                    '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                        jump whitemarshesorentiusafterdisputebanished03attack01b
                            '“Fine. You deserve it, I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                $ howlersdell_reputation += 1
                                if whitemarshes_attack_companion_pelt:
                                    $ iason_friendship += 1
                                if whitemarshes_attack_companion_galerocks:
                                    $ galerocks_reputation -= 1
                                if whitemarshes_attack_companion_bandits:
                                    $ glaucia_friendship += 1
                                jump whitemarshesorentiusafterdisputebanished03attack01a
                            '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                label whitemarshesorentiusafterdisputebanished03attack01b:
                                    $ howlersdell_reputation -= 1
                                    if whitemarshes_attack_companion_pelt:
                                        $ iason_friendship -= 1
                                    if whitemarshes_attack_companion_galerocks:
                                        $ galerocks_reputation += 1
                                    if whitemarshes_attack_companion_bandits:
                                        $ glaucia_friendship -= 1
                                    if whitemarshes_attack_companion_bandits:
                                        $ pc_hp = limit_pc_hp(pc_hp-2)
                                        show minus2hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                        if whitemarshes_attack_companion_galerocks:
                                            $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement,"
                                        else:
                                            $ custom2 = "Your allies frown, either reaching for their weapons, or raising them,"
                                        $ whitemarshes_attack_glauciaattackedpc = 1
                                        menu:
                                            '[custom2] but you then hear a loud “fuck this” behind your back. Right when you recognize {color=#f6d6bd}Glaucia’s{/color} voice, darkness covers your eyes.
                                            '
                                            'Unconscious, I fall on the ground.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Unconscious, I fall on the ground.')
                                                jump whitemarshesorentiusafterdisputebanished03attack02alt
                                    else:
                                        show areapicture bogcrossroadstowhitemarshes at basicfade
                                        if whitemarshes_attack_companion_galerocks:
                                            $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement, but the others frown, either reaching for their weapons, or raising them."
                                        else:
                                            $ custom2 = "Your allies frown, either reaching for their weapons, or raising them."
                                        menu:
                                            '[custom2] After a few tense moments, your people simply ignore you, stepping away and getting on with their tasks. After another few minutes, the pillagers, now with heavy sacks of loot, leave the village, and the hostages are left behind. You no longer lead this band.
                                            \n\nYou spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows he found, together with a pretty mug made of an auroch’s horn.
                                            '
                                            'Seems like I’ve been played after all.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                                jump whitemarshesorentiusafterdisputebanished03attack02
                                            'Whatever I tried to accomplish... I’m now a pillager.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                                jump whitemarshesorentiusafterdisputebanished03attack02

label whitemarshesorentiusARRIVAL_ALL:
    label whitemarshesorentius01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ orentius_met = 1
        if not renpy.music.get_playing(channel='music') == "<loop 5.0>audio/hinterheimfinnalylost_orentius_loop.ogg":
            play music "<loop 5.0>audio/hinterheimfinnalylost_orentius_loop.ogg" fadeout 1.0 fadein 1.0
        if helvius_about_oldtunnel_paid and helvius_about_oldtunnel_paid > day:
            $ helvius_about_oldtunnel_paid = 0
        # show areapicture whitemarshes01night at basicfade
        if thyrsus_orentius_helped:
            $ custom1 = "The dark figures spread. You sneak through the dark alleys, with no undead or guards in sight. A curious girl observes you from an open door until one of your guides pushes her head inside, telling her to go to sleep.\n\nYou approach the flooded grass, step on the wooden beams, and climb up the squeaky stairs. At the entrance, {color=#f6d6bd}Thyrsus{/color} takes a deep breath, but looks at you encouragingly."
        elif helvius_orentius_helped:
            $ orentius_friendship += 1
            $ custom1 = "The guards head toward the flooded grass, gesturing for you to climb up the wooden beams, then the squeaky stairs. The locals, lured by this unusual event, gather around the building, and the few lanterns they’re carrying reveal their eyes. In them, you find worry, curiosity, and hints of hope, or so you think. The boggy air grows denser from their silence.\n\nOn the top of the platform, a large guard steps aside, allowing you to reach the door."
        elif whitemarshes_attacked:
            $ custom1 = "Your people let you through. You climb up the wooden beams, then the squeaky stairs. The locals gather around the building, and the few lanterns they’re carrying reveal their eyes. In them, you find worry, curiosity, and hints of hope, or so you think. The boggy air grows denser from their silence.\n\nYou stand in front of the door, all by yourself."
        $ at_activate = 1
        $ at = 0
        menu:
            '[custom1]
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            'I knock gently.' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I knock gently.')
                $ at_activate = 0
                $ at = 0
                menu:
                    'You wait for a few breaths, then hear the hoarse voice of an elder. “Not hungry.”
                    '
                    '“It’s urgent, I’m afraid.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s urgent, I’m afraid.”')
                        $ orentius_friendship += 0
                        $ orentius_attitude = "distanced"
                        $ custom1 = "“Come.” You push the door, making the weak flame dance under the touch of cold air. The man gives you a reproachful look from the bench.\n\nThe chamber is humid and smells of sweat. It’s lit by a single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Here comes the warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “a dagger of the masters.”"
                        jump whitemarshesorentius02
                    '“Let me in. We need to talk.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me in. We need to talk.”')
                        $ orentius_friendship -= 1
                        $ orentius_attitude = "intimidating"
                        $ custom1 = "“In.” You push the door, making the weak flame dance under the touch of cold air. The man gives you a reproachful look from the bench.\n\nThe chamber is humid and smells of sweat. It’s lit by a single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Here comes the warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “to judge and punish.”"
                        jump whitemarshesorentius02
                    '“Forgive me, but I need to speak with you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forgive me, but I need to speak with you.”')
                        $ orentius_friendship += 1
                        $ orentius_attitude = "friendly"
                        $ custom1 = "“Come.” You push the door, making the weak flame dance under the touch of cold air. The man looks at you from the bench, speaking with concern, like a parent to a child. “I’ve nothing to forgive,” he swallows his saliva, struggling to speak. “Join me, an’ let’s be lost together.”\n\nThe chamber is humid and smells of sweat. The single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Speak to me, warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “an’ tell me of the destruction you’re planning.”"
                        jump whitemarshesorentius02
            'I tap a melody on the planks with my fingers.' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I tap a melody on the planks with my fingers.')
                $ at_activate = 0
                $ at = 0
                $ orentius_friendship -= 1
                $ orentius_attitude = "playful"
                $ custom1 = "After a few breaths, you hear the annoyed, raised voice of an elder. “In or out,” he commands, and you push the door. Without a word, the man sitting on the bench gives you a reproachful look.\n\nThe chamber is humid and smells of sweat. It’s lit by a single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Here comes the warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “to mock my creation and judge me.”"
                jump whitemarshesorentius02
            'I push the door and walk in.' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I push the door and walk in.')
                $ at_activate = 0
                $ at = 0
                $ orentius_friendship += 0
                $ orentius_attitude = "distanced"
                $ custom1 = "The weak flame dances under the touch of cold air. Without a word, the man sitting on the bench turns toward you, giving you an absent look.\n\nThe chamber is humid and smells of sweat. The single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“You’re that warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “a dagger of the masters.”"
                jump whitemarshesorentius02
            'I kick the door and barge in.' ( condition="at == 'intimidating' and not helvius_orentius_helped" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I kick the door and barge in.')
                $ at_activate = 0
                $ at = 0
                $ orentius_friendship -= 1
                $ orentius_attitude = "intimidating"
                $ custom1 = "The cool air scatters the sheets of parchment. The elder turns around on his bench, giving you a reproachful look without a word. Green ink is dripping from his fingers.\n\nThe chamber is humid and smells of sweat. It’s lit by a single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Here comes the warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “to judge and punish.”"
                jump whitemarshesorentius02
            'I barge in.' ( condition="at == 'intimidating' and helvius_orentius_helped" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I barge in.')
                $ at_activate = 0
                $ at = 0
                $ orentius_friendship -= 1
                $ orentius_attitude = "intimidating"
                $ custom1 = "The cool air scatters the sheets of parchment. The elder turns around on his bench, giving you a reproachful look without a word. Green ink is dripping from his fingers.\n\nThe chamber is humid and smells of sweat. It’s lit by a single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Here comes the warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “to judge and punish.”"
                jump whitemarshesorentius02
            'I push the door slowly. “Forgive me for disrupting your peace.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I push the door slowly. “Forgive me for disrupting your peace.”')
                $ at_activate = 0
                $ at = 0
                $ orentius_friendship += 1
                $ orentius_attitude = "vulnerable"
                $ custom1 = "The weak flame dances under the touch of cold air. The man sitting on the bench turns toward you, speaking with concern, like a parent to a child. “In years, no peace’s been found among these lands,” he swallows his saliva, struggling to speak. “Ba join me, we’ll look for it together.”\n\nThe chamber is humid and smells of sweat. The single wax candle that stands beneath a brass hourglass, dangerously close to an open codex, whose pages are covered with fresh letters. While the large collection of parchment must be of great value, the man has hardly any possessions - humble bowls and cups, writing instruments, enough candles to keep him company for the next ten days. You glance at the single pelt placed on the floor. To sleep on it, you’d have to curl up your legs.\n\n“Though I’d rather do so without a warden,” {color=#f6d6bd}the priest’s{/color} voice crackles, like a falling branch in dry woods, “for you’re here to destroy, not build.”"
                jump whitemarshesorentius02

    label whitemarshesorentius02:
        show areapicture orentiushouse01 at basicfade
        if thyrsus_orentius_helped:
            $ custom2 = "“Or why else would my enemies let you in? To bring me a hare pie? They know I won’t be moved by you.”"
        elif helvius_orentius_helped:
            $ custom2 = "“Or why else would you do so much to see me? Not to pray at Wright’s sign,” he touches the hourglass with his slender fingers. “My people know I won’t be moved by you.”"
        elif whitemarshes_attacked:
            $ custom2 = "“Or why else would the city send you against me? Not to hold my notes, ‘specially with the band you’ve gathered outside.”"
        menu:
            '[custom1]
            \n\nBefore you respond, he turns away. [custom2]
            '
            '“I just want to talk.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just want to talk.”')
                $ orentius_friendship += 0
                $ custom1 = "“An’ {i}I{/i} just don’t believe you, ba start,” his tone carries little invitation. “The night won’t be young forever.”"
                jump whitemarshesorentius03
            '“Tell me your side of the story.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me your side of the story.”')
                $ orentius_friendship += 1
                $ custom1 = "“{i}My{/i} side?” He flinches, then raises his wrinkled chin and clicks loudly, as if he’s munching on his tongue. “What may I say that you don’t see? We had to save our people, an’ {i}I{/i} was shown the way to do so. T’s not a tale, ba our lives. My voice won’t make them better or worse, for you can see them carved by the past,” as he pulls the neckline of his robe, revealing his skinny neck and chest, you think of all the other people you’ve seen in the village."
                jump whitemarshesorentius03
            '“I need you to stop this madness.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need you to stop this madness.”')
                $ custom1 = "He glances back at the open book, raising a quill, but without touching the inkwell. You spend a good minute in silence, yet the man doesn’t return to his work, instead reading the previous signs slowly. His lips are shaking."
                $ orentius_friendship -= 1
                jump whitemarshesorentius03

    label whitemarshesorentius03:
        if whitemarshes_attacked:
            $ custom2 = ""
        elif whitemarshes_reputation >= 8:
            $ orentius_friendship += 2
        else:
            $ orentius_friendship += 1
            $ custom2 = ""
        $ questionpreset = "orentius1"
        menu:
            '[custom1]
            \n\nIn this weak light, his yellowish skin resembles the very parchment he uses, tightly stretched over his shell, which holds no trace of fat. The hair in his ears and on his ink-stained fingers is thick and neglected, while his shaved face and scalp make him resemble an ill infant. After every few breaths he squints his two-colored eyes. His feet are dirty and covered with scratches, while his linen robe is little more than a rag.
            '
            '(orentius1 set)':
                pass

label whitemarshesorentiusaboutundeadaredangerousALL:
    label whitemarshesorentiusaboutundeadaredangerous01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You must be aware that undead are dangerous.”')
        $ orentius_argument_undeadaredangerous = 1
        menu:
            '“When left to themselves, like the flame f’a hearth,” he rests his elbows on the table and puts a finger to his lips, rubbing them gently. “They’re the night that follows a shell’s day, ba, like lightning or the wind, merely a part f’our world.”
            '
            '“You say it as if you’re awakening the undead with your pneuma alone, but I saw your rituals of blood. Is this a part of {i}our world{/i} as well?”' if sleep_whitemarshes and not orentius_argument_sleepingritual:
                jump whitemarshesorentiusaboutundeadaredangerous02sleepingritual
            '“Once you’re gone, the awoken shells will be out of anyone’s control, and will threaten everyone in the North. You’re playing a dangerous game.”' if aeli_about_necromancers_question02 and not orentius_argument_aeliaboutundead:
                jump whitemarshesorentiusaboutundeadaredangerous02aeliaboutundead
            '“The shells you’re using aren’t just your own dead. You stole the corpses of other families.”' if description_whitemarshes12 and not orentius_argument_notjusttheirowndead:
                jump whitemarshesorentiusaboutundeadaredangerous02notjusttheirowndead
            '“You may feel strongly about the undead now, but you already changed your views before. You used to reject any sort of {i}pagan magic{/i}.”' if thyrsus_about_druids2 and not orentius_argument_fickleness:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may feel strongly about the undead now, but you already changed your views before. You used to reject any sort of {i}pagan magic{/i}.”')
                $ orentius_argument_fickleness = 1
                $ orentius_arguments += 1
                $ custom1 = "Both his light and dark eyes are staring at you, as if you’re some mysterious mushroom. “Mayhap,” he says slowly, “ba I follow no pagan teachings. What I try to master was shown to me by The Only Spirit, an’ I’d rather hide my soul than stain it against Wright’s will.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“There are ways to get things done without necromancy. Instead, you could support {color=#f6d6bd}Eudocia’s{/color} work and use one of her golems.”' if eudocia_about_whitemarshes and not orentius_argument_eudocia_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There are ways to get things done without necromancy. Instead, you could support {color=#f6d6bd}Eudocia’s{/color} work and use one of her golems.”')
                $ orentius_argument_eudocia_about_whitemarshes = 1
                $ orentius_arguments += 1
                $ custom1 = "“Golems?” He waits for you to carry on, and has to think about an answer for quite a few breaths. “I canna say I’ve heard about it. Ba even if what you’re saying’s true, we’ve hardly anything to give her in return. I’ll... discuss it with {color=#f6d6bd}Helvius{/color}.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“If you say so.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you say so.”')
                $ questionpreset = "orentius1"
                menu:
                    'He moves his quill aside and covers his inkwell with a lid. His loud breath grows impatient.
                    '
                    '(orentius1 set)':
                        pass

    label whitemarshesorentiusaboutundeadaredangerous02:
        menu:
            '[custom1]
            '
            '“You say it as if you’re awakening the undead with your pneuma alone, but I saw your rituals of blood. Is this a part of {i}our world{/i} as well?”' if sleep_whitemarshes and not orentius_argument_sleepingritual:
                jump whitemarshesorentiusaboutundeadaredangerous02sleepingritual
            '“Once you’re gone, the awoken shells will be out of anyone’s control, and will threaten everyone in the North. You’re playing a dangerous game.”' if aeli_about_necromancers_question02 and not orentius_argument_aeliaboutundead:
                jump whitemarshesorentiusaboutundeadaredangerous02aeliaboutundead
            '“The shells you’re using aren’t just your own dead. You stole the corpses of other families.”' if description_whitemarshes12 and not orentius_argument_notjusttheirowndead:
                jump whitemarshesorentiusaboutundeadaredangerous02notjusttheirowndead
            '“You may feel strongly about the undead now, but you already changed your views before. You used to reject any sort of {i}pagan magic{/i}.”' if thyrsus_about_druids2 and not orentius_argument_fickleness:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may feel strongly about the undead now, but you already changed your views before. You used to reject any sort of {i}pagan magic{/i}.”')
                $ orentius_argument_fickleness = 1
                $ orentius_arguments += 1
                $ custom1 = "Both his light and dark eyes are staring at you, as if you’re some mysterious mushroom. “Mayhap,” he says slowly, “ba I follow no pagan teachings. What I try to master was shown to me by The Only Spirit, an’ I’d rather hide my soul than stain it against Wright’s will.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“There are ways to get things done without necromancy. Instead, you could support {color=#f6d6bd}Eudocia’s{/color} work and use one of her golems.”' if eudocia_about_whitemarshes and not orentius_argument_eudocia_about_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There are ways to get things done without necromancy. Instead, you could support {color=#f6d6bd}Eudocia’s{/color} work and use one of her golems.”')
                $ orentius_argument_eudocia_about_whitemarshes = 1
                $ orentius_arguments += 1
                $ custom1 = "“Golems?” He waits for you to carry on, and has to think about an answer for quite a few breaths. “I canna say I’ve heard about it. Ba even if what you’re saying’s true, we’ve hardly anything to give her in return. I’ll... discuss it with {color=#f6d6bd}Helvius{/color}.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            'I move on from this topic.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move on from this topic.')
                $ questionpreset = "orentius1"
                menu:
                    'He moves his quill aside and covers his inkwell with a lid. His loud breath grows impatient.
                    '
                    '(orentius1 set)':
                        pass

    label whitemarshesorentiusaboutundeadaredangerous02sleepingritual:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You say it as if you’re awakening the undead with your pneuma alone, but I saw your rituals of blood. Is this a part of {i}our world{/i} as well?”')
        $ orentius_argument_sleepingritual = 1
        menu:
            'He moves his shoulders with an embarrassed sigh, but then looks at you with his dark eye and regains his composure. “Suffering? F’course it is.”
            '
            '“The wounds you inflict upon yourself will lead to your death.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The wounds you inflict upon yourself will lead to your death.”')
                $ orentius_friendship += 1
                $ custom1 = "“They may, once my thoughts get clouded, ba you canna see how they’ve changed over the last few years. I grow stronger,” the sight of his fragile, drowsy shell fills you with doubt, “an’ more trusting in Wright’s light.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“Don’t you feel repulsed when you see what you’re doing? The blood drying on the cups, the corpses you awaken? It must touch your conscience.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you feel repulsed when you see what you’re doing? The blood drying on the cups, the corpses you awaken? It must touch your conscience.”')
                $ custom1 = "“Should a cityfolk truly speak to me this way?” He raises his hands to his chest, palms up, in a weak shrug. “For years, I’ve heard f’the chains your people put on human necks, f’the greed f’your priests, an’ the beggars on your streets. If I were to shape the realms to ease my {i}feelings{/i},” he taps his codex, then speaks with sudden strength, “your ships an’ strongholds would be swallowed by waves.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“Blood magic and necromancy may be a part of our world, but so are plagues and famines. We may need to accept them, but it doesn’t make them {i}right{/i}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Blood magic and necromancy may be a part of our world, but so are plagues and famines. We may need to accept them, but it doesn’t make them {i}right{/i}.”')
                $ orentius_arguments += 1
                $ custom1 = "He stares into his codex, tapping his fingers against each other. There’s thoughtfulness in his silence, if not approval."
                jump whitemarshesorentiusaboutundeadaredangerous02

    label whitemarshesorentiusaboutundeadaredangerous02aeliaboutundead:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Once you’re gone, the awoken shells will be out of anyone’s control, and will threaten everyone in the North. You’re playing a dangerous game.”')
        $ orentius_argument_aeliaboutundead = 1
        $ orentius_arguments += 1
        menu:
            'At first he twitches, as if your words have pinched him, but then twists his lips in anger. “An’ who taught you these old tales?”
            '
            '“Why would that matter?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would that matter?”')
                $ custom1 = "“For they ought to be left behind us. There are ways to protect ourselves from the mistakes f’the necromancers who lived before the emperors. I’ve no sole power over these shells. Others will carry my pneuma forward.”\n\nYou ask if he can name anyone among his followers who may be capable of replacing him, but he purses his lips."
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“{color=#f6d6bd}Aeli{/color}, a local monk.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Aeli{/color}, a local monk.”')
                $ orentius_friendship -= 1
                $ description_oldpagos10 = "According to {color=#f6d6bd}Orentius{/color}, the locals “have nuff zeal to spread doubt about us, yet lacked faith to help us when we needed them the most.”"
                $ custom1 = "He scoffs, then says something in what sounds like Old Speech, though you’re not sure what exactly. “The people {color=#f6d6bd}f’Old Págos{/color} have nuff zeal to spread doubt about us, yet lacked faith to help us when we needed them the most. The Wright’s guided me so far. With their light, the path forward will be clear to me, once I need to see it.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '(lie) “Everyone in the city knows it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Everyone in the city knows it.”')
                $ orentius_friendship += 1
                $ pc_lies += 1
                $ custom1 = "His hollow cheeks relax slightly. “Then you were taught by the untaught. There are ways to protect ourselves from the mistakes f’the necromancers who lived before the emperors. I’ve no sole power over these shells. Others will carry my pneuma forward.”\n\nYou ask if he can name anyone among his followers who may be capable of replacing him, but he purses his lips."
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“Are you saying you never experienced any troubles with your creations?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you saying you never experienced any troubles with your creations?”')
                $ orentius_arguments -= 1
                $ custom1 = "You’re not sure if he noticed that you avoided his question, for his voice suddenly grows stronger, and he rests his hand on his side proudly. “T’s the truth. My people don’t die as much from hard work anymore. The awoken shells may be unsightly, ba we’ve had no accidents, no tragedies.”\n\n“Yet,” you add, but he spares you only a snicker."
                jump whitemarshesorentiusaboutundeadaredangerous02

    label whitemarshesorentiusaboutundeadaredangerous02notjusttheirowndead:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The shells you’re using aren’t just your own dead. You stole the corpses of other families.”')
        $ orentius_argument_notjusttheirowndead = 1
        $ orentius_arguments += 1
        menu:
            '“I’d forgive a starving child who {i}stole{/i} a dropped plum,” he starts with conviction, repeating an answer he has well-memorized, but seeing your frown, his voice grows shaky, “or moving into a pillaged home. I take no pleasure in my deeds, ba I’ve been right to stain my innocence for the sake f’others.”
            '
            '“But you also hurt the memories and beliefs of other families and tribes. Their will deserves to be respected.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But you also hurt the memories and beliefs of other families and tribes. Their will deserves to be respected.”')
                $ orentius_friendship -= 1
                $ custom1 = "“It doesn’t,” his voice is close to a hiss. “Not when it stands in our only path to survival. Wright’s teachings ought to show us how to build a better world for ourselves, not imprison us in superstitions.”"
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“These matters are not for a single soul to judge. It may all make sense in your eyes, but these things get more complex the deeper you dig into them. There may be consequences you can’t yet see, but that are just as valid.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These matters are not for a single soul to judge. It may all make sense in your eyes, but these things get more complex the deeper you dig into them. There may be consequences you can’t yet see, but that are just as valid.”')
                $ orentius_arguments += 1
                $ custom1 = "“You say so as if I put ba a single thought into it, an’ not many years of prayers and reading.” His words, while clear, are undercut by his doubt. He looks at his hourglass, moving his lips quietly."
                jump whitemarshesorentiusaboutundeadaredangerous02
            '“If you keep hurting the beliefs of others, they’ll abandon you, or seek their revenge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you keep hurting the beliefs of others, they’ll abandon you, or seek their revenge.”')
                $ custom1 = " “Look around, warden. We were abandoned a long time ago. T’s what led us to our deeds, an’ our deeds make us grow even further apart. So is the tragedy f’the tormented tribes.”"
                jump whitemarshesorentiusaboutundeadaredangerous02

label whitemarshesorentiusaboutorthodoxyALL:
    label whitemarshesorentiusaboutorthodoxy01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should a priest of The Wright really involve themselves with forbidden rituals?”')
        $ orentius_argument_orthodoxy = 1
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'He gestures for you to sit down next to him, and puts a hand on your shoulder. The many types of ink he uses in his work have left colorful dots on his fingers - green, yellow, blue, black, red. “T’s a big thought for a layman, ba you can trust me. I put years into studying Wright’s will, an’ they’re guiding me through all f’this. I revealed the truth the Unites an’ Seekers were hiding in their arrogance, the words they mistook. One day, you may understand this too.”
            '
            '“And I also had an opportunity to study Wright’s Tablets. Can we talk about them?”' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And I also had an opportunity to study Wright’s Tablets. Can we talk about them?”')
                $ quarters += 1
                $ orentius_arguments += 1
                $ at_unlock_knowledge = 0
                $ at = 0
                $ custom1 = "In the following minutes, you must admit that {color=#f6d6bd}Orentius{/color} knows his passages well, and is capable of quoting large chunks of old stories from memory. However, you realize quickly that he has indeed misunderstood a few words used by Adir’s tribe, and fell into an old heresy, discussed and refuted a few centuries back in the cities. You explain his mistakes slowly, and while he rejects most of your observations, his confidence and eagerness diminish, especially when you mention that he’s far from being the first to come up with his ideas.\n\nHe rests his chin on the palm of his hand, nodding along as you close his copy of Wright’s teachings."
                jump whitemarshesorentiusaboutorthodoxy02
            '“I grew up in a fellowship as well, but I was always taught to pursue freedom, not security and progress. These awoken shells of yours worry me.”' if pc_religion == "fellowship":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I grew up in a fellowship as well, but I was always taught to pursue freedom, not security and progress. These awoken shells of yours worry me.”')
                $ quarters += 1
                $ orentius_arguments += 1
                $ at_unlock_knowledge = 0
                $ at = 0
                $ custom1 = "You may not be a priest, but you describe your issues and the traditions of your church. {color=#f6d6bd}Orentius{/color} has a few pointed attacks on the larger religions of The Wright, often referencing their greed and hypocrisy, but whenever you bring his attention back to your own views, he seems stuck, allowing you to finish your thought.\n\nEven though he’s far from convinced, he claims to “see” your points. He rests his chin on the palm of his hand, nodding along as you assure him that you’ll say hello to your people from him once you see them again."
                jump whitemarshesorentiusaboutorthodoxy02
            '{image=d6} “As a follower of The Wright, I’ll try to follow your thoughts on this. Explain them to me.”' ( condition="(at != 'knowledge' and pc_religion == 'theunitedchurch') or (at != 'knowledge' and pc_religion == 'ordersoftruth')" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “As a follower of The Wright, I’ll try to follow your thoughts on this. Explain them to me.”')
                $ quarters += 1
                $ at_unlock_knowledge = 0
                $ at = 0
                if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                    $ orentius_arguments += 1
                    $ custom1 = "You may not be a priest, but you manage to comprehend the meanderings of his beliefs. After you explain them back to him - in a much shorter way - he nods with approval, even though you point out a few contradictions in his tale. While he’s not at all convinced by your observations, he must admit that at least you understand his perspective - and his suspicious eyes grow a bit gentler."
                else:
                    $ custom1 = "You listen to the meanderings of his beliefs, but with little understanding. A few of his ideas seem to be completely detached from one another, and as you try to point this out, he asks you to repeat his arguments back to him - proving that you failed to remember a few crucial details.\n\nAfter a few minutes of back and forth, he raises his chin. A mocking twist crawls onto his lips. “Now you see - Wright’s mysteries take years f’prayers an’ studies. T’s not a pastime for wardens.”"
                jump whitemarshesorentiusaboutorthodoxy02
            'I have little understanding of Wright’s teachings. I won’t be able to convince him with my knowledge. (disabled)' ( condition="at != 'knowledge' and pc_religion != 'fellowship' and pc_religion != 'theunitedchurch' and pc_religion != 'ordersoftruth'" ):
                pass
            '{image=d6} (lie) I stare in his eyes. “How dare you doubt the strength of my faith?”' ( condition="at != 'knowledge' and pc_religion != 'fellowship'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} (lie) I stare in his eyes. “How dare you doubt the strength of my faith?”')
                $ at_unlock_knowledge = 0
                $ at = 0
                if (pc_lies+orentius_friendship) >= 14:
                    $ pc_lies += 1
                    $ orentius_arguments += 1
                    $ custom1 = "He returns your gaze for a good few breaths, then turns away. “Forgive me, warden.”"
                else:
                    $ pc_lies += 1
                    $ orentius_friendship -= 1
                    $ custom1 = "He doesn’t look back. “I do. Prove me wrong, then.” You listen to the meanderings of his beliefs, but with little understanding. A few of his ideas seem to be completely detached from one another, and as you try to point this out, he asks you to repeat his arguments back to him - proving that you failed to remember a few crucial details.\n\nAfter a few minutes of back and forth, he raises his chin. A mocking twist crawls onto his lips. “Now you see - Wright’s mysteries take years f’prayers an’ studies. T’s not a pastime for wardens.”"
                jump whitemarshesorentiusaboutorthodoxy02
            '“You’re the priest here, I guess.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re the priest here, I guess.”')
                $ orentius_friendship += 1
                $ at_unlock_knowledge = 0
                $ at = 0
                $ custom1 = "He smiles gently, pats your shoulder, and turns back to his writings."
                jump whitemarshesorentiusaboutorthodoxy02

    label whitemarshesorentiusaboutorthodoxy02:
        $ at = 0
        $ questionpreset = "orentius1"
        menu:
            '[custom1]
            '
            '(orentius1 set)':
                pass

label whitemarshesorentiusaboutcaius01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met this {i}prophet{/i} at {color=#f6d6bd}Foggy’s{/color}...”')
    $ orentius_argument_caius = 1
    $ quarters += 1
    menu:
        'You tell him about {color=#f6d6bd}Caius{/color}, his faith, past, and visions - of the great flood of Rivers of Faith, and of The New Cities, and of the judgment of sinners. {color=#f6d6bd}The priest{/color} listens carefully, until his patience fades away. “Why are you telling me all this?”
        '
        'I smile. “You know, he’s an {i}interesting{/i} person. Maybe you two should meet one day.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “You know, he’s an {i}interesting{/i} person. Maybe you two should meet one day.”')
            $ orentius_friendship += 1
            $ questionpreset = "orentius1"
            menu:
                'Unable to decide if you’re sarcastic or not, he smiles gently. “I’ll think about it.”
                '
                '(orentius1 set)':
                    pass
        '“Many claim they are guided by The Wright, but their visions can’t all be true at once - how am I to know who speaks the truth?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Many claim they are guided by The Wright, but their visions can’t all be true at once - how am I to know who speaks the truth?”')
            $ orentius_arguments += 1
            $ questionpreset = "orentius1"
            menu:
                'He absently stares at his hourglass, taking a long moment before he speaks. “Tha’s {i}the{/i} question, stranger.”
                '
                '(orentius1 set)':
                    pass
        '“I think he’s crazy. So is anyone who claims to be directly led by The Wright.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think he’s crazy. So is anyone who claims to be directly led by The Wright.”')
            $ orentius_friendship -= 1
            $ questionpreset = "orentius1"
            menu:
                'There’s no anger in his eyes, just compassion. “An’ {i}I{/i} think,” he says gently, “that people who haven’t been guided by them are missing the great joy f’life.”
                '
                '(orentius1 set)':
                    pass
        'I clear my throat. “I just wanted to hear what you think about it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “I just wanted to hear what you think about it.”')
            $ questionpreset = "orentius1"
            menu:
                'He leans away, not sure if you’re serious. “I’d need to talk to him on my own,” he says slowly, “ba I’d be worried to trust {i}a prophet{/i} who’s not doing with their life as much’s they already can.”
                \n\nThere’s pride in his posture, and strength in his voice.
                '
                '(orentius1 set)':
                    pass

label whitemarshesorentiusaboutlocalsALL:
    label whitemarshesorentiusaboutlocals01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you truly believe your people are grateful for your leadership?”')
        $ orentius_argument_locals = 1
        menu:
            '“I only guide their prayers an’ offer my rituals, I canna read anyone’s soul,” his feet are scratching the floor nervously. “I’m sure they have many dif’rent thoughts, ba I’m grateful for {color=#f6d6bd}our mayor’s{/color} trust. He’s young an’ impulsive, ba honest an’ brave, willing to change for the betta.”
            '
            '“But even {color=#f6d6bd}Helvius{/color} acts behind your back. I know for a fact he was more than willing to break your rules against hard drinks.”' if helvius_about_cidercask_thyrsus and not orentius_argument_locals_helviusbreaksrules:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But even {color=#f6d6bd}Helvius{/color} acts behind your back. I know for a fact he was more than willing to break your rules against hard drinks.”')
                $ orentius_argument_locals_helviusbreaksrules = 1
                if orentius_argument_locals_helviusiscruel:
                    $ orentius_arguments += 1
                $ custom1 = "You explain briefly what happened, and while his eyes are disappointed, his voice sounds more resigned than angry. “T’sn’t easy for the youth to find much joy in the bogs, s’pecially now, when we see no bards, or acrobats. We ought not to drink,” he says to himself, “ba we all make mistakes.”"
                jump whitemarshesorentiusaboutlocals02
            '“I saw how {color=#f6d6bd}Helvius{/color} treats the awoken shells. He’s cruel, sadistic.”' if helvius_cruel and not orentius_argument_locals_helviusiscruel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw how {color=#f6d6bd}Helvius{/color} treats the awoken shells. He’s cruel, sadistic.”')
                $ orentius_argument_locals_helviusiscruel = 1
                if orentius_argument_locals_helviusbreaksrules:
                    $ orentius_arguments += 1
                $ custom1 = "He avoids your look. “You say this much, yet know not a thing of what’s shaped his thoughts, or what’s happened to him over the years. He wounds no one,” his voice grows stronger, “an’ doesn’t deserve accusations, even if...” As he pauses, he strokes the edge of his codex gently. “Some feel worried around him.”"
                jump whitemarshesorentiusaboutlocals02
            '“Some of the locals have already left the village, or plan to do so. Because of your spells.”' if (whitemarshes_pursewoman_coins == 10 and not orentius_argument_locals_trytoleave) or (description_whitemarshes03 and not orentius_argument_locals_trytoleave):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals have already left the village, or plan to do so. Because of your spells.”')
                $ orentius_argument_locals_trytoleave = 1
                $ orentius_arguments += 1
                $ custom1 = "“Then let them, I build no cages, no dungeons. People change homes all the time, t’s good for children.” It’s clear even he doesn’t believe his quiet words."
                jump whitemarshesorentiusaboutlocals02
            '“Your people walk hungry. They struggle.”' if not orentius_argument_locals_hunger:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your people walk hungry. They struggle.”')
                $ orentius_argument_locals_hunger = 1
                $ orentius_friendship -= 2
                $ description_whitemarshes11 = "According to {color=#f6d6bd}Orentius{/color}, the village has gone through terrifying hunger."
                $ questionpreset = "orentius1"
                menu:
                    'He straightens up, leaning against the table with his hands, as if he’s stopping himself from getting to his feet. “How can you throw this at me, warden? Don’t you know our past? I offered my pneuma to the others only {i}after{/i} our children had started dying, with bark and toads in their teeth!”
                    \n\nYou try to add something, but he scoffs and waves for you to forget it. “I won’t listen to what you think f’our people, stranger.”
                    '
                    '(orentius1 set)':
                        pass
            '“{color=#f6d6bd}Thyrsus{/color} already took a stance against you. That’s why you made him an outcast.”' if thyrsus_about_himself3 and not orentius_argument_locals_thyrsusisoutsider:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color} already took a stance against you. That’s why you made him an outcast.”')
                $ orentius_argument_locals_thyrsusisoutsider = 1
                $ orentius_arguments += 1
                $ custom1 = "“It was his own choice,” his raised voice turns into a long cough, then a defeated groan. “Yes, there are fewer of us, ba those who remain aren’t suffering, nor are they held in the bellies of beasts. Those who follow me will be rewarded by Wright’s mercy.”"
                jump whitemarshesorentiusaboutlocals02
            '“Maybe you’re right.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you’re right.”')
                $ questionpreset = "orentius1"
                menu:
                    'His deep breath betrays his relief.
                    '
                    '(orentius1 set)':
                        pass

    label whitemarshesorentiusaboutlocals02:
        menu:
            '[custom1]
            '
            '“Even {color=#f6d6bd}Helvius{/color} acts behind your back. I know for a fact he was more than willing to break your rules against hard drinks.”' if helvius_about_cidercask_thyrsus and not orentius_argument_locals_helviusbreaksrules:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Even {color=#f6d6bd}Helvius{/color} acts behind your back. I know for a fact he was more than willing to break your rules against hard drinks.”')
                $ orentius_argument_locals_helviusbreaksrules = 1
                if orentius_argument_locals_helviusiscruel:
                    $ orentius_arguments += 1
                $ custom1 = "You explain briefly what happened, and while his eyes are disappointed, his voice sounds more resigned than angry. “T’sn’t easy for the youth to find much joy in the bogs, s’pecially now, when we see no bards, or acrobats. We ought not to drink,” he says to himself, “ba we all make mistakes.”"
                jump whitemarshesorentiusaboutlocals02
            '“I saw how {color=#f6d6bd}Helvius{/color} treats the awoken shells. He’s cruel, sadistic.”' if helvius_cruel and not orentius_argument_locals_helviusiscruel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw how {color=#f6d6bd}Helvius{/color} treats the awoken shells. He’s cruel, sadistic.”')
                $ orentius_argument_locals_helviusiscruel = 1
                if orentius_argument_locals_helviusbreaksrules:
                    $ orentius_arguments += 1
                $ custom1 = "He avoids your look. “You say this much, yet know not a thing of what’s shaped his thoughts, or what’s happened to him over the years. He wounds no one,” his voice grows stronger, “an’ doesn’t deserve accusations, even if...” As he pauses, he strokes the edge of his codex gently. “Some feel worried around him.”"
                jump whitemarshesorentiusaboutlocals02
            '“Some of the locals already left the village, or plan to do so. Because of your spells.”' if (whitemarshes_pursewoman_coins == 10 and not orentius_argument_locals_trytoleave) or (description_whitemarshes03 and not orentius_argument_locals_trytoleave):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals already left the village, or plan to do so. Because of your spells.”')
                $ orentius_argument_locals_trytoleave = 1
                $ orentius_arguments += 1
                $ custom1 = "“Then let them, I build no cages, no dungeons. People change homes all the time, t’s good for children.” It’s clear even he doesn’t believe his quiet words."
                jump whitemarshesorentiusaboutlocals02
            '“Your people walk hungry. They struggle.”' if not orentius_argument_locals_hunger:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your people walk hungry. They struggle.”')
                $ orentius_argument_locals_hunger = 1
                $ orentius_friendship -= 2
                $ description_whitemarshes11 = "According to {color=#f6d6bd}Orentius{/color}, the village has gone through terrifying hunger."
                $ questionpreset = "orentius1"
                menu:
                    'He straightens up, leaning against the table with his hands, as if he’s stopping himself from getting to his feet. “How can you throw this at me, warden? Don’t you know our past? I offered my pneuma to the others only {i}after{/i} our children had started dying, with bark and toads in their teeth!”
                    \n\nYou try to add something, but he scoffs and waves for you to forget it. “I won’t listen to what you think f’our people, stranger.”
                    '
                    '(orentius1 set)':
                        pass
            '“{color=#f6d6bd}Thyrsus{/color} already took a stance against you. That’s why you made him an outcast.”' if thyrsus_about_himself3 and not orentius_argument_locals_thyrsusisoutsider:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color} already took a stance against you. That’s why you made him an outcast.”')
                $ orentius_argument_locals_thyrsusisoutsider = 1
                $ orentius_arguments += 1
                $ custom1 = "“It was his own choice,” his raised voice turns into a long cough, then a defeated groan. “Yes, there are fewer of us, ba those who remain aren’t suffering, nor are they held in the bellies of beasts. Those who follow me will be rewarded by Wright’s mercy.”"
                jump whitemarshesorentiusaboutlocals02
            'I change the topic.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic.')
                $ questionpreset = "orentius1"
                menu:
                    'He touches the tip of the candle, making the tiny puddle of wax release the suffocated wick.
                    '
                    '(orentius1 set)':
                        pass

label whitemarshesorentiusaboutempathyALL:
    label whitemarshesorentiusaboutempathy01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may have good reasons to do what you’re doing...”')
        $ orentius_argument_empathy = 1
        if appearance_charisma:
            $ orentius_argument_empathy_appearancepoints + 1
        if item_wingedhourglass_worn:
            $ orentius_argument_empathy_appearancepoints + 1
        menu:
            'He squints his eyes, sizing you up. “Ba?”
            '
            '“...But you can still turn around from this path. Forget the past, start anew.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...But you can still turn around from this path. Forget the past, start anew.”')
                $ orentius_argument_empathy_appearancepoints += 2
                $ description_whitemarshes17 = "The locals feel threatened and may attempt to completely seperate themselves from the rest of the peninsula."
                $ custom1 = "He looks at you in silence, and you can’t decide which eye you should look at. “We aren’t safe yet, an’ as long’s the roads connect us to our {i}neighbors{/i}, we may never be. You can’t grasp our decisions, what we went through. You’re a child taught to ride a horse, to fight and kill, to carry out the will of the masters. Not to overcome the death of your tribe.”"
                jump whitemarshesorentiusaboutempathy02
            '“...But you’re reaching the point of no forgiveness. Stop, before someone stops you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...But you’re reaching the point of no forgiveness. Stop, before someone stops you.”')
                $ orentius_argument_empathy_appearancepoints += 0
                $ custom1 = "“You, mayhap?” He responds pugnaciously. “By what right? Who invited you to this land, or asked you for guidance? You think a child taught to ride a horse, to fight and kill, to carry out the will of the masters, wad grasp our choices?”"
                jump whitemarshesorentiusaboutempathy02
            '“...But try to see this situation from the perspective of the other tribes. They’re afraid.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...But try to see this situation from the perspective of the other tribes. They’re afraid.”')
                $ orentius_argument_empathy_appearancepoints += 0
                $ custom1 = "“Let them be. Why would we bend our paths under their will, when they were the first ones to cast us aside?” He raises his voice and fists. “What makes you believe you’re one to guide our village? You think a child taught to ride a horse, to fight and kill, to carry out the will of the masters, wad grasp our choices?”"
                jump whitemarshesorentiusaboutempathy02
            '“...But I have faith you’ll find a better path forward. With me around, the peninsula is no longer hopeless.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...But I have faith you’ll find a better path forward. With me around, the peninsula is no longer hopeless.”')
                $ orentius_argument_empathy_appearancepoints += 1
                $ custom1 = "His chuckle sounds like steps through shallow bogs. “You trust your judgment so much? Even if your heart is kind, you aren’t one f’us, you can’t grasp our choices. You’re a child taught to ride a horse, to fight and kill, to carry out the will of the masters. Not to overcome the death of your tribe.”"
                jump whitemarshesorentiusaboutempathy02
            '“...But the merchants and officials of {color=#f6d6bd}Hovlavan{/color} are interested in the peninsula. If they come here, your people will face persecution.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...But the merchants and officials of {color=#f6d6bd}Hovlavan{/color} are interested in the peninsula. If they come here, your people will face persecution.”')
                $ orentius_argument_empathy_appearancepoints -= 1
                $ custom1 = "“Then make them sit in their towers, so they can eat from bronze plates an’ bathe in perfumes made from the blood of the Southerners,” he speaks faster, and has to wipe spittle from the edge of his lips. “Neither you nor they can imagine what we went through. You think {i}you{/i}, a child taught to ride a horse, to fight and kill, to carry out the will of the masters, wad grasp our choices?”"
                jump whitemarshesorentius03

    label whitemarshesorentiusaboutempathy02:
        if orentius_argument_empathy_appearancepoints >= 2:
            $ orentius_friendship += 1
        elif orentius_argument_empathy_appearancepoints <= 0:
            $ orentius_friendship -= 1
        menu:
            '[custom1]
            '
            '“You may be right, but before I came here, I did my best to learn about your past struggles. The days of hunger, the way {color=#f6d6bd}Howler’s{/color} took away your timber trade. I {i}want{/i} to understand your situation.”' if description_whitemarshes05 and description_whitemarshes11:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right, but before I came here, I did my best to learn about your past struggles. The days of hunger, the way {color=#f6d6bd}Howler’s{/color} took away your timber trade. I {i}want{/i} to understand your situation.”')
                $ orentius_arguments += 1
                $ orentius_friendship += 1
                $ custom1 = "He looks at you with an open mouth, until, finding no response, his eyes and shoulders soften. His stained robe looks more like a grain sack. “You leave me speechless, {i}cityfolk{/i}. Your ears are open. I hope you’ll forgive my grumpiness.”"
            '{image=d6} (lie) “You wouldn’t believe the struggles I’ve faced. Yes, I was lucky to be supported by kind-hearted people, but you aren’t the only scarred soul.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} (lie) “You wouldn’t believe the struggles I’ve faced. Yes, I was lucky to be supported by kind-hearted people, but you aren’t the only scarred soul.”')
                if (pc_lies+orentius_friendship) >= 16:
                    $ orentius_arguments += 1
                    $ pc_lies += 1
                    $ custom1 = "He looks at you with an open mouth, until, finding no response, his eyes and shoulders soften. His stained robe looks more like a grain sack. “My words were cruel, {i}cityfolk{/i}. I hope you’ll forgive my grumpiness.”"
                    jump whitemarshesorentiusaboutempathy03
                else:
                    $ orentius_arguments -= 1
                    $ pc_lies += 1
                    $ custom1 = "He gestures for you to shut it, and raises his voice. “An’ how am I to believe a cityfolk? You think I’ve no past with the lies an’ promises f’the officials, even from before the war? Your arrival is not a thing more than a threat, for you’re from a dif’rent world, {i}judge{/i}. Our tongues may share sounds, ba are just echoes of each other.”\n\nHis shell may be paler than that of a merchant’s child, but he keeps his head high."
                    jump whitemarshesorentiusaboutempathy03
            '“Do you really think the city experienced no hardships of its own?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really think the city experienced no hardships of its own?”')
                $ orentius_arguments -= 1
                $ custom1 = "“I feel for the dockers caught by corsairs, for farmers who moved behind the walls after losing their fields,” he accompanies his rising voice with a confident gaze. “Ba why wad I pity the officials an’ their soldiers, the traders an’ their stolen goods? The days of restitution wad happen sooner or later. Our emperors wanted the {i}barbarians’{/i} iron an’ now it’s stuck in their throats.”\n\nHis shell may be paler than that of a merchant’s child, but he keeps his head high."
                jump whitemarshesorentiusaboutempathy03
            '“You may be right, but I {i}am{/i} willing to learn about your past before I make any judgment.”' if not description_whitemarshes05 or not description_whitemarshes11:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right, but I {i}am{/i} willing to learn about your past before I make any judgment.”')
                $ custom1 = "His shoulders soften, making his stained robe look more like a grain sack, and his eyes grow melancholic. “You come as a judge, yet want me to believe you’re here to {i}learn{/i}? Haven’t you heard how our days of selling wood have ended? Or how we ate bark an’ carrion, if we found them at all? Your soul is hard to read, cityfolk. You’re ba a stranger.”"
                jump whitemarshesorentiusaboutempathy03
            'I scowl at him, but say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scowl at him, but say nothing.')
                $ custom1 = "He looks at your lips, then scoffs and adjusts his stained robe. His shell may be paler than that of a merchant’s child, but he keeps his head high."
                jump whitemarshesorentiusaboutempathy03

    label whitemarshesorentiusaboutempathy03:
        $ questionpreset = "orentius1"
        menu:
            '[custom1]
            '
            '(orentius1 set)':
                pass

label whitemarshesorentiusabouttrust01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may be pushing this too far... “Can’t you see I’m trustworthy? I don’t wish you harm.”')
    $ orentius_argument_trust = 1
    if whitemarshes_attacked:
        $ orentius_arguments -= 1
        $ questionpreset = "orentius1"
        menu:
            '“An’ you want me to believe that, while at this very moment you’re raiding my home with your band? You must think...” His bewildered voice is interrupted by a weak cough, which leaves droplets of blood on his hand. Distracted, he wipes his hand on his robe, mixing the blood with dried ink.
            '
            '(orentius1 set)':
                pass
    elif orentius_friendship <= 0:
        $ orentius_arguments -= 1
        $ questionpreset = "orentius1"
        menu:
            '“An’ you want me to believe that, after all the things you told me? You must think I’m...” His bewildered voice is interrupted by a weak cough, which leaves droplets of blood on his hand. Distracted, he wipes his hand on his robe, mixing the blood with dried ink.
            '
            '(orentius1 set)':
                pass
    elif orentius_friendship < 5:
        $ questionpreset = "orentius1"
        menu:
            '“I can’t, an’ I still don’t understand you, warden. You came here...” His hesitant voice is interrupted by a weak cough, which leaves droplets of blood on his hand. Distracted, he wipes his hand on his robe, mixing the blood with dried ink.
            '
            '(orentius1 set)':
                pass
    else:
        $ orentius_arguments += 1
        $ questionpreset = "orentius1"
        menu:
            'He squints his eyes, but also gives you a warm smile. “I can, warden. I may not agree with some things you said...” His gentle voice is interrupted by a weak cough, which leaves droplets of blood on his hand. Distracted, he wipes his hand on his robe, mixing the blood with dried ink.
            '
            '(orentius1 set)':
                pass

label whitemarshesorentiusafterdispute01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess we’re done here.”')
    if orentius_arguments >= orentius_arguments_needed:
        jump whitemarshesorentiusafterdisputesuccess01
    else:
        jump whitemarshesorentiusafterdisputefail01

label whitemarshesorentiusafterdisputesuccess01:
    $ quarters += 1
    menu:
        'He spares you an absent glance, then turns around, steps away from the table, and falls on his knees. The cabin is so tiny he can lean his hands against the wall.
        \n\n“Why do you let me hear this voice again?” You think about a response, then realize it’s not you who’s currently being addressed. “I carry all the answers you taught me, yet I’m so torn! I begged you to give me a steady hand, ba even now I’m lost, burnt by the things I asked you about!”
        '
        'I lower my head.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lower my head.')
            if pc_religion == 'fellowship' or pc_religion == 'theunitedchurch' or pc_religion == 'ordersoftruth':
                $ pc_faithpoints += 1
            jump whitemarshesorentiusafterdisputesuccess02
        'I let him finish in peace.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let him finish in peace.')
            jump whitemarshesorentiusafterdisputesuccess02
        'I give him a pat on the back.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give him a pat on the back.')
            label whitemarshesorentiusafterdisputesuccess02:
                $ quarters = 95
                menu:
                    'His exhaustingly long prayer gets harder to understand the longer it goes on. The priest’s accent gets thicker, while at the same time he adds more and more words from Adir’s Tongue, and mentions names and events you’ve never heard of before, as if his worries need a lifetime to unravel. You may not convince the man to trust you, but you’ve awoken his long-buried fears.
                    \n\nAfter what feels like an hour, the sobbing, snotty man uses the bench to support his sore legs. He stands up, and approaches the door. “Come, warden. Time to fix this, all f’this.”
                    '
                    '“Thank you, {color=#f6d6bd}Orentius{/color}.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you, {color=#f6d6bd}Orentius{/color}.”')
                        jump whitemarshesorentiusafterdisputesuccess03
                    '“You’re doing the right thing.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re doing the right thing.”')
                        jump whitemarshesorentiusafterdisputesuccess03
                    'I straighten up proudly.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I straighten up proudly.')
                        label whitemarshesorentiusafterdisputesuccess03:
                            show areapicture whitemarshes01night at basicfade
                            if thyrsus_orentius_helped:
                                menu:
                                    'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. While both the stairs and the “pond” are surrounded by the dark figures who brought you here, the news has already spread. The other locals, most of them still wearing nightwears, are gathered with candles and lanterns, fearfully observing the building.
                                    \n\n{color=#f6d6bd}The prophet{/color}, who needs to lean against a walking stick, raises his free hand. The candle light touches his back, but his exhausted face is covered by darkness.
                                    \n\n“I was wrong, all this time,” he utters. “We need to go back.”
                                    \n\nThe silence follows, then from all directions bursts the mixture of relieved gasps, resentful shouts, and demands to explain what’s going on. {color=#f6d6bd}Orentius{/color} walks down the stairs, while {color=#f6d6bd}Thyrsus{/color} gestures for you to get closer. He leads you away from the commotion, making sure the crowd keeps its distance.
                                    '
                                    '“Any troubles?”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any troubles?”')
                                        menu:
                                            '“Hm? Nah, we’re fine, the guards woke up to no weapons, your beast’s safe,” lost in his thoughts, he adds nothing more.
                                            \n\nYou end up back at the shed, with your belongings intact. “Don’t step outside before dawn,” his sad eyes contrast the gentle smile. “We may’ve a rough few hours ahead of us. We’ll guard the building, ba don’t put more troubles on our backs.”
                                            \n\nWithout waiting for your response, he joins his hooded companions. Because of the loud gathering, you can’t hear what they’re talking about.
                                            '
                                            'Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.')
                                                $ whitemarshes_nomoreundeadfirstsleepdescription = 1
                                                $ sleep_destination = "whitemarshesaftersleep"
                                                jump sleeping
                                    'We walk in silence.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We walk in silence.')
                                        menu:
                                            'You end up back at the shed, with your belongings intact. “Good job, ba we now have to do our part,” his sad eyes contrast his gentle smile. “Don’t step outside before dawn. We may’ve a rough few hours ahead of us. We’ll guard the building, don’t worry.”
                                            \n\nWithout waiting for your response, he joins his hooded companions. Because of the loud gathering, you can’t hear what they’re talking about.
                                            '
                                            'Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.')
                                                $ whitemarshes_nomoreundeadfirstsleepdescription = 1
                                                $ sleep_destination = "whitemarshesaftersleep"
                                                jump sleeping
                            elif helvius_orentius_helped:
                                menu:
                                    'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. The small crowd of villagers still surrounds the “pond”, fearfully observing the building from above candles and lanterns.
                                    \n\n{color=#f6d6bd}The prophet{/color}, who needs to lean against a walking stick, raises his free hand. The candle light touches his back, but his exhausted face is covered by darkness.
                                    \n\n“I was wrong, all this time,” he utters. “We need to go back.”
                                    \n\nThe silence, disturbed by working undead, turns into a mixture of relieved gasps, resentful shouts, and demands to explain what’s going on. {color=#f6d6bd}Orentius{/color} walks down the stairs, while {color=#f6d6bd}Helvius{/color} moves by him, grabs your arm, and pushes you into a group of armed guards. They lead you away from the commotion, toward your mount.
                                    '
                                    '“Are you going to make me ride during the night?”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you going to make me ride during the night?”')
                                        menu:
                                            '“Just grab what’s yours,” the woman who previously took away your dagger speaks harshly. “You’ll spend the night in a shed.”
                                            \n\nYou pick up your belongings, making sure your axe is still in a sack, then follow the group further. They give you no orders, and answer no questions - once you cross the threshold, they leave you to yourself, joining the growing gathering at the yard. Seems like no one will get good sleep tonight.
                                            '
                                            'Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.')
                                                $ whitemarshes_nomoreundeadfirstsleepdescription = 1
                                                $ sleep_destination = "whitemarshesaftersleep"
                                                jump sleeping
                                    'We walk in silence.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We walk in silence.')
                                        menu:
                                            'The woman who previously took away your dagger sounds exhausted, and reaches for the sack containing your axe. “You’ll spend the night in a shed,” she instructs, and so you pick up your belongings. The guards are tense, and keenly observe the growing crowd. Seems like no one will get good sleep tonight.
                                            '
                                            'Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.')
                                                $ whitemarshes_nomoreundeadfirstsleepdescription = 1
                                                $ sleep_destination = "whitemarshesaftersleep"
                                                jump sleeping
                            elif whitemarshes_attacked:
                                jump whitemarshesorentiusafterdisputesuccess03attack01

label whitemarshesorentiusafterdisputesuccess03attackALL:
    label whitemarshesorentiusafterdisputesuccess03attack01:
        menu:
            'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. Your allies are still safeguarding the building, while the terrified and exhausted villagers, sparsely lit up by candles and torches, are surrounding the place so tightly that many of them have their feet in the chilling water.
            \n\n{color=#f6d6bd}The prophet{/color}, who needs to lean against a walking stick, raises his free hand. The candle light touches his back, but his absent face is covered by darkness.
            \n\n“I was wrong, all this time,” he utters. “We need to go back.”
            \n\nThe silence turns into a mixture of resentful shouts and weeping. {color=#f6d6bd}The elder{/color} walks down the stairs, rejecting the helping hands of {color=#f6d6bd}Thais’{/color} men, heading straight to {color=#f6d6bd}Helvius{/color} and his crew. Soon after, you join your band, who, still with weapons at hand, keep the locals at a distance. There are only a few hostages left, even though you see no signs of bloodshed.
            '
            '“He’ll convince the others to give up on necromancy. We’re done here.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’ll convince the others to give up on necromancy. We’re done here.”')
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ custom2 = "The group from {color=#f6d6bd}Gale Rocks{/color}, keep to themselves, scowling at the others, but saying nothing."
                else:
                    $ custom2 = ""
                if whitemarshes_attack_companion_bandits:
                    $ custom3 = "{color=#f6d6bd}Glaucia{/color} lingers behind, keeping her eyes on {color=#f6d6bd}the crying priest{/color}. With a hateful grimace, she spins her sickle sword, as if she’s but a moment of weakness away from dashing through the barrier of flesh that separates her from him.\n\n"
                else:
                    $ custom3 = ""
                menu:
                    'The fighters let out relieved sighs and chuckles, leading you to the exit - the braver villagers also follow, all too eager to close the gate again. [custom3]Before you leave the village, you notice that the guards from {color=#f6d6bd}Howler’s{/color} still haven’t dropped the weapons taken from the locals, and carry large, filled sacks you haven’t seen before. [custom1][custom2]
                    '
                    'I should have expected this. I say nothing.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have expected this. I say nothing.')
                        jump whitemarshesorentiusafterdisputesuccess03attack01a
                    'It’s not the right time to get into an argument. We need to look strong.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not the right time to get into an argument. We need to look strong.')
                        label whitemarshesorentiusafterdisputesuccess03attack01a:
                            show areapicture bogcrossroadstowhitemarshes at basicfade
                            if whitemarshes_attack_companion_galerocks:
                                $ custom2 = "{color=#f6d6bd}Tatius{/color} tells them to shut it - “you’ll spook all them beasts.”"
                            else:
                                $ custom2 = ""
                            menu:
                                'The turmoil no longer works in your favor. The locals hold more tools, many of them large enough to break a human skull, and some of them found their gambesons and bows. You leave before they fully regroup.
                                \n\nYou spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows she found in one of the houses, together with a pretty mug made of an auroch’s horn.[custom2]
                                '
                                'Seems like I’ve been played after all.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                    jump whitemarshesorentiusafterdisputesuccess03attack02
                                'Whatever I tried to accomplish... I’m now a pillager.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                    jump whitemarshesorentiusafterdisputesuccess03attack02
                                'Such are the rules of war.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Such are the rules of war.')
                                    jump whitemarshesorentiusafterdisputesuccess03attack02
                    'I point at the loot. “What’s going on here?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point at the loot. “What’s going on here?”')
                        if whitemarshes_attack_companion_pelt:
                            $ custom1 = "A hunter clears his throat. “I mean, we ain’t leaving empty-handed. We grabbed no seeds, no food, they’ll be fine.”\n\nA guard looks at you like you’re an idiot. “{color=#f6d6bd}Thais{/color} let us. Let’s move.”"
                        else:
                            $ custom1 = "A guard looks at you like you’re an idiot. “Just the spoils. {color=#f6d6bd}Thais{/color} told us what we need. Ne much. Let’s move.”"
                        menu:
                            '[custom1]
                            '
                            '“No one discussed this with me.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No one discussed this with me.”')
                                if whitemarshes_attack_companion_bandits:
                                    $ custom1 = "She shrugs. “So? There was nae need.”\n\nOne of {color=#f6d6bd}Glaucia’s{/color} men shifts from one foot to the other. “Time to scat, right? We’ve no time.”"
                                else:
                                    $ custom1 = "She shrugs. “So? There was nae need.”"
                                menu:
                                    '[custom1]
                                    '
                                    '“Fine. You deserve it, I guess.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                        $ howlersdell_reputation += 1
                                        if whitemarshes_attack_companion_pelt:
                                            $ iason_friendship += 1
                                        if whitemarshes_attack_companion_galerocks:
                                            $ galerocks_reputation -= 1
                                        if whitemarshes_attack_companion_bandits:
                                            $ glaucia_friendship += 1
                                        jump whitemarshesorentiusafterdisputesuccess03attack01a
                                    '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                        jump whitemarshesorentiusafterdisputesuccess03attack01b
                            '“Fine. You deserve it, I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                $ howlersdell_reputation += 1
                                if whitemarshes_attack_companion_pelt:
                                    $ iason_friendship += 1
                                if whitemarshes_attack_companion_galerocks:
                                    $ galerocks_reputation -= 1
                                if whitemarshes_attack_companion_bandits:
                                    $ glaucia_friendship += 1
                                jump whitemarshesorentiusafterdisputesuccess03attack01a
                            '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                label whitemarshesorentiusafterdisputesuccess03attack01b:
                                    $ howlersdell_reputation -= 1
                                    if whitemarshes_attack_companion_pelt:
                                        $ iason_friendship -= 1
                                    if whitemarshes_attack_companion_galerocks:
                                        $ galerocks_reputation += 1
                                    if whitemarshes_attack_companion_bandits:
                                        $ glaucia_friendship -= 1
                                    if whitemarshes_attack_companion_bandits:
                                        $ pc_hp = limit_pc_hp(pc_hp-2)
                                        show minus2hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                        if whitemarshes_attack_companion_galerocks:
                                            $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement,"
                                        else:
                                            $ custom2 = "Your allies frown, either reaching for their weapons, or raising them,"
                                        $ whitemarshes_attack_glauciaattackedpc = 1
                                        menu:
                                            '[custom2] but you then hear a loud “fuck this” behind your back. Right when you recognize {color=#f6d6bd}Glaucia’s{/color} voice, darkness covers your eyes.
                                            '
                                            'Unconscious, I fall on the ground.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Unconscious, I fall on the ground.')
                                                jump whitemarshesorentiusafterdisputesuccess03attack02alt
                                    else:
                                        show areapicture bogcrossroadstowhitemarshes at basicfade
                                        if whitemarshes_attack_companion_galerocks:
                                            $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement, but the others frown, either reaching for their weapons, or raising them."
                                        else:
                                            $ custom2 = "Your allies frown, either reaching for their weapons, or raising them."
                                        menu:
                                            '[custom2] The tense few breaths are quickly interrupted - the turmoil no longer works in your favor. The locals hold more tools, many of them large enough to break a human skull, and some of them found their gambesons and bows. You leave before they fully regroup, with you no longer being the leader.
                                            \n\nYou spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows she found in one of the houses, together with a pretty mug made of an auroch’s horn.
                                            '
                                            'Seems like I’ve been played after all.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                                jump whitemarshesorentiusafterdisputesuccess03attack02
                                            'Whatever I tried to accomplish... I’m now a pillager.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                                jump whitemarshesorentiusafterdisputesuccess03attack02

label whitemarshesorentiusafterdisputefail01:
    if orentius_arguments >= (orentius_arguments_needed/2):
        $ custom1 = "He gives you a cold look. “Good. I’ve listened to you, ba I won’t be threatened, an’ I won’t doubt Wright’s guidance again. My home doesn’t need cityfolk. Leave, an’ never come back.”"
    else:
        $ custom1 = "He gives you a cold look. “You told me not a thing worth hearing, as was to be expected from a cityfolk. Leave, an’ never come back.”"
    menu:
        '[custom1]
        \n\nHe runs his fingers over the hourglass, then taps the open pages of the codex, drawing his attention away from you. You reach for the door.
        '
        'I think about the dagger in my boot.' if orentius_dagger and not whitemarshes_attacked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the dagger in my boot.')
            menu:
                'The man’s neck is revealed. All you need is a confident grapple and a quick cut.
                '
                'I can’t do this. I walk away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t do this. I walk away.')
                    jump whitemarshesorentiusafterdispute02orentius_spared
                'I do it fast, not giving him time to realize what’s happening.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do it fast, not giving him time to realize what’s happening.')
                    jump whitemarshesorentiusafterdispute02orentiuskilled
                '“Forgive me. You leave me no other choice.” I murder the priest.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forgive me. You leave me no other choice.” I murder the priest.')
                    jump whitemarshesorentiusafterdispute02orentiuskilled
        'I reach for my axe.' if orentius_dagger and whitemarshes_attacked:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for my axe.')
            menu:
                'The man’s neck is revealed. All you need is a strong blow.
                '
                'I can’t do this. I walk away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t do this. I walk away.')
                    jump whitemarshesorentiusafterdispute02orentius_spared
                'I do it fast, not giving him time to realize what’s happening.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do it fast, not giving him time to realize what’s happening.')
                    jump whitemarshesorentiusafterdispute02orentiuskilled
                '“Forgive me. You leave me no other choice.” I murder the priest.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forgive me. You leave me no other choice.” I murder the priest.')
                    jump whitemarshesorentiusafterdispute02orentiuskilled
        'I have no blade with me. Attacking a sorcerer would be too risky. (disabled)' if not orentius_dagger:
            pass
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump whitemarshesorentiusafterdispute02orentius_spared

label whitemarshesorentiusafterdispute02orentius_spared:
    show areapicture whitemarshes01night at basicfade
    $ quarters = 95
    if thyrsus_orentius_helped:
        $ orentius_spared = 1
        $ thyrsus_friendship -= 1
        $ whitemarshes_reputation -= 2
        menu:
            'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. While both the stairs and the “pond” are surrounded by your allies, the news has already spread. The other locals, most of them still wearing nightwears, are gathered with candles and lanterns, fearfully observing the building.
            \n\n{color=#f6d6bd}Thyrsus{/color} is the first one to approach you. Seeing how you shake your head, his shoulders drop, and he grasps the amulets on his wrists - the only ones that were quiet enough to take here. “Well, you tried. Let’s get you back to the shelter.”
            \n\nAs you climb down, the crowd hits you with mocking chuckles, relieved sighs, and worried questions. The angry looks of {color=#f6d6bd}Helvius{/color} and his guards turn into scornful insults, and as they receive the stolen weapons from your allies, {color=#f6d6bd}the mayor{/color} hits you with his shoulder as he strides to the cabin.
            '
            '“Any troubles?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any troubles?”')
                $ quest_orentius = 3
                $ renpy.notify("Quest completed: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
                $ quest_orentius_thyrsus_description04 = "Not only did I fail at getting rid of the necromancers, the villagers will no longer put any trust in me. This matter is now out of my hands."
                menu:
                    '“Hm? Nah, we’re fine, the guards woke up to no blades, your beast’s safe,” lost in his thoughts, he adds nothing more.
                    \n\nYou end up back at the shed, with your belongings intact. “Don’t step outside before dawn,” his sad eyes avoid you. “Some souls here may get weird ideas.”
                    \n\nWithout waiting for your response, he joins his hooded companions. Because of the loud gathering, you can’t hear what they’re talking about.
                    '
                    'Before I go to sleep, I block the door with a barrel and make sure my blade is at hand.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I make sure my blade is at hand.')
                        $ sleep_destination = "whitemarshesaftersleep"
                        jump sleeping
            '“I’m sorry.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry.”')
                $ quest_orentius = 3
                $ renpy.notify("Quest completed: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
                $ quest_orentius_thyrsus_description04 = "Not only did I fail at getting rid of the necromancers, the villagers will no longer put any trust in me. This matter is now out of my hands."
                menu:
                    '“Hm? Well, we canna do anything now. We did our best,” lost in his thoughts, he adds nothing more.
                    \n\nYou end up back at the shed, with your belongings intact. “Don’t step outside before dawn,” his sad eyes avoid you. “Some souls here may get weird ideas.”
                    \n\nWithout waiting for your response, he joins his hooded companions. Because of the loud gathering, you can’t hear what they’re talking about.
                    '
                    'Before I go to sleep, I make sure my blade is at hand.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I make sure my blade is at hand.')
                        $ sleep_destination = "whitemarshesaftersleep"
                        jump sleeping
    elif helvius_orentius_helped:
        $ orentius_spared = 1
        $ whitemarshes_reputation -= 2
        menu:
            'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. The small crowd of villagers still surrounds the “pond”, though many of them now hold candles and lanterns, fearfully observing the building.
            \n\n{color=#f6d6bd}Helvius{/color} waits for a bit, then goes upstairs, making sure everything is under control. Hearing {color=#f6d6bd}the priest’s{/color} invitation, he gestures for you to go away, and enters the cabin.
            \n\nThe sounds of working undead are quickly accompanied by a mixture of mocking chuckles, relieved sighs, and worried questions. Once you reach the ground, a group of guards leads you away from the commotion, toward your mount.
            '
            '“Are you going to make me ride during the night?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you going to make me ride during the night?”')
                $ quest_orentius = 3
                $ renpy.notify("Quest completed: Orentius, the Necromancer")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
                $ quest_orentius_helvius_description04 = "Not only did I fail at getting rid of the necromancers, the villagers will no longer put any trust in me. This matter is now out of my hands."
                menu:
                    '“Just grab what’s yours,” the woman who previously took away your dagger speaks harshly. “You’ll spend the night in a shed.”
                    \n\nYou pick up your belongings, making sure your axe is still in a sack, then follow the group further. They give you no orders, and answer no questions - once you cross the threshold, they leave you to yourself, joining the gathering at the yard and telling everyone to disband.
                    '
                    'Before I go to sleep, I make sure my blade is at hand.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Before I go to sleep, I make sure my blade is at hand.')
                        $ sleep_destination = "whitemarshesaftersleep"
                        jump sleeping
    elif whitemarshes_attacked:
        jump whitemarshesorentiusafterdisputefail03attack01

label whitemarshesorentiusafterdisputefail03attack01:
    $ whitemarshes_reputation -= 1
    $ thais_friendship -= 1
    $ howlersdell_reputation -= 1
    if whitemarshes_attack_companion_pelt:
        $ iason_friendship -= 1
    if whitemarshes_attack_companion_galerocks:
        $ galerocks_reputation -= 1
    if whitemarshes_attack_companion_bandits:
        $ glaucia_friendship -= 1
    menu:
        'The gust of night wind eases your breath - only now do you realize how much sweat has gathered behind your neck. Your allies are still safeguarding the building, while the terrified and exhausted villagers, sparsely lit up by candles and torches, are surrounding the place so tightly that many of them have their feet in the chilling water.
        \n\nYou notice the puzzled looks of your band. As you shake your head, the silence grows tense - then, the locals sigh with relief, hitting you with mockery and threats, even though their own defenders, together with the mayor, are still gathered in the shed, as defenseless as they are hateful.
        \n\nYou walk downstairs. The turmoil no longer works in your favor. The locals hold more tools, many of them large enough to break a human skull, and some of them found their gambesons and bows. Even worse, there are only a few hostages left, even though you see no signs of bloodshed.
        \n\nYour allies, still with weapons at hand, keep the others away from you. You leave before they fully regroup.
        '
        '“I guess we’re done here. We won’t accomplish much, unless we want to butcher the village, and leave most of us to rot in the mud.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess we’re done here. We won’t accomplish much, unless we want to butcher the village, and leave most of us to rot in the mud.”')
            if whitemarshes_attack_companion_bandits:
                $ glaucia_friendship -= 1
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = " “Well, we tried,” shrugs one of the hunters."
                    $ custom4 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                    $ custom4 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ galerocks_reputation += 1
                    $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement, while the others are torn. "
                    $ custom5 = "The group from the north, who keep to themselves, scowl at the others, but say nothing."
                else:
                    $ custom2 = "Even though you say so, your allies are torn."
                    $ custom5 = ""
                $ custom3 = "\n\n“Our homes will need us,” capitulates a guard from {color=#f6d6bd}Howler’s{/color}, but {color=#f6d6bd}Glaucia{/color} runs her eyes over all of you, spinning her sickle sword.\n\n“You’re all cowards,” her voice makes everyone step away. “We ain’t throwing our families to their doom merely because the warden didn’t talk some old goblin out of turning the North into his slavedom. Step the fuck away,” she dashes toward the cabin, getting to the door with just a couple of steps - her stumpy shell moves as quickly as a youngster’s.\n\nYou hear the surprised calls of your companions, and the fearful shouts of the locals."
                jump whitemarshesorentiusafterdisputefail03glauciakillsorentius01
            else:
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = " “Well, we tried,” shrugs one of the hunters."
                    $ custom4 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                    $ custom4 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ galerocks_reputation += 1
                    $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement, while the others are torn. "
                    $ custom5 = "The group from the north, who keep to themselves, scowl at the others, but say nothing."
                else:
                    $ custom2 = "Even though you say so, your allies are torn."
                    $ custom5 = ""
                menu:
                    '[custom2][custom1]
                    \n\n“Our homes will need us,” capitulates a guard from {color=#f6d6bd}Howler’s{/color}, and the others head to the gate. You notice that your allies still haven’t dropped the weapons taken from the locals, and carry large, filled sacks you haven’t seen before. [custom4][custom5]
                    '
                    'I should have expected this. I say nothing.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have expected this. I say nothing.')
                        jump whitemarshesorentiusafterdisputefail03attack01a
                    'It’s not the right time to get into an argument. We need to look strong.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not the right time to get into an argument. We need to look strong.')
                        jump whitemarshesorentiusafterdisputefail03attack01a
        'I lower my voice. “We could still try to force the locals to give us the priest, and take him away from here.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lower my voice. “We could still try to force the locals to give us the priest, and take him away from here.”')
            if whitemarshes_attack_companion_bandits:
                $ glaucia_friendship += 1
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = " “We ain’t here to die,” mentions one of the hunters."
                    $ custom4 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                    $ custom4 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ galerocks_reputation -= 1
                    $ custom2 = "“You crazy?” The harsh voice of someone from {color=#f6d6bd}Gale Rocks{/color} is close to a shout, while the others are torn."
                    $ custom5 = "The group from the north, who keep to themselves, scowl at the others, but say nothing."
                else:
                    $ custom2 = "Even though you say so, your allies are torn."
                    $ custom5 = ""
                $ custom3 = "\n\n“Let’s rather fight the undead from our own walls,” capitulates a guard from {color=#f6d6bd}Howler’s{/color}, but {color=#f6d6bd}Glaucia{/color} runs her eyes over all of you, spinning her sickle sword.\n\n“Cowards, all of you but the warden,” her voice makes everyone step away. “We ain’t throwing our families to their doom merely because you’re too weak to stop some old goblin before he turns the North into his slavedom. Step the fuck away,” she dashes toward the cabin, getting to the door with just a couple of steps - her stumpy shell moves as quickly as a youngster’s.\n\nYou hear the surprised calls of your companions, and the fearful shouts of the locals."
                jump whitemarshesorentiusafterdisputefail03glauciakillsorentius01
            else:
                if whitemarshes_attack_companion_pelt:
                    $ custom1 = " “We ain’t here to die,” mentions one of the hunters."
                    $ custom4 = "Same goes for the hunters from {color=#f6d6bd}Pelt{/color}. "
                else:
                    $ custom1 = ""
                    $ custom4 = ""
                if whitemarshes_attack_companion_galerocks:
                    $ galerocks_reputation -= 1
                    $ custom2 = "“You crazy?” The harsh voice of someone from {color=#f6d6bd}Gale Rocks{/color} is close to a shout, while the others are torn."
                    $ custom5 = "The group from the north, who keep to themselves, scowl at the others, but say nothing."
                else:
                    $ custom2 = "Even though you say so, your allies are torn."
                    $ custom5 = ""
                menu:
                    '[custom2][custom1]
                    \n\n“Let’s rather fight the undead from our own walls,” capitulates a guard from {color=#f6d6bd}Howler’s{/color}, and the others nod. You head to the gate, and you notice that your allies still haven’t dropped the weapons taken from the locals, and carry large, filled sacks you haven’t seen before. [custom4][custom5]
                    '
                    'I should have expected this. I say nothing.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have expected this. I say nothing.')
                        jump whitemarshesorentiusafterdisputefail03attack01a
                    'It’s not the right time to get into an argument. We need to look strong.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s not the right time to get into an argument. We need to look strong.')
                        label whitemarshesorentiusafterdisputefail03attack01a:
                            show areapicture bogcrossroadstowhitemarshes at basicfade
                            if whitemarshes_attack_companion_galerocks:
                                $ custom2 = "{color=#f6d6bd}Tatius{/color} tells them to shut it - “you’ll spook all them beasts.”"
                            else:
                                $ custom2 = ""
                            menu:
                                'You spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows she found in one of the houses, together with a pretty mug made of an auroch’s horn.[custom2]
                                '
                                'Seems like I’ve been played after all.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                    jump whitemarshesorentiusafterdisputefail03attack02
                                'Whatever I tried to accomplish... I’m now a pillager.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                    jump whitemarshesorentiusafterdisputefail03attack02
                                'Such are the rules of war.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Such are the rules of war.')
                                    jump whitemarshesorentiusafterdisputefail03attack02
                    'I point at the loot. “What’s going on here?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point at the loot. “What’s going on here?”')
                        if whitemarshes_attack_companion_pelt:
                            $ custom1 = "A hunter clears his throat. “I mean, we ain’t leaving empty-handed. We grabbed no seeds, no food, they’ll be fine.”\n\nA guard looks at you like you’re an idiot. “{color=#f6d6bd}Thais{/color} let us. Let’s move.”"
                        else:
                            $ custom1 = "A guard looks at you like you’re an idiot. “Just the spoils. {color=#f6d6bd}Thais{/color} told us what we need. Ne much. Let’s move.”"
                        menu:
                            '[custom1]
                            '
                            '“No one discussed this with me.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No one discussed this with me.”')
                                menu:
                                    '[custom1]
                                    '
                                    '“Fine. You deserve it, I guess.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                        $ howlersdell_reputation += 1
                                        if whitemarshes_attack_companion_pelt:
                                            $ iason_friendship += 1
                                        if whitemarshes_attack_companion_galerocks:
                                            $ galerocks_reputation -= 1
                                        jump whitemarshesorentiusafterdisputefail03attack01a
                                    '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                        jump whitemarshesorentiusafterdisputefail03attack01b
                            '“Fine. You deserve it, I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. You deserve it, I guess.”')
                                $ howlersdell_reputation += 1
                                if whitemarshes_attack_companion_pelt:
                                    $ iason_friendship += 1
                                if whitemarshes_attack_companion_galerocks:
                                    $ galerocks_reputation -= 1
                                jump whitemarshesorentiusafterdisputefail03attack01a
                            '“I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t bring you here for you to plunder. Drop those things where you’re standing and let’s go.”')
                                $ howlersdell_reputation -= 1
                                if whitemarshes_attack_companion_pelt:
                                    $ iason_friendship -= 1
                                if whitemarshes_attack_companion_galerocks:
                                    $ galerocks_reputation += 1
                                label whitemarshesorentiusafterdisputefail03attack01b:
                                    show areapicture bogcrossroadstowhitemarshes at basicfade
                                    if whitemarshes_attack_companion_galerocks:
                                        $ custom2 = "Those from {color=#f6d6bd}Gale Rocks{/color} nod in agreement, but the others frown, either reaching for their weapons, or raising them."
                                    else:
                                        $ custom2 = "Your allies frown, either reaching for their weapons, or raising them."
                                    menu:
                                        '[custom2] After a tense few breaths, you know you’ve no authority over them, and you’re quickly interrupted - the turmoil no longer works in your favor. The locals hold more tools, many of them large enough to break a human skull, and some of them found their gambesons and bows. You leave before they fully regroup.
                                        \n\nYou spend some time in silence, observing the waters of the bog. Then, one member of the crew giggles, and mentions some sort of scuffle he got into with a {i}skinny boy{/i}. Someone brags about the new set of arrows she found in one of the houses, together with a pretty mug made of an auroch’s horn.
                                        '
                                        'Seems like I’ve been played after all.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I’ve been played after all.')
                                            jump whitemarshesorentiusafterdisputefail03attack02
                                        'Whatever I tried to accomplish... I’m now a pillager.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever I tried to accomplish... I’m now a pillager.')
                                            jump whitemarshesorentiusafterdisputefail03attack02

label whitemarshesorentiusafterdisputefail03glauciakillsorentius01:
    stop music fadeout 4.0
    menu:
        '[custom2][custom1][custom3]
        '
        'I order her to stop.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I order her to stop.')
            $ custom1 = "She doesn’t look back - with hatred in every gesture, and zeal reflecting on her blade, she bursts through the door. The prophet doesn’t even yell.\n\nSurrounded by weeping and curses, it takes a few moments for you to notice that not all of the shouts are marked with anger. While some people cry, others run away, deeper into the village."
            jump whitemarshesorentiusafterdisputefail03glauciakillsorentius02
        'I run after her.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run after her.')
            $ custom1 = "You almost catch up to her as she bursts through the door. The prophet doesn’t even yell. With hatred in every gesture, and zeal reflecting on her blade, she cuts off the prophet’s head. His shell lands on the table, spreading the ichor from his neck onto the pages. The corpse still holds the quill in its clenched fist.\n\n{color=#f6d6bd}Glaucia{/color} gives him a look that feels like an eternity. She breathes heavily, but her lower lip shakes in delight. “Finally,” she says to herself, then looks at the ceiling. You can’t hear what she whispers, but it looks to you like “thank you.”\n\nYou notice the many shouts coming from outside - not all of them marked with anger. You step away from the executioner, seeing that while some people cry, others run away, deeper into the village."
            jump whitemarshesorentiusafterdisputefail03glauciakillsorentius02
        'I let it be.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let it be.')
            $ custom1 = "The moments flow by slowly. You observe the terrified eyes of the man’s followers, their open mouths, the way they try to reach the stairs or fall on their knees, locked in prayer. While you hear not a single yell coming from the building, the hatred and determination of {color=#f6d6bd}Glaucia’s{/color} words made it clear that only a miracle can save the prophet.\n\nIt doesn’t come. When the executioner leaves the cabin, her face is blissful, the grip on her bloodied sword confident and strong.\n\nSurrounded by weeping and curses, it takes a few moments for you to notice that not all of the shouts are marked with anger. Some of the people run away, deeper into the village."
            label whitemarshesorentiusafterdisputefail03glauciakillsorentius02:
                if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                    play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
                menu:
                    '[custom1]
                    '
                    '“What’s going on?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s going on?”')
                        jump whitemarshesorentiusafterdisputefail03glauciakillsorentius03
                    'I look around.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                        label whitemarshesorentiusafterdisputefail03glauciakillsorentius03:
                            menu:
                                'In the flickering light of dropped lanterns, a few children and elders are rushing toward the square from a distant alley. The last of them limps, then falls to the ground, pinned by an awoken skeleton. The undead hit the villagers with the fierceness of wolves, even though their mouths make no sounds, cast no threats, and offer no alliance.
                                \n\nToo many things happen at once. The bringers of death come from all directions, charging at the defenseless workers who either flee in panic, or seek their scattered family members and friends. A few of the locals are ready to defend themselves, but not many are brave enough to stand in the way of merciless, ever-hungry shells.
                                \n\nThose of your people who were guarding the imprisoned guards throw them a dagger or two. Being unequipped and disorganized, they won’t be of much use.
                                '
                                '“To the gate, all of you!”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To the gate, all of you!”')
                                    $ custom1 = "“Stay where you are!” The thundering voice of {color=#f6d6bd}Glaucia{/color} makes your band freeze as they look up toward her. Her blade, still red, only adds more confidence to her firm stance. “These witless shitbags have no weapons. Make a tight row, we walk as one. Whoever scats,” she pauses, and looks at you. “I’ll kill them myself.”"
                                    jump whitemarshesorentiusafterdisputefail03glauciakillsorentius04
                                'I stay close to my allies.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay close to my allies.')
                                    $ custom1 = "“Listen up!” The thundering voice of {color=#f6d6bd}Glaucia{/color} makes your band freeze as they look up toward her. Her blade, still red, only adds more confidence to her firm stance. “These witless shitbags have no weapons. Make a tight row, we walk as one and leave as one.”"
                                    label whitemarshesorentiusafterdisputefail03glauciakillsorentius04:
                                        menu:
                                            '[custom1]
                                            \n\nYour band, while varied, puts its trust in her. You form a wall of blades and armor not a moment too soon - the first undead runs straight at you, as dumb as a thrown rock, and is dismembered in the blink of an eye, without so much as a grumble. In this darkness, which only grows deeper as the lights dwindle, you can’t even tell if the creature’s rotten flesh held any blood.
                                            '
                                            'I’ve no other way - I follow her command.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no other way - I follow her command.')
                                                show areapicture whitemarshesforaging01 at basicfade
                                                if whitemarshes_attack_numberofallies >= 3:
                                                    if armor >= 1:
                                                        $ armor = limit_armor(armor-1)
                                                        show minus1armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                                    else:
                                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                                        show minus1hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                                    if not cleanliness_clothes_blood:
                                                        $ cleanliness_clothes_blood = 1
                                                        show minus1appearance at appearancechange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                                                elif whitemarshes_attack_numberofallies == 2:
                                                    if armor >= 4:
                                                        $ armor = limit_armor(armor-1)
                                                        show minus1armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                                    elif armor >= 2:
                                                        $ armor = limit_armor(armor-2)
                                                        show minus2armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                                        if not cleanliness_clothes_torn:
                                                            $ cleanliness_clothes_torn = 1
                                                            show minus1appearance at appearancechange onlayer myoverlay
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                                    elif armor == 1:
                                                        $ armor = limit_armor(armor-1)
                                                        show minus1armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                                        show minus1hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                                        if not cleanliness_clothes_torn:
                                                            $ cleanliness_clothes_torn = 1
                                                            show minus1appearance at appearancechange onlayer myoverlay
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                                    else:
                                                        $ pc_hp = limit_pc_hp(pc_hp-2)
                                                        show minus2hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                                    if not cleanliness_clothes_blood:
                                                        $ cleanliness_clothes_blood = 1
                                                        $ cleanliness = limit_cleanliness(cleanliness-1)
                                                        show minus2appearance at appearancechange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                                    else:
                                                        $ cleanliness = limit_cleanliness(cleanliness-1)
                                                        show minus1appearance at appearancechange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                                                else:
                                                    if armor >= 4:
                                                        $ armor = limit_armor(armor-1)
                                                        show minus1armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                                    elif armor >= 3:
                                                        $ armor = limit_armor(armor-2)
                                                        show minus2armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                                        if not cleanliness_clothes_torn:
                                                            $ cleanliness_clothes_torn = 1
                                                            show minus1appearance at appearancechange onlayer myoverlay
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                                    elif armor == 2:
                                                        $ armor = limit_armor(armor-2)
                                                        show minus2armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                                        show minus1hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                                        if not cleanliness_clothes_torn:
                                                            $ cleanliness_clothes_torn = 1
                                                            show minus1appearance at appearancechange onlayer myoverlay
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                                    elif armor == 1:
                                                        $ armor = limit_armor(armor-1)
                                                        show minus1armor at armorchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                                        $ pc_hp = limit_pc_hp(pc_hp-2)
                                                        show minus2hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                                        if not cleanliness_clothes_torn:
                                                            $ cleanliness_clothes_torn = 1
                                                            show minus1appearance at appearancechange onlayer myoverlay
                                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                                    else:
                                                        $ pc_hp = limit_pc_hp(pc_hp-3)
                                                        show minus3hp at hpchange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                                    if not cleanliness_clothes_blood:
                                                        $ cleanliness_clothes_blood = 1
                                                        $ cleanliness = limit_cleanliness(cleanliness-1)
                                                        show minus2appearance at appearancechange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                                    else:
                                                        $ cleanliness = limit_cleanliness(cleanliness-1)
                                                        show minus1appearance at appearancechange onlayer myoverlay
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                                                if whitemarshes_attack_numberofallies >= 3:
                                                    $ whitemarshes_attack_numberofdead += 1
                                                    $ custom1 = "Thanks to all the allies you’ve gathered, most of you get through in one piece - but once you regroup behind the walls, you realize that a few souls are missing. “They left us to pillage and died alone,” {color=#f6d6bd}Glaucia{/color} states matter-of-factly. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                                                elif whitemarshes_attack_numberofallies == 2:
                                                    $ whitemarshes_attack_numberofdead += 3
                                                    $ custom1 = "A few of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Still, thanks to all the allies you’ve gathered, most of you get through with only slight wounds.\n\nOnce you regroup behind the walls, you realize that a few more souls are missing. “They left us to pillage and died alone,” {color=#f6d6bd}Glaucia{/color} states matter-of-factly. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                                                else:
                                                    $ whitemarshes_attack_numberofdead += 5
                                                    $ custom1 = "Many of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Having only a few guards and the bandits at your side, many of you get through with deep wounds - and once you regroup behind the walls, you realize that a few more souls are missing. “They left us to pillage and died alone,” {color=#f6d6bd}Glaucia{/color} gasps for air. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                                                $ whitemarshes_destroyed = 1
                                                $ whitemarshes_nomoreundead = day
                                                if quest_hiddenpurse == 1:
                                                    $ quest_hiddenpurse = 3
                                                if quest_readtheletter == 1:
                                                    $ quest_readtheletter = 3
                                                menu:
                                                    'Things happen quickly. The gates are just nearby, but the formation is forced to walk sideways, pushing away the attacks and stepping over corpses and abandoned possessions. Not being used to moving as a part of a unit, you’re among those selected to look after the back and sides, cutting through the creatures that arrive from different directions.
                                                    \n\n[custom1]
                                                    \n\nAfter some time, you let yourself take a brief break, exhausted, cold, and covered in blood. You look behind - there’s light and smoke above the place that, until this day, was known as {color=#f6d6bd}White Marshes{/color}.
                                                    '
                                                    'Someone must have dropped a candle on a pile of rugs.':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone must have dropped a candle on a pile of rugs.')
                                                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02
                                                    'That fucking woman.':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- That fucking woman.')
                                                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02
                                                    'Did she just say that my {i}band{/i} was robbing this place?':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Did she just say that my band was robbing this place?')
                                                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02
                                                    '...How could I bring her here?':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...How could I bring her here?')
                                                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02

label whitemarshesorentiusafterdispute02orentiuskilled:
    $ quarters = 95
    stop music fadeout 4.0
    if thyrsus_orentius_helped or helvius_orentius_helped:
        menu:
            'You dash forward, pull the man’s forehead to your chest, cut - and it’s done, as quick as breaking a chicken’s neck. He chokes on his blood as it spreads across his chest and the table, and as his shell twitches, you let it go and step away, not sure if you should look away. After the head smacks against the planks, you hear only your own heartbeat.
            \n\nBut not for long - shouts of fear and pain are coming from outside.
            '
            'I leave the building and look around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building and look around.')
                show areapicture whitemarshes01night at basicfade
                if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                    play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
                if thyrsus_orentius_helped:
                    $ custom1 = "{color=#f6d6bd}Thyrsus{/color} tries to regroup the other conspirators, but they lack both the numbers and the discipline, and the guards aren’t properly equipped. He looks at you, but only for a moment - his poorly lit eyes are as desperate as they are hateful.\n\nThe gates are open, offering retreat to the locals."
                elif helvius_orentius_helped:
                    $ custom1 = "You see {color=#f6d6bd}Helvius{/color} only for a moment, as he spares you a last, hateful glance. He leads his guards away, regrouping slowly, but you can already tell their numbers are too thin to make a real difference."
                menu:
                    'In the flickering light of dropped lanterns, a few children and elders are rushing toward the square from a distant alley. The last of them limps, then falls to the ground, pinned by an awoken skeleton. The undead hit the villagers with the fierceness of wolves, even though their mouths make no sounds, cast no threats, and offer no alliance.
                    \n\nToo many things happen at once. The bringers of death come from all directions, charging at the defenseless workers who either flee in panic, or seek their scattered family members and friends. A few of the locals are ready to defend themselves, but not many are brave enough to stand in the way of merciless, ever-hungry shells.
                    \n\n[custom1]
                    '
                    'I run to {color=#f6d6bd}[horsename]{/color}, stopping only if something attacks me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to {color=#f6d6bd}%s{/color}, stopping only if something attacks me.')
                        if armor >= 4:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        elif armor >= 3:
                            $ armor = limit_armor(armor-2)
                            show minus2armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 2:
                            $ armor = limit_armor(armor-2)
                            show minus2armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                        if not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            show minus2appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                        else:
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        show areapicture whitemarshesforaging01 at basicfade
                        menu:
                            'There’s enough walking prey to shield you. The few clashes are quick and, while painful, you don’t hope to win in the first place - you just run, cutting whatever tries to grab you, jumping over abandoned possessions and dead shells.
                            \n\nYou reach the terrified palfrey in what feels both like an eternity and the blink of an eye. You cut the rope and call for your companion. You run, hoping it will obey, but thankfully the undead have no interest in its flesh.
                            \n\nMany more people run through the fields and even enter the bogs, but you doubt many of them will get through the woodlands alive. They carry no blades, no torches.
                            '
                            'I climb up the saddle. I must get out of the wetlands.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the saddle. I must get out of the wetlands.')
                                $ travel_destination = "bogentrance"
                                $ quarters = 95
                                $ bogentrance_whitemarshes_destroyed = 1
                                jump finaldestinationafterevent
                                label bogentrance_whitemarshes_destroyed01:
                                    $ renpy.force_autosave(take_screenshot=True, block=True)
                                    $ bogentrance_whitemarshes_destroyed = 2
                                    $ can_leave = 0
                                    $ can_rest = 0
                                    $ can_items = 0
                                    $ whitemarshes_destroyed = 1
                                    $ pc_murdered = day
                                    $ vines_perma_closed = 1
                                    $ vines_perma_open = 0
                                    $ whitemarshes_nomoreundead = day
                                    if quest_hiddenpurse == 1:
                                        $ quest_hiddenpurse = 3
                                    if quest_readtheletter == 1:
                                        $ quest_readtheletter = 3
                                    menu:
                                        'After some time, you let yourself take a brief break, exhausted, cold, and covered in blood. You look behind - there’s light and smoke above the place that, until this day, was known as {color=#f6d6bd}White Marshes{/color}.
                                        '
                                        'Someone must have dropped a candle on a pile of rugs.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone must have dropped a candle on a pile of rugs.')
                                            jump bogentrance_whitemarshes_destroyed02
                                        'What a horrible night.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- What a horrible night.')
                                            jump bogentrance_whitemarshes_destroyed02
                                        'I did everything I could.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did everything I could.')
                                            jump bogentrance_whitemarshes_destroyed02
                                        'Fuck this.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Fuck this.')
                                            jump bogentrance_whitemarshes_destroyed02
                                        'I look at my hands. What have I done?':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at my hands. What have I done?')
                                            label bogentrance_whitemarshes_destroyed02:
                                                $ whitemarshes_nomoreundead = (day+1)
                                                $ quest_orentius = 2
                                                $ vines_perma_closed = 1
                                                $ vines_perma_open = 0
                                                $ renpy.notify("Quest completed: Orentius, the Necromancer")
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
                                                if thyrsus_orentius_helped:
                                                    $ quest_orentius_thyrsus_description05 = "I stopped the necromancers... And destroyed the entire village at the same time."
                                                elif helvius_orentius_helped:
                                                    $ quest_orentius_helvius_description05 = "I stopped the necromancers... And destroyed the entire village at the same time."
                                                $ can_leave = 1
                                                $ can_rest = 1
                                                $ can_items = 1
                                                menu:
                                                    'You look away, at the dark woods. The road is quiet.
                                                    '
                                                    'I’ve no time to waste. (disabled)':
                                                        pass
    elif whitemarshes_attacked:
        jump whitemarshesorentiusafterdisputefail03playerkilled01

label whitemarshesorentiusafterdisputefail03playerkilled01:
    menu:
        'You raise your axe, take a step, then a swing - and it’s done. The awkward cut didn’t chop the head off, but broke the man’s spine, stopping in the middle of the neck as it pushed his shell forward. His forehead hits the table loudly. The prophet lets out a painful gurgle, raising his hands slightly - then freezes, now only an empty shell. You hear your own heartbeat.
        \n\nBut not for long - shouts of fear and pain are coming from the outside.
        '
        'I leave the building and look around.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building and look around.')
            show areapicture whitemarshes01night at basicfade
            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
            menu:
                'In the flickering light of dropped lanterns, a few children and elders are rushing toward the square from a distant alley. The last of them limps, then falls to the ground, pinned by an awoken skeleton. The undead hit the villagers with the fierceness of wolves, even though their mouths make no sounds, cast no threats, and offer no alliance.
                \n\nToo many things happen at once. The bringers of death come from all directions, charging at the defenseless workers who either flee in panic, or seek their scattered family members and friends. A few of the locals are ready to defend themselves, but not many are brave enough to stand in the way of merciless, ever-hungry shells.
                \n\nThose of your people who were guarding the imprisoned guards throw them a dagger or two. Being unequipped and disorganized, they won’t be of much use.
                '
                '“To the gate, all of you!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To the gate, all of you!”')
                    show areapicture whitemarshesforaging01 at basicfade
                    if armor >= 4:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    elif armor >= 2:
                        $ armor = limit_armor(armor-2)
                        show minus2armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                        if not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                    elif armor == 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        if not cleanliness_clothes_torn:
                            $ cleanliness_clothes_torn = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-2)
                        show minus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_blood:
                        $ cleanliness_clothes_blood = 1
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus2appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                    else:
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ whitemarshes_attack_numberofdead += 10
                    $ whitemarshes_destroyed = 1
                    $ whitemarshes_nomoreundead = day
                    if quest_hiddenpurse == 1:
                        $ quest_hiddenpurse = 3
                    if quest_readtheletter == 1:
                        $ quest_readtheletter = 3
                    menu:
                        'They don’t wait for your example and run forward, without looking back - after all, the gate is so close. The undead knock down many of your allies, crushing and biting their necks and limbs. The other dead shells and abandoned possessions on the ground makes running through the night even more difficult. Even though you cut a few creatures and suffer only a few painful clashes, you can’t make much of a difference on your own.
                        \n\nYour people regroup, far away from the gate, but there aren’t many of them. More than a half haven’t returned - “the looters are gone as well,” adds one of the fighters, with tears in her eyes. She just lost a sister.
                        \n\n“We need to get out of here,” you order. Some of the warriors hesitate, a few even speak against you, but seeing how the others are already on the move, they have to join them.
                        \n\nAfter some time, you let yourself take a brief break, exhausted, cold, and covered in blood. You look behind - there’s light and smoke above the place that, until this day, was known as {color=#f6d6bd}White Marshes{/color}.
                        '
                        'Someone must have dropped a candle on a pile of rugs.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone must have dropped a candle on a pile of rugs.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                        'Did I hear correctly? My {i}band{/i} was robbing this place?':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Did I hear correctly? My {i}band{/i} was robbing this place?')
                            jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                        'We leave behind many good people... Who put their trust in me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- We leave behind many good people... Who put their trust in me.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                        'Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                        '...What have I done?':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...What have I done?')
                            jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                '“Stay together! Don’t let them break through!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Stay together! Don’t let them break through!”')
                    menu:
                        'They give you distrustful looks, but follow your lead. You form a simple unit not a moment too soon - the first undead runs straight at you, as dumb as a thrown rock, and is dismembered in the blink of an eye, without so much as a grumble. In this darkness, which only grows deeper as the lights dwindle, you can’t even tell if the creature’s rotten flesh held any blood.
                        '
                        '“Push forward!”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Push forward!”')
                            show areapicture whitemarshesforaging01 at basicfade
                            if whitemarshes_attack_numberofallies >= 3:
                                if armor >= 4:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif armor >= 2:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-2)
                                    show minus2hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus2appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                else:
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            elif whitemarshes_attack_numberofallies == 2:
                                if armor >= 4:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif armor == 3:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 2:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-2)
                                    show minus2hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-3)
                                    show minus3hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus2appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                else:
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            else:
                                if armor >= 4:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor >= 3:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 2:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-2)
                                    show minus2hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-3)
                                    show minus3hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-4)
                                    show minus4hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus2appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                else:
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            if whitemarshes_attack_numberofallies >= 3:
                                $ whitemarshes_attack_numberofdead += 2
                                $ custom1 = "Thanks to all the allies you’ve gathered, most of you get through in one piece - but once you regroup behind the walls, you’re told to wait. “What about those who went for spoils?” someone asks, but you know there’s nothing else you can do for them. “We need to get out of here,” you respond. Some of the warriors hesitate, a few even speak against you, but seeing how the others are already on the move, they have to join them."
                            elif whitemarshes_attack_numberofallies == 2:
                                $ whitemarshes_attack_numberofdead += 4
                                $ custom1 = "A few of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Still, thanks to all the allies you’ve gathered, most of you get through only slightly wounded - but once you regroup behind the walls, you’re told to wait. “What about those who went for spoils?” someone asks, but you know there’s nothing else you can do for them. “We need to get out of here,” you respond. Some of the warriors hesitate, a few even speak against you, but seeing how the others are already on the move, they have to join them."
                            else:
                                $ whitemarshes_attack_numberofdead += 6
                                $ custom1 = "Many of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Having only a few people at your side, many of you get through with deep wounds - and once you regroup behind the walls, you’re told to wait. “What about those who went for spoils?” someone asks, but you know there’s nothing else you can do for them. “We need to get out of here,” you respond. Some of the warriors hesitate, a few even speak against you, but seeing how the others are already on the move, they have to join them."
                            $ whitemarshes_nomoreundead = day
                            $ whitemarshes_destroyed = 1
                            if quest_hiddenpurse == 1:
                                $ quest_hiddenpurse = 3
                            if quest_readtheletter == 1:
                                $ quest_readtheletter = 3
                            menu:
                                'Things happen quickly. The gates are just nearby, but the formation is forced to walk sideways, pushing away the attacks and stepping over corpses and abandoned possessions. Not being used to moving as a part of a unit, you don’t do too good a job of leading in the front row. Even worse, the creatures come from other directions, and you lack means to keep all sides of the formation protected.
                                \n\n[custom1]
                                \n\nAfter some time, you let yourself take a brief break, exhausted, cold, and covered in blood. You look behind - there’s light and smoke above the place that, until this day, was known as {color=#f6d6bd}White Marshes{/color}.
                                '
                                'Someone must have dropped a candle on a pile of rugs.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone must have dropped a candle on a pile of rugs.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'At least I helped some of us make it out.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least I helped some of us make it out.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'Did I hear correctly? My {i}band{/i} was robbing this place?':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Did I hear correctly? My {i}band{/i} was robbing this place?')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                '...What have I done?':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...What have I done?')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                'I look at {color=#f6d6bd}Glaucia{/color}.' if whitemarshes_attack_companion_bandits:
                    $ glaucia_friendship += 1
                    $ whitemarshes_attack_glauciahelpedescape = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Glaucia{/color}.')
                    menu:
                        'You catch her fascinated gaze, and she nods in return. “Listen up!” Her thundering voice makes your band freeze. Her stance is firm and confident. “These witless shitbags have no weapons. Make a tight row, we walk as one and leave as one.”
                        \n\nYour band, while varied, puts its trust in her. You form a wall of blades and armor not a moment too soon - the first undead runs straight at you, as dumb as a thrown rock, and is dismembered in the blink of an eye, without so much as a grumble. In this darkness, which only grows deeper as the lights dwindle, you can’t even tell if the creature’s rotten flesh held any blood.
                        '
                        'I’ve no other way - I follow her command.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no other way - I follow her command.')
                            show areapicture whitemarshesforaging01 at basicfade
                            if whitemarshes_attack_numberofallies >= 3:
                                if armor >= 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            elif whitemarshes_attack_numberofallies == 2:
                                if armor >= 4:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif armor >= 2:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-2)
                                    show minus2hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus2appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                else:
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            else:
                                if armor >= 4:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif armor >= 3:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 2:
                                    $ armor = limit_armor(armor-2)
                                    show minus2armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                elif armor == 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    $ pc_hp = limit_pc_hp(pc_hp-2)
                                    show minus2hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                                    if not cleanliness_clothes_torn:
                                        $ cleanliness_clothes_torn = 1
                                        show minus1appearance at appearancechange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-3)
                                    show minus3hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus2appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                                else:
                                    $ cleanliness = limit_cleanliness(cleanliness-1)
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            if whitemarshes_attack_numberofallies >= 3:
                                $ whitemarshes_attack_numberofdead += 1
                                $ custom1 = "Thanks to all the allies you’ve gathered, most of you get through in one piece - but once you regroup behind the walls, you realize that a few souls are missing. “They left us to pillage and died alone,” {color=#f6d6bd}Glaucia{/color} states matter-of-factly. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                            elif whitemarshes_attack_numberofallies == 2:
                                $ whitemarshes_attack_numberofdead += 3
                                $ custom1 = "A few of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Still, thanks to all the allies you’ve gathered, most of you get through only slightly wounded - but once you regroup behind the walls, you realize that a few more souls are missing. “They left us to pillage and died alone,” {color=#f6d6bd}Glaucia{/color} states matter-of-factly. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                            else:
                                $ whitemarshes_attack_numberofdead += 5
                                $ custom1 = "Many of your allies fall beneath the blows of the undead, shouting in pain as their throats and limbs are torn and bitten. Having only a few guards and the bandits at your side, many of you get through with deep wounds - and once you regroup behind the walls, you realize that a few more souls are missing. “They left us to pillage and died alone,” states {color=#f6d6bd}Glaucia{/color} gasping for air. “Run, before the village falls!” Some of the warriors hesitate, a few even speak against her, but seeing how the others are already on the move, they have to join them."
                            $ whitemarshes_nomoreundead = day
                            $ whitemarshes_destroyed = 1
                            if quest_hiddenpurse == 1:
                                $ quest_hiddenpurse = 3
                            if quest_readtheletter == 1:
                                $ quest_readtheletter = 3
                            menu:
                                'Things happen quickly. The gates are just nearby, but the formation is forced to walk sideways, pushing away the attacks and stepping over corpses and abandoned possessions. Not being used to moving as a part of a unit, you’re among those selected to look after the back and sides, cutting through the creatures that arrive from different directions.
                                \n\n[custom1]
                                \n\nAfter some time, you let yourself take a brief break, exhausted, cold, and covered in blood. You look behind - there’s light and smoke above the place that, until this day, was known as {color=#f6d6bd}White Marshes{/color}.
                                '
                                'Someone must have dropped a candle on a pile of rugs.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone must have dropped a candle on a pile of rugs.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'It was wise of me to take an experienced leader with us.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was wise of me to take an experienced leader with us.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'Did she just say that my {i}band{/i} was robbing this place?':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Did she just say that my band was robbing this place?')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                'Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Why didn’t {color=#f6d6bd}Orentius{/color} listen to me? He brought all of this upon his own tribe.')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02
                                '...What have I done?':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...What have I done?')
                                    jump whitemarshesorentiusafterdisputeplayerkilled03attack02

label whitemarshesorentiusafterdisputetravelingtohowlersdellALL:
    # banished
    label whitemarshesorentiusafterdisputebanished03attack02:
        show areapicture fordtobogentrance at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ howlersdell_reputation += 1
        menu:
            'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
            \n\nThe few beasts who dare to approach you flee from your large numbers, shouts, and torches. The mostly peaceful trail provides you with little surprises, but, this time, you don’t let anyone scout the path ahead.
            \n\nThose of your people who have no loot take their turns carrying the unconscious priest.
            '
            'I can’t wait for this night to end.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                jump whitemarshesorentiusafterdisputebanished03attack02a
            'I did good, the best I could. I can endure one more hour of this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did good, the best I could. I can endure one more hour of this.')
                label whitemarshesorentiusafterdisputebanished03attack02a:
                    $ pc_area = "howlersdell"
                    show areapicture howlersdellfulldark at basicfade
                    if whitemarshes_attack_glauciaattackedpc:
                        $ custom5 = "After a few more minutes, you get back on your feet, and manage to reach the destination without assistance. "
                    else:
                        $ custom5 = ""
                    if whitemarshes_attack_companion_bandits:
                        if whitemarshes_attack_glauciaattackedpc:
                            $ custom3 = "{color=#f6d6bd}Glaucia{/color} is the first one to speak. She gives an accurate, if unflattering, description of what happened, giving you a moment to breathe, yet omitting the sucker punch she gifted you in the end. "
                        else:
                            $ custom3 = "{color=#f6d6bd}Glaucia{/color} is the first one to speak. She gives an accurate, if unflattering, description of what happened, giving you a moment to breathe. "
                    else:
                        $ custom3 = "Even though one of her guards tries to speak up, she asks {i}you{/i} to report to her. Not paying much attention to your words, you recap the more significant parts of the evening."
                    if not whitemarshes_attack_numberofdead:
                        $ thais_friendship += 1
                        $ custom4 = "“No losses,” she repeats with an unmasked wonder. “And to think we chopped wood for the occasion.”"
                    elif whitemarshes_attack_numberofdead <= 3:
                        $ custom4 = "“Hardly any losses,” she repeats with a kind nod. “We already have the wood for the pyre. We saved many more souls today, and will use the spoils to look after the families.”"
                    elif whitemarshes_attack_numberofdead <= 6:
                        $ thais_friendship -= 1
                        $ custom4 = "“The losses are severe,” she repeats with a sigh. “We saved many more souls today, but the spoils you brought with you will help us look after the families.”"
                    else:
                        $ thais_friendship -= 2
                        $ custom4 = "“The losses are hard to accept,” her voice is cold. “We saved many more souls today, but the spoils you brought here won’t be enough to compensate the families. I’ll have a lot of explaining to do.”"
                    menu:
                        '[custom5]You’re welcomed by open gates, lanterns, and bowls of warm stew. You don’t pay much attention to the tears and embraces shared among the locals - like most people in your group, you just want to sleep.
                        \n\nBut {color=#f6d6bd}the mayor{/color} won’t allow it just yet. As her neighbors walk away, making space for her, you notice an unusual pattern of lines left on her face, as well as the distorted rouge on her lips. There are white specks of powder on her sleeve - she must have taken a nap.
                        \n\n[custom3] [custom4]
                        \n\nShe then reaches for the deer on her buckle, and gives you a long, curious look. “Are you alright, [pcname]?”
                        '
                        '“I’d rather rest. If you need to talk, bother your guards.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather rest. If you need to talk, bother your guards.”')
                            $ thais_friendship -= 1
                            $ custom1 = "She bites her lip, then raises her voice and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. I’m sure you have many tales to share, but let’s save them for the next day. {color=#f6d6bd}The necromancer{/color} will be dealt with soon enough, we’ve no reason to let him bother us any longer.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputebanished03talkingwiththais
                        '“It’s just my head.”' if whitemarshes_attack_glauciaattackedpc:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just my head.”')
                            $ custom1 = "You spot a playful gleam in her eyes as she steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day. {color=#f6d6bd}The necromancer{/color} will be dealt with soon enough, we’ve no reason to let him bother us any longer.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputebanished03talkingwiththais
                        '“I just need to do some thinking.”' if not whitemarshes_attack_glauciaattackedpc:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just need to do some thinking.”')
                            $ custom1 = "You spot a playful gleam in her eyes as she steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day. {color=#f6d6bd}The necromancer{/color} will be dealt with soon enough, we’ve no reason to let him bother us any longer.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputebanished03talkingwiththais
                        'I sigh, then smile. “Just tired. It was good working with you.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh, then smile. “Just tired. It was good working with you.”')
                            $ thais_friendship += 1
                            $ custom1 = "Her brief grin shifts into laughter. You glance at the curious eyes of her people - is it just the light, or are they afraid of her?\n\nShe steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day. {color=#f6d6bd}The necromancer{/color} will be dealt with soon enough, we’ve no reason to let him bother us any longer.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputebanished03talkingwiththais
                        '“I didn’t go there to rob farmers. You lied to me.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t go there to rob farmers. You lied to me.”')
                            $ thais_friendship -= 2
                            $ custom1 = "She steps closer, then again, lowering her face so that no one can see her lips. “I tell you what you {i}need{/i} to know,” the strong scent of cloves hits your nose, but her voice is chilling. “And if you question me in front of my village one more time, you won’t wake up again.”\n\nShe then spreads her arms, looks around, and says something to her “guests,” but you no longer listen. All you remember are your heavy steps to the inn, and the announcement that {color=#f6d6bd}the necromancer{/color} will be {i}dealt with{/i} soon."
                            jump whitemarshesorentiusafterdisputebanished03talkingwiththais

    label whitemarshesorentiusafterdisputebanished03attack02alt:
        show areapicture fordtobogentrance at basicfade
        stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        # nvl clear
        # with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        $ whitemarshes_attack_numberofdead += 1
        $ pc_food = limit_pc_food(pc_food-2)
        show minus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
        $ cleanliness = limit_cleanliness(cleanliness-3)
        show minus3appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
        menu:
            'You wake up in a cart, next to a few bags of loot and the unconscious priest. You sit up, noticing the taste of vomit on your lips. You reach for your aching head - there’s blood in your hair.
            \n\n{color=#f6d6bd}Glaucia’s{/color} voice reaches you from ahead. With the rest of the group, she’s standing by the remains of a large wolf-like creature that’s crushing the remains of someone from {color=#f6d6bd}Howler’s{/color}. When she notices your gaze, she puts her hands on her sides. “Now you wake up? Missed the fight,” she glances at the others, who are trying to push the dead beast off their companion. “I did a bit too good of a job hitting you with that brick, but you got a bit crazy there for a moment.” The dead guard lands next to you. Someone pats your shoulder encouragingly, but everything seems a bit fuzzy.
            \n\nGetting no response from you, {color=#f6d6bd}the bandit leader{/color} orders everyone to regroup and carry on.
            '
            'I can’t wait for this night to end.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                jump whitemarshesorentiusafterdisputebanished03attack02a
            'I try to say something, but all I can manage for now is an awkward mumble.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to say something, but all I can manage for now is an awkward mumble.')
                jump whitemarshesorentiusafterdisputebanished03attack02a

    label whitemarshesorentiusafterdisputebanished03talkingwiththais:
        $ whitemarshes_nomoreundead = (day+1)
        # $ orentius_banished = 1
        $ quest_orentius = 2
        $ thais_quest_all_completed = 1
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ quest_orentius_thais_description06 = "I’ve taken care of {color=#f6d6bd}Orentius{/color}."
        if pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ renpy.notify("Quest completed: Orentius, the Necromancer.\nJournal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer. Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ renpy.notify("Quest completed: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        menu:
            '[custom1]
            '
            'I don’t even take off my armor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even take off my armor.')
                $ sleep_destination = "howlersdellwakinguproom"
                jump sleeping

    # success and convinced
    label whitemarshesorentiusafterdisputesuccess03attack02:
        show areapicture fordtobogentrance at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ howlersdell_reputation += 2
        menu:
            'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
            \n\nThe few beasts who dare to approach you flee from your large numbers, shouts, and torches. The mostly peaceful trail provides you with little surprises, but, this time, you don’t let anyone scout the path ahead.
            '
            'I can’t wait for this night to end.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                jump whitemarshesorentiusafterdisputesuccess03attack02a
            'I did good, the best I could. I can endure one more hour of this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did good, the best I could. I can endure one more hour of this.')
                label whitemarshesorentiusafterdisputesuccess03attack02a:
                    $ pc_area = "howlersdell"
                    show areapicture howlersdellfulldark at basicfade
                    if whitemarshes_attack_glauciaattackedpc:
                        $ custom5 = "After a few more minutes, you get back on your feet, and manage to reach the destination without assistance. "
                    else:
                        $ custom5 = ""
                    if whitemarshes_attack_companion_bandits:
                        if whitemarshes_attack_glauciaattackedpc:
                            $ custom3 = "{color=#f6d6bd}Glaucia{/color} is the first one to speak. She gives an accurate, if unflattering, description of what happened, giving you a moment to breathe, yet omitting the sucker punch she gifted you in the end. "
                        else:
                            $ custom3 = "{color=#f6d6bd}Glaucia{/color} is the first one to speak. She gives an accurate, if unflattering, description of what happened, giving you a moment to breathe. "
                    else:
                        $ custom3 = "Even though one of her guards tries to speak up, she asks {i}you{/i} to report to her. Not paying much attention to your words, you recap the more significant parts of the evening."
                    if not whitemarshes_attack_numberofdead:
                        $ thais_friendship += 1
                        $ custom4 = "“No losses,” she repeats with an unmasked wonder. “And to think we chopped wood for the occasion.”"
                    elif whitemarshes_attack_numberofdead <= 3:
                        $ custom4 = "“Hardly any losses,” she repeats with a kind nod. “We already have the wood for the pyre. We saved many more souls today, and will use the spoils to look after the families.”"
                    elif whitemarshes_attack_numberofdead <= 6:
                        $ thais_friendship -= 1
                        $ custom4 = "“The losses are severe,” she repeats with a sigh. “We saved many more souls today, but the spoils you brought with you will help us look after the families.”"
                    else:
                        $ thais_friendship -= 2
                        $ custom4 = "“The losses are hard to accept,” her voice is cold. “We saved many more souls today, but the spoils you brought here won’t be enough to compensate the families. I’ll have a lot of explaining to do.”"
                    menu:
                        '[custom5]You’re welcomed by open gates, lanterns, and bowls of warm stew. You don’t pay much attention to the tears and embraces shared among the locals - like most people in your group, you just want to sleep.
                        \n\nBut {color=#f6d6bd}the mayor{/color} won’t allow it just yet. As her neighbors walk away, making space for her, you notice an unusual pattern of lines left on her face, as well as the distorted rouge on her lips. There are white specks of powder on her sleeve - she must have taken a nap.
                        \n\n[custom3] [custom4]
                        \n\nShe then reaches for the deer on her buckle, and gives you a long, curious look. “Are you alright, [pcname]?”
                        '
                        '“I’d rather rest. If you need to talk, bother your guards.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather rest. If you need to talk, bother your guards.”')
                            $ thais_friendship -= 1
                            $ custom1 = "She bites her lip, then raises her voice and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. I’m sure you have many tales to share, but let’s save them for the next day.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputesuccess03talkingwiththais
                        '“It’s just my head.”' if whitemarshes_attack_glauciaattackedpc:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just my head.”')
                            $ custom1 = "You spot a playful gleam in her eyes as she steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputesuccess03talkingwiththais
                        '“I just need to do some thinking.”' if not whitemarshes_attack_glauciaattackedpc:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just need to do some thinking.”')
                            $ custom1 = "You spot a playful gleam in her eyes as she steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputesuccess03talkingwiththais
                        'I sigh, then smile. “Just tired. It was good working with you.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh, then smile. “Just tired. It was good working with you.”')
                            $ thais_friendship += 1
                            $ custom1 = "Her brief grin shifts into laughter. You glance at the curious eyes of her people - is it just the light, or are they afraid of her?\n\nShe steps closer and reaches toward your shoulder without touching it, and invites you with a gesture to head to the inn. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests,” she raises her voice, allowing the others to hear her well. “I’m sure you have many tales to share, but let’s save them for the next day.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputesuccess03talkingwiththais
                        '“I didn’t go there to rob farmers. You lied to me.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t go there to rob farmers. You lied to me.”')
                            $ thais_friendship -= 2
                            $ custom1 = "She steps closer, then again, lowering her face so that no one can see her lips. “I tell you what you {i}need{/i} to know,” the strong scent of cloves hits your nose, but her voice is chilling. “And if you question me in front of my village one more time, you won’t wake up again.”\n\nShe then spreads her arms, looks around, and says something to her “guests,” but you no longer listen. All you remember are your heavy steps to the inn."
                            jump whitemarshesorentiusafterdisputesuccess03talkingwiththais

    label whitemarshesorentiusafterdisputesuccess03attack02alt:
        show areapicture fordtobogentrance at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ whitemarshes_attack_numberofdead += 1
        $ pc_food = limit_pc_food(pc_food-2)
        show minus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
        $ cleanliness = limit_cleanliness(cleanliness-3)
        show minus3appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
        menu:
            'You wake up in a cart, next to a few bags of loot. You sit up, noticing the taste of vomit on your lips. You reach for your aching head - there’s blood in your hair.
            \n\n{color=#f6d6bd}Glaucia’s{/color} voice reaches you from ahead. With the rest of the group, she’s standing by the remains of a large wolf-like creature that’s crushing the remains of someone from {color=#f6d6bd}Howler’s{/color}. When she notices your gaze, she puts her hands on her sides. “Now you wake up? Missed the fight,” she glances at the others, who are trying to push the dead beast off their companion. “I did a bit too good of a job hitting you with that brick, but you got a bit crazy there for a moment.” The dead guard lands next to you. Someone pats your shoulder encouragingly, but everything seems a bit fuzzy.
            \n\nGetting no response from you, {color=#f6d6bd}the bandit leader{/color} orders everyone to regroup and carry on.
            '
            'I can’t wait for this night to end.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                jump whitemarshesorentiusafterdisputesuccess03attack02a
            'I try to say something, but all I can manage for now is an awkward mumble.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to say something, but all I can manage for now is an awkward mumble.')
                jump whitemarshesorentiusafterdisputesuccess03attack02a

    label whitemarshesorentiusafterdisputesuccess03talkingwiththais:
        $ whitemarshes_nomoreundead = (day+1)
        $ orentius_convinced = 1
        $ achievement_pyrepoints += 1
        $ quest_orentius = 2
        $ thais_quest_all_completed = 1
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ quest_orentius_thais_description06 = "I’ve taken care of {color=#f6d6bd}Orentius{/color}."
        if pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ renpy.notify("Quest completed: Orentius, the Necromancer.\nJournal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer. Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ renpy.notify("Quest completed: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        menu:
            '[custom1]
            '
            'I don’t even take off my armor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even take off my armor.')
                $ sleep_destination = "howlersdellwakinguproom"
                jump sleeping

    # fail and spared
    label whitemarshesorentiusafterdisputefail03attack02:
        show areapicture fordtobogentrance at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ howlersdell_reputation -= 1
        menu:
            'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
            \n\nThe few beasts who dare to approach you flee from your large numbers, shouts, and torches. The mostly peaceful trail provides you with little surprises, but, this time, you don’t let anyone scout the path ahead.
            '
            'I can’t wait for this night to end.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                jump whitemarshesorentiusafterdisputefail03attack02a
            'I failed. I failed. I failed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I failed. I failed. I failed.')
                label whitemarshesorentiusafterdisputefail03attack02a:
                    $ pc_area = "howlersdell"
                    show areapicture howlersdellfulldark at basicfade
                    if not whitemarshes_attack_numberofdead:
                        $ thais_friendship += 1
                        $ custom4 = "At least there were no losses,” her heavy breathing betrays that it’s not much solace. “All that’s left is for us to secure our walls.”"
                    elif whitemarshes_attack_numberofdead <= 3:
                        $ custom4 = "At least there were hardly any losses,” her heavy breathing betrays that it’s not much solace. “We already have the wood for the pyre. We’ll use the spoils to look after the families. All that’s left is for us to secure our walls.”"
                    elif whitemarshes_attack_numberofdead <= 6:
                        $ thais_friendship -= 1
                        $ custom4 = "The losses are severe,” she stares at you, breathing heavily. “We’ll use the spoils to look after the families, but even that may not be enough. Especially since now we have to secure our walls.”"
                    else:
                        $ thais_friendship -= 2
                        $ custom4 = "The losses are hard to accept,” she stares at you,breathing heavily. Her voice makes the square even colder, and a few people walk away from her sight. “We’ll use the spoils to look after the families, but even that may not be enough. Especially since now we have to secure our walls.”"
                    menu:
                        'You’re welcomed by open gates, lanterns, and bowls of warm stew. You don’t pay much attention to the tears and embraces shared among the locals - like most people in your group, you just want to sleep.
                        \n\nBut {color=#f6d6bd}the mayor{/color} won’t allow it just yet. As her neighbors walk away, making space for her, you notice an unusual pattern of lines left on her face, as well as the distorted rouge on her lips. There are white specks of powder on her sleeve - she must have taken a nap.
                        \n\nEven though one of her guards tries to speak up, she asks {i}you{/i} to report to her. Not paying much attention to your words, you recap the more significant parts of the evening. “So our last chance is gone, for whatever reason. [custom4]
                        \n\nShe then reaches for the deer on her buckle, and gives you a long, angry look. “Anything else?”
                        '
                        '“I’d rather rest. If you need to talk, bother your guards.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather rest. If you need to talk, bother your guards.”')
                            $ thais_friendship -= 1
                            $ custom1 = "She bites her lip, then raises her voice and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputefail03talkingwiththais
                        '“No. I just need to do some thinking.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. I just need to do some thinking.”')
                            $ custom1 = "Her green eyes soften, but not for long. “Do that,” she adjusts her robe and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up in bed."
                            jump whitemarshesorentiusafterdisputefail03talkingwiththais
                        '“I didn’t go there to rob farmers. You lied to me.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t go there to rob farmers. You lied to me.”')
                            $ thais_friendship -= 2
                            $ custom1 = "She steps closer, then again, lowering her face so that no one can see her lips. “I tell you what you {i}need{/i} to know,” the strong scent of cloves hits your nose, but her voice is chilling. “And you still can’t do your part. If you question me in front of my village one more time, you won’t wake up again.”\n\nShe then spreads her arms, looks around, and says something to her “guests,” but you no longer listen. All you remember are your heavy steps to the inn."
                            jump whitemarshesorentiusafterdisputefail03talkingwiththais

    label whitemarshesorentiusafterdisputefail03talkingwiththais:
        $ whitemarshes_nomoreundead = (day+1)
        $ orentius_spared = 1
        $ quest_orentius = 3
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ renpy.notify("Quest completed: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        $ quest_orentius_thais_description09 = "I failed - {color=#f6d6bd}Orentius{/color} has kept his position, and I doubt the villagers are going to accept me among them ever again."
        menu:
            '[custom1]
            '
            'I don’t even take off my armor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even take off my armor.')
                $ sleep_destination = "howlersdellwakinguphall"
                jump sleeping

    # glaucia killed orentius
    label whitemarshesorentiusafterdisputeglauciakilled03attack02:
        show areapicture westerncrossroadstoford at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ howlersdell_reputation += 0
        menu:
            'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
            \n\nBecause of your stench and the losses you already suffered, the beasts are now looking for an easy catch. Your shouts and torches help, but after a short clash you leave one more shell to a pack of wolf-like creatures. {i}What difference will yet another undead make anyway{/i}, you think, unable to feel any more dread.
            \n\nAfter you reach the crossroads, {color=#f6d6bd}Glaucia{/color} speaks again. “Time to split our paths,” she announces, making her people scowl at her, but they keep their thoughts to themselves. “The undead may wait for a few seasons before they start their hunt, or not at all. I won’t leave my friends at the camp to themselves.”
            \n\nShe spares the others a few nods, then gestures for her people to head east.
            '
            '“Should you really enter the woods by yourself, and so late?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should you really enter the woods by yourself, and so late?”')
                menu:
                    'She rests her hands on her sides, and looks at you with a gentle smirk. “These are {i}our{/i} woods, we know a few paths you wouldn’t even imagine. Farewell, outsider.”
                    \n\nAs she walks away, her pace is confident and light, as if she’s stopping herself from whistling.
                    '
                    'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02a
            '“Thank you for getting us out of there.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for getting us out of there.”')
                $ glaucia_friendship += 1
                menu:
                    'She approaches you, and pats your shoulder firmly. “We must stick together these days. Safe travels, outsider.”
                    \n\nAs she walks away, her pace is confident and light, as if she’s stopping herself from whistling.
                    '
                    'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02a
            '“You did a terrible thing. I want you to know this.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You did a terrible thing. I want you to know this.”')
                $ glaucia_friendship -= 1
                menu:
                    'Her words are slow and patient, yet she taps the hilt of her sword. “All I did was fix what you couldn’t, {i}roadwarden{/i}. If I hadn’t acted, the madness would have continued, devouring the entire village sooner or later. At least I cut it short, and we chopped some undead limbs as well. We’ve had a hard night, but we’re going to sleep as heroes.”
                    \n\nHer pace is confident and strong as she walks away.
                    '
                    'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02a
            '“We should arrest you, right here, right now.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should arrest you, right here, right now.”')
                $ glaucia_friendship -= 2
                $ whitemarshes_attack_glauciathreatened = 1
                menu:
                    'She raises her chin and meets your eyes. “It would be fun to see you try, but I’ve no time. Farewell, stranger.”
                    \n\nHer pace is confident and strong as she walks away.
                    '
                    'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                        jump whitemarshesorentiusafterdisputeglauciakilled03attack02a
            'Without a word, I observe their departure.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a word, I observe their departure.')
                jump whitemarshesorentiusafterdisputeglauciakilled03attack02a

    label whitemarshesorentiusafterdisputeglauciakilled03attack02a:
        $ pc_area = "howlersdell"
        show areapicture howlersdellfulldark at basicfade
        if whitemarshes_attack_numberofdead <= 3:
            $ custom4 = "“We hardly suffered any losses, I guess,” her voice is cold, “but without the spoils, we can’t use them to look after the families. All that’s left is for us to secure our walls.”"
        elif whitemarshes_attack_numberofdead <= 6:
            $ thais_friendship -= 1
            $ custom4 = "“We suffered severe losses,” her voice is cold, “and we have no spoils to divide between the family members. All that’s left is for us to secure our walls.”"
        else:
            $ thais_friendship -= 2
            $ custom4 = "“The losses are hard to accept,” she stares at you, breathing heavily. Her voice makes the square even colder, and a few people walk away from her sight. “Even worse, we’ve no spoils to share with the family members, and we have to start working on our own walls.”"
        menu:
            'You’re welcomed by open gates, lanterns, and bowls of warm stew. You don’t pay much attention to the tears and embraces shared among the locals - like most people in your group, you just want to sleep.
            \n\nBut {color=#f6d6bd}the mayor{/color} won’t allow it just yet. As her neighbors walk away, making space for her, you notice an unusual pattern of lines left on her face, as well as the distorted rouge on her lips. There are white specks of powder on her sleeve - she must have taken a nap.
            \n\nEven though one of her guards tries to speak up, she asks {i}you{/i} to report to her. Not paying much attention to your words, you recap the more significant parts of the evening, making everyone who can hear you fall silent. “{color=#f6d6bd}White Marshes{/color} has fallen,” people whisper, and these words spread like a wave, stinging your soul every time you hear the village’s name. {color=#f6d6bd}Thais{/color} orders them to let you speak, but you don’t have much to add.
            \n\n[custom4] She then reaches for the deer on her buckle, and gives you a long, angry look. “Anything else?”
            '
            '“I’d rather rest. If you need to talk, bother your guards.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather rest. If you need to talk, bother your guards.”')
                $ thais_friendship -= 1
                $ custom1 = "She bites her lip, then raises her voice and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up on a pile of furs."
                jump whitemarshesorentiusafterdisputeglauciakilled03talkingwiththais
            '“No. I just need to do some thinking.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. I just need to do some thinking.”')
                $ custom1 = "Her green eyes soften, but not for long. “Do that,” she adjusts her robe and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up on a pile of furs."
                jump whitemarshesorentiusafterdisputeglauciakilled03talkingwiththais
            '“Why were our people robbing that place? Did you lie to me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why were our people robbing that place? Did you lie to me?”')
                $ thais_friendship -= 2
                $ custom1 = "She steps closer, then again, lowering her face so that no one can see her lips. “I tell you what you {i}need{/i} to know,” the strong scent of cloves hits your nose, but her voice is chilling. “And you still can’t do your part. If you question me in front of my village one more time, you won’t wake up again.”\n\nShe then spreads her arms, looks around, and says something to her “guests,” but you no longer listen. All you remember are your heavy steps to the inn."
                jump whitemarshesorentiusafterdisputeglauciakilled03talkingwiththais

    label whitemarshesorentiusafterdisputeglauciakilled03talkingwiththais:
        $ whitemarshes_nomoreundead = (day+1)
        $ quest_orentius = 2
        $ thais_quest_all_completed = 1
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ renpy.notify("Quest completed: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        $ quest_orentius_thais_description06 = "I’ve taken care of {color=#f6d6bd}Orentius{/color}. Kind of."
        menu:
            '[custom1]
            '
            'I don’t even take off my armor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even take off my armor.')
                $ sleep_destination = "howlersdellwakinguphall"
                jump sleeping

    # pc killed orentius
    label whitemarshesorentiusafterdisputeplayerkilled03attack02:
        show areapicture westerncrossroadstoford at basicfade
        # stop music fadeout 4.0
        # play nature "audio/ambient/night01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg":
            play music "<loop 8.0>audio/jonathanfraserinterlude_violence_loop.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ howlersdell_reputation += 1
        if whitemarshes_attack_companion_bandits:
            menu:
                'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
                \n\nBecause of your stench and the losses you already suffered, the beasts are now looking for an easy catch. Your shouts and torches help, but after a short clash you leave one more shell to a pack of wolf-like creatures. {i}What difference will yet another undead make anyway{/i}, you think, unable to feel any more dread.
                \n\nAfter you reach the crossroads, {color=#f6d6bd}Glaucia{/color} speaks again. “Time to split our paths,” she announces, making her people scowl at her, but they keep their thoughts to themselves. “The undead may wait for a few seasons before they start their hunt, or not at all. I won’t leave my friends at the camp to themselves.”
                \n\nShe spares the others a few nods, then gestures for her people to head east.
                '
                '“Should you really enter the woods by yourself, and so late?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should you really enter the woods by yourself, and so late?”')
                    menu:
                        'She rests her hands on her sides, and looks at you with a gentle smirk. “These are {i}our{/i} woods, we know a few paths you wouldn’t even imagine. Farewell, [pcname]. You did the right thing.”
                        \n\nAs she walks away, her pace is confident and light, as if she’s stopping herself from whistling.
                        '
                        'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03a
                '“Thank you for getting us out of there.”' if whitemarshes_attack_glauciahelpedescape:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for getting us out of there.”')
                    $ glaucia_friendship += 1
                    menu:
                        'She approaches you, and pats your shoulder firmly. “We must stick together these days. Safe travels, [pcname]. I’m glad I went with you.”
                        \n\nAs she walks away, her pace is confident and light, as if she’s stopping herself from whistling.
                        '
                        'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03a
                '“I’m sorry for putting you at risk.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry for putting you at risk.”')
                    menu:
                        'She leans away, giving you a puzzled look. “What do you mean? You did well, roadwarden. You did what had to be done. The madness would have continued, devouring the entire village sooner or later. At least you cut it short, and we chopped some undead limbs as well. We’ve had a hard night, but we’re going to sleep as heroes.”
                        \n\nHer pace is confident and strong as she walks away.
                        '
                        'I lead the others back to {color=#f6d6bd}Howler’s{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others back to {color=#f6d6bd}Howler’s{/color}.')
                            jump whitemarshesorentiusafterdisputeplayerkilled03a
                'Without a word, I observe their departure.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a word, I observe their departure.')
                    jump whitemarshesorentiusafterdisputeplayerkilled03a
        else:
            menu:
                'Every minute spent in the darkness feels like ten. Your eyes track frightened birds, cracking twigs, moving leaves. Your limbs are heavy, and your senses are begging for a break.
                \n\nBecause of your stench and the losses you already suffered, the beasts are now looking for an easy catch. Your shouts and torches help, but after a short clash you leave one more shell to a pack of wolf-like creatures. {i}What difference will yet another undead make anyway{/i}, you think, unable to feel any more dread.
                \n\nYour companions don’t talk to each other, but you’ve heard the word “murderer” at least twice.
                '
                'I can’t wait for this night to end.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t wait for this night to end.')
                    jump whitemarshesorentiusafterdisputeplayerkilled03a
                'I tell them to shut up.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell them to shut up.')
                    label whitemarshesorentiusafterdisputeplayerkilled03a:
                        $ pc_area = "howlersdell"
                        show areapicture howlersdellfulldark at basicfade
                        if whitemarshes_attack_numberofdead <= 3:
                            $ custom4 = "“We hardly suffered any losses, I guess,” her voice is cold, “but without the spoils, we can’t use them to look after the families. All that’s left is for us to secure our walls.”"
                        elif whitemarshes_attack_numberofdead <= 6:
                            $ thais_friendship -= 1
                            $ custom4 = "“We suffered severe losses,” her voice is cold, “and we have no spoils to divide between the family members. All that’s left is for us to secure our walls.”"
                        else:
                            $ thais_friendship -= 2
                            $ custom4 = "“The losses are hard to accept,” she stares at you, breathing heavily. Her voice makes the square even colder, and a few people walk away from her sight. “Even worse, we’ve no spoils to share with the family members, and we have to start working on our own walls.”"
                        menu:
                            'You’re welcomed by open gates, lanterns, and bowls of warm stew. You don’t pay much attention to the tears and embraces shared among the locals - like most people in your group, you just want to sleep.
                            \n\nBut {color=#f6d6bd}the mayor{/color} won’t allow it just yet. As her neighbors walk away, making space for her, you notice an unusual pattern of lines left on her face, as well as the distorted rouge on her lips. There are white specks of powder on her sleeve - she must have taken a nap.
                            \n\nEven though one of her guards tries to speak up, she asks {i}you{/i} to report to her. Not paying much attention to your words, you recap the more significant parts of the evening, making everyone who can hear you fall silent. “{color=#f6d6bd}White Marshes{/color} has fallen,” people whisper, and these words spread like a wave, stinging your soul every time you hear the village’s name. {color=#f6d6bd}Thais{/color} orders them to let you speak, but you don’t have much to add.
                            \n\n[custom4] She then reaches for the deer on her buckle, and gives you a long, angry look. “Was there really no other option?”
                            '
                            '“You weren’t there. You wouldn’t understand.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You weren’t there. You wouldn’t understand.”')
                                $ thais_friendship -= 1
                                $ custom1 = "She bites her lip, then raises her voice and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up on a pile of furs."
                                jump whitemarshesorentiusafterdisputeplayerkilled03talkingwiththais
                            '“No. I did everything I could, but {color=#f6d6bd}Orentius{/color} was a fanatic. It was our last chance.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. I did everything I could, but {color=#f6d6bd}Orentius{/color} was a fanatic. It was our last chance.”')
                                $ thais_friendship += 1
                                $ custom1 = "Her green eyes soften, but not for long. “I believe you,” she adjusts her robe and looks around. “{color=#f6d6bd}Eryx{/color} prepared everything for our guests. We’ll get to work tomorrow morning.”\n\nYou don’t remember how you ended up on a pile of furs."
                                jump whitemarshesorentiusafterdisputeplayerkilled03talkingwiththais
                            '“I... Don’t know.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I... Don’t know.”')
                                $ custom1 = "You look down, not sure if the taste of salt on your lips comes from sweat, or tears.\n\nYou don’t remember how you ended up on a pile of furs."
                                jump whitemarshesorentiusafterdisputeplayerkilled03talkingwiththais
                            'I look her in the eyes. “Why were our people robbing that place? Did you lie to me?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look her in the eyes. “Why were our people robbing that place? Did you lie to me?”')
                                $ thais_friendship -= 2
                                $ custom1 = "She steps closer, then again, lowering her face so that no one can see her lips. “I tell you what you {i}need{/i} to know,” the strong scent of cloves hits your nose, but her voice is chilling. “And you still can’t do your part. If you question me in front of my village one more time, you won’t wake up again.”\n\nShe then spreads her arms, looks around, and says something to her “guests,” but you no longer listen. All you remember are your heavy steps to the inn."
                                jump whitemarshesorentiusafterdisputeplayerkilled03talkingwiththais

    label whitemarshesorentiusafterdisputeplayerkilled03talkingwiththais:
        $ whitemarshes_nomoreundead = (day+1)
        $ quest_orentius = 2
        $ thais_quest_all_completed = 1
        $ vines_perma_closed = 1
        $ vines_perma_open = 0
        $ renpy.notify("Quest completed: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        $ quest_orentius_thais_description06 = "I’ve taken care of {color=#f6d6bd}Orentius{/color}."
        menu:
            '[custom1]
            '
            'I don’t even take off my armor.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t even take off my armor.')
                $ sleep_destination = "howlersdellwakinguphall"
                jump sleeping
