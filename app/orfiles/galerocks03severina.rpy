# "perfumed guard" - Antonius?
default severina_firsttime = 0 # Severina the headwoman
default severina_friendship = 0
default severina_dayofvisit = 0
default severina_firstattitude = 0
default severina_treshholdcheck = 0 # day
default severina_annoyance_treshhold = 2
default severina_annoyance_treshhold_reached = 0 # day
default severina_annoyance = 0

# default severina_quest_akakios = 0
default severina_about_matchmaking_reward = 0

default severina_quest_lostmerchants = 0
default severina_quest_lostmerchants_receivedday = 0 # day
default severina_quest_lostmerchants_stayingsilent = 0
default severina_quest_lostmerchants_fallentree = 0
default severina_quest_lostmerchants_clues = 0

default severina_about_keytowatchtower = 0
default severina_about_oldtunnel = 0
default severina_about_clearedoldtunnel = 0
default severina_about_pastrobbery = 0
default severina_about_asterion1 = 0
default severina_about_asterion2 = 0
default severina_about_galerocks = 0
default severina_about_undead1 = 0
default severina_about_undead2 = 0
default severina_about_nomoreundead = 0
default severina_about_priest = 0
default severina_about_plague1 = 0
default severina_about_plague2 = 0
default severina_about_bandits = 0
default severina_about_orentius = 0
default severina_about_greenmountaintribe = 0
default severina_about_highisland = 0
default severina_about_steephouse = 0
default severina_about_galerockshelpingoldpagos1 = 0
default severina_about_galerockshelpingoldpagos2 = 0

