default thais_bigmad = 0
default thais_bigmad_beaten = 0
default thais_defeated = 0 # no longer a mayor
default thais_friendship = 0
default thais_friendship_pcwantsfood = 0
default thais_inn = 0 # day
default thais_afk = 0
default thais_afk_cause_aegidia = 0
default thais_afk_cause_magicfruit_tookbyforce = 0
default thais_afk_cause_betrayal = 0

default thais_about_questions = 0
default thais_about_bronzerod_threshold = 0
default thais_about_bronzerod_allowed = 0

default thais_about_highisland_recruitment = 0
default thais_about_highisland_recruitment_done = 0
default thais_about_highisland_recruitment_done_used = 0

default thais_about_asterion = 0
default thais_about_asteriona = 0
default thais_about_asterionb = 0
default thais_about_asterionc = 0
default thais_about_asteriond = 0
default thais_about_asterion_comment = 0
default thais_about_joiningthecity = 0
default thais_about_necromancers = 0
default thais_about_nomoreundead = 0
default thais_about_howlers = 0
default thais_about_golemsrods = 0
default thais_about_pyrrhos = 0
default thais_about_banditband = 0
default thais_about_banditband2 = 0
default thais_about_banditbandreward = 0
default thais_about_greenmountaintribe = 0
default thais_about_altar = 0
default thais_about_hermoney = 0
default thais_about_foundasterion = 0
default thais_about_steephouse_fail = 0
default thais_about_plague = 0
default thais_about_plague_cured = 0
default thais_about_daughter_learned = 0
default thais_about_pagans_pcenemy = 0
default thais_about_necklace = 0
default thais_about_wine_threatened = 0
default thais_about_wine = 0
default thais_about_asteriontablet = 0
default thais_about_elpis_playerinterested = 0
default thais_about_fancyclothes = 0

default thais_quest_all_completed = 0
default thais_quest_all_cancelled = 0
default thais_quest_orentius_betrayal_willadmit = 0
default thais_quest_orentius_betrayal_admitted = 0
default thais_quest_orentius02reported = 0
default thais_quest_orentius03a = 0
default thais_quest_orentius03b = 0
default thais_quest_orentius03c = 0
default thais_quest_orentius03d = 0
default thais_about_orentius_banished = 0

default thais_rumor_points = 0
default thais_rumor_points_threshold = 10
default thais_rumor_counter = 0
default thais_rumor_counter_threshold = 2
default thais_rumor_monks_golems = 0
default thais_rumor_eudocia_snakebait = 0
default thais_rumor_elpis_doubt = 0
default thais_rumor_monks_cave = 0
default thais_rumor_greenmountaintribe_found = 0
default thais_rumor_glaucia_found = 0
default thais_rumor_foggylake_purchase = 0
default thais_rumor_glaucia_undead = 0
default thais_rumor_soldiers_leaving = 0
default thais_rumor_soldiers_goal = 0
default thais_rumor_vein = 0
default thais_rumor_forestgarden = 0
default thais_rumor_creeks_missinghunters = 0
default thais_rumor_creeks_struggles = 0
default thais_rumor_galerocks_trading = 0
default thais_rumor_glaucia_revenge = 0
default thais_rumor_elpis_treason = 0

default thais_about_magicfruit = 0
default thais_about_magicfruit_price = 30
default thais_about_magicfruit_barter = 0
default thais_debt = 0
default thais_about_magicfruit_received = 0
default thais_about_magicfruit_tookbyforce = 0 # took it without payment
default thais_about_magicfruit_ate = 0

default thais_hovlavan01 = 0
default thais_hovlavan02 = 0
default thais_hovlavan03 = 0
default thais_hovlavan04 = 0
default thais_hovlavan05 = 0
default thais_hovlavan06 = 0

default thais_fisherhamlet_threshold = 12
default thais_whitemarshes_threshold = 22
default thais_whitemarshes_gray = 0

label howlersdellfirsttimewiththaisALL:
    label howlersdellfirsttimewiththais01:
        $ thais_inn = day
        menu:
            'She’s sitting on a chair with a four-year-old boy on her knees - she’s holding his hand gently, showing him how to eat gruel from a bowl. It’s not a {i}cheap{/i} meal, though - you spot nuts, berries, and milk, and the added honey makes it yellowish. The kid is clean and quiet, and once he notices your arrival, he crams his mouth with a spoonful of oats.
            \n\n“Now, now, love,” {color=#f6d6bd}the mayor{/color} titters, “do ne get {i}distracted{/i},” she rubs the meal off his face. “A few more spoons en you’ll go help papa in the kitchen, aye?” She gives you a radiant, though apologetic, smile, then turns her attention back to her companion.
            '
            'I observe her more closely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe her more closely.')
                menu:
                    'Her long, full-sleeved linen dress must have been dyed once in blue and once in red to achieve its dark, fancy purple, which would draw looks even in {color=#f6d6bd}Hovlavan{/color}. From her left shoulder hangs a green, woolen cape, as thin as a shawl. The brown belt on her waist has a large steel buckle that portrays a running deer with unrealistically large antlers, growing in all directions like tree branches.
                    \n\nUnlike her tribesfolk, she’s pale, with powdered and rouged cheeks, and her lips match her outfit, though they’re a bit closer to wine-red. The thick, gray strands in her long, blond hair look more like a fashion choice than a result of aging. Her eyes are the color of her cape, keen and vigorous.
                    \n\nShe’s shorter than most people around, though would still be the tallest woman in most of the Northern settlements. While she’s around forty, her slim hands add fragility to her appearance, even though her posture is upright, her legs confidently crossed, and her delicate voice assertive. She makes plenty of gestures, but her shoulders hardly ever move.
                    '
                    'I wait for as long as it takes.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for as long as it takes.')
                        $ minutes += 5
                        $ thais_friendship += 1
                        menu:
                            'After a few more minutes, the boy lets out a gentle cough and, after a pat on the back, {color=#f6d6bd}the mayor{/color} puts him on the ground. “You did a great job, love. But now I need to speak with our guest. Darling,” she addresses one of the inn workers, a girl close to fifteen. “Take him to father, will you?” Her tone suddenly gets firmer, leaving no hint of a question or suggestion.
                            \n\n“Yes, ma,” she responds. Both her hair and her eyes are nothing like those of her {i}brother{/i}, and neither of the kids resemble their {i}mother{/i}.
                            \n\n“So we have a roadwarden again? Please, sit down.” She vaguely shows you the palm of her open hand, letting you pick any place you want.
                            '
                            'Since I’m her guest, I sit on a bench next to her.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since I’m her guest, I sit on a bench next to her.')
                                jump howlersdellfirsttimewiththais01ap02a
                            'I sit on the stool, opposite her. I’m here as a trade partner.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit on the stool, opposite her. I’m here as a trade partner.')
                                jump howlersdellfirsttimewiththais01ap02b
                    'I need no invitations. I sit down on a bench.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need no invitations. I sit down on a bench.')
                        menu:
                            '“Just a moment, please,” she glances at you harshly and puts the boy on the ground. “I’m sorry, love, but I need to speak with our {i}guest{/i}. Darling,” she addresses one of the inn workers, a girl close to fifteen. “Take him to father, will you?” Her tone suddenly gets firmer, leaving no hint of a question or suggestion.
                            \n\n“Yes, ma,” she responds. Both her hair and her eyes are nothing like those of her {i}brother{/i}, and neither of the kids resemble their {i}mother{/i}.
                            \n\nThe flowing water hits silently the rocks and wooden stakes surrounding the isle, then splits into two streambeds. In {color=#f6d6bd}Hovlavan{/color} the river is surrounded by tall walls, protecting the banks from deterioration, and the water is seldom free of dirt. Here, the smell is as fresh as it would be in the woods.
                            \n\n“So we have a roadwarden again?” [custom1] “I’m sure you’re hungry. Ma husband will bring us something soon.”
                            '
                            '“I appreciate it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I appreciate it.”')
                                $ thais_friendship_pcwantsfood = 1
                                $ custom1 = "Do ne mention it. Hunger makes me peevish, en the day is too nice for that"
                                jump howlersdellfirsttimewiththais02yes
                            '“No food is free.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No food is free.”')
                                jump howlersdellfirsttimewiththais02no
                            '“I’m not hungry, thanks.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not hungry, thanks.”')
                                jump howlersdellfirsttimewiththais02thanksno

    label howlersdellfirsttimewiththais01ap02a:
        if appearance_charisma <= -1:
            $ thais_friendship -= 1
            $ custom1 = "observes your outfit carefully, at first looking as if she just ate an onion, but then puts on a polite smile. Once your eyes meet, she hardly ever looks away."
        elif appearance_charisma == 0:
            $ thais_friendship -= 0
            $ custom1 = "observes your outfit carefully, maintaining a polite, though cool, smile. Once your eyes meet, she hardly ever looks away."
        else:
            $ thais_friendship += appearance_charisma
            $ custom1 = "observes your outfit carefully, smiling at you with kind approval. Once your eyes meet, she hardly ever looks away. Her voice gets much warmer."
        menu:
            'The flowing water hits silently the rocks and wooden stakes surrounding the isle, then splits into two streambeds. In {color=#f6d6bd}Hovlavan{/color} the river is surrounded by tall walls, protecting the banks from deterioration, and the water is seldom free of dirt. Here, the smell is as fresh as it would be in the woods.
            \n\n{color=#f6d6bd}The mayor{/color} [custom1] “I’m sure you’re hungry. Ma husband will bring us something soon.”
            '
            '“I appreciate it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I appreciate it.”')
                $ thais_friendship_pcwantsfood = 1
                $ custom1 = "Do ne mention it. Hunger makes me peevish, en the day is too nice for that"
                jump howlersdellfirsttimewiththais02yes
            '“No food is free.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No food is free.”')
                jump howlersdellfirsttimewiththais02no
            '“I’m not hungry, thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not hungry, thanks.”')
                jump howlersdellfirsttimewiththais02thanksno

    label howlersdellfirsttimewiththais01ap02b:
        if appearance_charisma <= -1:
            $ custom1 = "observes your outfit carefully, at first looking as if she just ate an onion, but then puts on a polite smile. Once your eyes meet, she hardly ever looks away."
        elif appearance_charisma == 0:
            $ custom1 = "observes your outfit carefully, maintaining a polite, though cool, smile. Once your eyes meet, she hardly ever looks away."
        else:
            $ custom1 = "observes your outfit carefully, smiling at you with kind approval. Once your eyes meet, she hardly ever looks away."
        menu:
            'You have a good look at the inn’s front door, leading to a cellar-like ground floor. It’s dark, with crates and barrels covered with fruits, nuts, and vegetables. The “actual” inn is upstairs, but the only people who go in or out are the workers, most of whom are teenagers.
            \n\n{color=#f6d6bd}The mayor{/color} [custom1] “I’m sure you’re hungry. Ma husband will bring us something soon.”
            '
            '“I appreciate it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I appreciate it.”')
                $ thais_friendship_pcwantsfood = 1
                $ custom1 = "Do ne mention it. Hunger makes me peevish, en the day is too nice for that"
                jump howlersdellfirsttimewiththais02yes
            '“No food is free.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No food is free.”')
                jump howlersdellfirsttimewiththais02no
            '“I’m not hungry, thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not hungry, thanks.”')
                jump howlersdellfirsttimewiththais02thanksno

    label howlersdellfirsttimewiththais02no:
        menu:
            '“Now, now, let’s ne get silly,” she lowers her voice. “{i}Naething{/i} is free, but ne every act of kindness is a trap. I’ll fill your stomach now en we’ll both fill our pouches later on.”
            \n\n“En of course,” she brings back her smile, “‘tis a custom of ours to lend a hand to lost travelers. The forest is full of fruit, en the’s nae reason for us to suffer from hunger.”
            '
            '“Then I accept.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then I accept.”')
                $ thais_friendship_pcwantsfood = 1
                $ custom1 = "Tha’s a relief. You’re saving me from one awkward dinner"
                jump howlersdellfirsttimewiththais02yes
            '“Still, I’m good.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Still, I’m good.”')
                jump howlersdellfirsttimewiththais02nono

    label howlersdellfirsttimewiththais02thanksno:
        menu:
            '“But please, do ne let it stop you!” she chuckles. “He’s an {i}excellent{/i} cook, you do ne want to just {i}smell{/i} his roast. Let’s indulge ourselves, whilst we’re still alive!”
            \n\nWhile she smiles, the fingers of her left hand are tapping the table.
            '
            '“Gladly, thank you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gladly, thank you.”')
                $ thais_friendship_pcwantsfood = 1
                $ custom1 = "Tha’s a relief. You’re saving me from one awkward dinner"
                jump howlersdellfirsttimewiththais02yes
            '“Still, I’m good.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Still, I’m good.”')
                jump howlersdellfirsttimewiththais02nono

    label howlersdellfirsttimewiththais02yes:
        $ at_activate = 1
        $ at = 0
        menu:
            '“[custom1],” she taps her chest and looks at a flock of birds that fly above you loudly, heading south. “As we’re waiting, be so good as to help me understand something. Eva if you’re but a mercenary, I can ne imagine a {i}single{/i} reason for you to choose this realm for your wardening, ne so long after {color=#f6d6bd}Asterion’s{/color} disappearance. The’s nae glory or treasures to find here.”
            \n\nHer pale fingers form a tent on her stomach, then clasp, leaving the forefingers pointing at you. “You were sent here by the merchants. They want the peninsula.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            'I present {color=#f6d6bd}Hovlavan’s{/color} interest as an opportunity.' ( condition="at == 'friendly'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02friendly
            'I portray the situation as lightly as I can.' ( condition="at == 'playful'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02playful
            'I simply explain the situation.' ( condition="at == 'distanced'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02distanced
            'I make it clear that collaborating with the city would keep her people safe.' ( condition="at == 'intimidating'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02intimidating
            'Well, she caught me. I don’t hide the fact that the guild needs new opportunities.' ( condition="at == 'vulnerable'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02vulnerable

    label howlersdellfirsttimewiththais02nono:
        $ at_activate = 1
        $ at = 0
        menu:
            'Her eyes widen, contrasting with her sudden burst of laughter. “So be it! But do ne expect {i}me{/i} to sit here with an empty belly,” she taps her stomach, “I’m a host, ne a martyr! En as we’re waiting, be so good as to help me understand something. Eva if you’re but a mercenary, I can ne imagine a {i}single{/i} reason for you to choose this realm for your wardening, ne so long after {color=#f6d6bd}Asterion’s{/color} disappearance. The’s nae glory or treasures to find here.”
            \n\nHer pale fingers form a tent, then clasp, leaving the forefingers pointing at you. “You were sent here by the merchants. They want the peninsula.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            'I present {color=#f6d6bd}Hovlavan’s{/color} interest as an opportunity.' ( condition="at == 'friendly'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02friendly
            'I portray the situation as lightly as I can.' ( condition="at == 'playful'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02playful
            'I simply explain the situation.' ( condition="at == 'distanced'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02distanced
            'I make it clear that collaborating with the city would keep her people safe.' ( condition="at == 'intimidating'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02intimidating
            'Well, she caught me. I don’t hide the fact that the guild needs new opportunities.' ( condition="at == 'vulnerable'" ):
                $ at_activate = 0
                $ at = 0
                jump howlersdellfirsttimewiththais02vulnerable

    label howlersdellfirsttimewiththais02friendly:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I present {color=#f6d6bd}Hovlavan’s{/color} interest as an opportunity.')
        $ thais_friendship += 1
        $ minutes += 5
        menu:
            'You introduce yourself and touch on the more obvious sides of the potential deal with the guild and the city chief - the troops, their pay and the patrols they would establish, the overview of taxes. “Trade routes would bring new life to this place,” you try to sound warm. “It’s a win-win.”
            \n\nThroughout your speech, {color=#f6d6bd}the mayor{/color} observes you patiently, without interruptions. “I see,” she finally responds. As she observes your palfrey, she twists her deer-buckle, left and right, left and right.
            \n\n“If it was that simple, I’d be eager to applaud. But it never is {i}that{/i} simple, is it?” Her eyes fill up with melancholy, despite her smile. “I appreciate that you’re coming with a carrot, not a stick. But when it comes to the guild, there’s always a catch.”
            \n\nHer accent is now almost identical to the one used in the city.
            '
            '“What sort of catch?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of catch?”')
                jump howlersdellfirsttimewiththais02a
            '“I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”')
                jump howlersdellfirsttimewiththais02b
            '“You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”':
                $ thais_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”')
                jump howlersdellfirsttimewiththais02c
            '“You’re speaking from experience, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re speaking from experience, I assume.”')
                jump howlersdellfirsttimewiththais02d

    label howlersdellfirsttimewiththais02playful:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I portray the situation as lightly as I can.')
        $ thais_friendship += 2
        $ minutes += 5
        menu:
            '“Guilty as charged, {i}we{/i} are!” You answer with a loud whisper and raise your hands to the level of your chest, introducing yourself. You touch on the more obvious sides of the potential deal with the guild and the city chief - the troops, their pay and the patrols they would establish, the overview of taxes - but you keep adding more or less successful puns and casual phrases. “The merchants would bring new life to this place,” you conclude, “and not just them, but the acrobats and bards, as well!”
            \n\n“I get it, I get it!” {color=#f6d6bd}The mayor{/color} says with a smile. Even though she shared a giggle or two with you, she didn’t interrupt your speech. She takes a deep breath and moves the hair from her shoulder to her back, looking at your palfrey.
            \n\n“And sure, if it was just that, I’d ask you where to sign. But it never is {i}that{/i} simple, is it?” Her eyes fill up with melancholy. “I appreciate that you’re coming with a carrot, not a stick. But when it comes to the guild, there’s always a catch.”
            \n\nHer accent is now almost identical to the one used in the city.
            '
            '“What sort of catch?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of catch?”')
                jump howlersdellfirsttimewiththais02a
            '“I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”')
                jump howlersdellfirsttimewiththais02b
            '“You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”':
                $ thais_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”')
                jump howlersdellfirsttimewiththais02c
            '“You’re speaking from experience, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re speaking from experience, I assume.”')
                jump howlersdellfirsttimewiththais02d

    label howlersdellfirsttimewiththais02distanced:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I simply explain the situation.')
        $ minutes += 5
        menu:
            'You introduce yourself and confirm her suspicions. “The guild and the deputy are in agreement. They are willing to send troops to this place, defend the settlements, and patrol the roads. They’d cover their pay, you’d only have to look after their board and lodging.” You explain that the rate of taxes is open to negotiations, but they would be taken twice a year, in spring and fall. “You have time to think about it,” you assure her, “and you’re free to consult with your people. Safer roads bring many travelers, artisans, merchants. I know you realize it’s an opportunity...”
            \n\n“Yes, I do,” she finally interrupts you. “But roads bring other people as well. Not all of them {i}desired{/i} by us.” As she observes your palfrey, she twists her deer-buckle, left and right, left and right.
            \n\n“The times have changed and your superiors were kind enough to send a messenger, not a {i}temple guard{/i} with a list of demands.” She grasps the buckle with her fist. “But when it comes to the guild, there’s always a catch.”
            \n\nHer accent is now almost identical to the one used in the city.
            '
            '“What sort of catch?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of catch?”')
                jump howlersdellfirsttimewiththais02a
            '“I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”')
                jump howlersdellfirsttimewiththais02b
            '“You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”':
                $ thais_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”')
                jump howlersdellfirsttimewiththais02c
            '“You’re speaking from experience, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re speaking from experience, I assume.”')
                jump howlersdellfirsttimewiththais02d

    label howlersdellfirsttimewiththais02intimidating:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I make it clear that collaborating with the city would keep her people safe.')
        $ minutes += 5
        menu:
            'You introduce yourself and explain that nothing is set in stone yet. “Yes, the guild and the army are willing to send troops here, protect your homes and all travelers from beasts and highwaymen.” You touch on the more obvious parts of a potential deal with the city, such as taxes, but you draw her attention back to the matters of safety. “Your tribe will lose some supplies, but it won’t be much, and even less so when compared to the brighter, peaceful future you’ll earn,” you maintain a confident, strong voice.
            \n\nThroughout your speech, {color=#f6d6bd}the mayor{/color} observes you patiently, without interruptions. She keeps playing with her deer-buckle, and finally takes a deep breath, adjusting her cape to give her less of a cover.
            \n\n“If you weren’t a roadwarden, I’d assume that you’re trying to make me worried,” she looks you directly in the eyes. “At least the times have changed and your superiors were kind enough to send a messenger, not a {i}temple guard{/i} with a list of demands. Not that there’s any squad that could truly threaten us, but burning so many people would be a waste of wood.”
            \n\nHer accent is now almost identical to the one used in the city.
            '
            '“I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.”')
                jump howlersdellfirsttimewiththais02b
            '“You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”':
                $ thais_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”')
                jump howlersdellfirsttimewiththais02c
            '“You’re speaking from experience, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re speaking from experience, I assume.”')
                jump howlersdellfirsttimewiththais02d

    label howlersdellfirsttimewiththais02vulnerable:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - Well, she caught me. I don’t hide the fact that the guild needs new opportunities.')
        $ thais_friendship -= 1
        $ minutes += 5
        menu:
            'You introduce yourself and confirm her suspicions. “The war was merciless for all the coastal cities, and now the chief is in agreement with the merchants. Together, we’re stronger.” You touch on the more obvious parts of a potential deal with the city, such as taxes, but you draw her attention back to the matters of safety. “Keeping to yourself, you put your people at risk,” your voice shakes slightly. “By joining The Ten Cities, you’ll protect your people, your land.”
            \n\nThroughout your speech, {color=#f6d6bd}the mayor{/color} observes you without interruptions, but her fingers are tapping on the deer-buckle with frustration. Finally, she takes a deep breath and looks away, at her tribesfolk.
            \n\n“It’s foolish of you to assume {i}our{/i} weakness, [pcname]. We don’t need guidance from The Cities, nor protection. We don’t need {i}help{/i}, and I hope to find more than {i}survival{/i}.” When she looks directly into your eyes, you flinch. “I need real partners, ones who will aid us in our growth. Ones that don’t hide any catch in their promises.”
            \n\nHer accent is now almost identical to the one used in the city.
            '
            '“What sort of catch?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of catch?”')
                jump howlersdellfirsttimewiththais02a
            '“You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”':
                $ thais_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have to trust anyone blindly. The negotiations can satisfy both sides.”')
                jump howlersdellfirsttimewiththais02c
            '“You’re speaking from experience, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re speaking from experience, I assume.”')
                jump howlersdellfirsttimewiththais02d

    label howlersdellfirsttimewiththais02a: #What sort of catch?
        menu:
            '“Well, maybe I phrased it poorly,” she bursts into a joyless laughter. “Not {i}a{/i} catch, but rather all sorts of traps and... {i}omissions{/i}. Like with that saying: {i}give them a finger, and they’ll take the whole hand{/i}. Here, listen to this trick I learned about during my studies.” She theatrically clears her throat, patting her chest with one hand and covering her mouth with another, then leans forward and rests on her elbows, allowing her hands to freely make gestures.
            \n\n“You make a deal with a settlement. Flour and wool in exchange for coin and tools. You send the first traders and they imply that you’re ready to pay more for, let’s say, parchment. Months later, you want no more rye, just the parchment and wool. {i}We can ne butcher any more mouflons{/i}, the locals say. {i}Don’t worry{/i}, you answer. {i}We’ll send you a small flock, just turn one of your fields into a pasturage.{/i}”
            \n\nAs she pretends to speak as different characters, her voice comically shifts, and she has no issue switching between accents.
            '
            'I encourage her with a kind smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I encourage her with a kind smile.')
                jump howlersdellfirsttimewiththais02p02
            'I keep a straight face.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep a straight face.')
                jump howlersdellfirsttimewiththais02p02

    label howlersdellfirsttimewiththais02b: #I’m telling you everything I know. I can’t ask you to trust me, but I’m not hiding anything.
        menu:
            '“Even if I were eager to put trust in the words of a stranger, your {i}honesty{/i} has nothing to do with the truth, necessarily. It doesn’t put me in an easy position, as you can imagine. Here, listen to this trick I learned about during my studies.” She theatrically clears her throat, patting her chest with one hand and covering her mouth with another, then leans forward and rests on her elbows, allowing her hands to freely make gestures.
            \n\n“You make a deal with a settlement. Flour and wool in exchange for coin and tools. You send the first traders and they imply that you’re ready to pay more for, let’s say, parchment. Months later, you want no more rye, just the parchment and wool. {i}We can ne butcher any more mouflons{/i}, the locals say. {i}Don’t worry{/i}, you answer. {i}We’ll send you a small flock, just turn one of your fields into a pasturage.{/i}”
            \n\nAs she pretends to speak as different characters, her voice comically shifts, and she has no issue switching between accents.
            '
            'I encourage her with a kind smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I encourage her with a kind smile.')
                jump howlersdellfirsttimewiththais02p02
            'I keep a straight face.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep a straight face.')
                jump howlersdellfirsttimewiththais02p02

    label howlersdellfirsttimewiththais02c: #You don’t have to trust anyone blindly. The negotiations can satisfy both sides.
        menu:
            '“Oh I wouldn’t dare to trust some coin-hoarding trolls,” she laughs at her own joke. “They would devour the walls that defend them if they could. And I know some of the dirty tricks they use. Here, listen to this one.” She theatrically clears her throat, patting her chest with one hand and covering her mouth with another, then leans forward and rests on her elbows, allowing her hands to freely make gestures.
            \n\n“You make a deal with a settlement. Flour and wool in exchange for coin and tools. You send the first traders and they imply that you’re ready to pay more for, let’s say, parchment. Months later, you want no more rye, just the parchment and wool. {i}We can ne butcher any more mouflons{/i}, the locals say. {i}Don’t worry{/i}, you answer. {i}We’ll send you a small flock, just turn one of your fields into a pasturage.{/i}”
            \n\nAs she pretends to speak as different characters, her voice comically shifts, and she has no issue switching between accents.
            '
            'I encourage her with a kind smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I encourage her with a kind smile.')
                jump howlersdellfirsttimewiththais02p02
            'I keep a straight face.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep a straight face.')
                jump howlersdellfirsttimewiththais02p02

    label howlersdellfirsttimewiththais02d: #You’re speaking from experience, I assume.
        menu:
            '“Do I really sound that confident?” She titters and waves her hand by her chin, as if you just offered her a compliment. “I’ve seen such negotiations during my studies, though I can’t say I took an active part in them. Let me show you an example.” She theatrically clears her throat, patting her chest with one hand and covering her mouth with another, then leans forward and rests on her elbows, allowing her hands to freely make gestures.
            \n\n“You make a deal with a settlement. Flour and wool in exchange for coin and tools. You send the first traders and they imply that you’re ready to pay more for, let’s say, parchment. Months later, you want no more rye, just the parchment and wool. {i}We can ne butcher any more mouflons{/i}, the locals say. {i}Don’t worry{/i}, you answer. {i}We’ll send you a small flock, just turn one of your fields into a pasturage.{/i}”
            \n\nAs she pretends to speak as different characters, her voice comically shifts, and she has no issue switching between accents.
            '
            'I encourage her with a kind smile.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I encourage her with a kind smile.')
                jump howlersdellfirsttimewiththais02p02
            'I keep a straight face.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep a straight face.')
                jump howlersdellfirsttimewiththais02p02

    label howlersdellfirsttimewiththais02p02:
        menu:
            'She swings her hand above the table. “Another year goes by and while there’s more parchment, the village lacks some crops. The tribe needs not just tools and coins, {i}plenty{/i} of coins, but also seeds, and the guild is not satisfied. {i}Sending our wagons costs a lot and there are more highwaymen now. If you want us to come again, you need more mouflons, and to sell us their cheese.{/i}”
            \n\n“And guess what!” With a haunting laugh, she straightens up and spreads her arms, like someone a third her age. “Turns out that the village can’t say {i}no{/i} anymore. They lack supplies, seeds, and land. They can’t refuse!”
            '
            'I nod. She’s right, and it’s better not to say anything stupid.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. She’s right, and it’s better not to say anything stupid.')
                menu:
                    'The pause doesn’t linger for long. “I see we understand each other. Let’s finish the introductions: I’m {color=#f6d6bd}Thais{/color}, one of the keepers of the {color=#f6d6bd}Ape Ale{/color} inn and the mayor of {color=#f6d6bd}Howler’s Dell{/color}. I assume it would be convenient for you to take my answer back to {color=#f6d6bd}Hovlavan{/color}.” She wonders for a moment. “Say, when could we expect the first caravan? After winter?”
                    '
                    '“It depends on what you can sell. And what you want in return.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends on what you can sell. And what you want in return.”')
                        jump howlersdellfirsttimewiththais02p04
            '“Don’t you think the city would see value in keeping you strong? Fewer risks for them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you think the city would see value in keeping you strong? Fewer risks for them.”')
                menu:
                    '“Ha! I definitely {i}don’t{/i} think so. While The Ten Cities are trying to get back on their feet, the tribes are safe, but once they feel confident enough to strike down the resistance, oh, they will. Especially since there’s no imperial court to temper their ambitions.”
                    \n\nShe reaches for her buckle. “A weak settlement with a garrison loyal to {color=#f6d6bd}Hovlavan’s{/color} interest is always more reliable than a place like ours, which can always get loose. No matter what happens, I’m going to look at their hands. And you can tell them that,” she nods toward you, “but you should also take an example from our caution.”
                    \n\nShe straightens up and adjusts her cape. “Let’s finish the introductions: I’m {color=#f6d6bd}Thais{/color}, one of the keepers of the {color=#f6d6bd}Ape Ale{/color} inn and the mayor of {color=#f6d6bd}Howler’s Dell{/color}. I assume it would be convenient for you to take my answer back to {color=#f6d6bd}Hovlavan{/color}.” She wonders for a moment. “Say, when could we expect the first caravan? After winter?”
                    '
                    '“It depends on what you can sell. And what you want in return.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends on what you can sell. And what you want in return.”')
                        jump howlersdellfirsttimewiththais02p04
            'I smile. “I have no doubt that a smart leader like yourself is going to protect her people from these games.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I have no doubt that a smart leader like yourself is going to protect her people from these games.”')
                $ thais_friendship += 1
                menu:
                    '“Oh, how wonderful! Keep the compliments coming!” No soul in the square reacts to her loud laughter. “But all that doesn’t mean I can counter every single city ploy on my own. That’s the good thing about living here, with these kind people all around us,” she nods toward two little girls that are carrying a basket filled with vegetables between them. “If some of us struggle, we all have to deal with the consequences. We all struggle, but we all benefit. But {color=#f6d6bd}Hovlavan{/color}? If they see profit in chopping off our arms, they’ll sell them to the first bidder.”
                    \n\nShe gives you a sad glance, but cheers up after a sigh. “Let’s finish the introductions: I’m {color=#f6d6bd}Thais{/color}, one of the keepers of the {color=#f6d6bd}Ape Ale{/color} inn and the mayor of {color=#f6d6bd}Howler’s Dell{/color}. I assume it would be convenient for you to take my answer back to {color=#f6d6bd}Hovlavan{/color}.” She wonders for a moment. “Say, when could we expect the first caravan? After winter?”
                    '
                    '“It depends on what you can sell. And what you want in return.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends on what you can sell. And what you want in return.”')
                        jump howlersdellfirsttimewiththais02p04

    label howlersdellfirsttimewiththais02p04:
        $ quarters += 1
        if thais_friendship_pcwantsfood:
            $ pc_food = limit_pc_food(pc_food+2)
            show plus2food at foodchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
            menu:
                'While the conversation goes on, the food gets served. The refreshing aroma of roasted mutton, covered with a thick sauce made of mint, parsley, and honey tempts you to bite in right away. The juices are sinking into the round trencher - a plate made of simple, brown bread. There’s also a small bowl filled with chopped red radishes and a sliced boiled egg, and a mug filled with cold buttermilk.
                \n\nIt’s all brought by a few young people - all of them referring to {color=#f6d6bd}the mayor{/color} as their mother - and in the end, the innkeeper himself shows up to wish you a good meal. He’s wearing a clean orange tunic and a not-so-clean apron made of hemp. He politely introduces himself as {color=#f6d6bd}Eryx{/color} and, after confirming you won’t get sick from what he prepared, he leaves you and his wife to your conversation. {color=#f6d6bd}Thais{/color} tears the meat into smaller pieces, then eats slowly, often expressing her enjoyment with a hum.
                '
                'Meanwhile, we get to the important stuff.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Meanwhile, we get to the important stuff.')
                    jump howlersdellfirsttimewiththais02p05
        else:
            menu:
                'While the conversation goes on, the food gets served. The refreshing aroma of roasted mutton, covered with a thick sauce made of mint, parsley, and honey gives you second thoughts. The juices are sinking into the round trencher - a plate made of simple, brown bread. There’s also a small bowl filled with chopped red radishes and a sliced boiled egg, and a mug filled with cold buttermilk.
                \n\nIt’s all brought by a few young people - all of them referring to {color=#f6d6bd}the mayor{/color} as their mother - and in the end, the innkeeper himself shows up to wish you a good meal. He’s wearing a clean orange tunic and a not-so-clean apron made of hemp. He politely introduces himself as {color=#f6d6bd}Eryx{/color} and after confirming you have no interest in a meal, he leaves you and his wife to your conversation. {color=#f6d6bd}Thais{/color} tears the meat to smaller pieces, then eats slowly, often expressing her enjoyment with a hum.
                '
                'Meanwhile, we get to the important stuff.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Meanwhile, we get to the important stuff.')
                    jump howlersdellfirsttimewiththais02p05

    label howlersdellfirsttimewiththais02p05:
        $ quest_explorepeninsula_description10 = "The villagers from {color=#f6d6bd}Howler’s Dell{/color} are willing to sell linen and sturdy clothing in exchange for a squad of soldiers, as well as some iron. They are already well-off and as long as they won’t be forced to follow The United Church, they’re open for trading negotiations."
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        menu:
            'Sounds like the nearby ground is fertile - the village would gladly pay its taxes in grain and vegetables, with the expectation that a squad of soldiers would provide additional protection. “Our youth is strong,” she claims proudly, “so we don’t need {i}your{/i} guards on {i}our{/i} walls. But a lone roadwarden won’t keep the roads passable. We need fighters willing to patrol the paths, maybe even the heart of the woods. That’s what we’d expect in return.”
            \n\nYou’re not an expert when it comes to linen, cheese, and wool, so {color=#f6d6bd}the mayor{/color} spends a good couple of minutes describing the {i}outstanding{/i} quality of what the village has to offer, especially the clothes, which are meant to be as “unique as those made by {i}master Crispus{/i}”. You vaguely recognize the name of this tailor-shoemaker, but you’ve never earned enough to pay him for as much as a single sleeve.
            \n\n“And of course, we will never reject some steel and bronze. We lack alloys for sickles and scythes.”
            \n\nShe then repeats her question about starting a trade route.
            '
            '“Truth be told, the guild is not sure what the peninsula has to offer. It’s going to take more than your village to convince them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Truth be told, the guild is not sure what the peninsula has to offer. It’s going to take more than your village to convince them.”')
                if not quest_easternpath:
                    $ quest_easternpath = 1
                    $ quest_easternpath_description_teaser = "{color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, claims that the people from {color=#f6d6bd}Creeks{/color}, a hunting village in the far North, have some issues with maintaining their roads."
                    $ renpy.notify("New entry: Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Eastern Path{/i}')
                $ description_galerocks01 = "A large fishing village near the northern shore."
                $ description_creeks01 = "A village of fishers, hunters, and woodcutters in the far North."
                menu:
                    '“Understandable, but you won’t find much in the other tribes. They have barely enough to survive, even after they trade for our crops, for we have the only decent soil in this realm. At least the people of {color=#f6d6bd}Gale Rocks{/color} have salt and barrels of fish, while {color=#f6d6bd}Creeks{/color} sells meat and wood. Actually, if you haven’t been in {color=#f6d6bd}Creeks{/color} yet, the farthest village in the northeast, you could give them a chance,” she nods with a smile. “They could use your help with keeping their roads safe. {color=#f6d6bd}White Marshes{/color}, on the other hand, as well as {color=#f6d6bd}Old Págos{/color}, are close to worthless. For a trade route, that is,” she clears her throat.
                    \n\nAfter these words, she stands up, walks to another table, and offers her trencher to an elderly man who sits there by himself. With a trembling voice, he thanks her, then starts to chew on the soggy bread.
                    \n\nShe sits down, wipes her hand into a clean cloth, adjusts the folds of her cape, and once again crosses her legs. “So tell me, [pcname]. How’s {color=#f6d6bd}Hovlavan{/color}? I haven’t gathered much news since the Invasion.”
                    '
                    '“Things stay humble, but are starting to look brighter. The harbor is full of life and the kids grow strong.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Things stay humble, but are starting to look brighter. The harbor is full of life and the kids grow strong.”')
                        $ thais_hovlavan01 = 1
                        $ thaisfirstconversation = 1
                        $ questionpreset = "thais1"
                        menu:
                            '“I was hoping to hear that,” her smile shines with kindness. “I thought they were done for. Losing all those ships and getting cut off from so many tribes... I’m surprised the soldiers didn’t butcher all the priests and traders to fill their stomachs. It felt so unavoidable that I even came back home, afraid for my life. But I still carry memories of that place, most of them warm. I’m glad the others haven’t given up.”
                            \n\nHer smile fades away and she speaks without looking in your direction, giving you a moment of rest. “The first time I crossed the city walls and saw the streets my soul saw them as if they were made of dragon bones, not stone. All those people, and the noise, and high houses, and this... life, happening all around me. But after only two years everything collapsed, for the first time in human memory, like a burning dollhouse.” She pauses, rests her hands on her stomach, and turns back to you. “But don’t let me drag you away from your duties. How can I help you, [pcname]?”
                            '
                            '(thais1 preset)':
                                pass
                    '“Sometimes better, sometimes worse. Not everyone has their own bed, but the new generation is ready to start their own fight.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sometimes better, sometimes worse. Not everyone has their own bed, but the new generation is ready to start their own fight.”')
                        $ thais_hovlavan01 = 2
                        $ thaisfirstconversation = 1
                        $ questionpreset = "thais1"
                        menu:
                            '“And I was afraid it was lost to hunger,” her chuckle is trimmed with scorn. “Good to know I was wrong. When the invasion started, some merchants were cheering in their houses, happy that they would sell out all the blades and food they had stored, can you believe it? {i}This panic will make us rich{/i},” she imitates the voice of a pompous man. “That’s why when the Southerners reached the villages, they found almost nothing to eat.” She sighs. “Staying in a remote peninsula truly can be a blessing.”
                            \n\nShe pauses, hesitant to go on, then shakes her head slightly. “Well, we can’t change the past. How can I help you, [pcname]?”
                            '
                            '(thais1 preset)':
                                pass
                    '“It’s far from great. Children who lost their parents during the war have no trade in hand and there’s not enough settlements to send them away. Many people are unable to prosper.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s far from great. Children who lost their parents during the war have no trade in hand and there’s not enough settlements to send them away. Many people are unable to prosper.”')
                        $ thais_hovlavan01 = 3
                        $ thaisfirstconversation = 1
                        $ questionpreset = "thais1"
                        menu:
                            '“It couldn’t be easy, not after all the blows that landed on that place. That’s the thing with the works of humans, isn’t it? A house you build for half a year turns to dust with a single storm. A proud city falls, the emperor’s mask shatters. The children from this village,” she glances at a young girl cleaning the table, “are just as fragile. They have food, clothes, and walls, but there will be a time of disaster. And once it strikes, and only then, they’ll take to heart the same lesson that The Cities had to learn. And it will be forgotten again after the next sunny spring,” she pauses and looks at you with a sad smile. “But don’t let me babble any longer. What can I do for you, [pcname]?”
                            '
                            '(thais1 preset)':
                                pass

