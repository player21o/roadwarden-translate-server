label creeksfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ creeks_traveling = 2
    if creeks_road_helped:
        $ custom1 = "That’s a nice ibex."
    else:
        $ custom1 = "Caught any squirrels?"
    menu:
        'You follow the trail of shouts and laughter. Seven people, about twenty years old each, are gathered at the wooden bridge, leaning against the railing, bathing in the stream, lying on the grass. Pieces of clothing - made of fur and leather - are spread around, next to cudgels and throwing clubs.
        \n\nOnce the sound of hooves manages to break through the chattering, the curious, young eyes, untouched by wartime, turn toward you, and an excited whisper spreads. The shells are proudly displayed, and the confident smiles are both inviting and challenging.
        \n\n“How’s water,” {color=#f6d6bd}the hunter{/color} greets his tribesfolk while stepping on the logs. “Gentle and warm,” says a man resting on his friend’s shoulder. “[custom1]”
        \n\nThere are paths leading in many directions, but the main road will take you uphill.
        '
        'Awkward. As I walk past the naked people, I look at the watchtower.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Awkward. As I walk past the naked people, I look at the watchtower.')
            menu:
                'The hills around you form a valley, most likely spread from here to the very coast. The main spring supplying the creek is cutting through the walls, high above you. The bridge is young and robust, enduring the weight of the wanderers silently, as well as your mount and belongings.
                \n\nA single person is waving to you from the tower, but the roof makes it difficult for you to see what they look like. {color=#f6d6bd}Your guide{/color} speaks with enthusiasm. “We keep a soul there at all times, friend. Unless the night’s so dark one can’t even see the gate. It’s not hard work, but it’s {i}booooring{/i},” he says in a sing-song voice.
                '
                'I follow the twisting path.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the twisting path.')
                    jump creeksfirsttime02
        'There’s no reason for me to be embarrassed. I look at them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no reason for me to be embarrassed. I look at them.')
            $ creeks_youth_lookedat = 1
            if cleanliness < 1:
                $ custom1 = "greet you with kind nods, but you notice that the ones standing on the bridge are holding their breath and leaning away. You notice your own scent, and once you step off the logs, {color=#f6d6bd}the hunter{/color} chuckles. “Seeking warmth, aye? Don’t worry, you can always wash yourself in here.”"
            elif cleanliness_clothes_torn and not item_fancyclothes:
                $ custom1 = "greet you with kind nods, but you notice that their eyes are focused on your rugged clothes. Once you step off the bridge, {color=#f6d6bd}the hunter{/color} chuckles. “Seeking warmth, aye? Don’t worry, we’re not {i}that{/i} obsessed with outfits,” the wolf’s head bounces as he speaks."
            elif cleanliness_clothes_blood and not item_fancyclothes:
                $ custom1 = "greet you with kind nods, but you notice that their eyes are focused on the blood covering your clothes. Once you step off the bridge, {color=#f6d6bd}the hunter{/color} chuckles. “Seeking warmth, aye? Don’t worry, you can always wash your things in here.”"
            else:
                $ custom1 = "greet you with smiles and nods, and the ones you walk by on the bridge shift their stances, allowing you to see even more. Once you step off the logs, {color=#f6d6bd}the hunter{/color} chuckles. “Seeking warmth, aye? The youth here think more ‘bout wooing than traveling and beasts, but that’s good, means they’re healthy. They’re vain as birds, though, you won’t find much to talk ‘bout with them.”\n\nAs you look behind, you’re not so sure he’s right."
            if appearance >= 2:
                $ creeks_reputation += 1
            elif appearance >= 4:
                $ creeks_reputation += 2
            menu:
                'The light dances on wet hair, both on their heads and crotches, luring your eyes just as much as the revealed chests and muscular arms. You’ve interrupted not just their bath - the soul who’s speaking with {color=#f6d6bd}your guide{/color} is embracing another man as he’s sitting behind him, while one of the women is keeping her arm around the waist of yet another man.
                \n\nYou hardly see any wounds or marks caused by sickness - the harshest days of this group are still ahead. As you move your eyes from one person to another, they [custom1]
                '
                'I nod to the group, then follow the man.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to the group, then follow the man.')
                    jump creeksfirsttime02

    label creeksfirsttime02:
        show areapicture creeks00b at basicfade
        menu:
            'The palisade is as tall as trees, but being placed on the top of the crags makes it look impassable. “Hwat? Hwy’s the gate closed?” {color=#f6d6bd}The hunter{/color} turns to the watchtower and repeats his question, only louder. “Maybe call {color=#f6d6bd}Elah{/color}? Too blind to see we have a guest, aye?”
            \n\nA hardly visible guard with a female voice leans from the tower. “He’s coming, howler, relax!” Her shouts hint of no patience toward him. “The youth dine in the woods after the bath, hwy wouldn’t we close?”
            \n\n{color=#f6d6bd}The man{/color} glances at you.
            '
            'I wait patiently.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait patiently.')
                menu:
                    'They argue for a good minute, and you realize it’s just friendly banter. You don’t recognize some of their jokes, referencing events and people you’ve never met. Their accent resembles {color=#f6d6bd}Foggy’s{/color}, but is thicker and you’ll have to get used to it.
                    \n\n“Don’t let {color=#f6d6bd}Efren{/color} talk you to death, friend,” the soul from the tower shouts to you as the gate opens.
                    '
                    'We enter the village.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We enter the village.')
                        jump creeksfirsttime03
            '“Who’s {color=#f6d6bd}Elah{/color}?” I whisper.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who’s {color=#f6d6bd}Elah{/color}?” I whisper.')
                $ elah_efren_siblings = 1
                menu:
                    '“Just my brother,” he gestures for you to ignore it. “And I’m {color=#f6d6bd}Efren{/color}, so thanks to our parents, folks keep mistaking our names. But {color=#f6d6bd}Elah{/color} has a stick in his ass, and is as boring and nagging as a legless donkey.”
                    \n\nThe soul from the tower hides again, and the gate opens.
                    '
                    'We enter the village.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- We enter the village.')
                        jump creeksfirsttime03

    label creeksfirsttime03:
        show areapicture creeks00c at basicfade
        $ description_elah_efren00 = "The two brothers from {color=#f6d6bd}Creeks{/color} who speak with me the most. {color=#f6d6bd}Efren{/color} is a hunter, {color=#f6d6bd}Elah{/color} is a carpenter."
        if creeks_road_helped:
            $ custom1 = "A slightly overweight man is standing in front of the building, with open arms. “Welcome to {color=#f6d6bd}Creeks{/color}, friend!” His voice and eyes are gentle, but there’s vigor in his stance and gestures. “{color=#f6d6bd}Efren{/color} was meant to hunt, but I see he brought not one, but {i}two{/i} unusual creatures.” {color=#f6d6bd}The hunter{/color} rolls his eyes. “Don’t embarrass us with this prattle.” He raises his voice and fills it with bitterness, addressing no soul in particular. “And maybe ask {i}someone{/i} to help us with this ibex. It’s our shared catch,” he points at you.\n\n“Now I want to know to whom we are grateful,” {color=#f6d6bd}Elah{/color} nods toward you."
        elif creeks_road_triedtohelp:
            $ custom1 = "A slightly overweight man is standing in front of the building, with open arms. “Welcome to {color=#f6d6bd}Creeks{/color}, friend!” His voice and eyes are gentle, but there’s vigor in his stance and gestures. “{color=#f6d6bd}Efren{/color} was meant to hunt, but I see he brought a {i}very{/i} unusual creature.” {color=#f6d6bd}The hunter{/color} rolls his eyes. “Don’t embarrass us with this prattle,” he then raises his voice. “I almost brought us an ibex, but this traveler and I got outnumbered. Long story. But we tried!”\n\n{color=#f6d6bd}Elah’s{/color} smile widens. “Now I’m even more interested in who’s the one willing to assist strangers in the middle of nohwere.”"
        else:
            $ custom1 = "A slightly overweight man is standing in front of the building, with open arms. “Welcome to {color=#f6d6bd}Creeks{/color}, friend!” His voice and eyes are gentle, but there’s vigor in his stance and gestures. “{color=#f6d6bd}Efren{/color} was meant to hunt, but I see he brought a {i}very{/i} unusual creature.” {color=#f6d6bd}The hunter{/color} rolls his eyes. “Don’t embarrass us with this prattle,” he then raises his voice. “I almost brought us an ibex, but this traveler was no help. Long story. At least {i}I{/i} tried.”\n\n{color=#f6d6bd}Elah’s{/color} smile gets replaced by a raised eyebrow. “I trust you made the right decision... Friend.”"
        menu:
            'The sparse clumps of grass survive only on the edges of this spacious yard. The few onlookers wear working clothes, suitable for their hard labor - they’re carrying tools, planks, and logs. You’re next to a large building of unusual shape, either a temple or a house of gathering. It makes you think of a cabin that’s been getting larger over the course of the years, with the section in the middle being darker and more crude than the outer ones.
            \n\n[custom1]
            '
            'While I introduce myself, I observe him more closely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- While I introduce myself, I observe him more closely.')
                if foggylake_firsttime+2 < day:
                    $ custom1 = " We’ve heard of you from {color=#f6d6bd}Foggy{/color}."
                else:
                    $ custom1 = ""
                $ at_activate = 1
                $ at = 0
                menu:
                    'Being close to thirty years old, he’s one of the older souls around. Just like the other villagers, he has clothes made of animals, not plants. The leather pants and jacket are humble, but the shoulder cape, reaching from his neck to elbows, used to belong to a yellow elk. His brown skin is darker than that of a farmer, and as you look at the outreached hands, they carry the marks of being cut by tools.
                    \n\n“And I’m {color=#f6d6bd}Elah{/color}, the carpenter![custom1]” He takes a step toward the fruit trees and invites you to move forward. Like most men in the village, he’s cleanly shaved. “How ‘bout I show you the rest of the village? It may be humble, but it’s as beautiful as a blue starling.”
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“Thanks, {color=#f6d6bd}Elah{/color}. That sounds lovely.”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Thanks, {color=#f6d6bd}Elah{/color}. That sounds lovely.”')
                        $ at_activate = 0
                        $ at = 0
                        $ custom1 = "As he grins, you notice his unusually white teeth. He moves with heavy, but enthusiastic steps. “It won’t really take that long, but we have quite a view!”"
                        $ elah_friendship += 2
                        jump creeksfirsttime04yes
                    '“Oh, I already had an opportunity to see some of your {i}beauties{/i}.”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Oh, I already had an opportunity to see some of your {i}beauties{/i}.”')
                        $ at_activate = 0
                        $ at = 0
                        $ custom1 = "It takes a moment before {color=#f6d6bd}Elah{/color} figures out what you mean, but {color=#f6d6bd}Efren’s{/color} laughter is enough of a hint. The carpenter puts a hand on his bulging stomach and playfully taps his fingers. “Aye, the youth want to be longed for, but don’t find many {i}adventures{/i} in their small group. Our older generations see them as our offspring, not bedfellows. At least the bloodcrossing isn’t an issue, yet.”"
                        $ elah_friendship += 1
                        $ efren_friendship += 1
                        $ creeks_reputation += 1
                        $ creeks_reasonstojoin_hpcknowstruthaboutinbreeding = 1
                        $ minutes += 5
                        jump creeksfirsttime04yes
                    '“...Sure.”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “...Sure.”')
                        $ at_activate = 0
                        $ at = 0
                        show areapicture creeks00h at basicfade
                        $ custom1 = ""
                        $ elah_friendship -= 1
                        $ efren_friendship -= 1
                        $ elah_efren_siblings = 1
                        $ questionpreset = "elah1"
                        $ quarters += 1
                        if creeks_road_helped:
                            menu:
                                'The men wait for you to continue, then look at each other in silence. “Well,” says {color=#f6d6bd}Efren{/color}. “Ye’ve seen some curious places already, no doubt, and much larger ones. Let’s not waste our guest’s time, brother,” he turns to {color=#f6d6bd}Elah{/color}, who adjusts his cloak and leans against a tree.
                                \n\n“I {i}swear{/i},” {color=#f6d6bd}the hunter{/color} suddenly shouts, “I’m not carrying this ibex to the kitchen. Someone call the cooks!” After dropping the carcass on the ground, he springs away, fretting at the blood on his hands.
                                \n\n{color=#f6d6bd}Elah{/color} rubs his hands and lets out a breath. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads behyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass
                        else:
                            menu:
                                'The men wait for you to continue, then look at each other in silence. “Well,” says {color=#f6d6bd}Efren{/color}. “You’ve seen some curious places already, no doubt, and much larger ones. Let’s not waste our guest’s time, brother,” he turns to {color=#f6d6bd}Elah{/color}, who adjusts his cloak and leans against a tree.
                                \n\n“I need to wash off the sweat. Ye know. From {i}risking my life{/i} in the wilderness,” {color=#f6d6bd}Efren{/color} complains to {color=#f6d6bd}the carpenter{/color}, then waves at you. “See you later, friend.”
                                \n\n{color=#f6d6bd}Elah{/color} rubs his hands and lets out a breath. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads beyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass
                    '“I’ve wasted enough time.”' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I have things to take care of.”')
                        $ at_activate = 0
                        $ at = 0
                        show areapicture creeks00h at basicfade
                        $ custom1 = ""
                        $ elah_friendship -= 2
                        $ efren_friendship += 1
                        $ elah_efren_siblings = 1
                        $ questionpreset = "elah1"
                        $ quarters += 1
                        if creeks_road_helped:
                            menu:
                                '{color=#f6d6bd}Efren{/color} laughs and looks at the other man, whose eyes widen. “See? Other folks have no patience for your waste of air,” he shifts the weight to his other leg, gasping from carrying the ibex.
                                \n\n{color=#f6d6bd}The carpenter{/color} mutters something as he adjusts his cloak and leans against a tree, but his voice disappears in the sudden yells of {color=#f6d6bd}the hunter{/color}. “I {i}swear{/i}, I’m not carrying this to the kitchen. Someone call the cooks!” After dropping the carcass on the ground, he springs away, fretting at the blood on his hands.
                                \n\n{color=#f6d6bd}Elah{/color} rubs his hands and lets out a breath. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the main square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads beyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass
                        else:
                            menu:
                                '{color=#f6d6bd}Efren{/color} laughs and looks at the other man, whose eyes widen. “See? Other folks have no patience for your waste of air,” he moves to him and pats his shoulder. “Anyway, {i}I{/i} need to wash off the sweat. Ye know. From {i}risking my life{/i} in the wilderness,” he waves at you. “See you later, friend.”
                                \n\n{color=#f6d6bd}The carpenter{/color} rubs his hands and lets out a breath. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the main square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads beyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass
                    '“Can we talk about the peninsula instead?”' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Can we talk about the peninsula instead?”')
                        $ at_activate = 0
                        $ at = 0
                        show areapicture creeks00h at basicfade
                        $ custom1 = ""
                        $ elah_friendship -= 1
                        $ efren_friendship -= 1
                        $ creeks_reputation -= 1
                        $ elah_efren_siblings = 1
                        $ quarters += 1
                        $ questionpreset = "elah1"
                        if creeks_road_helped:
                            menu:
                                '{color=#f6d6bd}Elah{/color} frowns. “Of course, I didn’t realize you’re busy.” He glances at the other man, who shifts his weight to his other leg, gasping from carrying the ibex. “I guess my brother also has things to take care of.”
                                \n\n“I {i}swear{/i}”, {color=#f6d6bd}the hunter{/color} suddenly yells. “I’m not carrying this to the kitchen. Someone call the cooks!” After dropping the carcass on the ground, he springs away, fretting at the blood on his hands.
                                \n\n{color=#f6d6bd}Elah{/color} rubs his hands. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads beyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass
                        else:
                            menu:
                                '{color=#f6d6bd}Efren{/color} frowns. “Of course, I didn’t realize you’re busy.” He glances at the other man. “My brother and I will help to the best of our ability.”
                                \n\n{color=#f6d6bd}Efren{/color} scoffs. “Don’t involve me in this. {i}I{/i} need to wash off the sweat. Ye know. From {i}risking my life{/i} in the wilderness,” he waves at you. “See you later, friend.”
                                \n\n{color=#f6d6bd}The carpenter{/color} rubs his hands. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the square. The tools you notice are very simple, if not primitive. “So, hwat is it that you look for in our home? There are no more roads beyond our palisades.”
                                '
                                '(elah1 set)':
                                    pass

    label creeksfirsttime04yes:
        if creeks_road_helped:
            $ custom3 = "\n\n“I {i}swear{/i},” interrupts {color=#f6d6bd}the hunter{/color}, “I’m not carrying this ibex to the kitchen. Someone call the cooks!” After dropping the carcass on the ground, he springs away, fretting at the blood on his hands."
        else:
            $ custom3 = "\n\n{color=#f6d6bd}The hunter{/color} gives you an embarrassed look. “Don’t indulge him {i}too much{/i}, friend,” he says without lowering his voice. “He’d be proud of a falling wheelbarrow.”"
        menu:
            '[custom1] [custom3]
            \n\n“Let’s take a stroll, then,” says {color=#f6d6bd}Elah{/color} as he leads you forward. “Your mount can drink at the creek here.”
            '
            '“Come, {color=#f6d6bd}[horsename]{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come, {color=#f6d6bd}%s{/color}.”' %horsename)
                $ quarters += 1
                show areapicture creeks00d at basicfade
                $ oldhava_known = 1
                menu:
                    'You tether your mount to a tree, next to drying laundry. {color=#f6d6bd}Elah{/color} points at the land behind the bridge proudly. “Our newest addition to the village. The hunters grow old, so we are taking steps away from meat and fruits.”
                    \n\nYou spot only two people working in the {i}field{/i}, or rather a large garden covered with cabbages, carrots, onions, and garlic, indistinguishable from the wild plants growing in the woods. On the path between the two halves of the field {color=#f6d6bd}an elderly woman{/color} is sitting on a stool, looking in your direction as if you’re interrupting her contemplation.
                    \n\n“{color=#f6d6bd}Old Hava{/color} there will turn this place into a proper farm, one day. She has li’l strength, but keeps precious memories of her trade.”
                    '
                    '“You lack proper seeds.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You lack proper seeds.”')
                        $ creeks_reasonstojoin_lackingseeds = 1
                        $ description_whitemarshes08 = "{color=#f6d6bd}Efren{/color}, the hunter, believes the local seeds should not be trusted."
                        menu:
                            '“The good ones are expensive,” {color=#f6d6bd}Elah{/color} responds right away, as if it’s a part of a prepared speech, “and we weren’t sure ‘bout our soil. It’s all just a test.” He invites you with a gesture to follow him deeper into the village. “And there are no seeds in {color=#f6d6bd}Gale Rocks{/color}, hwile the folks at {color=#f6d6bd}Howler’s{/color} won’t spare their own, they’d rather force us to buy food from them.”
                            \n\n“There are farmers at {color=#f6d6bd}Hwite Marshes{/color},” adds {color=#f6d6bd}Efren{/color}, “but it’s a dark place. Who knows hwat we would reap after a year.”
                            '
                            '“That’s rough.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s rough.”')
                                jump creeksfirsttime05
                    'I speak quietly. “She seems... austere.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak quietly. “She seems... austere.”')
                        $ description_creeks06 = "I heard that {color=#f6d6bd}Old Hava{/color}, the farmer, doesn’t like being bothered and should be spoken to only when she allows it."
                        menu:
                            '{color=#f6d6bd}Efren{/color} snorts, holding his laughter. “Just be happy you haven’t grown under her. I’m lucky to have my ears, after all the pulling and pinching.”
                            \n\n“Don’t overcolor, she cares a lot,” {color=#f6d6bd}Elah{/color} invites you with a gesture to follow him deeper into the village. “At least ‘bout the {i}quiet{/i} children. Just let her do the talking, the fewer things you say, the fewer reasons for her to get upset.”
                            '
                            '“Yeah, I know the type.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah, I know the type.”')
                                jump creeksfirsttime05

    label creeksfirsttime05:
        show areapicture creeks00e at basicfade
        $ creeks_feast_known = 1
        menu:
            'The bonfire spot is surrounded by logs that were cut into tables and stools. {color=#f6d6bd}Elah{/color} approaches the nearest chair, rubbing its back with his cut hands. “When we share a meal, we do so here, sometimes beneath the stars. You’d have to see it, the flames dance on the walls to the monster roars and crickets.”
            \n\n{color=#f6d6bd}Efren’s{/color} voice also grows in enthusiasm. “Dining at the edge of the forest is something you wouldn’t forget. Unless you {i}can{/i} drink, don’t swallow anything stronger than spoiled ibex milk. The shadows, friend. Terrifying.”
            \n\nYou glance over the wooden buildings. While the walls seem fine, the roofs are primitive, mostly made of planks that are already soggy and bent. There are a few people working on cleaning bark from a log, but the square is mostly quiet, with a few kids observing you from above their toys.
            '
            '“Burning such fires must take a lot of wood.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Burning such fires must take a lot of wood.”')
                menu:
                    '“It’s not something we need to worry ‘bout,” {color=#f6d6bd}Elah{/color} shows you to look around. “We mostly burn hwat’s left after sawing and construction, gathering fuel for a few dozen days.”
                    \n\n“{i}Some{/i} of us think they can learn woodworking all by themselves,” {color=#f6d6bd}Efren{/color} says mockingly. “So we waste {i}a lot{/i} of wood. At least we can roast meat on long sticks as we sit here.”
                    \n\n“Nah, we already have results,” {color=#f6d6bd}the carpenter{/color} moves his hand from the chair to his stomach. “Everything you see here, friend, was built by us and our elders. How about I show you our old forest?”
                    '
                    '“Is it far away?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it far away?”')
                        $ custom2 = "You find the answer right away. "
                        jump creeksfirsttime06
            '“A bit of a fire hazard, isn’t it?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A bit of a fire hazard, isn’t it?”')
                $ description_creeks07 = "The locals practice various types of magic, including water control."
                menu:
                    '{color=#f6d6bd}Efren{/color} bursts into laughter. “Ye don’t know the half of it, friend!”
                    \n\n{color=#f6d6bd}Elah{/color} scowls at him, and his tone is grim. “We did have an accident before, we didn’t expect the sudden gale. But one of the reasons we live among the streams is to put our spellcasters to use,” he looks around, but finds no one to illustrate his point. “Water control is a part of hwat allowed us to survive.”
                    \n\n{color=#f6d6bd}The hunter{/color} moves away, raising his voice. “Still, we keep an eye on the weather. Come, you’ll see hwy the winds bother us.”
                    '
                    'I follow him.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him.')
                        $ custom2 = ""
                        jump creeksfirsttime06
            '“I imagine what such dinners would look like. One big family.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I imagine what such dinners would look like. One big family.”')
                $ elah_friendship += 1
                menu:
                    '{color=#f6d6bd}Elah{/color} flashes you a disarming, white smile. “Yeah, a {i}huge{/i} one, we don’t have any rooms to spare.” He looks at the children as they return to their crude, wooden toys. “They don’t realize yet how small our home is. They’ve hardly seen anyone from the world outside, and the trade occurs at {color=#f6d6bd}Foggy Lake{/color}.”
                    \n\n“And good for them,” {color=#f6d6bd}the hunter{/color} chips in. “They don’t miss much. Other than spouses, we have everything we need, and so far we have plenty of fresh meat. Some of us even too much,” he smirks at {color=#f6d6bd}the carpenter{/color}, who in response turns and walks away.
                    '
                    'I follow him.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him.')
                        $ custom2 = ""
                        jump creeksfirsttime06

    label creeksfirsttime06:
        show areapicture creeks00f at basicfade
        if quest_birdhunting_description07 and foragingground_bird_taken == 1:
            $ custom1 = "two brown boars, a black mouflon, and the runner you recently captured with the foragers. “I just realized, it’s {i}you{/i} who helped our folks at the hunt!” {color=#f6d6bd}Efren{/color}, excited, hits your back, not bothering with your boundaries. “Good job, I’ve heard. It’s much easier to just kill something.”"
        else:
            $ custom1 = "two brown boars and a black mouflon. “And here are our captives!” {color=#f6d6bd}Efren{/color} declares proudly. “I know, it’s still a bit empty, but we’ll crowd it just before winter.”"
        menu:
            '[custom2]You stand between two of the houses, in front of the gate of an animal pen. The walls are made of sharpened trunks, and are as tall as two humans. The captured beasts are tethered by ropes, but have enough freedom to wander and graze - [custom1]
            '
            '“I have some good news for you. I helped {color=#f6d6bd}the boys from Foggy’s{/color} catch a large bird that will soon be brought here.”' if quest_birdhunting_description06 and not quest_birdhunting_description07 and foragingground_bird_taken == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some good news for you. I helped {color=#f6d6bd}the boys from Foggy’s{/color} catch a large bird that will soon be brought here.”')
                $ creeks_reputation += 1
                $ foragers_friendship += 1
                $ minutes += 5
                menu:
                    'While you try to stay to the point, {color=#f6d6bd}Efren{/color} is full of energy. He asks about every detail, from the animal’s size to the way it acted in combat. Your brief answers are met with shouts, echoed by the silent bounces of the wolf’s head.
                    \n\n“It was a brave venture, I’m glad they didn’t try it without you.” {color=#f6d6bd}Elah{/color} gestures for {color=#f6d6bd}the hunter{/color} to drop it. “Thank you for giving us time to prepare.”
                    '
                    '“I was also told to ask for one dragon bone.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was also told to ask for one dragon bone.”')
                        show screen notifyimage( "Quest completed: Bird Hunt.\n+1", "gui/coin2.png")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunt. +1 {image=cointest}{/i}')
                        $ quest_birdhunting_description08 = "I received my reward for delivering the message."
                        $ quest_birdhunting = 2
                        $ coins += 1
                        $ minutes += 5
                        $ efren_friendship += 1
                        $ elah_efren_siblings = 1
                        menu:
                            '“Aye, of course.” {color=#f6d6bd}The carpenter{/color} looks around. “Pay for the messenger... Just give me a minute.” He scurries away, as quickly as his thick legs allow him. “We don’t carry dragons with us,” {color=#f6d6bd}the hunter{/color} explains. “So, how large is the beak? Something like this?” He demonstrates the size with his hands, and for another few minutes showers you with questions.
                            \n\nFinally, the dragon bone finds its place in your hand. “We... We’ll get to the preparations soon,” concludes {color=#f6d6bd}Elah{/color}, sweating. “Did my... brother show you the forest, friend?” He leans against the gate and points at the area behind the palisade.
                            '
                            'I look north.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look north.')
                                jump creeksfirsttime07
                    'I smile. “Yep. We did good.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Yep. We did good.”')
                        $ renpy.notify("Quest completed: Bird Hunting")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunting{/i}')
                        $ quest_birdhunting_description08 = "I delivered the message."
                        $ quest_birdhunting = 2
                        $ elah_friendship += 1
                        menu:
                            '{color=#f6d6bd}Efren{/color} praises your bravery, while {color=#f6d6bd}Elah{/color} leans against the gate and points at the area behind the palisade. “We’ll get to the preparations later on. Have you noticed the old forest, friend?”
                            '
                            'I look north.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look north.')
                                jump creeksfirsttime07
            '“Are the ropes really enough to keep them here? Can’t they chew through them?”' if not (quest_birdhunting_description06 and not quest_birdhunting_description07 and foragingground_bird_taken == 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are the ropes really enough to keep them here? Can’t they chew through them?”')
                menu:
                    'Both men look at the animals with a renewed curiosity. “Well,” {color=#f6d6bd}the hunter{/color} starts, “if they can free themselves from a hemp rope, then squeeze through the stakes, and hwile no soul sees them, and then get to freedom again... I’d say they deserve to do so.”
                    \n\n{color=#f6d6bd}Elah{/color} leans against the gate and points at the area behind the palisade. “The mouflon may disappear, but the boars would be stuck on this plateau. Have you noticed the old forest, friend?”
                    '
                    'I look north.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look north.')
                        jump creeksfirsttime07
            '“Are you going to care for them in winter?”' if not (quest_birdhunting_description06 and not quest_birdhunting_description07 and foragingground_bird_taken == 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you going to care for them in winter?”')
                $ creeks_reasonstojoin_beastattacks = 1
                menu:
                    '{color=#f6d6bd}The hunter{/color} swallows loudly, already thinking about his next meal. “Nah, they’re here just for the meat and skin. Once the snow falls, we’ll butcher them.”
                    \n\n{color=#f6d6bd}The carpenter{/color} gives him a sullen glance, then squeezes the lower edge of his jacket. “I’d love to keep them with us, I don’t even {i}like{/i} meat. We could start a mouflon herd, or any other, but it’s too dangerous with such weak defenses,” he leans on the gate. “Our houses are too small for them, and having loud beasts outside during cold months would lure predators. We tried.” He falls silent for a bit, and once he picks up the conversation, his voice returns to its previous proud tone. “you’ll understand better if you take a look at our old forest, friend,” he points at the area behind the palisade.
                    '
                    'I look north.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look north.')
                        jump creeksfirsttime07

    label creeksfirsttime07:
        show areapicture creeks00g at basicfade
        menu:
            'The vast clearing is returning to life, with shrubs spread between the paths and tree stumps. You move to the bridge, then a gateway, and have a chance to look around. “We can see the edge of our world from the watchtower,” {color=#f6d6bd}Elah{/color} narrates sublimely. “In the long distance, the plateau ends, surrounded by cliffs. Ye either climb up the mountains, or fall to your death.”
            \n\nBoth men tell you about the difficult past of the village. A desperate camp, then a cabin, then two, shifting its wooden walls as more and more trees were cut. “Without tree crowns, we can walk with no shadows, beast dens, gargoyle eyes,” concludes {color=#f6d6bd}the carpenter{/color}
            '
            '“Is it really better than a forest garden? It would produce much more food, now I only see berries.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it really better than a forest garden? It would produce much more food, now I only see berries.”')
                $ creeks_reasonstojoin_creeksaboutlackingmeat += 1
                menu:
                    '“You hit the heart of our worries, friend,” {color=#f6d6bd}Elah{/color} admits and is interrupted by {color=#f6d6bd}the hunter{/color} quickly. “We did what we had to do to push away the beasts. They don’t feel safe here and don’t seek food on the shrubs as they would on trees.”
                    \n\n{color=#f6d6bd}Elah{/color} tells you there’s one more thing to see and as you walk away, he returns to the matter at hand. “The animals keep their distance now, at least in the meadows, so hunting for them gets difficult. And meat with hardly any mushrooms and herbs gets bland. A forest garden would solve the problem, sure, but we don’t know enough to even {i}start{/i} one. Hence, a field of berries,” he taps his stomach.
                    \n\n“First we need to learn how to feed our children. We lack strength and skill,” {color=#f6d6bd}Efren{/color} looks at you, “but we have time.”
                    '
                    'I nod. “With time comes opportunity.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “With time comes opportunity.”')
                        jump creeksfirsttime08
                    'I frown. “We never have as much time as we want.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown. “We never have as much time as we want.”')
                        jump creeksfirsttime08
            '“I’m surprised that the wrath of the herds hasn’t smitten you yet. These pointed sticks won’t stop a unicorn.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised that the wrath of the herds hasn’t smitten you yet. These pointed sticks won’t stop a unicorn.”')
                $ creeks_reasonstojoin_creeksaboutlackingwall += 1
                menu:
                    '“Nothing will, friend,” {color=#f6d6bd}the hunter{/color} counters, and {color=#f6d6bd}the carpenter{/color} is eager to follow. “I thank the landscape. Blocking the path here was one of the first things our predecessors took care of and it may be that the beasts don’t realize how much this place has changed.”
                    \n\nHe tells you there’s one more thing to see and continues his tale as you walk away. “From time to time, something reaches our territory. We feel safe among the bushes, but not so that we would send a child there. We have plans, so many lifetimes won’t be enough to complete them,” he says with a mix of melancholy and excitement, making {color=#f6d6bd}Efren{/color} listen with attention. “I want to see a stone wall with a walk for archers, weapons made of copper, a tannery set at its own camp, so we’re free of its stench. Farmers, fishers, sorcerers, herbalists.”
                    \n\nYou return to the main square again. “The words of a dreamer,” {color=#f6d6bd}the hunter{/color} pats his companion’s back. “First we need to learn how to feed our children. We lack strength and skill,” {color=#f6d6bd}Efren{/color} looks at you, “but we have time.”
                    '
                    'I nod. “With time comes opportunity.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “With time comes opportunity.”')
                        jump creeksfirsttime08
                    'I frown. “We never have as much time as we want.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown. “We never have as much time as we want.”')
                        jump creeksfirsttime08

    label creeksfirsttime08:
        show areapicture creeks00h at basicfade
        $ questionpreset = "elah1"
        $ quarters += 1
        menu:
            'You reach the edge of the village, a cliff as tall as the wall. Beneath you, two creeks meet each other and form a gentle river. “These are the trees we use to learn more about woodwork,” {color=#f6d6bd}Elah{/color} is smiling as he leans his back against the wall of a house. “We plant new ones, but we’ll soon have to bring wood from further away, give the saplings a few years, or however long they grow. A decade?”
            \n\n“And this is where I leave the two of you with your boring tree talks,” {color=#f6d6bd}Efren{/color} points at you. “See me later if you need. I’ll be around, I rarely hunt alone.”
            \n\n{color=#f6d6bd}The carpenter{/color} watches his departing companion with genial eyes. “Well, there’s work to be done, a new chair awaits me.” He leads you to a humble working station, placed at the edge of the square. The tools you notice are very simple, if not primitive. “We don’t {i}have to{/i} talk about my trade, [pcname]. Hwat brings you to us?”
            '
            '(elah1 set)':
                pass
