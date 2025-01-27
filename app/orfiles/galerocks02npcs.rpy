label galerocksphotiosALL: # {color=#f6d6bd}Photios{/color}, the fisher
    label galerocksphotios01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_photios_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        if pc_area == "galerocks":
            $ custom1 = "You approach a group of workers who are loading barrels onto a cart, close to the log-made bridge. “{color=#f6d6bd}Photios{/color} is there,” one of them tells you, and points at the tallest man, dressed in undyed wool and linen. He’s discussing something with a group of workers, but as you head in his direction, he nods for you to join him on the side."
            show galerocksoverlay photios at basicfade
        if pc_area == "beforebeach":
            $ custom1 = "You approach the few workers in front of the group and ask who you should speak with. “{color=#f6d6bd}Photios{/color} is there,” one of them tells you, and points at the tallest man, dressed in undyed wool and linen, with crystalized salt still clinging to the drying fabric. You move in his direction, and he nods for you to join him in his walk."
        if pc_area == "beach":
            $ custom1 = "You approach a group of workers standing in front of the shed. “{color=#f6d6bd}Photios{/color} is there,” one of them tells you, and points at the tallest man, dressed in undyed wool and linen. He’s discussing something with a group of workers, but as you head in his direction, he nods for you to join him on the side."
        menu:
            '[custom1]
            \n\nHis outfit is heavy, appropriately so for someone who spends long hours under the hits of the cold onshore winds. The massive leather boots, thick tunic and pants, and the heavy cloak, now held under his arm, make you wonder if he’d even be able to swim.
            \n\nLike most seafolk, he has long limbs, almost no facial hair, and ears so flat they are hardly noticeable. His neck draws your eyes - it’s covered with marks left by the burning suckers of a sea monster, as wide as your finger is long. Below these scars he’s wearing a pendant made of a fist-sized black “beak”.
            \n\nHe speaks first, with the strong and confident voice of a young man, no older than twenty-five. “We don’t really sell any catch on our own, maybe ask our smokers, or the cook.”
            '
            '“That’s fine. I was hoping to speak with you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s fine. I was hoping to speak with you.”')
                $ questionpreset = "photios1"
                menu:
                    '“And who are you, exactly?” After you introduce yourself, the man raises a corner of his mouth in an angry grimace. “I won’t have much to tell you, {i}roadwarden{/i}. Like my neighbors,” he looks at the nearby fishers, “I struggle with day-to-day living, I do, not adventures, and even less so outsiders’ schemes.”
                    '
                    '(photios1 set)':
                        pass

    label galerocksphotios01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ questionpreset = "photios1"
        if pc_area == "galerocks":
            if quarters < 34:
                $ custom1 = "Some of the fishers are still a bit sleepy, and {color=#f6d6bd}Photios{/color} makes sure to see that all the preparations go smoothly."
            else:
                $ custom1 = "The exhausted fishers move slowly, allowing the other villagers to unload the barge. {color=#f6d6bd}Photios{/color} keeps a lantern in his hand, giving commands to the carriers."
            show galerocksoverlay photios at basicfade
        if pc_area == "beforebeach":
            $ custom1 = "{color=#f6d6bd}Photios{/color} discusses plans for tomorrow with the other workers, but politely nods to you."
        if pc_area == "beach":
            $ custom1 = "{color=#f6d6bd}Photios{/color} inspects the equipment and discusses future plans with the workers on the coast."
        menu:
            '[custom1]
            '
            '(photios1 set)':
                pass

    label galerocksphotiosafterinteraction01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ questionpreset = "photios1"
        $ custom1 = renpy.random.choice(['He raises his hand to scratch his neck, but stops himself before he does so, and lets out an annoyed sigh.', 'He gives a quick command to another fisher.', 'He gestures for you to go on.', '“So, are we done here?”', '“Anything else?”', 'He runs his eyes over the nearby workers.'])
        menu:
            '[custom1]
            '
            '(photios1 set)':
                pass

    label galerocks_photios_about_mundanejob01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any work for me?”')
        $ galerocks_photios_about_mundanejob = 1
        menu:
            '“Work? What do {i}you{/i} know about fishing?” You mention the docks of {color=#f6d6bd}Hovlavan{/color}, but after a few questions about fishing nets, boats, and winds, it’s clear you don’t impress in this conversation. “Teaching one how to work with us takes time, effort, and rescuing those who fall overboard. You ain’t a kid of ours, so if anything, it should be you who pays {i}us{/i} for sharing what our forebears have mastered.”
            \n\nYou explain that you can fight better than most, and that gives him an idea. “Our guards stay at the village, so we always move in groups, and waste time securing the beach from harpies and saurians, we do. We could put three more souls on the boat, and keep you on the beach, you’d guard those not fishing with nets.”
            '
            '“What’s in it for me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s in it for me?”')
                $ renpy.notify("New mundane job available.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New mundane job available.{/i}')
                $ minutes += 5
                $ questionpreset = "photios1"
                menu:
                    '“Ehm... How much do you want, stranger?” He responds carefully, and you spend a few minutes discussing the details. “Right, you’ll get a meal and two coins for a peaceful day, and another one for putting your life at risk,” he summarizes. “But you must be at the beach soon after dawm, while we’re preparing our boats. And have enough strength to convince me you’ll be more of a help than a bother.”
                    '
                    '(photios1 set)':
                        pass

    label galerocksphotiosofferingmundanejob01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Need help with fishing today?”')
        show screen mundanejob() with dissolve
        $ questionpreset = "photios1"
        menu:
            'You discuss the terms.
            '
            '(photios1 set)':
                pass

    label galerocksphotiosaftermundanejob01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Need help with fishing today?”')
        $ questionpreset = "photios1"
        $ galerocks_photios_about_mundanejob_totalnumber += 1
        $ quarters = (world_daylength-14)
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter)
        else:
            $ d100roll -= (pc_battlecounter/2)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if d100roll > 90:
            $ custom1 = "A large saurian tried to get inside the shelter, lured by the smell of fish. You and your companions managed to fight it off, but as the front-line fighter, you took a serious hit from its claws. At least you receive a fresh, roasted fish with a bowl of cold veggie stew and some dried nuts, and an extra dragon bone for your efforts."
            $ pc_battlecounter += 1
            if armor >= 3:
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            elif armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ cleanliness_clothes_torn = 1
            $ cleanliness_clothes_blood = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus4appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
            $ galerocks_work_hours += 8
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png" )
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_food = limit_pc_food(pc_food+3)
            show plus3food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        elif d100roll > 70:
            $ custom1 = "A flock of harpies tried to distract your companions to get to some of the open barrels of fish, but your group managed to fight them off. Still, as the front-line fighter, you took a few serious scratches and bites. At least you receive a fresh, roasted fish with a bowl of cold veggie stew, and an extra dragon bone for your efforts."
            $ pc_battlecounter += 1
            if armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness_clothes_torn = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus3appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            $ galerocks_work_hours += 8
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png" )
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_food = limit_pc_food(pc_food+2)
            show plus2food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        elif d100roll > 40:
            if armor < 2:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "A flock of harpies tried to strike one of the spearfishers that was hunting from a rock, but your group managed to fight it off. Even you, the front-line fighter, got away with only a few scratches, but you got covered with mud and salt in the process. In the middle of the day, you receive a fresh, roasted fish with a bowl of cold veggie stew, and an extra dragon bone for your efforts."
            else:
                $ custom1 = "A flock of harpies tried to strike one of the spearfishers that was hunting from a rock, but your group managed to fight it off. Even you, the front-line fighter, got away safe, with your armor protecting you from any threats, but you got covered with mud and salt in the process. In the middle of the day, you receive a fresh, roasted fish with a bowl of cold veggie stew, and an extra dragon bone for your efforts."
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ galerocks_work_hours += 7
            $ coins += 3
            show screen notifyimage( "+3", "gui/coin2.png" )
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
            $ pc_food = limit_pc_food(pc_food+2)
            show plus2food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        else:
            $ custom1 = "It turns out you don’t have much to do. The hours go by, and during the lazy break, you receive a fresh, roasted fish with a bowl of cold veggie stew."
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ galerocks_work_hours += 7
            $ coins += 2
            show screen notifyimage( "+2", "gui/coin2.png" )
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 {image=cointest}{/i}')
            $ pc_food = limit_pc_food(pc_food+2)
            show plus2food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        menu:
            '[custom1]
            '
            '(photios1 set)':
                pass

    label galerocks_photios_about_beingafisher01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s it like, being a fisher?”')
        $ galerocks_photios_about_beingafisher = 1
        menu:
            '“Tedious, yet tense,” he answers without giving it even a heartbeat of reflection. “Just like centuries ago. I’ve heard tales of our forebears, so I know some things have changed. We don’t swim as well as those from the legends, but our boats are quicker, and nets are replacing our spear hunters. But our days are harsh, we lose someone to the sea every year,” he points at his scarred neck. “But we grow strong, with plenty of sun, salt, and more food than we can eat. I’ll fight for many years, but many of the older fishers grow timesick. Silent, bored, {i}resting{/i} by looking at walls and tides.” He looks away, hesitant to continue. “{i}Melancholic{/i}, I think you’d say in the city.”
            \n\nHe glances back at you. “And how’s being a roadwarden?”
            '
            '“Exciting, of course. No day is the same.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Exciting, of course. No day is the same.”')
                $ questionpreset = "photios1"
                $ galerocks_photios_friendship -= 1
                menu:
                    '“Is that what your life is about? Excitement?” He doesn’t give you time to answer. “In {color=#f6d6bd}Gale Rocks{/color}, we do what we have to, not what we want. We support each other and our families, resting in winter, if at all. No matter how wounded or disfigured one is, we’ll spend our days caring for them,” he points at his scarred neck, then shows you his left hand. One finger and a half are already gone. “I’m proud of such a home, I am. Your paths are twisted.”
                    '
                    '(photios1 set)':
                        pass
            '“It’s just another job. Some days are better, others are worse.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just another job. Some days are better, others are worse.”')
                $ questionpreset = "photios1"
                menu:
                    'He scoffs. “No traveler knows a real trade. Once you get back to the city, try to carry crates and barrels day after day, for five years straight. You’ll understand what it means to live like other people do, no matter if they want to or not.”
                    '
                    '(photios1 set)':
                        pass
            '“It sucks. Danger, mistrust, dirt. It’s a struggle, but I must endure it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It sucks. Danger, mistrust, dirt. It’s a struggle, but I must endure it.”')
                $ questionpreset = "photios1"
                $ galerocks_photios_friendship += 1
                menu:
                    'There’s sympathy in his eyes. “Makes one wonder why anyone would do such a trade, right? I’m going to guess coins.” He doesn’t give you time to respond. “At least you’re not an adventurer, I can see {i}some{/i} use for your trade.”
                    '
                    '(photios1 set)':
                        pass
            '“Oh, I wouldn’t know. I’m just starting.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, I wouldn’t know. I’m just starting.”')
                $ questionpreset = "photios1"
                menu:
                    'He frowns, tilts his head left, then right. “Right.”
                    '
                    '(photios1 set)':
                        pass

    label galerocks_photios_about_fishtraps01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wouldn’t it be easier for you to use the fish traps? Like a basket?”')
        $ galerocks_photios_about_fishtraps = 1
        $ galerocks_photios_friendship += 1
        $ questionpreset = "photios1"
        menu:
            'You explain briefly how it would work. “Aw right, I see. Like the tribe of {color=#f6d6bd}Creeks{/color} does? We’d rather stick to what we have, stranger. These {i}traps{/i} are fragile, and the sea is harsh. They would get crushed by tides, or broken by big fish and birds. Nets are already a big help, we used to have only spear hunters.” He gives you an unusually warm smile. “I appreciate the thought, but fishing is in our blood. We know what we’re doing, we do.”
            '
            '(photios1 set)':
                pass

    label photios_about_recruitahunter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} working with you often?”')
        if (galerocks_photios_friendship+appearance_charisma+galerocks_reputation) < 6 and not quest_spiritrock == 2:
            $ quest_recruitahunter_spokento_photios_gray = 1
            $ questionpreset = "photios1"
            menu:
                'His eyes narrow. “I used to, now I don’t. Such are the things. She’s an annoying lass, but that’s about it.”
                '
                '(photios1 preset)':
                    pass
        else:
            label photios_about_recruitahunter02:
                $ quest_recruitahunter_spokento_photios = 1
                $ quest_recruitahunter_cassia_points += 1
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
                    $ quest_recruitahunter_cassia_points_notify2 = 1
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                $ questionpreset = "photios1"
                if quest_recruitahunter_spokento_photios_gray:
                    $ custom1 = "He shrugs. “"
                else:
                    $ custom1 = "His eyes narrow. “I used to, now I don’t. "
                menu:
                    '[custom1]There were a few times she told me she was asked to guard the gate, but then it turned out she told the guards back home that {i}I{/i} asked {i}her{/i} for help. She was merely idling about, like a child. The fishers don’t need someone like this around here.”
                    '
                    '(photios1 preset)':
                        pass

        label photios_about_recruitahunter01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why does {color=#f6d6bd}Cassia{/color} annoy you?”')
            jump photios_about_recruitahunter02

    label galerocks_photios_about_highisland01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to {color=#f6d6bd}High Island{/color}?”')
        $ galerocks_photios_about_highisland = 1
        $ questionpreset = "photios1"
        if quest_reachthepaganvillage == 1:
            $ renpy.notify("Journal updated: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
        if not quest_reachthepaganvillage:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("New entry: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
        $ description_highisland11 = "According to {color=#f6d6bd}Photios{/color}, the direct route from his village to the island is crowded with harpies, but having an inexperienced crew would make taking the longer path quite tiring."
        $ description_greenmountaintribe09 = "Apparently they forbade other villages to enter {color=#f6d6bd}High Island{/color}."
        menu:
            '“Why, are you a sailor now?” He doesn’t hide his sneer, but after you say you may need to get there, he reaches for the beak on his neck. “Don’t you know that visiting the island is forbidden? Not just by {color=#f6d6bd}The Green Mountain Tribe{/color}, but because it’s a dangerous place. Wicked, and wild.”
            \n\n“So you haven’t been there?” You ask gently.
            \n\n“Right, and I don’t plan to. Them harpies sit on every rock on the route from our pier to the island, and it would take twice as long to sail around them. Rowing there would exhaust anyone, barring the most experienced arms.”
            '
            '(photios1 set)':
                pass

    label galerocks_photios_quest_spiritrock01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure you don’t need help with something that would fit my... Skills? I spend many hours on the road.”')
        menu:
            'He gives you a long look. “You know what, outsider? There’s something you could do for me, you can’t really ruin it by trying. I need you to help my daughter, {color=#f6d6bd}Phoibe{/color},” seeing your look, he raises his hands. “Don’t worry, she’s... Fine. Merely spell-less. For generations, my family used pneuma to lure fish and hold our breaths, but no matter how much she practices, she can’t cast even the tiniest spell. There’s something wrong with her soul,” he pauses, and his voice grows pained. “She’s my only child, and I seek no new wife. I want her to have the choice to do whatever she wants, and it breaks me to think she won’t have a way to follow in my footsteps.”
            '
            '“I don’t really know how I can help you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t really know how I can help you.”')
                $ quest_spiritrock = 1
                $ renpy.notify("New entry: A Spirit Rock")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: A Spirit Rock{/i}')
                menu:
                    'His eyes are absent. “A few years ago our traders were at the home of {color=#f6d6bd}this weird enchantress{/color} by the eastern road, I don’t know her name. She lives close to the old watchtower, you can’t miss it. {i}If{/i} she’s alive, she may still have these weird rocks... {i}Spirit rocks{/i}, I think. They help weakened mages. Buy one, bring it here. Maybe eating some pneuma will help {color=#f6d6bd}Phoibe{/color} learn.”
                    '
                    '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                        jump galerocks_photios_quest_spiritrock_question_pay01
                    '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                        jump galerocks_photios_quest_spiritrock03
                    'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                        pass
                    '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                     jump galerocks_photios_quest_spiritrock_question_eudocia01
                    '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                        jump galerocks_photios_quest_spiritrock_question_phoibe01
                    '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                        jump galerocks_photios_quest_spiritrock_question_doubt01
                    '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                        jump galerocks_photios_quest_spiritrock_question_doubt02
                    '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                        $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                        $ galerocks_photios_quest_spiritrock_doubts_points += 1
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                        $ custom1 = "“Why, though?”"
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                        jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the spirit rock...”')
            menu:
                '“You’ve got it?”
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_question_pay01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my payment.”')
            $ galerocks_photios_quest_spiritrock_question_pay = 1
            menu:
                '“I’m not a drifter, I don’t hoard any savings. We gather everything in the keep, we do. A spirit rock should cost about ten coins. Since it’s quite a journey from here, I’m ready to pay almost everything I’ve got. Fifteen.”
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_question_eudocia01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about this {color=#f6d6bd}enchantress{/color}?”')
            $ galerocks_photios_quest_spiritrock_question_eudocia = 1
            $ description_eudocia07 = "According to {color=#f6d6bd}Photios{/color}, she’s “tall, with cold eyes. For the few days she was around, she kept to herself. People say she’s a witch, and a mad one at that.”"
            menu:
                '“Ehm, I’ve only seen her a few times, when I was a teenager... Though she was also young, I suppose. Tall, not as tall as I am,” he smiles briefly, “with cold eyes. For the few days she was around, she kept to herself. People say she’s a witch, and a mad one at that.”
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_question_phoibe01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What does your daughter think about all this?”')
            $ galerocks_photios_quest_spiritrock_question_phoibe = 1
            menu:
                '“What does {i}she{/i} think?” He looks at you as if you’re mad, then glances at the nearby fishers. “She’d be heartbroken to realize she’s soul-le... I mean, spell-less. I won’t tell her unless I have no other way. She’s merely a child. I’m doing what’s best for her.”
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_question_doubt01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This sounds like a very unusual healing attempt. Are you sure you want to try this?”')
            $ galerocks_photios_quest_spiritrock_question_doubt += 1
            menu:
                '“I’ve asked our sorcerers about what they felt when they used the stones. Their pneuma got stronger than on most days, and nothing bad happened to them. We risk nothing, {i}outsider{/i},” he says, with growing irritation, and stops himself from scratching the scars on his neck.
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_question_doubt02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you asked any herbalists, though? Maybe a priest, or another enchanter?”')
            $ galerocks_photios_quest_spiritrock_question_doubt += 1
            menu:
                '“Have you heard about the previous roadwarden? {color=#f6d6bd}Asterion{/color}?” You nod. “In spring, I sent him to one of the greatest mages in the peninsula, some druid, I think, and that old prick told me there was nothing he could do, you hear that? And I had {i}paid{/i} the messenger to learn this!” He squeezes his cloak even tighter to his side. “We have no herbalists here, but since the spirit rocks are safe, I’d rather spend my last coins for such a chance than try nothing and regret it.”
                '
                '“You forgot to mention my payment.”' if not galerocks_photios_quest_spiritrock_question_pay:
                    jump galerocks_photios_quest_spiritrock_question_pay01
                '“Prepare the dragon bones. I have one with me.”' if galerocks_photios_quest_spiritrock_question_pay and item_spiritrock:
                    jump galerocks_photios_quest_spiritrock03
                'I don’t have a spirit rock with me. (disabled)' if galerocks_photios_quest_spiritrock_question_pay and not item_spiritrock:
                    pass
                '“What can you tell me about this {color=#f6d6bd}enchantress{/color}?”' if not galerocks_photios_quest_spiritrock_question_eudocia:
                 jump galerocks_photios_quest_spiritrock_question_eudocia01
                '“What does your daughter think about all this?”' if not galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_question_phoibe:
                    jump galerocks_photios_quest_spiritrock_question_phoibe01
                '“This sounds like a very unusual healing attempt. Are you sure you want to try this?”' if not galerocks_photios_quest_spiritrock_question_doubt:
                    jump galerocks_photios_quest_spiritrock_question_doubt01
                '“Have you asked any herbalists, though? Maybe a priest, or another enchanter?”' if galerocks_photios_quest_spiritrock_question_doubt == 1:
                    jump galerocks_photios_quest_spiritrock_question_doubt02
                '“I think what you’re asking for may be risky...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and not galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think what you’re asking for may be risky...”')
                    $ custom1 = "“Why would it be? No one has ever been hurt by the previous stones.”"
                    $ galerocks_photios_quest_spiritrock_doubts_points += 1
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“Let’s discuss this once more...”' if galerocks_photios_quest_spiritrock_question_doubt > 1 and galerocks_photios_quest_spiritrock_doubts_points:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss this once more...”')
                    $ custom1 = "“Why, though?”"
                    jump galerocks_photios_quest_spiritrock_doubts01
                '“I’ll tell you when I have a spirit rock.”' if galerocks_photios_quest_spiritrock_question_pay:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I have a spirit rock.”')
                    jump galerocksphotiosafterinteraction01

        label galerocks_photios_quest_spiritrock_doubts01:
            if galerocks_photios_quest_spiritrock_doubts_points >= 8:
                $ quest_spiritrock = 2
                $ coins += 5
                show screen notifyimage( "Quest completed: A Spirit Rock\n+5", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Spirit Rock. +5 {image=cointest}{/i}')
                $ galerocks_photios_quest_spiritrock_dayofcompleting = day
                $ quest_spiritrock_description04 = "I didn’t deliver the stone, but I collected my reward."
                $ questionpreset = "photios1"
                $ galerocks_photios_friendship += 1
                $ galerocks_work_hours += 8
                $ minutes += 5
                if galerocks_photios_quest_spiritrock_doubts_phoibe:
                    menu:
                        'He looks at you in silence. “So these people... And even {color=#f6d6bd}Phoibe{/color}... I need to speak with her myself,” he observes you in silence, then tells you to wait a few moments. After his return, he hands you a few dragon bones. “That’s for all the riding. Forget about the stone.”
                        \n\nHe looks north. “I don’t know what to think about all this. Do you need anything else?”
                        '
                        '(photios1 set)':
                            pass
                else:
                    menu:
                        'He looks at you in silence. “All these people... You traveled to all those places to make sure I won’t hurt {color=#f6d6bd}Phoibe{/color}?” He observes you in silence, then tells you to wait a few moments. After his return, he hands you a few dragon bones. “That’s for all the riding. Forget about the stone.”
                        \n\nHe looks north. “I don’t know what to think about all this. Do you need anything else?”
                        '
                        '(photios1 set)':
                            pass
            else:
                if pc_class == "scholar" and not galerocks_photios_quest_spiritrock_doubts_knowledge:
                    $ at_unlock_knowledge = 1
                    $ at = 0
                menu:
                    '[custom1]
                    '
                    '“I’ve studied many tales, both legends and archives. There is no alchemy that could change the nature of a spell-less soul.”' ( condition="at == 'knowledge' and not galerocks_photios_quest_spiritrock_doubts_knowledge" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve studied many tales, both legends and archives. There is no alchemy that could change the nature of a spell-less soul.”')
                        $ custom1 = "“So now you ain’t only a drifter, but also a scholar? If you’re so smart, maybe get back to your pens and ink, and leave the risk to me.”"
                        $ galerocks_photios_quest_spiritrock_doubts_knowledge = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 1
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“I talked to {color=#f6d6bd}Phoibe{/color}. She doesn’t seem to care much about pneuma, but it hurts her to see your disappointment.”' if galerocks_phoibe_firsttime and not galerocks_photios_quest_spiritrock_doubts_phoibe:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I talked to {color=#f6d6bd}Phoibe{/color}. She doesn’t seem to care much about pneuma, but it hurts her to see your disappointment.”')
                        $ custom1 = "“{i}Disappointment{/i}? But I just... I would never!” His voice swings between shouts and whispers. “I’m just trying to help her, any parent would do that for their only child.”"
                        $ galerocks_photios_quest_spiritrock_doubts_phoibe = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 3
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“{color=#f6d6bd}Eudocia{/color} herself told me the stone will likely kill any shell that can’t hold the stone’s pneuma.”' if eudocia_about_spiritrock_problem and not galerocks_photios_quest_spiritrock_doubts_eudocia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color} herself told me the stone will likely kill any shell that can’t hold the stone’s pneuma.”')
                        $ custom1 = "His face turns pale. “She said this?” After he clears his throat, he squeezes the monstrous beak on his chest, and his courage returns. “Then you’ve spoken with her, and you know she’s crazy. Instead of chatting with people, just bring me what I’m paying you for.”"
                        $ galerocks_photios_quest_spiritrock_doubts_eudocia = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 2
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“I traveled to {color=#f6d6bd}the old druid{/color} you had mentioned. He’s convinced you need to accept the way the spirits shaped your daughter’s soul, not change it.”' if druidcave_druid_about_spiritrock and not galerocks_photios_quest_spiritrock_doubts_druid:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I traveled to {color=#f6d6bd}the old druid{/color} you had mentioned. He’s convinced you need to accept the way the spirits shaped your daughter’s soul, not change it.”')
                        $ custom1 = "“{i}Spirits{/i}? Why would you even listen to this pagan nonsense? He’s just pushing his lies into you, he is.”"
                        $ galerocks_photios_quest_spiritrock_doubts_druid = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 1
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“{color=#f6d6bd}Thyrsus{/color}, the warlock from {color=#f6d6bd}White Marshes{/color}, told me his village is weak in pneuma, and if there would be any way to prevent spell-lessness, his people would do everything to find it. But there’s none.”' if thyrsus_about_spiritrock and not galerocks_photios_quest_spiritrock_doubts_thyrsus:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, the warlock from {color=#f6d6bd}White Marshes{/color}, told me his village is weak in pneuma, and if there would be any way to prevent spell-lessness, his people would do everything to find it. But there’s none.”')
                        $ custom1 = "“Who cares about some skeleton shaggers,” he gestures for you to stop, but his voice is far from convinced. “I told you, I {i}may{/i} be wrong, but it doesn’t mean that using the stone is going to be dangerous.”"
                        $ galerocks_photios_quest_spiritrock_doubts_thyrsus = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 1
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“{color=#f6d6bd}Aeli{/color}, the voice of the monastery, says that you need to forget the tales about being {i}soul-less{/i}. Not casting spells doesn’t make someone a lesser human, Wright’s Tablets are clear on that.”' if aeli_about_spiritrock and not galerocks_photios_quest_spiritrock_doubts_aeli:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Aeli{/color}, the voice of the monastery, says that you need to forget the tales about being {i}soul-less{/i}. Not casting spells doesn’t make someone a lesser human, Wright’s Tablets are clear on that.”')
                        $ galerocks_church_knowsabout += 1
                        $ custom1 = "“How does he...” He suddenly scowls at you. “Fine, if the monks say The Wright says so, I’ll believe it. But wouldn’t you try to heal a cut arm, or a broken back? Even if her soul is, well, {i}in her{/i}, it’s going to struggle.”"
                        $ galerocks_photios_quest_spiritrock_doubts_aeli = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 2
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    '“I spoke with {color=#f6d6bd}The Tribe of The Green Mountain{/color}. They know many tales of weak wizards growing in strength during their long and dangerous journeys, the same way warriors and hunters do, but none of these stories suggests that a spell-less human may become a sorcerer.”' if cephasgaiane_about_spiritrock and not galerocks_photios_quest_spiritrock_doubts_greenmountain:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with {color=#f6d6bd}The Tribe of The Green Mountain{/color}. They know many tales of weak wizards growing in strength during their long and dangerous journeys, the same way warriors and hunters do, but none of these stories suggest that a spell-less human may become a sorcerer.”')
                        $ custom1 = "“You’ve been to their tribe and this is what they’ve told you?” His eyes and voice are distrustful, but seeing your stance, he lets out a sigh. “We’re not {i}in{/i} the old stories, outsider. Things change, people get smarter. Even our boats get better with every generation.”"
                        $ galerocks_photios_quest_spiritrock_doubts_greenmountain = 1
                        $ galerocks_photios_quest_spiritrock_doubts_points += 2
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocks_photios_quest_spiritrock_doubts01
                    'I could look for people who have something to say about this. (disabled)' if not cephasgaiane_about_spiritrock or not aeli_about_spiritrock or not thyrsus_about_spiritrock or not eudocia_about_spiritrock_problem or not druidcave_druid_about_spiritrock or not galerocks_phoibe_firsttime:
                        pass
                    '“That’s all I have to say.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I have to say.”')
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump galerocksphotiosafterinteraction01
                    '“I don’t know how to convince you, but you’re asking me to do something really risky. The deal is off.”' if galerocks_photios_quest_spiritrock_doubts_points >= 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know how to convince you, but you’re asking me to do something really risky. The deal is off.”')
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        $ galerocks_photios_friendship -= 5
                        $ galerocks_reputation -= 1
                        $ quest_spiritrock = 3
                        $ renpy.notify("Quest completed: A Spirit Rock")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Spirit Rock{/i}')
                        $ galerocks_photios_quest_spiritrock_dayofcompleting = day
                        $ quest_spiritrock_description04 = "I called off the deal."
                        $ description_asterion14 = "According to {color=#f6d6bd}Photios{/color}, Asterion was “useless”, for he refused to give a spirit rock to his daughter."
                        $ questionpreset = "photios1"
                        if pc_hp >= 4 or pc_class == "warrior":
                            $ custom1 = "he tries to hit your chest with an open palm, but you dash back quickly, with your instincts already moving your hand toward your blade"
                        else:
                            $ custom1 = "he hits your chest with an open palm, and you step back awkwardly"
                        menu:
                            '“Don’t you dare to tell me how to raise my child, you drifting piece of shit,” [custom1]. Surprised, he looks you in the eyes with anger. “As useless as the previous one. That’s why I don’t pay any vagabond upfront.”
                            \n\nA man with a thick beard approaches the two of you, more to make sure his friend is safe than to ease the tensions. After a few more breaths, {color=#f6d6bd}Photios{/color} scratches his neck and bites his upper lip. “What else do you want, {i}outsider{/i}?”
                            '
                            '(photios1 set)':
                                pass

        label galerocks_photios_quest_spiritrock03:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Prepare the dragon bones. I have one with me.”')
            $ galerocks_photios_friendship += 2
            $ galerocks_reputation += 1
            $ item_spiritrock -= 1
            $ quest_spiritrock = 2
            $ coins += 15
            show screen notifyimage( "Quest completed: A Spirit Rock\n+15", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Spirit Rock. +15 {image=cointest}{/i}')
            $ galerocks_phoibe_coma_dayoff = day+1
            $ galerocks_photios_quest_spiritrock_dayofcompleting = day
            $ quest_spiritrock_description04 = "I collected my reward."
            $ questionpreset = "photios1"
            menu:
                'He lets out a triumphant shout. “Good job, roadwarden! I’ll give it to her this very evening. I’ll just grab your pay.”
                \n\nAfter a few minutes, your pouch gets much larger, and the man shows other fishers his new medicament, gaining their encouraging smiles and questions.
                '
                '(photios1 set)':
                    pass

    label galerocks_photios_quest_spiritrockaskingaboutphoibe01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How’s {color=#f6d6bd}Phoibe{/color} doing?”')
        $ galerocks_photios_quest_spiritrock_about_phoibe_after = 1
        $ questionpreset = "photios1"
        if galerocks_phoibe_coma:
            menu:
                '“She’s far from well, stranger,” he avoids your eyes. “She sucked on the stone, she did, went to sleep right after... And is still sleeping. Nothing wakes her up. Touch, water, shouts...” He stops when his voice cracks.
                '
                '(photios1 set)':
                    pass
        elif galerocks_photios_quest_spiritrock_doubts_phoibe:
            $ galerocks_reputation += 1
            $ galerocks_photios_friendship += 2
            $ pc_goal_iwanttohelppoints += 1
            menu:
                '“She’s alright,” he meets your eyes with a weak smile. “She’s planning to be either a woodcutter, or a tailor, but I don’t think {color=#f6d6bd}Rufina{/color} needs any help right now. To me, she can be even a carrier, if she decides so. Better than an empty shell.” He shuts his eyelids, holding tears. “You stopped me from shattering the very last shard of my family, [pcname]. Thank you.”
                '
                '(photios1 set)':
                    pass
        else:
            menu:
                '“She’s the same as she was yesterday, and the day before that,” he avoids your eyes. “Don’t ask me anymore, outsider. I don’t want to think about the time she’s going to ask me why she’s broken.”
                '
                '(photios1 set)':
                    pass

    label galerocks_photios_about_empresscarp01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was sent here by an old druid from the South. He claims that you owe him a male empress carp.”')
        $ galerocks_photios_about_empresscarp = 1
        if quest_spiritrock == 2:
            $ questionpreset = "photios1"
            $ galerocks_photios_about_empresscarp_ordered = day
            if not galerocks_phoibe_coma_dayoff:
                menu:
                    'He nods with enthusiasm. “Right, I guess that pagan was right all along, he was. I’ll have your fish tomorrow, stranger. I’ll look for it myself.”
                    '
                    '(photios1 set)':
                        pass
            else:
                menu:
                    'He nods slowly. “Right, I guess that pagan was right all along, he was. I’ll have your fish tomorrow, stranger. I’ll look for it myself.”
                    '
                    '(photios1 set)':
                        pass
        else:
            $ questionpreset = "photios1"
            $ galerocks_photios_about_empresscarp_ordered = day
            menu:
                '“What? I owe nothing to that old fool. I can have it here tomorrow, if you want, but better have a coin with you. I need to ask someone to look for it with a net, and that will take hours.”
                '
                '(photios1 set)':
                    pass

        label galerocks_photios_about_empresscarp02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you catch the empress carp?”')
            if pc_area == "galerocks":
                $ custom1 = "He approaches the nearby shed and brings you a bucket covered with lids that are held by hemp cords. He lets you hold it for a bit - it’s heavy and its weight shifts, as if it’s filled with water."
            if pc_area == "beforebeach":
                $ custom1 = "He approaches one of the wagons, which carries a few buckets covered with lids that are held by hemp cords. He lets you hold it for a bit - it’s heavy and its weight shifts, as if it’s filled with water."
            if pc_area == "beach":
                $ custom1 = "He approaches the nearby shed and brings you a bucket covered with lids that are held by hemp cords. He lets you hold it for a bit - it’s heavy and its weight shifts, as if it’s filled with water."
            $ galerocks_photios_about_empresscarp_caught = 1
            if quest_spiritrock == 2:
                $ questionpreset = "photios1"
                $ galerocks_photios_about_empresscarp_bought = day
                $ item_empresscarp_timelimit = day
                $ item_empresscarp += 1
                $ renpy.notify("Journal updated: An Empress Carp. You received a bucket with a fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: An Empress Carp. You received a bucket with a fish.{/i}')
                menu:
                    '“Right, and a few of them, but most of them females.” [custom1] “Better deliver it quickly, or it’s going to choke itself to death, ehm, or die of hunger, I don’t know much about keeping fish alive. But {i}if{/i} it dies, I can sell you another one for a coin. Remember, this one is free because of what you did for me, but that’s it.”
                    '
                    '(photios1 set)':
                        pass
            else:
                menu:
                    '“Right, and a few of them, but most of them females.” [custom1] “You’ll need to deliver it quickly, or it’s going to choke itself to death, ehm, or die of hunger, I don’t know much about keeping fish alive. But {i}if{/i} it dies, I can sell you another one for another coin.”
                    '
                    '“Fine.” I pay him one dragon bone.' if coins:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.” I pay him one dragon bone.')
                        $ galerocks_photios_about_empresscarp_bought = day
                        $ item_empresscarp_timelimit = day
                        $ item_empresscarp += 1
                        $ coins -= 1
                        show screen notifyimage( "Journal updated: An Empress Carp\nYou received a bucket with a fish\n-1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: An Empress Carp. You received a bucket with a fish. -1 {image=cointest}{/i}')
                        $ questionpreset = "photios1"
                        jump galerocksphotiosafterinteraction01
                    'I can’t afford it. (disabled)' if coins == 0:
                        pass
                    '“I’ll tell you when I’m ready to take it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I’m ready to take it.”')
                        jump galerocksphotiosafterinteraction01

        label galerocks_photios_about_empresscarp02alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still need an empress carp.”')
            if quest_spiritrock == 2:
                $ questionpreset = "photios1"
                $ galerocks_photios_about_empresscarp_bought = day
                $ item_empresscarp_timelimit = day
                $ item_empresscarp += 1
                $ renpy.notify("Journal updated: An Empress Carp. You received a bucket with a fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: An Empress Carp. You received a bucket with a fish.{/i}')
                menu:
                    '“You helped me, so fine, this one is for free, but that’s it.”
                    '
                    '(photios1 set)':
                        pass
            else:
                menu:
                    '“My price is the same.”
                    '
                    '“Fine.” I pay him one dragon bone.' if coins:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.” I pay him one dragon bone.')
                        $ galerocks_photios_about_empresscarp_bought = day
                        $ item_empresscarp_timelimit = day
                        $ item_empresscarp += 1
                        $ coins -= 1
                        show screen notifyimage( "Journal updated: An Empress Carp\nYou received a bucket with a fish\n-1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: An Empress Carp. You received a bucket with a fish. -1 {image=cointest}{/i}')
                        $ questionpreset = "photios1"
                        jump galerocksphotiosafterinteraction01
                    'I can’t afford it. (disabled)' if coins == 0:
                        pass
                    '“I’ll tell you when I’m ready to take it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I’m ready to take it.”')
                        jump galerocksphotiosafterinteraction01

        label galerocks_photios_about_empresscarp03:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need another empress carp.”')
            menu:
                '“You killed it? Too much fun on the road?” He sneers. “Right. My price is the same.”
                '
                '“Fine.” I pay him one dragon bone.' if coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.” I pay him one dragon bone.')
                    $ galerocks_photios_about_empresscarp_bought = day
                    $ item_empresscarp_timelimit = day
                    $ item_empresscarp += 1
                    $ coins -= 1
                    show screen notifyimage( "Journal updated: An Empress Carp\nYou received a bucket with a fish\n-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: An Empress Carp. You received a bucket with a fish. -1 {image=cointest}{/i}')
                    $ questionpreset = "photios1"
                    jump galerocksphotiosafterinteraction01
                'I can’t afford it. (disabled)' if coins == 0:
                    pass
                '“I’ll tell you when I’m ready to take it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I’m ready to take it.”')
                    jump galerocksphotiosafterinteraction01

label galerocksaquilaALL: # {color=#f6d6bd}Aquila{/color}, the bath man
    label galerocksaquila01firsttime:
        $ galerocks_aquila_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ shop = "galerocksbath"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay aquila at basicfade
        menu:
            'The steep banks are damp, so you head upstream, to the wooden bridge, but you can hardly reach any water with your fingers there. You consider getting undressed, but a sudden voice behind you tells you to quit it. “This current is strong, it’ll catch you and bam,” the man swings his arm, “you’ll crack your skull against the rocks,” he points downstream.
            \n\nHe’s a large person, with heavy boots that are dirty from mud, and a necklace made of a colorful shell as large as your hand. He approaches you, holding a few empty buckets, each one attached to a rope. He places them on the logs and crouches down, filling the buckets one by one.
            '
            'I ask him about washing myself at a well.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask him about washing myself at a well.')
                $ renpy.notify("New trader unlocked.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
                if not galerocks_bath_free:
                    $ custom1 = ""
                else:
                    $ custom1 = "\n\nAfter you explain that you were promised a free service, he raises his voice. “Right, so you’re that roadwarden! Very well, no fees for you.”"
                menu:
                    'He frowns. “Ehm, what are you, a child? What’s your name?” After you introduce yourself, he gives you a gentle nod. “And I’m {color=#f6d6bd}Aquila{/color}. We bathe in tubs, right? I have warm water in the shed,” he directs your eyes at the boulder next to the path, though it in no way resembles {i}sheds{/i} that one would find in the city. He straightens up and carries the buckets up the bank, one by one. “Either help me carry water around the village for a few hours or pay me if you’re lazy enough, I’ll make you a fine bath and wash your togs.”[custom1]
                    \n\nHe places the last bucket next to the boat, and you notice that another man is already taking one of them to the eastern gate. “I could also sell you a bottle of perfumes, though it won’t be of much use if you have no soap,” he grins with his yellow teeth, as if there’s a punchline hidden in his words. “We pick flowers of roses, violets, lavender, cherry... Good for hair, ears, and wrists. Just don’t drink it.”
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01

    label galerocksaquila01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerocksbath"
        show galerocksoverlay aquila at basicfade
        menu:
            'You find him while he’s collecting empty buckets around the village, ready to carry them to his regular spot at the bridge. “What is it, outsider? Got dirty?”
            '
            '{image=cointest} “Tell me about your services.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                jump galerocksaquila02
            '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_aquila_about_recruitahunter01
            '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                jump galerocks_aquila_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksaquila02:
        $ shop = "galerocksbath"
        show screen shopscreen with dissolve
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay aquila at basicfade
        menu:
            'He gladly gestures for you to follow him.
            '
            '{image=cointest} “Tell me about your services.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                jump galerocksaquila02
            '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_aquila_about_recruitahunter01
            '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                jump galerocks_aquila_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksbathafterinteraction:
        menu:
            'He reaches for a bucket and looks around, seeking a spot where it may be of use.
            '
            '{image=cointest} “Tell me about your services.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                jump galerocksaquila02
            '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_aquila_about_recruitahunter01
            '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                jump galerocks_aquila_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksbathbuyingperfume:
        $ quarters += 1
        $ cleanliness_equipment += 1
        menu:
            'He grins and asks you to wait with your horse, then heads toward the western gate. Once he returns, he carries a small, wooden box. He places it inside the shed, on one of the old barrels. The box is filled with wool and small, earthenware bottles, which he opens one at a time, allowing you to get a whiff of their contents.
            \n\n“We make them as a village, the coins ain’t for me,” he explains. “But they’re nice, ain’t they? Which one do you want?”
            '
            '“Rose.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Rose.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Rose"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Lavender.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Lavender.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Lavender"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Violet.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Violet.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Violet"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Rosemary.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Rosemary.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Rosemary"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Clove.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Clove.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Clove"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Cherry.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Cherry.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Cherry"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He smiles, picks up a bottle, and puts it on the barrel, waiting for you to smell it again before you pay. You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01
            '“Just give me a nice one.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just give me a nice one.”')
                $ galerocks_aquila_shop_perfume_bought = 1
                $ item_perfume = 1
                $ item_perfume_type = "Cherry"
                if galerocks_reputation < 4:
                    $ galerocks_aquila_shop_perfume_price = 6
                elif galerocks_reputation < 8:
                    $ galerocks_aquila_shop_perfume_price = 5
                else:
                    $ galerocks_aquila_shop_perfume_price = 4
                $ coins -= galerocks_aquila_shop_perfume_price
                show screen notifyimage( "You add the perfume to your travel set.\n-%s" %galerocks_aquila_shop_perfume_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the bottle of perfume. -%s {image=cointest}{/i}' %galerocks_aquila_shop_perfume_price)
                menu:
                    'He scowls at you, then picks up a bottle and puts it on the barrel, waiting for you to pay. “Cherry it is, then.” You add the bottle to your other fragile pieces of equipment, and the man closes the box again and carries it away.
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01

    label galerocks_aquila_about_recruitahunter01:
        if (galerocks_reputation+appearance_charisma) < 4 and not galerocks_aquila_shop_perfume_bought:
            $ quest_recruitahunter_spokento_aquila_gray = 1
            menu:
                'He looks into a bucket, as if seeking escape from your gaze. “Nah. It’s not right, talking behind one’s back with a stranger.”
                '
                '{image=cointest} “Tell me about your services.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                    jump galerocksaquila02
                '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                    jump galerocks_aquila_about_recruitahunter01
                '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                    jump galerocks_aquila_about_recruitahunter01alt
                'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                    pass
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump galerocksafterinteraction01
        else:
            label galerocks_aquila_about_recruitahunter02:
                $ quest_recruitahunter_spokento_aquila = 1
                $ quest_recruitahunter_cassia_points += 1
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
                    $ quest_recruitahunter_cassia_points_notify2 = 1
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                menu:
                    'He raises an eyebrow, then looks around, making sure nobody approaches his shed. “There ain’t much to say. All them guards are trouble from time to time, but she’s lucky to still have the job. No one would take her anyway, she goes for days without washing her togs, and keeps arguing left and right. The best she’s for is distracting beasts, you get it.”
                    '
                    '{image=cointest} “Tell me about your services.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about your services.”')
                        jump galerocksaquila02
                    '“Any thoughts on {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_aquila_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any thoughts on {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_aquila_about_recruitahunter01
                    '“Tell me about {color=#f6d6bd}Cassia{/color}.”' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) >= 4) or (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and galerocks_aquila_shop_perfume_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
                        jump galerocks_aquila_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and (galerocks_reputation+appearance_charisma) < 4) and (not quest_recruitahunter_spokento_aquila and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_aquila_gray and not galerocks_aquila_shop_perfume_bought):
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01

        label galerocks_aquila_about_recruitahunter01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Cassia{/color}.”')
            jump galerocks_aquila_about_recruitahunter02

label galerocksalbusALL: # {color=#f6d6bd}Albus{/color}, the salter
    label galerocksalbus01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_albus_firsttime = 1
        show galerocksoverlay albus at basicfade
        menu:
            'The building has many entrances and windows, and each of them lets out so much steam that one could take this place for a city sauna.
            \n\nYou address a man that’s carrying a basket of firewood. “Ehm, I’m {i}working{/i},” he growls, “speak with {color=#f6d6bd}Albus{/color}!” The last word is shouted through the open door, to another worker. Hearing it, he looks in your direction, puts away a wooden mould, and heads outside, taking a few deep breaths of cool air.
            \n\n“Cheers, cheers. Are you by yourself? Who do you represent?” He’s not older than thirty. Matching his name, his skin and hair are white, though with a healthy pink hidden in his cheeks, nose, and lips, making him look as if he’s blushing.
            \n\nWhen you vaguely state that you’re “from {color=#f6d6bd}Hovlavan{/color},” his curiosity is already satisfied. “Alright, good to have you back after, what, five years? Our process is the same, and so the lumps look the same. The guild will be satisfied, better keep your head low.”
            '
            'I follow him inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him inside.')
                menu:
                    'The tour takes a good couple of minutes, and while your guide seems very confident in describing the salt making process step-by-step in great detail, he doesn’t take into consideration that you may be completely unqualified to have a conversation about the topic. You try to catch the gist of it, though neither the sound of flames and scratching, nor the humid air or the smell of sweaty bodies help you to focus.
                    \n\nThe brine is carried here from a cave pond, deep beneath the village, and then boiled in large open pans, made of coarse ceramic, heated by stoves. As water evaporates, it leaves salt behind and steams a few planks above it, before they get back to the carpenters. The salt is carried onto a drying surface, then lumped into white “bricks” with the use of wooden moulds.
                    \n\n“Many things can go wrong,” he finishes his tale, “but nothing goes to waste. Them shattered lumps get into our fish barrels, all is good. We won’t sell you anything of poor quality.”
                    '
                    'I try to learn a bit about the price.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to learn a bit about the price.')
                        menu:
                            'He gives you a few numbers - how many coins, how much flour, or how much iron the locals would take for a single lump, and at first the prices surprise you, but you then take one of the clumps and rub it with your thumb. One brick would be more than a household would use in a year.
                            \n\n{color=#f6d6bd}Albus{/color} interrupts your thoughts. “Questions?” You put the salt on a table and glance at the steaming pan again. Even though there are only three workers here, you realize the production must consume a mound of firewood every year.
                            '
                            'I ask him where they get their trees from.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask him where they get their trees from.')
                                menu:
                                    'He doesn’t answer right away, choosing his words carefully. “We have supplies, and we trade for them with other villages, or at least used to. We cut trees as well, used to do so more, back in the day. We had a lumberjack hamlet, far away, so the beasts didn’t get angry, they didn’t.”
                                    '
                                    'I thank him for his time and let him work in peace.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank him for his time and let him work in peace.')
                                        $ quarters += 1
                                        $ galerocks_npcsmet += 1
                                        if galerocks_resource_barrels or galerocks_resource_fish:
                                            $ galerocks_resource_salt = "and find a great amount of salt"
                                        else:
                                            $ galerocks_resource_salt = "find a great amount of salt"
                                        jump galerocksafterinteraction01

    label galerocksalbus01:
        show galerocksoverlay albus at basicfade
        menu:
            'The workers carry buckets of brine, boil it in open pans, look after fuel, form lumps of salt in wooden moulds... From time to time, their sweat mixes with the water.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerocksdomitiaALL: # {color=#f6d6bd}Domitia{/color}, the cooper
    label galerocksdomitia01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_domitia_firsttime = 1
        $ galerocks_npcsmet += 1
        show galerocksoverlay domitia at basicfade
        menu:
            'The coopers, and carpenters in general, have their space at the edge of the village, separated from the saltery with a stone wall that catches the shavings before they reach the fish, and which are then swept into a pile and moved to the smokehouse.
            \n\nYou walk between the four woodworkers while the last one, a young woman with an apologetic smile, leaves the thatched store. She’s wearing a heavy, worn robe, half-brown, half-yellow, covered with dust and woodchips, and carries under her arm a stack of willow withies. Two small seashells, in many shades of orange, are hanging from her ears. “Ehm, stranger. We need space here.”
            '
            '“I was hoping to learn a bit about your work. I’m from {color=#f6d6bd}Hovlavan{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping to learn a bit about your work. I’m from {color=#f6d6bd}Hovlavan{/color}.”')
                menu:
                    'With a sigh of relief, she approaches an unfinished barrel, whose staves are getting pressed together with a dense cage of weaved withies. In the city, the coopers would use old, iron hoops, which would take less than a twentieth of the labor. She drops her delivery and touches your shoulder with her large, strong hand.
                    \n\n“So the guild wants to speak trade again? Very well, alright, {i}very well{/i}. Let me show you around, I’m {color=#f6d6bd}Domitia{/color}, the head carpenter, I guess,” she states with hesitation and one of her workers mockingly snorts. {color=#f6d6bd}Your guide{/color} laughs in response. “Shag an eel, idiot.” Her small crew laughs as well.
                    '
                    'I smile as well.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile as well.')
                        $ custom1 = "Her teeth are mostly yellow, but straight. “My predecessor lost his eyes to a harpy a few days back, so I’m new to this role. But don’t worry, I know what I’m doing,” she confidently straightens up."
                        jump galerocksdomitia01firsttime02
                    'I tellingly look toward the gate.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tellingly look toward the gate.')
                        $ custom1 = "She covers her embarrassment with a fake cough."
                        label galerocksdomitia01firsttime02:
                            menu:
                                '[custom1] “Right. We have two types of work. Barrels, and everything else. On good days, we make a barrel. On bad days, we fail,” she laughs, “but that’s fine, we can always get it done after a good sleep.”
                                \n\nShe goes into greater detail, and your eyes start to wander between the benches, pieces of cut wood, mallets, axes, and shaving tools. Noticing this, she nods toward the other workers. “When the barrels are resting or bending, we do other things, but only for our own farmers, builders, fishers. {color=#f6d6bd}Navica{/color} is the most experienced of us, so she makes boats, paddles, right? Responsible tasks.” The tiny woman she points at doesn’t even raise her eyes. “We sometimes make furniture, we do, but merely when something breaks.”
                                '
                                '“So the barrels are the most important. Do you have enough wood for them?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So the barrels are the most important. Do you have enough wood for them?”')
                                    menu:
                                        '“Not really! We use oak, beech, and pine, but staves have to rest for three years, sometimes two, sometimes four. Every day, I bring fourteen staves and two headers here, and we replace them with new ones. We’re careful with what we have, it’s hard to plan years ahead.”
                                        \n\nShe gives you a warm smile. “You need to talk about it with my neighbors first, but maybe the guild would like to provide us with timber? We’d rather barter than lock the coins in the keep, you see.”
                                        '
                                        '“The guild won’t move wood from their own stalls so far to the north, but they may help you set up a new hamlet, or find you a partner who lives closer to {color=#f6d6bd}Hag Hills{/color}.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The guild won’t move wood from their own stalls so far to the north, but they may help you set up a new hamlet, or find you a partner who lives closer to {color=#f6d6bd}Hag Hills{/color}.”')
                                            menu:
                                                '“Right, it would need to be someone outside of the peninsula. Here everyone cuts only for themselves, they do, even those jesters from {color=#f6d6bd}Creeks{/color}. We used to have a camp of lumberjacks, but now our warehouse gets emptier every day.”
                                                \n\nFor a bit, you discuss with her the value of a wagon filled with logs or planks, but the discussion leaves your area of expertise quickly. You simply promise to get the message to the merchants, and {color=#f6d6bd}Domitia{/color} wishes you a safe journey.
                                                '
                                                'I take one more look around and leave the “workshop.”':
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take one more look around and leave the “workshop.”')
                                                    $ quarters += 1
                                                    $ galerocks_npcsmet += 1
                                                    $ galerocks_resource_barrels += 1
                                                    if galerocks_resource_salt:
                                                        $ galerocks_resource_barrels = "sell plenty of wood, "
                                                    else:
                                                        $ galerocks_resource_barrels = "sell plenty of wood "
                                                    jump galerocksafterinteraction01

    label galerocksdomitia01:
        show galerocksoverlay domitia at basicfade
        menu:
            'The carpenters work without haste, shaping the precious beams and planks carefully, yet confidently. The smell of raw fish from the saltery gets a bit too intense.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerocks_iuno_ALL: # {color=#f6d6bd}Iuno{/color}, the builder
    label galerocks_iuno_01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_iuno_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        show galerocksoverlay iuno at basicfade
        menu:
            'The locals explain that the centuries old caves need little work, and the humble fixes they put into the walls and sheds are taken care of whenever such a need arises. After a few minutes of chatting, one of the children leads you to an elderly woman responsible for looking after the condition of “them buildings” - the digger called {color=#f6d6bd}Iuno{/color}, already wrinkled, gray-haired, and slightly stooped.
            \n\nShe’s sitting at the eastern gate, placing tiny building blocks on the table, raising a tall tower without making it collapse. Her hands are steady and precise, and her large eyes blink so rarely that you want to rub your own.
            \n\nShe spares you a look and leans back, resting against the wall, then crosses her arms and critically observes her toys. “Cheers, stranger. I have time.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay iuno at basicfade
        if not galerocks_iuno_about_oldtunnel_cleared:
            $ custom1 = "outsider"
        else:
            $ custom1 = "roadwarden"
        menu:
            '[galerocks_iuno_fluff] “Cheers, [custom1].”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_oldtunnelopen01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The tunnel in the south is open again. The undead are gone.”')
        $ galerocks_iuno_about_oldtunnel_cleared = 1
        $ galerocks_iuno_about_oldtunnel_defeated = 1
        menu:
            'As {color=#f6d6bd}Iuno{/color} shakes the table, her toy structures fall apart. “Merely like that? You cleared all them awoken on your own?” After your nod, she looks at your axe, then at her toys. “Better tell our {color=#f6d6bd}headwoman{/color} about it, and I’ll talk with the others. We can move to some serious work in spring, but it would be better for us to do the groundwork before snow falls.”
            \n\nShe shuffles the wooden blocks and moves them into a single row. “And if the tunnel is somewhat safe, could you take a closer look at it, inspect the chambers? Report to me, and I’ll ask one of my neighbors to give you an easier time.” Even though she seems to put no thought into it, the blocks are now ordered from the brightest to the darkest.
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_oldtunnelopen01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The tunnel is open again.”')
        $ galerocks_iuno_about_oldtunnel_cleared = 1
        $ galerocks_iuno_about_oldtunnel_defeated = 1
        menu:
            '“Better tell our {color=#f6d6bd}headwoman{/color} about it, and I’ll talk with the others. We can move to some serious work in spring, but it would be better for us to do the groundwork before snow falls.”
            \n\nShe shuffles the wooden blocks and moves them into a single row. “And if the tunnel is somewhat safe, could you take a closer look at it, inspect the chambers? Report to me, and I’ll ask one of my neighbors to give you an easier time.” Even though she seems to put no thought into it, the blocks are now ordered from the brightest to the darkest.
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_oldtunnel01:
        $ galerocks_iuno_about_oldtunnel = 1
        menu:
            '“It’s older than any human soul, it is, but not ancient. Those who dug through the mountain were still around when I was but a small lass. The village saved everything it got from trade for more than a generation to bring the bronze gate from {color=#f6d6bd}Hovlavan{/color} here, the pickaxes, and all them tools and nails. It has a single, long corridor that reaches from one end to the other, and a few chambers on both sides, where travelers used to spend a night if they were desperate enough. Don’t try it without a group of guards, now. Monsters also love deep caves, and the days are getting colder.”
            '
            '“How come it’s locked in the first place?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How come it’s locked in the first place?”')
                if not quest_ruins_10yclue10 and quest_ruins == 1 and quest_ruins_description01:
                    $ renpy.notify("Journal updated: The Ruined Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                $ quest_ruins_10yclue10 = "The people of {color=#f6d6bd}Gale Rocks{/color} started neglecting their tunnel in the south."
                menu:
                    '“It depends on who you ask. Let’s just say that a great turmoil happened ten years ago, right? The settlements grew further apart, traded less. Keeping a garrison of fighters and builders at the tunnel brought little value. We had to put greater trust in our own work, not in the caravans, once again foraging, cutting trees, and farming. With time, more and more beasts gathered around the tunnel, getting used to seeing no pushback.”
                    \n\nShe looks at an old plank that’s been resting behind her stool. She compares its thickness with her toys, then reaches for a gouge and a hand saw. “Ehm. It was three years back when a few traders of ours went missing. Our searching group found the gate, locked from the inside. They tried to check it, but left the place when they saw moving shells, dead and fleshless. We’ve decided to clean it some day in the future, maybe hire a group of strangers to take the risk upon themselves,” she glances at you, “but so far none have reached our village.”
                    '
                    '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                        jump galerocks_iuno_about_oldtunnelopen01
                    '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                        jump galerocks_iuno_about_oldtunnelopen01alt
                    '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                        jump galerocks_iuno_about_defeated01
                    '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                        jump galerocks_iuno_about_hourglass01
                    '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                        jump galerocks_iuno_about_oldtunnel01
                    '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                        jump galerocks_iuno_about_oldtunnel01
                    '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                        jump galerocks_iuno_about_oldtunnel_explored01
                    'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                        pass
                    'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                        pass
                    '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                        jump galerocks_iuno_about_introduction01
                    '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                        jump galerocks_iuno_about_herself01
                    '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                        jump galerocks_iuno_about_keep01
                    '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                        jump galerocks_iuno_about_trade01
                    '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_iuno_about_recruitahunter01
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        jump galerocksafterinteraction01

    label galerocks_iuno_about_defeated01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”')
        $ galerocks_iuno_about_oldtunnel_defeated = 1
        menu:
            'As {color=#f6d6bd}Iuno{/color} shakes the table, her toy structures fall apart. “Merely like that? You cleared all them awoken on your own?” After your nod, she looks at your axe, then at her toys. “I don’t have it, I’m afraid. Its place is at the armory, in a hiding place behind the fake brick, marked with an hourglass. You need to press it with a pendant, like those we wear in our village. A clever mechanism, this one.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_hourglass01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where can I find an hourglass pendant?”')
        $ galerocks_iuno_about_oldtunnel_hourglass = 1
        menu:
            '“Ask {color=#f6d6bd}Rufina, the tailor{/color}. Tell her I’d like to give you one, as a gift.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_oldtunnel_explored01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve explored the entirety of the tunnel...”')
        $ galerocks_iuno_about_oldtunnel_explored = 1
        $ galerocks_reputation += 1
        $ quarters += 1
        menu:
            'After your initial report, {color=#f6d6bd}Iuno{/color} comes up with one question after another, and while some of them are specific and significant, others are absurdly simple, as if she’s making sure you’re not lying to her. You don’t know all of the answers, but in the end, she smiles at you, clapping her hands without a sound.
            \n\n“With that, we can gather timber, rocks, and tools, and I already know which ones will be just {i}perfect{/i}. Cheers, roadwarden. If you want, I can ask one of my neighbors to repay your hard work, and not just once.”
            '
            '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
                $ galerocks_food_free = 1
                $ custom1 = "“Right,” she starts to build a wall from the wooden blocks. “I’ll speak with {color=#f6d6bd}Porcia{/color}, the cook.”"
                jump galerocks_iuno_about_oldtunnel_explored02
            '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
                $ galerocks_fulvia_knowsabout = 1
                $ galerocks_sleep_free = 1
                $ custom1 = "“Right,” she starts to build a wall from the wooden blocks. “I’ll speak with {color=#f6d6bd}Fulvia{/color}, she should have a room to spare.”"
                jump galerocks_iuno_about_oldtunnel_explored02
            '“Maybe five free repairs of my gambeson?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
                $ galerocks_armorer_free += 5
                $ custom1 = "“Right,” she starts to build a wall from the wooden blocks. “I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor.”"
                jump galerocks_iuno_about_oldtunnel_explored02
            '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
                $ galerocks_bath_free = 1
                $ custom1 = "“Right,” she starts to build a wall from the wooden blocks. “I’ll speak with {color=#f6d6bd}Aquila{/color}, the bath man.”"
                jump galerocks_iuno_about_oldtunnel_explored02
            '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
                $ galerocks_navica_boat_price_base -= 10
                $ custom1 = "“Right,” she starts to build a wall from the wooden blocks. “I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker.”"
                jump galerocks_iuno_about_oldtunnel_explored02
            '“I don’t need any favors. Just make sure to tell everyone what I did, in {i}very{/i} kind words.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure to tell everyone what I did, in {i}very{/i} kind words.”')
                $ galerocks_reputation += 2
                $ custom1 = "“So kind-hearted you are, ehm?” She smiles. “Right, I’ll let the others know what a useful roadwarden you turned out to be.”"
                jump galerocks_iuno_about_oldtunnel_explored02

        label galerocks_iuno_about_oldtunnel_explored02:
            menu:
                '[custom1]
                '
                '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                    jump galerocks_iuno_about_oldtunnelopen01
                '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                    jump galerocks_iuno_about_oldtunnelopen01alt
                '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                    jump galerocks_iuno_about_defeated01
                '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                    jump galerocks_iuno_about_hourglass01
                '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                    jump galerocks_iuno_about_oldtunnel01
                '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                    jump galerocks_iuno_about_oldtunnel01
                '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                    jump galerocks_iuno_about_oldtunnel_explored01
                'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                    pass
                'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                    pass
                '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                    jump galerocks_iuno_about_introduction01
                '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                    jump galerocks_iuno_about_herself01
                '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                    jump galerocks_iuno_about_keep01
                '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                    jump galerocks_iuno_about_trade01
                '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                    jump galerocks_iuno_about_recruitahunter01
                '“Farewell.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                    jump galerocksafterinteraction01

    label galerocks_iuno_about_introduction01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was told you are the one who looks after the local construction works.”')
        $ galerocks_iuno_introduction = 1
        menu:
            '“That’s pretty much it, right,” she glances at the spread wooden blocks. “Every few springs or summers I gather a crew to build something new, or rather replace an old hovel with something fresh, but most of the days I just make sure that roofs don’t fall on our heads, and that the cribbing in the caves ain’t too moist. Then the coopers help me, or a bunch of fishers.” She gives your axe a long look, then reaches for her much smaller hatchet and shaves one of her toys slightly, narrowing it. “For centuries there’s been merely one digger at a time, and this custom serves us well, it does.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_herself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A {i}digger{/i} is an unusual name for your trade.”')
        $ galerocks_iuno_about_herself = 1
        menu:
            '“And what would be a {i}usual{/i} name in the city? A {i}builder{/i}?” After your shrug, {color=#f6d6bd}Iuno{/color} grasps one of her wooden blocks like a dagger. “Our forebears used to, ehm, {i}dig{/i} in rocks, widening the caves, and it was a name with great honor behind it. When I look around,” she does so, as to prove her point, “it reminds me of our long path. From hiding, to thriving, and on the surface.” She can’t hide her smile.
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_keep01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”')
        $ galerocks_iuno_about_keep = 1
        menu:
            'She looks in its direction. The whitewashed walls make it look brighter than many clouds. “We started when I was only a teen, still learning from the previous digger,” her voice is full of pride. “There used to be a humble watchtower there, with tents around it. Now we can all stay locked inside thick walls, but also shoot arrows from the wall, roof, and windows.”
            \n\nYou ask her if the keep has ever been used by the locals in combat, and she suddenly grows disheartened. “You would be surprised, you would. There are tales of dragons, pirates, and bandits... But all of those happened before the war. Those lands were different, though I can’t exactly say how.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_trade01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m with the merchants. Do you have enough building materials for your needs?”')
        $ galerocks_iuno_about_trade = 1
        menu:
            '“Better ask the coopers, they struggle with timber. The good thing about digging in hills is that we always have enough stone. Our rocks are crude, but we don’t need to sculpt, just pile them on,” she turns a few building blocks into a small wall.
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_iuno_about_recruitahunter01:
        $ quest_recruitahunter_spokento_iuno = 1
        menu:
            '“Ain’t she one of the guards? I don’t bother with kids’ problems,” she looks forward and makes a telling nod. “Speak with {color=#f6d6bd}Tatius{/color} there. He trains with every fighter in our tribe, he does.”
            '
            '“The tunnel in the south is open again. The undead are gone.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01
            '“The tunnel is open again.”' if oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_oldtunnelopen01alt
            '“I got rid off the undead from the old tunnel in the south, but I’m missing the key to the gate.”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and not galerocks_iuno_about_oldtunnel_defeated:
                jump galerocks_iuno_about_defeated01
            '“Where can I find an hourglass pendant?”' if not galerocks_iuno_about_oldtunnel_cleared and oldtunnel_exploration_scrap19_trygate and oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap13_open and galerocks_iuno_about_oldtunnel_defeated and not item_wingedhourglass and not galerocks_iuno_about_oldtunnel_hourglass:
                jump galerocks_iuno_about_hourglass01
            '“I’d like to learn more about the tunnel that leads through the mountain in the south.”' if not galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about the tunnel that leads through the mountain in the south.”')
                jump galerocks_iuno_about_oldtunnel01
            '“Tell me more about that tunnel.”' if galerocks_iuno_about_oldtunnel_cleared and not galerocks_iuno_about_oldtunnel:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about that tunnel.”')
                jump galerocks_iuno_about_oldtunnel01
            '“I’ve explored the entirety of the tunnel...”' if not galerocks_iuno_about_oldtunnel_explored and oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                jump galerocks_iuno_about_oldtunnel_explored01
            'I could still examine the tunnel for her. (disabled)' if not galerocks_iuno_about_oldtunnel_explored and not oldtunnel_inside_explored and galerocks_iuno_about_oldtunnel_cleared:
                pass
            'She wants me to open the tunnel. (disabled)' if not oldtunnel_inside_opened and not galerocks_iuno_about_oldtunnel_cleared and galerocks_iuno_about_oldtunnel:
                pass
            '“I was told you are the one who looks after the local construction works.”' if not galerocks_iuno_introduction:
                jump galerocks_iuno_about_introduction01
            '“A {i}digger{/i} is an unusual name for your trade.”' if not galerocks_iuno_about_herself and galerocks_iuno_introduction:
                jump galerocks_iuno_about_herself01
            '“Did {i}your{/i} crew build that keep on the hill? It must have taken you many years.”' if not galerocks_iuno_about_keep and galerocks_iuno_introduction:
                jump galerocks_iuno_about_keep01
            '“I’m with the merchants. Do you have enough building materials for your needs?”' if not galerocks_iuno_about_trade and galerocks_iuno_introduction:
                jump galerocks_iuno_about_trade01
            '“What can you tell me about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_iuno and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_iuno_about_recruitahunter01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump galerocksafterinteraction01

label galerocksnavicaALL: # {color=#f6d6bd}Navica{/color}, the boat maker
# (quarters < world_daylength and galerocks_navica_firsttime and not galerocks_navica_about_herself and not galerocks_navica_boat_about) or (quarters < world_daylength and galerocks_navica_firsttime and item_asteriontablet_read and not galerocks_navica_about_asterion) or (quarters < world_daylength and galerocks_navica_firsttime and galerocks_rumor_asterion and not galerocks_navica_about_asterion) or (quarters < world_daylength and galerocks_navica_firsttime and world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail) or (quarters < world_daylength and galerocks_navica_firsttime and galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland) or (quarters < world_daylength and galerocks_navica_firsttime and highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (quarters < world_daylength and galerocks_navica_firsttime and highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (quarters < world_daylength and galerocks_navica_firsttime and not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought) or (quarters < world_daylength and galerocks_navica_firsttime and not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment) or (quarters < world_daylength and galerocks_navica_firsttime and quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04) or (quarters < world_daylength and galerocks_navica_firsttime and quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day) or (quarters < world_daylength and galerocks_navica_firsttime and quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day) or (quarters < world_daylength and galerocks_navica_firsttime and quest_cursedcoins == 1 and quest_cursedcoins_description03) or (quarters < world_daylength and galerocks_navica_firsttime and quest_cursedcoins == 1 and quest_cursedcoins_description04)
    label galerocksnavica01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_navica_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        show galerocksoverlay navica at basicfade
        menu:
            '“{color=#f6d6bd}Navica{/color} is the best boatmaker in the North,” says a young boy with a proud posture. “Come, I’ll take you to her.” The carpenters have their space at the edge of the village, separated from the saltery with a stone wall that catches the shavings before they reach the fish, and which are then swept into a pile and moved to the smokehouse.
            \n\nThe tiny woman keeps her distance from the other workers, partially because of the many bits and pieces she needs constantly at hand, as well as logs, steamed planks, and a boat keel only a few steps away from her. She must be at least forty, older than any other woodworker in sight. Her light brown hair is in a ponytail, letting her work, and the simple tunic and pants, made of hemp in three shades of red, have short sleeves and legs. Her tanned skin is like dark honey.
            \n\nShe glances at you from afar and turns away, cutting some sort of log without pause, as if hoping you won’t notice her. The massive broad axe, made of fine steel, looks even larger as it’s resting on her back, and it’s engraved with the shape of a toothed eel twisted into a spiral. The kid leaves you alone, and you’re standing in silence.
            '
            '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                jump galerocks_navica_about_herself01
            '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                jump galerocks_navica_about_asterion01
            '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                jump galerocksnavicaabouthighisland00fail
            '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                jump galerocksnavicaabouthighisland01
            '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                jump galerocksnavicaaboutbuyingtheboat01
            '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                jump galerocksnavicaaboutbuyingtheboat01alt
            '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                jump galerocks_navica_about_highisland_recruitment01
            'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                pass
            'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                pass
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                jump galerocks_navica_about_highisland_recruitment02a
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                jump galerocks_navica_about_highisland_recruitment02b
            '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                jump galerocks_navica_about_highisland_recruitment02c
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksnavica01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay navica at basicfade
        $ custom1 = "She glances at you, then turns her head away and pays attention to the log she’s carving."
        jump galerocksnavicaafterinteraction01

    label galerocksnavicaafterinteraction01:
        menu:
            '[custom1]
            '
            '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                jump galerocks_navica_about_herself01
            '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                jump galerocks_navica_about_asterion01
            '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                jump galerocksnavicaabouthighisland00fail
            '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                jump galerocksnavicaabouthighisland01
            '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                jump galerocksnavicaaboutbuyingtheboat01
            '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                jump galerocksnavicaaboutbuyingtheboat01alt
            '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                jump galerocks_navica_about_highisland_recruitment01
            'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                pass
            'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                pass
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                jump galerocks_navica_about_highisland_recruitment02a
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                jump galerocks_navica_about_highisland_recruitment02b
            '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                jump galerocks_navica_about_highisland_recruitment02c
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocks_navica_about_herself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard you make boats.”')
        $ galerocks_navica_about_herself = 1
        $ custom1 = "“Yep. I make boats,” she doesn’t raise her eyes."
        jump galerocksnavicaafterinteraction01

    label galerocks_navica_about_asterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”')
        $ galerocks_navica_about_asterion = 1
        $ asterion_highisland_clues += 1
        if not galerocks_navica_about_herself_highisland:
            menu:
                'You tell her what you’ve learned, and her hands slow, then finally stop. “You’ve some wrong ideas. I don’t know where he is now, or if he’s alive or dead. Just that he needed a small boat, I sold it to him, he took it to the beach, and that’s all I’ve seen of him.”
                '
                '“Are you saying that you don’t know where he set off?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you saying that you don’t know where he set off?”')
                    menu:
                        '“I...” She pauses and scowls at you. “Yep. That’s what I’m saying.”
                        '
                        '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                            jump galerocks_navica_about_herself01
                        '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                            jump galerocks_navica_about_asterion01
                        '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                            jump galerocksnavicaabouthighisland00fail
                        '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                            jump galerocksnavicaabouthighisland01
                        '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                            jump galerocksnavicaaboutbuyingtheboat01
                        '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                            jump galerocksnavicaaboutbuyingtheboat01alt
                        '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                            jump galerocks_navica_about_highisland_recruitment01
                        'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                            pass
                        'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                            pass
                        '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                            jump galerocks_navica_about_highisland_recruitment02a
                        '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                            jump galerocks_navica_about_highisland_recruitment02b
                        '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                            jump galerocks_navica_about_highisland_recruitment02c
                        'I walk away.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                            jump galerocksafterinteraction01
        else:
            menu:
                'You tell her what you’ve learned, and her hands slow, then finally stop. “You’ve some wrong ideas. I don’t know where he is now, or if he’s alive or dead. Just that he needed a small boat to get to {color=#f6d6bd}High Island{/color}, I sold it to him, he took it to the beach, and that’s all I’ve seen of him.”
                '
                '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                    jump galerocks_navica_about_herself01
                '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                    jump galerocks_navica_about_asterion01
                '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                    jump galerocksnavicaabouthighisland00fail
                '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                    jump galerocksnavicaabouthighisland01
                '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                    jump galerocksnavicaaboutbuyingtheboat01
                '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                    jump galerocksnavicaaboutbuyingtheboat01alt
                '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                    jump galerocks_navica_about_highisland_recruitment01
                'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                    pass
                'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                    pass
                '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                    jump galerocks_navica_about_highisland_recruitment02a
                '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                    jump galerocks_navica_about_highisland_recruitment02b
                '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                    jump galerocks_navica_about_highisland_recruitment02c
                'I walk away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                    jump galerocksafterinteraction01

    label galerocksnavicaabouthighisland00fail:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}High Island{/color}?”')
        $ galerocks_navica_about_herself_highisland_fail = 1
        $ custom1 = "She speaks slowly, stepping between words as if they’re poison ivy. “Not much. It’s a deadly place, and we are {i}forbidden{/i} to travel there, we are. All them old deals between the tribes and villages, who could understand them? It ain’t like the fish there are worth the effort.”"
        jump galerocksnavicaafterinteraction01

    label galerocksnavicaabouthighisland01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve been to {color=#f6d6bd}High Island{/color}.”')
        $ at_activate = 1
        $ at = 0
        menu:
            'She looks at you with a mixture of shock and hatred. “And what do you want to do about it? Make others turn against me, {i}roadwarden{/i}? My village will stand by my side.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            '“Don’t worry, I’m not trying to use this against you. I just seek information, you don’t have to tell me anything.”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Don’t worry, I’m not trying to use this against you. I just seek information, you don’t have to tell me anything.”')
                $ galerocks_navica_friendship += 5
                $ at_activate = 0
                $ at = 0
                $ galerocks_navica_about_herself_highisland = 1
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland08 = "According to {color=#f6d6bd}Navica{/color}, I need to reach the cave behind the “closer” waterfall."
                $ description_highisland09 = "I’ve heard about a group of cityfolk who landed on it during wartime, and never returned."
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                menu:
                    'She looks at you in silence. “Are you serious?” Seeing your nod, she sighs with relief. “Yep, a few cityfolk paid me to take them there, just as the war started. It was more than half my age ago, right? I thought coins would save us from barbarians, stupid. I landed at the edge of the island, waited for them until dawn. They were meant to look for something at the bottom of the... Volcano, I guess? They didn’t come back, so I came back, all alone.”
                    \n\n“Dawn?” You repeat, and she gulps loudly, then clicks her tongue. “Yep, yep. You can’t get to {color=#f6d6bd}High Island{/color} in sunlight, the tides are too low to reach the cave. You know about the cave? Behind the closer waterfall?” She doesn’t wait for your answer, growling as she tries to recollect her memories. “I ain’t seen what’s inside. Did my best to stay quiet.”
                    '
                    '“So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”')
                        $ custom1 = "“Yep. Or you could just, {i}not{/i} do all that, and stay on the land,” she spares you a weak smile."
                        jump galerocksnavicaafterinteraction01
            '“Relax! I plan to see it myself. Want me to look for a nice seashell?”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Relax! I plan to see it myself. Want me to look for a nice seashell?”')
                $ galerocks_navica_friendship -= 3
                $ at_activate = 0
                $ at = 0
                $ galerocks_navica_about_herself_highisland = 1
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland08 = "According to {color=#f6d6bd}Navica{/color}, I need to reach the cave behind the “closer” waterfall."
                $ description_highisland09 = "I’ve heard about a group of cityfolk who landed on it during wartime, and never returned."
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                menu:
                    'She reaches for the axe on her back, but as you step away, she looks toward the other carpenters and lowers her hand. “You dare to scratch my old wounds, then make light of them? Shame on you, you harpy.” You try to respond, but she scoffs at you with a loud exhale. “Yep, a few cityfolk paid me to take them there, just as the war started. It was more than half my age ago, right? I thought coins would save us from barbarians, stupid. I landed at the edge of the island, waited for them until dawn. They were meant to look for something at the bottom of the... Volcano, I guess? They didn’t come back, so I came back, all alone.”
                    \n\n“Dawn?” You repeat, and she gulps loudly, then clicks her tongue. “Yep, yep. You can’t get to {color=#f6d6bd}High Island{/color} in sunlight, the tides are too low to reach the cave. You know about the cave? Behind the closer waterfall?” She doesn’t wait for your answer, growling as she tries to recollect her memories. “I ain’t seen what’s inside. Did my best to stay quiet.”
                    '
                    '“So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”')
                        $ custom1 = "“Sucks to be you,” she reaches for an adze and grabs it with great strength."
                        jump galerocksnavicaafterinteraction01
            '“I’m not one to spread rumors - tell me what you know about it and I’ll keep quiet.”' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I’m not one to spread rumors - tell me what you know about it and I’ll keep quiet.”')
                $ galerocks_navica_friendship -= 1
                $ at_activate = 0
                $ at = 0
                $ galerocks_navica_about_herself_highisland = 1
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland08 = "According to {color=#f6d6bd}Navica{/color}, I need to reach the cave behind the “closer” waterfall."
                $ description_highisland09 = "I’ve heard about a group of cityfolk who landed on it during wartime, and never returned."
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                menu:
                    'She scowls at you. “And it’s meant to make me trust you? You’re kidding right? You think you could hurt me?” You’re thinking of an answer when she carries on. “Yep, a few cityfolk paid me to take them there, just as the war started. It was more than half my age ago, right? I thought coins would save us from barbarians, stupid. I landed at the edge of the island, waited for them until dawn. They were meant to look for something at the bottom of the... Volcano, I guess? They didn’t come back, so I came back, all alone.”
                    \n\n“Dawn?” You repeat, and she gulps loudly, then clicks her tongue. “Yep, yep. You can’t get to {color=#f6d6bd}High Island{/color} in sunlight, the tides are too low to reach the cave. You know about the cave? Behind the closer waterfall?” She doesn’t wait for your answer, growling as she tries to recollect her memories. “I ain’t seen what’s inside. Did my best to stay quiet.”
                    '
                    '“So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”')
                        $ custom1 = "“Sucks to be you,” she reaches for an adze and grabs it with great strength."
                        jump galerocksnavicaafterinteraction01
            '“Tell me all you know, or I’ll make sure your misdeed won’t be forgotten. Is that clear enough?”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Tell me all you know, or I’ll make sure your misdeed won’t be forgotten. Is that clear enough?”')
                $ galerocks_navica_friendship -= 5
                $ at_activate = 0
                $ at = 0
                $ galerocks_navica_about_herself_highisland = 1
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland08 = "According to {color=#f6d6bd}Navica{/color}, I need to reach the cave behind the “closer” waterfall."
                $ description_highisland09 = "I’ve heard about a group of cityfolk who landed on it during wartime, and never returned."
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                menu:
                    'She reaches for the axe on her back, but as you step away, she looks toward the other carpenters and lowers her hand. “You’re kidding right? You think you could hurt me?” You try to respond, but she scoffs at you with a loud exhale. “Yep, a few cityfolk paid me to take them there, just as the war started. It was more than half my age ago, right? I thought coins would save us from barbarians, stupid. I landed at the edge of the island, waited for them until dawn. They were meant to look for something at the bottom of the... Volcano, I guess? They didn’t come back, so I came back, all alone.”
                    \n\n“Dawn?” You repeat, and she gulps loudly, then clicks her tongue. “Yep, yep. You can’t get to {color=#f6d6bd}High Island{/color} in sunlight, the tides are too low to reach the cave. You know about the cave? Behind the closer waterfall?” She doesn’t wait for your answer, growling as she tries to recollect her memories. “I ain’t seen what’s inside. Did my best to stay quiet.”
                    '
                    '“So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”')
                        $ custom1 = "“Sucks to be you,” she reaches for an adze and grabs it with great strength."
                        jump galerocksnavicaafterinteraction01
            '“Please, {color=#f6d6bd}Navica{/color}. I need your help. I have to know what may await me there.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Please, {color=#f6d6bd}Navica{/color}. I need your help. I have to know what may await me there.”')
                $ galerocks_navica_friendship += 3
                $ at_activate = 0
                $ at = 0
                $ galerocks_navica_about_herself_highisland = 1
                $ highisland_howtoreach_pcknows = 1
                $ description_highisland08 = "According to {color=#f6d6bd}Navica{/color}, I need to reach the cave behind the “closer” waterfall."
                $ description_highisland09 = "I’ve heard about a group of cityfolk who landed on it during wartime, and never returned."
                $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
                $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
                $ description_highisland02 = "I’ve heard rumors of “treasures and huge monsters” that can be found there."
                $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
                menu:
                    'She looks at you in silence. “How come everyone needs {i}my{/i} help, and I’m just sitting here, making boats, not bothering anyone?” Seeing your sad smile, she lets out a heavy sigh. “Yep, a few cityfolk paid me to take them there, just as the war started. It was more than half my age ago, right? I thought coins would save us from barbarians, stupid. I landed at the edge of the island, waited for them until dawn. They were meant to look for something at the bottom of the... Volcano, I guess? They didn’t come back, so I came back, all alone.”
                    \n\n“Dawn?” You repeat, and she gulps loudly, then clicks her tongue. “Yep, yep. You can’t get to {color=#f6d6bd}High Island{/color} in sunlight, the tides are too low to reach the cave. You know about the cave? Behind the closer waterfall?” She doesn’t wait for your answer, growling as she tries to recollect her memories. “I ain’t seen what’s inside. Did my best to stay quiet.”
                    '
                    '“So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So I need a boat to get there... {i}And{/i} I need to do so during nighttime.”')
                        $ custom1 = "“Yep. Or you could just, {i}not{/i} do all that, and stay on the land,” she reaches for an adze and grabs it with great strength."
                        jump galerocksnavicaafterinteraction01

    label galerocksnavicaaboutbuyingtheboat01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”')
        $ galerocks_navica_boat_about = 1
        if galerocks_navica_about_herself_highisland:
            $ custom1 = "She sighs. “This again? "
        else:
            $ custom1 = "She freezes. “To {color=#f6d6bd}High Island{/color}? Are you serious?” After you confirm your words, she shakes her head slightly. “"
        menu:
            '[custom1]Looking for ways to die? I ain’t {i}making{/i} you a boat,” her tone mocks the very thought. “It would take us {i}seasons{/i} of work, it would, if not a year or more. Tell you what, I fixed one old piece of driftwood some time back. It stays afloat, merely takes a lot of muscle to push forward, for it has only the paddles. It’s now wasting itself under the rains.”
            '
            '“So what’s your price?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So what’s your price?”')
                $ galerocks_navica_boat_price = (galerocks_navica_boat_price_base-(galerocks_reputation/3)+(appearance_price*2)-galerocks_navica_friendship)
                if galerocks_navica_boat_price < 5:
                    $ galerocks_navica_boat_price = 5
                menu:
                    'She runs her eyes over you. “Well, I could speak with a few neighbors of mine, but judging by what I know about you,” she crosses her arms. “[galerocks_navica_boat_price] coins will be fair.”
                    '
                    '“...How about I rent it?”' if galerocks_navica_boat_price >= 20:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...How about I rent it?”')
                        menu:
                            '“How about you stop wasting the air? I wouldn’t lend you a boat for fishing, and even less so for traveling to a forbidden island. The rocks at the coast are like teeth.”
                            '
                            '“I don’t think I have much of a choice...” I grab my pouch.' if coins >= galerocks_navica_boat_price:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think I have much of a choice...” I grab my pouch.')
                                jump galerocksnavicaaboutbuyingtheboat02
                            'I can’t afford it. (disabled)' if coins < galerocks_navica_boat_price:
                                pass
                            '“I need to think about it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                                $ custom1 = "“Think as much as you have to, I’d rather have a boat than your coins anyway.”"
                                jump galerocksnavicaafterinteraction01
                    '“I don’t think I have much of a choice...” I grab my pouch.' if coins >= galerocks_navica_boat_price and galerocks_navica_boat_price >= 20:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think I have much of a choice...” I grab my pouch.')
                        jump galerocksnavicaaboutbuyingtheboat02
                    '“So be it.”' if coins >= galerocks_navica_boat_price and galerocks_navica_boat_price < 20:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                        jump galerocksnavicaaboutbuyingtheboat02alt
                    'I can’t afford it. (disabled)' if coins < galerocks_navica_boat_price:
                        pass
                    '“I need to think about it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                        $ custom1 = "“Think as much as you have to, I’d rather have a boat than your coins anyway.”"
                        jump galerocksnavicaafterinteraction01

    label galerocksnavicaaboutbuyingtheboat01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still interested in that boat.”')
        $ galerocks_navica_boat_price = (galerocks_navica_boat_price_base-(galerocks_reputation/3)+(appearance_price*2)-galerocks_navica_friendship)
        if galerocks_navica_boat_price < 5:
            $ galerocks_navica_boat_price = 5
        menu:
            '“Seriously? Fine, let’s say [galerocks_navica_boat_price].”
            '
            'I sigh and grab my pouch.' if coins >= galerocks_navica_boat_price and galerocks_navica_boat_price >= 20:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh and grab my pouch.')
                jump galerocksnavicaaboutbuyingtheboat02
            '“So be it.”' if coins >= galerocks_navica_boat_price and galerocks_navica_boat_price < 20:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump galerocksnavicaaboutbuyingtheboat02alt
            'I can’t afford it. (disabled)' if coins < galerocks_navica_boat_price:
                pass
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                $ custom1 = "“Think, think. I’m sure it’s time well-spent,” she scoffs."
                jump galerocksnavicaafterinteraction01

    label galerocksnavicaaboutbuyingtheboat02:
        $ coins -= galerocks_navica_boat_price
        $ galerocks_navica_boat_bought = day
        show screen notifyimage( "The boat will wait for you at the beach.\n-%s" %galerocks_navica_boat_price, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The boat will wait for you at the beach. -%s {image=cointest}{/i}' %galerocks_navica_boat_price)
        $ galerocks_reputation += 1
        $ minutes += 10
        menu:
            'Her eyes widen. “You ain’t joking?” She puts away her tools and reaches out to you with her open palms, listening as you count down the dragon bones. “Well I’ll be trampled. {color=#f6d6bd}Domitia{/color}!” She calls the cooper who’s been working nearby, who gasps after seeing the pile of coins. “What’s that for?”
            \n\n{color=#f6d6bd}Navica{/color} explains the situation, without avoiding an opportunity to call you an idiot. Still, the looks you receive from the locals get much warmer. “Someone take it to the keep,” {color=#f6d6bd}the cooper{/color} orders. “We can now buy ourselves enough nails for a few new boats!”
            \n\nThe commotion and questions go on for the next few minutes, until the locals leave you and {color=#f6d6bd}the boatmaker{/color} to yourselves, though she doesn’t seem any more eager to chat with you. “So, what do you want now? Your boat is on the beach, you’ll recognize it. I made it from three others.”
            '
            '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                jump galerocks_navica_about_herself01
            '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                jump galerocks_navica_about_asterion01
            '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                jump galerocksnavicaabouthighisland00fail
            '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                jump galerocksnavicaabouthighisland01
            '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                jump galerocksnavicaaboutbuyingtheboat01
            '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                jump galerocksnavicaaboutbuyingtheboat01alt
            '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                jump galerocks_navica_about_highisland_recruitment01
            'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                pass
            'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                pass
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                jump galerocks_navica_about_highisland_recruitment02a
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                jump galerocks_navica_about_highisland_recruitment02b
            '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                jump galerocks_navica_about_highisland_recruitment02c
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksnavicaaboutbuyingtheboat02alt:
        $ coins -= galerocks_navica_boat_price
        $ galerocks_navica_boat_bought = day
        show screen notifyimage( "The boat will wait for you at the beach.\n-%s" %galerocks_navica_boat_price, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The boat will wait for you at the beach. -%s {image=cointest}{/i}' %galerocks_navica_boat_price)
        $ galerocks_reputation += 1
        $ minutes += 1
        menu:
            'She nods. “Quite a discount you earned around here. So, what do you want now? Your boat is on the beach, you’ll recognize it. I made it from three others.”
            '
            '“I’ve heard you make boats.”' if not galerocks_navica_about_herself and not galerocks_navica_boat_about:
                jump galerocks_navica_about_herself01
            '“I have a reason to believe you know what happened to {color=#f6d6bd}Asterion{/color}.”' if (item_asteriontablet_read and not galerocks_navica_about_asterion) or (galerocks_rumor_asterion and not galerocks_navica_about_asterion):
                jump galerocks_navica_about_asterion01
            '“What can you tell me about {color=#f6d6bd}High Island{/color}?”' if world_popupnarration_highisland1 and not galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland and not galerocks_navica_about_herself_highisland_fail:
                jump galerocksnavicaabouthighisland00fail
            '“You’ve been to {color=#f6d6bd}High Island{/color}.”' if galerocks_navica_pcknowsabout_highisland and not galerocks_navica_about_herself_highisland:
                jump galerocksnavicaabouthighisland01
            '“I need you to make me a boat that will reach {color=#f6d6bd}High Island{/color}.”' if (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about) or (highisland_howtoreach_pcknows and not asterion_found and quest_asterion == 1 and not galerocks_navica_boat_about):
                jump galerocksnavicaaboutbuyingtheboat01
            '“I’m still interested in that boat.”' if not asterion_found and quest_asterion == 1 and galerocks_navica_boat_about and not galerocks_navica_boat_bought:
                jump galerocksnavicaaboutbuyingtheboat01alt
            '“I could use the help of an experienced sailor.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and galerocks_navica_boat_bought and galerocks_navica_about_herself_highisland and not galerocks_navica_about_highisland_recruitment_blocked and not galerocks_navica_about_highisland_recruitment:
                jump galerocks_navica_about_highisland_recruitment01
            'I still need to lift the curse from her dragon bones. (disabled)' if quest_cursedcoins == 1 and not quest_cursedcoins_description01 and not quest_cursedcoins_description02 and not quest_cursedcoins_description03 and not quest_cursedcoins_description04:
                pass
            'I should wait until tomorrow to make my lie sound convincing. (disabled)' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived == day:
                pass
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description01 and quest_cursedcoins_dayofreceived < day:
                jump galerocks_navica_about_highisland_recruitment02a
            '(lie) “The coins are gone.”' if quest_cursedcoins == 1 and quest_cursedcoins_description03:
                jump galerocks_navica_about_highisland_recruitment02b
            '“The curse is no more.”' if quest_cursedcoins == 1 and quest_cursedcoins_description04:
                jump galerocks_navica_about_highisland_recruitment02c
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocks_navica_about_highisland_recruitmentALL:
        label galerocks_navica_about_highisland_recruitment01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use the help of an experienced sailor.”')
            $ galerocks_navica_about_highisland_recruitment = 1
            if galerocks_navica_friendship <= 0:
                $ galerocks_navica_about_highisland_recruitment_blocked = 1
                $ custom1 = "“You must be kidding,” seeing your look, she gestures for you to get out of here. “I wouldn’t trust your harpy ass even if I were a young lass.”"
                jump galerocksnavicaafterinteraction01
            else:
                menu:
                    'She exhales and takes a few steps away. “I bet. But first, do something for me.”
                    '
                    '“Go on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Go on.”')
                        $ minutes += 5
                        menu:
                            'She leaves you alone for a few minutes and returns with a small, wooden casket. She raises the lid, revealing a fistful of dragon bones.
                            \n\n“Remember the cityfolk I told you about? That time I took them to the island, this was the first share of my pay. Never got the second one,” a long pause, “but I spent not a single coin. They’re cursed,” she looks you in the eyes, “must be because of greed, both theirs and mine. Ever since I had got them, bad things started to happen. Even after I tried to lock them in our chapel, or threw them away,” she looks around and closes the box again.
                            '
                            '“What do you want me to do about it?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want me to do about it?”')
                                $ custom1 = "“"
                                jump galerocks_navica_about_highisland_recruitment01a
                            '“How can I be sure {i}I{/i} won’t get cursed?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can I be sure {i}I{/i} won’t get cursed?”')
                                $ custom1 = "Her nervous glance betrays that she never considered such a possibility. Her fingers get white from being clenched around the casket. “Just listen. "
                                jump galerocks_navica_about_highisland_recruitment01a
                            '“Oh, I’d {i}love{/i} to free you from a haunted treasure.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, I’d {i}love{/i} to free you from a haunted treasure.”')
                                $ galerocks_navica_friendship -= 1
                                $ custom1 = "“Shut up,” she doesn’t even let you finish. “"
                                label galerocks_navica_about_highisland_recruitment01a:
                                    $ beholder_name_known = 1
                                    menu:
                                        '[custom1]The pagans of {color=#f6d6bd}Howler’s Dell{/color} worship {color=#f6d6bd}Beholder{/color}, a cursed tree growing south of their fields. It {i}eats{/i} pneuma, good or bad. Put the coins on its altar. It will destroy them, for sure, but it’s better than having them on The Land.”
                                        '
                                        '“Very well. I’ll take it to that altar.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll take it to that altar.”')
                                            $ renpy.notify("New entry: The Cursed Coins.\nYou received the casket with coins.")
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Cursed Coins.\nYou received the casket with coins.{/i}')
                                            $ quest_cursedcoins = 1
                                            $ item_casket = 1
                                            $ quest_cursedcoins_dayofreceived = day
                                            $ custom1 = "“Lovely,” she says while pressing the casket against your stomach, then approaches the beams she was previously working on."
                                            jump galerocksnavicaafterinteraction01
                                        '“I’m not playing with dark magic. Ask an herbalist for help, or a priest.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not playing with dark magic. Ask an herbalist for help, or a priest.”')
                                            $ galerocks_navica_about_highisland_recruitment_blocked = 1
                                            $ galerocks_navica_friendship -= 1
                                            $ custom1 = "She puts the casket on a nearby stool, then turns it around, as if to keep its front from “looking” at her. “Then you’ve nothing to give me.”"
                                            jump galerocksnavicaafterinteraction01

        label galerocks_navica_about_highisland_recruitment02a:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “The coins are gone.”')
            $ pc_lies += 2
            jump galerocks_navica_about_highisland_recruitment03

        label galerocks_navica_about_highisland_recruitment02b:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “The coins are gone.”')
            $ pc_lies += 1
            jump galerocks_navica_about_highisland_recruitment03

        label galerocks_navica_about_highisland_recruitment02c:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The curse is no more.”')
            label galerocks_navica_about_highisland_recruitment03:
                $ quest_cursedcoins = 2
                $ quest_cursedcoins_description05 = 1
                $ renpy.notify("Quest completed: The Cursed Coins")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Cursed Coins{/i}')
                $ galerocks_navica_about_highisland_recruitment_done = 1
                $ pc_goal_iwanttohelppoints += 1
                $ galerocks_navica_friendship += 2
                menu:
                    'She takes a deep breath, tapping on the table. “I felt that, I did. The weight off my shoulders. So you now want me to die in the sea?” She glances at your boots. “Fine, fine. I’ll keep my end.”
                    '
                    '“To be honest, I doubt I’m going to need your assistance anytime soon.”' if asterion_found:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “To be honest, I doubt I’m going to need your assistance anytime soon.”')
                        $ galerocks_reputation += 1
                        $ custom1 = "She shrugs. “Then I’ll tell the others how {i}selfless{/i} you are. Now scat.” She spits in her hands, rubs them together, and reaches for an axe."
                        jump galerocksnavicaafterinteraction01
                    '“I’ll tell you when we’re ready to leave.”' if not asterion_found:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when we’re ready to leave.”')
                        $ custom1 = "“Right, but you can take your time, you know.” She spits in her hands, rubs them together, and reaches for an axe."
                        jump galerocksnavicaafterinteraction01