label howlersdellwaitingforthais01: # I ask the nearby guard to find {color=#f6d6bd}the mayor{/color} for me.
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if thais_afk_cause_aegidia == 1:
        jump howlersdellthaisafterafk01
    if thais_afk_cause_betrayal == 1:
        jump howlersdell_thaismad00
    if thais_bigmad:
        jump howlersdell_thaismad01
    if thais_about_asterion_comment:
        if thais_about_asterion_comment == 3:
            $ thais_friendship -= 1
            $ custom1 = "“I was sad to learn not {i}all{/i} of my neighbors returned from your expedition, but the alloys we received will make our tears sweeter.” She observes you for a bit, then smiles. “Good to see you back.”"
        elif thais_about_asterion_comment == 1:
            $ custom1 = "“I’m happy to find you in one piece. My neighbors mentioned your expedition was dangerous, but the alloys they brought back will make their sweat much sweeter.” She observes you for a bit, then smiles. “Good to see you back.”"
        elif thais_about_asterion_comment == 2:
            $ thais_friendship += 1
            $ custom1 = "“I’m happy I can personally thank you for keeping my neighbors safe during your expedition. The alloys you brought are going to be of great help to us.” She gives you a radiant smile. “Lovely to see you back.”"
        $ thais_about_asterion_comment = 0
        $ thais_about_foundasterion = 1
        $ questionpreset = "thais1"
        menu:
            'When the other villagers notice your arrival, they spread quickly. {color=#f6d6bd}Thais{/color} gestures for you to sit down right next to her, where you can smell her strong rose perfume. [custom1]
            '
            '(thais1 preset)':
                pass
    if (thais_about_magicfruit_received and not thais_about_magicfruit_ate) or (thais_about_magicfruit_tookbyforce and not thais_about_magicfruit_ate):
        $ thais_about_magicfruit_ate = 1
        $ minutes += 10
        if thais_afk_cause_magicfruit_tookbyforce == 1:
            $ thais_afk_cause_magicfruit_tookbyforce = 2
        if thais_about_magicfruit_tookbyforce:
            $ quarters += 1
            $ custom1 = "So there’s not {i}that much{/i} bad blood between us, roadwarden!"
            $ custom2 = "is currently busy, but will soon join you."
        else:
            $ minutes += 5
            $ custom1 = "You don’t even know how happy I am to see you!"
            $ custom2 = "needs a few more minutes."
        $ questionpreset = "thais1"
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} [custom2]. You sit down on the bench, and when {color=#f6d6bd}Thais{/color} approaches, she looks much younger, with lively steps, darker cheeks, hair that’s more intensely blond, and lips which are as red as usual, even though they weren’t rouged. “[custom1]” She titters with a strong, inviting voice. “How can I help you today?”
            '
            '(thais1 preset)':
                pass
    if item_fancyclothes and not thais_about_fancyclothes:
        $ thais_about_fancyclothes = 1
        $ thais_friendship += 1
        $ minutes += 5
        $ questionpreset = "thais1"
        menu:
            '“She’ll be here soon,” he responds, so you sit down on the regular bench. After a few minutes, {color=#f6d6bd}Thais{/color} welcomes you with a radiant smile and sits down on her chair. “{color=#f6d6bd}Bion’s{/color} style really looks good on you, [pcname]! You made the right choice trusting her!”
            '
            '(thais1 preset)':
                pass
    if thais_about_pyrrhos < 2 and pyrrhos_quest_escorting:
        $ thais_about_pyrrhos = 2
        $ thais_friendship -= 1
        $ minutes += 15
        $ questionpreset = "thais1"
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} is currently busy, but he’ll mention to her that you’re waiting. You sit down on a bench and wait for quite a while.
            \n\nWhen {color=#f6d6bd}Thais{/color} approaches, she’s far from happy. “I see that {color=#f6d6bd}Pyrrhos{/color} is back, but this time he brings even fewer goods. He shouldn’t be here, [pcname]. His tales are not good for our youngsters.”
            '
            '(thais1 preset)':
                pass
    $ questionpreset = "thais1"
    if thais_friendship+appearance_charisma >= 15:
        menu:
            '{color=#f6d6bd}Thais{/color} joins you even before you speak with the guard, and you sit down by the table together. “It’s {i}lovely{/i} to see you,” her delicate hand grasps yours as she stares at you with her green eyes.
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 12:
        $ minutes += 2
        menu:
            '“Aye, I know. She’ll be here soon,” she says even before you ask. After a minute or two, {color=#f6d6bd}Thais{/color} welcomes you with spread arms, and as she touches your hand gently and sits down next to you, you catch the scent of her rose perfume. “[pcname]! Are your bringing any good news?”
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 9:
        $ minutes += 5
        menu:
            '“She’ll be here soon,” he responds, so you sit down on the regular bench. After a few minutes, {color=#f6d6bd}Thais{/color} welcomes you with a radiant smile and sits down on her chair. “I’m happy to see you, [pcname]!”
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 6:
        $ minutes += 10
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} is currently busy, but she’ll mention to her that you’re waiting. You sit down on a bench and wait for a good few minutes.
            \n\nWhen {color=#f6d6bd}Thais{/color} joins you, she smiles and apologizes for the wait. “It’s always good to see you, [pcname]. How can I help you?”
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 3:
        $ minutes += 15
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} is currently busy, but he’ll mention to her that you’re waiting. You sit down on a bench and wait for quite a while.
            \n\nWhen {color=#f6d6bd}Thais{/color} joins you, she apologizes for the wait. “Welcome back to our village, [pcname]. You wanted to see me?”
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 0:
        $ minutes += 20
        menu:
            'The guard informs you that she needs to look for her, so you sit down on a bench and wait for what feels like an eternity.
            \n\nWhen {color=#f6d6bd}Thais{/color} joins you, she apologizes for the wait, though her voice and eyes are harsh.
            '
            '(thais1 preset)':
                pass

label howlersdelltalkingtothais01: #I head to {color=#f6d6bd}the mayor{/color}.
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if thais_bigmad:
        jump howlersdell_thaismad02
    $ questionpreset = "thais1"
    if thais_about_asterion_comment:
        if thais_about_asterion_comment == 3:
            $ thais_friendship -= 1
            $ custom1 = "“I was sad to learn not {i}all{/i} of my neighbors returned from your expedition, but the alloys we received will make our tears sweeter.” She observes you for a bit, then smiles. “Good to see you back.”"
        elif thais_about_asterion_comment == 1:
            $ custom1 = "“I’m happy to find you in one piece. My neighbors mentioned your expedition was dangerous, but the alloys they brought back will make their sweat much sweeter.” She observes you for a bit, then smiles. “Good to see you back.”"
        elif thais_about_asterion_comment == 2:
            $ thais_friendship += 1
            $ custom1 = "“I’m happy I can personally thank you for keeping my neighbors safe during your expedition. The alloys you brought are going to be of great help to us.” She gives you a radiant smile. “Lovely to see you back.”"
        $ thais_about_asterion_comment = 0
        $ thais_about_foundasterion = 1
        $ questionpreset = "thais1"
        menu:
            'When the other villagers notice your arrival, they spread quickly. {color=#f6d6bd}Thais{/color} gestures for you to sit down right next to her, where you can smell her strong rose perfume. [custom1]
            '
            '(thais1 preset)':
                pass
    if (thais_about_magicfruit_received and not thais_about_magicfruit_ate) or (thais_about_magicfruit_tookbyforce and not thais_about_magicfruit_ate):
        $ thais_about_magicfruit_ate = 1
        $ minutes += 10
        if thais_afk_cause_magicfruit_tookbyforce == 1:
            $ thais_afk_cause_magicfruit_tookbyforce = 2
        if thais_about_magicfruit_tookbyforce:
            $ quarters += 1
            $ custom1 = "So there’s not {i}that much{/i} bad blood between us, roadwarden!"
            $ custom2 = "is currently busy, but will soon join you."
        else:
            $ minutes += 5
            $ custom1 = "You don’t even know how happy I am to see you!"
            $ custom2 = "needs a few more minutes."
        $ questionpreset = "thais1"
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} [custom2]. You sit down on the bench, and when {color=#f6d6bd}Thais{/color} approaches, she looks much younger, with lively steps, darker cheeks, hair that’s more intensely blond, and lips which are as red as usual, even though they weren’t rouged. “[custom1]” She titters with a strong, inviting voice. “How can I help you today?”
            '
            '(thais1 preset)':
                pass
    if item_fancyclothes and not thais_about_fancyclothes:
        $ thais_about_fancyclothes = 1
        $ thais_friendship += 1
        $ minutes += 5
        $ questionpreset = "thais1"
        menu:
            '“She’ll be here soon,” he responds, so you sit down on the regular bench. After a few minutes, {color=#f6d6bd}Thais{/color} welcomes you with a radiant smile and sits down on her chair. “{color=#f6d6bd}Bion’s{/color} style really looks good on you, [pcname]! You made the right choice trusting her!”
            '
            '(thais1 preset)':
                pass
    if thais_about_pyrrhos < 2 and pyrrhos_quest_escorting:
        $ thais_about_pyrrhos = 2
        $ thais_friendship -= 1
        $ minutes += 15
        $ questionpreset = "thais1"
        menu:
            'The guard informs you that {color=#f6d6bd}the mayor{/color} is currently busy, but he’ll mention to her that you’re waiting. You sit down on a bench and wait for quite a while.
            \n\nWhen {color=#f6d6bd}Thais{/color} approaches, she’s far from happy. “I see that {color=#f6d6bd}Pyrrhos{/color} is back, but this time he brings even fewer goods. He shouldn’t be here, [pcname]. His tales are not good for our youngsters.”
            '
            '(thais1 preset)':
                pass
    if thais_friendship+appearance_charisma >= 15:
        menu:
            'When the other villagers notice your arrival, they spread quickly, but give the two of you curious glances. As you sit down, her delicate hand grasps yours and, with a warm smile, she stares into your eyes.
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 12:
        menu:
            'When the other villagers notice your arrival, they spread quickly. {color=#f6d6bd}Thais{/color} gestures for you to sit down right next to her, where you can smell her strong rose perfume.
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 9:
        menu:
            'She welcomes you with a radiant smile, gesturing for her neighbors to leave the two of you alone.
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 6:
        menu:
            'When she notices your approach, she smiles and invites you to sit down.
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 3:
        menu:
            '{color=#f6d6bd}Thais{/color} turns toward you with a polite smile. “How can I help you, [pcname]?”
            '
            '(thais1 preset)':
                pass
    elif thais_friendship+appearance_charisma >= 0:
        menu:
            '{color=#f6d6bd}Thais{/color} speaks with her neighbor, but after you wait for a minute, she nods politely. “What else do you need?”
            '
            '(thais1 preset)':
                pass
    else:
        menu:
            '{color=#f6d6bd}Thais{/color} spares you but a harsh glance. “Yes?”
            '
            '(thais1 preset)':
                pass

label howlersdellthaisafterquestions_ALL:
    label howlersdellthaisafterquestions:
        $ questionpreset = 0
        if thais_bigmad:
            jump howlersdellthaisafterquestionsBIGMAD
        if not thais_about_questions: # the Backwood Corner
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“I wonder... Back in {color=#f6d6bd}Hovlavan{/color}, did you spend any time in Backwood Corner? It used to be this dark, dirty alley, with muggers {i}working{/i} even in daylight. I stayed there with Octavia, the miller, in exchange for doing chores for her. She had this small, wooden hut.”
                '
                '“Since the war, even the soldiers have avoided that street. People say it’s a home for thugs.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Since the war, even the soldiers have avoided that street. People say it’s a home for thugs.”')
                    $ thais_hovlavan02 = 1
                    $ questionpreset = "thais1"
                    menu:
                        '“Oh dear, is that so? Maybe it was bound to happen. Kindness and hospitality don’t bloom in days of hunger. I hope the good old lady of The Boarhead Inn didn’t have to see that. She did her best to keep the children off the street, it must have been heartbreaking to see them turn against each other.”
                        '
                        '(thais1 preset)':
                            pass
                '“You wouldn’t recognize it. It’s now a respectable street, with one of the fanciest inns in the city - The Apple And The Boar.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wouldn’t recognize it. It’s now a respectable street, with one of the fanciest inns in the city - The Apple And The Boar.”')
                    $ thais_hovlavan02 = 2
                    $ questionpreset = "thais1"
                    menu:
                        'You describe how a family of Southerners started a large shipyard right next to the alley, working on exotic boats in unusual shapes. Needing hands to work, they offered food and coins to many local thugs, and with time, more light and stalls showed up in the alley.
                        \n\nAs you describe the new inn, {color=#f6d6bd}Thais{/color} bursts into cheerful laughter. “So it’s the same family that ran The Boarhead Inn? And to think that I dared to doubt the old lady’s endurance! People like her, brave enough to bear the toil of their world, are going to bring salvation to all of us.”
                        '
                        '(thais1 preset)':
                            pass
                '“It would make you feel like you’re in the old days. The Boarhead Inn is almost fifty years old, now.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It would make you feel like you’re in the old days. The Boarhead Inn is almost fifty years old, now.”')
                    $ thais_hovlavan02 = 3
                    $ questionpreset = "thais1"
                    menu:
                        'You explain that while the place is still called the {i}bad{/i} part of the city, The Boarhead makes good coin selling beer and ale to students, mercenaries, and adventurers. “The whole Land may turn wild one day,” you quote one of the local traders, “but Backwood Corner will stay the same.”
                        \n\nShe sighs with relief and puts her left hand on her hip. “Comforting, don’t you think? That there are these places, these dark corners, where you can always find what you expect. Living there, though? That sounds awful, and always was,” she chuckles. “I bet the thugs of my youth are no longer around, so I wouldn’t count on them giving me a free pass. But I wish I could have a chance to drink a mug or two with the innkeeper once more. The old lady was always too good to stay in that muck.”
                        '
                        '(thais1 preset)':
                            pass
                '“There’s no such street anymore. It fell to a great fire.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s no such street anymore. It fell to a great fire.”')
                    $ thais_hovlavan02 = 4
                    $ questionpreset = "thais1"
                    menu:
                        'You tell her about the riots that happened two years after the invasion, led by hungry, ill people with no place to go. You describe briefly the streets that have risen from the ashes, but it doesn’t spark her interest. “I can’t say I {i}miss{/i} that place, but it’s weird to think that such a strong memory is no longer a part of reality. Like a tree that you’ve walked by a thousand times, and one day it’s been cut down.” She sits silent, absently observing your lips.
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 1: # what do people wear?
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“Tell me, how do people dress in the city these days? Is it similar to what we have here? Before the war, the merchants were wearing those really long dresses and robes, way too long for my taste. They got mud stains after every rain, and I see no reason to keep shoes completely hidden.”
                '
                '“Not anymore. There’s always a shortage of fabric. Most people wear tunics, like in the old days.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not anymore. There’s always a shortage of fabric. Most people wear tunics, like in the old days.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan03 = 1
                    menu:
                        '“At least we can hope that if the visitors arrive, we won’t stand out much!” She laughs, but also adjusts her dress, drawing your attention to its superb quality. “And who knows, maybe our little village here is going to help those unfortunate clothiers? I’m sure we could spare a couple of sheets of fabric.”
                        '
                        '(thais1 preset)':
                            pass
                '“For years there was not enough hemp and wool at hand, so people have started to wear furs again.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “For years there was not enough hemp and wool at hand, so people have started to wear furs again.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan03 = 2
                    menu:
                        '“Now, that’s just sad. When I was there, only the monks wore them, for... some reason. I’ve no doubt that the vengeful beasts have thrown the roads into a nightmare. The cityfolk would be smarter putting on rags.” Even though she sighs, there’s a cruel satisfaction in her smile.
                        '
                        '(thais1 preset)':
                            pass
                '“As far as I can tell, many folks wear headgear.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “As far as I can tell, many folks wear headgear.”')
                    $ questionpreset = "thais1"
                    $ quarters += 1
                    $ thais_friendship += 1
                    $ thais_hovlavan03 = 3
                    menu:
                        'You describe the complex world of veils, worn by rich folks who try to express their {i}modesty{/i} by covering their long hair; of hoods, which, thanks to the colorful embroidery, get fancier with every year; of light caps and heavier {i}turbans{/i} introduced by merchants from The Southern Realms.
                        \n\n{color=#f6d6bd}The mayor{/color} has plenty of questions about colors, materials, prices... Only after you satisfy her curiosity does she let you change the topic, though still with shining eyes.
                        '
                        '(thais1 preset)':
                            pass
                '“I’m not sure. I don’t pay much attention to... {i}fashion{/i}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not sure. I don’t pay much attention to... {i}fashion{/i}.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship -= 1
                    $ thais_hovlavan03 = 4
                    menu:
                        'She pushes you with more detailed questions: What do the merchants wear? How about priests? Do armorers have enough linen and padding?” You struggle to say much, and she finally falls silent, observing you with annoyance.
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 2: # where is the player from
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“We talk and talk, but I still don’t know where you are from, [pcname]. What’s your story? Have you lived in {color=#f6d6bd}Hovlavan{/color} your entire life?”
                '
                '“In a way. I know it as well as any other cityfolk, but every spring I trained in horsemanship in a nearby village.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In a way. I know it as well as any other cityfolk, but every spring I trained in horsemanship in a nearby village.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan04 = "I know it as well as any other cityfolk, but every spring I trained in horsemanship in a nearby village."
                    if pc_class == "scholar":
                        $ custom1 = "like that of a soul of books and quills"
                    else:
                        $ custom1 = "like that of a merchant"
                    menu:
                        '“I was just about to ask about it! I couldn’t imagine someone building a stable and a paddock in a place where you can’t squeeze in a single new house. Your accent is very city-like, [custom1].”
                        '
                        '(thais1 preset)':
                            pass
                '“Only for a bit. I was raised in a small village just nearby, and moved to the city after I had decided to look for luck as a roadwarden.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Only for a bit. I was raised in a small village just nearby, and moved to the city after I had decided to look for luck as a roadwarden.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan04 = "I was raised in a small settlement and moved to the city after I had decided to look for luck as a roadwarden."
                    menu:
                        '“To see the city for the first time, after being surrounded by a couple of small houses and fields... It’s a strange feeling, isn’t it?” She puts her hand on the table. “Even after my second winter there I felt like a stranger. But those who know how to live in the countryside, close to the wilderness... We will always find a new home for ourselves, don’t you think?” She gives you an encouraging smile.
                        '
                        '(thais1 preset)':
                            pass
                '“My past is already buried. Let’s not dig into it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My past is already buried. Let’s not dig into it.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan04 = "I don’t like to talk about my past there."
                    menu:
                        'After a few heartbeats, she breaks the awkwardness with a smile. “And what else bothers you in the present?”
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 3: # co jedzą localsi
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“I keep thinking... Surely, cityfolk don’t eat just wild game, salt fish, and groats. What animals do people breed in the nearby villages?”
                '
                '“Mostly ibexes. They do well on the hills.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Mostly ibexes. They do well on the hills.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan05 = 1
                    menu:
                        '“So just like in the old days! I even saw some of them in the city, they are annoyingly good at climbing onto roofs and walls. But more importantly,” she adjusts her dress and smiles, “it means that our mouflon cheese and wool are going to be quite a commodity.”
                        '
                        '(thais1 preset)':
                            pass
                '“There’s a lot of mouflons. The monks need their parchment.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a lot of mouflons. The monks need their parchment.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan05 = 2
                    menu:
                        '“Oh, that’s terrible!” You catch a hint of annoyance in her laughter. “Our livestock won’t sell well! But that’s fine. It’s hard to keep the number of lambs high, we would need to sacrifice a field to raise a new flock.”
                        '
                        '(thais1 preset)':
                            pass
                '“It depends. Mostly pond fish and fowl, but some can afford to buy boars.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends. Mostly fish and fowl, but some can afford to buy boars.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan05 = 3
                    menu:
                        '“Ah, {i}the meat of the tribes{/i}, yet as delicious as any. Our druids say that birds and fish are better for you than pork and mutton, would you believe? Even if they’re right, our {color=#f6d6bd}Creek{/color} has very little life in it, we rarely catch more than two fish a day.”
                        '
                        '(thais1 preset)':
                            pass
                '“There’s barely any meat, so people have started to raise crickets and rats.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s barely any meat, so people have started to raise crickets and rats.”')
                    $ thais_hovlavan05 = 4
                    menu:
                        'She covers her mouth. “I’ve tasted a few rats before, of course, but crickets? How do they taste?”
                        '
                        '“It depends on the way you cook them and what you feed them with.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends on the way you cook them and what you feed them with.”')
                            $ questionpreset = "thais1"
                            menu:
                                '“Purely fascinating. At least now I know that if someone serves me a plate of insects, it’s not an affront,” she titters. “Though I do hope they don’t taste as good as mutton. I’m not going to sell our livestock cheap.”
                                '
                                '(thais1 preset)':
                                    pass
                        '“A bit like nuts, but they’re also ground into a {i}flour{/i}, of sorts. They’re good.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A bit like nuts, but they’re also ground into a {i}flour{/i}, of sorts. They’re good.”')
                            $ questionpreset = "thais1"
                            menu:
                                '“Purely fascinating. At least now I know that if someone serves me a plate of insects, it’s not an affront,” she titters. “Though I do hope they don’t taste as good as mutton. I’m not going to sell our livestock cheap.”
                                '
                                '(thais1 preset)':
                                    pass
                        '“I don’t know. I don’t have a stomach for them. And they look disgusting.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know. I don’t have a stomach for them. And they look disgusting.”')
                            $ questionpreset = "thais1"
                            menu:
                                'She bursts into laughter. “Oh, butchering mouflons also isn’t pretty! I’m more than open to a little adventure. Maybe we should try to cook some on our own.”
                                '
                                '(thais1 preset)':
                                    pass
                '“Whatever people can buy, I guess. I don’t eat animals when I can avoid it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Whatever people can buy, I guess. I don’t eat animals when I can avoid it.”')
                    menu:
                        '“Oh, [pcname]! I believe you, but just indulge me. Listening about the city takes me back to the days when my bones were still strong.”
                        '
                        '“Mostly ibexes. They do well on the hills.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Mostly ibexes. They do well on the hills.”')
                            $ questionpreset = "thais1"
                            $ thais_hovlavan05 = 1
                            menu:
                                '“So just like in the old days! I even saw some of them in the city, they are annoyingly good at climbing onto roofs and walls. But more importantly,” she adjusts her dress and smiles, “it means that our mouflon cheese and wool are going to be quite a commodity.”
                                '
                                '(thais1 preset)':
                                    pass
                        '“There’s a lot of mouflons. The monks need their parchment.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a lot of mouflons. The monks need their parchment.”')
                            $ questionpreset = "thais1"
                            $ thais_hovlavan05 = 2
                            menu:
                                '“Oh, that’s terrible!” You catch a hint of annoyance in her laughter. “Our livestock won’t sell well! But that’s fine. It’s hard to keep the number of lambs high, we would need to sacrifice a field to raise a new flock.”
                                '
                                '(thais1 preset)':
                                    pass
                        '“It depends. Mostly pond fish and fowl, but some can afford to buy boars.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends. Mostly fish and fowl, but some can afford to buy boars.”')
                            $ questionpreset = "thais1"
                            $ thais_hovlavan05 = 3
                            menu:
                                '“Ah, {i}the meat of the tribes{/i}, yet as delicious as any. Our druids say that birds and fish are better for you than pork and mutton, would you believe? Even if they’re right, our {color=#f6d6bd}Creek{/color} has very little life in it, we rarely catch more than two fish a day.”
                                '
                                '(thais1 preset)':
                                    pass
                        '“There’s barely any meat, so people have started to raise crickets and rats.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s barely any meat, so people have started to raise crickets and rats.”')
                            $ thais_hovlavan05 = 4
                            menu:
                                'She covers her mouth. “I’ve tasted a few rats before, of course, but crickets? How do they taste?”
                                '
                                '“It depends on the way you cook them and what you feed them with.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It depends on the way you cook them and what you feed them with.”')
                                    $ questionpreset = "thais1"
                                    menu:
                                        '“Purely fascinating. At least now I know that if someone serves me a plate of insects, it’s not an affront,” she titters. “Though I do hope they don’t taste as good as mutton. I’m not going to sell our livestock cheap.”
                                        '
                                        '(thais1 preset)':
                                            pass
                                '“A bit like nuts, but they’re also ground into a {i}flour{/i}, of sorts. They’re good.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A bit like nuts, but they’re also ground into a {i}flour{/i}, of sorts. They’re good.”')
                                    $ questionpreset = "thais1"
                                    menu:
                                        '“Purely fascinating. At least now I know that if someone serves me a plate of insects, it’s not an affront,” she titters. “Though I do hope they don’t taste as good as mutton. I’m not going to sell our livestock cheap.”
                                        '
                                        '(thais1 preset)':
                                            pass
                                '“I don’t know. I don’t have a stomach for them. And they look disgusting.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know. I don’t have a stomach for them. And they look disgusting.”')
                                    $ questionpreset = "thais1"
                                    menu:
                                        'She bursts into laughter. “Oh, butchering mouflons also isn’t pretty! I’m more than open to a little adventure. Maybe we should try to cook some on our own.”
                                        '
                                        '(thais1 preset)':
                                            pass
        elif thais_about_questions == 4: # "why are you really here"
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                'She leans forward and even though she smiles, her voice is close to a whisper. “I wonder... Why are you here? What pushes someone to becoming a roadwarden?”
                '
                '“I need coin to help someone I care about.”' if pc_goal == "ineedmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need coin to someone I care about.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship += 1
                    menu:
                        '“Quite a burden! Many would turn to thievery, or plots, or blood magic. Your pursuit is... respectable.” She straightens up with an encouraging smile. “{color=#f6d6bd}Hovlavan{/color} is suffocating. All the churches, traders, soldiers, and craft guilds won’t welcome a stranger in need. Still...” she smirks, “better this than being an adventurer.”
                        '
                        '(thais1 preset)':
                            pass
                '“I’ll use the coins to retire early, in prosperity and safety.”' if pc_goal == "iwantmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll use the coins to retire early, in prosperity and safety.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“Ah, the life of white bread and mead! Though even the richest cityfolk invest and work, one way or another. You can’t eat coins,” you catch a hint of mockery in her titter, “and you need more than a lock to protect yourself from envy and greed.” For a moment, she observes your palfrey. “Maybe move to a village? It’s easier to keep thieves away.”
                        '
                        '(thais1 preset)':
                            pass
                '“I need to build connections with the local leaders. I’ll be a new player in the merchant guild.”' if pc_goal == "iwantstatus":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to build connections with the local leaders. I’ll be a new player in the merchant guild.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship += 1
                    menu:
                        'She gives you a wide, white grin. “A {i}healthy{/i} ambition, and a lovely one! With my weak bones, I couldn’t be a fighter, but with a few investments I sculpted a place for myself. If you want some advice from me,” she looks around, “remember your friends. Allies can carry you further than the heaviest pouch.” As she moves away, you once again notice the expensive rouge on her cheeks.
                        '
                        '(thais1 preset)':
                            pass
                '“I want to be remembered as the one who brought peace and order to this realm.”' if pc_goal == "iwanttoberemembered":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to be remembered as the one who brought peace and order to this realm.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“Such hubris!” You notice doubt in her brief laughter. “To think this place needs one’s touch, and even more so yours! I can’t {i}wait{/i} to see if you’re a soul led by a vision, or arrogance.”
                        '
                        '(thais1 preset)':
                            pass
                '“I just want to help people. If I can make this area safer, I’m going to do it.”' if pc_goal == "iwanttohelp":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just want to help people. If I can make this area safer, I’m going to do it.”')
                    $ questionpreset = "thais1"
                    menu:
                        'She waits, expecting that there’s more to be said, then lets out a nervous chuckle. “Forgive me, it’s something I mostly hear from children, not travelers.” She observes you with keen eyes, but after another few breaths, shrugs her doubts off. “What else do you need?”
                        '
                        '(thais1 preset)':
                            pass
                '“A new life, that’s all I need. It doesn’t matter why.”' if pc_goal == "iwanttostartanewlife":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A new life, that’s all I need. It doesn’t matter why.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“So mysterious! But I understand. So you’re more of an adventurer than a soldier. I’d say it’s going to suit you well in the peninsula. One needs to know how to... Improvise.” There’s something uneasy about her smile.
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “I need coin to help a friend I care about.”' if pc_goal != "ineedmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I need coin to help a friend I care about.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship += 1
                    $ pc_lies += 1
                    menu:
                        '“Quite a burden! Many would turn to thievery, or plots, or blood magic. Your pursuit is... respectable.” She straightens up with an encouraging smile. “{color=#f6d6bd}Hovlavan{/color} is suffocating. All the churches, traders, soldiers, and craft guilds won’t welcome a stranger in need. Still...” she smirks, “better this than being an adventurer.”
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “I’ll use the coins to retire early, in prosperity and safety.”' if pc_goal != "iwantmoney":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’ll use the coins to retire early, in prosperity and safety.”')
                    $ questionpreset = "thais1"
                    $ pc_lies += 1
                    menu:
                        '“Ah, the life of white bread and mead! Though even the richest cityfolk invest and work, one way or another. You can’t eat coins,” you catch a hint of mockery in her titter, “and you need more than a lock to protect yourself from envy and greed.” For a moment, she observes your palfrey. “Maybe move to a village? It’s easier to keep thieves away.”
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “I need to build connections with the local leaders. I’ll be a new player in the merchant guild.”' if pc_goal != "iwantstatus":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I need to build connections with the local leaders. I’ll be a new player in the merchant guild.”')
                    $ questionpreset = "thais1"
                    $ pc_lies += 1
                    $ thais_friendship += 1
                    menu:
                        'She gives you a wide, white grin. “A {i}healthy{/i} ambition, and a lovely one! With my weak bones, I couldn’t be a fighter, but with a few investments I sculpted a place for myself. If you want some advice from me,” she looks around, “remember your friends. Allies can carry you further than the heaviest pouch.” As she moves away, you once again notice the expensive rouge on her cheeks.
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “I want to be remembered as the one who brought peace and order to this realm.”' if pc_goal != "iwanttoberemembered":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I want to be remembered as the one who brought peace and order to this realm.”')
                    $ questionpreset = "thais1"
                    $ pc_lies += 1
                    menu:
                        '“Such hubris!” You notice doubt in her brief laughter. “To think this place needs one’s touch, and even more so yours! I can’t {i}wait{/i} to see if you’re a soul led by a vision, or arrogance.”
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “I just want to help people. If I can make this area safer, I’m going to do it.”' if pc_goal != "iwanttohelp":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I just want to help people. If I can make this area safer, I’m going to do it.”')
                    $ questionpreset = "thais1"
                    $ pc_lies += 1
                    menu:
                        'She waits, expecting that there’s more to be said, then lets out a nervous chuckle. “Forgive me, it’s something I mostly hear from children, not travelers.” She observes you with keen eyes, but after another few breaths, shrugs her doubts off. “What else do you need?”
                        '
                        '(thais1 preset)':
                            pass
                '(lie) “A new life, that’s all I need. It doesn’t matter why.”' if pc_goal != "iwanttostartanewlife":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “A new life, that’s all I need. It doesn’t matter why.”')
                    $ pc_lies += 1
                    $ questionpreset = "thais1"
                    menu:
                        '“So mysterious! But I understand. So you’re more of an adventurer, than a soldier. I’d say it’s going to suit you well in the peninsula. One needs to know how to... Improvise.” There’s something uneasy about her smile.
                        '
                        '(thais1 preset)':
                            pass
                '“That’s for me to know. My motivations are of no importance.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s for me to know. My motivations are of no importance.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship -= 1
                    menu:
                        '“So mysterious! And rude!” While she laughs, her hand clenches around her buckle. “As you wish, dear roadwarden. Do you need anything else?”
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 5 and not thais_hovlavan06: # role of a church
            $ minutes += 5
            $ thais_about_questions = 6
            menu:
                '“You surely don’t avoid hard conversations, do you? Most cityfolk feel hesitant when they meet... {i}pagans{/i}.” She smirks, but the hand clenched around her deer-buckle makes you alert. “Are you that open to strangers, or did The United Church loosen its grasp? I’m interested in who could take their place. The guilds and artisans? The army?”
                '
                'I don’t like her assumptions. “I {i}don’t{/i} enjoy spending time with pagans, but I’m willing to look past our differences.”' if pc_religion != "pagan" and pc_religion != "none":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='-I don’t like her assumptions. “I {i}don’t{/i} enjoy spending time with pagans, but I’m willing to look past our differences.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship -= 1
                    $ howlersdell_reputation -= 1
                    $ thais_about_pagans_pcenemy = 1
                    $ thais_hovlavan06 = 1
                    menu:
                        'Her eyes shift from keen to angry. After a moment, she relaxes her shoulders, but also crosses her arms. “Are we done here?”
                        '
                        '(thais1 preset)':
                            pass
                '“The United Church stands strong, and so do its laws. {color=#f6d6bd}Hovlavan{/color} is still loyal to the Empress, even if she’s not around.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The United Church stands strong, and so do its laws. {color=#f6d6bd}Hovlavan{/color} is still loyal to the Empress, even if she’s not around.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan06 = 2
                    menu:
                        '“Well, that’s hardly good news, is it? Signing a deal with {color=#f6d6bd}Hovlavan{/color} will bring their {i}sacred{/i} butchers here, ready to {i}teach us{/i} how to change our path.” She sighs, but with clear exaggeration. “Emperors or not, their priests don’t take {i}no{/i} for an answer.”
                        '
                        '(thais1 preset)':
                            pass
                '“The Unites are matched by the new order of Seekers, but nothing is set in stone yet.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The Unites are matched by the new order of Seekers, but nothing is set in stone yet.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan06 = 3
                    menu:
                        '“Perfect! Let’s hope it’s going to last for a decade or so. We don’t need their preachers here, nor the blood they are so happy to shed.”
                        '
                        '(thais1 preset)':
                            pass
                '“Soon after the war, the army had to take over, and never let go of its power.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Soon after the war, the army had to take over, and never let go of its power.”')
                    $ questionpreset = "thais1"
                    $ iason_name = "Iason"
                    if peltnorth_firsttime:
                        $ custom1 = "She’s pretty good at mimicking his voice."
                    else:
                        $ custom1 = "Her voice shifts, as if to mimic someone."
                    $ thais_hovlavan06 = 4
                    menu:
                        '“How the times have changed,” she says with wide open eyes. “It used to be a custom to gather the chief and commanders with every new year, then order them to pledge their allegiance to the Church,” she adjusts her cape. “I remember what {color=#f6d6bd}Iason{/color} from {color=#f6d6bd}Pelt of the North{/color} used to say. {i}The war never ended{/i}.” [custom1]
                        '
                        '(thais1 preset)':
                            pass
                '“The maritime trade keeps the city alive. The merchants took the lead.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The maritime trade keeps the city alive. The merchants took the lead.”')
                    $ questionpreset = "thais1"
                    $ thais_hovlavan06 = 5
                    menu:
                        '“The roads might turn wild, but the sea won’t ever sate its hunger for ships. People who lost everything are more likely to risk it all.” She still smiles, but her eyes are melancholic. “When the world shakes, it’s also time to change the old order. Maybe it’s the only time.”
                        '
                        '(thais1 preset)':
                            pass
                '“Honestly? I don’t bother with politics.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Honestly? I don’t bother with politics.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship -= 1
                    $ thais_hovlavan06 = 6
                    menu:
                        'Her eyes turn from keen to angry, then again to tranquil, though her voice is tart. “Are we done here?”
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 6: # she often talks with others
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“Can you give us a moment?” As you frown, a muscular, crudely dressed woman approaches the table, asking {color=#f6d6bd}Thais{/color} for directions - something about moist logs and breaking boards.
                \n\nYou stop paying attention quickly, and instead wonder why {color=#f6d6bd}the mayor{/color} insists on holding these meetings outside.
                '
                'She’s so busy she needs to be constantly available to the others.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- She’s so busy she needs to be constantly available to the others.')
                    $ questionpreset = "thais1"
                    menu:
                        '“Great job,” she sends off the worker with an encouraging smile, though when her eyes meet yours, you notice her tired sigh.
                        '
                        '(thais1 preset)':
                            pass
                'I’m neither a threat, nor someone important enough to be worthy of her exclusive time.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m neither a threat, nor someone important enough to be worthy of her exclusive time.')
                    $ questionpreset = "thais1"
                    menu:
                        '“Great job,” she sends off the worker with an encouraging smile, though when her eyes meet yours, you catch a hint of contempt.
                        '
                        '(thais1 preset)':
                            pass
                'It’s all theater. She wants to show how much she cares about the others.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s all theater. She wants to show how much she cares about the others.')
                    $ questionpreset = "thais1"
                    menu:
                        '“Great job,” she sends off the worker with an encouraging smile, though when her eyes meet yours, it shifts into a challenging smirk.
                        '
                        '(thais1 preset)':
                            pass
                'It would be inappropriate for a married person to spend this much time with an outsider away from everyone’s eyes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be inappropriate for a married person to spend this much time with an outsider away from everyone’s eyes.')
                    $ questionpreset = "thais1"
                    menu:
                        '“Great job,” she sends off the worker with an encouraging smile, though when her eyes meet yours, there’s something playful to it.
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 7: # pytanie o rodzinę
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '{color=#f6d6bd}Eryx{/color} shows up with a plate of red radishes, salted, roasted, and cut into slices. He invites you both to help yourselves, but before he leaves, {color=#f6d6bd}Thais{/color} grabs his hand and looks into his eyes. They smile at each other, without a word.
                \n\nAfter a few heartbeats, she turns back toward you. “I don’t really know your plans, [pcname]. Are you planning to stay in the North? Maybe find a family?”
                '
                '“I already have a family. And they need me back home.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I already have a family. And they need me back home.”')
                    $ pc_futureplans = "stayincity"
                    $ pc_hasfamily = 1
                    $ questionpreset = "thais1"
                    menu:
                        '“Oh, I see,” her smile is as encouraging as her voice. “Leaving behind those dear to you would be cowardice,” {color=#f6d6bd}her husband{/color} chips in, then walks away.
                        '
                        '(thais1 preset)':
                            pass
                '“I’m not looking for a new place. I want to travel.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not looking for a new place. I want to travel.”')
                    $ questionpreset = "thais1"
                    $ pc_futureplans = "travel"
                    menu:
                        '“{i}Living life to its fullest{/i}, aye?” {color=#f6d6bd}the innkeep{/color} smiles, and {color=#f6d6bd}his wife{/color} chuckles. “That’s {i}not{/i} for me, I never understood the wandering souls, unless they hope to {i}find{/i} a goal.”
                        \n\n{color=#f6d6bd}Eryx{/color} pats her shoulders. “She always knows what to pursue. Her heart’s too strong to doubt.”
                        \n\n“{i}You{/i} are my heart,” she holds in her laughter as she kisses his hand, and the man gives her a radiant smile, then walks back to the inn.
                        '
                        '(thais1 preset)':
                            pass
                '“I’ll start a new life in {color=#f6d6bd}Hovlavan{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll start a new life in {color=#f6d6bd}Hovlavan{/color}.”')
                    $ questionpreset = "thais1"
                    $ pc_futureplans = "stayincity"
                    menu:
                        '“Oh, I do see the appeal of living behind thick walls, but for me, living so close to the woods is just so...” as she hesitates, {color=#f6d6bd}Eryx{/color} chips in. “Honest?”
                        \n\nYou notice her confused glance, as if she’s having second thoughts. Her voice lacks conviction. “Yes! Knowing my neighbors, eating the plants we grow, being a part of the woods, not its enemy.” {color=#f6d6bd}Her husband{/color} nods in approval. “Cities are airless. Unnatural.” He pats her shoulder, nods toward you, and heads back to the inn. {color=#f6d6bd}Thais’{/color} hand is twisting her buckle.
                        '
                        '(thais1 preset)':
                            pass
                '“Yes, actually. I think I’ll look for a new home here.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes, actually. I think I’ll look for a new home here.”')
                    $ questionpreset = "thais1"
                    $ pc_futureplans = "liveinpeninsula"
                    if howlersdell_reputation > 8 and (thais_friendship+appearance_charisma) > 8:
                        menu:
                            'Both of them observe you with warm smiles, as if they’re posing for a painter. “Maybe we’ll find a free corner somewhere after winter,” {color=#f6d6bd}the innkeep{/color} starts, and {color=#f6d6bd}his wife{/color} interrupts him with a titter. “We’ll see, we’ll see. Let’s take care of some more {i}pressing{/i} issues first.”
                            \n\nHe gives her a surprised glance, but then nods toward you, and heads back to the inn.
                            '
                            '(thais1 preset)':
                                pass
                    else:
                        menu:
                            '{color=#f6d6bd}The innkeep{/color} nods politely. “The peninsula could use a regular warden...” Before he finishes his thought, {color=#f6d6bd}his wife{/color} chips in. “Too bad we can’t really squeeze a new house into our village. But I’m sure you’ll find plenty of empty huts in the North.”
                            \n\nHe gives her a surprised glance, but then nods toward you, and heads back to the inn. {color=#f6d6bd}Thais{/color} gives you a polite smile.
                            '
                            '(thais1 preset)':
                                pass
                '“Maybe, maybe.” I smile politely.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe, maybe.” I smile politely.')
                    $ questionpreset = "thais1"
                    menu:
                        'She frowns slightly, and it’s {color=#f6d6bd}the innkeep{/color} who speaks first. “The peninsula could use a regular warden. Especially one who’s ne lazy.” His wife squeezes his hand gently, and soon after he leaves the two of you alone. Her gaze is rather absent.
                        '
                        '(thais1 preset)':
                            pass
                'I look at her sternly. “You don’t need to know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at her sternly. “You don’t need to know.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship -= 2
                    menu:
                        'They both stare at you in silence, until {color=#f6d6bd}the surprised innkeep{/color} pats his wife’s shoulder, and she tells him that “‘tis alright.” While he gives you an angry glance, he obediently heads back to the inn.
                        '
                        '(thais1 preset)':
                            pass
        elif thais_about_questions == 8: # What future do you see for the peninsula?
            $ minutes += 5
            $ thais_about_questions += 1
            menu:
                '“Here’s a silly question, [pcname]. What future do you see for the peninsula? Imagine being {i}the chieftain of the North{/i}. What would be your order?”
                '
                '“Under my command, the settlements would join The Ten Cities. Standing aloof puts the locals in danger.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Under my command, the settlements would join The Ten Cities. Standing aloof puts the locals in danger.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“I expected this of you,” she smiles. “And yes, I’d also consider it. But having soldiers, priests, and bards among our walls is like inviting dragons. They wound tribes with intrigues and poisonous thoughts,” she grabs her deer-buckle, “and that may be even worse for us than fire.”
                        '
                        '(thais1 preset)':
                            pass
                '“I’d focus on creating a trade route with the guild, without joining The Cities.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d focus on creating a trade route with the guild, without joining The Cities.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“A compromise, then,” she gives you a habitual smile. “But the city’s attempts would never, ever end, not while we have anything they want. And yes, I’m ready to play their game, but are the other settlements? Will the next mayor of {color=#f6d6bd}Howler’s{/color} be able to handle this? If I sign a deal that pushes our children into chains twenty years from now, will I be responsible?” She looks at a nearby group that’s practicing a local song.
                        '
                        '(thais1 preset)':
                            pass
                '“Working with The Ten Cities will take away your freedom. If it were my call alone, I’d send the news to cut the negotiations.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Joining The Ten Cities will take away your freedom. If it were my call alone, I would send the news to cut the negotiations.”')
                    $ questionpreset = "thais1"
                    menu:
                        '“It’s... {i}not{/i} what I expected to hear from a guild’s delegate,” she chuckles. “I must admit, you’ve managed to baffle me. But still... Keeping our distance for so long may be dangerous. Today, we’re strong, but if there’s one thing that the war has taught us, it’s that no place is {i}too{/i} great to fall.”
                        '
                        '(thais1 preset)':
                            pass
                '“The settlements should work together, share their goals to make this place safer. Maybe start a new village.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The settlements should work together, share their goals to make this place safer. Maybe start a new village.”')
                    $ questionpreset = "thais1"
                    menu:
                        'You find sadness in her eyes. “I had similar hopes, but there’s too much bad blood between us. It makes us weak,” she looks toward the creek, “but it would take a soul of great charisma to bury our discords.”
                        '
                        '(thais1 preset)':
                            pass
                '“I’d never dare to make such a call. Every community has the right to govern themselves.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d never dare to make such a call. Every community has the right to govern themselves.”')
                    $ questionpreset = "thais1"
                    $ thais_friendship += 1
                    menu:
                        'For a few heartbeats, she closes her eyes. “You {i}do{/i} understand our ways.” When your eyes meet again, she’s both less cheerful, and more relaxed. “But I’m sure that {color=#f6d6bd}Hovlavan{/color} thinks the exact opposite. Tribes should have the right to leave the city whenever they wish to do so, and we both know,” she nods toward you again, “that the officials are far from willing to let go of what they’ve once grasped.”
                        '
                        '(thais1 preset)':
                            pass
        # elif thais_about_questions == 9:
        #     $ minutes += 5
        #     $ thais_about_questions += 1
        #     menu:
        #         '
        #         \n\n
        #         '
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             $ questionpreset = "thais1"
        #             menu:
        #                 '“”
        #                 '
        #                 '(thais1 preset)':
        #                     pass
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             $ questionpreset = "thais1"
        #             menu:
        #                 '“”
        #                 '
        #                 '(thais1 preset)':
        #                     pass
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             $ questionpreset = "thais1"
        #             menu:
        #                 '“”
        #                 '
        #                 '(thais1 preset)':
        #                     pass
        #         '':
        #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
        #             $ questionpreset = "thais1"
        #             menu:
        #                 '“”
        #                 '
        #                 '(thais1 preset)':
        #                     pass
        else:
            label howlersdellthaisafterquestionsALL:
                if thais_bigmad:
                    jump howlersdellthaisafterquestionsBIGMAD
                $ questionpreset = "thais1"
                $ custom1 = renpy.random.choice(['“Do you need anything else?”', 'She smiles widely.', '“Can I help you with anything?”', 'She lets out a chuckle.', '“Go ahead.”'])
                menu:
                    '[custom1]
                    '
                    '(thais1 preset)':
                        pass

    label howlersdellthaisafterquestionsALL2:
        $ questionpreset = "thais1"
        menu:
            '“Fantastic,” she says with a radiant smile. Her hand is as soft as that of a wealthy merchant. “Do you need anything else?”
            '
            '(thais1 preset)':
                pass

    label howlersdellthaisafterquestionsALL3:
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
            '[custom1]
            '
            '(thais1 preset)':
                pass