label severina_firsttimeALL: # {color=#f6d6bd}Severina{/color}, the headwoman.
    label severina_01firsttimepositive:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show galerocksoverlay keep at basicfade
        $ galerocks_work_hours += 2
        menu:
            '“{color=#f6d6bd}Our headwoman{/color} is in the keep,” says a young basket weaver with legs too short and thin for her to stand on. “But she’s not very patient with strangers, she’s not. Or with loud neighbors.”
            \n\nYou thank her with a nod and head to the hill on the western bank, walking past the big kitchen. The steep path leads through an open, unguarded gate. As you look around the yard, you notice a few pigeons running around, keenly observed by a pet griffon tied to a wooden beam; some drying underwear hanging from a rope; a spiked flail, leaning against the wall carelessly; and a knocked over bucket lying in a puddle of water.
            \n\nThe place may be messy, but is not impaired in its function. Preparing it for defense wouldn’t take longer than a few minutes, and judging by the wall-walk of the bailey, it could stand an attack from a large squad of soldiers. The current state of the place makes you think of {color=#f6d6bd}Hovlavan{/color}, whose stronghold yards and temple walls are often surrounded by small peddlers, a few of which are even allowed to set up their stalls. As long as they don’t hinder anyone else’s tasks, they are allowed to pursue the scarce scraps of open space.
            '
            'I look at the keep.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the keep.')
                jump severina_firsttime01

    label severina_01firsttimenegative:
        show galerocksoverlay keep at basicfade
        $ galerocks_work_hours -= 5
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'A young basket weaver with legs too short and thin for her to stand on scoffs at your question. “Ehm, you don’t even know her name, or that we call her a {color=#f6d6bd}headwoman{/color}? Like all them outsiders, you know nothing of our customs, yet think you can bother us.” Before you respond, she looks at the white building on the hill. “She’s in the keep. Scat.”
            \n\nYou head to the western bank and walk past the big kitchen. The steep path leads through an open, unguarded gate. As you look around the yard, you notice a few pigeons running around, keenly observed by a pet griffon tied to a wooden beam; some drying underwear hanging from a rope; a spiked flail, leaning against the wall carelessly; and a knocked over bucket lying in a puddle of water.
            \n\nThe place may be messy, but is not impaired in its function. Preparing it for defense wouldn’t take longer than a few minutes, and judging by the wall-walk of the bailey, it could stand an attack from a large squad of soldiers. The current state of the place makes you think of {color=#f6d6bd}Hovlavan{/color}, whose stronghold yards and temple walls are often surrounded by small peddlers, a few of which are even allowed to set up their stalls. As long as they don’t hinder anyone else’s tasks, they are allowed to pursue the scarce scraps of open space.
            '
            'I look at the keep.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the keep.')
                jump severina_firsttime01

    label severina_firsttime01:
        $ severina_firsttime = 1
        $ galerocks_npcsmet += 1
        $ world_known_npcs += 1
        $ quarters += 1
        if severina_dayofvisit != day:
            $ severina_annoyance = 0
            $ severina_dayofvisit = day
        menu:
            'The bright walls stand out from the other structures in the village, and as far as you can tell, the current layer of whitewash is still fresh. There must be at least three floors inside, enough space to contain more than a hundred people, though without much between them. There are arrowslits in the walls, and the roof is surrounded by a fence-like barrier, a perfect spot for boulder throwers and archers.
            \n\nThe large entrance door is ajar, with a wrinkled man sitting on a pillow placed on the stairs. He’s not wearing a gambeson, but the fine, steel sickle sword at his side makes it clear he’s not just a regular guard. He stops what he was doing, carving a figurine from a log, and stands up to greet you. “Cheers, roadwarden. {color=#f6d6bd}Severina{/color} was told about your arrival. Follow me.” He may be old, but he is tall, with the long and thin arms of a seafolk, a neatly groomed beard, and his gray hair in a ponytail. As you follow him, you’re hit by the strong scent of cloves.
            '
            'I climb up the stairs.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the stairs..')
                show areapicture galerockskeep01 at basicfade
                hide galerocksoverlay
                hide galerocksboat
                menu:
                    'The door is thick and can be barricaded with two wooden bars. The hall is filled with benches, some of which are placed on top of the others, giving a bit more space for now. There is one path to the next floor, suspiciously covered with planks.
                    \n\nThe chamber is free of the roaring of the river, the shouts of workers, the chaos of animals, or the smell of cooked food. The room is well-lit both by sunlight and candles, and quite drafty, though you still smell perfumes and aging wood. You doubt anyone lives here, or even uses this room for dining.
                    \n\n“The roadwarden is here,” says the guard and approaches the desk, standing between you and the old woman sitting behind it.
                    '
                    'I take a closer look at her.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at her.')
                        menu:
                            'So far, she hasn’t spared you as much as a glance. She’s writing on a large wax tablet, with a stylus as large as a dagger, and since she’s a bit stooped, you see her only from the chest up. She’s wearing a thick, warm dress in the color of a cherry, and an even darker, modest hat that’s covering her hair. She could be older than seventy, yet her face and hands have been spared from scars harsher than some pockmarks carved by illnesses. If you were to encounter her in {color=#f6d6bd}Hovlavan{/color}, you would expect her to be an official, or maybe a rich scribe.
                            \n\nSome of her belongings, however, wouldn’t be found at the city’s desks. The wax of her tablet isn’t dyed; instead of keeping water in a cup, she has a large, colorful seashell; and the winged hourglass placed on a stone stand is made of dried seaweed.
                            '
                            'I glance at the young woman who sits in the corner.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the young woman who sits in the corner.')
                                $ at_activate = 1
                                $ at = 0
                                menu:
                                    'Her crossbow is pointing at you. The resemblance between her and the elder is stunning, though she’s slim and a bit taller, and wears a simple, dark-blue and black woolen tunic. While she’s resting on a chair, she looks at you almost without blinking, with hardly any movement, like a cat staring at a rat, trying to judge if you’re defenseless prey, or a threat.
                                    '
                                    ' (disabled)' ( condition="at == 0" ):
                                        pass
                                    '“It’s nice to meet you, {color=#f6d6bd}Severina{/color}. I came here to see if your village needs any help from a roadwarden.”' ( condition="at == 'friendly'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “It’s nice to meet you, {color=#f6d6bd}Severina{/color}. I came here to see if your village needs any help from a roadwarden.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She raises her violet eyes, but only for a moment. “Where do you think you are, outsider? Some lost tribe desperate for help from adventurers and vagabonds? Our village carries blood older than {i}your{/i} city, it does, and we’ve endured hardships you couldn’t imagine.”\n\nHer accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words.\n\n“Better tell me what you want from {i}my{/i} people, and scat.” Her face shifts into indifference, and, still holding her stylus, she once against bends over her tablet."
                                        $ severina_friendship -= 1
                                        $ severina_firstattitude = "friendly"
                                        jump severina_firsttime02
                                    'I smile and spread my arms. “Considering the effort put into building this keep, I expected a bit of a larger garrison.”' ( condition="at == 'playful'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I smile and spread my arms. “Considering the effort put into building this keep, I expected a bit of a larger garrison.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She freezes for a moment, then scowls at you with her violet eyes, with lips twitching from anger and fingers clenched around her stylus. “You’ve spent merely a few breaths in our village and think we’re interested in learning how {i}you{/i} judge what we do, and how we do it?” You try to explain that it was just a joke, but are then welcomed with a long, awkward pause. “Speak what you must, outsider, and scat.”\n\nHer accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words.\n\nShe puts away her stylus, takes a deep breath, and clasps her hands on the desk, observing you like a hawk."
                                        $ severina_friendship -= 2
                                        $ severina_firstattitude = "playful"
                                        jump severina_firsttime02
                                    '“Greetings.”' ( condition="at == 'distanced'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “Greetings.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She raises her violet eyes slowly and looks at you kindly, putting away her stylus. “Outsider,” she nods gently. “I expect there’s something only {i}I{/i} can help you with.” After a short pause, she clasps her hands on the desk. “Let’s hear it.”\n\nHer accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words."
                                        $ severina_firstattitude = "distanced"
                                        $ severina_friendship += 1
                                        jump severina_firsttime02
                                    '“Cheers, headwoman.”' ( condition="at == 'distanced'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “Cheers, headwoman.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She raises her violet eyes slowly and looks at you kindly, putting away her stylus. “Cheers, roadwarden,” she speaks with a hint of amusement, but it lasts only so long as those two words. “I expect there’s something only {i}I{/i} can help you with.” After a short pause, she clasps her hands on the desk. “Let’s hear it.”\n\nHer accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words."
                                        $ severina_friendship += 1
                                        $ galerocks_work_hours += 1
                                        $ severina_firstattitude = "distanced"
                                        jump severina_firsttime02
                                    'I pat my axe. “You seem to be worried, yet you skipped a few important steps when it comes to security.”' ( condition="at == 'intimidating'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I pat my axe. “You seem to be worried, yet you skipped a few important steps when it comes to security.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She looks at the young woman aiming at you. “We’d rather have you feel as if you have a chance of fighting for yourself,” her violet eyes turn toward you, studying you carefully, “not peck a butcher’s hand like a squab. We won’t attack you, but neither do we trust you. Follow our customs, and you’ll be safe.”\n\nHer accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words.\n\n“If you want to chat, find yourself a gossiper, we have enough old people in the village. But if there’s something only {i}I{/i} can help you with, speak.” She puts away her stylus and clasps her hands on the desk, observing you gently, but also glancing at the exit."
                                        $ severina_friendship += 1
                                        $ severina_firstattitude = "intimidating"
                                        jump severina_firsttime02
                                    '“I’m sorry to intrude while you’re busy, I won’t take much of your time.”' ( condition="at == 'vulnerable'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “I’m sorry to intrude while you’re busy, I won’t take much of your time.”')
                                        $ at_activate = 0
                                        $ at = 0
                                        $ custom1 = "She raises her violet eyes, but only for a moment. “I’m not interested in your apologies, and I don’t spend time chatting, barring merchants.” Her accent is not as thick as that among the younger villagers, keeping a shadow of the years when the guild had tighter ties with the peninsula, but since she has no teeth, you have to think for a moment before you recognize some of her words. “What do you want?”\n\nHer face slowly shifts into indifference, and, still holding her stylus, she once again bends over her tablet."
                                        $ severina_friendship -= 1
                                        $ severina_firstattitude = "vulnerable"
                                        jump severina_firsttime02

    label severina_firsttime02:
        if pc_goal_iwantnewlife_galerocks:
            $ severina_annoyance_treshhold = 20
        elif appearance_charisma >= 2:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 8
            else:
                $ severina_annoyance_treshhold = 6
        elif appearance_charisma <= -1:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 4
            else:
                $ severina_annoyance_treshhold = 2
        else:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 6
            else:
                $ severina_annoyance_treshhold = 4
        $ questionpreset = "severina1"
        menu:
            '[custom1]
            '
            '(severina1 set)':
                pass

label severina_01:
    if severina_dayofvisit != day:
        $ severina_annoyance = 0
        $ severina_dayofvisit = day
    if severina_treshholdcheck != day:
        $ severina_treshholdcheck = day
        if appearance_charisma >= 2:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 8
            else:
                $ severina_annoyance_treshhold = 6
        elif appearance_charisma <= -1:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 4
            else:
                $ severina_annoyance_treshhold = 2
        else:
            if galerocks_reputation+severina_friendship >= 8:
                $ severina_annoyance_treshhold = 6
            else:
                $ severina_annoyance_treshhold = 4
    if severina_annoyance_treshhold_reached == day:
        show galerocksoverlay keep at basicfade
        menu:
            'You ascend the hill. The guard stands up and puts his woodwork on his pillow, but then closes the door and stands in your way. “{color=#f6d6bd}Severina{/color} is tired from your questions and problems, roadwarden. You’re asked to visit her another day.”
            '
            'I leave the hill.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the hill.')
                jump galerocksafterinteraction01
    else:
        hide galerocksoverlay
        hide galerocksboat
        show areapicture galerockskeep01 at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You ascend the hill. The guard stands up and puts his woodwork on his pillow, then asks you to wait. You hear his and the headwoman’s voices coming from the hall, and once the man returns, he nods gently. “You’re asked to enter.”
            '
            'I follow him inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him inside.')
                if whitemarshes_attacked and whitemarshes_attack_companion_galerocks and not severina_about_nomoreundead:
                    $ severina_about_nomoreundead = 1
                    if whitemarshes_nomoreundead:
                        if orentius_convinced:
                            $ questionpreset = "severina1"
                            $ severina_friendship += 2
                            menu:
                                '{color=#f6d6bd}Severina{/color} puts away her writing instruments and looks at you kindly. “I’m glad to see you in good health, we’re most grateful for what you did in {color=#f6d6bd}White Marshes{/color},” her violet eyes smile gently. “Not only did you make the danger disappear, you also saved the bridge between our villages.” She notes something in a wax tablet, and her voice gets close to a whisper. “Actually, we may need to share some fish with them, chiefly since {color=#f6d6bd}Thais{/color} didn’t stop herself from pillaging...”
                                '
                                '(severina1 set)':
                                    pass
                        elif orentius_banished:
                            $ questionpreset = "severina1"
                            $ severina_friendship += 1
                            menu:
                                '{color=#f6d6bd}Severina{/color} puts away her writing instruments and looks at you gently. “If you’re here to get my thanks for what you did in {color=#f6d6bd}White Marshes{/color},” her lips flinch, “then I guess you deserve them. I’m sad we had to torch the bridge between our villages, but better this than facing danger that would be too great for us to handle on our own.”
                                '
                                '(severina1 set)':
                                    pass
                        elif whitemarshes_destroyed:
                            $ questionpreset = "severina1"
                            $ severina_friendship += 0
                            menu:
                                '{color=#f6d6bd}Severina{/color} puts away her writing instruments and looks at you keenly. “The news of what happened in {color=#f6d6bd}White Marshes{/color} brought me great sorrow. Our woods have seen way too many deaths since the end of the war, they did.”
                                '
                                '(severina1 set)':
                                    pass
                    else:
                        $ questionpreset = "severina1"
                        $ severina_friendship -= 1
                        menu:
                            '{color=#f6d6bd}Severina{/color} puts away her writing instruments and frowns. “After what happened in {color=#f6d6bd}White Marshes{/color}, I hope you’re bringing some good news.”
                            '
                            '(severina1 set)':
                                pass
                else:
                    if severina_annoyance_treshhold == 8:
                        $ custom1 = "{color=#f6d6bd}Severina{/color} puts away her writing instruments and looks at you with a gentle smile. “Is everything alright?”"
                    elif severina_annoyance_treshhold == 6:
                        $ custom1 = "{color=#f6d6bd}Severina{/color} puts away her writing instruments and looks at you keenly. “What’s the matter?”"
                    elif severina_annoyance_treshhold == 4:
                        $ custom1 = "{color=#f6d6bd}Severina{/color} puts away her writing instruments and sighs, but doesn’t say anything. Her violet eyes are absent."
                    elif severina_annoyance_treshhold == 2:
                        $ custom1 = "{color=#f6d6bd}Severina{/color} puts away her writing instruments, glances at you, then frowns. The closer you get, the more annoyed she seems to be, but she says nothing."
                    $ questionpreset = "severina1"
                    menu:
                        '[custom1]
                        '
                        '(severina1 set)':
                            pass

label severina_afterinteraction01:
    if severina_annoyance_treshhold_reached == day:
        $ severina_friendship -= 1
        $ questionpreset = "severina1"
        menu:
            'She observes you without a word, but her fingers are tapping on the table. The guard gives you a telling look.
            '
            '(severina1 set)':
                pass
    elif severina_annoyance >= severina_annoyance_treshhold:
        $ severina_annoyance_treshhold_reached = day
        menu:
            '“My patience runs short, outsider,” {color=#f6d6bd}Severina{/color} gestures for you to pause. “Are you sure other matters can’t wait till tomorrow?”
            '
            '“Fine. Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Farewell.”')
                jump galerocksafterinteraction01
            '“There’s something else we need to discuss.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s something else we need to discuss.”')
                $ questionpreset = "severina1"
                menu:
                    '“We {i}need{/i} to, do we now,” she says through clenched teeth. “And what is it?”
                    '
                    '(severina1 set)':
                        pass
    else:
        $ questionpreset = "severina1"
        menu:
            'She glances at the exit.
            '
            '(severina1 set)':
                pass

label severina_rewards01:
    menu:
        '“Right. You worked for us, now I can tell one of my neighbors to overlook the usual fees or duties they’d ask of you. Do you need anyone’s help?”
        '
        '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
            $ galerocks_food_free = 1
            $ custom1 = "“In that case, I’ll speak with {color=#f6d6bd}Porcia{/color}, our head cook. You’ll find her just down the path, close to the hill.”"
            jump severina_rewards02
        '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
            $ galerocks_fulvia_knowsabout = 1
            $ galerocks_sleep_free = 1
            $ custom1 = "“Very well. Speak with {color=#f6d6bd}Fulvia{/color} in the evening, she should have a room to spare. She’s in the building just at the edge of the small vegetable field, close to the gate.”"
            jump severina_rewards02
        '“Maybe five free repairs of my gambeson?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
            $ galerocks_armorer_free += 5
            $ custom1 = "“Then I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor. She’s close to the hill we’re on. You need to take the path to the left, you’ll find her behind the dining tables.”"
            jump severina_rewards02
        '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
            $ galerocks_bath_free = 1
            $ custom1 = "She nods with a gentle smile. “{color=#f6d6bd}Aquila{/color} helps us with water, and he can ask someone to wash your clothes. His work has him walking around the entire village, but look for him on the eastern bank, close to the pier.”"
            jump severina_rewards02
        '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
            $ galerocks_navica_boat_price_base -= 10
            $ custom1 = "“I doubt it, but very well. I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker. On most days, she works with the carpenters, on the eastern bank.”"
            jump severina_rewards02
        '“I don’t need any favors. Just make sure everyone learns that I’m useful.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure everyone learns that I’m useful.”')
            $ galerocks_reputation += 2
            $ custom1 = "“You won’t buy fish merely with fame,” she starts slowly, but then nods. “I’ll mention it soon to the council of our elders and head workers.”"
            jump severina_rewards02

    label severina_rewards02:
        menu:
            '[custom1]
            '
            '“Great.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great.”')
                jump severina_afterinteraction01

    label severina_rewardsafterdebate01:
        menu:
            '[custom1]
            '
            '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
                $ galerocks_food_free = 1
                $ custom1 = "“In that case, I’ll speak with {color=#f6d6bd}Porcia{/color}, our head cook. You’ll find her just down the path, close to the hill.”"
                jump severina_rewards02
            '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
                $ galerocks_fulvia_knowsabout = 1
                $ galerocks_sleep_free = 1
                $ custom1 = "“Very well. Speak with {color=#f6d6bd}Fulvia{/color} in the evening, she should have a room to spare. She’s in the building just at the edge of the small vegetable field, close to the gate.”"
                jump severina_rewards02
            '“Maybe five free repairs of my gambeson?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
                $ galerocks_armorer_free += 5
                $ custom1 = "“Then I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor. She’s close to the hill we’re on. You need to take the path to the left, you’ll find her behind the dining tables.”"
                jump severina_rewards02
            '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
                $ galerocks_bath_free = 1
                $ custom1 = "She nods with a gentle smile. “{color=#f6d6bd}Aquila{/color} helps us with water, and he can ask someone to wash your clothes. His work has him walking around the entire village, but look for him on the eastern bank, close to the pier.”"
                jump severina_rewards02
            '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
                $ galerocks_navica_boat_price_base -= 10
                $ custom1 = "“I doubt it, but very well. I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker. On most days, she works with the carpenters, on the eastern bank.”"
                jump severina_rewards02
            '“I don’t need any favors. Just make sure everyone learns that I’m useful.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure everyone learns that I’m useful.”')
                $ galerocks_reputation += 2
                $ custom1 = "“You won’t buy fish merely with fame,” she starts slowly, but then nods. “I’ll mention it soon to the council of our elders and head workers.”"
                jump severina_rewards02

        label severina_rewardsafterdebate02:
            menu:
                '[custom1]
                '
                'I thank her and go down the hill.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great.”')
                    jump severina_afterinteraction01