label galerocks_petronius_ALL: # {color=#f6d6bd}Petronius{/color}, the gossip
    label galerocks_petronius_01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_petronius_firsttime = 1
        hide galerocksoverlay
        if quarters > world_daylength-10 or quarters < 34:
            show galerocksboat behind galerocksoverlay at basicfade
        else:
            hide galerocksboat
        if galerocks_npcsmet >= 3:
            $ custom1 = "You realize there’s been someone following you around, or at least {i}accidentally{/i} showing up wherever you go. “Ehm, bored with walking around?” He spares you a smirk."
        else:
            $ quarters += 1
            $ custom1 = "You try to exchange gossip with a few of the locals, but to no avail. Finally, someone taps you on the back, and as you turn around, he smirks at you. “Want to talk? I can talk.”"
        $ galerocks_npcsmet += 1
        menu:
            '[custom1]
            \n\nHe’s a short man, dressed in a worn, gray-black woolen robe, with a belt as wide as your hand, and a buckle decorated with a large shell, now placed annoyingly just two inches away from the center of his stomach. He may be only thirty, but it’s clear why he has no tasks to bother with - his fingers are paralyzed at unnatural angles, spread like an osier tree’s branches. While he’s capable of moving around both of his arms slightly, they are constantly bent both at the elbows, and at the wrists. He’s wearing no boots.
            '
            '“I’ve got a few questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got a few questions.”')
                show galerocksoverlay petronius at basicfade
                menu:
                    '“I know,” he nods for you to follow him and leads you to the orchard, where you stay in the shadow of a cherry tree.
                    \n\n“Right,” he looks around, scowling at the nearby kid, who instantly turns around and gets out of your sight. “Name’s {color=#f6d6bd}Petronius{/color}. I can be your guide,” his soft voice is close to a whisper. “One coin, one question,” he looks at the small leather sack hanging from his neck. “No backsies. You decide my answers ain’t worth it, you stop asking.”
                    '
                    '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                        jump galerocks_petronius_about_asterion01
                    '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                        jump galerocks_petronius_about_bandits01
                    '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                        jump galerocks_petronius_about_traders01
                    '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                        jump galerocks_petronius_about_artisans01
                    '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                        jump galerocks_petronius_about_gainingreputation01
                    '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                        jump galerocks_petronius_about_severina01
                    '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                        jump galerocks_petronius_about_fulviassecret01
                    '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                        jump galerocks_petronius_pastrobbery01
                    '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                        jump galerocks_petronius_about_lumberjackcamp01
                    '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                        jump galerocks_petronius_about_recruitahunter01
                    '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                        jump galerocks_petronius_about_himself01
                    '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                        jump galerocks_petronius_about_himself02
                    '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                        pass
                    '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                        pass
                    'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                        pass
                    '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                        pass
                    '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                        pass
                    '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                        pass
                    '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                        pass
                    '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                        pass
                    '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                        pass
                    '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                        pass
                    '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                        pass
                    '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                        pass
                    '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                        jump galerocksafterinteraction01
                    '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                        jump galerocksafterinteraction01

    label galerocks_petronius_01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if galerocks_petronius_questions_counter >= 3 and not galerocks_petronius_questions_tier2:
            hide galerocksoverlay
            if quarters > world_daylength-10 or quarters < 34:
                show galerocksboat behind galerocksoverlay at basicfade
            else:
                hide galerocksboat
            menu:
                'Something’s changed. He seems to be nowhere in sight, and once you find him, his usual confidence is gone. As he leads you away from the others, he stares at the ground, and some of his neighbors scowl at you.
                \n\n“There’s a {i}rumor{/i} that I’m spying for an outsider.” An awkward pause. “Better get back to your beast, or smelly name will drop on both of us, it will.”
                '
                '{image=cointest} “I don’t care, and I’m willing to pay you one dragon right away. Take it, or leave it.”' if coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I don’t care, and I’m willing to pay you one dragon right away. Take it, or leave it.”')
                    $ galerocks_petronius_questions_tier2 = 1
                    $ galerocks_reputation -= 1
                    $ coins -= 1
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                    show galerocksoverlay petronius at basicfade
                    menu:
                        'He looks at your hand, then sighs. “Fine. To the orchard we go.”
                        '
                        '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                            jump galerocks_petronius_about_asterion01
                        '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                            jump galerocks_petronius_about_bandits01
                        '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                            jump galerocks_petronius_about_traders01
                        '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                            jump galerocks_petronius_about_artisans01
                        '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                            jump galerocks_petronius_about_gainingreputation01
                        '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                            jump galerocks_petronius_about_severina01
                        '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                            jump galerocks_petronius_about_fulviassecret01
                        '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                            jump galerocks_petronius_pastrobbery01
                        '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                            jump galerocks_petronius_about_lumberjackcamp01
                        '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                            jump galerocks_petronius_about_recruitahunter01
                        '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                            jump galerocks_petronius_about_himself01
                        '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                            jump galerocks_petronius_about_himself02
                        '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                            pass
                        '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                            pass
                        'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                            pass
                        '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                            pass
                        '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                            pass
                        '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                            pass
                        '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                            pass
                        '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                            pass
                        '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                            pass
                        '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                            pass
                        '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                            pass
                        '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                            pass
                        '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                            jump galerocksafterinteraction01
                        '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                            jump galerocksafterinteraction01
                'My pouch is empty. (disabled)' if not coins:
                    pass
                '“So be it. Farewell.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it. Farewell.”')
                    jump galerocksafterinteraction01
        else:
            show galerocksoverlay petronius at basicfade
            menu:
                'You find him right away as he’s following you like a shadow. He answers your approach with a nod and leads you to the orchard.
                '
                '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                    jump galerocks_petronius_about_asterion01
                '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    jump galerocks_petronius_about_bandits01
                '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                    jump galerocks_petronius_about_traders01
                '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                    jump galerocks_petronius_about_artisans01
                '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                    jump galerocks_petronius_about_gainingreputation01
                '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                    jump galerocks_petronius_about_severina01
                '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                    jump galerocks_petronius_about_fulviassecret01
                '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                    jump galerocks_petronius_pastrobbery01
                '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                    jump galerocks_petronius_about_lumberjackcamp01
                '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                    jump galerocks_petronius_about_recruitahunter01
                '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                    jump galerocks_petronius_about_himself01
                '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                    jump galerocks_petronius_about_himself02
                '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                    pass
                '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    pass
                'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                    pass
                '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                    pass
                '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                    pass
                '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                    pass
                '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                    pass
                '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                    pass
                '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                    pass
                '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                    pass
                '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                    pass
                '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                    pass
                '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                    jump galerocksafterinteraction01
                '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                    jump galerocksafterinteraction01

    label galerocks_petronius_about_himself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you need coins?”')
        $ galerocks_petronius_about_himself = 1
        menu:
            'He lowers his arms a bit, as if trying to hide them. “Why?” He clears his throat and straightens up, though it doesn’t make him much taller. “Why don’t you pay first?”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_himself02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Why do you need coins?”')
        $ galerocks_petronius_about_himself = 2
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]“Ehm. {color=#f6d6bd}Gale Rocks{/color} is good to me, but I’ve got no family left. I get merely as much food as I need, and not the {i}good{/i} stuff, like the head workers or the guards. Just fish every day, with greens and gruel. I’d rather buy some dried herbs once the merchants come, and ask the cooks to add some to my meals.”
            \n\n“You’re gathering coins to buy dried herbs?” You try to spot a lie in his eyes.
            \n\n“You say it as if it’s any different than drunks paying for mugs of ale,” he growls. “The Wright took away my hands, so I’ll get my share of what’s good in this life any way I can, I bloody will.” He looks at one of the apples growing on the nearby tree. “A nice smell and togs wouldn’t hurt me, either.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_recruitahunter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”')
        $ quest_recruitahunter_spokento_petronius = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        $ quest_recruitahunter_cassia_points += 2
        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
            $ quest_recruitahunter_cassia_points_notify2 = 1
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        menu:
            '[custom1] “The opposite,” he straightens up. “Can’t stop lying, can’t stop arguing, and used to drink until she fell on the ground, until she was banned by {color=#f6d6bd}the headwoman{/color} once she fell into the stream, almost drowned.” He glances east. “Something’s wrong with her.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_asterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”')
        $ galerocks_rumor_asterion = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            'He steps away, fighting himself to decline your offer, but finally breaks. [custom1]“{color=#f6d6bd}Navica{/color}. She’s our boatmaker, and the last few times {color=#f6d6bd}Asterion{/color} was here, he always talked with her.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01



    label galerocks_petronius_about_bandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Do the locals struggle with the bandits?”')
        if galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
            $ galerocks_petronius_about_tiestobandits_gray = 1
            menu:
                'He crosses his forearms, blocking the pouch hanging on his neck. “Can’t talk about this. Made a promise, you know.”
                '
                '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                    jump galerocks_petronius_about_asterion01
                '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    jump galerocks_petronius_about_bandits01
                '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                    jump galerocks_petronius_about_traders01
                '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                    jump galerocks_petronius_about_artisans01
                '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                    jump galerocks_petronius_about_gainingreputation01
                '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                    jump galerocks_petronius_about_severina01
                '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                    jump galerocks_petronius_about_fulviassecret01
                '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                    jump galerocks_petronius_pastrobbery01
                '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                    jump galerocks_petronius_about_lumberjackcamp01
                '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                    jump galerocks_petronius_about_recruitahunter01
                '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                    jump galerocks_petronius_about_himself01
                '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                    jump galerocks_petronius_about_himself02
                '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                    pass
                '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    pass
                'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                    pass
                '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                    pass
                '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                    pass
                '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                    pass
                '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                    pass
                '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                    pass
                '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                    pass
                '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                    pass
                '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                    pass
                '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                    pass
                '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                    jump galerocksafterinteraction01
                '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                    jump galerocksafterinteraction01
        else:
            $ galerocks_petronius_about_tiestobandits = 1
            $ banditshideout_galerocks_tiestobandits = 1
            if not galerocks_about_bandits_thais:
                $ banditshideout_villagesasked_aboutattacks += 1
                $ galerocks_about_bandits_thais = 1
            $ quest_intelforpeltnorth_description04c = "The people of {color=#f6d6bd}Gale Rocks{/color} claim that bandits are not a big issue."
            $ description_glaucia02 = "I heard that she was raised by her family in the {color=#f6d6bd}Gale Rocks{/color} village."
            $ coins -= 1
            $ galerocks_petronius_questions_counter += 1
            show screen notifyimage( "-1", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
            menu:
                'He makes an annoyed grunt, but accepts your dragon bone. “{color=#f6d6bd}Glaucia{/color} is from around here. She brings here coins and loot, and gets food and arrows in return.” His eyes get harsh. “I know merely because I saw blood on one of the sacks, when they stored them in a shed beyond the walls. Most people here don’t know the truth.”
                '
                '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                    jump galerocks_petronius_about_asterion01
                '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    jump galerocks_petronius_about_bandits01
                '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                    jump galerocks_petronius_about_traders01
                '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                    jump galerocks_petronius_about_artisans01
                '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                    jump galerocks_petronius_about_gainingreputation01
                '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                    jump galerocks_petronius_about_severina01
                '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                    jump galerocks_petronius_about_fulviassecret01
                '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                    jump galerocks_petronius_pastrobbery01
                '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                    jump galerocks_petronius_about_lumberjackcamp01
                '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                    jump galerocks_petronius_about_recruitahunter01
                '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                    jump galerocks_petronius_about_himself01
                '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                    jump galerocks_petronius_about_himself02
                '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                    pass
                '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                    pass
                'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                    pass
                '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                    pass
                '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                    pass
                '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                    pass
                '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                    pass
                '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                    pass
                '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                    pass
                '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                    pass
                '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                    pass
                '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                    pass
                '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                    jump galerocksafterinteraction01
                '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                    jump galerocksafterinteraction01

    label galerocks_petronius_about_traders01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Who in the village can sell me some decent equipment?”')
        $ galerocks_petronius_about_traders = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]“You’ll get dinner from {color=#f6d6bd}the cook{/color}. {color=#f6d6bd}The tailor{/color} mostly fixes old rags, she does. Maybe our {color=#f6d6bd}bath man{/color} has something. But {color=#f6d6bd}the armorer{/color} won’t sell much to an outsider.”
            \n\nWhen you ask for their names, he answers slowly, trying to recover lost memories. “Ehm. That would be {color=#f6d6bd}Porcia{/color}, {color=#f6d6bd}Rufina{/color}, {color=#f6d6bd}Aquila{/color}, and... {color=#f6d6bd}Tatius{/color}?”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_artisans01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What kinds of artisans can I find in the village?”')
        $ galerocks_petronius_about_artisans = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]“Only ones that would matter to a caravan, not a traveller. We have the {color=#f6d6bd}coopers{/color}, {color=#f6d6bd}salters{/color}, and {color=#f6d6bd}smokers{/color}, who also salt fish. If you use a bow, go to {color=#f6d6bd}Florus, the fletcher{/color}.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_gainingreputation01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “How do I get on your neighbors’ good side?”')
        $ galerocks_petronius_about_gainingreputation = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]”With labor,” he says briefly, though you hear the pain in his voice. “They may call for coins, but what they truly want to see is a reliable soul, and a strong shell.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_severina01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Tell me about the people who lead this village.”')
        $ galerocks_petronius_about_severina = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        $ description_galerocks13 = "According to {color=#f6d6bd}Petronius{/color}, {color=#f6d6bd}Severina{/color} has a short patience. “When I speak with her, I’d rather say less, but quickly. And it’s better to tell her only one, two things at once, bring her other news after she gets a good sleep.”"
        menu:
            '[custom1]“Before becoming our {color=#f6d6bd}headwoman{/color}, {color=#f6d6bd}Severina{/color} was the head trader of our village. When she’s in doubt, she consults with those of our neighbors who hold great responsibilities, artisans and elders. They gather at the keep and vote. Right, but people trust her enough to let her handle most decisions.”
            \n\nYou ask him if you understand correctly that by having enough support from the villagers you could outvote {color=#f6d6bd}Severina’s{/color} decision, and he gives you a curious look. “Trust may get you far, I suppose.”
            \n\nAfter you ask for any additional tips on dealing with her, he lowers his head, scratching his cheek with the back of his hand. “When I speak with her, I’d rather say less, but quickly. And it’s better to tell her only one, two things at once, before her patience runs out. Bring her other news after she gets a good sleep.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_fulviassecret01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”')
        $ galerocks_fulvia_secret_knowsabout = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]“You are. She spent most of her young days, and even some of the nights, on the roads, chiefly on the path leading through the heart of the woods. She never got wounded... Yet with years, her eyes gave up. The Wright laughs when we feel safe.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_pastrobbery01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”')
        $ galerocks_petronius_about_pastrobbery = 1
        $ galerocks_pastrobbery = 1
        $ coins -= 1
        if galerocks_petronius_questions_counter <= 0:
            $ custom1 = "You offer him one dragon, but he doesn’t even try to grab it with his stiff fingers. Instead, he pushes his chest forward, inviting you to untie the pouch on his neck and drop the coin inside. The dull sound suggests it’s not the first bone that’s landed there. "
        if galerocks_petronius_questions_counter == 1:
            $ custom1 = "You push a dragon bone into the sack on his neck. "
        else:
            $ custom1 = ""
        $ galerocks_petronius_questions_counter += 1
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            '[custom1]He suddenly squeezes his sides with his elbows, and moves his hands to the front of his stomach. “I had {i}nothing{/i} to do with any of it!” You tell him to calm down, and he explains quickly that thefts happened many times in the past, both in the village and on the roads, and every kid knows to watch out for outsiders. Some of the tales he was told as a {i}young lad{/i} used words that felt as old as the ones he heard spoken by the priest when he read from Wright’s Tablets.
            \n\n“But there was a man here, ehm, in the beginning of summer. A scavenger, said his name was {color=#f6d6bd}Pyrrhos{/color}, such a timid guy. He was here for a bit, and suddenly disappeared, keeping his sleeping spot packed with our own rags. And, right, a part of our supplies was also missing, iron included. We didn’t chase after him, he could have gone anywhere, and likely left the peninsula.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

    label galerocks_petronius_about_lumberjackcamp01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I was told something about an old lumberjack hamlet...”')
        $ galerocks_petronius_about_lumberjackcamp += 1
        $ galerocks_petronius_questions_counter += 1
        menu:
            'He tells you to put away the dragon. “Ehm, I can’t help you with this one. I know there used to be such a place, but I never left my home. Better ask a lumberjack, or someone who knows the peninsula well, if there are such people left.”
            '
            '{image=cointest} “Who here may know something about {color=#f6d6bd}Asterion{/color}?”' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins >= 1:
                jump galerocks_petronius_about_asterion01
            '{image=cointest} “Do the locals struggle with the bandits?”' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                jump galerocks_petronius_about_bandits01
            '{image=cointest} “Who in the village can sell me some decent equipment?”' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins >= 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins >= 1):
                jump galerocks_petronius_about_traders01
            '{image=cointest} “What kinds of artisans can I find in the village?”' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins >= 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins >= 1):
                jump galerocks_petronius_about_artisans01
            '{image=cointest} “How do I get on your neighbors’ good side?”' if not galerocks_petronius_about_gainingreputation and coins >= 1:
                jump galerocks_petronius_about_gainingreputation01
            '{image=cointest} “Tell me about the people who lead this village.”' if not severina_firsttime and not galerocks_petronius_about_severina and coins >= 1:
                jump galerocks_petronius_about_severina01
            '{image=cointest} “{color=#f6d6bd}Fulvia{/color} isn’t just any elder, am I right?”' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins >= 1:
                jump galerocks_petronius_about_fulviassecret01
            '{image=cointest} “I’ve heard something about your neighbors getting robbed by strangers?”' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins >= 1:
                jump galerocks_petronius_pastrobbery01
            '{image=cointest} “I was told something about an old lumberjack hamlet...”' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and not galerocks_petronius_about_lumberjackcamp and coins >= 1):
                jump galerocks_petronius_about_lumberjackcamp01
            '{image=cointest} “Is {color=#f6d6bd}Cassia{/color} trustworthy?”' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins >= 1:
                jump galerocks_petronius_about_recruitahunter01
            '“Why do you need coins?”' if not galerocks_petronius_about_himself:
                jump galerocks_petronius_about_himself01
            '{image=cointest} “Why do you need coins?”' if galerocks_petronius_about_himself == 1 and coins >= 1:
                jump galerocks_petronius_about_himself02
            '{image=coingray} “Who here may know something about Asterion?” (disabled)' if not galerocks_rumor_asterion and not world_popupnarration_highisland1 and coins < 1:
                pass
            '{image=coingray} “Do the locals struggle with the bandits?” (disabled)' if (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and not galerocks_petronius_about_tiestobandits_gray) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter >= 4) or (banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins < 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_tier2):
                pass
            'He avoids talking about the bandits. (disabled)' if banditshideout_bandits_pchearedabout and not banditshideout_galerocks_tiestobandits and not galerocks_petronius_about_tiestobandits and coins >= 1 and galerocks_petronius_about_tiestobandits_gray and galerocks_petronius_questions_counter < 4 and not galerocks_petronius_questions_tier2:
                pass
            '{image=coingray} “Who in the village can sell me some decent equipment?” (disabled)' if (not galerocks_porcia_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_rufina_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_tatius_firsttime and not galerocks_petronius_about_traders and coins < 1) or (not galerocks_aquila_firsttime and not galerocks_petronius_about_traders and coins < 1):
                pass
            '{image=coingray} “What kinds of artisans can I find in the village?” (disabled)' if (not galerocks_domitia_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_albus_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_saltery_firsttime and not galerocks_petronius_about_artisans and coins < 1) or (not galerocks_florus_firsttime and not galerocks_petronius_about_artisans and coins < 1):
                pass
            '{image=coingray} “How do I get on your neighbors’ good side?” (disabled)' if not galerocks_petronius_about_gainingreputation and coins < 1:
                pass
            '{image=coingray} “Tell me about the people who lead this village.” (disabled)' if not severina_firsttime and not galerocks_petronius_about_severina and coins < 1:
                pass
            '{image=coingray} “Fulvia isn’t just any elder, am I right?” (disabled)' if galerocks_fulvia_firsttime and not galerocks_fulvia_secret_knowsabout and coins < 1:
                pass
            '{image=coingray} “I’ve heard something about your neighbors getting robbed by strangers?” (disabled)' if description_galerocks11 and not galerocks_petronius_about_pastrobbery and coins < 1:
                pass
            '{image=coingray} “I was told something about an old lumberjack hamlet...” (disabled)' if (galerocks_albus_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1) or (galerocks_domitia_firsttime and not banditshideout_knowsaboutlumberjackcamp and coins < 1):
                pass
            '{image=coingray} “Is Cassia trustworthy?” (disabled)' if not quest_recruitahunter_spokento_petronius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and coins < 1:
                pass
            '{image=coingray} “Why do you need coins?” (disabled)' if galerocks_petronius_about_himself == 1 and coins < 1:
                pass
            '“Let’s talk later.”' if (galerocks_petronius_questions_counter) or (not galerocks_petronius_questions_counter and not coins):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk later.”')
                jump galerocksafterinteraction01
            '“I’m not paying you. Farewell.”' if not galerocks_petronius_questions_counter and coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not paying you. Farewell.”')
                jump galerocksafterinteraction01