label howlersdellleavingthais01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for your time.”')
    $ questionpreset = 0
    if (thais_friendship+howlersdell_reputation) >= 30 and not howlersdell_food_free and quest_fisherhamlet == 2:
        $ howlersdell_food_free = 1
        menu:
            'She also stands up. “Once you have a moment, talk with {color=#f6d6bd}Akakios{/color}. He has something for you. A small token of our appreciation.”
            '
            'I nod and walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and walk away.')
                jump howlersdellsquaafterinteraction01
            '“And what am I appreciated {i}for{/i}, if I may ask?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what am I appreciated {i}for{/i}, if I may ask?”')
                menu:
                    'Her face brightens up and as she bows to you, holding her cape, her voice is playful. “For being a kind part of our recent days, [pcname]. It’s just a sign of... What would you like to call it?” She straightens up and looks into your eyes. “Alliance, maybe?”
                    '
                    '“Sounds about right... My ally.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds about right... My ally.”')
                        $ howlersdell_reputation_status = "ally"
                        menu:
                            'Her eyes narrow in approval. “Safe travels. You’re always welcome here.”
                            '
                            'I walk away.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                                jump howlersdellsquaafterinteraction01
                    '“{i}A token of friendship{/i} has a better ring to it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}A token of friendship{/i} has a better ring to it.”')
                        $ howlersdell_reputation_status = "friend"
                        menu:
                            'She bursts into laughter. “Yet our village has no friends, so how could it be!” She rubs her chin and looks at the sky. “Today, it has at least one. And you’re always welcome here.”
                            \n\nShe reaches for your hand, squeezes it, and walks away, toward a daughter of hers who’s fixing a broken chair.
                            '
                            'I turn away.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn away.')
                                jump howlersdellsquaafterinteraction01
                    '“No matter what you call it, I’m just doing my job.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No matter how you call it, I’m just doing my job.”')
                        menu:
                            'She bursts into a laughter and sends you off with a wave of her hand, then heads back to the inn.
                            '
                            'I turn away.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn away.')
                                jump howlersdellsquaafterinteraction01
    else:
        jump howlersdellsquaafterinteraction01

    label howlersdellleavingthais02:
        jump howlersdellsquaafterinteraction01

