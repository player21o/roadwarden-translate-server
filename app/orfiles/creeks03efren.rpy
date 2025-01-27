# {color=#f6d6bd}Efren{/color}, Elah’s brother, now main hunter, goofball. Leather pants, a long, brown woolen cloak, and a matching pelt of a wolf on his head and shoulders, like a haunting hood. 20 years old, he laughs a lot, is either weirdly tense or relaxed, engages in shell contact, often touches his "hat". radosny, potrafi mówić aż za dużo, tubalnie się śmieje, repining - głośno marudzi, mówi o przeznaczeniu i duchach, ale sarkastycznie, "showers you with questions", szacuje rozmiary swoimi dłońmi

default efren_friendship = 0
default efren_club = 0
default efren_lastseen = 0
default efren_fluff = 0
default efren_killedspider = 0

default efren_about_elah = 0
default efren_about_himself = 0
default efren_about_shortcut = 0
default efren_about_birdhunting = 0
default efren_about_peltnorthhunters = 0
default efren_about_peltnorthhunters_newhunter = 0
default efren_about_weapons = 0
default efren_about_highisland = 0
default efren_about_highisland_recruitment_done = 0
default efren_highisland_joined = 0
default efren_about_greenmountaintribe = 0
default efren_took_rawhide = 0

default efren_about_missinghunters_questions01 = 0
default efren_about_missinghunters_questions02 = 0
default efren_about_missinghunters_questions03 = 0
default efren_about_missinghunters_questions04 = 0
default efren_about_missinghunters_questions05 = 0
default efren_about_missinghunters_questions06 = 0
default efren_about_missinghunters_dayreported = 0

label creeksefren01:
    if efren_lastseen != day:
        $ efren_lastseen = day
        $ efren_fluff = renpy.random.choice(['He’s inside the house of gatherings, comparing a few sharpened cudgels placed on one of the tables. ', 'He’s sitting beneath the watchtower, observing the area and playing with the wolf’s head. ', 'He’s resting on a bridge, sitting on its edge and keeping his feet in the cold water. ', 'He’s in the yard, just next to the gate, practicing his steps and swings while holding a blunt cudgel. ', 'He’s just returning from a trip to the area behind the northern palisade, holding a hare in his hands. ', 'You find him jogging along the creek, next to the small forest, with a heavy bag on his back. ', 'You find him sitting at the main square, using one of the log-made tables to fix his club by swapping one of the broken obsidian blades with a new one. '])
        if efren_friendship >= 6:
            $ custom1 = "He welcomes you with a bow. “Good fortune to you, friend!”"
        elif efren_friendship >= 3:
            $ custom1 = "As you get closer, he spares you a polite smile. “Good to see you in one piece, traveler.”"
        elif efren_friendship >= 0:
            $ custom1 = "Once you get closer, he nods politely."
        else:
            $ custom1 = "Once he notices you, he purses his lips, then lowers the wolf’s head to partially cover his eyes."
    else:
        $ efren_lastseen = day
        $ efren_fluff = ""
        if efren_friendship >= 6:
            $ custom1 = "He laughs. “You can’t get enough of me, aye?”"
        elif efren_friendship >= 3:
            $ custom1 = "He raises an eyebrow, then the wolf’s head, as if to see you better."
        elif efren_friendship >= 0:
            $ custom1 = "He’s lost in his thoughts."
        else:
            $ custom1 = "At first, he doesn’t look at you."
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if efren_about_himself and not quest_missinghunters and day > 20:
        $ questionpreset = "efren1"
        $ quest_missinghunters = 3
        menu:
            '[efren_fluff] Once you get closer, you notice that his eyes are red. He yawns, and explains he hasn’t slept in a few days. “Aye, friend. We came to believe our three tribesfolk will never be back. I need a few quiet days.”
            '
            '(efren1 set)':
                pass
    else:
        $ questionpreset = "efren1"
        menu:
            '[efren_fluff][custom1]
            '
            '(efren1 set)':
                pass

label creeksefrenafterinteraction01:
    $ questionpreset = "efren1"
    $ efren_fluff = renpy.random.choice(['“And that’s that,” he shrugs.', 'He looks at the sky. “Are we done here?”', 'He raises the mouth of the wolf’s head.', 'He glances at a pigeon that’s been sitting nearby, and moves his hand toward his obsidian club.'])
    menu:
        '[efren_fluff]
        '
        '(efren1 set)':
            pass

label creeksleavingefren01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away. “Good hunting.”')
    jump creeksafterinteraction01