label galerocksgateguardALL: # {color=#f6d6bd}the gate guard{/color}
    label galerocksgateguard01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay gate at basicfade
        if galerocks_reputation <= 1:
            $ custom1 = "He sighs when he notices your gaze. “What?”"
        elif galerocks_reputation <= 4:
            $ custom1 = "Once he notices your gaze, he frowns, and waits for you to speak."
        elif galerocks_reputation <= 8:
            $ custom1 = "As you get closer, he nods to you."
        else:
            $ custom1 = "Noticing your gaze, he straightens up. “How can I help you?”"
        menu:
            '{color=#f6d6bd}The guard{/color} you met when you first arrived at the village is leaning against the wall, observing both the gates and your mount. Whenever {color=#f6d6bd}[horsename]{/color} snorts, {color=#f6d6bd}the gatekeeper{/color} reaches for his axe.
            \n\n[custom1]
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksgateguard_about_recruitahunter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you ever working with {color=#f6d6bd}Cassia{/color}?”')
        $ quest_recruitahunter_spokento_guard = 1
        $ quest_recruitahunter_cassia_points += 1
        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
            $ quest_recruitahunter_cassia_points_notify2 = 1
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        menu:
            'He stops you with an annoyed grunt. “What did she do this time?” Getting no answer, he waves it off. “Right, I give her orders sometimes, but she’s a tough rock, and won’t get polished easily. More often than not, she’s the first one to run away, saying she’ll {i}get the others{/i}. Give me a break.”
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksgateguardundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I encountered undead in the tunnel south from here...”')
        $ galerocks_guard_about_undead = 1
        menu:
            '“Right, they almost got my wife, they did, when she tried to check out the locked passage. We stay away from there, but talk to our {color=#f6d6bd}digger{/color}. She’s there, with her toys,” he steps away from the wall and looks at the nearest table, where an elderly woman is putting together a humble structure from wooden building blocks.
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksgateguardaboutoutsiders01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In most settlements, people are much more... Hospitable.”')
        $ galerocks_guard_about_outsiders = 1
        $ description_galerocks11 = "I heard that in the past they’ve been mistreated and robbed by outsiders."
        $ description_oldpagos03a = "In {color=#f6d6bd}Gale Rocks{/color}, I heard that the locals are willing to welcome outsiders."
        $ galerocks_church_knowsabout += 1
        menu:
            'He gives you an irritated glance, then stares into the river. “Most settlements have fewer memories of getting robbed by drifters, or of wasting their time on good-for-nothing adventurers. All them {i}free{/i} souls think they have the right to our patience and care, as if they’re some saviors of ours, each one of them. Well, we’ve been beating this land for centuries, with Wright’s help and the patience of our forebears, and if anyone wants our respect, they’d better work for it.”
            \n\nWhen you notice that getting away with theft must not be an easy task, he answers slowly. “Don’t get any weird ideas, outsider. It’s easy to disappear in the hills, or at the crossroads. We’ve got to be vigilant, more than our allies, the stonecutters at {color=#f6d6bd}Old Págos{/color}. They can let themselves be more open to strangers. They have neighbors, gentler roads, and... less of a wall to defend.”
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksgateguardaboutplague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”')
        $ galerocks_guard_about_plague = 1
        menu:
            '“{i}The plague?{/i}” His voice is close to a shout, and a few people glance toward the two of you. The guard grows pale. “Better take it to our {color=#f6d6bd}headwoman{/color}, warden. We were planning trade with them, we were.”
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

    label galerocksgateguardaboutbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you been bothered by bandits in recent seasons?”')
        $ galerocks_guard_about_bandits = 1
        $ description_bandits04 = "The gate guard from {color=#f6d6bd}Gale Rocks{/color} seemed surprised when I mentioned the bandits. He claimed that {color=#f6d6bd}Glaucia{/color} and her band are but a group of treasure hunters and traders."
        $ description_glaucia14 = "The gate guard from {color=#f6d6bd}Gale Rocks{/color} seemed surprised when I mentioned the bandits. He claimed that {color=#f6d6bd}Glaucia{/color} and her band are but a group of treasure hunters and traders."
        if not galerocks_about_bandits_thais:
            $ banditshideout_villagesasked_aboutattacks += 1
            $ galerocks_about_bandits_thais = 1
        menu:
            '“Ehm? What do you mean, {i}bandits{/i}? That useless group of soldiers already faced them half a year ago, ain’t you heard in {color=#f6d6bd}Hovlavan{/color}? They killed and got killed,” he shrugs, as if there’s nothing more to add, but you try to push him harder, sharing some of the gathered rumors.
            \n\n“{color=#f6d6bd}Glaucia{/color} and her group? You’re wrong. She’s from here, she wouldn’t bother us, or our neighbors. She’s just one of the lost {i}free{/i} folk, couldn’t force herself to come back here after... the events that can’t be changed now. She’s just hunting for treasures in the ruins, trading. That’s where she gets her stuff and coins.”
            '
            '“I encountered undead in the tunnel south from here...”' if oldtunnel_inside_undead_seen and not galerocks_iuno_about_oldtunnel_cleared and not severina_about_clearedoldtunnel and not galerocks_guard_about_undead:
                jump galerocksgateguardundead01
            '“In most settlements, people are much more... Hospitable.”' if not galerocks_guard_about_outsiders:
                jump galerocksgateguardaboutoutsiders01
            '“Have you heard about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}?”' if not severina_about_plague1 and not galerocks_guard_about_plague and oldpagos_plague_known:
                jump galerocksgateguardaboutplague01
            '“Were you ever working with {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_guard and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                jump galerocksgateguard_about_recruitahunter01
            '“Have you been bothered by bandits in recent seasons?”' if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b and not galerocks_guard_about_bandits and not galerocks_dabate_abandonsglaucia and not galerocks_dabate_loyaltoglaucia):
                jump galerocksgateguardaboutbandits01
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump galerocksafterinteraction01

label galerocksporciaALL: # {color=#f6d6bd}Porcia{/color}, the cook
    label galerocksporcia01firsttime:
        $ galerocks_porcia_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ shop = "galerocksdinner"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay porcia at basicfade
        menu:
            'You head to the building that releases not only smoke, but also the smell of roasting meat and spices. In front of it, you find a sweating, wrinkled woman with a shaved head and a simple, rag-like band on her hips, and another one, restricting her breasts tightly, as if any movement outside of her control would be too much of a risk to take. She doesn’t even spare you a glance, too busy with mixing ingredients in bowls and cutting vegetables on wooden boards. Her eyes are focused, but whenever she tilts her head high enough for you to see her face, you spot her subtle, yet challenging smile.
            \n\nInside the building, you find another few people, most of them elders, as well as a large fireplace that’s smoking a few dozen hanging fish. When one of the cooks, currently scaling a fresh fish, notices you, he lowers his head and, with a bored voice, addresses the woman. “{color=#f6d6bd}Porcia!{/color} You have an outsider, you do.”
            \n\nThe woman turns toward you in the blink of an eye, standing on spread legs, as if her shell can’t spare you more than a single flinch. “Ehm, didn’t notice you there, stranger. You hungry?” She reaches for a bowl, but stops suddenly. “Right! We serve more than a hundred stomachs, we do, so better give me a reason.”
            '
            '“Such as?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Such as?”')
                $ renpy.notify("New trader unlocked.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
                if not galerocks_food_free:
                    $ custom1 = ""
                else:
                    $ custom1 = "\n\nAfter you explain that you were promised a free service, she chuckles. “Alright, I remember now! Why didn’t you say so sooner!”"
                menu:
                    '“Everyone works for their share. Join them,” she points at the people inside the hollowed cave, but after a few moments, she shakes her head left and right and gets back to her work. “Or pay me a dragon, I guess. It’ll land in the keep’s chest.”[custom1]
                    '
                    '{image=cointest} “I’d like a meal.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                        jump galerocksporcia02
                    # 'I’m not hungry. (disabled)' if pc_food >= 4:
                    #     pass
                    '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                        jump galerocks_porcia_about_herself01
                    '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_porcia_about_recruitahunter01
                    '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                        jump galerocks_porcia_about_recruitahunter01alt
                    'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01

    label galerocksporcia01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerocksdinner"
        show galerocksoverlay porcia at basicfade
        menu:
            'She notices your arrival, but doesn’t spare you more than a nod, still focused on the tasks at hand.
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksporcia02:
        $ shop = "galerocksdinner"
        show screen shopscreen with dissolve
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay porcia at basicfade
        menu:
            'She spares you a short glance.
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksdinnerafterinteraction:
        menu:
            'She’s too busy with her work to pay you attention.
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksdinnerbuyingfoodlabor:
        label galerocks_food_fluffloop:
            $ galerocks_food_fluff = renpy.random.choice(['You’re served a few salad leaves, each wrapped around a different fish - a salted one, a smoked one, and a baked one. You enjoy bits of each and finish with a sliced cucumber and some peas from a bowl.', 'You join a few other people who eat fish soup from large seashells, as well as carrots and slices of melons piled in the center of the table.', 'You’re served hot, baked trout covered with a very salty butter-based garlic sauce.', 'You get a fresh pie, one of dozens that were baked in the morning, and eat it with a few fresh plums on a lonely bench.'])
            if galerocks_food_fluff_old == galerocks_food_fluff:
                jump galerocks_food_fluffloop
            else:
                $ galerocks_food_fluff_old = galerocks_food_fluff
        $ quarters += 9
        $ galerocks_work_hours += 2
        $ pc_food = limit_pc_food(pc_food+3)
        show plus3food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        if quarters > world_daylength-10 or quarters < 34:
            show galerocksboat behind galerocksoverlay at basicfade
        else:
            hide galerocksboat
        menu:
            'You help the cooks wash the dishes and cauldrons, keep the fire alive, cut vegetables, move the barrels, and bring water from the river, then sit down at the table. [galerocks_food_fluff]
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksdinnerbuyingfoodmoney:
        label galerocks_food_fluffloop2:
            $ galerocks_food_fluff = renpy.random.choice(['You’re served a few salad leaves, each wrapped around a fish to pick from - a salted one, a smoked one, and a baked one. You enjoy bits of each and finish with a sliced cucumber and some peas from a bowl.', 'You join a few other people who eat fish soup from bowls, as well as carrots and slices of melons piled in the center of the table.', 'You’re served hot, baked trout covered with a very salty butter-based garlic sauce.', 'You get a fresh pie, one of dozens that were baked in the morning, and eat it with a few fresh plums on a lonely bench.'])
            if galerocks_food_fluff_old == galerocks_food_fluff:
                jump galerocks_food_fluffloop2
            else:
                $ galerocks_food_fluff_old = galerocks_food_fluff
        $ pc_food = limit_pc_food(pc_food+3)
        show plus3food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        show screen notifyimage( "-1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
        menu:
            'You reach for your pouch and the cook turns around, grabbing this and that and placing whatever she finds on the table. [galerocks_food_fluff]
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksdinnerbuyingfoodfree:
        label galerocks_food_fluffloop3:
            $ galerocks_food_fluff = renpy.random.choice(['You’re served a few salad leaves, each wrapped around a fish to pick from - a salted one, a smoked one, and a baked one. You enjoy bits of each and finish with a sliced cucumber and some peas from a bowl.', 'You join a few other people who eat fish soup from bowls, as well as carrots and slices of melons piled in the center of the table.', 'You’re served hot, baked trout covered with a very salty butter-based garlic sauce.', 'You get a fresh pie, one of dozens that were baked in the morning, and eat it with a few fresh plums on a lonely bench.'])
            if galerocks_food_fluff_old == galerocks_food_fluff:
                jump galerocks_food_fluffloop3
            else:
                $ galerocks_food_fluff_old = galerocks_food_fluff
        $ quarters += 1
        $ pc_food = limit_pc_food(pc_food+3)
        show plus3food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        menu:
            'The cook turns around, grabbing this and that and placing whatever she finds on the table. [galerocks_food_fluff]
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocks_porcia_about_herself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your group cooks for the {i}entire{/i} village?”')
        $ galerocks_porcia_about_herself = 1
        menu:
            'She grins toward you. “Right! Safer than fishing, and, you know,” she squeezes her revealed stomach, which is unusually flat. You notice how muscular her arm is. “I move a lot, so I can {i}eat{/i} a lot!” She lets out a chuckle, then moves a large basket of freshly cleaned apples inside the building. “I have only a few years before my back gives up, but I’ve done enough to deserve my slower days!”
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocks_porcia_about_recruitahunter01:
        $ quest_recruitahunter_spokento_porcia_gray = 1
        menu:
            'She puts her hands on her sides and takes a deep breath. “I’m a bit busy here, stranger.”
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocks_porcia_about_recruitahunter01alt:
        $ quest_recruitahunter_spokento_porcia = 1
        $ quest_recruitahunter_cassia_points += 1
        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
            $ quest_recruitahunter_cassia_points_notify2 = 1
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        menu:
            '“More of her fables? If she keeps getting caught sleeping in the middle of her shift, she’ll soon be happy to get any scraps at the end of the day. We don’t have patience around here for the lazy ones,” she gives you a harsh look and turns toward her cutting board.
            '
            '{image=cointest} “I’d like a meal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’d like a meal.”')
                jump galerocksporcia02
            # 'I’m not hungry. (disabled)' if pc_food >= 4:
            #     pass
            '“Your group cooks for the {i}entire{/i} village?”' if not galerocks_porcia_about_herself:
                jump galerocks_porcia_about_herself01
            '“Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me anything about {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_porcia_about_recruitahunter01
            '“{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and galerocks_porcia_about_herself and quest_recruitahunter_spokento_cassia:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Cassia{/color} must be having some extra large meals if she’s as much a fighter as she claims.”')
                jump galerocks_porcia_about_recruitahunter01alt
            'I better speak with other villagers before I ask her more questions about Cassia. (disabled)' if not quest_recruitahunter_spokento_porcia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_porcia_gray and not quest_recruitahunter_spokento_cassia:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

label galerockstatiusALL: # {color=#f6d6bd}Tatius{/color}, the weaponsmith
    label galerockstatius01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_tatius_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ shop = "galerocksweaponsmith"
        show galerocksoverlay tatius at basicfade
        menu:
            'The outer armory is right next to the eastern gate, but you are led behind it, through a fence gate, to the training ground. You are introduced to {color=#f6d6bd}Tatius{/color}, a muscular man who’s walking in just his pants, displaying his muscular chest and arms, tanned and hairy, and his dusty, dirty feet. His teenage pupils, gathered on the trampled ground, also wear no boots and wear old, torn tunics, with marks of blood and scratches both on their clothes and skin.
            \n\nThe man is looking through a few toy weapons gathered in a barrel - a wooden sword, a few spears with their tips wrapped in rags, and similar looking clubs. After your arrival, the man throws a “spear” to one of the younger kids, tells the others to “get to him like mad boars,” and soon after that you hear a painful thud and cheerful laughter.
            \n\nHe then offers you vivid-red cherries, “maybe the last ones this season.” He may be just over thirty years old, yet his wide shoulders, unusual height, and straight posture make even his kindest words sound like a threat. “You need something from me, roadwarden?”
            '
            '“I’m looking for better equipment.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for better equipment.”')
                $ renpy.notify("New trader unlocked.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
                menu:
                    '“Then you came to the wrong village, we don’t sell anything we’ve stored at our armory, we need these things for ourselves.” When you mention dragon bones, he looks away at the fighting kids, and orders them to divide into two teams, letting the assaulted “spearman” rest for a bit. “And what am I to do with dragons? Buy blades?” His chuckle, while fake, is loud, and moves his chest up and down.
                    \n\nAfter you insist that he may want to think if there’s nothing for an axe user, such as yourself, to find here, he puffs out his cheeks, thinking as he exhales. “You know what? Come, take a look. And you!” He looks at the teens. “A few minutes of rest, don’t lose any eyes!”
                    \n\nYou go back to the armory’s door, and after a few breaths the man shows you a kite shield, so large it could cover half your shell with ease. “It’s a gift we received, but we don’t use such a shape, it’s too weird for us. You can buy it, if you wish, or maybe you’d like to grab some quarrels, if you have a crossbow? We have enough of those.”
                    '
                    '“Let’s discuss the price.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss the price.”')
                        show screen shopscreen with dissolve
                        jump galerocksweaponsmithafterinteraction

    label galerockstatius01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerocksweaponsmith"
        show galerocksoverlay tatius at basicfade
        menu:
            '{color=#f6d6bd}Tatius{/color} is behind the armory, teaching a young pupil how to duck.
            '
            '{image=cointest} “I look for new equipment.”' if not item_shield or not galerocks_tatius_shop_bolts:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I look for new equipment.”')
                jump galerockstatius02
            '“Did you use to instruct {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_tatius_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you use to instruct {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_tatius_about_recruitahunter01
            '“I mentioned {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) >= 6) or (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and galerocks_tatius_shop_shield_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_tatius_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) < 6) and (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and not galerocks_tatius_shop_shield_bought):
                pass
            'He has nothing I need. (disabled)' if item_shield and galerocks_tatius_shop_bolts:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerockstatius02:
        $ shop = "galerocksweaponsmith"
        show screen shopscreen with dissolve
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay tatius at basicfade
        menu:
            '{color=#f6d6bd}Tatius{/color} is behind the armory, teaching a young pupil how to duck.
            '
            '{image=cointest} “I look for new equipment.”' if not item_shield or not galerocks_tatius_shop_bolts:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I look for new equipment.”')
                jump galerockstatius02
            '“Did you use to instruct {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_tatius_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you use to instruct {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_tatius_about_recruitahunter01
            '“I mentioned {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) >= 6) or (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and galerocks_tatius_shop_shield_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_tatius_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) < 6) and (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and not galerocks_tatius_shop_shield_bought):
                pass
            'He has nothing I need. (disabled)' if item_shield and galerocks_tatius_shop_bolts:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocksweaponsmithafterinteraction:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerocksweaponsmith"
        menu:
            'He shrugs. “Aside from what I’ve shown you, we need everything we have.”
            '
            '{image=cointest} “I look for new equipment.”' if not item_shield or not galerocks_tatius_shop_bolts:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I look for new equipment.”')
                jump galerockstatius02
            '“Did you use to instruct {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_tatius_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you use to instruct {color=#f6d6bd}Cassia{/color}?”')
                jump galerocks_tatius_about_recruitahunter01
            '“I mentioned {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) >= 6) or (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and galerocks_tatius_shop_shield_bought):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_tatius_about_recruitahunter01alt
            'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) < 6) and (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and not galerocks_tatius_shop_shield_bought):
                pass
            'He has nothing I need. (disabled)' if item_shield and galerocks_tatius_shop_bolts:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump galerocksafterinteraction01

    label galerocks_tatius_about_recruitahunter01:
        if (galerocks_reputation+appearance_charisma) < 6 and not galerocks_tatius_shop_shield_bought:
            $ quest_recruitahunter_spokento_tatius_gray = 1
            menu:
                'You can’t read much from his absent eyes. “Yeah.”
                '
                '{image=cointest} “I look for new equipment.”' if not item_shield or not galerocks_tatius_shop_bolts:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I look for new equipment.”')
                    jump galerockstatius02
                '“Did you use to instruct {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_tatius_gray:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you use to instruct {color=#f6d6bd}Cassia{/color}?”')
                    jump galerocks_tatius_about_recruitahunter01
                '“I mentioned {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) >= 6) or (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and galerocks_tatius_shop_shield_bought):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
                    jump galerocks_tatius_about_recruitahunter01alt
                'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) < 6) and (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and not galerocks_tatius_shop_shield_bought):
                    pass
                'He has nothing I need. (disabled)' if item_shield and galerocks_tatius_shop_bolts:
                    pass
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump galerocksafterinteraction01
        else:
            label galerocks_tatius_about_recruitahunter02:
                $ quest_recruitahunter_spokento_tatius = 1
                $ quest_recruitahunter_cassia_points += 1
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
                    $ quest_recruitahunter_cassia_points_notify2 = 1
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                menu:
                    'He starts to stretch his arms, giving himself a few breaths before he replies. “I don’t know what you want from her, but you’d do better looking for another pair of arms. When necessary, I can put her to use. But she won’t listen to an outsider, no matter the coins.”
                    '
                    '{image=cointest} “I look for new equipment.”' if not item_shield or not galerocks_tatius_shop_bolts:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I look for new equipment.”')
                        jump galerockstatius02
                    '“Did you use to instruct {color=#f6d6bd}Cassia{/color}?”' if not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_tatius_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you use to instruct {color=#f6d6bd}Cassia{/color}?”')
                        jump galerocks_tatius_about_recruitahunter01
                    '“I mentioned {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) >= 6) or (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and galerocks_tatius_shop_shield_bought):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
                        jump galerocks_tatius_about_recruitahunter01alt
                    'He’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and (galerocks_reputation+appearance_charisma) < 6) and (not quest_recruitahunter_spokento_tatius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_tatius_gray and not galerocks_tatius_shop_shield_bought):
                        pass
                    'He has nothing I need. (disabled)' if item_shield and galerocks_tatius_shop_bolts:
                        pass
                    'I step away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                        jump galerocksafterinteraction01

        label galerocks_tatius_about_recruitahunter01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mentioned {color=#f6d6bd}Cassia{/color}...”')
            jump galerocks_tatius_about_recruitahunter02

label galerocksrufinaALL: # {color=#f6d6bd}Rufina{/color}, the tailor
    label galerocksrufina01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_rufina_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ shop = "galerockstailor"
        show galerocksoverlay rufina at basicfade
        menu:
            'You get directions to one of the smaller buildings, which turns out to consist of only one, spacious chamber. Like other caves in the village, it lacks sunlight, but the workbench standing right next to the entrance is well-lit by an oil lamp. The old iron lantern is decorated with the shapes of seaweed and monstrous tentacles.
            \n\nOn the counter you see threads, scraps of clothes, old tunics, and some boots. Behind it, there’s a mature woman, though you can’t precisely guess her age - the flame, dancing because of your movements, distorts the shadows cast by her wrinkles and large nose. Her bright red tunic is light, made of something lighter than hemp or wool. The sleeves end at her elbows, allowing her hands to sew together two pieces of fabric.
            '
            '“Greetings.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Greetings.”')
                $ renpy.notify("New trader unlocked.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
                if not galerocks_armorer_free:
                    $ custom1 = ""
                else:
                    $ custom1 = "\n\nAfter you explain that you were promised a free service, she gives you another glance. “You’re {i}the{/i} roadwarden? Right, I’ll look after your armor for no fee a few times, but nothing more. Work I put into your stuff takes away hours of what could have been done for my neighbors, and we merely need you alive, not pretty.”"
                menu:
                    'She runs her dark, yellow eyes over your clothes. Her hair may be getting gray, but the colorful wooden beads among them distract you right away. “Cheers, stranger. You need something patched up?” After you nod, she looks deeper into the store. “Good, as I’m better at fixing tears than making togs. Take a look.”
                    \n\nIndeed, while there’s plenty of shelves and cupboards covered with pants, tunics, jackets, robes, hats, boots, and bags, many of them seem old, or made from two or three combined pieces of garment. “We buy outfits from other villages,” explains the tailor, maintaining her bored tone. “And as they get worn and damaged, I turn them into something new.”[custom1]
                    '
                    '“Do you have anything for sale?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have anything for sale?”')
                        menu:
                            '“Ehm, my neighbors walk in and put on whatever they feel like wearing, but I ain’t wasting our fabric on outsiders. Maybe you’d like some jewelry?” When you mention you’d rather take something useful for a traveller, she hesitates. “Well... If you really need, I can pack you some old tools of mine. They’d help you fix your armor and togs without anyone’s help, though it ain’t as easy as you would think.”
                            '
                            '“Fine, let’s discuss the prices.”' if not galerocks_iuno_about_oldtunnel_hourglass:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, let’s discuss the prices.”')
                                show screen shopscreen with dissolve
                                jump galerockstailorafterinteraction
                            '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”')
                                $ galerocks_rufina_shop_hourglass_free = 1
                                menu:
                                    '“First time {i}I’m{/i} hearing about it.” As she looks up, the beads in her hair dance in the light. “I’ll just ask her later on. You can pick it up from there,” she nods at a box with pendants, rings, buttons, and buckles. All of them bear the touch of previous owners.
                                    '
                                    'I look around the store.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around the store.')
                                        show screen shopscreen with dissolve
                                        jump galerockstailorafterinteraction

    label galerocksrufina01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerockstailor"
        show galerocksoverlay rufina at basicfade
        menu:
            'Once you enter the dark cave room, {color=#f6d6bd}Rufina{/color} welcomes you with a nod. “Is everything fine?”
            '
            '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                jump galerocks_rufina_about_hourglass_free01
            '{image=cointest} “What can you do for me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                show screen shopscreen with dissolve
                jump galerockstailorafterinteraction
            '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                jump galerocks_rufina_about_recruitahunter01
            '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                jump galerocks_rufina_about_recruitahunter02
            '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_rufina_about_recruitahunter02
            'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                pass
            '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                jump galerocks_rufina_about_necklace01
            '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring01
            '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring02
            '“Thanks.” I head outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                jump galerocksafterinteraction01

    label galerockstailorafterinteraction:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ shop = "galerockstailor"
        menu:
            'She taps her fingers, casting new shadows on the countertop.
            '
            '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                jump galerocks_rufina_about_hourglass_free01
            '{image=cointest} “What can you do for me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                show screen shopscreen with dissolve
                jump galerockstailorafterinteraction
            '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                jump galerocks_rufina_about_recruitahunter01
            '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                jump galerocks_rufina_about_recruitahunter02
            '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_rufina_about_recruitahunter02
            'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                pass
            '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                jump galerocks_rufina_about_necklace01
            '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring01
            '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring02
            '“Thanks.” I head outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                jump galerocksafterinteraction01

    label galerocks_rufina_about_hourglass_free01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_rufina_shop_hourglass_free = 1
        $ shop = "galerockstailor"
        menu:
            '“First time {i}I’m{/i} hearing about it.” As she looks up, the beads in her hair dance in the light. “I’ll just ask her later on. You can pick it up from there,” she nods at a box with pendants, rings, buttons, and buckles. All of them bear the touch of previous owners.
            '
            '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                jump galerocks_rufina_about_hourglass_free01
            '{image=cointest} “What can you do for me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                show screen shopscreen with dissolve
                jump galerockstailorafterinteraction
            '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                jump galerocks_rufina_about_recruitahunter01
            '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                jump galerocks_rufina_about_recruitahunter02
            '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_rufina_about_recruitahunter02
            'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                pass
            '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                jump galerocks_rufina_about_necklace01
            '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring01
            '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring02
            '“Thanks.” I head outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                jump galerocksafterinteraction01

    label galerocks_rufina_about_necklace01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have this necklace with me...”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_rufina_about_necklace = 1
        $ shop = "galerockstailor"
        menu:
            'You show her the strip that’s holding a bunch of flakes and a shell, and she only gives it a glance, then gets back to sewing. “So old, the ones I now make are {i}elegant{/i}. Tell {color=#f6d6bd}Glaucia{/color} I can give her a new one. But the next time she speaks with our {color=#f6d6bd}headwoman{/color} without visiting me I’ll kick her teeth out, be sure she knows that.”
            '
            '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                jump galerocks_rufina_about_hourglass_free01
            '{image=cointest} “What can you do for me?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                show screen shopscreen with dissolve
                jump galerockstailorafterinteraction
            '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                jump galerocks_rufina_about_recruitahunter01
            '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                jump galerocks_rufina_about_recruitahunter02
            '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                jump galerocks_rufina_about_recruitahunter02
            'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                pass
            '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                jump galerocks_rufina_about_necklace01
            '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring01
            '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                jump galerocks_rufina_about_ring02
            '“Thanks.” I head outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                jump galerocksafterinteraction01

    label galerocks_rufina_about_ring01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This bone ring looks like something from here.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_rufina_about_ring = 1
        menu:
            'She moves it to the light, widens her eyes, and speaks with melancholy. “I made it myself, I did, as a little lass. For someone who used to be madly in love, but is now taken by the storms. He was better at digging, than sailing.”
            \n\nShe puts the ring on the counter. “His wife is still around, though. Leave it with me for two coins? It will mean a lot to her.”
            '
            '“Take it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it.”')
                label galerocks_rufina_about_ring02a:
                    show screen notifyimage( "You sold the bone ring.\n+2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the bone ring. +2 {image=cointest}{/i}')
                    $ item_bonering = 0
                    $ galerocks_rufina_about_ring_received = 1
                    $ galerocks_reputation += 1
                    $ coins += 2
                    $ can_leave = 0
                    $ can_rest = 0
                    $ can_items = 0
                    $ shop = "galerockstailor"
                    menu:
                        '“Much appreciated,” she takes out two dragon bones from a box that’s indistinguishable from the one with fasteners, then leaves your ring on the counter.
                        '
                        '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                            jump galerocks_rufina_about_hourglass_free01
                        '{image=cointest} “What can you do for me?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                            show screen shopscreen with dissolve
                            jump galerockstailorafterinteraction
                        '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                            jump galerocks_rufina_about_recruitahunter01
                        '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                            jump galerocks_rufina_about_recruitahunter02
                        '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                            jump galerocks_rufina_about_recruitahunter02
                        'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                            pass
                        '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                            jump galerocks_rufina_about_necklace01
                        '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                            jump galerocks_rufina_about_ring01
                        '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                            jump galerocks_rufina_about_ring02
                        '“Thanks.” I head outside.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                            jump galerocksafterinteraction01
            '“I’d rather keep it for now.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ shop = "galerockstailor"
                menu:
                    '“Ehm, I see,” her eyes narrow.
                    '
                    '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                        jump galerocks_rufina_about_hourglass_free01
                    '{image=cointest} “What can you do for me?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                        show screen shopscreen with dissolve
                        jump galerockstailorafterinteraction
                    '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                        jump galerocks_rufina_about_recruitahunter01
                    '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                        jump galerocks_rufina_about_recruitahunter02
                    '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                        jump galerocks_rufina_about_recruitahunter02
                    'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                        pass
                    '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                        jump galerocks_rufina_about_necklace01
                    '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                        jump galerocks_rufina_about_ring01
                    '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                        jump galerocks_rufina_about_ring02
                    '“Thanks.” I head outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                        jump galerocksafterinteraction01

    label galerocks_rufina_about_ring02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still have the bone ring. You can take it.”')
        jump galerocks_rufina_about_ring02a

    label galerocks_rufina_about_recruitahunter01:
        if (galerocks_reputation+appearance_charisma) < 7:
            $ quest_recruitahunter_spokento_rufina_gray = 1
            menu:
                'She doesn’t look at you, but her hands start to move faster. “And why would {i}I{/i} be the one to ask about her?”
                '
                '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                    jump galerocks_rufina_about_hourglass_free01
                '{image=cointest} “What can you do for me?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                    show screen shopscreen with dissolve
                    jump galerockstailorafterinteraction
                '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                    jump galerocks_rufina_about_recruitahunter01
                '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                    jump galerocks_rufina_about_recruitahunter02
                '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                    jump galerocks_rufina_about_recruitahunter02
                'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                    pass
                '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                    jump galerocks_rufina_about_necklace01
                '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                    jump galerocks_rufina_about_ring01
                '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                    jump galerocks_rufina_about_ring02
                '“Thanks.” I head outside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                    jump galerocksafterinteraction01
        else:
            label galerocks_rufina_about_recruitahunter02:
                $ quest_recruitahunter_spokento_rufina = 1
                $ quest_recruitahunter_cassia_points += 1
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
                    $ quest_recruitahunter_cassia_points_notify2 = 1
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                $ minutes += 5
                menu:
                    'She puts away her tools, leans away, and meets your eyes. “You try to hire her for something, alright? She’s {i}difficult{/i}. Taught herself lies said with a strong voice and confident chest can take one far, but that ain’t a good path in a tribe. Like all souls she has good sides and bad sides, but is too afraid to admit the latter.”
                    \n\nYou chat for a few more minutes. While the tailor’s words are harsh, she can’t hide the sadness of her voice.
                    '
                    '“{color=#f6d6bd}Iuno{/color} mentioned she’d like you to give me an hourglass pendant. As a gift.”' if galerocks_iuno_about_oldtunnel_hourglass and not galerocks_rufina_shop_hourglass_free:
                        jump galerocks_rufina_about_hourglass_free01
                    '{image=cointest} “What can you do for me?”': #UWAŻAJ{image=cointest}
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What can you do for me?”')
                        show screen shopscreen with dissolve
                        jump galerockstailorafterinteraction
                    '“I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”' if not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and not quest_recruitahunter_spokento_rufina_gray:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}Cassia{/color}, the guard.”')
                        jump galerocks_rufina_about_recruitahunter01
                    '“{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and quest_recruitahunter_spokento_fulvia):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Fulvia{/color} mentioned {color=#f6d6bd}Cassia{/color} is you sister.”')
                        jump galerocks_rufina_about_recruitahunter02
                    '“About {color=#f6d6bd}Cassia{/color}...”' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) >= 7 and not quest_recruitahunter_spokento_fulvia):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Cassia{/color}...”')
                        jump galerocks_rufina_about_recruitahunter02
                    'She’s not willing to speak about Cassia with me. (disabled)' if (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and (galerocks_reputation+appearance_charisma) < 7) and (not quest_recruitahunter_spokento_rufina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed and quest_recruitahunter_spokento_rufina_gray and not quest_recruitahunter_spokento_fulvia):
                        pass
                    '“I have this necklace with me...”' if item_oceannecklace and not galerocks_rufina_about_necklace:
                        jump galerocks_rufina_about_necklace01
                    '“This bone ring looks like something from here.”' if item_bonering and not galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                        jump galerocks_rufina_about_ring01
                    '“I still have the bone ring. You can take it.”' if item_bonering and galerocks_rufina_about_ring and not galerocks_rufina_about_ring_received:
                        jump galerocks_rufina_about_ring02
                    '“Thanks.” I head outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.” I head outside.')
                        jump galerocksafterinteraction01