label howlersdellquestionsasterionALL:
    label howlersdellquestionsasterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}.”')
        $ thais_about_asterion = 1
        if thais_about_daughter_learned == 1:
            $ thais_about_asterionc = 1
            $ elah_about_asterion_friendship += 1
            $ quest_asterion_description05b = "She believes I should look for him in the northern villages."
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
            $ minutes += 2
            $ questionpreset = "thais1"
            menu:
                'She stares at you in silence, reaching for her buckle. “I’m not the one you should ask. I blamed {i}him{/i} for {color=#f6d6bd}Aegidia’s{/color} disappearance, but...” She pauses again, tapping her fingers against the deer’s head. “He’s still a liar, a trickster of a spirit. While he’s not welcome here, I’m ready to hear his apologies, if you can find him.”
                \n\nShe leans away. “Try asking for him in the North. He spent most of his time between {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}. Here, he wasn’t that eager to share his plans.”
                '
                '(thais1 preset)':
                    pass
        $ questionpreset = 0
        menu:
            'She stares you in the eyes, then turns toward {color=#f6d6bd}[horsename]{/color}. “Is your palfrey a mare? We have two jacks, could use some mules.”
            '
            '“A stallion, so it won’t give you anything stronger than a hinny.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A stallion, so it won’t give you anything stronger than a hinny.”')
                menu:
                    '“So I’ve heard...” her eyes wander over the square. “That the small donkey bellies bring weak offspring to horses.” Her pale fingers reach for her own stomach.
                    \n\nWhen her eyes return to you, they regain their sharpness. “I’d rather avoid long talks about that man, let him remain as a part of the past spring. Since you’re asking about him, I can only assume he was indeed sharing his goal with yours.”
                    '
                    '“I won’t deny that.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t deny that.”')
                        $ thais_friendship += 1
                        jump howlersdellquestionsasterion01c
                    '(lie) “I know nothing about it. I’ll get paid for finding him, that’s all.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I know nothing about it. I’ll get paid for finding him, that’s all.”')
                        $ pc_lies += 1
                        jump howlersdellquestionsasterion01d
            '“It is, but I need it to stay strong and healthy.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It is, but I need it to stay strong and healthy.”')
                menu:
                    '“Right, there’s no time for the romances of draught animals. It would take almost a year, correct? It was all just a thought.”
                    \n\nWhen her eyes return to you, they regain their sharpness. “I’d rather avoid long talks about that man, let him remain as a part of the past spring. Since you’re asking about him, I can only assume he was indeed sharing his goal with yours.”
                    '
                    '“I won’t deny that.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t deny that.”')
                        $ thais_friendship += 1
                        jump howlersdellquestionsasterion01c
                    '(lie) “I know nothing about it. I’ll get paid for finding him, that’s all.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I know nothing about it. I’ll get paid for finding him, that’s all.”')
                        $ pc_lies += 1
                        jump howlersdellquestionsasterion01d
            '“I’m looking for {color=#f6d6bd}Asterion{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}.”')
                $ thais_friendship -= 1
                jump howlersdellquestionsasterion02

    label howlersdellquestionsasterion01c:
        menu:
            '“Yet you’re already different from him. I like it when travelers don’t try to sell me blue grass.” Seeing your frown, she waves it off. “It’s just a saying. His words were stronger than his deeds. And he’s no longer welcome here.”
            '
            '“What are his wrongdoings?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are his wrongdoings?”')
                jump howlersdellquestionsasterion03

    label howlersdellquestionsasterion01d:
        menu:
            'You sit without a word, listening to the creek, until she sighs exaggeratedly. “Why are you doing this to me, traveler? Now I have to figure out if you’re lying, or simply wrong. But back to your question.” She takes a deep breath.
            \n\n“{color=#f6d6bd}Asterion{/color} is not welcome here, and I don’t know where he went.”
            '
            '“What are his wrongdoings?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are his wrongdoings?”')
                jump howlersdellquestionsasterion03

    label howlersdellquestionsasterion02:
        menu:
            '“I {i}heard{/i} you, but he’s not welcome here,” her voice is harsh, “and I don’t know where he went. We haven’t burned him, or fought his awoken shell. Wherever he is,” a long pause, “it’s not {i}our{/i} problem.”
            '
            '“What are his wrongdoings?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are his wrongdoings?”')
                jump howlersdellquestionsasterion03

    label howlersdellquestionsasterion03:
        $ quest_asterion_description05 = "According to {color=#f6d6bd}Thais{/color}, {color=#f6d6bd}Howler’s Dell{/color} has banished Asterion as a result of his failed mission."
        $ renpy.notify("Journal updated: Find the Roadwarden")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        $ description_aegidia02 = "According to {color=#f6d6bd}Thais{/color}, she died during an accident that involved {color=#f6d6bd}Asterion{/color}."
        $ minutes += 5
        menu:
            '“If you {i}have to{/i} know, he failed, and won’t get a second chance. He was meant to escort {color=#f6d6bd}Aegidia{/color}, a daughter of mine, to her betrothed in {color=#f6d6bd}Gale Rocks{/color}. She was a great archeress, and the road from here to the coast is not {i}that{/i} dangerous. When they saw goblins on the road, {color=#f6d6bd}Asterion{/color} ordered her to push through. Right into their trap.”
            \n\nShe touches her deer-shaped buckle. “They got jumped like a bunch of wealthy pilgrims. A {i}roadwarden{/i} worth their gruel should know better. He can fight with a blade, but my girl? She never had a chance.”
            \n\nShe sighs and looks at the gate. “He disappeared soon after his pitiful attempt at apologizing to me, and we closed our doors behind him - for good. I’ll let you know if he ever tries to return.”
            '
            '“Any ideas where I can look for him?”' if not thais_about_asterionc:
                jump howlersdellquestionsasterion06
            '“Why did you let him leave?”' if not thais_about_asteriona:
                jump howlersdellquestionsasterion04
            '“Did you ever find your daughter?”' if not thais_about_asterionb:
                jump howlersdellquestionsasterion05
            '“You have quite a big family.”' if thais_about_asterionb == 1 and not thais_about_asteriond:
                jump howlersdellquestionsasterion05b
            '“Thanks for the help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the help.”')
                jump howlersdellthaisafterquestions

    label howlersdellquestionsasterion04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why did you let him leave?”')
        $ description_asterion07 = "If {color=#f6d6bd}Thais{/color} speaks the truth, {color=#f6d6bd}Asterion{/color} was ready to face the consequences of his wrongdoings."
        $ thais_about_asteriona = 1
        $ minutes += 2
        menu:
            '“He didn’t do anything, well, {i}forbidden{/i} by our laws. He was simply stupid, and cannot be trusted, but this isn’t {color=#f6d6bd}Hovlavan{/color}. We have no rich folk to dread. We treat each other fairly.”
            \n\nLost in her thoughts, she rubs the neckline of her dress. “One good thing I can say about him is that he didn’t try to justify his decisions, or to avoid the consequences. But I’d rather have him prove first he can do what’s asked of him.”
            '
            '“Any ideas where I can look for him?”' if not thais_about_asterionc:
                jump howlersdellquestionsasterion06
            '“Why did you let him leave?”' if not thais_about_asteriona:
                jump howlersdellquestionsasterion04
            '“Did you ever find your daughter?”' if not thais_about_asterionb:
                jump howlersdellquestionsasterion05
            '“You have quite a big family.”' if thais_about_asterionb == 1 and not thais_about_asteriond:
                jump howlersdellquestionsasterion05b
            '“Thanks for the help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the help.”')
                jump howlersdellthaisafterquestions

    label howlersdellquestionsasterion05:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you ever find your daughter?”')
        $ thais_about_asterionb = 1
        $ description_aegidia04 = "According to {color=#f6d6bd}Thais{/color}, she “listened to people, was ready to help them and to cry with them.”"
        $ minutes += 2
        menu:
            'For a few breaths, her green eyes seek something in your face. Her words are careful, yet hesitant. “She’s with the fogs now. The goblins were after food, so they carried her shell away. One day she’s going to charge at our walls, awoken and empty. Even though she was a bit... mawkish, her heart was strong, and patient. She listened to people, was ready to help them and to cry with them. I could tell you stories, but what for? Let the dead rest.”
            '
            '“Any ideas where I can look for him?”' if not thais_about_asterionc:
                jump howlersdellquestionsasterion06
            '“Why did you let him leave?”' if not thais_about_asteriona:
                jump howlersdellquestionsasterion04
            '“Did you ever find your daughter?”' if not thais_about_asterionb:
                jump howlersdellquestionsasterion05
            '“You have quite a big family.”' if thais_about_asterionb == 1 and not thais_about_asteriond:
                jump howlersdellquestionsasterion05b
            '“Thanks for the help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the help.”')
                jump howlersdellthaisafterquestions

    label howlersdellquestionsasterion05b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You have quite a big family.”')
        $ thais_about_asterionb = 2
        $ thais_about_asteriond = 1
        $ minutes += 2
        $ description_howlersdell02 = "It’s customary for the village mayor to look after the village orphans."
        menu:
            'She titters weakly. “At one point, there were twelve kids living in our house. Nine girls, three boys. They come and go, as it should be. A few are already with the forest, but most are all grown now, even started their own families.”
            \n\nShe looks away, at a girl wiping spilled milk with a wet cloth. “To be perfectly clear, they aren’t exactly {i}our{/i} children. It’s a custom of our village for the mayor to look after the orphans. Thankfully, {color=#f6d6bd}Eryx{/color} has a big heart, and much more patience than I do.” As she speaks, her smile widens.
            '
            '“Any ideas where I can look for him?”' if not thais_about_asterionc:
                jump howlersdellquestionsasterion06
            '“Why did you let him leave?”' if not thais_about_asteriona:
                jump howlersdellquestionsasterion04
            '“Did you ever find your daughter?”' if not thais_about_asterionb:
                jump howlersdellquestionsasterion05
            '“You have quite a big family.”' if thais_about_asterionb == 1 and not thais_about_asteriond:
                jump howlersdellquestionsasterion05b
            '“Thanks for the help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the help.”')
                jump howlersdellthaisafterquestions

    label howlersdellquestionsasterion06:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any ideas where I can look for him?”')
        $ thais_about_asterionc = 1
        $ elah_about_asterion_friendship += 1
        $ quest_asterion_description05b = "She believes I should look for him in the northern villages."
        $ renpy.notify("Journal updated: Find the Roadwarden")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        $ minutes += 2
        menu:
            'She adjusts her cape with an annoyed shrug. “Try asking for him in the North. He spent most of his time between {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}. Here, he wasn’t that eager to share his plans.”
            '
            '“Any ideas where I can look for him?”' if not thais_about_asterionc:
                jump howlersdellquestionsasterion06
            '“Why did you let him leave?”' if not thais_about_asteriona:
                jump howlersdellquestionsasterion04
            '“Did you ever find your daughter?”' if not thais_about_asterionb:
                jump howlersdellquestionsasterion05
            '“You have quite a big family.”' if thais_about_asterionb == 1 and not thais_about_asteriond:
                jump howlersdellquestionsasterion05b
            '“Thanks for the help.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the help.”')
                jump howlersdellthaisafterquestions

label howlersdellquestionsfoundasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
    $ thais_about_foundasterion = 1
    $ howlersdell_reputation += 1
    $ minutes += 5
    $ questionpreset = "thais1"
    menu:
        'You describe the island and the cave, but before you mention the roadwarden’s shell, she leans away and sighs. “Leave this to the bards. Is he dead, or not?” After your one-word response, she waves it off. “Very well. I’ll tell the others.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionssteephouse_fail01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was in the ruined village, south from here...”')
    $ thais_about_steephouse_fail = 1
    $ minutes += 1
    $ questionpreset = "thais1"
    menu:
        'Her tense gaze shifts into an awkward click of her tongue as she leans away from you. “I don’t even want to {i}think{/i} about their tragic fate. No one can negotiate with the wrath of the herds.” A long pause. “And I better not find you upsetting my neighbors with these sad questions. It was a challenging time for all of us, a wound we won’t forget.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsjoiningthecityALL:
    label howlersdellquestionsjoiningthecity01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would it take to make you consider joining {color=#f6d6bd}Hovlavan{/color}?”')
        $ thais_about_joiningthecity = 1
        $ questionpreset = 0
        menu:
            '“Ah, I can {i}consider{/i} it right now!” While she laughs, her eyes remain keen. “But if you want me to give you some answers, let’s see...” She looks up and to the right, theatrically raising her hand to her chin. “Some {i}gestures of goodwill{/i} would be a great start. Since you’re the guild’s messenger, I need to know you can be relied on.” She gives you a wide, white grin.
            '
            '“And that’s only the first step, I assume?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And that’s only the first step, I assume?”')
                $ quest_howlerssupport = 1
                $ renpy.notify("New entry: The Support of Howler’s Dell")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Howler’s Dell{/i}')
                menu:
                    '“Of course! Do you even have the power to handle tax negotiations?” She scoffs loudly at your head shake. “Do enough for my village and I’ll hand you a beautiful, signed letter. A list of all the things my neighbors are looking for, as well as what they can give in return. Your superiors are going to see more than enough to prepare their offer.”
                    \n\nShe rubs her hands. “I think that’s fair.”
                    '
                    '“Yeah. Looks like we’re in agreement.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah. Looks like we’re in agreement.”')
                        jump howlersdellquestionsjoiningthecity02a
                    '“{i}Do enough for my village{/i} is a bit vague.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Do enough for my village{/i} is a bit vague.”')
                        menu:
                            'She nods toward the people gathered by the tables. “I’m not the ruler of this place. My friends trust me because I see things as they are, and am willing to act. Prove that you’re helpful and they’ll be happy to match your efforts. I {i}want{/i} you to succeed,” she puts her hand on her chest, “but we don’t give strangers more than we can get from them. If you want me to argue in your favor, show us your worth.”
                            '
                            '“...Looks like we’re in agreement.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Looks like we’re in agreement.”')
                                jump howlersdellquestionsjoiningthecity02a

    label howlersdellquestionsjoiningthecity02a:
        if not howlersdell_mundanework_available:
            $ howlersdell_mundanework_available = 1
            $ renpy.notify("New mundane jobs available in the village.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New mundane jobs available in the village.{/i}')
        menu:
            '“Perfect! One more thing, though,” she puts her elbows on the table, leaning closer to you. “If you go behind my back, I’m not going to wait for a dagger. I’ll end you first.”
            \n\nShe rests her chin against her open palms, giving you a disarmingly warm smile. “I’m sure people already know that we have a {i}new{/i} roadwarden. Maybe ask around to see if anyone needs your help. The more my neighbors trust you and need you, the more willing they’ll be to offer you better pay.”
            '
            '“Well, let’s start here. What can I do for you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, let’s start here. What can I do for you?”')
                $ quest_howlerssupport_description01 = "{color=#f6d6bd}Thais{/color} wants me to spy for her."
                $ renpy.notify("Journal updated: The Support of Howler’s Dell")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Support of Howler’s Dell{/i}')
                menu:
                    '“Aw, so kind of you to ask! But before I ask you to run, let’s see how you can walk, shall we?”
                    \n\nHer eyes wander left and right, and she gestures for a nearby guard to move away. He nods, then gestures at a few other souls to follow him. While a few of the locals cast curious looks at you, they turn away as quickly as you notice them.
                    \n\n{color=#f6d6bd}The mayor’s{/color} shiny green eyes are still locked on you, and her voice is close to a whisper. “Since {color=#f6d6bd}Asterion’s{/color} disappearance, there’s little trade on the roads, and not much news reaches us. {i}Be so kind{/i},” her flirtatious tone distracts you with how obviously fake it is, “and help me learn some interesting {i}tales{/i} about our neighbors.”
                    '
                    'I smile back at her. “You mean ones that weren’t meant to reach you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her. “You mean ones that weren’t meant to reach you.”')
                        $ questionpreset = "thais2"
                        $ thais_rumor_counter_threshold = 0
                        menu:
                            '“See, I knew that deep down you’re a true sage,” she titters and straightens up, adjusting her cape without haste. “Do you have something to share?”
                            '
                            '(thais2 preset)':
                                pass
                    '“I’m not a spy.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not a spy.”')
                        $ thais_friendship -= 1
                        $ thais_rumor_counter_threshold = 2
                        $ questionpreset = "thais1"
                        menu:
                            'She sighs exaggeratedly and straightens up. “If you need to sleep on it, that’s fine.”
                            '
                            '(thais1 preset)':
                                pass