label creeksefrenonelah01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think about {color=#f6d6bd}Elah{/color}?”')
    $ efren_about_elah = 1
    if efren_friendship+appearance_charisma < 3:
        $ questionpreset = "efren1"
        menu:
            'He repeats your question, making sure he heard correctly. “I {i}respect{/i} him, he took good care of me as an older brother. Our tale isn’t an easy one, so I’d rather keep it to ourselves, before you blurt something back to him.”
            '
            '(efren1 set)':
                pass
    else:
        $ efren_about_elah = 2
        if efren_about_elah == 2 and elah_about_efren == 2:
            $ creeks_reasonstojoin_beastattacks += 1
        $ questionpreset = "efren1"
        menu:
            'He repeats your question, making sure he heard correctly, then scratches the wolf’s head. “I {i}respect{/i} him, he took good care of me as an older brother. He’s boring, you know that, and hides a lot behind those smiles of his. He spends days in the workshop, thinking we may be both as weak as we are now, and smart enough to prosper. {i}There’s work to be done!{/i}” He mimics the carpenter’s cadence. “Aye, there always is.”
            \n\nYou want to ask about the “weakness,” but he gives you no time to speak. “There’s almost no folks from the older generations left, did you notice? {color=#f6d6bd}Foggy{/color} and {color=#f6d6bd}Old Hava{/color} are the only two still capable of doing work, but they aren’t getting any younger, and are already wounded.” You think about the tavern keeper’s lost arm. “We were always lacking in numbers, blades, tools, and skills. The beasts took many souls, but {color=#f6d6bd}Elah{/color} won’t talk ‘bout it. He’d rather forget them and tie this place to the other villages, making us merchants and rotten {i}carpenters{/i},” he adjusts his cloak, boiling from frustration, “than risk the lives of the younger tribesfolk on training and hunting. We’ve suffered so much, yet we’re becoming even weaker.”
            \n\nHe calms himself down with silence.
            '
            '(efren1 set)':
                pass
    label creeksefrenonelah02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was wondering about {color=#f6d6bd}Elah{/color}...”')
        $ efren_about_elah = 2
        if efren_about_elah == 2 and elah_about_efren == 2:
            $ creeks_reasonstojoin_beastattacks += 1
        $ questionpreset = "efren1"
        menu:
            'He scratches the wolf’s head, then nods. “He’s boring, you know that, and hides a lot behind those smiles of his. He spends days in the workshop, thinking we may be both as weak as we are now, and smart enough to prosper. {i}There’s work to be done!{/i}” He mimics the carpenter’s cadence. “Aye, there always is.”
            \n\nYou want to ask about the “weakness,” but he gives you no time to speak. “There’s almost no folks from the older generations left, did you notice? {color=#f6d6bd}Foggy{/color} and {color=#f6d6bd}Old Hava{/color} are the only two still capable of doing work, but they aren’t getting any younger, and are already wounded.” You think about the tavern keeper’s lost arm. “We were always lacking in numbers, blades, tools, and skills. The beasts took many souls, but {color=#f6d6bd}Elah{/color} won’t talk ‘bout it. He’d rather forget them and tie this place to the other villages, making us merchants and rotten {i}carpenters{/i},” he adjusts his cloak, boiling from frustration, “then risk the lives of the younger tribesfolk on training and hunting. We’ve suffered so much, yet we’re becoming even weaker.”
            \n\nHe calms himself down with silence.
            '
            '(efren1 set)':
                pass

label creeksefrenaboutwoodenweapons01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I noticed that no soul in your tribe carries a weapon that contains iron or copper.”')
    $ efren_about_weapons = 1
    $ creeks_reasonstojoin_lackofmetal = 1
    $ foragingground_foraging_vein_rumor = 1
    $ questionpreset = "efren1"
    menu:
        '“Not because of some priest prattle, we just have neither,” he taps the sharpened obsidian of his club proudly. “But we do hwat we can, and with fine results. We hunt nothing larger than a deer, and cast rocks from slingshots. {color=#f6d6bd}Elah{/color} hopes to trade for copper with his firewood, uhm, {i}chairs{/i}. We’ll see.” His eyes tell you that you’ll see nothing of the sort.
        \n\n“There was even a traveler here, a year or two ago, who was seeking ore in this land. He went to the eastern ravine at the foraging ground, south of here, and...” He gives you a playful look, then suddenly claps his hands and steps forward, making the wolf’s jaw bounce up and down. “Dead. His tent is still there, but the shell went into the fogs.”
        '
        '(efren1 set)':
            pass

label creeksefren_about_himself01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you the only hunter around?”')
    $ efren_about_himself = 1
    $ questionpreset = "efren1"
    if day <= 5:
        $ custom1 = "“Well... There’s just one issue. Three of my friends left the village just a few days ago... And they haven’t returned yet. But they should. {color=#f6d6bd}Elah{/color} is going to ask questions, and soon.”"
    elif day <= 10:
        $ custom1 = "“Well... There’s just one issue. Three of my friends left the village just a few days ago... And they haven’t returned yet. But they should. {color=#f6d6bd}Elah{/color} is growing worried.”"
    elif day <= 15:
        $ custom1 = "“Well... There’s just one issue. Three of my friends left the village many days ago... And I’m really afraid for them. {color=#f6d6bd}Elah{/color} thinks they’re already dead.”"
    else:
        $ custom1 = "“Well... There’s just one issue. Three of my friends left the village many days ago... And I think they may be dead already. {color=#f6d6bd}Elah{/color} sure thinks so.”"
    menu:
        '“But of course not, there’s,” he takes a suspiciously long pause, “{i}seven{/i} of us! The tribe is small, we have enough food without daily trips. If we catch too much meat, it spoils, so it’s better to let the animals feel safe.”
        \n\nYou try to change the topic, but the man suddenly looks around and lowers his wolf’s head. [custom1]
        '
        '(efren1 set)':
            pass

label creeksefren_about_himself01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you the only hunter around?”')
    $ efren_about_himself = 1
    $ quest_missinghunters = 3
    $ questionpreset = "efren1"
    menu:
        '“It sure feels like it.” He lets out a long sigh and takes off his wolf-hat. “There’s... Four of us left. Too bad you weren’t on these roads earlier, friend. Some of our tribesfolk most likely needed your help, but are now gone. We’ve accepted that they won’t be back.”
        \n\nAfter a long pause, he puts on his hat again. “Our village is small, but we now have to do almost daily trips. If we catch too much meat, it spoils, but recently that hasn’t been an issue.”
        '
        '(efren1 set)':
            pass

label creeksefren_about_peltnorthhunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do the hunters from {color=#f6d6bd}Pelt of the North{/color} hinder your job?”')
    $ efren_about_peltnorthhunters = 1
    $ description_bighunters06 = "According to {color=#f6d6bd}Efren{/color}, “at least they smile, unlike others in the peninsula.”"
    $ questionpreset = "efren1"
    menu:
        '“Nah! They only get closer when they chase after wounded prey, so our woods stay mostly the same. You could have another village, twice our size,” he glances toward the gate, “halfway from here to {color=#f6d6bd}Pelt{/color} and there would still be more than enough game for every belly, as long as they would forage and set up farms.”
        \n\nYou ask him if he has ever considered joining professional hunters, but he takes off the wolf’s head and gives it to you so you can take a better look. It’s weirdly warm from the sun. “That’s the {i}only{/i} wolf any of us felled in the last five years, you see? Not that we’re cowards,” he suddenly raises his voice. “Our trade just isn’t like the big game hunters’. I place fish traps, put glue to catch birds, shoot rocks at rats and rabbits. When in a group, we may seek roe deer or aurochs.”
        \n\nHe takes the hat back and looks at it with nostalgia. “Those in the inn seek trophies, not meat, so they hunt for big beasts, ones that, you know. Fight back. Our ways are different, but I like that bunch. At least they smile, unlike others in the peninsula. Hunters will always find a common tongue. Once you see enough blood and guts, you have to laugh, or go crazy.”
        '
        '(efren1 set)':
            pass

    label creeksefren_about_peltnorthhunters02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever had an opportunity to work with {color=#f6d6bd}Erastos{/color} from {color=#f6d6bd}Howler’s Dell{/color} and {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}? Do they know their trade?”')
        $ quest_recruitahunter_spokento_efren = 1
        $ quest_recruitahunter_erastos_points += 1
        $ quest_recruitahunter_cassia_points += 1
        if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_erastos_points_notify2:
            $ quest_recruitahunter_erastos_points_notify2 = 1
            $ quest_recruitahunter_erastos_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_erastos_points_notify1:
            $ quest_recruitahunter_erastos_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold2 and not quest_recruitahunter_cassia_points_notify2:
            $ quest_recruitahunter_cassia_points_notify2 = 1
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        elif quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify1:
            $ quest_recruitahunter_cassia_points_notify1 = 1
            $ renpy.notify("Journal updated: Recruit a Hunter")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
        $ questionpreset = "efren1"
        menu:
            '“Aye, with both of them, but I’d rather hunt for frogs than waste my time teaching them both how to not trip over their own feet.” He rubs the forehead of his wolf, not aware that you’re waiting for him to tell you more. “What, surprised?” he finally adds. “{color=#f6d6bd}Erastos{/color} barely knows how to catch a rabbit or a sparrow, he’s as much of a trapper as a child with a stick is a soldier. And {color=#f6d6bd}Cassia{/color} is even worse, big mouth, sure, but whenever we seek blades at {color=#f6d6bd}Gale Rocks{/color} to help us catch a big prey, she suddenly gets a headache.”
            '
            '(efren1 set)':
                pass

label creeksefren_about_shortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the road running through the heart of the forest?”')
    $ efren_about_shortcut = 1
    $ description_shortcut07 = "According to {color=#f6d6bd}Efren{/color}, I may encounter gnolls and frightapes. He told me a bit more about them."
    $ questionpreset = "efren1"
    $ minutes += 5
    menu:
        '“I know to avoid it. {i}Blood there.{/i}” Seeing that you’re waiting for a longer tale, he adjusts his heavy cloak, spending a good minute on making sure that you understand it’s a dangerous place. “You’ll do better riding around it, the northern road is the safest,” he concludes.
        \n\nAfter you insist that any sort of guidance may be of use, he scratches the wolf’s head. “I’ve heard from a friend that gnolls were moving there. Those very small beastfolks, you know?” He moves an open hand close to his hips, portraying the height. “They’ll threaten you until you give them some meat, and that’s all they eat. No fruits, no, I don’t know, bones. But it’s the frightapes that scare me the most, and there’s an entire family of them. Trust me, if you ever hear the terrible scream of a human somehwere in the tree crowns, run as fast as you can, don’t seek it, and certainly don’t {i}fight{/i} it. Just ride as fast as you can.”
        '
        '(efren1 set)':
            pass

label creeksefren_about_birdhunting01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I plan to help {color=#f6d6bd}the foragers{/color} with catching a big runner. Any tips on how to approach this?”')
    $ efren_about_birdhunting = 1
    menu:
        '“So that’s their scheme?” He looks in the tavern’s direction, pausing for a moment, then straightens up. “Ah, so you’re seeking advice from a more {i}experienced{/i} hunter?” He pats his club proudly. “Well, there is the usual stuff. Don’t fight hungry, have a decent jacket, be sure to have something to block a bird’s charge. Oh, and maybe!” He points at the sky, then stretches out his arms, as if holding a long stick. “A spear! The longer you keep a runner at a distance, the better.”
        '
        '“Why don’t {i}you{/i} help the foragers?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why don’t {i}you{/i} help the foragers?”')
            $ efren_about_birdhunting = 2
            $ questionpreset = "efren1"
            menu:
                '“Well, they didn’t ask any of our tribesfolk, so I guess we’re not welcome. I thought they had realized they weren’t fit to be hunters. {color=#f6d6bd}Ilan{/color} is a bit of a sissy, and {color=#f6d6bd}Tzvi{/color}...” He takes a longer pause. “Would have a hard time finding anyone to hunt with. It’s a matter of trust, you see.”
                '
                '(efren1 set)':
                    pass
        '“Have you ever fought such a bird?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever fought such a bird?”')
            $ efren_friendship += 1
            $ questionpreset = "efren1"
            menu:
                '“Not yet, but I ran away from a few, and not everyone can say that!” He lets out a burst of jaunty laughter. “They are way too common at the edges of our woods, if you ask me! Ever since I met the first one, I jog. Maybe not {i}every{/i} day, but almost!”
                '
                '(efren1 set)':
                    pass

label creeksefren_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know of any creatures that live on {color=#f6d6bd}High Island{/color}?”')
    $ efren_about_highisland = 1
    $ description_highisland07 = "Since there are many harpies between the island and the coast, it may be better to have a proper ranged weapon, or a shooting expert."
    $ questionpreset = "efren1"
    menu:
        '“How could I, friend? I haven’t been there,” he suddenly looks to the sky, raises his hand, and starts to tap the top of the wolf’s head. “But the harpies... Aye, they’re common on the coast, and on open waters, I saw them from {color=#f6d6bd}Gale Rocks’{/color} beach. Rocks and sticks don’t fly well when thrown upward, a bow would be a safer bet.”
        '
        '(efren1 set)':
            pass

label creeksefren_about_highisland02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your help on {color=#f6d6bd}High Island{/color}. It will make us even.”')
    $ efren_about_highisland_recruitment_done = 1
    $ questionpreset = "efren1"
    menu:
        '“Hwat am I, a fish?” He emphasizes his question by grabbing his hat’s jaw. “I’m going to kill you if you let me drown. Salt water tastes like pee.”
        \n\nBefore you ask him how much does he know about the taste of piss, he raises his voice proudly. “You had my word, and I’ll be ready to answer your call, friend!”
        '
        '(efren1 set)':
            pass

label efren_about_greenmountaintribe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”')
    $ efren_about_greenmountaintribe = 1
    $ description_greenmountaintribe11 = "According to {color=#f6d6bd}Efren{/color}, The Tribe uses the Old Speech, and has a custom of giving gifts to whom it visits, as well as of receiving ones from those who visit them."
    $ questionpreset = "efren1"
    menu:
        'He leans away, gives you a surprised look, but then shrugs so nonchalantly that his “hat” falls on his back. “Nah, they use the Old Speech, it sounds like a drinking song of a seagull,” he scoffs at his own joke. “They only talked to our elders, like {color=#f6d6bd}Foggy{/color},” he whispers, “aye, though don’t call her that. There was the time when they gave us seeds and spears on a visit, and {i}we{/i} also brought {i}them{/i} gifts to ask for something, hwat was it...” After he prates for a bit, you change the topic.
        '
        '(efren1 set)':
            pass

label creeksefrenontraps01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What sort of traps would you put in an old tunnel?”')
    $ oldtunnel_exploration_knowledge = 1
    $ minutes += 20
    $ quest_closedtunnel_description01a = "The tunnel hides a group of undead. To have a better chance at fighting them, I could construct some simple traps."
    $ renpy.notify("Journal updated: The Closed Tunnel")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
    $ questionpreset = "efren1"
    menu:
        '“Depends,” he drawls. “Got anyone to help you? Then start with taking a good look around. Find some sticks, tools, maybe beast tusks, this long,” he shows a span with his fingers. “Or bigger... What’s your catch?”
        \n\nYou mention the skeletons and he scratches the side of his hat, grunting. “Then-then-then! A bit fast, aye? Put something fast too, but firm, but hitting right away, but camouflaged, but...” He sees your frown and straightens up. “Well, let’s say you can find any wood. Put deadfalls where you can gather hard things to drop, maybe above doors, and whip traps behind turns and corners. But these take a lot of work. Foothold traps are easier to make, but if the tunnel is rocky... Oh lazy spirits, just come with me.”
        \n\nYou take a short walk to the woods and he shows you a few spots with traps for animal feet, made of short slats surrounding camouflaged holes, and tells you how to place some larger traps without having trees around. You head back to the village and you repeat his instructions.
        '
        '(efren1 set)':
            pass

label creeksefrenaboutmissinghuntersALL:
    label creeksefrenaboutmissinghunters01v1:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Aren’t you worried about the other hunters?”')
        jump creeksefrenaboutmissinghunters01
        label creeksefrenaboutmissinghunters01v2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you think these other hunters aren’t back yet?”')
            jump creeksefrenaboutmissinghunters01
        label creeksefrenaboutmissinghunters01v3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll try to find these hunters. Tell me what you know.”')
            jump creeksefrenaboutmissinghunters01
        label creeksefrenaboutmissinghunters01:
            $ creeks_reasonstojoin_missinghunters = 1
            menu:
                'He walks around, from time to time looking at you with an open mouth, not sure how to start. He takes off his heavy cloak and looks you in the eyes.
                \n\n“They left for a few days to seek and kill some big game, each of them a different one, then bring all of them for me to judge,” his confident voice falters when he mentions his own part. “The winner would have caught me the prey of the greatest size, rarity, utility. And of the greatest threat.” He turns away and lowers the wolf’s mouth.
                '
                '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                    jump efren_about_missinghunters_questions05
                '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                    jump efren_about_missinghunters_questions04
                '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                    jump efren_about_missinghunters_questions01
                '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                    jump efren_about_missinghunters_questions02
                '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                    jump efren_about_missinghunters_questions03
                '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                    jump efren_about_missinghunters_questions06
                '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                    jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions05:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me more about those three.”')
        $ efren_about_missinghunters_questions05 = 1
        menu:
            '“They are hunters and fighters, but also close friends. If one of them was in trouble, the others would have done all they could to help. They’ve been a team for years, and were planning to start a family this winter, you know? Their last big adventure before {color=#f6d6bd}Dalia’s{/color} belly locks her at home.”
            \n\nHe gives you quite a tale of their deeds and features. {color=#f6d6bd}Dalia{/color} is “the bravest of them, with strong legs. She has simple ways and looks for beasts in the open, by the roads. Her hair is light, always tied in a single braid.”
            \n\n{color=#f6d6bd}Admon{/color} “is a man who seeks paths and challenges.” He believes that seeking knowledge of the peninsula will bring the tribe ways to survive hardships. “He was, {i}is{/i} smaller than the others, and knows more ‘bout dressing the wild game than any of us. His arms are small, so he often places traps. His hair is a bit darker than {color=#f6d6bd}Dalia’s{/color}, but short, just like his beard.”
            \n\n{color=#f6d6bd}Vaschel{/color} “is not a man, though they were born with a prick,” and “wears browns and greens to blend in with the trees. They hunt like a gargoyle, hiding among leaves, jumping at a creature when it gets close.” Because of that, they have often roamed in the woods, even those that are far away from the village.
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This sounds serious, but if you want me to look for them, I still deserve a reward.”')
        $ efren_about_missinghunters_questions04 = 1
        menu:
            '“Isn’t helping three young, strong souls enough?” Seeing your look, he raises his voice, draws his obsidian-edged club, and touches his chest with it. “Then I will loyally assist you, friend! For your brave deeds, you may count on me on a day of great challenge!”
            \n\nAs he lowers his weapon, he winks at you. “And others will be grateful as well, you know that.”
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions06:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your {i}assistance{/i}, huh? ...How about some dragon bones?”')
        $ efren_about_missinghunters_questions06 = 1
        $ efren_friendship -= 1
        menu:
            'He purses his lips, swallowing his pride. “Oh. Well, I’ve none. Our village doesn’t really trade.”
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And where should I start?”')
        $ efren_about_missinghunters_questions01 = 1
        menu:
            'He looks at you as if you’re slow. “I... would have found them myself if I knew, aye? Let the horse take you to other settlements, ask there?”
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
        $ efren_about_missinghunters_questions02 = 1
        menu:
            '“Have you no shred of optimism? Maybe they’re fine. Just tell them to come home, we’ve got enough wood and food to start the next feast! And I have a hint that an {i}honorable guest{/i} may be welcome there,” he smiles at you, and for a moment you think you see the wolf head’s wink.
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label efren_about_missinghunters_questions03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does your tribe often send lone hunters? Why not work in groups?”')
        $ efren_about_missinghunters_questions03 = 1
        menu:
            '“This isn’t a {i}hunt{/i}, but a competition. The winner names their first child. Aye, I’ve heard their arguments, you wouldn’t believe how hard it is to pick a name when you have three parents,” he chuckles to himself.
            \n\nOnce the memory fades, he gets serious again. “But I can’t disagree with you, friend. It’s the first time in many years since my tribesfolk have gone on such’ reckless trip, and I fear it may remind us hwy the peninsula isn’t a place for adventures.”
            '
            '“Tell me more about those three.”' if not efren_about_missinghunters_questions05:
                jump efren_about_missinghunters_questions05
            '“This sounds serious, but if you want me to look for them, I still deserve a reward.”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions04:
                jump efren_about_missinghunters_questions04
            '“And where should I start?”' if efren_about_missinghunters_questions05 and not efren_about_missinghunters_questions01:
                jump efren_about_missinghunters_questions01
            '“Let’s say I were to find them. What should I tell them?”' if not efren_about_missinghunters_questions02:
                jump efren_about_missinghunters_questions02
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                jump efren_about_missinghunters_questions03
            '“Your {i}assistance{/i}, huh? ...How about some dragon bones?”' if efren_about_missinghunters_questions04 and not efren_about_missinghunters_questions06:
                jump efren_about_missinghunters_questions06
            '“I’ll tell you if I find anything.”' if efren_about_missinghunters_questions04 and efren_about_missinghunters_questions05:
                jump creeksefrenaboutmissinghunters01after

    label creeksefrenaboutmissinghunters01after:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see what I can do.”')
        $ quarters += 1
        $ quest_missinghunters = 1
        $ renpy.notify("New entry: The Missing Hunters")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Missing Hunters{/i}')
        menu:
            '“Thanks, friend. And if all you have is a tale of their dead shells, bring me something to prove it, aye? A trinket, a weapon. A thing we can throw into a pyre.”
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll try.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll try.”')
                jump creeksefrenafterinteraction01

    label creeksefrenaboutmissinghunters02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the hunters...”')
        menu:
            '“Any good news?”
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label efren_about_missinghunters_questions01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
        $ efren_about_missinghunters_questions01 = 1
        menu:
            'He looks at you as if you’re slow. “I... would have found them myself if I knew, aye? Let the horse take you to other settlements, ask there?”
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label efren_about_missinghunters_questions02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
        $ efren_about_missinghunters_questions02 = 1
        menu:
            '“Have you no shred of optimism? Maybe they’re fine. Just tell them to come home, we’ve got enough wood and food to start the next feast! And I have a hint that an {i}honorable guest{/i} may be welcome there,” he smiles at you, and for a moment you think you see the wolf head’s wink.
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label efren_about_missinghunters_questions03alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does your tribe often send lone hunters? Why not work in groups?”')
        $ efren_about_missinghunters_questions03 = 1
        menu:
            '“This isn’t a {i}hunt{/i}, but a competition. The winner names their first child. Aye, I’ve heard their arguments, you wouldn’t believe how hard it is to pick a name when you have three parents,” he chuckles to himself.
            \n\nOnce the memory fades, he gets serious again. “But I can’t disagree with you, friend. It’s the first time in many years my tribesfolk have gone on such’ reckless trip, and I fear it may remind us hwy the peninsula isn’t a place for adventures.”
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label creeksefrenaboutfindingadmon01:
        $ bestiary_ghouls_legend = 1
        $ quarters += 1
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        menu:
            '[custom3] “So there’s no shell, only someone who heard ‘bout him going east, and, well... A ghoul. Everyone knows hwat that means. He’ll soon wake up,” he shakes his head, as if to drop the thought. “D’you have any proof that you’ve found him?”
            '
            'I give him the broken knife. “Keep this. I think you’ll recognize it.”' if item_brokenknife:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give him the broken knife. “Keep this. I think you’ll recognize it.”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                $ quest_missinghunters_admonknown = 1
                menu:
                    'He reaches for it without thinking twice, then brings it close to his face, studying the tiny details of the bone. “I do,” he whispers, “it was his mother’s.” He lowers it, but holds it tightly. “But she’s not around anymore.”
                    '
                    '“I see.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '(lie) “There wasn’t much with him. Just some pieces of clothing, torn and molding.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “There wasn’t much with him. Just some pieces of clothing, torn and molding.”')
                $ pc_lies += 1
                $ quest_missinghunters_admonfound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 1
                $ quest_missinghunters_admonknown = 1
                menu:
                    'He looks away. “That’s a shame. His mother used to have a beautiful knife with a handle made of bone, my pa had carved it. It would be a memory worth the last fire.”
                    '
                    '“Yes. A tragedy.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes. A tragedy.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“There was a broken knife... But I don’t have it with me anymore.”' if not item_brokenknife:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There was a broken knife... But I don’t have it with me anymore.”')
                $ quest_missinghunters_admonfound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 0
                $ quest_missinghunters_admonknown = 1
                menu:
                    'He looks away. “That’s a shame. His mother used to have a beautiful knife with a handle made of bone, my pa had carved it. It would be a memory worth the last fire.”
                    '
                    'I clear my throat awkwardly.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat awkwardly.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    '“Yeah. It was probably the same.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah. It was probably the same.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutfindingadmon02alt:
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        $ quest_missinghunters_admonknown = 1
        $ bestiary_ghouls_legend = 1
        $ quarters += 1
        menu:
            'He reaches for it without thinking twice, then brings it close to his face, studying the tiny details of the bone. “I do,” he whispers, “it belonged to {color=#f6d6bd}Admon’s{/color} mother.” He lowers it, but holds it tightly. “But she’s not around anymore. Hwere was it?”
            \n\n[custom3] “So there’s no shell, only a ghoul... Everyone knows hwat that means. He’ll wake up soon,” he shakes his head, as if to drop the thought.
            '
            '“It may be so.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be so.”')
                jump creeksefrenaboutmissinghunters02afterinteraction
            'I stay quiet.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I stay quiet.”')
                jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutrawhide01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Does this rawhide belong to your tribe?”')
        $ item_rawhide = 0
        $ renpy.notify("You lost the rawhide.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the rawhide.')
        $ efren_took_rawhide = 1
        $ northernroad_rawhide_owner = 1
        menu:
            'He gives it only a glance, then throws it away. “I think so?” After you describe where you found it, he reaches toward the wolf’s head, but doesn’t touch it. “Me and the other hunters go to this place in spring, when there’s fewer beasts around, sit on blankets,” he points at the hide, “eat before the hunt. Maybe you’ll find a trail there?”
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label creeksefrenaboutfindingdalia01abandoned:
        $ quarters += 1
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        $ quest_missinghunters_daliafound = 3
        $ creeks_reputation += 0
        $ efren_friendship += 1
        $ quest_missinghunters_daliaknown = 1
        menu:
            '[custom3] “Caught by a cat, buried by howls. A grim, violent tale,” he looks around. “Let’s hope there are no {i}eavesdropping children{/i} in sight,” he says emphatically, but as no one responds, he carries on. “Though I’m not so sure {i}I{/i} believe you, friend, as you have nothing to show me.”
            '
            'I stay silent.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutfindingdalia01:
        $ quarters += 1
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        menu:
            '[custom3] “Caught by a cat, buried by howls. A grim, violent tale,” he looks around. “Let’s hope there are no {i}eavesdropping children{/i} in sight,” he says emphatically, but as no one responds, he carries on. “But d’you have anything to prove your words?”
            '
            '“These bones... And this belt buckle.”' if item_pileofbones and item_bonebuckle:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones and the decorative buckle.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 2
                $ efren_friendship += 2
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “I’d recognize that buckle anyhwere. {color=#f6d6bd}Dalia{/color} had a gift, was ready to give up the hunt if it would mean more craft time for her. But honestly, friend, her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“I found this belt buckle. Take it.”' if item_bonebuckle:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle. Take it.”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“I was so hoping you were lying,” he reaches for the buckle without giving it a closer look. “I’d recognize it anyhwere. {color=#f6d6bd}Dalia{/color} had a gift, was ready to give up the hunt if it would mean more craft time for her.” A sudden realization comes to him. “Aye, shag it. I hope the cat didn’t play with its prey.”
                    '
                    '“I’m sure it was quick and effective.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure it was quick and effective.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    '“Best not to think about it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Best not to think about it.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“These bones belong to her.”' if item_pileofbones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to her.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                $ quest_missinghunters_daliafound = 2
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“This rawhide helped me get to her.”' if item_rawhide:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This rawhide helped me get to her.”')
                $ item_rawhide = 0
                $ renpy.notify("You lost the rawhide.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the rawhide.')
                $ quest_missinghunters_daliafound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    'He holds it with his fingers, then throws it on the ground. “That’s hardly enough, friend. It’s just a piece of trash, and it could belong to anyone.” He observes you for a moment, then scratches the wolf’s head. “But I have to trust you with this one.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“The rawhide I gave you is what helped me find her.”' if efren_took_rawhide:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The rawhide I gave you is what helped me find her.”')
                $ quest_missinghunters_daliafound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    'He sighs. “That’s hardly enough, friend. It’s just a piece of trash, and it could belong to anyone.” He observes you for a moment, then scratches the wolf’s head. “But I have to trust you with this one.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“I had to get out of there, and quickly. I had no time to search her bones.”' if not howlerslair_corpse_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had to get out of there, and quickly. I had no time to search her bones.”')
                $ quest_missinghunters_daliafound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“Aye, your tale makes it hard to believe you survived. Or that you were there,” he gives you a distrustful look, but then shrugs. “Though I think I don’t have a choice.”
                    '
                    'I stay silent.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '(lie) “She was nothing but a pile of bones. I found nothing of value.”' if howlerslair_corpse_item:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “She was nothing but a pile of bones. I found nothing of value.”')
                $ pc_lies += 1
                $ quest_missinghunters_daliafound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“Aye, I don’t doubt it. I bet nothing of value may remain at the heart of the house of thieves. But her siblings won’t be so easily convinced,” he gives you a melancholic look, then adjusts the wolf’s head. “Still, I don’t have a choice. It’s not like you’re going to put bones in a sack.”
                    '
                    'I clear my throat and look away.' if howlerslairpileofbonesgathered:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat and look away.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    '“Exactly.”' if not howlerslairpileofbonesgathered:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Exactly.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“There was a decorative buckle, but I didn’t bring it.”' if howlerslair_corpse_item and not item_bonebuckle:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There was a decorative buckle, but I didn’t bring it.”')
                $ quest_missinghunters_daliafound = 3
                $ creeks_reputation += 0
                $ efren_friendship -= 1
                $ quest_missinghunters_daliaknown = 1
                menu:
                    '“Hwat happened, you {i}lost{/i} it?” He gives you a distrustful look. “Or maybe sold it? That’d be a low punch, {i}friend{/i}. But fine, I hope her siblings are going to believe me. I don’t have a choice but to trust you.”
                    '
                    'I stay silent.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                        jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutfindingdalia02alt:
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        $ quarters += 1
        $ quest_missinghunters_daliaknown = 1
        menu:
            'He reaches for the buckle without giving it a closer look. “I’d recognize it anyhwere. {color=#f6d6bd}Dalia{/color} had a gift, was ready to give up the hunt if it would mean more craft time for her. So, hwere was it?”
            \n\n[custom3] A sudden realization comes to him. “Aye, shag it. I hope the cat didn’t play with its prey.”
            '
            '“I’m sure it was quick and effective.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure it was quick and effective.”')
                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Best not to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Best not to think about it.”')
                jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutfindingvaschel01:
        $ quarters += 1
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        menu:
            '[custom3] “So you don’t really know hwat happened. Just that their shell was in the woods.”
            \n\nHe gives you a long look, but finally nods. “Any evidence?”
            '
            '“I took this earring from their shell.”' if item_boneearring:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I took this earring from their shell.”')
                $ item_boneearring = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the earring.')
                $ quest_missinghunters_vaschelfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                $ quest_missinghunters_vaschelknown = 1
                menu:
                    'He observes it for a few moments, then lets out a sigh. “So you did. They made this when they were but a li’l kid, and told me that once they had a child, they would never wear {i}such ugly things{/i}. Their words.” He lowers his fist, then looks toward the entrance to the village. “I mean, it’s not such’ bad trinket.”
                    '
                    '“It’s elegant.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s elegant.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    '“I’d trust {color=#f6d6bd}Vaschel’s{/color} judgment here.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d trust {color=#f6d6bd}Vaschel’s{/color} judgment here.”')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '(lie) “Their shell was in such a shape that, well. I didn’t find anything I could bring.”' if not item_boneearring and shortcut_darkforest_furlesswolf_takingtheearing:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Their shell was in such a shape that, well. I didn’t find anything I could bring.”')
                $ pc_lies += 1
                $ quest_missinghunters_vaschelfound = 3
                $ custom1 = ""
                $ creeks_reputation += 0
                $ efren_friendship += 0
                $ quest_missinghunters_vaschelknown = 1
                menu:
                    'He observes it for a few moments, then lets out a sigh. “You’re not making it easy on me, friend.” He looks into your eyes, then lowers the wolf’s mouth. “I guess all I have is your word.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    'I shrug.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
            '“They had an earring made of bone... But it’s not with me.”' if not item_boneearring and shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They had an earring made of bone... But it’s not with me.”')
                $ quest_missinghunters_vaschelfound = 3
                $ creeks_reputation += 0
                $ efren_friendship += 0
                $ quest_missinghunters_vaschelknown = 1
                menu:
                    'He observes it for a few moments, then lets out a sigh. “I wish it was. They made it when they were but a li’l kid, and told me that once they had a child, they would never wear {i}such ugly things{/i}. Their words.” He looks into your eyes. “I guess all I have is your word.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump creeksefrenaboutmissinghunters02afterinteraction
                    'I shrug.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                        jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutfindingvaschel02alt:
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom3 = "He interrupts your tale many times, but having little knowledge to spare, you can’t satisfy his curiosity."
        elif quest_missinghunters_reported == 1:
            $ custom3 = "He keeps chipping in until you tell him to listen to the end. He respects your wish, though he frowns so much that you wonder if he can see you."
        else:
            $ custom3 = "This time he listens patiently, knowing you are saying as much as you can."
        $ quarters += 1
        $ quest_missinghunters_vaschelknown = 1
        $ quest_missinghunters_vaschelfound = 3
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        menu:
            'You explain that the shell was in the deep woods, in an area where you’d heard they were heading, and they were beyond help. [custom3] He observes you for a few moments, then lets out a sigh. “You’re not making it easy on me, friend.” He looks into your eyes, then lowers the wolf’s mouth. “I guess all I have is your word.”
            '
            '“Seems like it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Seems like it.”')
                jump creeksefrenaboutmissinghunters02afterinteraction
            'I stay silent.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                jump creeksefrenaboutmissinghunters02afterinteraction

    label creeksefrenaboutmissinghunters02afterinteraction:
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ custom2 = "“Let’s stay positive, aye?”"
        elif quest_missinghunters_reported == 1:
            $ custom2 = "“One bit of bad news isn’t all, aye? Maybe the others are fine.”"
        elif quest_missinghunters_reported == 2:
            $ custom2 = "“Thanks for help, friend.” After these words, {color=#f6d6bd}Efren{/color} is unusually quiet."
        elif quest_missinghunters_reported >= 3:
            jump creeksefrenaboutmissinghunters03
        menu:
            '[custom2]
            '
            'I can’t spend even more time on this. “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”' if (day >= 20 and not quest_missinghunters_admonfound) or (day >= 20 and not quest_missinghunters_daliafound) or (day >= 20 and not quest_missinghunters_vaschelfound):
                jump creeksefrenaboutmissinghuntersgivingup01
            '“I found {color=#f6d6bd}Admon{/color}.”' if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Admon{/color}.”')
                jump creeksefrenaboutfindingadmon01
            '“Do you recognize this knife?”' if item_brokenknife and not quest_missinghunters_admonknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you recognize this knife?”')
                $ item_brokenknife = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the broken knife.')
                $ quest_missinghunters_admonfound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingadmon02alt
            '“Does this rawhide belong to your tribe?”' if item_rawhide and not quest_missinghunters_daliafound and not northernroad_rawhide_owner:
                jump creeksefrenaboutrawhide01
            '“I know where {color=#f6d6bd}Dalia{/color} disappeared.”' if howlerslair_corpse_status == "abandoned" and quest_missinghunters_daliaknown and quest_missinghunters_daliafound < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know where {color=#f6d6bd}Dalia{/color} disappeared.”')
                jump creeksefrenaboutfindingdalia01abandoned
            '“{color=#f6d6bd}Dalia{/color} is gone.”' if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Dalia{/color} is gone.”')
                jump creeksefrenaboutfindingdalia01
            '“I found this belt buckle made of bone...”' if item_bonebuckle and not quest_missinghunters_daliaknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this belt buckle made of bone...”')
                $ item_bonebuckle = 0
                $ item_bonebuckle_returned = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the belt buckle.')
                $ quest_missinghunters_daliafound = 2
                $ creeks_reputation += 1
                $ efren_friendship += 1
                jump creeksefrenaboutfindingdalia02alt
            '“These bones belong to {color=#f6d6bd}Dalia{/color}.”' if item_pileofbones and quest_missinghunters_daliaknown and quest_missinghunters_daliafound == 2 and not item_pileofbones_returned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “These bones belong to {color=#f6d6bd}Dalia{/color}.”')
                $ item_pileofbones = 0
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the pile of bones.')
                $ item_pileofbones_returned = 1
                $ achievement_pyrepoints += 1
                $ creeks_reputation += 1
                $ efren_friendship += 1
                menu:
                    '“Hwat in the troll shit?” He steps away as you try to handle the sack. “I... Hwat?”
                    '
                    '“Take it and burn it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take it and burn it.”')
                        menu:
                            'He points at the ground and you place the sack there. He grabs it only to turn it around. “Let’s... {i}not{/i} show it to children before the burning,” he whispers, but after a few breaths his confidence returns. “Her siblings and uncle will be glad she’s not coming back as an awoken.”
                            '
                            '“I’m glad.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad.”')
                                jump creeksefrenaboutmissinghunters02afterinteraction
                            '“Every human deserves a proper pyre.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every human deserves a proper pyre.”')
                                if pc_religion != "none" and pc_religion != "unknown":
                                    $ pc_faithpoints += 1
                                jump creeksefrenaboutmissinghunters02afterinteraction
            '“Something bad happened to {color=#f6d6bd}Vaschel{/color}.”' if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something bad happened to {color=#f6d6bd}Vaschel{/color}.”')
                jump creeksefrenaboutfindingvaschel01
            '“I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”' if shortcut_darkforest_furlesswolf and not quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t examine it, but I’m almost sure I saw {color=#f6d6bd}Vaschel’s{/color} shell.”')
                $ quest_missinghunters_vaschelfound = 3
                $ efren_friendship -= 1
                jump creeksefrenaboutfindingvaschel02alt
            '“Where would you start if you were me?”' if not efren_about_missinghunters_questions01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where would you start if you were me?”')
                jump efren_about_missinghunters_questions01alt
            '“Let’s say I were to find any of them. What should I tell them?”' if not efren_about_missinghunters_questions02 and not quest_missinghunters_reported:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find them. What should I tell them?”')
                jump efren_about_missinghunters_questions02alt
            '“Does your tribe often send lone hunters? Why not work in groups?”' if not efren_about_missinghunters_questions03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s say I were to find any of them. What should I tell them?”')
                jump efren_about_missinghunters_questions03alt
            'I still need to find Admon. (disabled)' if not quest_missinghunters_admonfound or (quest_missinghunters_admonfound and not quest_missinghunters_admonknown):
                pass
            'I still need to find Dalia. (disabled)' if not quest_missinghunters_daliafound:
                pass
            'I still need to find Vaschel. (disabled)' if not quest_missinghunters_vaschelknown or (quest_missinghunters_vaschelknown and not shortcut_darkforest_furlesswolf and quest_missinghunters_vaschelfound != 1):
                pass
            '“I’ll tell you if I find anything.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I find anything.”')
                jump creeksefrenafterinteraction01

    label creeksefrenaboutmissinghuntersgivingup01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s been many days since your friends left the village, {color=#f6d6bd}Efren{/color}. They aren’t coming back.”')
        $ quest_missinghunters_reported = 0
        if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3:
            $ quest_missinghunters_reported += 1
        if quest_missinghunters_reported == 0:
            $ efren_friendship -= 3
            $ creeks_reputation -= 3
            $ custom2 = "Shocked, he purses his lips, then scoffs at you. “You’re giving up? Without even trying to find them? Stick to the saddle, {i}roadwarden{/i}.” As he rolls his eyes, the wolf’s head tilts to the left."
        elif quest_missinghunters_reported == 1:
            $ efren_friendship -= 2
            $ creeks_reputation -= 2
            $ custom2 = "He purses his lips, but spares you a slow nod. “I’m grateful that you found one of us... But that’s not hwat I was hoping for. In stories, roadwardens are capable of more,” he sizes you up with an angry look. “The deal is off, {i}friend{/i}.”"
        elif quest_missinghunters_reported == 2:
            $ efren_friendship -= 1
            $ creeks_reputation -= 1
            $ custom2 = "He purses his lips, but gives you a slow nod. “Aye. You found two of us, and knowing that they didn’t protect each other, I think there’s no point in waiting. We may still be surprised, but...” He lowers the wolf’s head."
        elif quest_missinghunters_reported >= 3:
            jump creeksefrenaboutmissinghunters03
        menu:
            '[custom2]
            '
            '“I’m sorry for your loss.”' if quest_missinghunters_reported >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry for your loss.”')
                $ quest_missinghunters_gaveup = 1
                jump creeksefrenaboutmissinghunters03
            'I nod with a sigh.' if quest_missinghunters_reported >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod with a sigh.')
                $ quest_missinghunters_gaveup = 1
                jump creeksefrenaboutmissinghunters03
            'I nod. “I did as much as I could.”' if quest_missinghunters_reported < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I did as much as I could.”')
                $ quest_missinghunters_description03 = "This task wasn’t worth the effort."
                $ quest_missinghunters = 3
                $ renpy.notify("Quest completed: The Missing Hunters")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters{/i}')
                jump creeksefrenafterinteraction01
            'I shrug.' if quest_missinghunters_reported < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                $ quest_missinghunters_description03 = "This task wasn’t worth the effort."
                $ quest_missinghunters = 3
                $ renpy.notify("Quest completed: The Missing Hunters")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters{/i}')
                jump creeksefrenafterinteraction01

    label creeksefrenaboutmissinghunters03:
        menu:
            '“Well, we had a deal, and you did your part. Thanks, I think.” He puts an open palm on his forehead and closes his eyes. Once he notices that the wolf’s head obstructs his fingers, he takes it off. “{color=#f6d6bd}Vaschel{/color} liked this head,” his voice is empty. “He told me he’d get an even larger one. I...”
            \n\nHe looks at you. There are tears in his eyes, yet his voice is absent. “Yes, we had a deal. I’ll join you on your own venture when the time comes, but I need to first close this ordeal.” You ask him what he needs, but he puts on the hood and quirks his lips into a shadow of a smile. “Nothing from you, friend. I already spoke with the others. The wood is ready for a pyre, we’ve meat to roast. You did a lot for our li’l tribe, and we’d love to see you at our table. There may be some tears among us, but there will be laughter, songs, and enough of {color=#f6d6bd}Foggy’s{/color} casks to forget a thing or two.”
            '
            '“I can’t promise anything, but...”':
                label creeksefrenaboutmissinghunters03part2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t promise anything, but...”')
                menu:
                    'You suddenly realize the opportunity at hand. A group of vulnerable, dazed souls may open their ears to your requests. If you’re on their good side and know enough about them, it’ll be a perfect moment to offer them a covenant with {color=#f6d6bd}Hovlavan{/color}.
                    '
                    '“I’m sure I can spare an evening. I assume it’s {color=#f6d6bd}Elah{/color} who’s preparing it? I’ll speak with him when I’m ready.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sure I can spare an evening. I assume it’s {color=#f6d6bd}Elah{/color} who’s preparing it? I’ll speak with him when I’m ready.”')
                        $ quest_missinghunters_description01 = "When possible, I should speak with {color=#f6d6bd}Elah{/color} during the evening hours and participate in the parting rites."
                        $ quest_creekssupport = 1
                        $ renpy.notify("New entry: The Support of Creeks\nJournal updated: The Missing Hunters")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Creeks. Journal updated: The Missing Hunters{/i}')
                        $ efren_about_missinghunters_dayreported = day
                        $ questionpreset = "efren1"
                        menu:
                            '“Just don’t keep us waiting for too long, aye? I may be in your debt, but I want to put all of this behind me, focus on hwat’s to come.”
                            '
                            '(efren1 set)':
                                pass