label galerocksleavingseverina01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Farewell.')
    if (severina_friendship+galerocks_reputation) >= 10 and item_ironingot_sold_galerocks and severina_about_clearedoldtunnel and quest_galerockssupport == 2 and not pc_goal_iwantnewlife_galerocks:
        $ pc_goal_iwantnewlife_galerocks = 1
        if pc_goal == "iwanttostartanewlife":
            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
        if galerocks_navica_boat_price_base >= 10:
            $ galerocks_navica_boat_price_base -= 10
        menu:
            'Before you leave the hall, {color=#f6d6bd}Severina{/color} asks you to wait. “The people of our village are sharing good rumors about you,” she starts. “Quite a feat. And now that we’ll try to invite more merchants, we may need help on the roads around the tunnel, and therefore, a skilled rider. Chiefly one honest enough to bring us our lost ingot, instead of selling it at the nearest inn.”
            \n\nShe looks away as she gets back to her scrolls and tablets. “You are free to visit us again, once you’re done in the city. We’ll offer you a regular job, daily meals, and a warm bed. That’s all.”
            \n\nEven though she pretends to ignore you, both the crossbowwoman and the nearby guard send you warm smiles.
            '
            'I nod to them and walk away in silence.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to them and walk away in silence.')
                jump galerocksafterinteraction01
            'I smile back at them. “I’ll consider it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at them. “I’ll consider it.”')
                jump galerocksafterinteraction01
    elif ((severina_friendship*2)+galerocks_reputation+appearance_charisma) >= 10 and not severina_about_pastrobbery and not item_ironingot_sold_galerocks:
        $ severina_about_pastrobbery = 1
        $ galerocks_pastrobbery = 1
        menu:
            'Before you leave the hall, {color=#f6d6bd}Severina{/color} asks you to wait. “The people of our village are sharing good rumors about you,” she starts. “Quite a feat, it is. If you’re as much of a hard worker as I’ve heard, maybe you’ll find a way to restore something we lost to an {i}actual{/i} vagabond. Not a young lad, called himself {color=#f6d6bd}Pyrrhos{/color}. Was staying with us almost half a summer ago, and one day left before sunrise, carrying away our iron ingot.” Her granddaughter gives her a silent, but pained look. “If he had any sort of wits, I’m sure he left the peninsula a long time ago, through the eastern route. Or died trying. But maybe he was dumber than I thought.”
            \n\nYou ask what exactly she wants you to do, and she responds without hesitation. “Merely return the ingot. It was nothing more than crude iron, not something to murder each other for, but still,” she points at you with her stylus. “A sin worthy of a coward. And believe me, not the first robbery that’s happened to us.”
            '
            'I clear my throat. “Right! I’ll let you know if I find it.”' if item_ironingot_sold_pelt or item_ironingot_sold_howlers or item_ironingot_sold_whitemarshes or item_ironingot_sold_greenmountain or pyrrhos_debt:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “Right! I’ll let you know if I find it.”')
                jump galerocksafterinteraction01
            'I think about the blood I found at his shelter. There was no ingot there. “I’ll let you know.”' if quest_escortpyrrhos == 3 and pyrrhos_about_himself and not item_ironingot:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the blood I found at his shelter. There was no ingot there.”')
                jump galerocksafterinteraction01
            '“...I think I’ve already found it. Let me bring it here.”' if item_ironingot:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...I think I’ve already found it. Let me bring it here.”')
                jump severina_receivesironingot01after
            'I nod. “I’ll let you know if I find it.”' if not item_ironingot_sold_pelt and not item_ironingot_sold_howlers and not item_ironingot_sold_whitemarshes and not item_ironingot_sold_greenmountain and not pyrrhos_debt and not (quest_escortpyrrhos == 3 and pyrrhos_about_himself == 2) :
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I’ll let you know if I find it.”')
                jump galerocksafterinteraction01
    else:
        jump galerocksafterinteraction01

label severina_about_galerocks01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you tell me a bit about {color=#f6d6bd}Gale Rocks{/color}?”')
    $ severina_about_galerocks = 2
    $ severina_annoyance += 1
    menu:
        'She speaks slowly, with a kindness someone may show an annoying brat that has one last chance to learn from their mistake. “Do I look like someone who’d be interested in spending time as a guide, or a telltale?” Before you answer, she starts to move around a few small packages, and looks inside one. “Scat, spend some time among our walls. Speak with the fishers, the artisans. All them lads and lasses whose blood keeps the shell of our village alive.”
        '
        'I sigh.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh.')
            jump severina_afterinteraction01