label howlersdellquestionsrumorsALL:
    label howlersdellquestionsrumors01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring {i}news{/i} about the other parts of the peninsula.”')
        $ custom1 = renpy.random.choice(['“I’m listening.”', 'She gives you a curious look.', 'Her eyes narrow gently.', 'With a smile, she gestures for you to go on.', '“I can’t wait to hear it.”', 'She glances at a nearby waiter, a young girl, who walks away quickly.'])
        $ questionpreset = "thais2"
        menu:
            '[custom1]
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_monks_golems:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}The monks{/color} are worried about {color=#f6d6bd}Eudocia’s{/color} golems. They asked me to make sure they’re not a threat.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 7
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ minutes += 2
        $ questionpreset = "thais2"
        menu:
            '“I can’t say I blame them... But I thought she and they share at least some of their goals.” She crosses her legs, dangling her foot as she gathers her thoughts. “That sorceress is only a few seasons away from being a crazy witch. One who lives in a tower surrounded by a thunderstorm, with a pointy hat and a talking doorknob.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_eudocia_snakebait:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color}, the enchantress, seems to be addicted to snake bait.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 6
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ minutes += 2
        $ questionpreset = "thais2"
        menu:
            'She scornfully twists her lips. “And I thought it’s more of a fighters’ thing, that herb. Maybe we’ll be able to {i}generously{/i} help her with supplies,” she chuckles.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_elpis_doubt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “As far as I can tell, {color=#f6d6bd}Elpis{/color} doesn’t hold you in high regard.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 8
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        menu:
            'Her face is a perfect mask of indifference, yet she squeezes her deer-shaped buckle. She doesn’t say a thing.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_monks_cave:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to the caves under {color=#f6d6bd}the monastery{/color}. The monks are trying to engrave the entirety of Wright’s Tablets on the walls.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 15
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ minutes += 5
        $ questionpreset = "thais2"
        menu:
            'She listens to your tale with a growing smirk. “And that’s it? No treasury, no...” she waves her hand by her face, as if she’s trying to gather more ideas from the air, “secret spells, or napping dragons? Ridiculous, just a dumb waste of effort.” She bursts into laughter, and asks a young man to bring both you and her a mug of ale. “Well, that’s one thing I don’t have to worry about.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_greenmountaintribe_found:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to {color=#f6d6bd}The Tribe of The Green Mountain{/color}...”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 12
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        $ quarters += 1
        menu:
            'You explain how you reached it and what you saw. She rubs her hands cheerfully. “Judging by your tale, they aren’t bothered by their humble lives, and even less so by what we try to build here. Splendid! I don’t need more chaos in our land.”
            \n\nShe leans forward with a smile, resting her chin on her wrist. “Only the oldest of our forest speakers have ever been in that place. It’s remarkable that you’ve managed to find it.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_glaucia_found:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know the location of the bandits’ hideout.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 18
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ banditshideout_knowsaboutlumberjackcamp += 1
        $ banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp += 1
        $ questionpreset = "thais2"
        menu:
            'After your brief explanation, she chips in, and snaps her fingers a few times. “Ah, the lumberjack hamlet? It used to belong to {color=#f6d6bd}Gale Rocks{/color}. Now if {color=#f6d6bd}Glaucia{/color} starts causing any trouble, we’ll know where to strike.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_foggylake_purchase:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Seems like {color=#f6d6bd}%s{/color} is looking to purchase {color=#f6d6bd}Foggy Lake{/color}.”' %iason_name)
        # $ thais_friendship += 1
        $ thais_rumor_points += 6
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        menu:
            '“That’s far from ideal. Allowing two inns to be controlled by a single soul may cause trouble for the third one,” she points at {color=#f6d6bd}Ape Ale{/color} with her thumb, “and in this case, {i}the third one{/i} is the one that really matters.”
            \n\nShe leans back and starts to tap the table with her fingers.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_glaucia_undead:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve learned why {color=#f6d6bd}Glaucia{/color} is so obsessed with taking the necromancers down.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 10
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        menu:
            'As you share {color=#f6d6bd}Glaucia’s{/color} story, {color=#f6d6bd}Thais{/color} gives you a cold look. “So that’s what this was all about. I always struggled to see how she, a soul who, I think you’ll agree, is rather {i}sane{/i}, has worn blinkers for so many years. I knew I was missing a part of the puzzle.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_soldiers_leaving:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The squad that made camp at the southern crossroads is now nothing more than two people. They plan to return to {color=#f6d6bd}Hovlavan{/color} before the fall.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 5
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        menu:
            '“Since they cleared that camp of brigands, they went so quiet I almost forgot about them,” she rubs her chin with her thumb. “I’m surprised they’ve managed to stay alive till this day. Sending such an inexperienced group here shows that the officials misjudged this land.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_soldiers_goal:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The soldiers who came here in spring were meant to find a good spot for a new outpost.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 8
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        menu:
            'She smiles widely. “You don’t say? Knowing that, I’ll prepare a few {i}very{/i} tempting suggestions for the officials.” After she seals her lips, she still lets out a quiet chuckle.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_vein:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I probably should take this news straight to the guild, but... “I found a copper vein. Here, in the North.”')
        # $ thais_friendship += 2
        $ thais_rumor_points += 20
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ howlersdell_reputation += 1
        $ questionpreset = "thais2"
        $ foragingground_foraging_vein_sabotaged = 1
        $ quarters += 1
        menu:
            '“Are you serious? Where, exactly?” You tell her about your finding, though she hesitates to trust you. For a few long minutes she asks you for details, and you suddenly notice that a few of her questions are overlapping - she’s searching for lies.
            \n\nOnce satisfied, she gives you a grateful nod, crossing her legs and clasping her hands around the higher knee. “I can’t do anything with it before spring... But we’ll be prepared. Starting any work so close to the tribe from {color=#f6d6bd}Creeks{/color} won’t be easy, but I’ll figure this out.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_forestgarden:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The forest garden at the edge of the bogs is now mostly abandoned.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 3
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ minutes += 1
        $ questionpreset = "thais2"
        menu:
            '“I see... But that place is so far away from here we can’t properly guard it, not without a hamlet. I need to think if it’s worth the effort,” she spares you a gentle nod.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_creeks_missinghunters:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} has suffered quite a blow. Three of their best hunters either died, or have disappeared.”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 6
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ minutes += 5
        $ questionpreset = "thais2"
        menu:
            'She struggles to hide her smile. “Who were they, exactly?” Your story is brief, and she admits she’s never heard of them. As she’s holding her buckle, her voice suddenly grows solemn. “I hope their families will find comfort in what you’ve learned.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_creeks_struggles:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Creeks{/color} face many struggles...”')
        # $ thais_friendship += 1
        $ thais_rumor_points += 6
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        $ quarters += 1
        menu:
            'Your tale takes quite a few minutes - not only does {color=#f6d6bd}Thais{/color} have many questions, she finally asks {color=#f6d6bd}Eryx{/color} to bring her a wax tablet, in which she starts making notes. Once you’re done, she lets out a relieved sigh, and speaks more to herself than to you. “If it just so happens that the tribe will need {i}my{/i} help, I’ll be prepared to answer their call.” She looks you in the eyes and smiles warmly, then closes the tablet loudly.
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_galerocks_trading:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Severina{/color} of {color=#f6d6bd}Gale Rocks{/color} tries to get an edge by paying messengers to avoid your village.”')
        # $ thais_friendship += 2
        $ thais_rumor_points += 18
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        $ quarters += 1
        menu:
            '“That old bat,” she grabs her deer-buckle, but you catch a glimpse of a smile in her eyes. “She must have convinced quite a few people to lie to me. I wonder what the caravans will have to say to that. Their {i}embarrassment{/i} will help our negotiations greatly.”
            '
            '(thais2 preset)':
                pass
    label howleresdellthais_rumor_glaucia_revenge:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} won’t forgive the way you handled {color=#f6d6bd}Steep House{/color}. Once she runs out of undead to fight with, she’ll target either you, or your people.”')
        # $ thais_friendship += 2
        $ thais_rumor_points += 22
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        $ questionpreset = "thais2"
        $ coins += 5
        show screen notifyimage( "+5", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+5 {image=cointest}{/i}')
        menu:
            'She looks away, with tightened lips. Her chest moves from deep breaths, and after a moment, she gestures for {color=#f6d6bd}Akakios{/color} to step closer. “Give [pcname] five rings,” she says without as much as looking at him. Her green eyes reveal a mixture of anger and amusement. “She’s in for a surprise,” she titters, making {color=#f6d6bd}the trader{/color} scuttle away once he leaves the coins on the table. “I was letting her do her thing for too long. I’ll get her next year.”
            '
            '(thais2 preset)':
                pass

    label howleresdellthais_rumor_elpis_treason:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elpis{/color} hides something from you. She wants me to go with someone to the forest garden.”')
        # $ thais_friendship += 2
        $ howlersdell_elpis_friendship -= 10
        $ howlersdell_reputation -= 1
        $ thais_rumor_points += 18
        if thais_rumor_points >= thais_rumor_points_threshold:
            $ thais_friendship += 1
        if not thais_rumor_elpis_doubt:
            $ thais_rumor_elpis_doubt = 1
            $ thais_rumor_points += 4
            if thais_rumor_points >= thais_rumor_points_threshold:
                $ thais_friendship += 1
        $ questionpreset = "thais2"
        $ coins += 5
        show screen notifyimage( "+5", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+5 {image=cointest}{/i}')
        $ minutes += 5
        if quest_thyrsusgift == 1:
            $ elpis_about_thyrsusgift1 = 0
            $ howlersdell_mundanework_type = "hunters"
            $ quest_thyrsusgift = 3
            $ renpy.notify("Quest completed: Thyrsus’ Wand")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Thyrsus’ Wand{/i}')
            $ quest_thyrsusgift_description_faildescription = "Now that I betrayed {color=#f6d6bd}Elpis{/color}, {color=#f6d6bd}Thyrsus{/color} won’t get any help from her."
        menu:
            'You mention the role of the guards as well, and she reaches for her buckle. “Is that right?” She gestures for one of the guards to approach her - a man you’ve noticed around whenever you hold a conversation with the mayor. Her orders are dripping with cruel disappointment. “I’m going to speak with the archdruidess soon, and right after that we’re going to hold a gathering of all the guards. Tell them all to prepare themselves. And,” she sends you a delighted smile, “bring five dragon bones for our very helpful guardian of the roads.”
            \n\nSoon, the coins, tied together with a thread, appear in front of you, but even though {color=#f6d6bd}Thais’{/color} tone remains bright, you’ve no doubt something has just ended.
            '
            '(thais2 preset)':
                pass

    label howlersdellquestionsrumors01leaving:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I have to say.”')
        if thais_rumor_counter < thais_rumor_counter_threshold:
            jump howlersdellthaisafterquestionsALL
        else:
            $ thais_rumor_counter_threshold += 2
            jump howlersdellthaisafterquestions

label howlersdellquestionsnecromancers01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard of the necromancers in the North?”')
    $ thais_about_necromancers = 1
    $ questionpreset = "thais1"
    menu:
        'She taps her fingers on the table. “Yes, I have.”
        \n\nAfter you ask her to tell you more, she seems to regain her confidence. “You mean {color=#f6d6bd}White Marshes{/color}, for sure. I don’t know all that much about what’s happening there. We avoid their lands, if we can.” She frowns. “I shouldn’t gossip about it with strangers. We can talk about it on another occasion.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionshowlers01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Howler’s Dell{/color}?”')
    $ thais_about_howlers = 1
    $ quarters += 1
    $ description_howlersdell06a = "{color=#f6d6bd}Thais{/color} calls it the “greatest village in the far North.”"
    $ description_howlersdell05 = "The locals are following the teachings of a group of druids."
    $ questionpreset = 0
    menu:
        '“It is what it seems like, the greatest village in the far North!” She raises her hand and makes an inviting gesture. “Though I hope to still improve this and that,” she winks at you, but is suddenly interrupted by the pained cry of a little boy, who hurt his knee during a fall. As an amused elder tries to calm him down, {color=#f6d6bd}the mayor{/color} shrugs it off and titters, then meets your eyes again.
        \n\n“Life’s good here. We have what we need and a lot of what we want, building on top of more than twelve generations of hard work and bravery.” She spends a good few minutes telling you about mouflons, wheat, rye, hemp, cheese, and wool, proud of every glimpse of prosperity. Whenever she mentions an artisan, shepherd, or farmer, she doesn’t miss a chance to mention how significantly she improved their conditions.
        \n\nShe also omits some topics. You hear of no tales, songs, ancestors, rituals, or days of prayer. It’s like listening to a tax collector.
        \n\nOnly at the very end of her speech does she mention the “wisdom of the elders,” now kept in the teachings of the druids, who help her guide those who trust her. They “heal our wounds and our gardens,” she explains, but then changes the topic to all the fruit trees, hares, and nuts in the woods.
        '
        'Once she’s done with it, I nod politely.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once she’s done with it, I nod politely.')
            jump howlersdellthaisafterquestions

label howlersdellquestionsplague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”')
    $ thais_about_plague = 1
    $ howlersdell_elpis_firsttime_theywant = 1
    $ howlersdell_reputation += 1
    $ oldpagos_plague_warnedplaces += 1
    $ questionpreset = "thais1"
    menu:
        'For a few breaths, she doesn’t even blink. “So close to us, a plague? How?” She adjusts her cape and calls a guard with a gesture. “Tell the others to gather by {color=#f6d6bd}Ape Ale{/color},” she tells her, then looks back into your eyes. “I’ll pass them the news once we’re done here. We have close the gates, maybe keep strangers away...”
        \n\nShe starts to tap on her deer-buckle. “At least we can make some preparations, thanks to you. Good wardening,” she says with little conviction, “but you should also speak with our {color=#f6d6bd}druids{/color}. They may have more questions for you.”
        \n\nThe guard returns, and {color=#f6d6bd}the mayor{/color} sends her away again: “Warn {color=#f6d6bd}Elpis{/color}. She must speak with [pcname] soon.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionspyrrhos01:
    $ questionpreset = "thais1"
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think about the scavenger who has been here before?”')
    $ thais_about_pyrrhos = 1
    $ description_pyrrhos04 = "According to {color=#f6d6bd}Thais{/color}, she doesn’t like his company. “The farther away he stays from here, the better.”"
    menu:
        '“Ah, he’s still alive,” she says with distaste. “He brought us some news from the North and paid off his debt to us, but he’s an idler and a prattler. Drinks, too. The farther away he stays from here, the better.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsgreenmountaintribe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”')
    $ thais_about_greenmountaintribe = 1
    $ description_greenmountaintribe05 = "According to {color=#f6d6bd}Thais’{/color} deceased sister, they were “wearing animal faces.”"
    $ questionpreset = 0
    menu:
        'She opens her mouth, but needs a few breaths to respond. “I... compliment you for finding out about their existence at all,” she rubs the back of her neck. “I {i}can’t{/i} tell you much about them. To be honest, I wouldn’t be allowed to, even if I wanted to.”
        \n\n“Ma!” Hearing the call of a little girl, {color=#f6d6bd}Thais{/color} flinches. It turns out the child is demanding a change of shirt - she points at a large stain on her stomach. “What happened here,” {color=#f6d6bd}the mayor{/color} asks as she turns away from you to help the girl change, but doesn’t wait for her response. “I haven’t spoken with {color=#f6d6bd}The Tribe{/color} in ten years or so. As a child I was told that one should never seek their home,” she takes a look at her daughter. The “new” shirt is as worn and dull as the old one - it’s an old garment for adults. On her small frame, it looks like a baggy tunic. “Very nice, go play,” she concludes absently and looks back at you, sighing with annoyance.
        \n\n“My sister used to brag that she saw them once in the woods, during their hunt. That they were wearing the faces of animals, looking like the beastfolk. She tried to make a mask of her own, but the druids told her to stop fooling around. {i}Kids are liars{/i}, my father said,” she lets out a quiet titter.
        '
        '“Could I ask her a couple of questions?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could I ask her a couple of questions?”')
            menu:
                '“I’m afraid she’s with the forest now. A bolt of lightning hit her, right in the head.”
                '
                '“I’m sorry to hear that.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry to hear that.”')
                    jump howlersdellthaisafterquestions
                '“I see.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                    jump howlersdellthaisafterquestions

label howlersdellquestionsaltar01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve seen a weird tree south from here. The one with the altar standing in front of it.”')
    $ thais_about_altar = 1
    $ questionpreset = "thais1"
    $ beholder_name_known = 1
    menu:
        'She straightens up and raises her chin. “You mean {color=#f6d6bd}Beholder{/color}, the guardian spirit of our wetlands. Every fall, we bring it our gifts and in return it provides us with its blessed fruit, the flesh of the forest,” she stares into your eyes. “It’s older than the oldest books and the oldest thoughts. The druids help us honor its sleep and show us how to ask for its help. Neither of these rituals,” she scoffs, “would be of use for you.”
        '
        '(thais1 preset)':
            pass

label howlersdellthaisoceannecklace01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the necklace I found at the hamlet. “Have you ever seen such a trinket?”')
    $ thais_about_necklace = 1
    $ questionpreset = "thais1"
    menu:
        'She reaches for it, but doesn’t touch it. In her green eyes, you notice disgust.
        \n\n“Let me think,” she mutters. “No, I can’t say I have. An ugly little thing, but tells me nothing.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsabouthermoney01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You seem to be fairly well-off, even more so than the other people in the village. What’s your secret?”')
    $ thais_about_hermoney = 1
    $ thais_friendship -= 1
    $ questionpreset = "thais1"
    menu:
        'She reaches for her buckle, and her voice grows cold. “There’s no {i}secret{/i}, traveler. There’s hard work, risks and sacrifices, and the support of those that care about me. The good things that happened to me shine on my people just as much. Think about it before you mention it again,” she adjusts her cape.
        '
        '(thais1 preset)':
            pass

label thais_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a few questions about {color=#f6d6bd}Erastos{/color}.”')
    if (thais_friendship+appearance_charisma) < 6:
        $ quest_recruitahunter_spokento_thais_gray = 1
        $ questionpreset = "thais1"
        menu:
            'She makes an odd grimace, trying to smile while expressing confusion. “I doubt there’s much to say here. He’s just a trapper, and not the best one.”
            '
            '(thais1 preset)':
                pass
    else:
        label thais_about_recruitahunter02:
            $ quest_recruitahunter_spokento_thais = 1
            $ quest_recruitahunter_erastos_points += 1
            if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_erastos_points_notify2:
                $ quest_recruitahunter_erastos_points_notify2 = 1
                $ quest_recruitahunter_erastos_points_notify1 = 1
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
            elif quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_erastos_points_notify1:
                $ quest_recruitahunter_erastos_points_notify1 = 1
                $ renpy.notify("Journal updated: Recruit a Hunter")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
            $ questionpreset = "thais1"
            if quest_recruitahunter_spokento_thais_gray:
                $ custom1 = "This time, her gaze is much harsher. “This again? Why not just let it go?”"
            else:
                $ custom1 = "She makes an odd grimace, trying to smile while expressing confusion. “I doubt there’s much to say here. He’s just a trapper, and not the best one.”"
            menu:
                '[custom1] After you explain the situation, she scratches the table by accident. “Let’s just say I won’t oppose him leaving our village, but I have no warm words to say about him.”
                '
                '(thais1 preset)':
                    pass

    label thais_about_recruitahunter01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Back to {color=#f6d6bd}Erastos{/color}...”')
        jump thais_about_recruitahunter02

label howlersdellquestionsgolemsALL:
    label howlersdellquestionsgolems01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I’d like to hang this rod on a watchtower for her.”')
        $ thais_about_golemsrods = 1
        $ questionpreset = 0
        menu:
            'You let her weigh a rod in her hand. “It’s empty,” she says. “What is it for?”
            '
            '(lie) “I don’t know. Some sort of magic, I assume.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I don’t know. Some sort of magic, I assume.”')
                $ thais_about_bronzerod_threshold = 10
                $ pc_lies += 1
                menu:
                    '“Well, that’s a lot of trust you want me to invest into something that may give me nothing in return. I don’t know, traveler. Not only do you want me to trust you, but also a crazy witch.” She spends a few long breaths in silence, rolling the piece of bronze on the table.
                    '
                    'I wait for her decision.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her decision')
                        $ minutes += 2
                        jump howlersdellquestionsgolems02
            '{image=d6} (lie) “It tracks rain and winds. She’s trying to learn if the entire peninsula has the same weather at all times.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} (lie) “It tracks rain and winds. She’s trying to learn if the entire peninsula has the same weather at all times.”')
                if (pc_lies+appearance_charisma) >= 6:
                    $ pc_lies += 1
                    $ thais_about_bronzerod_threshold = 7
                    menu:
                        '“Oh,” she looks at you with a kind smile. “I must admit, such knowledge could have its use. Though I’m far from trusting her, even if you’re on her side.” She spends a few long breaths in silence, rolling the piece of bronze on the table.
                        '
                        'I wait for her decision.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her decision')
                            $ minutes += 2
                            jump howlersdellquestionsgolems02
                else:
                    $ pc_lies += 1
                    $ thais_about_bronzerod_threshold = 12
                    menu:
                        'She clasps her hands around her knee. “Since when does she pay attention to the skies? You want me to believe she’s looking after crops?” She tilts her head to the left and purses her lips. “Even if such knowledge could have its use, I’m far from trusting her. You should also be worried.” She spends a few long breaths in silence, rolling the piece of bronze on the table.
                        '
                        'I wait for her decision.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her decision')
                            $ minutes += 2
            '“It’s meant to help her golems cover longer distances without going crazy.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s meant to help her golems cover longer distances without going crazy.”')
                $ thais_about_bronzerod_allowed = -1
                $ questionpreset = "thais1"
                menu:
                    'She gives you a long look, then rolls the piece of bronze back to you. “The answer is {i}no{/i}. And if any of us finds such a rod in our woods, you and I are going to have a talk. I have no desire to wake up in the middle of the night, surrounded by her stone army.”
                    '
                    '(thais1 preset)':
                        pass

    label howlersdellquestionsgolems02:
        $ questionpreset = 0
        if (thais_friendship+howlersdell_reputation+appearance_charisma) >= thais_about_bronzerod_threshold:
            $ thais_about_bronzerod_allowed = 1
            if thais_friendship >= ((thais_about_bronzerod_threshold/2)+1):
                $ custom1 = "So far, you’ve been rather reliable,” she smiles, “and I don’t think a piece of bronze will hurt us much."
            elif howlersdell_reputation >= ((thais_about_bronzerod_threshold/2)+1):
                $ custom1 = "My neighbors have some kind words to say about you, they won’t oppose a piece of bronze."
            else:
                $ custom1 = "So far, I’ve heard rather good words about you, even if you don’t have many friends among us. I’ll do you a favor."
            menu:
                '“[custom1] You have my permission to put it on whichever tower you want.”
                '
                '“Thanks.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                    jump howlersdellthaisafterquestions
        else:
            $ questionpreset = "thais1"
            menu:
                '“I’ve heard enough. I can’t know it’s not some nasty trick. If you want to have my permission to do your magical experiments, I need to know I can trust you.”
                '
                '(thais1 preset)':
                    pass

    label howlersdellquestionsgolems01b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About that bronze rod...”')
        $ thais_about_bronzerod_allowed = 1
        $ questionpreset = 0
        if thais_friendship >= ((thais_about_bronzerod_threshold/2)+1):
            $ custom1 = "So far, you’ve been rather reliable,” she smiles, “and I don’t think a piece of bronze will hurt us much."
        elif howlersdell_reputation >= ((thais_about_bronzerod_threshold/2)+1):
            $ custom1 = "My neighbors have some kind words to say about you, they won’t oppose a piece of bronze."
        else:
            $ custom1 = "So far, I’ve heard rather good words about you, even if you don’t have many friends among us. I’ll do you a favor."
        menu:
            '“[custom1] You have my permission to put it on whichever tower you want.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump howlersdellthaisafterquestions

label howlersdellquestionsthais_about_asteriontabletALL:
    label howlersdellquestionsthais_about_asteriontablet01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you read me this tablet?”')
        $ thais_about_asteriontablet = 1
        $ item_asteriontablet_read = 1
        $ asterion_highisland_clues += 1
        $ minutes += 5
        $ questionpreset = 0
        menu:
            '“Dirty,” she raises her open palms. You open the tablet yourself and push it toward her. She leans forward with a sigh.
            \n\n“Well, half of it is just nonsense. Some letters, numbers, a picture of a... boat, I think, and one of a volcano. Scrawling about the size of an oar...” She stops suddenly. “Oh, here’s a name. {color=#f6d6bd}Navica{/color}.”
            \n\nShe sees your look and shakes her head gently. “I don’t know her. Why are you interested in this tablet, anyway? Who’s the owner?”
            '
            '“It may have belonged to {color=#f6d6bd}Asterion{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may have belonged to {color=#f6d6bd}Asterion{/color}.”')
                $ questionpreset = "thais1"
                menu:
                    'At first you think she nods to confirm she heard you, then you realize she’s gesturing to make you take the tablet away. “I see. So it’s not really my problem.”
                    \n\nShe turns away and looks at {color=#f6d6bd}Eryx{/color}. “Can you wipe this?” She points at the table and soon after he shows up with a wet cloth.
                    '
                    '(thais1 preset)':
                        pass
            '“I’m not sure yet. But it may be important.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not sure yet. But it may be important.”')
                $ questionpreset = "thais1"
                menu:
                    'At first you think she nods to confirm she heard you, then you realize she’s gesturing to make you take the tablet away. “Well, you could look for boats in {color=#f6d6bd}Gale Rocks{/color}. They know them better than us {i}inlanders{/i}.”
                    \n\nShe turns away and looks at {color=#f6d6bd}Eryx{/color}. “Can you wipe this?” She points at the table and soon after he shows up with a wet cloth.
                    '
                    '(thais1 preset)':
                        pass
            '(lie) “I’ve got no clue.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’ve got no clue.”')
                $ thais_friendship -= 1
                $ pc_lies += 1
                $ questionpreset = "thais1"
                menu:
                    'She smirks and gestures for you to take the tablet away. “Right, right...”
                    \n\nShe turns away and looks at {color=#f6d6bd}Eryx{/color}. “Can you wipe this?” She points at the table and soon after he shows up with a wet cloth.
                    '
                    '(thais1 preset)':
                        pass

label howlersdellquestionsthais_about_readtheletter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I show her the troll-bone tablet. “Could you tell me what’s in here?”')
    $ item_letterwhitemarshes_read = 1
    $ minutes += 5
    $ questionpreset = "thais1"
    menu:
        '“Pretty!” She taps on the carving of the back. “You sure you don’t want to leave it with {color=#f6d6bd}Akakios{/color} for a few bones?” She glances at the letters, then puts the tablet on the table. “It’s just some farewell letter, written to {color=#f6d6bd}Valens{/color}. His husband says he couldn’t stand {i}this nightmarish village{/i}, and that he met someone else during his hunting trip. It ends with {i}we will start a new family, goodbye{/i}. No signature.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionwineALL:
    label howlersdellquestionwine01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this bottle of wine. Any ideas what it is?”')
        $ thais_about_wine = 1
        $ minutes += 5
        $ questionpreset = 0
        if (thais_friendship+howlersdell_reputation+appearance_charisma) >= 12:
            $ item_asterionwine_pcknows_2 = 1
            if pc_goal == "ineedmoney":
                $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                $ quest_pc_goal_description_completed_ineedmoney = "I have a bottle of {color=#f6d6bd}Night’s Bane{/color}, a wine left by {color=#f6d6bd}Asterion{/color}. If it’s the real deal, it will help me save my sibling - if I combine it with the pay from the merchant guild."
            if pc_goal == "iwantmoney":
                $ quest_pc_goal_description_completed_iwantmoney = "I have a bottle of {color=#f6d6bd}Night’s Bane{/color}, a wine left by {color=#f6d6bd}Asterion{/color}. If it’s the real deal, it will make me incredibly rich in {color=#f6d6bd}Hovlavan{/color} - if I combine it with the pay from the merchant guild."
                $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
            menu:
                'With wide-open eyes she observes the engraved letters, rotating the bottle gently. She pulls out the wax seal and sniffs the contents. Her voice is tense and quiet.
                \n\n“You’re tempting me to lie to you, but as a mayor I’m obliged to honor those who’ve helped our village. One day in the past, this bottle stored {color=#f6d6bd}Night’s Banes{/color}, one of the priciest drinks I saw while I was in {color=#f6d6bd}Hovlavan{/color}, many years ago. Even back then, it was worth about a hundred dragons.”
                \n\nShe seals it again. “Most likely, the liquid inside is not the real deal, but I wouldn’t know. Better take it to merchants. Here, you won’t find any {i}wine collectors{/i},” she says this with a smirk and adjusts her cape.
                '
                '“Would you like to buy it?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would you like to buy it?”')
                    jump howlersdellquestionwine01a
                '“Thank you for your honesty.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for your honesty.”')
                    $ thais_friendship += 1
                    jump howlersdellthaisafterquestions
                '“You realize that lying to me would end poorly for you, right? Sooner or later, I’d know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You realize that lying to me would end poorly for you, right? Sooner or later, I’d know.”')
                    jump howlersdellquestionwine01c
        else:
            menu:
                'With wide-open eyes she observes the engraved letters, rotating the bottle gently. She pulls out the wax seal and sniffs the contents. Her voice is tense and quiet.
                \n\n“Well... A wine is a wine, [pcname]. Worth a couple of dragons, but that’s about it. It would look great in our inn during rainy days, we could put a candle into it.” She relaxes a bit and crosses her legs, dangling her foot. “What do you plan to do with it?”
                '
                '“Would you like to buy it?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would you like to buy it?”')
                    jump howlersdellquestionwine01d
                '“I think I’ll keep it. Just in case I run into a wine lover, you know.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ll keep it. Just in case I run into a wine lover, you know.”')
                    jump howlersdellquestionwine01e
                '“...Are you sure that you told me all you know?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Are you sure that you told me all you know?”')
                    menu:
                        'She titters. “My dear, you can’t expect that I would tell you {i}everything{/i}.”
                        '
                        '“Would you like to buy it?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would you like to buy it?”')
                            jump howlersdellquestionwine01d
                        '“I think I’ll keep it. Just in case I run into a wine lover, you know.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think I’ll keep it. Just in case I run into a wine lover, you know.”')
                            jump howlersdellquestionwine01e

    label howlersdellquestionwine01a:
        menu:
            'She once again picks up the bottle, tapping on it with her pale fingers. “Don’t make me choose!” She bursts into laughter. “I {i}shouldn’t{/i}. We do have a few coins to spare, but they’re meant to help us send one of our children to study in {color=#f6d6bd}Hovlavan{/color}. I ought to not make risky investments,” she sighs. “But thank you.”
            '
            '“Thank you for your honesty.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for your honesty.”')
                $ thais_friendship += 1
                jump howlersdellthaisafterquestions
            '“If you had lied to me, I would have learned the truth, sooner or later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You realize that lying to me would end poorly for you, right? Sooner or later, I’d know.”')
                jump howlersdellquestionwine01c

    label howlersdellquestionwine01c:
        $ thais_friendship -= 1
        $ thais_about_wine_threatened = 1
        $ questionpreset = "thais1"
        menu:
            'With an innocent smile, she lowers her voice to a whisper. You need to pay close attention to her dark-red lips.
            \n\n“Don’t be foolish. Try to raise your hand, and see what happens.” You look around, and notice that even right now there’s a couple of guards standing only a few steps away from you, chatting, but also paying close attention to your gestures. The man who helped you see the village from the top of the watchtower is holding a crossbow.
            \n\n“I’m fed up with your barking.” She leans away and rests her clasped hands on her stomach, giving you a long, piercing look.
            '
            '(thais1 preset)':
                pass

    label howlersdellquestionwine01d:
        menu:
            '“What would I do with it?” Her charming smile adds innocence to her tone.
            '
            '“Drink it, obviously.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Drink it, obviously.”')
                jump howlersdellquestionwine01da
            '“Sell it to the next caravan.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sell it to the next caravan.”')
                jump howlersdellquestionwine01db
            '“It would look fancy on a mead shelf.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It would look fancy on a mead shelf.”')
                jump howlersdellquestionwine01dc

    label howlersdellquestionwine01da:
        menu:
            'She laughs and picks up the bottle again. “We already have barrels of ale and cider! Though I guess it could help me think about the days I spent in the city. How about eight coins?”
            '
            '“Ten sounds much better.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Ten sounds much better.”')
                $ coins += 10
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine.\n+10", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +10 {image=cointest}{/i}')
                menu:
                    '“Maybe for you!” She laughs, but reaches for her pouch. “Very well! For the sake of our {i}friendship{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“Perfect.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Perfect.”')
                $ coins += 8
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine.\n+8", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +8 {image=cointest}{/i}')
                menu:
                    'She exhales and reaches for her pouch. “I still feel like I’m losing here, but well, for the sake of our {i}future collaboration{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“That’s not even close. I’ll keep it with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s not even close. I’ll keep it with me.”')
                $ questionpreset = "thais1"
                menu:
                    '“Oh. As you wish.” Her disappointed voice betrays her indifferent gaze. “Is there anything else?” she asks as you shove the bottle into a sack.
                    '
                    '(thais1 preset)':
                        pass

    label howlersdellquestionwine01db:
        menu:
            'She clicks her tongue and sighs. “I shouldn’t waste our thin treasury for such risky investments.” She picks up the bottle again. “How about six?”
            '
            '“Eight sounds much better.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Eight sounds much better.”')
                $ coins += 8
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine. +8", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +8 {image=cointest}{/i}')
                menu:
                    '“Maybe for you!” She laughs, but reaches for her pouch. “Very well! For the sake of our {i}friendship{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“Perfect.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Perfect.”')
                $ coins += 6
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine. +6", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +6 {image=cointest}{/i}')
                menu:
                    'She exhales and reaches for her pouch. “I still feel like I’m losing here, but well, for the sake of our {i}future collaboration{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“That’s not even close. I’ll keep it with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s not even close. I’ll keep it with me.”')
                $ questionpreset = "thais1"
                menu:
                    '“Oh. As you wish.” Her disappointed voice betrays her indifferent gaze. “Is there anything else?” she asks as you shove the bottle into a sack.
                    '
                    '(thais1 preset)':
                        pass

    label howlersdellquestionwine01dc:
        menu:
            '“Makes sense! It would be a surpising treat for a rich traveler.” She picks up the bottle again. “How about ten?”
            '
            '“Twelve sounds much better.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Twelve sounds much better.”')
                $ coins += 12
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine.\n+12", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +12 {image=cointest}{/i}')
                menu:
                    '“Maybe for you!” She laughs, but reaches for her pouch. “Very well! For the sake of our {i}friendship{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“Perfect.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Perfect.”')
                $ coins += 10
                $ item_asterionwine = 0
                show screen notifyimage( "You sold a bottle of wine.\n+10", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a bottle of wine. +10 {image=cointest}{/i}')
                menu:
                    'She exhales and reaches for her pouch. “I still feel like I’m losing here, but well, for the sake of our {i}future collaboration{/i}.”
                    \n\nWhen you grab the dragon bones, you can’t help feeling that there’s a triumphant smirk hidden in her red lips.
                    '
                    'Well, it’s me who ended up with the coin.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, it’s me who ended up with the coin.')
                        jump howlersdellthaisafterquestions
            '“That’s not even close. I’ll keep it with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s not even close. I’ll keep it with me.”')
                $ questionpreset = "thais1"
                menu:
                    '“Oh. As you wish.” Her disappointed voice betrays her indifferent gaze. “Is there anything else?” she asks as you shove the bottle into a sack.
                    '
                    '(thais1 preset)':
                        pass

    label howlersdellquestionwine01e:
        $ questionpreset = "thais1"
        menu:
            '“Who knows!” She titters, but you catch her disappointed glance. “You may find a luxurious hermitage in the mountains. Just try to not break the bottle in the meantime.”
            \n\nAs you hide the bottle in a bag, she taps her pale fingers on the table.
            '
            '(thais1 preset)':
                pass