label galerocksfulviaALL: # {color=#f6d6bd}Fulvia{/color}, the room keeper
    label galerocksfulvia01firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ galerocks_fulvia_firsttime = 1
        $ galerocks_npcsmet += 1
        show galerocksoverlay fulvia at basicfade
        menu:
            'Following the instructions, you reach a building with an entrance from the garden side. You step through the door leading into the mouth of the cave, and call the person you were told to speak with - {color=#f6d6bd}Fulvia{/color}, the room keeper. She comes to you from the half-dark corridor.
            \n\nShe fits the description you heard - slightly round, partially because of the tunic and heavy pants hidden beneath the dark-green robe. She looks like an eccentric city priest, what with the massive hourglass made of beautifully polished driftwood she wears and the kerchief covering both her neck and hair.
            \n\nOne feature that hasn’t been mentioned by the locals are her eyes - gray, asymmetrical, partially closed, and unfocused. Once she gets closer, she turns her head, gazing into the rock, and pointing her left ear at you. Her steps are confident, and her hands keep touching the walls on both sides. She’s old, wrinkled, and pale, but her voice remains strong.
            \n\nYour first instinct is to nod, only then realizing it won’t really help you much. She repeats: “You smell of a horse. Room?”
            '
            '“Yes.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes.”')
                menu:
                    '“Right,” she simply walks down the corridor, between the few humble chambers, some of which are inhabited by sleeping souls. After just a few steps, the light coming from the entrance helps you no more. You follow the sounds of boots and the smell of rosemary perfume, then suddenly hear a rock hitting something made of metal. The lit candle makes you sigh with relief.
                    \n\n“What color?” After a quiet moment, she tries again. “The horse coat.”
                    '
                    '“Bay.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bay.”')
                        $ item_horse_coat = "Your horse has a bay coat - intense brown with black legs. Such mounts used to be bred in the capital, by the servants of the emperors."
                        $ custom1 = "She lets out a sigh. “The {i}beast of the emperors{/i}... Must be a beauty.”"
                        jump galerocksfulvia02firsttime
                    '“Black.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Black.”')
                        $ item_horse_coat = "Your horse has a black coat. Such mounts used to be bred for unusual missions, signaling that the messenger shouldn’t be disturbed, for they’re carrying a grim and important message."
                        $ custom1 = "A pause. “The grim messengers... Must not be many of them left,” she says slowly. “I doubt many chiefs can pick and choose one beast for one task, and one for another.”"
                        jump galerocksfulvia02firsttime
                    '“Gray.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gray.”')
                        $ item_horse_coat = "Your horse has a gray coat. Such mounts were popular in the hills around The Growing Mountains, where they can blend-in with the landscape."
                        $ custom1 = "She lets out a surprised grunt. “So far from The Growing Mountains? I guess there are {i}some{/i} gray hills around here.”"
                        jump galerocksfulvia02firsttime
                    '“Mouse dun.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Mouse dun.”')
                        $ item_horse_coat = "Your horse has a mouse dun coat. Such mounts are known for blending in with the northern landscapes of The Dragonwoods."
                        $ custom1 = "Her tongue makes a satisfied click. “My favorite,” she confesses, “blends in with these woods better than any other. I’ll throw it a few pears.”"
                        jump galerocksfulvia02firsttime
                    '“It has white-and-black stripes.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It has white-and-black stripes.”')
                        $ item_horse_coat = "Your horse has white-and-black stripes. Such mounts stand out in the wilderness of The Dragonwoods, but there’s more of them ever since The Southern Invasion."
                        $ custom1 = "“From the {i}barbarians{/i}?” She uses this word with the type of irritation that’s rare among the post-war generations. “I doubt it’ll avoid the beasts for long, standing out so much.”"
                        jump galerocksfulvia02firsttime

    label galerocksfulvia02firsttime:
        menu:
            '[custom1]
            \n\nThe room is far from comforting - the ceiling is only a head above you, the walls are rounded and bare of any decorations, and the only “chest” looks more like a crude crate. At least the dried grasses covering the sleeping pallet are bug-free, and smell of freshness.
            \n\n“You don’t have to share it,” she says with amusement.
            '
            '“How much for... this delight?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much for... this delight?”')
                $ quarters += 1
                $ can_rest = 1
                $ galerocks_fulvia_sleep = 1
                $ renpy.notify("New shelter unlocked.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
                if not galerocks_sleep_free:
                    $ custom1 = ""
                else:
                    $ custom1 = "\n\nAfter you explain that you were promised a free service, she shrugs. “So you’re that roadwarden, are you? Right-alright.”"
                menu:
                    'She chuckles, still turned to you with her profile. “Don’t worry, you won’t be cold, and we don’t let anything mold in here, I have a nose for it,” she demonstrates with a loud sniff. “You can work for the village for merely a few hours in the morning, move some weights around, {i}or{/i} you can pay me two coins. I won’t take less, for I need none at all, I’ll just throw it to {color=#f6d6bd}Severina’s{/color} chest in a few days.”[custom1]
                    '
                    'I have nothing to say to her. (disabled)' if not (shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut) and not (shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2) and not (not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                        pass
                    '“I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”' if shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”')
                        jump galerocks_fulvia_about_shortcut01
                    '“I was at this “orchard” you mentioned. It’s still there, as if someone still looks after it.”' if shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was at the “orchard” you mentioned. It’s still there, as if someone still cares for it.”')
                        jump galerocks_fulvia_about_shortcut02
                    'I bet the road to the “orchard” has changed, but maybe I can still find it by accident. (disabled)' if not shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut:
                        pass
                    '“Do you know who {color=#f6d6bd}Cassia{/color} is?”' if not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know who {color=#f6d6bd}Cassia{/color} is?”')
                        jump galerocks_fulvia_about_recruitahunter01
                    'I leave the cave.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the cave.')
                        jump galerocksafterinteraction01

    label galerocksfulvia01:
        $ can_leave = 0
        $ can_rest = 1
        $ can_items = 0
        show galerocksoverlay fulvia at basicfade
        menu:
            '{color=#f6d6bd}The keeper{/color} doesn’t acknowledge your arrival until you call her. After she leaves the dark tunnel, she says nothing, waiting patiently.
            '
            'I have nothing to say to her. (disabled)' if not (shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut) and not (shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2) and not (not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                pass
            '“I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”' if shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”')
                jump galerocks_fulvia_about_shortcut01
            '“I was at this “orchard” you mentioned. It’s still there, as if someone still looks after it.”' if shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was at the “orchard” you mentioned. It’s still there, as if someone still cares for it.”')
                jump galerocks_fulvia_about_shortcut02
            'I bet the road to the “orchard” has changed, but maybe I can still find it by accident. (disabled)' if not shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut:
                pass
            '“Do you know who {color=#f6d6bd}Cassia{/color} is?”' if not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know who {color=#f6d6bd}Cassia{/color} is?”')
                jump galerocks_fulvia_about_recruitahunter01
            'I leave the cave.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the cave.')
                jump galerocksafterinteraction01

    label galerocks_fulvia_about_shortcut01:
        $ galerocks_fulvia_about_shortcut = 1
        $ shortcut_deepforest_fruitgrove_bestspots = 1
        $ quarters += 1
        menu:
            '“Who’s been saying such {i}silly{/i} things about me?” Hearing your answer, she chuckles. “Ehm, when I was merely a young lass, that road was still wild, barring the wall and the watchtower...”
            \n\nShe shares a few memories with you, but often mentions how the roads changed with every season, with keepers - such as her - being more like pathfinders than guides. For a few minutes, her stories get a bit dark, yet are brought up with a warm smile. Trying to memorize her meandering takes you a bit of an effort. “And every time we reached the tall woods, not the dark ones, in the east, but the tall ones, in the west, right?” She vaguely describes a path leading south, to an “old orchard”.
            \n\n“There were so many fruits, and nuts, and berries, and...” She sighs. “Beasts! So we were picking whatever we could find, but chiefly the hazelnuts, best in the North, and with no worms in them... But stay merely a bit too long, right? And the monsters get to you, from all sides! But without travelers, it must have already overgrown, such a pity!”
            \n\nThe conversation goes on for a few more minutes, but you don’t expect much of it will be of use to you.
            '
            'I have nothing to say to her. (disabled)' if not (shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut) and not (shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2) and not (not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                pass
            '“I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”' if shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”')
                jump galerocks_fulvia_about_shortcut01
            '“I was at this “orchard” you mentioned. It’s still there, as if someone still looks after it.”' if shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was at the “orchard” you mentioned. It’s still there, as if someone still cares for it.”')
                jump galerocks_fulvia_about_shortcut02
            'I bet the road to the “orchard” has changed, but maybe I can still find it by accident. (disabled)' if not shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut:
                pass
            '“Do you know who {color=#f6d6bd}Cassia{/color} is?”' if not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know who {color=#f6d6bd}Cassia{/color} is?”')
                jump galerocks_fulvia_about_recruitahunter01
            'I leave the cave.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the cave.')
                jump galerocksafterinteraction01

    label galerocks_fulvia_about_shortcut02:
        $ galerocks_fulvia_about_shortcut2 = 1
        $ galerocks_reputation += 1
        $ galerocks_church_knowsabout += 1
        if not quest_reachthepaganvillage:
            $ quest_reachthepaganvillage = 1
            $ renpy.notify("New entry: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
        menu:
            'She laughs, clapping her hands, then rubbing her elbows, as if she’s trying to make herself warm. “Still there, oh glorious Wright!” She tilts her blind eyes at the ceiling. “I can’t wait to tell everyone... But who could care about this place, after so many years? It can’t be {color=#f6d6bd}Old Págos{/color}, could it? Or maybe {color=#f6d6bd}The Tribe of The Green Mountain{/color}?” She flinches, as if she said a forbidden secret, then tells you she needs to take care of something, and right away.
            '
            'I have nothing to say to her. (disabled)' if not (shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut) and not (shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2) and not (not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                pass
            '“I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”' if shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”')
                jump galerocks_fulvia_about_shortcut01
            '“I was at this “orchard” you mentioned. It’s still there, as if someone still looks after it.”' if shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was at the “orchard” you mentioned. It’s still there, as if someone still cares for it.”')
                jump galerocks_fulvia_about_shortcut02
            'I bet the road to the “orchard” has changed, but maybe I can still find it by accident. (disabled)' if not shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut:
                pass
            '“Do you know who {color=#f6d6bd}Cassia{/color} is?”' if not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know who {color=#f6d6bd}Cassia{/color} is?”')
                jump galerocks_fulvia_about_recruitahunter01
            'I leave the cave.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the cave.')
                jump galerocksafterinteraction01

    label galerocks_fulvia_about_recruitahunter01:
        $ quest_recruitahunter_spokento_fulvia = 1
        menu:
            'She needs a moment to think. “{color=#f6d6bd}Rufina’s{/color} sister, ehm? Last time I spoke with her she was but a small lass.”
            '
            'I have nothing to say to her. (disabled)' if not (shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut) and not (shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2) and not (not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                pass
            '“I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”' if shortcut_pcknowsabout and galerocks_fulvia_secret_knowsabout and not galerocks_fulvia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that you used to be quite a traveler. Have you seen anything interesting on the road leading through the heart of the woods?”')
                jump galerocks_fulvia_about_shortcut01
            '“I was at this “orchard” you mentioned. It’s still there, as if someone still looks after it.”' if shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut and not galerocks_fulvia_about_shortcut2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was at the “orchard” you mentioned. It’s still there, as if someone still cares for it.”')
                jump galerocks_fulvia_about_shortcut02
            'I bet the road to the “orchard” has changed, but maybe I can still find it by accident. (disabled)' if not shortcut_deepforest_fruitgrove and galerocks_fulvia_about_shortcut:
                pass
            '“Do you know who {color=#f6d6bd}Cassia{/color} is?”' if not quest_recruitahunter_spokento_fulvia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know who {color=#f6d6bd}Cassia{/color} is?”')
                jump galerocks_fulvia_about_recruitahunter01
            'I leave the cave.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the cave.')
                jump galerocksafterinteraction01

label galerocks_florus_ALL: # {color=#f6d6bd}Florus{/color}, the fletcher.
    label galerocks_florus_01firsttime:
        $ galerocks_florus_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay florus at basicfade
        menu:
            'A short man with absent eyes is leaning against the fence, spending his break observing the people gathered at the stools. He’s wearing a torn shirt, patched together from wool in two shades of blue, and has his long hair in a ponytail. When you get closer, he spares you a warm smile. “Cheers, stranger. Are you looking for me?”
            \n\n“That depends,” you respond, and he tilts his head away, observing the sky. “Right. I’m {color=#f6d6bd}Florus{/color}, I make arrows. But I don’t really sell them to outsiders, it’s just {i}our{/i} thing, it is.” As his elbows rest on the wooden planks, his hands dangle loosely, and you notice that they are very clean and well-kept, unusually so for an artisan.
            '
            '“That’s fine. I don’t use a bow.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s fine. I don’t use a bow.”')
                menu:
                    '“Then no hard feelings!” He titters, raises his hands to his head, stretches his back with a yawn, and gets to his stall-like spot, with a workbench covered with wooden staves, knives, sand, flint, quartz, and even obsidian. There are also oddly shaped tools that you can’t really name.
                    \n\nThe man sits down on a chair. “Ehm, you need something from me?”
                    \n\nBefore you respond, you notice the already finished arrows sticking out from a tall basket. They are divided into handspan-sized bunches, each of which has a fletching in different colors and sizes. You step closer, noticing that they also have varied thicknesses, lengths, and use different materials.
                    '
                    '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                        jump galerocks_florus_about_work01
                    '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                        jump galerocks_florus_about_arrows01
                    '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                        jump galerocks_florus_about_magicinarrows01
                    '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                        jump galerocks_florus_about_rhythm01
                    '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                        jump galerocks_florus_about_recruitahunter01
                    'I leave him to his work.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                        jump galerocksafterinteraction01

        label galerocks_florus_01:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            show galerocksoverlay florus at basicfade
            menu:
                '{color=#f6d6bd}Florus{/color} nods toward you, then keeps his eyes on the arrow he’s working on.
                '
                '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                    jump galerocks_florus_about_work01
                '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                    jump galerocks_florus_about_arrows01
                '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                    jump galerocks_florus_about_magicinarrows01
                '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                    jump galerocks_florus_about_rhythm01
                '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                    jump galerocks_florus_about_recruitahunter01
                'I leave him to his work.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                    jump galerocksafterinteraction01

        label galerocks_florus_about_arrows01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do your arrows have so many colors?”')
            $ galerocks_florus_about_arrows = 1
            $ galerocks_florus_about_arrow = 1
            $ galerocks_arrow_clue = 1
            if item_arrow:
                $ custom1 = "\n\nYou think about the arrow you carry in your bundles. Orange and black."
            else:
                $ custom1 = ""
            $ galerocks_florus_interactions += 1
            menu:
                'He turns toward the basket and looks at the arrows, as if he’s just noticed them. “Different needs, different arrows,” he simply states, resting a hand on his knee. “As our forebears learned after using many spells and tools to find the best combinations that these barren hills allow for,” with a nod, he draws your attention to the far east, with its sparse greens and harsh rock faces. “The gray-feathered ones are for harpies, the blue-and-yellow for critters you want to skin for their furs.”
                \n\nYou mention that there are arrows that have partially orange fletching, yet somewhat differ from each other. “Right! Orange is for shells that walk on two legs. If they are also green, they’re for goblins, black are for humans, silver for beastfolk. We don’t shoot at trolls, no point,” he shrugs. [custom1]
                \n\nAfter you ask if the different types truly make a difference, he clicks his tongue. “Maybe? I was taught that spells make it so, but I’m no enchanter. Doesn’t hurt to be prepared.”
                '
                '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                    jump galerocks_florus_about_work01
                '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                    jump galerocks_florus_about_arrows01
                '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                    jump galerocks_florus_about_magicinarrows01
                '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                    jump galerocks_florus_about_rhythm01
                '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                    jump galerocks_florus_about_recruitahunter01
                'I leave him to his work.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                    jump galerocksafterinteraction01

        label galerocks_florus_about_work01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about your work.”')
            $ galerocks_florus_about_hiswork = 1
            $ galerocks_florus_interactions += 1
            menu:
                'He hums to himself for a bit, tilting his head left and right, looking at various tools and parts in front of him. “There’s... A lot to say, stranger. And I won’t look for a successor anytime soon.” After you suggest that he can be as brief as he would like to be, he shrugs. “Ehm, then I don’t know. I grab this,” he reaches for a stave, “round it with this,” he points at some sort of tool, then at the sand, “then cut the feathers, press them into a nock, that’s this groove here...” He lets you take a closer look and carries on. “Then I make a proper head, all by myself... You tie everything, and there it is. An arrow.”
                \n\nSeeing your confusion, he simply clears his throat and gets back to work.
                '
                '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                    jump galerocks_florus_about_work01
                '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                    jump galerocks_florus_about_arrows01
                '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                    jump galerocks_florus_about_magicinarrows01
                '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                    jump galerocks_florus_about_rhythm01
                '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                    jump galerocks_florus_about_recruitahunter01
                'I leave him to his work.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                    jump galerocksafterinteraction01

        label galerocks_florus_about_rhythm01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”')
            $ galerocks_florus_about_therhythm = 1
            $ galerocks_florus_interactions += 1
            menu:
                'He speaks slowly, just discovering this idea together with you. “Ehm, more arrows, right... But doing the same thing, over and over, for hours?” He leans away, with reluctance growing in his eyes by the second. “That would be even {i}more{/i} boring, I’d rather {i}die{/i},” he says with an exaggerated sigh. “We don’t need to sell arrows, just to have enough of them.”
                \n\nAfter you mention that this is the method that would be used in the city, he gives you a sorrowful glance. “Nightmarish.”
                '
                '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                    jump galerocks_florus_about_work01
                '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                    jump galerocks_florus_about_arrows01
                '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                    jump galerocks_florus_about_magicinarrows01
                '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                    jump galerocks_florus_about_rhythm01
                '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                    jump galerocks_florus_about_recruitahunter01
                'I leave him to his work.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                    jump galerocksafterinteraction01

        label galerocks_florus_about_magicinarrows01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could help you learn if there’s real magic in them, you know.”')
            if pc_class == "mage":
                $ at_unlock_spell = 1
                $ manacost = 1
            menu:
                'He dusts his hands and looks into your eyes with hesitation. “How so?”
                '
                '“I have this amulet that, thanks to a ritual I know, can recognize pneuma.” [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have this amulet that, thanks to a ritual I know, can recognize pneuma.”')
                    $ at_unlock_spell = 0
                    $ galerocks_reputation += 1
                    $ galerocks_florus_about_arrow_magic += 1
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ quarters += 2
                    $ galerocks_florus_interactions += 1
                    menu:
                        'After his excited response and way too many questions, you head toward {color=#f6d6bd}[horsename]{/color}, who seems a bit bored. You unpack the wooden spheres, pleasantly smooth and light. The entire set fits in the palm of your hand.
                        \n\nYou place them in various spots - on a single arrow, on a whole bunch, a few steps away from the basket. You begin the ritual, after which all you can do is wait, chatting with the fletcher.
                        \n\nWhen you collect your amulets, their temperature is uneven. The closer a sphere was to an arrow, the warmer it got, but those surrounded by a whole bunch got significantly warmer, as if it’s sensing pneuma from all of them at once.
                        \n\nYou shake the spheres until they cool off, then hide them in your satchel. {color=#f6d6bd}Florus{/color} speaks first. “Any clues?”
                        '
                        '“Well... There’s definitely {i}some{/i} spell held by these arrows, though a weak one. It may be that the stories were true.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well... There’s definitely {i}some{/i} spell held by these arrows, though a weak one. It may be that the stories were true.”')
                            menu:
                                'He flashes you a wide smile and puts his gentle hands together. “Then all those lessons were not for nothing. I...” He pauses, trying to make his voice a bit more dignified. “I’m humbled to know it for sure. Thank you, traveller, I can’t wait to tell this to my neighbors.”
                                \n\nAs he turns away, he still mumbles to himself. “Right... Maybe I {i}should{/i} find myself a student...”
                                '
                                '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                                    jump galerocks_florus_about_work01
                                '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                                    jump galerocks_florus_about_arrows01
                                '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                                    jump galerocks_florus_about_magicinarrows01
                                '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                                    jump galerocks_florus_about_rhythm01
                                '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                                    jump galerocks_florus_about_recruitahunter01
                                'I leave him to his work.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                                    jump galerocksafterinteraction01
                'I lack pneuma to use my wooden spheres. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana" ):
                    pass
                '“You know what? Maybe another time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know what? Maybe another time.”')
                    $ at_unlock_spell = 0
                    jump galerocksafterinteraction01

    label galerocks_florus_about_recruitahunter01:
        $ quest_recruitahunter_spokento_florus = 1
        $ quest_recruitahunter_cassia_points += 1
        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
            $ quest_recruitahunter_cassia_points_notify2 = 1
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        menu:
            'He shakes his head, makes sure he heard you right, and snorts. “Her? Why, rightly not! She’s lucky to have muscles that can handle a club. She ain’t getting anything as precise as this,” he waggs an arrow at you.
            '
            '“Tell me about your work.”' if not galerocks_florus_about_hiswork:
                jump galerocks_florus_about_work01
            '“Why do your arrows have so many colors?”' if not galerocks_florus_about_arrows:
                jump galerocks_florus_about_arrows01
            '“I could help you learn if there’s real magic in them, you know.”' if galerocks_florus_about_arrows and not galerocks_florus_about_arrow_magic and pc_class == "mage":
                jump galerocks_florus_about_magicinarrows01
            '“Wouldn’t it be easier for you to make just the shafts for a day, then the heads on another one? With a good rhythm, you would make more arrows in less time.”' if galerocks_florus_about_hiswork and not galerocks_florus_about_therhythm:
                jump galerocks_florus_about_rhythm01
            '“Is {color=#f6d6bd}Cassia{/color} a decent archer?”' if not quest_recruitahunter_spokento_florus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Cassia{/color} a decent archer?”')
                jump galerocks_florus_about_recruitahunter01
            'I leave him to his work.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave him to his work.')
                jump galerocksafterinteraction01

label galerocksasterionALL: # {color=#f6d6bd}Asterion{/color}
    label galerocksasterion01firsttime:
        $ galerocks_rumor_asterion_firsttime = 1
        $ quarters += 1
        if galerocks_reputation < 6:
            menu:
                '“Right, your {i}wardening{/i} friend?” A guard you speak with doesn’t hide her contempt. “He ain’t been here for many days, almost since the start of the season.” You ask where you could find him, but she gives you a bored shrug and walks away.
                \n\nYou ask other folks as well, but they don’t have much more to say. “He did some small jobs for a few of us,” says a salt worker without meeting your eyes, too busy with throwing firewood into a basket. “The last soul...” He suddenly freezes, then looks around. “Ehm. {i}We{/i} are the last {i}people{/i} to ask, I mean.”
                \n\nYou try to push him into sharing more, but he finds an escape when his overseer shouts at him to “get his ass moving.”
                '
                'I look for someone else.':
                    hide galerocksoverlay
                    if quarters > world_daylength-10 or quarters < 34:
                        show galerocksboat behind galerocksoverlay at basicfade
                    else:
                        hide galerocksboat
                    python:
                        search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump galerockssearch01
                'That’s enough for now.':
                    jump galerocksafterinteraction01
        else:
            $ galerocks_rumor_asterion = 1
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                '“Right, your {i}wardening{/i} friend?” A guard you speak with doesn’t hide her contempt. “He ain’t been here for many days, almost since the start of the season.” You ask where you could find him, but she gives you a bored shrug and walks away.
                \n\nYou ask other folks as well, but they don’t have much more to say. “He did some small jobs for a few of us,” says a salt worker without meeting your eyes, too busy with throwing firewood into a basket. “The last soul...” He suddenly freezes, then looks around. “Ehm. The last soul who spoke with him, that {i}I{/i} know of, was {color=#f6d6bd}Navica{/color}, our boatmaker. They were talking often, you see.”
                '
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    jump galerocksafterinteraction01

    label galerocksasterion01:
        if galerocks_reputation < 6:
            menu:
                'You didn’t learn anything new - according to the locals, {color=#f6d6bd}Asterion{/color} hasn’t been around in many days.
                '
                'I look for someone else.':
                    hide galerocksoverlay
                    if quarters > world_daylength-10 or quarters < 34:
                        show galerocksboat behind galerocksoverlay at basicfade
                    else:
                        hide galerocksboat
                    python:
                        search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump galerockssearch01
                'That’s enough for now.':
                    jump galerocksafterinteraction01
        else:
            jump galerocksasterion02

    label galerocksasterion02:
        if not galerocks_rumor_asterion:
            $ galerocks_rumor_asterion = 1
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                'Since your conversations with the locals are unfolding much more smoothly, you return to the salter who previously hesitated to tell you what he knows about {color=#f6d6bd}Asterion{/color}. He clears his throat, but finally caves in.
                \n\n“There was one soul who spoke with him more than anyone in the village. {color=#f6d6bd}Navica{/color}, our boatmaker.”
                '
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    jump galerocksafterinteraction01
        else:
            menu:
                'You ask around, and everyone confirms that {color=#f6d6bd}Asterion{/color} hasn’t shown up in recent days.
                '
                'I look for someone else.':
                    hide galerocksoverlay
                    if quarters > world_daylength-10 or quarters < 34:
                        show galerocksboat behind galerocksoverlay at basicfade
                    else:
                        hide galerocksboat
                    python:
                        search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump galerockssearch01
                'That’s enough for now.':
                    jump galerocksafterinteraction01

label galerocksbanditsALL: # {color=#f6d6bd}bandits{/color}
    label galerocksbandits01firsttime:
        $ galerocks_rumor_bandits = 1
        if galerocks_dabate_abandonsglaucia:
            jump galerocksbandits02
        elif galerocks_dabate_loyaltoglaucia:
            jump galerocksbandits03
        $ quest_intelforpeltnorth_description04c = "The people of {color=#f6d6bd}Gale Rocks{/color} claim that bandits are not a big issue."
        menu:
            '“What are you asking about, outsider?” A broad-shouldered man raises his voice, and the rest of the group of laborers also scowl at you. “Is it whether we are bandits, or whether we struggle with them?”
            \n\n“Both answers would be {i}stick to your own shit{/i},” chips in a man with burnt hands. “As we do so.”
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01
    label galerocksbandits01:
        if galerocks_dabate_abandonsglaucia:
            jump galerocksbandits02
        elif galerocks_dabate_loyaltoglaucia:
            jump galerocksbandits03
        menu:
            'Whenever you ask any of the locals about the bandits, they tell you they have no time for gossip, and walk away, giving you angry looks.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

    label galerocksbandits02:
        menu:
            'The locals don’t meet your eyes. In their gestures, you spot shame, doubt, and anger.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01
    label galerocksbandits03:
        menu:
            'The locals challenge you with their own gaze. “Our dealings with our neighbors ain’t yours to know.”
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerocksglauciaALL: # {color=#f6d6bd}Glaucia{/color}
    label galerocksglaucia01firsttime:
        $ galerocks_rumor_glaucia = 1
        if galerocks_dabate_abandonsglaucia:
            jump galerocksbandits02
        elif galerocks_dabate_loyaltoglaucia:
            jump galerocksbandits03
        menu:
            '“She’s not here, ain’t been in many months,” says an animal keeper. “Right? If you want to speak with her, find her on your own.”
            \n\nYou ask in a few other places as well, and while everyone seems to confirm these words, you notice that you don’t have to explain who she is, even once.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01
    label galerocksglaucia01:
        if galerocks_dabate_abandonsglaucia:
            jump galerocksbandits02
        elif galerocks_dabate_loyaltoglaucia:
            jump galerocksbandits03
        menu:
            'The locals claim they haven’t seen {color=#f6d6bd}Glaucia{/color} in the recent past, but everyone recognizes her name.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerocksvitaandvaleriusALL: # {color=#f6d6bd}Glaucia’s parents{/color}
    label galerocksvitaandvalerius01firsttime:
        $ galerocks_vitaandvalerius_firsttime = 1
        $ quarters += 1
        $ galerocks_npcsmet += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay vitaandvalerius at basicfade
        menu:
            'You are told to head to the largest “building” in the village, a web of caves and tunnels inhabited by the locals. The first few chambers you walk by are tiny, sometimes shorter than an adult human, with little furniture beside the sleeping spots, a chest or a cupboard, maybe a table and a few stools. It’s a shelter for those who have to spend the night away from the rains, not a “home”.
            \n\nThe walls and ceiling are covered with soot, and all the windows are closed - after you make a turn, you find an almost complete darkness. Not knowing where to go, you ask for assistance, and suddenly {color=#f6d6bd}a young woman{/color} with keen eyes and a candleholder shows up next to you. You can’t tell where she came from. In her other hand, she’s holding a smelly chamber pot. “Stranger? You won’t find anything here. Our lives happen outside.” She’s young, pale, and wears a rugged, undyed tunic.
            '
            '“I’m looking for {color=#f6d6bd}Glaucia’s family{/color}. I was told her parents live here.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m looking for {color=#f6d6bd}Glaucia’s family{/color}. I was told her parents live here.')
                menu:
                    'She whispers, very slowly. “Right. But they are... Old. Tired, and confused, they are,” she gives you a suspicious look. “Follow me, the elders who live here are under my protection, and I’ll give you nothing bar a minute. Don’t haunt them with their past. They already forgot most of it.”
                    \n\nShe holds the candle a bit higher, sharing the light with you, but the first step you take, with the echo making it sound like thunder, makes her flinch. You then hear someone’s weak moan. “Don’t worry, let’s go,” she says as if to herself. She’s walking barefoot, as quiet as your breath.
                    \n\nShe leads you to a set of stairs, then another. It’s hard to believe how many chambers, tiny, dark, and damp, there are.
                    '
                    'I ask her if I can borrow her candle.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask her if I can borrow her candle.')
                        menu:
                            '“Ehm, I ain’t leaving a stranger behind,” she states matter-of-factly. “Either speak while I listen, or not at all.”
                            \n\nYou end up in a chamber that doesn’t stand out from all the others. It has a lit candle inside, and two shapes among the furs, one of them covered with a blanket. You see the movement of their breathing shells, but the elders don’t react to your arrival, and you’re not sure if they are conscious.
                            \n\n“{color=#f6d6bd}Vita{/color}, {color=#f6d6bd}Valerius{/color}. This roadwarden came to see you,” says {color=#f6d6bd}your guide{/color}, then takes a step back.
                            \n\n{color=#f6d6bd}The man{/color} raises his head slowly and puts weight on his elbows. He’s skinny, covered with brown dots, sparse hair, and isn’t as stooped as his companion, who most likely wouldn’t be able to get up on her own. “A warden? Not {color=#f6d6bd}Glaucia{/color}?”
                            '
                            'I chuckle. “Oh, {color=#f6d6bd}Glaucia{/color} is the opposite of a roadwarden.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I chuckle. “Oh, {color=#f6d6bd}Glaucia{/color} is the opposite of a roadwarden.”')
                                $ galerocks_vitaandvalerius_bothered += 1
                                $ custom1 = "“Ehm?” Before you repeat your words, but louder, {color=#f6d6bd}your guide{/color} hisses at you. “Don’t make me regret it.”\n\n"
                                jump galerocksvitaandvalerius01firsttime02
                            '“Maybe she will come later.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe she will come later.”')
                                $ custom1 = ""
                                label galerocksvitaandvalerius01firsttime02:
                                    menu:
                                        '[custom1]“Oh, she’s busy, she is,” says {color=#f6d6bd}the old woman{/color}, but her voice is muffled and you have to lean forward to hear her at all. “She has a new husband now!”
                                        \n\n{color=#f6d6bd}Valerius{/color} chuckles, or maybe clears his throat. “Our little lass, now all grown up... Almost twenty! A child will come soon, alright.”
                                        '
                                        '“She’s married?”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s married?”')
                                            menu:
                                                '“But right, ain’t you heard?” {color=#f6d6bd}Vita’s{/color} voice sounds almost insulted by your question. “This nice cobbler’s lad, what’s his name?”
                                                \n\n{color=#f6d6bd}Both elders{/color} throw a few names around, and {color=#f6d6bd}your guide{/color} adds but a shrug to them.
                                                \n\n“Well, we’ll ask him when we visit, one day,” {color=#f6d6bd}the man{/color} concludes. “They’ll have a new house, in... far away, that village...”
                                                \n\n“In the south,” {color=#f6d6bd}the woman{/color} adds drowsily.
                                                '
                                                '“{color=#f6d6bd}Steep House{/color} is long gone.”' if ruinedvillage_firsttime and ruinedvillage_name == "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Steep House{/color} is long gone.”')
                                                    $ galerocks_vitaandvalerius_bothered += 1
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}gone{/i}? Where did they go?”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Maybe {color=#f6d6bd}Steep House{/color}?”' if ruinedvillage_firsttime and ruinedvillage_name == "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe {color=#f6d6bd}Steep House{/color}?”')
                                                    $ custom1 = "“Right! The wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Those ruins at the southern road?”' if ruinedvillage_firsttime and ruinedvillage_name != "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Those ruins at the southern road?”')
                                                    $ galerocks_vitaandvalerius_bothered += 1
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}bruins{/i}? Are they on their way to {color=#f6d6bd}Steep House{/color}?”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Yes, I... Know the place.”' if ruinedvillage_firsttime and ruinedvillage_name != "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes, I... Know the place.”')
                                                    $ custom1 = "“Yes, help me with... {color=#f6d6bd}Steep House{/color}, right, the wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“I haven’t even heard of such a place. It must have been long ago.”' if not ruinedvillage_firsttime:
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I haven’t even heard of such a place. It must have been long ago.”')
                                                    $ galerocks_vitaandvalerius_bothered += 1
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}long ago{/i}? The wedding was just a few, a few... They just left to {color=#f6d6bd}Steep House{/color}.”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“I see... The village in the south.”' if not ruinedvillage_firsttime:
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see... The village in the south.”')
                                                    $ custom1 = "“Right, you know... {color=#f6d6bd}Steep House{/color}, the wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                        '“She was married?”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She was married?”')
                                            $ galerocks_vitaandvalerius_bothered += 1
                                            menu:
                                                '“What do you mean? Don’t you know our lass?” {color=#f6d6bd}Vita’s{/color} voice grows angry at the very thought. “She just left with that nice cobbler’s lad, what’s his name?”
                                                \n\n{color=#f6d6bd}Both elders{/color} throw a few names around, and {color=#f6d6bd}your guide{/color} adds but a shrug to them.
                                                \n\n“Well, we’ll tell ask him when we visit, one day,” {color=#f6d6bd}the man{/color} concludes. “They’ll have a new house, in... far away, that village...”
                                                \n\n“In the south,” {color=#f6d6bd}the woman{/color} adds drowsily.
                                                '
                                                '“{color=#f6d6bd}Steep House{/color} is long gone.”' if ruinedvillage_firsttime and ruinedvillage_name == "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Steep House{/color} is long gone.”')
                                                    $ galerocks_vitaandvalerius_bothered += 2
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}gone{/i}? Where did they go?”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Maybe {color=#f6d6bd}Steep House{/color}?”' if ruinedvillage_firsttime and ruinedvillage_name == "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe {color=#f6d6bd}Steep House{/color}?”')
                                                    $ custom1 = "“Right! The wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Those ruins at the southern road?”' if ruinedvillage_firsttime and ruinedvillage_name != "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Those ruins at the southern road?”')
                                                    $ galerocks_vitaandvalerius_bothered += 2
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}bruins{/i}? Are they on their way to {color=#f6d6bd}Steep House{/color}?”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“Yes, I... Know the place.”' if ruinedvillage_firsttime and ruinedvillage_name != "Steep House":
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes, I... Know the place.”')
                                                    $ custom1 = "“Yes, help me with... {color=#f6d6bd}Steep House{/color}, right, the wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“I haven’t even heard of such a place. It must have been long ago.”' if not ruinedvillage_firsttime:
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I haven’t even heard of such a place. It must have been long ago.”')
                                                    $ galerocks_vitaandvalerius_bothered += 1
                                                    $ custom1 = "“Ehm?” You hear the painful voice of {color=#f6d6bd}Valerius{/color}, who covers his face with his hands. “What do you mean, {i}long ago{/i}? The wedding was just a few, a few... They just left to {color=#f6d6bd}Steep House{/color}.”\n\n“Such a late hour,” {color=#f6d6bd}your guide{/color} cuts in. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03
                                                '“I see... The village in the south.”' if not ruinedvillage_firsttime:
                                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see... The village in the south.”')
                                                    $ custom1 = "“Right, you know... {color=#f6d6bd}Steep House{/color}, the wondrous little place, with oats, and river, and fire, and...” {color=#f6d6bd}Valerius{/color} stops suddenly, then raises his hands to his eyes, covering them with his shaking fingers. {color=#f6d6bd}Your guide{/color} leans inside, trying to stay calm and reassuring. “Yes, it’s the most beautiful place, and your daughter knows it best!” She gestures for you to step away. “Roadwarden needs to leave now. You’ve been very helpful, both of you. Rest, I’ll be back soon.”"
                                                    jump galerocksvitaandvalerius01firsttime03

        label galerocksvitaandvalerius01firsttime03:
            $ ruinedvillage_name = "Steep House"
            $ description_glaucia02 = "I heard that she was raised by her family in the {color=#f6d6bd}Gale Rocks{/color} village."
            $ description_glaucia12 = "I’ve learned that many years ago she found a husband in the south - in the village of {color=#f6d6bd}Steep House{/color}."
            $ description_glaucia13 = "Her parents are losing their wits, as well as memories."
            if galerocks_vitaandvalerius_bothered < 2:
                $ custom2 = "You go back downstairs, where her voice remains gentle, yet firm. “They shouldn’t have such talks, stranger. They’re in pain, don’t bother them again.” She stops and meets your eyes. “But at least you weren’t cruel. I can appreciate that. Now, scat.” She turns away and disappears in one of the chambers."
                $ pc_lies += 1
            else:
                $ custom2 = "You go back downstairs, where she raises her voice, clutching her fingers around the candle holder. “They shouldn’t have such talks, outsider. They’re in pain, and your cruelty is of no help. Scat, before I kick you outside.” She steps away, but keeps an eye on you."
                $ galerocks_reputation -= 1
            # show galerocksoverlay vitaandvalerius at basicfade
            menu:
                '[custom1]
                \n\n[custom2]
                '
                'I leave the building.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                    jump galerocksafterinteraction01

    label galerocksvitaandvalerius01:
        if galerocks_vitaandvalerius_bothered >= 2:
            jump galerocksvitaandvalerius02
        show galerocksoverlay vitaandvalerius at basicfade
        menu:
            'Soon after you enter the building the young woman with keen eyes and a candle gets in your way. “I can’t let you bother {color=#f6d6bd}Vita{/color} and {color=#f6d6bd}Valerius{/color} any longer, stranger.” Her tone is polite, but won’t take “no” for an answer.
            \n\nYou move outside.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

    label galerocksvitaandvalerius02:
        show galerocksoverlay vitaandvalerius at basicfade
        menu:
            'Soon after you enter the building the young woman with keen eyes and a candle gets in your way. “{color=#f6d6bd}Vita{/color} and {color=#f6d6bd}Valerius{/color} are resting, and will be resting for as long as you are around, outsider.” Her tone makes it clear she won’t take “no” for an answer.
            \n\nYou move outside.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerockspriestALL: # {color=#f6d6bd}Priest{/color}
    label galerockspriest01firsttime:
        $ galerocks_priest_firsttime = 1
        $ galerocks_church_knowsabout += 1
        $ galerocks_npcsmet += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay priest at basicfade
        menu:
            'The first person you speak with, a young cooper on the brink of adulthood, tells you to follow her to the western bank. “Our priest vanished when I was merely this little,” she holds her hand to the height of her chest, “but my family still prays at the temple, every midday. It’s one of the oldest caves in the village!” She says with unmasked pride.
            \n\nYou move past the thatched shed, the smelly kitchen, and around the fortified hill, approaching a humble orchard and what seems to be a training ground for fighters, then descend into a small basin, toward small caves hidden in shadows. The girl enters the mouth without a door.
            '
            'I enter after her and look around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter after her and look around.')
                $ quarters += 1
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                    $ pc_faithpoints_opportunities += 1
                if quarters <= 46 and quarters > 52:
                    $ custom1 = "You arrived during the hours of prayer. There’s more than a dozen whispering people, most of them having wounded or old shells, but also a few children, even though not all of them seem to pay much attention to the solemnity of the moment."
                    if item_wingedhourglass_worn:
                        $ custom2 = "The girl looks at the sacred symbol on your neck and smiles, but says nothing."
                        $ galerocks_reputation += 1
                    else:
                        $ custom2 = "The girl glances at your neck, then in silence observes the sacred symbol on the wall."
                else:
                    $ custom1 = "At this hour, there are only two other souls in sight - an elderly man, napping on a blanket spread in one of the rounded corners, and a boy, who stops his prayer once you come inside, and quickly leaves, giving you an embarrassed look."
                    if item_wingedhourglass_worn:
                        $ custom2 = "Lowering her voice, the girl looks at the sacred symbol on your neck and smiles. “A humbling place, right?”"
                        $ galerocks_reputation += 1
                    else:
                        $ custom2 = "The girl glances at your neck, then observes the sacred symbol on the wall in silence."
                menu:
                    '[custom1]
                    \n\nThe cave is lit by a few oil lamps, with flames surrounded by dyed glass, but the chamber couldn’t fit more than thirty people, even if they were all standing. There are a few stone benches, an altar, and a large, though crude hourglass made of bronze, clean as new. You recognize the gentle hum of a creek, somewhere below you.
                    \n\n[custom2]
                    '
                    'I glance at her and whisper. “Would anyone mind if I were to pray?”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at her and whisper. “Would anyone mind if I were to pray?”')
                        $ pc_faithpoints += 1
                        $ quarters += 1
                        $ galerocks_work_hours += 1
                        $ galerocks_priest_prayer_day = day
                        if pc_religion == "theunitedchurch":
                            $ custom1 = "This place could just as well belong to any other village, having no signs of its fishing or artisan roots, putting humility over expression. It’s united with the River of Faith that you’ve trusted so far, and once you finish your prayer, you feel at home."
                        elif pc_religion == "ordersoftruth":
                            $ custom1 = "You’ve no doubt this place has heard human prayers for centuries, and you try to echo these voices with your own words of praise and request, traveling through generations built on trust. Once you finish your prayer, you feel like you’ve touched the cradle of humanity, finding comfort in a cave that, sometime in the past, gave birth to a human tribe."
                        else:
                            $ custom1 = "This place could just as well belong to any other village, as long as it would be a humble and quiet one. Any prayer here must be honest, with no vanity, nor performative gestures. There is just you and your thoughts, and once you finish your prayer, you know The Wright welcomes it."
                        menu:
                            'She invites you with a gesture and leaves the room. You kneel down, trying to focus. [custom1]
                            '
                            'I get back on my feet, dust off my pants, and step outside.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back on my feet, dust off my pants, and step outside.')
                                jump galerocksafterinteraction01
                    'I nod and step outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and step outside.')
                        jump galerocksafterinteraction01

    label galerockspriest01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay priest at basicfade
        if quarters <= 46 and quarters > 52:
            $ custom1 = "You arrive during the hours of prayer. There’s more than a dozen whispering people, most of them having wounded or old shells, but also a few children, even though not all of them seem to pay much attention to the solemnity of the moment."
        else:
            $ custom1 = "At this hour, there is almost no one inside, and the silence of this place touches you even more."
        menu:
            '[custom1]
            '
            'I spend some time on prayer.' if (pc_religion == "theunitedchurch" and galerocks_priest_prayer_day != day) or (pc_religion == "ordersoftruth" and galerocks_priest_prayer_day != day) or (pc_religion == "fellowship" and galerocks_priest_prayer_day != day) or (pc_religion == "unknown" and galerocks_priest_prayer_day != day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at her and whisper. “Would anyone mind if I were to pray?”')
                jump galerockspriest02
            'I leave the building.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                jump galerocksafterinteraction01

    label galerockspriest02:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ pc_faithpoints_opportunities += 1
        $ pc_faithpoints += 1
        $ quarters += 1
        if quarters <= 46 and quarters > 52:
            $ galerocks_work_hours += 2
        else:
            $ galerocks_work_hours += 1
        $ galerocks_priest_prayer_day = day
        show galerocksoverlay priest at basicfade
        if pc_religion == "theunitedchurch":
            $ custom1 = "This place could just as well belong to any other village, having no signs of its fishing or artisan roots, putting humility over expression. It’s united with the River of Faith that you’ve trusted so far, and once you finish your prayer, you feel at home."
        elif pc_religion == "ordersoftruth":
            $ custom1 = "You’ve no doubt this place has heard human prayers for centuries, and you try to echo these voices with your own words of praise and request, traveling through generations built on trust. Once you finish your prayer, you feel like you’ve touched the cradle of humanity, finding comfort in a cave that, sometime in the past, gave birth to a human tribe."
        else:
            $ custom1 = "This place could just as well belong to any other village, as long as it would be a humble and quiet one. Any prayer here must be honest, with no vanity, nor performative gestures. There is just you and your thoughts, and once you finish your prayer, you know The Wright welcomes it."
        menu:
            'You kneel down, trying to focus. [custom1]
            '
            'I get back on my feet, dust off my pants, and step outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back on my feet, dust off my pants, and step outside.')
                jump galerocksafterinteraction01

label galerockscreekshuntersALL: # {color=#f6d6bd}creekshunters{/color}
    label galerockscreekshunters01firsttime:
        $ galerocks_rumor_missinghunters = 1
        $ quarters += 1
        menu:
            'While some of the locals claim to know the hunters from {color=#f6d6bd}Creeks{/color}, they haven’t seen them in recent days.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

    label galerockscreekshunters01:
        menu:
            'Neither of the hunters have been spotted by the villagers since the last time you asked.
            '
            'I look for someone else.':
                hide galerocksoverlay
                if quarters > world_daylength-10 or quarters < 34:
                    show galerocksboat behind galerocksoverlay at basicfade
                else:
                    hide galerocksboat
                python:
                    search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump galerockssearch01
            'That’s enough for now.':
                jump galerocksafterinteraction01

label galerocks_singlepeople_ALL:
    label galerocks_singlepeople_01firsttime:
        $ galerocks_singlepeople_firsttime = 1
        $ galerocks_npcsmet += 1
        $ galerocks_church_knowsabout += 2
        $ quarters += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        hide galerocksoverlay
        if quarters > world_daylength-10 or quarters < 34:
            show galerocksboat behind galerocksoverlay at basicfade
        else:
            hide galerocksboat
        if not quest_matchmaking:
            $ quest_matchmaking = 1
            $ renpy.notify("New entry: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Matchmaking{/i}')
        else:
            $ renpy.notify("Journal updated: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
        menu:
            'While the vast majority of the locals see this place as their home, and even feel indebted to their families and neighbors for looking after them, {color=#f6d6bd}Paulus{/color} seeks a different path. He isn’t even twenty, but, trained to work on the beach, is strong, slim, and a bit loud. “I can even hunt fish, if that’s the only work left,” he admits when asked about his plans for the future, “just not here, not after all them neighbors turned a blind eye toward my harpy of a mother,” he reveals the scars on his back, left by willow withies.
            \n\nYou mention religion, and he shrugs without a second thought. “Ehm, I can do whatever, barring wicked spells,” you make sure he means necromancy and blood magic. “Right. All I want is a companion for the mornings and evenings, a woman with a kind soul, and if good winds allow us, to be the mother of our children. I’m ready to work for them till I faint,” he flexes his muscles. “I’d gage my arm for that.”
            \n\n{color=#f6d6bd}Marina{/color} is a few years older, but much shorter, pale, and with dark circles under her eyes. While she hopes to find “a wife or a husband”, she won’t leave the village. “I’ve a six-year-old, his father went into the fogs on a foraging trip. I’d love to have more kids, but my forebears have been living in this village for longer than anyone can tell, and I’d rather not make our blood too thick.”
            \n\nYou ask about what sort of traits she’s looking for. “Someone kind, loyal, serious... And diligent, no matter if they’re a water carrier or an artisan. My own back is weak, it is, suffers after standing for long hours. I help with fish smoking, cleaning, foraging... Whatever there is to do.” When asked about her convictions, she looks at you as if the question is beyond absurd. “I won’t lie with a lad or lass that’s a stranger to Wright’s teachings.”
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

    label galerocks_singlepeople_01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        hide galerocksoverlay
        if quarters > world_daylength-10 or quarters < 34:
            show galerocksboat behind galerocksoverlay at basicfade
        else:
            hide galerocksboat
        if not galerocks_singlepeople_paulus_matched and not galerocks_singlepeople_marina_notmatched:
            $ custom1 = "Both {color=#f6d6bd}Paulus{/color} and {color=#f6d6bd}Marina{/color} are still looking for a match."
        elif not galerocks_singlepeople_paulus_matched:
            $ custom1 = "{color=#f6d6bd}Paulus{/color} asks if you have any news."
        elif not galerocks_singlepeople_marina_notmatched:
            $ custom1 = "{color=#f6d6bd}Marina{/color} asks if you have any news."
        else:
            $ custom1 = "There are no other locals who need your help with finding a match. “Come next year,” you hear."
        menu:
            '[custom1]
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

    label galerocks_singlepeople_paulusaskedabouttimo01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.')
        $ galerocks_singlepeople_paulus_timo = 1
        menu:
            'He asks you a few additional questions - some of which are centered around {color=#f6d6bd}Timo’s{/color} face and figure and spoken with embarrassment - then flashes you a wide smile. “Right, she sounds dreamy! If she’s in, I’m in. Let me know what she thinks about me.”
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

    label galerocks_singlepeople_paulus_matched01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.')
        $ galerocks_singlepeople_paulus_work = 1
        $ galerocks_singlepeople_paulus_matched = 1
        $ galerocks_work_hours += 8
        $ quest_matchmaking_points += 1
        if quest_matchmaking_points >= quest_matchmaking_points_max:
            $ quest_matchmaking = 2
            $ pc_goal_iwanttohelppoints += 1
            $ renpy.notify("Quest completed: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Matchmaking{/i}')
        else:
            $ renpy.notify("Journal updated: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
        if not galerocks_singlepeople_marina_notmatched:
            $ custom1 = "You’re still helping {color=#f6d6bd}Marina{/color}, right? We’ve already talked to {color=#f6d6bd}our headwoman{/color}, she agreed to reward your work once your matchmaking is done. Be sure to meet her then."
        else:
            $ custom1 = "You’ve already helped {color=#f6d6bd}Marina{/color}, right? Better speak with our headwoman, then. She has a reward for you."
        menu:
            'He responds with a smile, then warm laughter. “And that’s all? Of course I agree, as long as she teaches me them pyre dances, or whatever it is they do. Tell her I’ll arrive with the spring thaw to meet her,” his voice lowers suddenly, cut by pain. “Without anyone else, I suppose.”
            \n\nHe’s first to mention the compensation for your service. “[custom1]”
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

    label galerocks_singlepeople_marina_shoshi01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.')
        $ galerocks_singlepeople_marina_shoshi = 1
        $ galerocks_singlepeople_marina_religion1 = 1
        menu:
            'She looks around nervously, and her voice is low and hesitant. “An {i}open{/i} relationship, as if...” Seeing her blush, you nod. “Our forebears wouldn’t encourage such a way of living. Does she pray?”
            \n\nWhen you mention that her village in general seems to not put much importance on matters of faith, she seems to lose hope. “Is she pretty at all?” She says without meeting your eyes. You try to answer some more specific questions, making her interest suddenly grow. “If she’s really looking for safe, slow days, ask her if she’s willing to abandon this weird wish. Tell her,” she pauses, then straightens up and speaks with confidence, as if she’s reciting an old story. “Tell her this, outsider. {i}You can find love of soul and shell with me, and a new path free of empty cravings. You won’t ever look back and regret it.{/i}”
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

    label galerocks_singlepeople_marinaaskedaboutreligion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.')
        $ galerocks_singlepeople_marina_religion2 = 1
        $ galerocks_singlepeople_marina_notmatched = 1
        $ galerocks_work_hours += 8
        $ quest_matchmaking_points += 1
        if quest_matchmaking_points >= quest_matchmaking_points_max:
            $ quest_matchmaking = 2
            $ pc_goal_iwanttohelppoints += 1
            $ renpy.notify("Quest completed: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Matchmaking{/i}')
        else:
            $ renpy.notify("Journal updated: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
        if not galerocks_singlepeople_paulus_matched:
            $ custom1 = "You’re also trying to match {color=#f6d6bd}Paulus{/color}, I’ve heard. We asked {color=#f6d6bd}our headwoman{/color} to reward you after you help us both. Be sure to meet her then."
        else:
            $ custom1 = "You’ve already matched {color=#f6d6bd}Paulus{/color}, I’ve heard,” she says, without hiding her jealousy. “Go and speak with our headwoman. She’ll reward your help."
        menu:
            'Her blushing cheeks contrast with the pale skin of her hands. “I can’t,” she says, after a longer moment. “I thought about our previous conversation, roadwarden. I’m not ready for such changes, not just because my son deserves the peace we have now. I’d rather join a monastery than put pleasure above prayer.”
            \n\n“[custom1]”
            '
            'I tell {color=#f6d6bd}Paulus{/color} what I’ve learned about {color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s{/color}.' if howlersdell_timo_firsttime and not galerocks_singlepeople_paulus_timo:
                jump galerocks_singlepeople_paulusaskedabouttimo01
            'I tell {color=#f6d6bd}Paulus{/color} about {color=#f6d6bd}Timo’s{/color} conditions.' if galerocks_singlepeople_paulus_timo and howlersdell_timo_paulus and not galerocks_singlepeople_paulus_work:
                jump galerocks_singlepeople_paulus_matched01
            'I tell {color=#f6d6bd}Marina{/color} what I’ve learned about {color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color}.' if shoshi_single and not galerocks_singlepeople_marina_shoshi:
                jump galerocks_singlepeople_marina_shoshi01
            'I share {color=#f6d6bd}Shoshi’s{/color} message with {color=#f6d6bd}Marina{/color}.' if galerocks_singlepeople_marina_shoshi and shoshi_religion and not galerocks_singlepeople_marina_religion2:
                jump galerocks_singlepeople_marinaaskedaboutreligion01
            'I look for someone else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for someone else.')
                jump galerocksafterinteraction01

label galerocks_cassiaALL: # {color=#f6d6bd}Cassia{/color}
    label galerocks_cassia00:
        if not quest_recruitahunter_spokento_cassia and quest_recruitahunter == 1:
            jump galerocks_cassia01
        elif quest_recruitahunter_spokento_cassia:
            menu:
                'Whenever {color=#f6d6bd}Cassia{/color} notices you, she gets on her feet and starts to “patrol” the village.
                '
                'I look for someone else.':
                    hide galerocksoverlay
                    if quarters > world_daylength-10 or quarters < 34:
                        show galerocksboat behind galerocksoverlay at basicfade
                    else:
                        hide galerocksboat
                    python:
                        search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump galerockssearch01
                'That’s enough for now.':
                    jump galerocksafterinteraction01
        elif quest_recruitahunter == 0 or quest_recruitahunter == 3:
            menu:
                'While there is one guard known as {color=#f6d6bd}Cassia{/color}, you don’t have anything to say to her.
                '
                'I look for someone else.':
                    hide galerocksoverlay
                    if quarters > world_daylength-10 or quarters < 34:
                        show galerocksboat behind galerocksoverlay at basicfade
                    else:
                        hide galerocksboat
                    python:
                        search = renpy.input("Which person or service are you looking for?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump galerockssearch01
                'That’s enough for now.':
                    jump galerocksafterinteraction01

    label galerocks_cassia01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 10
        menu:
            'Finding her takes quite a few minutes. The other guards claim that she’s patrolling the grounds around the village, but you find her sitting against the western wall. Once she sees you, she straightens up, greeting you with spread arms.
            \n\n“An outsider, in our delightful village!” Her shouts make you stop long before you reach her. “And how can {i}I{/i} be of service? Do you need help with bloodthirsty beasts? Are the treacherous bandits chasing after you? Have you lost the taste of life?” Her sudden laughter makes the pigeons fly away. “Speak, speak!”
            '
            '“{color=#f6d6bd}Dalit{/color} heard you’d like to be a huntress.”' if not quest_recruitahunter_spokento_cassia_questions1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalit{/color} heard you’d like to be a huntress.”')
                $ quest_recruitahunter_spokento_cassia_questions1 = 1
                $ custom1 = "“Splendid! As long as you can promise we’ll head to {i}Porcia{/i} for a filling dinner first, I’m ready to leave first thing in the morning!”\n\nHer voice remains loud, adding to her confident gestures and cheerful stance. She’s wearing a decent gambeson, but it’s lazily put on, without tightening the straps and cords, matching her loose, dirty short hair. She’s large, both tall and wide, but has a prominent stomach. The only weapon she’s carrying is a club longer than your arm, and she swings it with enthusiasm. Her dark, yellow eyes are as large as dragon bones, but you can’t read much from them."
                jump galerocks_cassia02

    label galerocks_cassia02:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“Tell me about your talents.”' if quest_recruitahunter_spokento_cassia_questions1 and not quest_recruitahunter_spokento_cassia_questions2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about your talents.”')
                $ quest_recruitahunter_spokento_cassia_questions2 = 1
                $ custom1 = "“And where am I to start?” She raises her club above her head. “I can crush, I can smash, I can catch, I can... Dispatch,” she takes a wide swing and steps forward. “I tore out the first harpy head when I was eight, bare hands!” She shows you her open palm, twice the size of most humans. “{i}Trollhand{/i}, sister called me, until I,” she hits the air between the two of you."
                jump galerocks_cassia02
            '“Are you not satisfied with living here?”' if quest_recruitahunter_spokento_cassia_questions1 and not quest_recruitahunter_spokento_cassia_questions3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you not satisfied with living here?”')
                $ quest_recruitahunter_spokento_cassia_questions3 = 1
                $ custom1 = "“Great home, great people,” she assures you, “great fish, and salt! But the beasts, the space to grow?” She moves her right hand in front of her eye, holding the thumb and the index finger just slightly spread apart. “Tiny!”"
                jump galerocks_cassia02
            '“Fighting is one thing, but the wilderness takes cunning.”' if quest_recruitahunter_spokento_cassia_questions2 and not quest_recruitahunter_spokento_cassia_questions4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fighting is one thing, but the wilderness takes cunning.”')
                $ quest_recruitahunter_spokento_cassia_questions4 = 1
                $ custom1 = "You catch the glimpse of her hesitation when she narrows her eyes, but she soon returns to her loud self. “Are you this eager to hear the tales of my deeds? Want me to tell you how I lifted the curse blocking the mountain trail? Or how I led all them saurians away from our pier? Without me, this place,” she kicks the wall next to her, “would have fallen long ago!”"
                jump galerocks_cassia02
            '“Before I ask you to go anywhere, I want to hear what your tribe has to say about you.”' if quest_recruitahunter_spokento_cassia_questions1 and quest_recruitahunter_spokento_cassia_questions2 and quest_recruitahunter_spokento_cassia_questions3 and quest_recruitahunter_spokento_cassia_questions4 and not quest_recruitahunter_spokento_cassia_questions5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Before I ask you to go anywhere, I want to hear what your tribe has to say about you.”')
                $ quest_recruitahunter_spokento_cassia_questions5 = 1
                $ custom1 = "Suddenly, she looks down and clears her throat, then points at you with her weapon. “Ehm, you ain’t saying you don’t believe me, do you, stranger?” Before you respond, she bursts into laughter. “I guessed so! We're a busy tribe, I better not hear you’re causing trouble around here! Cheers!” She says the last few words while being turned away from, heading to the top of the nearest hill."
                $ quest_recruitahunter_cassia_points += 1
                if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
                    $ quest_recruitahunter_cassia_points_notify2 = 1
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
                    $ quest_recruitahunter_cassia_points_notify1 = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                jump galerocks_cassia02
            '“I’ve no more questions.”' if quest_recruitahunter_spokento_cassia_questions1 and not quest_recruitahunter_spokento_cassia_questions5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve no more questions.”')
                if not quest_recruitahunter_spokento_cassia:
                    $ quest_recruitahunter_spokento_cassia = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                jump galerocksafterinteraction01
            'I leave her alone.' if quest_recruitahunter_spokento_cassia_questions1 and quest_recruitahunter_spokento_cassia_questions5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave her alone.')
                if not quest_recruitahunter_spokento_cassia:
                    $ quest_recruitahunter_spokento_cassia = 1
                    $ renpy.notify("Journal updated: Recruit a Hunter")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
                jump galerocksafterinteraction01