label severina_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are your thoughts on {color=#f6d6bd}Cassia{/color}?”')
    $ quest_recruitahunter_spokento_severina = 1
    $ severina_annoyance += 1
    menu:
        '“The thought I’m bearing right now is that I’d rather not spread rumors about those I look after.” Her annoyed eyes contradict her calm voice. “Can’t you bother the elders with such questions? Or speak with {color=#f6d6bd}Petronius{/color}, the gossip. He’ll be happy to share with you all the dirty laundry he touched.”
        '
        '“Maybe I will.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe I will.”')
            jump severina_afterinteraction01

label severina_about_keytowatchtower01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to get inside the watchtower standing at the eastern road.”')
    $ severina_about_keytowatchtower = 1
    if severina_friendship+galerocks_reputation+appearance_charisma < 6:
        $ severina_annoyance += 1
        $ questionpreset = "severina1"
        menu:
            'She and the perfumed guard exchange looks. “Why would I give {i}you{/i} a key?” You mention that looking after roadside shelters is a part of your responsibilities, and she smirks, raising her hands slightly. “Ah, you don’t say? We’re not in {color=#f6d6bd}Old Págos{/color}, one’s {i}duty{/i} means nothing here until a soul proves they can be trusted.”
            '
            '(severina1 set)':
                pass
    else:
        $ severina_about_keytowatchtower = 2
        $ severina_annoyance += 2
        $ item_watchtowerkey = 1
        $ renpy.notify("You received an iron key.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received an iron key.{/i}')
        menu:
            '“Why would I give {i}you{/i} a key?” You mention that looking after roadside shelters is a part of your responsibilities. She and the perfumed guard exchange looks, and once he confirms that they have a few spare keys at hand, she asks her granddaughter to fetch one. Soon, a cold iron object, not much larger than your finger, is placed in your hand. “I trust you with it because I’ve heard good things about you, I have,” adds {color=#f6d6bd}Severina{/color}. “But don’t expect me to give you another one if you lose it.”
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump severina_afterinteraction01
    label severina_about_keytowatchtower02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I borrow the key to the watchtower?”')
        $ severina_about_keytowatchtower = 2
        $ severina_annoyance += 1
        $ item_watchtowerkey = 1
        $ renpy.notify("You received an iron key.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received an iron key.{/i}')
        menu:
            'She nods. “I’ve heard good things about you, I have, so I’ll trust you with a spare one. But don’t expect me to give you another one if you lose it.” She asks her granddaughter to fetch it, and after a minute or so, the cold iron object, not much larger than your finger,is placed in your hand.
            '
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump severina_afterinteraction01

label severina_receivesironingot01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I believe this ingot belongs to your people.”')
    label severina_receivesironingot01after:
        $ severina_about_pastrobbery = 2
        $ item_ironingot_sold_galerocks = 1
        $ pc_goal_iwanttohelppoints += 1
        $ galerocks_reputation += 3
        $ severina_friendship += 2
        $ severina_annoyance -= 1
        menu:
            'She opens her toothless mouth in silence, and her granddaughter stands up to have a better view. “And what are we to do with it now?” {color=#f6d6bd}The guard{/color} laughs. “Put it on a socle, name it {i}Honest Soul{/i}?”
            \n\n{color=#f6d6bd}Severina{/color} knocks on the ingot with her knuckles, then reaches for a small sack on her desk. “Make the nails we need, of course. I already wrote this iron off, I wouldn’t have guessed it would take one traveler to fix the misdeeds of another. Ten coins is about half the price you would get from other traders, and a fair finder’s fee, I think.”
            \n\nShe doesn’t wait for your response, asking the crossbowwoman to pass you the pouch and take the ingot away, to the armory. As her granddaughter runs up the stairs, you notice that every plank she steps on lets out a loud creak - no doubt on purpose.
            '
            'I nod to thank her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to thank her.')
                $ item_ironingot -= 1
                $ coins += 10
                show screen notifyimage( "You lost the iron ingot. +10", "gui/coin2.png" )
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the iron ingot. +10 {image=cointest}{/i}')
                menu:
                    '“I can also tell one of my neighbors to overlook the usual fees or duties they’d ask of you. Do you need anyone’s help?”
                    '
                    '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
                        $ galerocks_food_free = 1
                        $ custom1 = "“In that case, I’ll speak with {color=#f6d6bd}Porcia{/color}, our head cook. You’ll find her just down the path, close to the hill.”"
                        jump severina_rewards02
                    '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
                        $ galerocks_fulvia_knowsabout = 1
                        $ galerocks_sleep_free = 1
                        $ custom1 = "“Very well. Speak with {color=#f6d6bd}Fulvia{/color} in the evening, she should have a room to spare. She’s in the building just at the edge of the small vegetable field, close to the gate.”"
                        jump severina_rewards02
                    '“Maybe five free repairs of my gambeson?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
                        $ galerocks_armorer_free += 5
                        $ custom1 = "“Then I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor. She’s close to the hill we’re on. You need to take the path to the left, you’ll find her behind the dining tables.”"
                        jump severina_rewards02
                    '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
                        $ galerocks_bath_free = 1
                        $ custom1 = "She nods with a gentle smile. “{color=#f6d6bd}Aquila{/color} helps us with water, and he can ask someone to wash your clothes. His work has him walking around the entire village, but look for him on the eastern bank, close to the pier.”"
                        jump severina_rewards02
                    '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
                        $ galerocks_navica_boat_price_base -= 10
                        $ custom1 = "“I doubt it, but very well. I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker. On most days, she works with the carpenters, on the eastern bank.”"
                        jump severina_rewards02
                    '“I don’t need any favors. Just make sure everyone learns that I’m useful.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure everyone learns that I’m useful.”')
                        $ galerocks_reputation += 2
                        $ custom1 = "“You won’t buy fish merely with fame,” she starts slowly, but then nods. “I’ll mention it soon to the council of our elders and head workers.”"
                        jump severina_rewards02

label severina_about_oldtunnel01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the tunnel, south from here?”')
    $ severina_about_oldtunnel = 1
    $ severina_annoyance += 2
    menu:
        '“I can tell you that the venerable {color=#f6d6bd}digger Iuno{/color} will tell you more about it than you want to hear, she will. Before the war, it used to be crossed every ten, twenty days, enough for us to keep it garrisoned, but with how little use it now has, I’d be mad to ask any of our youth to throw themselves at the beasts that live there.”
        \n\nShe glances at an open pouch that’s lying just nearby, with a few dragon bones sticking out of it. Her toothless grimace is hard to read. “And don’t offer me your {i}services{/i} to merely get rid of the awoken. I need long-term solutions, not violence, and sooner or later another threat will take their place. It may just as well stay {i}occupied{/i}, at least no vagabonds will take it over.”
        '
        '“If you say so.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you say so.”')
            jump severina_afterinteraction01

    label severina_about_clearedoldtunnel01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put the gate key on her desk. “The undead from your tunnel are gone.”')
        $ severina_friendship += 1
        $ galerocks_reputation += 2
        $ severina_about_clearedoldtunnel = 1
        $ item_oldtunnelkey = 0
        $ renpy.notify("You lost the bronze key.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the bronze key.{/i}')
        if severina_about_oldtunnel:
            $ custom1 = "“You faced this threat for no good reason, I already told you I wasn’t planning to work on the tunnel.” "
        else:
            $ severina_about_oldtunnel = 1
            $ custom1 = "“You faced this threat for no good reason. I need long-term solutions, not witless violence, and sooner or later another threat will take the place of the awoken. The tunnel could just as well stay {i}occupied{/i}, at least no vagabonds would take it over.”\n\n"
        if not quest_ruins_10yclue10 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            'As she drags the key over the desk, it looks comically large in her tiny hand. “Now would you look at that,” she says to no one in particular, then looks you in the eyes. [custom1]She scratches the desk with the key, thinking. “But I ain’t going to deny that it opens {i}some{/i} opportunities. My neighbors are going to appreciate your {i}selfless{/i} efforts.” She tries to push the key into the nearby bags, but is suddenly interrupted by the voice of the {color=#f6d6bd}perfumed guard{/color}, who speaks directly to you.
            \n\n“I used to be the head of the garrison that kept the tunnel safe,” he steps toward you, “until it was left to itself ten years ago, against my advice. I don’t care if you’re a roadwarden, an adventurer, or a drifter. You deserve a reward, and if {color=#f6d6bd}our headwoman{/color} ain’t willing to reward your contribution,” he reaches for the belt that holds his sickle sword, and {color=#f6d6bd}Severina{/color}, with unmasked frustration, tells him to hold it.
            \n\n“Don’t get so dramatic. Here,” she tosses a small pouch, and it land at the edge of the desk. “Ten should be enough, considering you weren’t {i}asked{/i} to move as much as a finger. Scat and talk to {color=#f6d6bd}Iuno{/color}, our digger. She’ll have some grand plans coming to her soul, maybe you’ll manage to keep them on a leash.”
            '
            '“I’ll talk with her.”' if not galerocks_iuno_about_oldtunnel_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll talk with her.”')
                $ severina_annoyance += 1
                $ coins += 10
                show screen notifyimage( "+10", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+10 {image=cointest}{/i}')
                jump severina_afterinteraction01
            '“I already talked with her. I’m just here to leave the key with you.”' if galerocks_iuno_about_oldtunnel_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I already talked with her. I’m just here to leave the key with you.”')
                $ coins += 10
                show screen notifyimage( "+10", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+10 {image=cointest}{/i}')
                jump severina_afterinteraction01

label severina_about_asterion101:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you seen {color=#f6d6bd}Asterion{/color} recently? He’s also a roadwarden.”')
    $ severina_about_asterion1 = 1
    $ severina_annoyance += 2
    menu:
        'She shrugs and reaches for one of the candles, casting better light on one of her smaller wax tablets. “I know who he is, but I’ve only spoken with him a few times, and heard that he stopped visiting the village at the beginning of summer. If he was around, I would know about it, I would.”
        \n\nYou mention that you doubt a roadwarden would simply ignore a headwoman of such a large village, and she looks at the ceiling, chewing on her bottom lip. “I don’t know what you’re {i}trying{/i} to imply,” she says with a tone that won’t accept any discussion. “I had as much in common with him as I have with you. I don’t trust strangers with crucial tasks, and if a warden of any kind wants to demonstrate that they know what they’re doing, I invite them to survive a year or two before they bark.”
        '
        'I don’t respond.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t respond.')
            jump severina_afterinteraction01

    label severina_about_asterion202:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color} on {color=#f6d6bd}High Island{/color}.”')
        $ severina_about_asterion2 = 1
        $ severina_annoyance += 1
        $ questionpreset = "severina1"
        menu:
            'As you speak, she pours water from a pitcher to a seashell, and responds without looking at you. “Right. Well, he knew the rules, the same rules you broke,” she takes a sip and licks her wrinkled lips. “But I guess you’re still in one piece, so I won’t dwell upon it.”
            '
            '(severina1 set)':
                pass

label severina_about_matchmaking_reward01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I believe {color=#f6d6bd}Paulus{/color} and {color=#f6d6bd}Marina{/color} already talked with you.”')
    $ severina_annoyance += 1
    $ severina_about_matchmaking_reward = 1
    jump severina_rewards01

label severina_about_steephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I believe something awful happened to the village in the distant south, the one turned to ruins. Could you tell me anything about it?”')
    $ severina_about_steephouse = 1
    $ severina_annoyance += 1
    $ questionpreset = "severina1"
    menu:
        'A polite smile crosses her lips, while her violet eyes remain firm. “I’d rather not talk about it, alright.” After a moment of hesitation, she continues, but slowly. “A few of the hurt families are still with us, and we agreed to leave it to them if they were to seek retribution.”
        '
        '(severina1 set)':
            pass

label severina_about_highisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about {color=#f6d6bd}High Island{/color}.”')
    $ severina_about_highisland = 1
    $ description_highisland12 = "According to {color=#f6d6bd}Severina{/color}, the locals are forbidden to sail to this island."
    $ severina_annoyance += 1
    $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
    menu:
        '“Then you should ask someone interested in old tales. We forbid our fishers to swim near it, and our neighbors ain’t challenging us on this.” She reaches for one of the tablets and notes something quickly, and as she carries on, she sounds disinterested, more than frustrated. “The volcano there erupts rarely, and merely hits us with the tides. We have nothing to gain from those woods but claws and thorns, and even getting to the land is a dangerous task.”
        '
        '“Thanks.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
            jump severina_afterinteraction01

label severina_aboutthegreenmountaintribe01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard something about {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”')
    $ severina_about_greenmountaintribe = 1
    $ description_greenmountaintribe12 = "According to {color=#f6d6bd}Severina{/color}, her village refuses to talk about them out of respect."
    menu:
        '“Did you, now. Then find someone who holds them in little regard, for we promised to keep them safe from guests, we did,” she pauses, glancing at your blade. “Especially the armed cityfolk, I hope you understand.”
        \n\nYou try to learn anything else, but she runs out of patience quickly. “{color=#f6d6bd}Gale Rocks{/color} was one of the very few settlements that used to trade with {color=#f6d6bd}The Tribe{/color}, and I ain’t speak of merely the things I remember myself, but even some that happened {i}hundreds{/i} of years ago,” the proud words make her voice get stronger and louder. “{color=#f6d6bd}Hovlavan’s{/color} merchants won’t find anything there, and there are no roads for you to patrol. Forget about them, outsider.”
        '
        'I frown, but agree to change the topic.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown, but agree change the topic.')
            jump severina_afterinteraction01

label severina_about_undead01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some necromancers in the North.”')
    jump severina_about_undead01after
    label severina_about_undead01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are your thoughts about the necromancers in {color=#f6d6bd}White Marshes{/color}?”')
        jump severina_about_undead01after
    label severina_about_undead01after:
        $ severina_about_undead1 = 1
        $ description_whitemarshes01 = "A village of foragers and peat gatherers set among the western bogs."
        $ description_whitemarshes02 = "The locals use the awoken undead to do their bidding."
        $ description_whitemarshes11 = "According to {color=#f6d6bd}Severina{/color}, the village has gone through terrifying hunger."
        $ severina_annoyance += 1
        menu:
            'You almost jump away when the crossbowwoman shifts her position, but she turns out to just be uncomfortable with the way she’s sitting. {color=#f6d6bd}Severina{/color} smirks, but as she starts to speak, her voice grows worried.
            \n\n“What happens in {color=#f6d6bd}White Marshes{/color} is a sign of cowardice and weakness. I’ve seen my share of harsh years, and I... {i}sympathize{/i}, I do, with tribes that had to feed their people with tree bark, or decide which mother will eat enough to feed infants. But all them walking corpses will get out of the charms and murder their masters, like they always do, and instead of hunger and cold, they’ll face the end of their souls. All we can do is keep ourselves safe.”
            \n\nYou try to ask a few more questions, but to no avail. “We don’t really travel there often, stranger. And some of the knowledge we gathered on this place is for our ears alone.”
            '
            'I nod. She can’t trust that I will keep anything between us.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. She can’t trust that I will keep anything between us.')
                jump severina_afterinteraction01

    label severina_about_undead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Considering that the people of your village follow The Wright, I’m surprised you’re not pressured into taking action against the undead of {color=#f6d6bd}White Marshes{/color}.”')
        $ severina_about_undead2 = 1
        $ description_galerocks12 = "{color=#f6d6bd}Severina{/color} seems to be convinced that the villagers are close to being defenseless without their walls."
        $ severina_annoyance += 2
        menu:
            '“And what do you think we {i}ought{/i} to do? {i}Encourage{/i} them by taking their land, or startle their wild game? Maybe torch their roofs?” She takes an awkwardly long pause, yet as you start to answer, she instantly cuts in. “We have no plans to conquer or pillage their home, and while {i}some{/i} of us would like to take matters into their own hands, I ain’t risking our lives in battle with mere heretics. Without walls, we’ll have nothing to keep us safe.”
            '
            'I say nothing, expecting for her to interrupt me again.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing, expecting for her to interrupt me again.')
                jump severina_afterinteraction01

    label severina_about_orentius01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} of {color=#f6d6bd}Howler’s Dell{/color} is considering confronting {color=#f6d6bd}Orentius{/color}, the necromancer, directly. Will your people aid her in this task?”')
        $ severina_about_orentius = 1
        $ quest_orentius_thais_description03a06 = "{color=#f6d6bd}Severina{/color} of {color=#f6d6bd}Gale Rocks{/color} is not fully convinced, but is willing to send a group to discuss it."
        $ renpy.notify("Journal updated: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        if severina_about_undead2:
            $ custom1 = "“I was thinking about the things you said, roadwarden. Our late priest would never let go of the cruelties committed by the necromancers, he wouldn’t. Without him, the severance got easier, but it doesn’t make it right. I have to speak with the council first, but no matter what we decide, I think it’s time for a group of our fighters to experience {color=#f6d6bd}Howler’s{/color} hospitality. Tell {color=#f6d6bd}Thais{/color} she’ll have some explaining to do. The decision will be made when the time comes, but she’ll have my endorsement.”"
            $ severina_about_priest = 1
            $ severina_friendship += 1
        else:
            $ custom1 = "“Alright. I can’t answer without speaking with the council first, but no matter what we decide, I think it’s time for a group of our fighters to experience {color=#f6d6bd}Howler’s{/color} hospitality. Tell {color=#f6d6bd}Thais{/color} she’ll have some explaining to do. The decision will be made when the time comes.”"
            $ severina_annoyance += 1
        menu:
            'She purses her lips, then reaches for her seashell, taking a sip of water, and observing the exit. [custom1]
            '
            '“She’d rather have a direct {i}yes{/i} or {i}no{/i}, but as you wish.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’d rather have a direct {i}yes{/i} or {i}no{/i}, but as you wish.”')
                jump severina_afterinteraction01

label severina_about_nomoreundeadALL:
    label severina_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}White Marshes{/color}. The local necromancer has agreed to abandon his practice.”')
        $ severina_about_nomoreundead = 1
        $ severina_friendship += 2
        $ galerocks_reputation += 2
        $ severina_annoyance -= 1
        $ quarters += 1
        $ questionpreset = "severina1"
        menu:
            'She exchanges looks with her surprised guards, then reaches for a wax tablet. “Do tell.”
            \n\nShe interrupts your tale often, seeking lies and omissions. Finally, her violet eyes smile gently. “Not only did you deal with the danger, you saved the bridge between our villages.” She notes something on a wax tablet. “You’re free to spread the news,” she tells the man in front of the table, then looks at you. “We will catch a much deeper rest tonight, [pcname]. You’re exceeding expectations.”
            '
            '(severina1 set)':
                pass

    label severina_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}White Marshes{/color}. The local necromancer has been taken away from the village, but not before he turned his awoken into a pile of flesh.”')
        $ severina_about_nomoreundead = 1
        $ severina_friendship += 1
        $ galerocks_reputation += 1
        $ quarters += 1
        $ questionpreset = "severina1"
        menu:
            'She exchanges looks with her surprised guards, then reaches for a wax tablet. “Do tell.”
            \n\nShe interrupts your tale often, seeking lies and omissions. Finally, her lips flinch in a brief smile. “I guess you deserve our thanks. I’m sad you had to torch the bridge between our villages, but better this than facing danger that would be too great for us to handle on our own.”
            \n\nThe man in front of the table adjusts his belt. “Should I spread the news?”
            \n\n“Not yet,” she responds. “I need to think how to phrase it well,” she notes something on the wax tablet.
            '
            '(severina1 set)':
                pass

    label severina_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} has fallen, but it’s undead are going to roam through the North. You may want to work on your defenses, and soon.”')
        $ severina_about_nomoreundead = 1
        $ quarters += 1
        menu:
            'She exchanges looks with her surprised guards, then reaches for a wax tablet. “Do tell.”
            \n\nShe interrupts your tale often, seeking lies and omissions. When she speaks, her voice is cracking. “It brings me great sorrow, guess you deserve our thanks. Our woods have seen way too many deaths since the end of the war, they did.”
            \n\nThe man in front of the table adjusts his belt. “Should I spread the news?”
            \n\n“Not yet,” she responds. “I need to think how to phrase it well,” she notes something on the wax tablet. She starts to swing her stylus slightly, lost in her thoughts. “What do you think, outsider? Was this the only way?”
            '
            '“I’m not sure.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not sure.”')
                $ questionpreset = "severina1"
                menu:
                    '“We may never know,” she sighs.
                    '
                    '(severina1 set)':
                        pass
            '“No, but I can’t change the past.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No, but I can’t change the past.”')
                $ questionpreset = "severina1"
                menu:
                    '“I was just asking,” she pushes the tablet away.
                    '
                    '(severina1 set)':
                        pass
            '“Definitely.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Definitely.”')
                $ severina_friendship += 1
                $ questionpreset = "severina1"
                menu:
                    'She nods. “Then I’m glad you had confidence to rightly finish what you started.”
                    '
                    '(severina1 set)':
                        pass

label severina_about_plague1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The village of {color=#f6d6bd}Old Págos{/color} is struggling with a plague, and isolates itself from trade and travelers.”')
    $ severina_annoyance += 1
    $ severina_about_plague1 = 1
    $ oldpagos_plague_warnedplaces += 1
    $ galerocks_work_hours += 5
    menu:
        'She looks at the perfumed man, who’s standing with an open mouth. You glance at the crossbowwoman, who has lowered her weapon. {color=#f6d6bd}The headwoman{/color}, still without a word, leans forward, and rests her forehead on the back of her hand. Her guard tries to speak, but she looks at him with sorrow. “Let me think,” she states, and after less than a minute, tells him to gather the council once your meeting is over.
        '
        'I say nothing.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
            jump severina_afterinteraction01

    label severina_about_plague02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve helped to cure the plague of {color=#f6d6bd}Old Págos{/color}, but the seasons to come will be grim for them.”')
        $ severina_about_plague2 = 1
        $ quarters += 1
        $ galerocks_church_knowsabout += 1
        $ galerocks_reputation += 1
        $ severina_friendship += 1
        menu:
            '“What do you mean, {i}cure the plague{/i}?” She keeps her voice low, but the spark in her violet eyes betrays her utter shock. She clears her throat and rests her elbows on the desk. “Were they just getting cold?”
            \n\nYou try to tell her the entire story, and even though at first she stares at you from above her clasped fingers, she seems to get smaller and weaker each time you mention the old druid, or the mysterious altar at the edge of the swamp. Finally, she stares at the wax tablet, defeated rather than joyful.
            \n\n“May The Wright bless the kindness of that pagan,” the perfumed guard announces briskly. “As well as yours, roadwarden. You’ve helped our old friends in need, where we thought there was no hope. {color=#f6d6bd}Severina{/color},” he turns to the old woman, “let’s offer this stranger some help. Is there some labor you struggle within our village?” He smiles at you.
            '
            '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
                $ galerocks_food_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “In that case, I’ll speak with {color=#f6d6bd}Porcia{/color}, our head cook. You’ll find her just down the path, close to the hill.”"
                jump severina_rewards02
            '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
                $ galerocks_fulvia_knowsabout = 1
                $ galerocks_sleep_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “Very well. Speak with {color=#f6d6bd}Fulvia{/color} in the evening, she should have a room to spare. She’s in the building just at the edge of the small vegetable field, close to the gate.”"
                jump severina_rewards02
            '“Maybe five free repairs of my gambeson?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
                $ galerocks_armorer_free += 5
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor. She’s close to the hill we’re on. You need to take the path to the left, you’ll find her behind the dining tables.”"
                jump severina_rewards02
            '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
                $ galerocks_bath_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “{color=#f6d6bd}Aquila{/color} helps us with water, and he can ask someone to wash your clothes. His work has him walking around the entire village, but look for him on the eastern bank, close to the pier.”"
                jump severina_rewards02
            '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
                $ galerocks_navica_boat_price_base -= 10
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “I doubt it, but very well. I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker. On most days, she works with the carpenters, on the eastern bank.”"
                jump severina_rewards02
            '“I don’t need any favors. Just make sure everyone learns that I’m useful.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure everyone learns that I’m useful.”')
                $ galerocks_reputation += 2
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “You won’t buy fish merely with fame,” she starts slowly, but then nods. “I’ll mention it soon to the council of our elders and head workers.”"
                jump severina_rewards02

    label severina_about_plague02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The village of {color=#f6d6bd}Old Págos{/color} has been struggling with a plague. I’ve helped them overcome it, but the seasons to come will be grim for them.”')
        $ severina_about_plague1 = 1
        $ severina_about_plague2 = 1
        $ oldpagos_plague_warnedplaces += 1
        $ galerocks_church_knowsabout += 1
        $ galerocks_reputation += 1
        $ severina_friendship += 1
        $ quarters += 1
        menu:
            'She looks at the perfumed man, who’s standing with an open mouth. You glance at the crossbowwoman, who has lowered her weapon. {color=#f6d6bd}The headwoman{/color} leans forward, and rests her forehead on the back of her hand. “What do you mean, {i}overcome it{/i}?” She keeps her voice low. “Were they just getting cold?”
            \n\nYou try to tell her the entire story, and even though at first she stares at you from above her clasped fingers, she seems to get smaller and weaker each time you mention the old druid, or the mysterious altar at the edge of the swamp. Finally, she stares at the wax tablet, defeated rather than joyful.
            \n\n“May The Wright bless the kindness of that pagan,” the guard announces briskly. “And yours as well, roadwarden. We should call the council soon, but since you’ve helped our old friends in need... {color=#f6d6bd}Severina{/color},” he turns to the old woman, “let’s offer this stranger some help. Is there some labor you struggle within our village?” He smiles at you.
            '
            '“Free food to fill my belly, that’s all I need.”' if not galerocks_food_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Free food to fill my belly, that’s all I need.”')
                $ galerocks_food_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “In that case, I’ll speak with {color=#f6d6bd}Porcia{/color}, our head cook. You’ll find her just down the path, close to the hill.”"
                jump severina_rewards02
            '“I need a free room where I could spend the nights.”' if not galerocks_sleep_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a free room where I could spend the nights.”')
                $ galerocks_fulvia_knowsabout = 1
                $ galerocks_sleep_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “Very well. Speak with {color=#f6d6bd}Fulvia{/color} in the evening, she should have a room to spare. She’s in the building just at the edge of the small vegetable field, close to the gate.”"
                jump severina_rewards02
            '“Maybe five free repairs of my gambeson?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe five free repairs of my gambeson?”')
                $ galerocks_armorer_free += 5
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “I’ll speak with {color=#f6d6bd}Rufina{/color}, the tailor. She’s close to the hill we’re on. You need to take the path to the left, you’ll find her behind the dining tables.”"
                jump severina_rewards02
            '“Maybe some free baths and laundry?”' if not galerocks_bath_free:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe some free baths and laundry?”')
                $ galerocks_bath_free = 1
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “{color=#f6d6bd}Aquila{/color} helps us with water, and he can ask someone to wash your clothes. His work has him walking around the entire village, but look for him on the eastern bank, close to the pier.”"
                jump severina_rewards02
            '“I may be in need of a boat one day. I could use a discount.”' if not galerocks_navica_boat_bought and galerocks_navica_boat_price_base >= 10 and not asterion_found:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may be in need of a boat one day. I could use a discount.”')
                $ galerocks_navica_boat_price_base -= 10
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “I doubt it, but very well. I’ll speak with {color=#f6d6bd}Navica{/color}, the boatmaker. On most days, she works with the carpenters, on the eastern bank.”"
                jump severina_rewards02
            '“I don’t need any favors. Just make sure everyone learns that I’m useful.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t need any favors. Just make sure everyone learns that I’m useful.”')
                $ galerocks_reputation += 2
                $ custom1 = "{color=#f6d6bd}Severina{/color} raises her head and sighs. “You won’t buy fish merely with fame,” she starts slowly, but then nods. “I’ll mention it soon to the council of our elders and head workers.”"
                jump severina_rewards02

label severina_about_galerockshelpingoldpagos01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Old Págos{/color} could use an {i}old friend{/i} right now. Maybe some supplies for winter.”')
    $ severina_about_galerockshelpingoldpagos1 = 1
    $ severina_annoyance += 1
    menu:
        'She straightens up and frowns. “I think you misunderstand the shape of our past alliance, you do. While it is true that our forebears had strong ties, even before {color=#f6d6bd}Págos{/color} started following The Wright in their own river of faith, for years now we’ve been at odds, contacting each other merely out of necessity. Ever since we were accused of robbing them,” she suddenly pauses, glancing at her granddaughter and clearing her throat, “{i}wrongly{/i} accused, we are not welcomed at their gates, and I’ve no doubt they wouldn’t help us either.”
        '
        '“You know already that {color=#f6d6bd}Glaucia{/color} is willing to lie to you. You could heal old wounds by helping the sick and weak.”' if quest_lostmerchants == 2 and banditshideout_galerocks_tiestobandits:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know already that {color=#f6d6bd}Glaucia{/color} is willing to lie to you. You could heal old wounds by helping the sick and weak.”')
            jump severina_about_galerockshelpingoldpagos02alt
        '“If you say so.”' if quest_lostmerchants != 2 or not banditshideout_galerocks_tiestobandits:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you say so.”')
            jump severina_afterinteraction01

    label severina_about_galerockshelpingoldpagos02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You say that the people of {color=#f6d6bd}Old Págos{/color} have accused you of thievery, but you know already that {color=#f6d6bd}Glaucia{/color} lied to you about different events. You could heal old wounds by helping the sick and weak.”')
        jump severina_about_galerockshelpingoldpagos02alt
        label severina_about_galerockshelpingoldpagos02alt:
            $ severina_about_galerockshelpingoldpagos2 = 1
            $ severina_annoyance += 1
            $ oldpagos_plague_helpfromgalerocks = 1
            $ oldpagos_plague_helpfromgalerocks_dayofleaving = (day+1)
            $ galerocks_reputation += 1
            menu:
                '“Your words are harsh, outsider, but hard to argue with, alright. {i}I{/i} haven’t much of my own,” she glances at the sleeves of her dress and the cup-like seashell, “but I’ll present this case to the council. You’ve already helped us learn that the tool-selling caravan won’t take their share of our fish, so we may have a few barrels to spare. Though I can’t promise you much. I can’t promise you anything, actually.”
                '
                '“A few barrels of fish is enough to save lives.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A few barrels of fish is enough to save lives.”')
                    menu:
                        'She glances at her granddaughter, lets her fingertips tap against each other, and sighs. “Not a large price. I’ll do my best.”
                        \n\n“And I’ll vote {i}yes{/i},” says the guard with a wide smile.
                        '
                        '“Thanks for being willing to try, at least.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for being willing to try, at least.”')
                            jump severina_afterinteraction01

label severina_quest_lostmerchants01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spend a lot of time traveling between places. Do you have any work for me?”')
    $ severina_quest_lostmerchants = 1
    if (severina_friendship+galerocks_reputation+appearance_charisma) < 7:
        $ questionpreset = "severina1"
        $ severina_annoyance += 1
        menu:
            'She runs her eyes over you, then frowns without as much as a hint of subtlety. “Show me first that you’re worth something. Work with our fishers, find someone seeking a messenger. I don’t need a stranger before autumn, when we’ll trade for winter grain.”
            '
            '(severina1 set)':
                pass
    else:
        $ severina_quest_lostmerchants = 2
        $ severina_annoyance += 1
        $ severina_quest_lostmerchants_receivedday = day
        $ quest_lostmerchants = 1
        $ renpy.notify("New entry: The Lost Merchants")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Lost Merchants{/i}')
        menu:
            '“I don’t need a stranger before autumn, when we’ll trade for winter grain. Although...” She runs her eyes over you, then glances at the guard in front of her. “There’s something that may be an easy task for a traveler, chiefly one that doesn’t talk {i}too{/i} much.”
            \n\nShe reaches for one of her tablets, then nods with approval. “Right. I want you to {i}look{/i} around, not {i}ask{/i} around. There’s a group of spice and tools merchants that was meant to reach our village some time ago, yet they fell silent, most likely taken to the fogs by some beasts. Keep your eyes open, maybe you’ll find their shells, or even better, wares.”
            \n\n“Once you learn what happened, I’ll pay you...” She starts to hum to herself, looking into a pouch from the desk. “Five coins. Just don’t speak with any other tribe about it,” she stares at you harshly. “We must keep this between ourselves. And if the merchants turn out to be {i}nowhere{/i} to be found, I’ll pay you as well.”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01
    label severina_quest_lostmerchants02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could still do some work for you.”')
        $ severina_quest_lostmerchants = 2
        $ severina_quest_lostmerchants_receivedday = day
        $ severina_annoyance += 1
        $ quest_lostmerchants = 1
        $ renpy.notify("New entry: The Lost Merchants")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Lost Merchants{/i}')
        menu:
            'She runs her eyes over you, then glances at the guard in front of her. “There’s something that may be an easy task for a traveler, chiefly one that doesn’t talk {i}too{/i} much.”
            \n\nShe reaches for one of her tablets, then nods with approval. “Right. I want you to {i}look{/i} around, not {i}ask{/i} around. There’s a group of spice and tools merchants that was meant to reach our village some time ago, yet they fell silent, most likely taken to the fogs by some beasts. Keep your eyes open, maybe you’ll find their shells, or even better, wares.”
             \n\n“Once you learn what happened, I’ll pay you...” She starts to hum to herself, looking into a pouch from the desk. “Five coins. Just don’t speak with any other tribe about it,” she stares at you harshly. “We must keep this between ourselves. And if the merchants turn out to be {i}nowhere{/i} to be found, I’ll pay you as well.”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01

    label severina_quest_lostmerchants03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the lost merchants...”')
        menu:
            '“You found something?”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01

    label severina_quest_lostmerchants02a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”')
        $ severina_quest_lostmerchants_stayingsilent = 1
        menu:
            '“You’re already making me reconsider my decision to ask you in the first place, stranger,” she stares at you rebukingly, but carries on. “There ain’t many merchants willing to come here, and most of them do so every year or so, knowing the risk. Thanks to our deals, they hire expensive messengers and send them through the eastern route, avoiding all them settlements. This way, we prepare ourselves for their arrival ahead of time, preparing food and wares, while the other villages are taken by surprise, forced to haggle for worse prices.”
            \n\nShe glances at the pouches placed on the desk. “I think it’s obvious now {i}why{/i} we need to keep other villages from learning about my little request.”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01

    label severina_quest_lostmerchants02b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found an abandoned wagon on the eastern path...”')
        $ severina_quest_lostmerchants_fallentree = 1
        menu:
            'You describe your findings, but she’s hesitant to trust you. “Right, I would expect them to have a wagon... But that ain’t enough to be sure. Better get there fast, seek some trails. The cart breaking could have forced its owners to turn back.”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01

    label severina_quest_lostmerchants02c:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any ideas where I could start?”')
        $ severina_quest_lostmerchants_clues = 1
        menu:
            '“Most merchants take the western path, so in your place, I’d hang around some villages, I would. But these ones were new, they could try to use the eastern route, which is faster, but more dangerous. If they are at one of the settlements, it would be a group big enough to fill an entire inn. Just don’t {i}ask{/i} anyone about them.”
            '
            '“They were robbed by {color=#f6d6bd}Glaucia{/color}.”' if quest_lostmerchants_description01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They were robbed by {color=#f6d6bd}Glaucia{/color}.”')
                jump severina_quest_lostmerchants04success01
            '“I haven’t found them yet, and I don’t think anyone will.”' if (severina_quest_lostmerchants_receivedday+5) < day and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants04fail01
            '“Any ideas where I could start?”' if not severina_quest_lostmerchants_clues and not quest_lostmerchants_description01:
                jump severina_quest_lostmerchants02c
            '“Why shouldn’t I ask anyone if they saw these merchants? It could save me a lot of time.”' if not severina_quest_lostmerchants_stayingsilent:
                jump severina_quest_lostmerchants02a
            '“I found an abandoned wagon on the eastern path...”' if not quest_lostmerchants_description01 and fallentree_firsttime and not severina_quest_lostmerchants_fallentree:
                jump severina_quest_lostmerchants02b
            '“Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”' if severina_quest_lostmerchants_receivedday == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Find a clear sign of the merchants, report only to you, come here for my dragon bones. Got it.”')
                jump severina_afterinteraction01
            '“I’ll tell you if I learn anything.”' if severina_quest_lostmerchants_receivedday != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll tell you if I learn anything.”')
                jump severina_afterinteraction01

    label severina_quest_lostmerchants04fail01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I haven’t found them yet, and I don’t think anyone will.”')
        $ galerocks_reputation += 1
        $ severina_friendship += 1
        $ severina_annoyance += 1
        menu:
            '“Fair enough,” she reaches for a pouch, then puts five dragon bones in a single row and pushes them forward. “Something must have happened to them before they got to the peninsula, alright. You deserve your pay.”
            '
            'I nod and take the coins.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and take the coins.')
                $ quest_lostmerchants = 3
                $ coins += 5
                show screen notifyimage( "Quest completed: The Lost Merchants. +5", "gui/coin2.png" )
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Lost Merchants. +5 {image=cointest}{/i}')
                $ quest_lostmerchants_description03 = "I decided to tell her that they are nowhere around."
                jump severina_afterinteraction01

    label severina_quest_lostmerchants04success01:
        $ severina_friendship += 2
        $ severina_annoyance += 2
        menu:
            'Her gaze is grim, but after a simple “I see,” she reaches for a pouch, then puts five dragon bones in a single row and pushes them forward. “Thank you for your assistance.”
            '
            '“You don’t sound surprised.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound surprised.”')
                menu:
                    'She looks at her granddaughter, who, without even noticing, has lowered her crossbow. “I asked {color=#f6d6bd}Glaucia{/color} about this very thing, I did,” {color=#f6d6bd}Severina{/color} admits. “I don’t think you’re mistaken, roadwarden. It’s a natural step on her path, but it means she’s lied to {i}our{/i} people. And I won’t be able to avoid the confrontation. Still, I’m grateful to learn it.”
                    '
                    'I reach for the coins. “You don’t just {i}speak{/i} with {color=#f6d6bd}Glaucia{/color}. You collaborate with her, and you got betrayed.”' if banditshideout_galerocks_tiestobandits:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the coins. “You don’t just {i}speak{/i} with {color=#f6d6bd}Glaucia{/color}. You collaborate with her, and you got betrayed.”')
                        $ quest_lostmerchants = 2
                        $ coins += 5
                        show screen notifyimage( "Quest completed: The Lost Merchants. +5", "gui/coin2.png" )
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Lost Merchants. +5 {image=cointest}{/i}')
                        $ quest_lostmerchants_description02 = "I received my payment."
                        jump severina_about_bandits02alt
                    'I nod and take the coins.' if not banditshideout_galerocks_tiestobandits:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and take the coins.')
                        $ quest_lostmerchants = 2
                        $ coins += 5
                        show screen notifyimage( "Quest completed: The Lost Merchants. +5", "gui/coin2.png" )
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Lost Merchants. +5 {image=cointest}{/i}')
                        $ quest_lostmerchants_description02 = "I received my payment."
                        jump severina_afterinteraction01

label severina_about_bandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Has the village faced any struggles with the bandits?”')
        $ severina_annoyance += 1
        $ severina_about_bandits = 1
        if not galerocks_about_bandits_thais:
            $ banditshideout_villagesasked_aboutattacks += 1
            $ galerocks_about_bandits_thais = 1
        $ quest_intelforpeltnorth_description04c = "The people of {color=#f6d6bd}Gale Rocks{/color} claim that bandits are not a big issue."
        $ questionpreset = "severina1"
        menu:
            'She looks at her guard, then around her. “Have you noticed where we are? We’re safe enough to fight a dragon, and if there {i}are{/i} any bandits in our woods, they eat nothing barring timber and worms. Whenever we trade, we send groups of ten, twenty souls strong, enough to push away a few footpads.”
            '
            '(severina1 set)':
                pass

label severina_about_bandits02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t just {i}speak{/i} with {color=#f6d6bd}Glaucia{/color}. You collaborate with her, and you got betrayed.”')
    jump severina_about_bandits02alt
    label severina_about_bandits02alt:
        $ severina_annoyance += 2
        $ severina_about_bandits = 1
        if not galerocks_about_bandits_thais:
            $ banditshideout_villagesasked_aboutattacks += 1
            $ galerocks_about_bandits_thais = 1
        $ quest_intelforpeltnorth_description04c = "The people of {color=#f6d6bd}Gale Rocks{/color} claim that bandits are not a big issue."
        menu:
            'She looks at her granddaughter and nods at the exit. She frowns, raising her crossbow gently, but obediently leaves the room. The perfumed man moves his hand to the grip of his sickle sword, as if trying to compensate for the sudden lack of assistance.
            \n\n“{color=#f6d6bd}Glaucia{/color} was born and raised in this village, and many of those who joined her band used to be our neighbors, or their spouses. We ain’t talking here about some strangers I’d put a bounty on.”
            '
            '“Understood.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Understood.”')
                $ quarters += 1
                menu:
                    'You discuss the matter for some time. You focus on the link between highwaymen and the rare visits of trading caravans. “I’m sure you’ve heard about the squad of soldiers sent here by the city,” you conclude. “Their fight at {color=#f6d6bd}Hag Hills’ pass{/color} has pretty much crushed them. Once the officials learn that there’s yet another group of armed bandits, and fully supported by a crucial trading partner at that, it won’t bode well for your current lifestyle.”
                    \n\nShe listens carefully, and her answer is close to a whisper. “Tell me what you propose, stranger.”
                    '
                    '“It’s time for your village to join forces with {color=#f6d6bd}Hovlavan{/color}. If {color=#f6d6bd}Glaucia{/color} is ready to put your lives in danger, you need to have soldiers at hand, someone ready to maintain the roads and keep the beasts and bandits away.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s time for your village to join forces with {color=#f6d6bd}Hovlavan{/color}. If {color=#f6d6bd}Glaucia{/color} is ready to put your lives in danger, you need to have soldiers at hand, someone ready to maintain the roads and keep the beasts and bandits away.”')
                        menu:
                            'The crossbowwoman peeks inside, as if surprised there has been no bloodshed yet. {color=#f6d6bd}Severina{/color} reacts to it with nothing more than a glance, staring at you like a statue from above her clasped fingers.
                            \n\n“Is it too late to admit I was sure this is where you’ve been leading me with all your talk? I’m ready to ask the council to listen to you, I am.” She can’t completely hide the pain in her voice. “There’s been more and more talk of such a treaty in recent years, as our lives get harsher than they’ve been in many decades, and we even grow apart from our neighbors.”
                            \n\nShe then notes something on her tablet, and gives it to the guard, sharing a telling nod with him. “But I ain’t sure yet what’s right, stranger, and the elders and head workers won’t be so sure either. You’ll have only one chance to convince us that we should push our family members and friends toward a cliff, and instead obey some outsiders from the city. I don’t envy you such a task.”
                            \n\nSeeing the kind look of her grandmother, the young woman returns to her chair, but, at least for now, lets her crossbow rest.
                            '
                            '“Very well. I’ll speak with you when I’m ready to face the council.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll speak with you when I’m ready to face the council.”')
                                $ quest_galerockssupport = 1
                                $ renpy.notify("New entry: The Support of Gale Rocks")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Gale Rocks{/i}')
                                jump severina_afterinteraction01
                            'I nod in silence. Maybe {color=#f6d6bd}Glaucia{/color} would like to know about this.' if glaucia_friendship >= 2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod in silence. Maybe {color=#f6d6bd}Glaucia{/color} would like to know about this.')
                                $ quest_galerockssupport = 1
                                $ renpy.notify("New entry: The Support of Gale Rocks")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Support of Gale Rocks{/i}')
                                jump severina_afterinteraction01