label howlersdellthais_about_healingtheplague00:
    show areapicture howlersdellfull at basicfade
    $ renpy.force_autosave(take_screenshot=False, block=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    label howlersdellthais_about_healingtheplague01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ thais_inn = day
        $ questionpreset = 0
        menu:
            'Once you’re done with the unpacking, three armed men show up behind you. Their gambesons are tightly fastened, eyes grim.
            \n\n“She wants to see you,” says the man with a braided beard. He’s holding a large stone mace. “En you’ll come now.”
            '
            '“You mean {color=#f6d6bd}Thais{/color}?”' if howlersdell_elpis_firsttime == 2 and description_druids07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You mean {color=#f6d6bd}Thais{/color}?”')
                menu:
                    'He ignores your question. “Leave your weapon here,” he nods toward {color=#f6d6bd}[horsename]{/color}. “Move.”
                    '
                    'Seems like I don’t have a choice.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I don’t have a choice.')
                        jump howlersdellthais_about_healingtheplague02
            '“{color=#f6d6bd}Elpis{/color}?”' if howlersdell_elpis_firsttime == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Elpis{/color}?”')
                $ thais_friendship -= 1
                $ thais_about_elpis_playerinterested = 1
                menu:
                    'He exchanges surprised looks with the other guards. His voice is harsh. “Why would she? {color=#f6d6bd}The mayor{/color}, of course. Leave your weapon here,” he nods toward {color=#f6d6bd}[horsename]{/color}.
                    '
                    'Seems like I don’t have a choice.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems like I don’t have a choice.')
                        jump howlersdellthais_about_healingtheplague02
            '“After you, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “After you, then.”')
                jump howlersdellthais_about_healingtheplague02

    label howlersdellthais_about_healingtheplague02:
        menu:
            'You’re surrounded by curious glances and worried whispers. {color=#f6d6bd}Thais{/color} is in her usual spot, holding a mug with both hands. She doesn’t have to say a thing - the dining neighbors get on their feet and leave the square, without bothering with their plates. {color=#f6d6bd}Eryx{/color} enters the building, {color=#f6d6bd}Akakios{/color} heads toward the tiny islet. Excluding the guards, who watch your every step, you two are alone.
            \n\nShe waves her hand and you get pushed onto a stool, almost hitting the ground. “Forgive us all these precautions,” she says with a thick, local accent, observing you with piercing, green eyes, “but I’m ne sure who you are. Ne an ally, ne a threat.” Her pale fingers are tapping on the wood, yet her face is like a statue.
            '
            '“I’m a roadwarden. The people of {color=#f6d6bd}Old Págos{/color} called for help and I answered. May they keep their scrap of The Land safer, for the sake of all of us.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Like you said. I’m a roadwarden. The people of {color=#f6d6bd}Old Págos{/color} called for help, and I was ready to answer. May they keep their scrap of The Land safer, for the sake of all of us.”')
                menu:
                    '“Your view of the peninsula is off. You can ne help us all yet stay on the side. When some of us gain, others lose. You took away {i}our{/i} treasure, en now one of us will die because of it. A sick elder, a weak child, a hunter who can’t be healed with a spell.” Her eyes narrow, and keep piercing through your skull. “Would you push one of us from a cliff to save another village? How about killing me? How many lives am I worth?”
                    '
                    '“If I had no other choice than to decide, I would.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If I had no other choice than to decide, I would.”')
                        menu:
                            '“You think {i}you{/i} are the one to make such calls, at {i}our{/i} expense? That we can ne decide on our own?” She takes a sip from her mug, and after a few heartbeats, her eyes soften. “At least your actions are based on conviction, ne on a soft heart. But once these convictions cross ma way, I’ll cut the rotting limb off.”
                            '
                            '“Don’t worry. I’m on your side.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry. I’m on your side.”')
                                $ custom1 = "We’ll see. "
                                jump howlersdellthais_about_healingtheplague03
                            '“Understood.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Understood.”')
                                $ custom1 = "Good. "
                                jump howlersdellthais_about_healingtheplague03
                    '“{i}Murdering{/i} someone would not be the same thing.”':
                        $ thais_friendship -= 2
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Murdering{/i} someone would not be the same thing.”')
                        menu:
                            '“Your inner voice may say so, but to those who you have hurt, the result is the same.” Her voice rises slightly. “Ne only do you claim to have the right to make such calls, you make them from your weakness, ne from conviction.” When she realizes that her fingernails are scratching the wood, she hides her hands under the table. “So this is it. You took our treasure, thinking ‘twas not a big deal. I en the others,” she runs her eyes over the people who are staying at the edge of the square. “will have to pay for it. You’re ne to be trusted.”
                            '
                            '“If you say so.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you say so.”')
                                $ custom1 = ""
                                jump howlersdellthais_about_healingtheplague03
                    'I speak softly, returning her gaze. “I would never hurt you.”' if (thais_friendship+appearance_charisma) >= 8:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak softly, returning her gaze. “I would never hurt you.”')
                        $ thais_friendship += 1
                        menu:
                            'She flinches, straightens up, and takes a sip from her mug. “But you already did, [pcname]. In a way. We can ne tell the consequences of your deeds, but they’ll bring suffering, one way or another.”
                            \n\nShe avoids your eyes.
                            '
                            'I wait for her to speak.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her to speak.')
                                $ custom1 = ""
                                jump howlersdellthais_about_healingtheplague03
                    '“Have mercy on me, {color=#f6d6bd}Thais{/color}. I was meant to deliver messages, kill goblins, and escort travelers. I take no pleasure in making these decisions.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have mercy on me, {color=#f6d6bd}Thais{/color}. I was meant to deliver messages, kill goblins, and escort travelers. I take no pleasure in making these decisions.”')
                        $ thais_friendship -= 1
                        menu:
                            'She straightens up and pushes her mug to the side. “You’re biting off more than you can chew, en we’re paying the price. You are ne a leader. You do ne understand the price such sacrifices put on one’s soul,” she raises her chin, “en they will break you. Either grow a spine, or follow those who did.”
                            '
                            '“You may be right.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You may be right.”')
                                $ custom1 = ""
                                jump howlersdellthais_about_healingtheplague03
            '“I was just pursuing my goals. It doesn’t need to affect our common efforts.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was just pursuing my goals. It doesn’t need to affect our common efforts.”')
                menu:
                    'She stares into your eyes, but the tension in her lips and shoulders softens. “It scares me to think what those goals may be. You must know such a road will surround you ne just with allies, but with foes. Be smart en recognize which village will be stronger in either of these roles.” A long pause. “You have your games, I have mine. Do ne make me think you’re in the way.”
                    '
                    'I don’t respond.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t respond.')
                        $ custom1 = ""
                        jump howlersdellthais_about_healingtheplague03
                    '“Don’t worry. I’m on your side.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t worry. I’m on your side.”')
                        $ custom1 = "We’ll see. "
                        jump howlersdellthais_about_healingtheplague03
                    '“I don’t like to be threatened.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t like to be threatened.”')
                        $ custom1 = "Find someone who gives a shit. "
                        jump howlersdellthais_about_healingtheplague03
            '“I wouldn’t forgive myself for sacrificing this many lives. You can spare one magic fruit for them, {color=#f6d6bd}Thais{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wouldn’t forgive myself for sacrificing this many lives. You can spare one magic fruit for them, {color=#f6d6bd}Thais{/color}.”')
                $ thais_friendship -= 1
                menu:
                    'She covers her mug with her palm. “Do ne dare to tell me what I can en can ne spare. I owe shit to the other tribes. You think {i}they{/i} would save me from danger? Or any of the souls I care about?”
                    \n\nWhen she realizes that her fingernails are scratching the wood, she hides her hands under the table. “So this is it. You took away our treasure because of a soft heart. The others,” she runs her eyes over the people who are staying at the edge of the square. “do ne know what it means to fight for their own good. There are sacrifices harsher than blood en magic trinkets.” She stares at you harshly. “En you’re sacrificing my trust.”
                    '
                    'I stay silent.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                        $ custom1 = ""
                        jump howlersdellthais_about_healingtheplague03

    label howlersdellthais_about_healingtheplague03:
        menu:
            '“[custom1]I’m not petty, [pcname],” she returns to the accent of the cityfolk. “You can still enjoy your stay at our lovely village,” she says with a sigh, then puts on her usual smile, with a hint of a smirk. “We can still use your services. You may be a stranger, but at least you carry dragon bones.”
            \n\nThe guard pushes you away, and the other people read it as a sign. They get back to their tasks and meals, avoiding your the eyes, and the air gets lighter.
            '
            'I look around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
                jump howlersdellsquareregular01

label howlersdellquestionsgivingawaytheseedALL:
    label howlersdellquestionsgivingawaytheseed01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have the Seed of Beholder. What can you give me for it?”')
        $ thais_about_magicfruit = 1
        $ questionpreset = 0
        menu:
            'She looks at you in silence, then narrows her eyes. “How?” She then tilts her head to the right. “And lower your voice.”
            '
            'I’m close to a whisper. “You know how.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m close to a whisper. “You know how.”')
                if (thais_friendship+appearance_charisma) >= 12:
                    menu:
                        'She leans forward with a radiant smile. “I’d be in your debt, [pcname]. If you ever need my help with a {i}risky{/i} endeavour... You may need {i}my{/i} debt. And to make sure you can reach this point in one piece...” She reaches out to you, palm up. “[thais_about_magicfruit_price] dragon bones.”
                        '
                        '“I don’t need more favors. Just offer me a better price.”' if not thais_about_magicfruit_barter:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need more favors. Just offer me a better price.”')
                            $ thais_about_magicfruit_barter = 1
                            $ thais_about_magicfruit_price += 20
                            menu:
                                'Her eyes get grimmer, but she nods. “[thais_about_magicfruit_price], and we’re done here.”
                                '
                                '“Very well.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                                    $ item_magicfruit_lost = 1
                                    $ thais_about_magicfruit_received = 1
                                    $ thais_friendship += 3
                                    $ item_magicfruit = 0
                                    $ coins += thais_about_magicfruit_price
                                    $ minutes += 5
                                    show screen notifyimage( "You sold the Seed.\n+%s" %thais_about_magicfruit_price, "gui/coin2.png")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the Seed.\n+%s {image=cointest}{/i}' %thais_about_magicfruit_price)
                                    menu:
                                        'She licks her wine-red lips, tells you to wait, then stands up and enters the inn. She returns with a pouch and a small, empty sack. She looks around nervously, her hands shaking, but you notice that she also took time to comb her hair. She throws you both bags and sits down. “Put the fruit into the empty one. Keep it under the table.”
                                        \n\nThe pouch is pleasantly heavy. You cover the fruit and move it to the mayor, who attaches it to her belt, like a potato carried from a trader. She puts a finger on her lips, and as you hide your dragons, you’re hit by her dazzling smile.
                                        '
                                        'I smile back at her.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her.')
                                            jump howlersdellthaisafterquestions
                                '“I need to think about it.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                                    $ questionpreset = "thais1"
                                    menu:
                                        '“Fantastic,” her tone could kill a sparrow. “Do you need anything else?”
                                        '
                                        '(thais1 preset)':
                                            pass
                        '“Very well.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                            $ item_magicfruit_lost = 1
                            $ thais_about_magicfruit_received = 1
                            $ thais_friendship += 5
                            $ item_magicfruit = 0
                            $ coins += thais_about_magicfruit_price
                            $ minutes += 5
                            if not thais_about_magicfruit_barter:
                                $ thais_debt = 1
                            show screen notifyimage( "You sold the Seed.\n+%s" %thais_about_magicfruit_price, "gui/coin2.png")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the Seed.\n+%s {image=cointest}{/i}' %thais_about_magicfruit_price)
                            menu:
                                'She licks her wine-red lips, tells you to wait, then stands up and enters the inn. She returns with a pouch and a small, empty sack. She looks around nervously, her hands shaking, but you notice that she also took time to comb her hair. She throws you both bags and sits down. “Put the fruit into the empty one. Keep it under the table.”
                                \n\nThe pouch is pleasantly heavy. You cover the fruit and move it to the mayor, who attaches it to her belt, like a potato carried from a trader. She puts a finger on her lips, and as you hide your dragons, you’re hit by her dazzling smile.
                                '
                                'I smile back at her.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her.')
                                    jump howlersdellthaisafterquestions
                        '“I need to think about it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                            $ questionpreset = "thais1"
                            menu:
                                '“Fantastic,” her tone could kill a sparrow. “Do you need anything else?”
                                '
                                '(thais1 preset)':
                                    pass
                elif (thais_friendship+appearance_charisma) >= 5:
                    $ thais_about_magicfruit_price -= 10
                    $ thais_friendship -= 1
                    menu:
                        'She thinks for a good moment, observing both you and the people nearby. After she leans forward, both her voice and eyes are cold. “You have quite the audacity to come here with what rightfully belongs to my neighbors, {i}and{/i} hoping to not only avoid getting thrown into the woods, but also to get rewarded for your crime.” Her pale fingers are clasped.
                        \n\n“I can give you... [thais_about_magicfruit_price] dragon bones, and I’ll be in your debt, ready to help you with any... {i}Risky{/i} endeavour you may plan.” Seeing that you want to say something, she points at you and wags her finger. “{i}Don’t{/i} push me. You’re already threading through a quagmire.”
                        '
                        '“I don’t need more favors. Just offer me a better price.”' if not thais_about_magicfruit_barter:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need more favors. Just offer me a better price.”')
                            $ thais_about_magicfruit_barter = 1
                            $ thais_about_magicfruit_price += 15
                            menu:
                                'Her eyes get grimmer, but she nods. “[thais_about_magicfruit_price], and we’re done here.”
                                '
                                '“Very well.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                                    $ item_magicfruit_lost = 1
                                    $ thais_about_magicfruit_received = 1
                                    $ thais_friendship += 3
                                    $ item_magicfruit = 0
                                    $ coins += thais_about_magicfruit_price
                                    $ minutes += 5
                                    show screen notifyimage( "You sold the Seed.\n+%s" %thais_about_magicfruit_price, "gui/coin2.png")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the Seed.\n+%s {image=cointest}{/i}' %thais_about_magicfruit_price)
                                    menu:
                                        'She tells you to wait, then stands up and enters the inn. She returns with a pouch and a small, empty sack. She looks around nervously, her hands shaking, but you notice that she also took time to comb her hair. She throws you both bags and sits down. “Put the fruit into the empty one. Keep it under the table.”
                                        \n\nThe pouch is pleasantly heavy. You cover the fruit and move it to the mayor, who attaches it to her belt, like a potato carried from a trader. She puts a finger on her lips, and as you hide your dragons, you’re hit by her dazzling smile.
                                        '
                                        'I smile back at her.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her.')
                                            jump howlersdellthaisafterquestions
                                '“I need to think about it.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                                    $ questionpreset = "thais1"
                                    $ thais_friendship -= 1
                                    menu:
                                        '“Don’t test my patience,” she leans back. “The fruit doesn’t belong to you.”
                                        '
                                        '(thais1 preset)':
                                            pass
                        '“Very well.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                            $ questionpreset = "thais1"
                            $ item_magicfruit_lost = 1
                            $ thais_about_magicfruit_received = 1
                            $ thais_friendship += 5
                            $ item_magicfruit = 0
                            $ coins += thais_about_magicfruit_price
                            $ minutes += 5
                            if not thais_about_magicfruit_barter:
                                $ thais_debt = 1
                            show screen notifyimage( "You sold the Seed.\n+%s" %thais_about_magicfruit_price, "gui/coin2.png")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the Seed.\n+%s {image=cointest}{/i}' %thais_about_magicfruit_price)
                            menu:
                                'She tells you to wait, then stands up and enters the inn. She returns with a pouch and a small, empty sack. She looks around nervously, her hands shaking, but you notice that she also took time to comb her hair. She throws you both bags and sits down. “Put the fruit into the empty one. Keep it under the table.”
                                \n\nThe pouch is pleasantly heavy. You cover the fruit and move it to the mayor, who attaches it to her belt, like a potato carried from a trader. She puts a finger on her lips, and as you hide your dragons, you’re hit by her dazzling smile.
                                '
                                '(thais1 preset)':
                                    pass
                        '“I need to think about it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                            $ questionpreset = "thais1"
                            $ thais_friendship -= 1
                            menu:
                                '“Don’t test my patience,” she leans back. “The fruit doesn’t belong to you.”
                                '
                                '(thais1 preset)':
                                    pass
                else:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                    label howlersdellquestionsgivingawaytheseed01fail:
                        $ thais_about_magicfruit = 1
                        $ thais_afk = day
                        $ thais_afk_cause_magicfruit_tookbyforce = 1
                        $ item_magicfruit_lost = 1
                        $ thais_about_magicfruit_tookbyforce = 1
                        $ item_magicfruit = 0
                        $ renpy.notify("You lost the Seed.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the Seed.{/i}')
                        menu:
                            'She stands up, holding her deer-shaped buckle with her pale fingers. Every word of hers is both quiet, and clear. “You have quite the audacity to come here with what rightfully belongs to my neighbors, {i}and{/i} hoping to not only avoid getting thrown into the woods, but also to get rewarded for your crime.” She then raises her hand, pointing her forefinger at the sky.
                            \n\nThe guards surround you, one of them already holding a flail, another one stringing a bow. An older man, previously eating soup, gets up and scuttles away. {color=#f6d6bd}Thais{/color} ignores all the looks. “You’re threading through a quagmire, traveler. Give me back what’s ours, or face your days as an outlaw.”
                            \n\nYou look for help, but the eyes of the fighters are unforgiving, and the other folks do their best to avoid your eyes. An approaching blade shines in the light. You reach for the fruit, and {color=#f6d6bd}the mayor{/color} takes it from you angrily.
                            \n\nHer frail hand is not much darker than the bone-like skin of the fruit. “If you have to, speak with me tomorrow,” she gasps for breath, but you see triumph in her eyes. She heads to the inn, followed by the looks of her guards - but no one follows her.
                            '
                            'I leave the square.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the square.')
                                jump howlersdellafterinteraction

    label howlersdellquestionsgivingawaytheseed02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can have the Seed.”')
        $ questionpreset = 0
        $ item_magicfruit_lost = 1
        $ thais_about_magicfruit_received = 1
        if thais_about_magicfruit_barter:
            $ thais_friendship += 3
        else:
            $ thais_friendship += 5
        $ item_magicfruit = 0
        $ coins += thais_about_magicfruit_price
        $ minutes += 5
        if not thais_about_magicfruit_barter:
            $ thais_debt = 1
        show screen notifyimage( "You sold the Seed.\n+%s" %thais_about_magicfruit_price, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the Seed.\n+%s {image=cointest}{/i}' %thais_about_magicfruit_price)
        menu:
            'She licks her wine-red lips, tells you to wait, then stands up and enters the inn. She returns with a pouch and a small, empty sack. She looks around nervously, her hands shaking, but you notice that she also took time to comb her hair. She throws you both bags and sits down. “Put the fruit into the empty one. Keep it under the table.”
            \n\nThe pouch is pleasantly heavy. You cover the fruit and move it to the mayor, who attaches it to her belt, like a potato carried from a trader. She puts a finger on her lips, and as you hide your dragons, you’re hit by her dazzling smile.
            '
            'I smile back at her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at her.')
                jump howlersdellthaisafterquestions

label thais_about_highisland_recruitmentALL:
    label thais_about_highisland_recruitment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I believe I can find {color=#f6d6bd}Asterion{/color} on {color=#f6d6bd}High Island{/color}, but I need to take a few fighters with me.”')
        $ thais_about_highisland_recruitment = 1
        $ minutes += 2
        if quest_ruins_choice == "thais_alliance" or thais_debt:
            $ thais_about_highisland_recruitment_done = 1
            $ questionpreset = "thais1"
            menu:
                'She chuckles and leans forward, then realizes you’re not joking. “Tell me more.”
                \n\nYou keep your explanations brief, but no matter the way you cut it, your plan sounds like a ludicrous task. {color=#f6d6bd}The mayor{/color} gestures for you to wait, then adjusts her cloak and lowers her voice. “I’ll find you a few {i}volunteers{/i}, but if you want our assistance, don’t take anyone else. They’ll go as a team, and won’t risk their skin for drunk mercenaries. For now, better be sure you’re ready, and that you have a half-decent boat.”
                '
                '(thais1 preset)':
                    pass
        else:
            $ questionpreset = "thais1"
            menu:
                'She chuckles and leans forward, then realizes you’re not joking. “Tell me more.”
                \n\nYou keep your explanations brief, but no matter the way you cut it, your plan sounds like a ludicrous task. “I {i}can’t{/i} put the lives of my neighbors at such pointless risk,” she straightens up. “I must refuse.”
                '
                '(thais1 preset)':
                    pass

    label thais_about_highisland_recruitment02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a few of your guards on {color=#f6d6bd}High Island{/color}. The officials will want to learn the truth about {color=#f6d6bd}Asterion{/color}.”')
        $ thais_about_highisland_recruitment_done = 1
        $ questionpreset = "thais1"
        menu:
            '{color=#f6d6bd}The mayor{/color} gestures for you to wait, then adjusts her cloak and lowers her voice. “I’ll find you a few {i}volunteers{/i}, but if you want our assistance, don’t take anyone else. They’ll go as a team, and won’t risk their skin for drunk mercenaries. For now, better be sure you’re ready, and that you have a half-decent boat.”
            '
            '(thais1 preset)':
                pass

label howlersdellquestionsbanditsALL:
    label howlersdellquestionsbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was in Pelt of the North. The innkeeper feels uneasy about Glaucia’s band.”')
        $ thais_about_banditband = 1
        $ questionpreset = 0
        menu:
            'When you mention the “raids” on the northern villages, her eyes narrow. “Are you sure? It’s the first I’ve heard about it. {color=#f6d6bd}Glaucia{/color} has been around since years back, but she’s not much of a nuisance.”
            '
            '“I’m just a messenger. He’s asking for you to join forces with him.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m just a messenger. He’s asking for you to join forces with him.”')
                menu:
                    '“Well, I can’t give you my answer. I won’t ask our hunters to endanger their lives in the pursuit of some gossip.”
                    '
                    '“I could ask around, learn more about this.”' if (banditshideout_villagesasked_aboutattacks < 3 and not whitemarshes_attacked) and not (banditshideout_villagesasked_aboutattacks == 2 and druidcave_druid_about_bandits1 and not helvius_about_bandits2):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could ask around, learn more about this.”')
                        $ quest_intelforpeltnorth_description04 = "{color=#f6d6bd}Thais{/color} won’t answer my question until I learn more about the “raids” from the northern villages - {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}."
                        $ renpy.notify("Journal updated: Glaucia’s Band")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}') # TEST
                        menu:
                            'She sighs with exaggerated relief. “What a {i}splendid{/i} idea! There are only three villages in the North. {color=#f6d6bd}White Marshes{/color}, farther north by the western road, {color=#f6d6bd}Gale Rocks{/color}, by the northern coast, and {color=#f6d6bd}Creeks{/color} in the far east. Bring me news from those places and you will get my answer.”
                            '
                            '“I’m paid for passing the message from here to {color=#f6d6bd}Pelt of the North{/color}. Asking me to ride for you through half of the peninsula and back is a different deal entirely.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m paid for passing the message from here to {color=#f6d6bd}Pelt of the North{/color}. Asking me to ride for you through half of the peninsula and back is a different deal entirely.”')
                                jump howlersdellquestionsbandits03
                            '“I can do that.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can do that.”')
                                jump howlersdellthaisafterquestions
                    '“From what I’ve heard, the only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”' if (banditshideout_villagesasked_aboutattacks >= 3) or (banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “From what I’ve heard, the only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”')
                        $ quest_intelforpeltnorth_description04 = "{color=#f6d6bd}Thais{/color} won’t answer my question until I learn more about the “raids” from the northern villages - {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}."
                        jump howlersdellquestionsbandits202
                    '“I don’t have time for this. Should I tell {color=#f6d6bd}the innkeep{/color} that you’re not interested in collaboration?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have time for this. Should I tell {color=#f6d6bd}the innkeep{/color} that you’re not interested in collaboration?”')
                        $ quest_intelforpeltnorth_description05 = "{color=#f6d6bd}Thais{/color} has decided to reject the collaboration. I should bring the news to the innkeeper."
                        $ renpy.notify("Journal updated: Glaucia’s Band")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
                        $ questionpreset = "thais1"
                        $ thais_friendship -= 1
                        menu:
                            'She raises her chin. “I guess you should.”
                            '
                            '(thais1 preset)':
                                pass

    label howlersdellquestionsbandits03:
        menu:
            'She lets out a brief chuckle, but her eyes observe you carefully. “And how much are you being paid, if I can ask?”
            '
            '“[quest_intelforpeltnorth_rewardvalue] dragons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “%s dragons.”' %quest_intelforpeltnorth_rewardvalue)
                $ thais_about_banditbandreward = quest_intelforpeltnorth_rewardvalue
                menu:
                    '“And I’ll pay you another [quest_intelforpeltnorth_rewardvalue]. Fair?”
                    '
                    '“Fair.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fair.”')
                        jump howlersdellthaisafterquestions
            '“You can’t.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can’t.”')
                $ thais_about_banditbandreward = 2
                $ thais_friendship -= 1
                menu:
                    'Her smile disappears. “Now, that’s just plain rude. Bring me the news that I’ve asked for and I’ll give you two dragon bones. No more, no less.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump howlersdellthaisafterquestions

    label howlersdellquestionsbandits201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Glaucia’s{/color} band.”')
        $ questionpreset = 0
        menu:
            '“And what are they?”
            '
            '“The only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”')
                jump howlersdellquestionsbandits202

    label howlersdellquestionsbandits202:
        $ quest_intelforpeltnorth_description06 = "I brought the news to {color=#f6d6bd}Thais{/color}, but she has decided to reject the invitation. I should return to the innkeeper."
        $ thais_friendship += 1
        $ thais_about_banditband2 = 1
        $ renpy.notify("Journal updated: Glaucia’s Band")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        menu:
            'She exhales and raises her open palms. “So there’s no reason to worry. The people of {color=#f6d6bd}White Marshes{/color} are no friends of ours and if {color=#f6d6bd}Glaucia{/color} is eager to bother with the poorest settlement in the North, especially one filled with awoken, it must be personal for her. We have no reason to stand in the middle of it.”
            \n\nShe straightens up and adjusts her cape, then stares into your eyes. Her voice is solemn. “{i}As the mayor of {color=#f6d6bd}Howler’s Dell{/color}, I appreciate your concern, but I don’t share your apprehension. The guards of our village will stay on our walls. Be sure to come see us soon, we would gladly share a lamb and tale with you.{/i}”
            '
            '“Very well. I’ll pass it to him.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll pass it to him.”')
                if thais_about_banditbandreward:
                    $ coins += thais_about_banditbandreward
                    show screen notifyimage( "+%s" %thais_about_banditbandreward, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+%s {image=cointest}{/i}' %thais_about_banditbandreward)
                    menu:
                        'She reaches for her pouch. “And here’s what I promised you. Good work, [pcname].”
                        '
                        '“Let me know if you need anything else.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me know if you need anything else.”')
                            jump howlersdellthaisafterquestions
                else:
                    jump howlersdellthaisafterquestions

label howlersdellnewquestsALL:
    label howlersdellnewquests01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need my assistance?”')
        if (thais_friendship + howlersdell_reputation + appearance_charisma) < thais_fisherhamlet_threshold:
            $ quest_fisherhamlet_gray = 1
            $ questionpreset = "thais1"
            menu:
                '“First, I need to be sure you can handle yourself. Bring me some {i}juicy{/i} rumors, won’t you? And maybe talk with my neighbors. We could use a few coins, or someone with a steady hand.”
                '
                '(thais1 preset)':
                    pass
        elif not quest_fisherhamlet:
            jump howlersdellaboutfisherhamlet01

    label howlersdellnewquests02:
        $ thais_quest_all_cancelled = 1
        $ questionpreset = "thais1"
        menu:
            '“I was going to mention a tiny issue of mine... But it’s safe to say you already handled it for me,” she humbly smiles and taps her fingertips against each other. “For now, my neighbors need to prepare for winter.”
            '
            '(thais1 preset)':
                pass

    label howlersdellnewquests03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need my assistance?”')
        if (thais_friendship + howlersdell_reputation + appearance_charisma) < thais_whitemarshes_threshold:
            $ thais_whitemarshes_gray = 1
            $ questionpreset = "thais1"
            menu:
                'She licks her lips. “Let me think about it, won’t you? In the meantime, you could bring me some {i}delightful{/i} rumors.”
                '
                '(thais1 preset)':
                    pass
        elif orentius_met:
            $ thais_quest_all_cancelled = 1
            $ thais_friendship += 1
            $ questionpreset = "thais1"
            menu:
                'She looks around, then adjusts her cape and lowers her voice. “Have you ever spoken with {color=#f6d6bd}Orentius{/color}, the necromancer of {color=#f6d6bd}White Marshes{/color}?”
                \n\nYou tell her about your conversation briefly. “I doubt I’ll ever be allowed to speak with him again, especially since the villagers now see me as an enemy of theirs,” you conclude while she plays with her deer-shaped buckle.
                \n\n“It surely looks like there’s nothing else we can do about this,” she speaks carefully. “Too bad I didn’t ask you sooner, maybe we could have handled his dark rituals together. For now, I’ve nothing else I need help with, but thank you for asking.”
                '
                '(thais1 preset)':
                    pass

        else:
            jump thais_quest_orentius01

label howlersdellaboutfisherhamletALL:
    label howlersdellaboutfisherhamlet00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use some work.”')
        jump howlersdellaboutfisherhamlet01

    label howlersdellaboutfisherhamlet01:
        $ questionpreset = 0
        menu:
            'She sighs with relief and gestures for you to follow her to the creek. The light dances on its surface, and you can’t miss the fact that it’s humming conveniently camouflages {color=#f6d6bd}the mayor’s{/color} voice. “I’ve a {i}perfect{/i} task for someone of your trade. Behind our northern gate you’ll find a road. It leads to a coastal beach that used to be occupied by our fishers.” Hit by a cold gust of wind, she adjusts her cape, covering her neck. “That hamlet allowed us to watch the sea, and every ten days we had as many fish and crabs as we desired, without the grace of the villages in the North.”
            \n\nShe looks into your eyes. “However, an earthquake led to a rockslide, and has made the road impassable. We weren’t ready to clear it, and now almost a decade later, the route is too unknown for us to risk long journeys.”
            \n\nShe raises her arm, trying to place it around your shoulders.
            '
            'I allow her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow her.')
                $ thais_friendship += 1
                $ description_howlersdell07 = "It used to have access to the fishing hamlet set on the western coast."
                menu:
                    'Her gentle hand is as light as a leaf. “The druids have convinced my people to accept the way it is, the {i}will of the wilderness{/i}.” She smells of roses. “But enough time has passed. The roads grow desolate, and we need to put our trust in ourselves. Help me clear the pass, and my neighbors will follow us - if not because of their ideals, then because of their stomachs.”
                    \n\nAs she steps away, her fingers stroke your neck gently. “The more time we spend on the road, the more monsters will hunt us. With your palfrey, you can save us from danger. Help me retrieve the hamlet and you’ll prove to me that you’re a friend of {color=#f6d6bd}Howler’s Dell{/color}. Start by riding to the buried pass, see if there’s any lairs there that would need our interference.”
                    '
                    '“You’re asking for a lot for a scrap of parchment.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for a lot for a scrap of parchment.”')
                        jump howlersdellaboutfisherhamlet02
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                $ description_howlersdell07 = "It used to have access to the fishing hamlet set on the western coast."
                menu:
                    'With narrowed eyes, she freezes, then crosses her arms. “Let’s not make a scene. Just listen.”
                    \n\n“My neighbors deserve to reclaim the sea, but after all this, it will be difficult. With your palfrey, you can help us explore these places. Help me retrieve the hamlet and you’ll prove to me that you’re on our side. Start by riding to the buried pass, see if there’s any lairs there that would need our interference.”
                    '
                    '“You’re asking for a lot for a scrap of parchment.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re asking for a lot for a scrap of parchment.”')
                        jump howlersdellaboutfisherhamlet02

    label howlersdellaboutfisherhamlet02:
        $ quest_fisherhamlet = 1
        $ renpy.notify("New entry: The Old Hamlet")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Old Hamlet{/i}')
        menu:
            '“Oh, but there will be coin, of course,” laughing, she returns to her chair. “Five for helping us clear the pass, five for letting me know what you’ve learned about the hamlet. Another three if you have to fight in any of these places. For a day or two of work? That’s more than fair.”
            '
            '“I’ll see what I can do.”' if not quest_fisherhamlet_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see what I can do.”')
                jump howlersdellthaisafterquestions
            '“I’ve already been to the collapsed mountain pass.”' if quest_fisherhamlet_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to the collapsed mountain pass.”')
                jump howlersdellfisherhamletupdates02

    label howlersdellfisherhamletupdates01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the fishing hamlet...”')
        $ questionpreset = 0
        menu:
            'She encourages you with a smile.
            '
            'She waits for me to examine the mountain pass. (disabled)' if not quest_fisherhamlet_description01 and not quest_fisherhamlet_description02:
                pass
            '“I’ve been to the mountain pass.”' if quest_fisherhamlet_description01 and not quest_fisherhamlet_description02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to the mountain pass.”')
                jump howlersdellfisherhamletupdates02
            '“I’m ready to escort your people to the rockslide.”' ( condition="quest_fisherhamlet_description02 and not quest_fisherhamlet_description03 and quarters < 40 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to escort your people to the rockslide.”')
                jump howlersdellfisherhamletupdates03
            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not quest_fisherhamlet_description03 and quarters >= 40" ):
                pass
            'I’m too tired to protect the workers at the rockslide. (Required vitality: 2) (disabled)' ( condition="quest_fisherhamlet_description02 and not quest_fisherhamlet_description03 and pc_hp <= 1" ):
                pass
            '“The road is clear.”' if quest_fisherhamlet_description03 and not quest_fisherhamlet_description04 and not quest_fisherhamlet_description05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The road is clear.”')
                jump howlersdellfisherhamletupdates04
            'She waits for me to examine the hamlet. (disabled)' if quest_fisherhamlet_description04 and not quest_fisherhamlet_description05:
                pass
            '“I’ve been to the hamlet.”' if quest_fisherhamlet_description05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to the hamlet.”')
                jump howlersdellfisherhamletupdates05
            '“I’m going to take care of it soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to take care of it soon.”')
                jump howlersdellthaisafterquestionsALL

    label howlersdellfisherhamletupdates02: #I’ve been to the mountain pass.
        $ renpy.notify("Journal updated: The Old Hamlet")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
        $ quest_fisherhamlet_description02 = "Once I’m ready, I should get to {color=#f6d6bd}Howler’s{/color} during the early morning hours. We’re going to organize workers and clear the rockslide, though it may take up to an entire day."
        menu:
            'She rests her chin on the back of her hand and listens patiently to your story, and taps on the table once you mention the buried rags. “None of us were there on the day of the earthquake, and whatever corpses may be there, they’ve surely been awoken by the fogs by now.”
            \n\nShe straightens up. “It’s still better than a wyvern, or a lair of harpies. The plan stays the same. You’ll take twenty diggers and guards and escort them to the rockslide. Your job is to keep them alive and well.”
            \n\nShe looks at the sky. “It may take many hours, maybe even an entire day, so you should start in the morning. You’ll get the first share of your payment once you clear the pass.”
            '
            '“I’m ready to escort your people to the rockslide.”' ( condition="quest_fisherhamlet_description02 and not quest_fisherhamlet_description03 and quarters < 40" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to escort your people to the rockslide.”')
                jump howlersdellfisherhamletupdates03
            'It’s too late to take the workers to the rockslide. (disabled)' ( condition="quest_fisherhamlet_description02 and not quest_fisherhamlet_description03 and quarters >= 40" ):
                pass
            '“I’m going to take care of it soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to take care of it soon.”')
                jump howlersdellthaisafterquestionsALL

    label howlersdellfisherhamletupdates03: #I’m ready to escort your people to the rockslide.
        $ quarters += 1
        $ rockslide_workers = 1
        $ travel_destination = "rockslide"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'Without wasting any time, {color=#f6d6bd}Thais{/color} helps you muster the guards and diggers. They’re healthy, well-fed, and in most cases young. Their chattering is filled with excitement - the younger ones are eager to mention that they’ve never been so far away from the walls.
            \n\nThe older expedition members are going more to lead and advise. They listen to the instructions carefully and are first to take spears from the guards.
            \n\nIt doesn’t take long before you’re ready to leave.
            '
            'I ask the guards to open the gate.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask the guards to open the gate.')
                jump finaldestinationafterevent

    label howlersdellfisherhamletupdates03b:
        $ quarters += 1
        $ rockslide_workers = 1
        $ travel_destination = "rockslide"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You approach a few guards and ask them to help you with the diggers - {color=#f6d6bd}the mayor’s{/color} orders are already well known in the village. Your companions-to-be are healthy, well-fed, and in most cases young. Their chattering is filled with excitement - the younger ones are eager to mention that they’ve never been so far away from the walls.
            \n\nThe older expedition members are going more to lead and advise. They listen to the instructions carefully and are first to take spears from the guards.
            \n\nIt doesn’t take long before you’re ready to leave.
            '
            'I ask the guards to open the gate.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask the guards to open the gate.')
                jump finaldestinationafterevent

    label howlersdellfisherhamletupdates04: #The road is clear.
        if not quest_fisherhamlet_description06:
            $ thais_friendship += 2
            menu:
                'She leans forward. Her voice is close to a whisper, but warmer, like a sunny meadow. “You’re smart to speak with me instead of {color=#f6d6bd}Elpis{/color}. She’s getting... meddlesome.” She straightens up. “Hit me with the good news, [pcname]!”
                \n\nAfter you mention the undead, she stops herself from shedding tears of laughter. “A skeleton with no legs! That {i}must{/i} be a good sign!” Still chuckling, her hand reaches to her belt, from which she unpins a leather pouch, which she then hands you politely.
                \n\n“You’ve done well! Our work isn’t finished yet, but we’re close, so close!” You take the pouch and peek inside. Eight dragons.
                '
                '“Time for me to search the hamlet.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to search the hamlet.”')
                    show screen notifyimage( "Journal updated: The Old Hamlet\n+8", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet\n+8 {image=cointest}{/i}')
                    $ coins += 8
                    $ quest_fisherhamlet_description04 = "I was asked to cross the mountain pass and to reach the hamlet itself. I need to inspect the buildings and look for unusual creatures."
                    jump howlersdellfisherhamletupdates04p02a
                '“I can’t say the {i}fight{/i} we had was worthy of three dragons.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t say the {i}fight{/i} we had was worthy of three dragons.”')
                    show screen notifyimage( "Journal updated: The Old Hamlet\n+8", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet\n+8 {image=cointest}{/i}')
                    $ coins += 8
                    $ quarters += 1
                    $ quest_fisherhamlet_description04 = "I was asked to cross the mountain pass and to reach the hamlet itself. I need to inspect the buildings and look for unusual creatures."
                    jump howlersdellfisherhamletupdates04p02b
        else:
            menu:
                'She leans forward. Her voice is close to a whisper and cold, like a gust of wind. “I wish you’d come to me right away, instead of opening your ears to {color=#f6d6bd}Elpis{/color}.” Her red lips keep wearing her usual smile, but the green eyes match the fury of her tone. “She’s getting... Meddlesome. Watch out for what she tries to sell you.”
                \n\nBefore you get a chance to answer, she straightens up. “Don’t let me wait any longer! Hit me with the good news, [pcname]!”
                \n\nAfter you mention the undead, she stops herself from shedding tears of laughter. “A skeleton with no legs! That {i}must{/i} be a good sign!” Still chuckling, her hand reaches to her belt, from which she unpins a leather pouch. “You’ve done well! Our work isn’t finished yet, but we’re close, so close!” She picks five dragon bones, then pushes them toward you, holding each one with a separate finger.
                '
                '“Time for me to search the hamlet.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to search the hamlet.”')
                    show screen notifyimage( "Journal updated: The Old Hamlet\n+5", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet\n+5 {image=cointest}{/i}')
                    $ coins += 5
                    $ quarters += 1
                    $ quest_fisherhamlet_description04 = "I was asked to cross the mountain pass and to reach the hamlet itself. I need to inspect the buildings and look for unusual creatures."
                    jump howlersdellfisherhamletupdates04p02a

    label howlersdellfisherhamletupdates04p02a:
        menu:
            '“What is this nightmarish trick, you read my soul, [pcname]! Pay close attention to what you’ll find,” she rubs her pale hands, then starts to count down on her pale fingers. “How many cabins are still standing? Are there any lairs nearby? Any signs of vagabonds? Soul-eating mold? Broken walls? The more you learn, the better.”
            '
            '“I’ll see you soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you soon.”')
                jump howlersdellthaisafterquestions

    label howlersdellfisherhamletupdates04p02b:
        menu:
            '“Oh, don’t be so humble now, I hate it,” she bursts into laughter. “I know what I’m paying you for.”
            \n\nShe crosses her legs and rests her hand on her knee. “Now that the rocks are out of the way, I need you to get to the hamlet itself. Pay close attention to what you’ll find! How many cabins are still standing? Are there any lairs nearby? Any signs of vagabonds? Soul-eating mold? Broken walls? The more you learn, the better.”
            '
            '“I’ll see you soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you soon.”')
                jump howlersdellthaisafterquestions

    label howlersdellfisherhamletupdates05: #I’ve been to the hamlet.
        menu:
            'As she puts on a wide, expectant smile, you notice a few more wrinkles around her eyes.
            \n\nAccording to your tale...
            '
            'The hamlet needs some work, but that won’t be a challenge. {color=#f6d6bd}Aegidia{/color} is hiding in one of the buildings.' if aegidia_alive and aegidia_favor != "iwill" and aegidia_favor != "iwillforatime":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The hamlet needs some work, but that won’t be a challenge. {color=#f6d6bd}Aegidia{/color} is hiding in one of the buildings.')
                $ quest_fisherhamlet_description07 = "I talked with {color=#f6d6bd}Thais{/color}. I encouraged her to send workers to the hamlet and I’ve told her about her daughter."
                $ renpy.notify("Journal updated: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
                $ quest_fisherhamlet_description11 = "{color=#f6d6bd}Thais{/color} has walked away without handing me the letter that she promised. I should speak with her tomorrow."
                $ thais_friendship += 2
                $ howlersdell_reputation += 3
                $ thais_afk = day
                $ thais_afk_cause_aegidia = 1
                menu:
                    'You start with the description of the hamlet. {color=#f6d6bd}Thais’{/color} eyes shine, and whenever she interrupts you with a question, her hands enhance every word. At one point, she calls one of her sons, and asks him to bring each of you a mug of buttermilk and a bowl of honeyed nuts.
                    \n\nBut after you mention {color=#f6d6bd}Aegidia{/color}, the cheerfulness gives way to an empty smile, and her questions stop. She stands up, opens a pouch, and scatters the coins on the table. Without a word, she hobbles toward {color=#f6d6bd}Eryx{/color}. A few of her children approach quickly, but she gestures for them to stay away.
                    \n\nAfter she heads upstairs, the innkeep outshouts the entire square. “{color=#f6d6bd}Ma wife{/color} is ill! Whoever wants to speak with her, wait till tomorrow.” He then closes the door and moves behind the counter, looking down.
                    \n\nYou glance at the dragon bones. There’s eight of them.
                    '
                    'I take them and walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take them and walk away.')
                        show screen notifyimage( "+8", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+8 {image=cointest}{/i}')
                        $ coins += 8
                        jump howlersdellsquaafterinteraction01
            'I only mention the good condition of the hamlet.' if aegidia_alive and aegidia_favor:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I only mention the good condition of the hamlet.')
                $ quest_fisherhamlet_description08 = "I talked with {color=#f6d6bd}Thais{/color}. I encouraged her to send workers to the hamlet, but I’ve kept the truth about her daughter to myself."
                $ quest_fisherhamlet = 2
                $ renpy.notify("Quest completed: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Old Hamlet{/i}')
                $ thais_friendship += 3
                $ howlersdell_reputation += 2
                menu:
                    'You start with the description of the hamlet. {color=#f6d6bd}Thais’{/color} eyes shine, and whenever she interrupts you with a question, her hands enhance every word. At one point, she calls one of her sons, and asks him to bring each of you a mug of buttermilk and a bowl of honeyed nuts.
                    \n\nAfter you finish, she leans back and closes her eyes, though her hand is already reaching for a pouch. “I know we said {i}five{/i}, but let’s bump it to eight. Buy yourself something tasty from {color=#f6d6bd}my beloved{/color}.” She places the coins on the table.
                    '
                    'I take them. “Thanks.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take them. “Thanks.”')
                        show screen notifyimage( "+8", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+8 {image=cointest}{/i}')
                        $ coins += 8
                        $ quarters += 1
                        $ custom1 = "She opens her eyes and lets out a satisfied sigh. “And I thank you. A good year is ahead of us. We’ll wait until fall, give the forest spirits some time to adapt to the path you’ve cleared. But our patience is already stronger than any healthy wit,” she titters. “We’ll remove the debris before it snows, and start building in the early spring. We already have too many farmers.” She stands up and adjusts her cape. “Wait for a minute, will you?”"
                        jump howlersdellfisherhamletupdates05part02
            '(half-lie) The hamlet is beyond restoration. {color=#f6d6bd}Aegidia{/color} occupies a nearby cave.' if aegidia_alive and aegidia_favor != "iwill" and aegidia_favor != "iwillforatime":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (half-lie) The hamlet is beyond restoration. {color=#f6d6bd}Aegidia{/color} occupies a nearby cave.')
                $ quest_fisherhamlet_description09 = "I talked with {color=#f6d6bd}Thais{/color}. I told her to stay away from the hamlet and about her daughter."
                $ thais_afk = day
                $ pc_lies += 1
                $ thais_afk_cause_aegidia = 1
                $ renpy.notify("Journal updated: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
                $ quest_fisherhamlet_description11 = "{color=#f6d6bd}Thais{/color} has walked away without handing me the letter that she promised. I should speak with her tomorrow."
                $ thais_friendship += 1
                $ howlersdell_reputation += 2
                menu:
                    'You portray the demolished, rotten cabins, harpy nests, and the collapsed ground. {color=#f6d6bd}Thais’{/color} eyes lose their spark, but she keeps her composure, and even asks for more details.
                    \n\nAfter you mention {color=#f6d6bd}Aegidia{/color}, her questions stop. She stands up, opens a pouch, and scatters the coins on the table. Without a word, she hobbles toward {color=#f6d6bd}Eryx{/color}. A few of her children approach quickly, but she gestures for them to stay away.
                    \n\nAfter she heads upstairs, the innkeep outshouts the entire square. “{color=#f6d6bd}Ma wife{/color} is ill! Whoever wants to speak with her, wait till tomorrow.” He then closes the door and moves behind the counter, looking down.
                    \n\nYou glance at the dragon bones. There’s eight of them.
                    '
                    'I take them and walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take them and walk away.')
                        show screen notifyimage( "+8", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+8 {image=cointest}{/i}')
                        $ coins += 8
                        jump howlersdellsquaafterinteraction01
            '(lie) The hamlet is uninhabitable, even if empty.' if aegidia_alive and aegidia_favor:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) The hamlet is uninhabitable, even if empty.')
                $ quest_fisherhamlet_description10 = "I’ve talked with {color=#f6d6bd}Thais{/color}. I told her to stay away from the hamlet, but I’ve kept the truth about her daughter to myself."
                $ pc_lies += 2
                $ quest_fisherhamlet = 2
                $ renpy.notify("Quest completed: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Old Hamlet{/i}')
                $ thais_friendship += 2
                $ howlersdell_reputation += 1
                menu:
                    'You portray the demolished, rotten cabins, harpy nests, and the collapsed ground. {color=#f6d6bd}Thais’{/color} eyes lose their spark, but she keeps her composure, and even asks for more details.
                    \n\nAfter you finish, she leans forward and rests her cheek on her hand. You don’t even notice where the pouch in her hand came from. “Well, at least the harpies left your eyes alone. Did they bother you?” She slowly counts down three dragon bones, placing them on the table loudly.
                    '
                    'I nod. “You wouldn’t believe the scent of their blood.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “You wouldn’t believe the scent of their blood.”')
                        show screen notifyimage( "+6", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+6 {image=cointest}{/i}')
                        $ coins += 6
                        $ custom1 = "She adds another three bones. “I hear you, no trophies from those freaks. Here’s your compensation.” She observes her pale fingers without a word, then asks you to give her a minute."
                        jump howlersdellfisherhamletupdates05part02
                    'I pack my reward. “Nah. I’m fine.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my reward. “Nah. I’m fine.”')
                        show screen notifyimage( "+3", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 {image=cointest}{/i}')
                        $ coins += 3
                        $ custom1 = "“Good to see someone around here who doesn’t need my help,” she says with little joy and observes her pale fingers. After a few breaths, she asks you to give her a minute."
                        jump howlersdellfisherhamletupdates05part02

        label howlersdellfisherhamletupdates05part02:
            menu:
                '[custom1]
                \n\nAfter she returns from the inn, her lips are covered with a new layer of rouge, darker than usual. One of her sons carries a large bag made of leather, and after you peek inside, you find a sheet of parchment rolled onto two wooden handles. The scroll is new, heavy, tied with a tight linen cord, sealed with wax.
                \n\n“You’ve proven yourself trustworthy, both to me and to my neighbors,” says {color=#f6d6bd}the mayor{/color}. “Take this letter to the masters of the guild. May the negotiations begin.” With a smile, she reaches out her hand.
                '
                'I shake it with enthusiasm. “It was my pleasure.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake it with enthusiasm. “It was my pleasure.”')
                    $ quest_fisherhamlet = 2
                    $ quest_howlerssupport = 2
                    $ quest_fisherhamlet_description12 = "I received my reward."
                    $ quest_howlerssupport_description05 = "I received my reward."
                    $ item_thaisletter = 1
                    if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                        $ pc_goal_iwantstatuspoints += 2
                    if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                        $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell.\nJournal updated: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell. Journal updated: %s{/i}' %quest_pc_goal_name)
                    else:
                        $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell{/i}')
                    jump howlersdellthaisafterquestionsALL2
                'Without a word, I shake it as briefly as I can without upsetting her tribe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a word, I shake it as briefly as I can without upsetting her tribe.')
                    $ quest_fisherhamlet = 2
                    $ quest_howlerssupport = 2
                    $ quest_fisherhamlet_description12 = "I received my reward."
                    $ quest_howlerssupport_description05 = "I received my reward."
                    $ item_thaisletter = 1
                    if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                        $ pc_goal_iwantstatuspoints += 2
                    if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                        $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell.\nJournal updated: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell. Journal updated: %s{/i}' %quest_pc_goal_name)
                    else:
                        $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell{/i}')
                    jump howlersdellthaisafterquestionsALL2

label howlersdellthaisafterafkALL:
    label howlersdellthaisafterafk01:
        $ thais_afk_cause_aegidia = 2
        $ questionpreset = 0
        menu:
            '{color=#f6d6bd}Thais{/color} shows up soon after you sit down on the bench. One of her sons carries a large bag made of leather, and after you peek inside, you find a sheet of parchment rolled onto two wooden handles. The scroll is new, heavy, tied with a tight linen cord, sealed with wax.
            \n\n“I’m glad to see you, [pcname],” {color=#f6d6bd}the mayor’s{/color} voice is hoarse, but confident. “I apologize for yesterday’s inexcusable manners.”
            '
            '“There’s nothing to forgive.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s nothing to forgive.”')
                $ custom1 = "“I appreciate it.” She straightens up and smiles gently. Even though she’s wearing even more powder than usual, she wasn’t able to mask her exhausted, red eyes.\n\n"
                jump howlersdellthaisafterafk02
            '“Don’t mention it. Do you want me to bring {color=#f6d6bd}Aegidia{/color} to you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t mention it. Do you want me to bring {color=#f6d6bd}Aegidia{/color} to you?”')
                $ description_aegidia03 = "Her mother disowned her once she learned of Aegidia’s deception."
                $ custom1 = "“{color=#f6d6bd}Aegidia{/color}, you say? I’ve never heard of such a soul. And we have more important things to discuss.” The tone of her voice could cut a troll in half, but once she meets your eyes, her gaze is as keen as ever.\n\n"
                jump howlersdellthaisafterafk02
            'I speak after a moment of silence. “You have something for me?”':
                $ thais_friendship -= 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak after a moment of silence. “You have something for me?”')
                $ custom1 = "She casts you an angry look, but carries on. "
                jump howlersdellthaisafterafk02

    label howlersdellthaisafterafk02:
        $ questionpreset = 0
        menu:
            '[custom1]“This letter is your reward. Take this letter to the masters of the guild. You’ve proven yourself trustworthy, both to me and to my neighbors, so may the negotiations begin.” With a smile, she reaches out her hand.
            '
            'I shake it with enthusiasm. “It was my pleasure.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake it with enthusiasm. “It was my pleasure.”')
                $ quest_fisherhamlet = 2
                $ quest_howlerssupport = 2
                $ quest_fisherhamlet_description12 = "I received my reward."
                $ quest_howlerssupport_description05 = "I received my reward."
                $ item_thaisletter = 1
                if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                    $ pc_goal_iwantstatuspoints += 2
                if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell.\nJournal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell. Journal updated: %s{/i}' %quest_pc_goal_name)
                else:
                    $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell{/i}')
                jump howlersdellthaisafterquestionsALL2
            'Without a word, I shake it as briefly as I can without upsetting her tribe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a word, I shake it as briefly as I can without upsetting her tribe.')
                $ quest_fisherhamlet = 2
                $ quest_howlerssupport = 2
                $ quest_fisherhamlet_description12 = "I received my reward."
                $ quest_howlerssupport_description05 = "I received my reward."
                $ item_thaisletter = 1
                if (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and pc_goal == "iwantstatus") or (quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter_opened and pc_goal == "iwantstatus"):
                    $ pc_goal_iwantstatuspoints += 2
                if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter and quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell.\nJournal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell. Journal updated: %s{/i}' %quest_pc_goal_name)
                else:
                    $ renpy.notify("Quests completed: The Old Hamlet,\nSupport of Howler’s Dell")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quests completed: The Old Hamlet, Support of Howler’s Dell{/i}')
                jump howlersdellthaisafterquestionsALL2

label thais_quest_orentiusALL:
    label thais_quest_orentius01:
        $ minutes += 5
        show areapicture howlersdellbehindinn01 at basicfade
        hide howlersdellsquareutensils
        $ questionpreset = 0
        menu:
            'She looks around, then adjusts her cape and lowers her voice. “Have you ever spoken with {color=#f6d6bd}Orentius{/color}, the necromancer of {color=#f6d6bd}White Marshes{/color}?”
            \n\n“I haven’t,” you respond, and she bursts into laughter so unprompted and loud it makes you quake. “Have you been to my favorite spot, right behind the corner? Sometimes, all I want is to take a nap there, with a cat on my lap and mint tisane at hand. Come, I’ll show you!”
            \n\nOnce you reach the boar pen, the noise of work and conversations is suppressed by the humming water. {color=#f6d6bd}The mayor{/color} glances at the window above you, then strokes her lips with her thumb. “Let’s rest here,” she leaves you enough space to sit down with her. The scent of her rose perfume is strong, but this time her eyes are absently aimed at {color=#f6d6bd}Bion’s{/color} home.
            \n\n“What I’m going to tell you needs to stay between us,” she says hesitantly.
            '
            '“I figured.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I figured.”')
                menu:
                    'She crosses her legs, clasping her pale hands around her knee. “We need to get rid of the undead.”
                    '
                    '“Of the undead, or the necromancer?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “With the undead, or the necromancers?”')
                        menu:
                            '“We both know the former won’t get away without the latter.” Her voice relaxes a bit and she starts to dangle her sandaled foot. “{color=#f6d6bd}White Marshes{/color} is a threat to us all. We ought to burn the wound while it’s still fresh.”
                            '
                            '“What’s your plan?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your plan?”')
                                jump thais_quest_orentius03

    label thais_quest_orentius03:
        if not quest_orentius:
            $ quest_orentius = 1
            $ renpy.notify("New entry: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Orentius, the Necromancer{/i}')
        else:
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        $ quest_orentius_thais_description00 = "{color=#f6d6bd}Thais{/color} wants to get rid of the undead that serve {color=#f6d6bd}Orentius{/color}, the priest of {color=#f6d6bd}White Marshes{/color}."
        $ quest_orentius_thais_description01 = "My first task is to reach {color=#f6d6bd}White Marshes{/color} and see the scale of the problem with my own eyes. I should ask the locals to allow me to speak with the priest."
        $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
        menu:
            '“Start with reaching the village. It’s not far away from here, just ride north and on the second turn east enter the bogs. Take a closer look, see how many shells they’ve awoken, how dangerous they are. Just don’t mention me at all, being a roadwarden affiliated only with {color=#f6d6bd}Hovlavan{/color} works to your advantage.”
            \n\nOn the opposite bank of the creek, a seagull is preening its feathers, unaware that a young boy is trying to sneak up on it with comically raised hands. “Maybe the locals will allow you to meet with {color=#f6d6bd}the priest{/color}, ask him what his plans are. Just don’t act hastily, and keep me informed.”
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03d
            '“You forgot to mention my reward.”' if not thais_quest_orentius03a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my reward.”')
                jump thais_quest_orentius03a
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03b
            '“What will you do if he refuses to release the corpses?”' if thais_quest_orentius03b and not thais_quest_orentius03c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do if he refuses to release the corpses?”')
                jump thais_quest_orentius03c
            '“I can already tell you this and that about the village.”' if helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump thais_quest_orentius04alt
            '“I’ll be back once I learn anything.”' if not helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back once I learn anything.”')
                jump thais_quest_orentius04

    label thais_quest_orentius03d: #“Explain why you want to interfere.”
        $ thais_quest_orentius03d = 1
        $ description_whitemarshes02 = "The locals use the awoken undead to do their bidding."
        menu:
            '“The people of {color=#f6d6bd}White Marshes{/color} always kept to themselves, but now we’ve got no clue what’s going on there. It’s {i}possible{/i} that they had no other choice but to seek help in dark magic, but if so, they should have abandoned it years back. Maybe they’re building an army, right under our noses? Someone needs to get to the bottom of this, and they won’t trust a soul {i}who does ne sound like a traveler,{/i}” she mockingly switches to her tribe’s accent.
            \n\n“Oh, and awakening dead shells is {i}very, very bad{/i},” she adds with a chuckle, but it sounds a bit different than usual.
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03d
            '“You forgot to mention my reward.”' if not thais_quest_orentius03a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my reward.”')
                jump thais_quest_orentius03a
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03b
            '“What will you do if he refuses to release the corpses?”' if thais_quest_orentius03b and not thais_quest_orentius03c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do if he refuses to release the corpses?”')
                jump thais_quest_orentius03c
            '“I can already tell you this and that about the village.”' if helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump thais_quest_orentius04alt
            '“I’ll be back once I learn anything.”' if not helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back once I learn anything.”')
                jump thais_quest_orentius04

    label thais_quest_orentius03a: #“You forgot to mention my reward.”
        $ thais_quest_orentius03a = 1
        $ thais_friendship -= 1
        menu:
            '“Don’t make me laugh, [pcname],” her voice is grim. “I’m not asking you for a favor, I’m offering you {i}my help{/i}. You think we’re the ones who would suffer from the hands of the undead? It’s the smaller settlements, the roads, the inns, the travelers who’d take the lethal blow. {i}We{/i} can handle the direct threat, but I’d rather see our lives grow in comfort, not conflict.”
            \n\nShe observes her fingers, rubbing them together, as if she’s getting used to a different skin. “If the guild were to see dozens of corpses roaming through the North, they would decide it’s not worth their effort. Do I really have to explain why you shouldn’t stay idle? If you and I act together, I’ll invest coins, time, fighters, and supplies.” With every word, the annoyance in her voice grows. “What else could you want? A blade from cold steel, a riding ibex, a soft shell to warm up your nights, a staff of immortality?” She takes a deep breath, but falls silent.
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03d
            '“You forgot to mention my reward.”' if not thais_quest_orentius03a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my reward.”')
                jump thais_quest_orentius03a
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03b
            '“What will you do if he refuses to release the corpses?”' if thais_quest_orentius03b and not thais_quest_orentius03c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do if he refuses to release the corpses?”')
                jump thais_quest_orentius03c
            '“I can already tell you this and that about the village.”' if helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump thais_quest_orentius04alt
            '“I’ll be back once I learn anything.”' if not helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back once I learn anything.”')
                jump thais_quest_orentius04

    label thais_quest_orentius03b: #“What can you tell me about Orentius?”
        $ thais_quest_orentius03b = 1
        $ description_orentius02 = "According to {color=#f6d6bd}Thais{/color}, he used to have no interest in being a leader."
        menu:
            'She waves it off. “I didn’t pay any attention to him back in the day. His tribe had a regular mayor, whatever her name was. One day he revealed himself to be {i}Wright’s prophet{/i} and somehow convinced his tribe to follow him. I don’t think he’s left his village ever since.”
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03d
            '“You forgot to mention my reward.”' if not thais_quest_orentius03a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my reward.”')
                jump thais_quest_orentius03a
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03b
            '“What will you do if he refuses to release the corpses?”' if thais_quest_orentius03b and not thais_quest_orentius03c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do if he refuses to release the corpses?”')
                jump thais_quest_orentius03c
            '“I can already tell you this and that about the village.”' if helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump thais_quest_orentius04alt
            '“I’ll be back once I learn anything.”' if not helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back once I learn anything.”')
                jump thais_quest_orentius04

    label thais_quest_orentius03c: #“What will you do if he refuses to release the corpses?”
        $ thais_quest_orentius03c = 1
        menu:
            'In her green eyes you find an unwavering confidence. “I’ll take the matter into my own hands.”
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03d
            '“You forgot to mention my reward.”' if not thais_quest_orentius03a:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You forgot to mention my reward.”')
                jump thais_quest_orentius03a
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03b
            '“What will you do if he refuses to release the corpses?”' if thais_quest_orentius03b and not thais_quest_orentius03c:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do if he refuses to release the corpses?”')
                jump thais_quest_orentius03c
            '“I can already tell you this and that about the village.”' if helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it.”')
                jump thais_quest_orentius04alt
            '“I’ll be back once I learn anything.”' if not helvius_about_orentius1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back once I learn anything.”')
                jump thais_quest_orentius04

    label thais_quest_orentius04:
        menu:
            'You stand up and take another look at the seagull, still unaware of the danger. The boy is just about to jump.
            '
            'I let the kid have some fun.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the kid have some fun.')
                menu:
                    'The kid grasps the creature and lets out a triumphant cry, holding the bird as it squawks in panic and flaps its wings. In a few heartbeats, the creature’s neck is hanging at an unnatural angle.
                    \n\nHe raises the seagull above his head, waiting for {color=#f6d6bd}the mayor’s{/color} approving nod, then takes his prey away, whistling.
                    '
                    'I head to the square.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the square.')
                        jump howlersdellsquaafterinteraction01
            'I shout: “Don’t touch it, it’s dirty!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout: “Don’t touch it, it’s dirty!”')
                $ achievement_animalssavedpoints += 1
                menu:
                    'The bird looks around and, once it notices the moving shadow, flaps its wings in panic, running into the water. “Oh, come on,” the boy yells toward you, observing the creature as it flies away. He puts his fists on his sides, but once he notices the mayor, he strides away angrily.
                    '
                    'I head to the square.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the square.')
                        jump howlersdellsquaafterinteraction01

    label thais_quest_orentius04alt:
        menu:
            '“You waste no time, I see,” {color=#f6d6bd}Thais’{/color} voice is warm, but you both look toward the seagull, still unaware of the danger. The boy is just about to jump.
            '
            'I let the kid have some fun.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the kid have some fun.')
                menu:
                    'The kid grasps the creature and makes a triumphant cry, holding the bird as it squawks in panic and flaps its wings. In a few heartbeats, the creature’s neck is hanging at an unnatural angle.
                    \n\nHe raises the seagull above his head, waiting for {color=#f6d6bd}the mayor’s{/color} approving nod, then takes his prey away, whistling.
                    \n\n{color=#f6d6bd}Your companion{/color} lets out a chuckle and leans away, resting against the inn’s wall with crossed arms. “So, did you manage to get in touch with {color=#f6d6bd}the priest{/color}?”
                    '
                    '“Won’t happen. I can try to gain the locals’ trust, but I doubt {color=#f6d6bd}Orentius{/color} will listen to reason.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Won’t happen. I can try to gain the locals’ trust, but I doubt {color=#f6d6bd}Orentius{/color} will listen to reason.”')
                        jump howlersdellorentiusmagicupdates02
            'I shout: “Don’t touch it, it’s dirty!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout: “Don’t touch it, it’s dirty!”')
                $ achievement_animalssavedpoints += 1
                menu:
                    'The bird looks around and, once it notices the moving shadow, flaps its wings in panic, running into the water. “Oh, come on,” the boy yells toward you, observing the creature as it flies away. He puts his fists on his sides, but once he notices the mayor, he strides away angrily.
                    \n\n{color=#f6d6bd}Your companion{/color} gives you a puzzled look and leans forward, resting her shoulders on her leg. “So, did you manage to get in touch with {color=#f6d6bd}the priest{/color}?”
                    '
                    '“Won’t happen. I can try to gain the locals’ trust, but I doubt {color=#f6d6bd}Orentius{/color} will listen to reason.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Won’t happen. I can try to gain the locals’ trust, but I doubt {color=#f6d6bd}Orentius{/color} will listen to reason.”')
                        jump howlersdellorentiusmagicupdates02

label howlersdellorentiusmagicupdatesALL:
    label howlersdellorentiusmagicupdates01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}White Marshes{/color}...”')
        show areapicture howlersdellbehindinn01 at basicfade
        hide howlersdellsquareutensils
        $ questionpreset = 0
        if thais_quest_orentius_betrayal_willadmit and not thais_quest_orentius_betrayal_admitted:
            menu:
                'She nods. “Let’s move to a quiet spot.” Stepping away, you wonder how to explain your actions, and take a look around. The guards keep their distance.
                \n\nYou start to speak before you reach the bench.
                '
                '“{color=#f6d6bd}Helvius{/color}, the mayor of {color=#f6d6bd}White Marshes{/color}, knows about your scheme. His tribe will be ready to push back any attack.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Helvius{/color}, the mayor of {color=#f6d6bd}White Marshes{/color}, knows about your scheme. His tribe will be ready to push back any attack.”')
                    $ thais_quest_orentius_betrayal_admitted = 1
                    $ thais_bigmad = 1
                    $ thais_quest_all_cancelled = 1
                    menu:
                        'She stops, but doesn’t turn around. You look at the back of her head, noticing that the graying of her hair mercilessly progresses, and will soon catch up with her years. “Because of you.”
                        '
                        '“I couldn’t allow you to sink the village in blood.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I couldn’t allow you to sink the village in blood.”')
                            $ thais_friendship -= 15
                            $ howlersdell_reputation -= 2
                            menu:
                                'You wait in silence for her response, but after a few breaths, she simply walks by you. Before she enters the inn, she gestures for the guards to come closer, and after a few words, they give you angry glances, but don’t approach you.
                                '
                                'I guess that’s the end of that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess that’s the end of that.')
                                    jump howlersdellsquaafterinteraction01
                        '“Trust me, I have a plan. I’m going to fix this on my own.”' if not orentius_met:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Trust me, I have a plan. I’m going to fix this on my own.”')
                            $ thais_friendship -= 12
                            $ howlersdell_reputation -= 1
                            menu:
                                'You wait in silence for her response, but after a few breaths, she simply walks by you. She mentions something to {color=#f6d6bd}Eryx{/color}, who gives you an angry look, then enters the inn.
                                '
                                'I guess that’s the end of that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess that’s the end of that.')
                                    jump howlersdellsquaafterinteraction01
                        '“I had a plan, I was going to fix this on my own. But I failed.”' if orentius_met and not whitemarshes_nomoreundead:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had a plan, I was going to fix this on my own. But I failed.”')
                            $ thais_friendship -= 14
                            $ howlersdell_reputation -= 2
                            menu:
                                'You wait in silence for her response, but after a few breaths, she simply walks by you. She mentions something to {color=#f6d6bd}Eryx{/color}, who gives you an angry look, then enters the inn.
                                '
                                'I guess that’s the end of that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess that’s the end of that.')
                                    jump howlersdellsquaafterinteraction01
                        '“Yes.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes.”')
                            $ thais_friendship -= 10
                            $ howlersdell_reputation -= 1
                            menu:
                                'You wait in silence for her response, but after a few breaths, she simply walks by you. Without addressing anyone, she enters the inn, but a few of her children give you curious glances.
                                '
                                'I guess that’s the end of that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess that’s the end of that.')
                                    jump howlersdellsquaafterinteraction01
        elif orentius_met and not whitemarshes_nomoreundead:
            menu:
                'She nods. “Let’s move to a quiet spot.” Stepping away, you wonder how to explain your actions. You start to speak before you reach the bench.
                '
                '“I managed to meet with {color=#f6d6bd}Orentius{/color}, tried to convince him to stop his rituals. I failed. I doubt I’ll ever be allowed to speak with him again, especially since the villagers now see me as an enemy of theirs.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I managed to meet with {color=#f6d6bd}Orentius{/color}, tried to convince him to stop his rituals. I failed. I doubt I’ll ever be allowed to speak with him again, especially since the villagers now see me as an enemy of theirs.”')
                    $ thais_quest_all_cancelled = 1
                    $ quest_orentius = 3
                    $ renpy.notify("Quest completed: Orentius, the Necromancer")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
                    menu:
                        'She turns around. At first, her eyes shine from anger, but she then lets out a sigh. “You trusted yourself too much, and placed a burden not only on {i}my{/i} shoulders. At least learn your lesson from all of this.”
                        '
                        '“Next time, I’ll be more prepared.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Next time, I’ll be more prepared.”')
                            $ thais_friendship -= 4
                            $ howlersdell_reputation -= 1
                            $ custom1 = "She meets your eyes and scoffs, then leads you back to the square. “Don’t be so full of yourself. Those who pursue great results can’t be too proud to ask for assistance when something outgrows them. Well,” she sits down at the table, “I’ve nothing else I need help with. It’s time for my village to begin winter preparations.”"
                            jump howlersdellthaisafterquestionsALL3
                        '“I would do better sticking to you plan.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I would do better sticking to you plan.”')
                            $ thais_friendship -= 2
                            $ howlersdell_reputation -= 1
                            $ custom1 = "She meets your eyes and nods with approval, then leads you back to the square. “For whatever reason, people learn this simple fact only {i}after{/i} they burn themselves with their own schemes. Even my own tribe. Well,” she sits down at the table, “I’ve nothing else I need help with. It’s time for us to prepare for winter.”"
                            jump howlersdellthaisafterquestionsALL3
        else:
            menu:
                '“Let’s take a look at the creek, shall we?” After a few moments, you take a place next to her on the bench, once again surrounded by her rose perfumes.
                '
                '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                    jump thais_quest_orentius03dver02
                '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                    jump thais_quest_orentius03bver02
                '“I’m ready to tell you what I’ve learned in the village.”' if quest_orentius_thais_description02 and not thais_quest_orentius02reported and not quest_orentius_thais_description03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                    jump howlersdellorentiusmagicupdates02
                '“Let’s talk about our allies.”' if (quest_orentius_thais_description03 and quest_orentius_thais_description03a01) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a06) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a07):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                    jump howlersdellorentiusmagicupdates03
                'So far, I’ve gathered no allies to our cause. (disabled)' if quest_orentius_thais_description03 and not quest_orentius_thais_description03a01 and not quest_orentius_thais_description03a06 and not quest_orentius_thais_description03a07:
                    pass
                '“I’m going to take care of this soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to take care of it soon.”')
                    $ custom1 = "“I can’t wait,” she stands up and leads you back to your usual table."
                    jump howlersdellthaisafterquestionsALL3

    label thais_quest_orentius03dver02:
        $ thais_quest_orentius03d = 1
        menu:
            '“The people of {color=#f6d6bd}White Marshes{/color} always kept to themselves, but now we’ve got no clue what’s going on there. It’s {i}possible{/i} that they had no other choice but to seek help in dark magic, but if so, they should have abandoned it years back. Maybe they’re building an army, right under our noses? Someone needs to get to the bottom of this, and they won’t trust a soul {i}who does ne sound like a traveler,{/i}” she mockingly switches to her tribe’s accent.
            \n\n“Oh, and awakening dead shells is {i}very, very bad{/i},” she adds with a chuckle, but it sounds a bit different than usual.
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03dver02
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03bver02
            '“I’m ready to tell you what I’ve learned in the village.”' if quest_orentius_thais_description02 and not thais_quest_orentius02reported and not quest_orentius_thais_description03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                jump howlersdellorentiusmagicupdates02
            '“Let’s talk about our allies.”' if (quest_orentius_thais_description03 and quest_orentius_thais_description03a01) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a06) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a07):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                jump howlersdellorentiusmagicupdates03
            'So far, I’ve gathered no allies to our cause. (disabled)' if quest_orentius_thais_description03 and not quest_orentius_thais_description03a01 and not quest_orentius_thais_description03a06 and not quest_orentius_thais_description03a07:
                pass
            '“I’m going to take care of this soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to take care of it soon.”')
                $ custom1 = "“I can’t wait,” she stands up and leads you back to your usual table."
                jump howlersdellthaisafterquestionsALL3

    label thais_quest_orentius03bver02:
        $ thais_quest_orentius03b = 1
        menu:
            'She waves it off. “I didn’t pay any attention to him back in the day. His tribe had a regular mayor, whatever her name was. One day he revealed himself to be {i}Wright’s prophet{/i} and somehow convinced his tribe to follow him. I don’t think he’s left his village ever since.”
            '
            '“Explain why you want to interfere.”' if not thais_quest_orentius03d:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain why you want to interfere.”')
                jump thais_quest_orentius03dver02
            '“What can you tell me about {color=#f6d6bd}Orentius{/color}?”' if not thais_quest_orentius03b:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about {color=#f6d6bd}Orentius{/color}?”')
                jump thais_quest_orentius03bver02
            '“I’m ready to tell you what I’ve learned in the village.”' if quest_orentius_thais_description02 and not thais_quest_orentius02reported and not quest_orentius_thais_description03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                jump howlersdellorentiusmagicupdates02
            '“Let’s talk about our allies.”' if (quest_orentius_thais_description03 and quest_orentius_thais_description03a01) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a06) or (quest_orentius_thais_description03 and quest_orentius_thais_description03a07):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to tell you what I’ve learned in the village.”')
                jump howlersdellorentiusmagicupdates03
            'So far, I’ve gathered no allies to our cause. (disabled)' if quest_orentius_thais_description03 and not quest_orentius_thais_description03a01 and not quest_orentius_thais_description03a06 and not quest_orentius_thais_description03a07:
                pass
            '“I’m going to take care of this soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to take care of it soon.”')
                $ custom1 = "“I can’t wait,” she stands up and leads you back to your usual table."
                jump howlersdellthaisafterquestionsALL3

    label howlersdellorentiusmagicupdates02:
        $ thais_quest_orentius02reported = 1
        $ thais_friendship += 1
        $ quest_orentius_thais_description03 = "I was asked to speak with the {i}leaders{/i} of other settlements and find some allies willing to join our efforts."
        $ minutes += 5
        $ renpy.notify("Journal updated: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        menu:
            'After you give her the overview of the situation, she asks you for a minute to collect her thoughts. Resting in the cool wind, she keeps staring in the distance. Once she speaks, you catch no hint of hesitation in her voice.
            \n\n“In such a case, avoid meeting with {color=#f6d6bd}Orentius{/color}. It’s better for his people to not know how determined you are to stop him. Instead, carry on with your general patrol route, and speak with the leaders of other settlements, at least those who are willing to listen. Tell them we need to unite our forces to enter {color=#f6d6bd}White Marshes{/color} and force the necromancer to release the awoken. I’ll handle most of the obstacles, but I need at least one tribe to join me. You’re the one who’ll lead the fighters - we’d rather avoid bloodshed anyway, and you know the bogs better than any of our hunters.”
            \n\nShe adjusts her purple dress, as if she’s just finished a meal. “Once you find someone, come here and speak to me, ideally in the morning. We’ll begin our preparations.”
            '
            '“Very well. I’ll prepare myself for a difficult day.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll prepare myself for a difficult day.”')
                $ custom1 = "“I’m sure you will,” she stands up, her voice absent. After a few steps, you return to your usual table."
                jump howlersdellthaisafterquestionsALL3
            '“Wouldn’t it be better to abstain from violence altogether? Any attack will end up grim, no matter how carefully executed.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wouldn’t it be better to abstain from violence altogether? Any attack will end up grim, no matter how carefully executed.”')
                menu:
                    '“If you want to avoid unnecessary violence,” she stands up slowly, her tone having run out of patience, “find me two, maybe even three groups of fighters. The more of us there are, the dumber it will be for the defenders to oppose us.”
                    '
                    '“Fine. I’ll ask around.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll ask around.”')
                        $ custom1 = "“I’m sure you will,” she says absently. After a few steps, you return to your usual table."
                        jump howlersdellthaisafterquestionsALL3
                    '“So you want me to organize a raid? I can’t agree to this.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want me to organize a raid? I can’t agree to this.”')
                        $ quest_orentius_thais_description10 = "I decided to refuse to collaborate with {color=#f6d6bd}Thais{/color}."
                        $ renpy.notify("Journal updated: Orentius, the Necromancer")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
                        $ thais_quest_all_cancelled = 1
                        $ thais_friendship -= 5
                        $ custom1 = "“So you’d rather put everyone in danger, than gain my trust and save them?” Despite her fragile shell, she now towers over you. Her scornful gaze makes you look away. “Very well, our collaboration ends here. Come, but don’t waste my time.”\n\nAfter a few steps, you return to your usual table."
                        jump howlersdellthaisafterquestionsALL3

    label howlersdellorentiusmagicupdates03:
        $ whitemarshes_attack_numberofallies = 0
        if quest_orentius_thais_description03a01 and not peltnorth_ban_perm:
            $ whitemarshes_attack_numberofallies += 1
        if quest_orentius_thais_description03a06:
            $ whitemarshes_attack_numberofallies += 1
        if quest_orentius_thais_description03a07 and not banditshideout_banned:
            $ whitemarshes_attack_numberofallies += 1
        if quest_orentius_thais_description03a01 and peltnorth_ban_perm:
            $ custom1 = "\n{color=#6a6a6a}Since you’ve been banned from Pelt, the hunters won’t join you.{/color}"
        elif quest_orentius_thais_description03a01 and not peltnorth_ban_perm:
            $ custom1 = "\nThe hunters from {color=#f6d6bd}Pelt{/color} will join you."
        else:
            $ custom1 = ""
        if quest_orentius_thais_description03a06:
            $ custom2 = "\n{color=#f6d6bd}Severina{/color} promised to help you."
        else:
            $ custom2 = ""
        if quest_orentius_thais_description03a07 and banditshideout_banned:
            $ custom3 = "\n{color=#6a6a6a}Since you’ve sabotaged Glaucia’s efforts, she won’t join you.{/color}"
        elif quest_orentius_thais_description03a07 and not banditshideout_banned:
            $ custom3 = "\n{color=#f6d6bd}Glaucia{/color} agreed to work with you."
        else:
            $ custom3 = ""
        if not whitemarshes_attack_numberofallies:
            $ custom4 = "{color=#6a6a6a}So far, you’ve gathered no allies.{/color}"
        elif whitemarshes_attack_numberofallies == 1:
            $ custom4 = "Having only one ally, the raid would present a great challenge."
        elif whitemarshes_attack_numberofallies == 2:
            $ custom4 = "With two allies on your side, you’ll outnumber the village defenses."
        else:
            $ custom4 = "With three allies on your side, you’ll take the village by storm."
        menu:
            '[custom4][custom1][custom2][custom3]
            \n\nYou should begin your preparations in the early morning hours - preferably right after you wake up.
            \n\nYou should expect an exhausting evening - you need to be in good shape.
            '
            '“Let’s set off this evening. I’ll travel to our allies, tell them to gather here.”' ( condition="whitemarshes_attack_numberofallies and pc_hp >= 3 and quarters < 40" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s set off this evening. I’ll travel to our allies, tell them to gather here.”')
                jump howlersdellorentiusmagicupdates03a
            'I have no allies other than Thais. (disabled)' ( condition="not whitemarshes_attack_numberofallies" ):
                pass
            'I’m too tired to take part in a raid. (Required vitality: 3) (disabled)' ( condition="pc_hp < 3" ):
                pass
            'It’s too late to start organizing the raid. (disabled)' ( condition="quarters >= 40" ):
                pass
            '“I’ll tell you when I’m ready.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you when I’m ready.”')
                $ custom1 = "“I can’t wait,” she stands up and leads you back to your usual table."
                jump howlersdellthaisafterquestionsALL3

    label howlersdellorentiusmagicupdates03a:
        menu:
            '“We don’t have much time,” she straightens up and adjusts her dress. “I’ll handle the supplies, shelters, torches. With the help of your {i}friends{/i}, we can get rid of the necromancer this very day.”
            \n\nShe looks into your eyes, then puts on a wide, innocent smile. “I’m counting on you, [pcname]. Safe travels.”
            \n\nBefore you respond, she heads toward the closest guards, leaving behind the strong scent of roses.
            '
            'Time to prepare {color=#f6d6bd}[horsename]{/color}. I have a long road ahead of me.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to prepare {color=#f6d6bd}%s{/color}. I have a long road ahead of me.' %horsename)
                show areapicture howlersdellfull at basicfade
                hide howlersdellsquareutensils
                jump whitemarshes_attacked01
            'Time to prepare {color=#f6d6bd}[horsename]{/color}. There’s a long road ahead of us.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to prepare {color=#f6d6bd}%s{/color}. There’s a long road ahead of us.' %horsename)
                show areapicture howlersdellfull at basicfade
                hide howlersdellsquareutensils
                jump whitemarshes_attacked01

label howlersdellthais_about_nomoreundeadALL:
    label howlersdellthais_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The necromancer of {color=#f6d6bd}White Marshes{/color} has no more control over the village, and his {i}laborers{/i} are gone.”')
        $ thais_about_nomoreundead = 1
        if quest_orentius_thais_description00 and not thais_quest_orentius_betrayal_admitted:
            $ thais_friendship -= 1
            $ custom1 = "titters, but her harsh, green eyes look around as she lowers her voice. “So you’ve put all my preparations to waste,” she leans away, adjusting her cape. “I’ll let my neighbors know. They’ll gladly hear about your {i}resourcefulness{/i}.”"
        elif quest_orentius_thais_description00 and thais_quest_orentius_betrayal_admitted:
            $ thais_friendship += 0
            $ custom1 = "titters, but her harsh, green eyes look around as she lowers her voice. “At least your betrayal didn’t go to waste. Fine.” She leans away, adjusting her cape. “I’ll let my neighbors know. They’ll gladly hear about your {i}resourcefulness{/i}.”"
        elif thais_bigmad:
            $ custom1 = "lowers her voice, staring at you with her harsh, green eyes. “Just don’t tell me you expect my gratitude,” she leans away, adjusting her cape. “I’ll let my neighbors know.”"
        else:
            $ thais_friendship += 1
            $ custom1 = "gives you a curious glance. Her green eyes are keen, but you don’t find much joy in them. “I’m used to being the one who has to fix everything around here, yet you’ve managed to stay a few steps ahead of me,” she lets out a titter. “I’ll let my neighbors know. They’ll {i}gladly{/i} hear about your talents!”"
        $ howlersdell_reputation += 2
        $ questionpreset = "thais1"
        menu:
            'You describe your conversation, omitting how you managed to meet with {color=#f6d6bd}Orentius{/color} in the first place. {color=#f6d6bd}Thais{/color} [custom1]
            '
            '(thais1 set)':
                pass

    label howlersdellthais_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The necromancer of {color=#f6d6bd}White Marshes{/color} is dead, and his {i}laborers{/i} will soon start to roam through these woods. The bogs should be avoided.”')
        $ thais_about_nomoreundead = 2
        if quest_orentius_thais_description00 and not thais_quest_orentius_betrayal_admitted and not thais_bigmad:
            $ thais_friendship -= 3
            $ custom1 = "gives you a long look, with her lips forming an awkward smile. Her harsh, green eyes look around as she lowers her voice. “Why would you try this without my help? We could have solved all this without any bloodshed.” Her words are close to a hiss. “You wasted all my preparations and threw my lands into chaos.” She leans away, adjusting her cape. “I’ll let my neighbors know. I can’t promise they’ll be happy about all this.”"
        elif quest_orentius_thais_description00 and thais_quest_orentius_betrayal_admitted:
            $ thais_friendship -= 2
            $ custom1 = "gives you a long look, with her lips forming an awkward smile. Her harsh, green eyes look around as she lowers her voice. “So first you sabotage my plans, then you throw my lands into chaos. Hopeless, just hopeless.” She leans away, adjusting her cape. “I’ll let my neighbors know. I can’t promise they’ll be happy about all this.”"
        elif thais_bigmad:
            $ thais_friendship -= 2
            $ custom1 = "gives you a long look, with her lips forming an awkward smile. Her harsh, green eyes look around as she lowers her voice. “Not only did you prove to be a piece of shit, you now throw my lands into chaos. Hopeless, just hopeless.” She leans away, adjusting her cape. “I’ll let my neighbors know. I can’t promise they’ll be happy about all this.”"
        else:
            $ thais_friendship -= 0
            $ custom1 = "gives you a long look, with her lips forming an awkward smile. Her green eyes are keen, and you don’t find much anger in them. “I’m used to being the one who has to fix everything around here, yet you’ve managed to stay a few steps ahead of me,” she sighs. “I’d rather avoid the violence that the undead will bring us, but I’m sure it’s better for this disaster to happen now, rather then later. I’ll let my neighbors know. We’ll be prepared.”"
        $ howlersdell_reputation += 1
        $ questionpreset = "thais1"
        menu:
            'You describe {color=#f6d6bd}Orentius’{/color} fate, unable to hide your responsibility for the village’s collapse. {color=#f6d6bd}Thais{/color} [custom1]
            '
            '(thais1 set)':
                pass

label thais_about_orentius_banished01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will happen to {color=#f6d6bd}Orentius{/color} now that you have him locked up here?”')
    $ thais_about_orentius_banished = 1
    $ questionpreset = 0
    menu:
        '“I’d like to at least {i}speak{/i} with him before I make any judgment.” She glances toward the druids’ part of the village. “The elders look after him in his sleep, but can’t make any promises. I’m not sure if he’s drinking any water.” She meets your eyes with a playful smile. “We don’t keep prisoners, nor torture anyone, but his crimes are beyond redemption. I’ll likely vote for a weaponless banishment.”
        \n\nYou nod. Knowing the northern roads, even on the other side of {color=#f6d6bd}Hag Hills{/color}, you’ve no doubt that such a punishment would be no different than a death sentence, especially for an elder.
        '
        'In {color=#f6d6bd}Hovlavan{/color}, they wouldn’t be so merciful.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- In {color=#f6d6bd}Hovlavan{/color}, they wouldn’t be so merciful.')
            jump howlersdellthaisafterquestions
