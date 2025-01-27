# ###################### BANDITS HIDEOUT
default banditshideout_firsttime = 0
default banditshideout_dayofreaching = 0 # day
default banditshideout_banned = 0
default banditshideout_bandits_pchearedabout = 0 # 1 - just knows. 2 - they are not a problem
default banditshideout_bandits_pchearedabouthideout = 0
default banditshideout_villagesasked_aboutattacks = 0

default banditshideout_pcknowswhere = 0
default banditshideout_knowsaboutlumberjackcamp = 0
default banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp = 0

default banditshideout_fluff = ""
default banditshideout_fluff_old = ""
default banditshideout_description2 = ""

default banditshideout_galerocks_tiestobandits = 0

default banditshideout_aboutcleanwater = 0
default banditshideout_aboutrest = 0

label banditshideout01:
    scene empty #part A of...
    scene layoutfull #part B of hididng all images
    nvl clear
    $ pc_area = "banditshideout"
    $ renpy.music.play("audio/track_04banditshideout.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    label banditshideout_fluffloop:
        $ banditshideout_fluff = ""
        $ banditshideout_fluff = renpy.random.choice(['An archer observes you from the top of the crag. The gate is guarded by a few armed men.', 'The birds and monkeys follow you as you ride up the path. You barely notice the few people who leave the thicket and get in your way, slowing you down, but they let you ride forward.', 'While someone watches you from one of the trees, whistling, it’s the sound of the hooves that lures a few people out to the gate.', 'You reach the gate without issue, but a trail of blood makes you suddenly stop. A few people approach the gate, talking about the deer they just caught.', 'A few men are discussing something at the gate, but fall quiet once they notice you.'])
        if banditshideout_fluff_old == banditshideout_fluff:
            jump banditshideout_fluffloop
        else:
            $ banditshideout_fluff_old = banditshideout_fluff

    if glaucia_firstattitude == "friendly":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The highwaymen give you distrustful looks, and, holding their weapons, tell you to move slowly, and to put your axe on the ground."
        else:
            $ banditshideout_description2 = "Aside from a few polite nods, the highwaymen observe you distrustfully, and tell you to keep your weapon with your bundles."
    elif glaucia_firstattitude == "playful":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "Aside from a few polite nods, the highwaymen observe you distrustfully, and tell you to keep your weapon with your bundles."
        else:
            $ banditshideout_description2 = "The highwaymen nod politely to you, and even though their weapons are at hand, they keep their distance."
    elif glaucia_firstattitude == "distanced":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The highwaymen give you distrustful looks, and, holding their weapons, tell you to move slowly, and to put your axe on the ground."
        else:
            $ banditshideout_description2 = "Aside from a few polite nods, the highwaymen observe you distrustfully, and tell you to keep your weapon with your bundles."
    elif glaucia_firstattitude == "intimidating":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The highwaymen nod politely to you, and even though their weapons are at hand, they keep their distance."
        else:
            $ banditshideout_description2 = "A few of the highwaymen welcome you by mentioning your trade, and while you’re being observed, no one reaches for their weapon."
    elif glaucia_firstattitude == "vulnerable":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "As you dismount, the highwaymen stay upright, a few of them towering over you. You look around, and a man and a woman at a distance whisper to one another, giggling once you notice them. You’re told to leave your weapon with one of the gatekeepers."
        else:
            $ banditshideout_description2 = "The highwaymen give you distrustful looks, and, holding their weapons, tell you to move slowly, and to put your axe on the ground."

    $ can_leave = 0
    $ can_rest = 0
    $ shop = "glaucia"
    if banditshideout_firsttime:
        show areapicture banditshideout01 at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")

    if not banditshideout_firsttime:
        $ minutes += 5
        $ world_known_npcs += 2
        $ world_known_areas += 1
        $ banditshideout_firsttime = 1
        $ banditshideout_bandits_pchearedabouthideout = 1
        $ banditshideout_dayofreaching = day
        $ can_items = 0
        $ glaucia_dayoflastvisit = day
        jump banditshideoutfirsttime01
    else:
        $ can_items = 1
        jump banditshideoutregular01

label banditshideoutfirsttime01:
    show areapicture banditshideout00a at basicfade
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'The path is beaten, yet your mount has to step over branches, large rocks, and even animal bones. While the trees aren’t pruned, they grow sparse enough for you to have a good view of your surroundings.
        \n\nA pile of rotting logs, the remains of food, and even a broken wagon rest at the feet of the crag. You look up - the palisade has a massive gap in it, which now serves as a vantage point for {color=#f6d6bd}a person you can’t see clearly{/color}. They’re holding an arrow on their strung bow and while they aren’t aiming at you, they’d have enough time to shoot before you got off the saddle.
        \n\n“You’ve a horse,” the masculine voice announces loudly, then stares at you. “Thought a mad deer was running, I did! Almost shot it in the nose.” Another pause. “Who?”
        '
        'I shout back. “[pcname], a roadwarden.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout back. “%s, a roadwarden.”' %pcname)
            if appearance >= 5:
                $ glaucia_friendship += 1
                $ custom1 = "And such a fancy one at that, togs and all,” he speaks with a mixture of amusement and admiration. “Head up, but act {i}nice{/i}, or we won’t.”"
            elif appearance >= 2:
                $ custom1 = "Are you all a family of suiciders or something? Head up, but I’ve my eyes on you, I do.”"
            else:
                $ custom1 = "You sure do look like you rode through ten swamps. Head up, but I’ve my eyes on you, I do.”"
            menu:
                '{color=#f6d6bd}The archer{/color} crouches, as if watching you from two feet closer is going to make a difference. He shouts, but more so toward someone behind the wall. “Wait, {i}another{/i} roadwarden? [custom1]
                \n\nThe hamlet could be a generation old, and while the freshly beaten paths, spread trash, and newly fallen trees and gathered rocks make it clear that the dwellers are still altering their surroundings, the woods around you are filled with wildlife, crowding in the tree crowns, grasses, and trunks. A boar flees up the path, keeping its eyes on you as it runs. A dragonling is drinking from the pond you just rode by.
                \n\nThere are a few people gathered at the gate, and more of them approach you from behind. You count eight of them in total, with only one female face among them. All are younger than forty, with weapons at their sides or in their hands - simple flails, two-handed axes on long hafts, maces, spears, throwing clubs. Equipment so heavy and unwieldy that you can’t be sure if it’s meant to threaten you, or to get through the skin of nearby monsters, if necessary.
                \n\nSome of those who came through the open gate have bare chests, displaying their scars and bandages, but the others are wearing heavy jackets, and look nothing like pure farmers seeking shelter for a night.
                \n\nThey observe your mount in silence, together with the curious rooks sitting on the top of the wall.
                '
                '{image=d6} I dismount smoothly and stand upright, then give everyone a threatening glance.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I dismount smoothly and stand upright, then give everyone a threatening glance.')
                    if pc_hp <= 0:
                        $ glaucia_friendship -= 1
                        $ custom1 = "The strangers meet your eyes, and after some of them react with an unpleasant smirk, you hear a chuckle. “Watch out to not fall on your face!” You frown, then realize that you can hear your own breathing - the days you spent on the road are burdening your shoulders.\n\nOne of the men puts his axe back behind his belt, and as he rests his hands on his sides, he speaks scoffingly. “Alright, {i}roadwarden{/i}. Drop your blades, tie the beast somewhere,” he points his thumb behind him, leading your eyes to a loose stake of the palisade. “{color=#f6d6bd}Glaucia’s{/color} on her way,” he adds matter-of-factly, as if to a regular waiting for an alehouse keeper. You try to follow his commands, but after he suddenly steps forward, raising his hand, you step away, staggering. The group laughs, while the man pretends to fix his hair, towering over you.\n\n“What’s so funny?” interrupts the voice of the woman who now steps through the gate, making her people fall silent. Her massive winter boots make heavy footfalls - they are made of a leather that still remembers the garnet dye of the past, and have wide and firm heels. The bronze of the decorative buckles is polished, without a hint of green."
                    elif pc_hp == 1:
                        $ custom1 = "The strangers meet your eyes, and some of them react with an unpleasant smirk. After a moment, you hear your own breathing - the days you spent on the road are burdening your shoulders.\n\nOne of the men puts his axe back behind his belt, and as he rests his hands on his sides, he speaks scoffingly. “Alright, {i}roadwarden{/i}. Drop your blades, tie the beast somewhere,” he points his thumb behind him, leading your eyes to a loose stake of the palisade. “{color=#f6d6bd}Glaucia’s{/color} on her way,” he adds matter-of-factly, as if to a regular waiting for an alehouse keeper. You follow his commands.\n\nFrom afar, you hear the heavy footfalls of the person who joins you soon after. Her massive winter boots are made of a leather that still remembers the garnet dye of the past, and have wide and firm heels. The bronze of the decorative buckles is polished, without a hint of green."
                    elif pc_hp <= 3:
                        $ custom1 = "Most of the strangers meet your eyes. One of them puts his axe back behind his belt, but then crosses his arms, returning your challenging look. “Alright. Leave here every blade, tie the beast somewhere,” he points his thumb behind him, leading your eyes to a loose stake of the palisade. “{color=#f6d6bd}Glaucia’s{/color} on her way,” he adds matter-of-factly, as if to a regular waiting for an alehouse keeper. You follow his commands.\n\nFrom afar, you hear the heavy footfalls of the person who joins you soon after. Her massive winter boots are made of a leather that still remembers the garnet dye of the past, and have wide and firm heels. The bronze of the decorative buckles is polished, without a hint of green."
                    else:
                        $ glaucia_friendship += 1
                        $ custom1 = "Some of the strangers avoid your eyes, while others accept the challenge. One of the men steps closer, offering to help you “tie your beast” to one of the palisade’s loose beams. Another one clears his throat. “Em. Leave your blades here, right?” He moves his shoulders, trying to take a more confident stance. “{color=#f6d6bd}Glaucia’s{/color} on her way,” he adds matter-of-factly, as if to a regular waiting for an alehouse keeper. Slowly, you follow his commands, making sure to glance behind you from time to time.\n\nFrom afar, you hear the heavy footfalls of the person who joins you soon after. Her massive winter boots are made of leather that still remembers the garnet dye of the past, and have wide and firm heels. The bronze of the decorative buckles is polished, without a hint of green."
                    jump banditshideoutfirsttime02
                'I get down slowly, then keep my open hands in the air.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get down slowly, then keep my open hands in the air.')
                    $ custom1 = "One of the strangers nods in approval, while another gestures for you to step away from your mount, making sure you’re not hiding anything. “Alright. Leave here every blade, tie the beast somewhere,” he points his thumb behind him, leading your eyes to a loose stake of the palisade. “{color=#f6d6bd}Glaucia’s{/color} on her way,” he adds matter-of-factly, as if to a regular waiting for an alehouse keeper. You follow his commands, waiting with the dwellers in silence.\n\nFrom afar, you hear the heavy footfalls of the person who joins you soon after. Her massive winter boots are made of leather that still remembers the garnet dye of the past, and have wide and firm heels. The bronze of the decorative buckles is polished, without a hint of green."
                    jump banditshideoutfirsttime02

    label banditshideoutfirsttime02:
        show areapicture banditshideout00b at basicfade
        menu:
            '[custom1]
            \n\nHer emerald eyes are running over your mount and equipment, reaching your face last, and with little curiosity. She’s broad-shouldered, with a muscular figure and round face. Her long, shining mail rests on a green aketon, making noise with every movement of her arms. Her right hand is tapping the hilt of the sickle sword - a broad blade meant for chopping not just flesh, but also twigs - sheathed at her side. The short, dark hair of a fighter is carefully cut, and her skin is healthily tanned.
            \n\nIt takes another few breaths for you to notice the other side of her appearance. While she’s wider than anyone in sight, she’s more than a head shorter than you. You spot the gray strands of her hair, and wrinkles cut by scars on her cheeks and lips. Her hand is missing a thumb, explaining why the blade is on her right side, and an old bruise surrounding her left eye hinders her from fully opening it, so it’s difficult for you to match her gaze.
            '
            'She’s just acting tough.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- She’s just acting tough.')
                jump banditshideoutfirsttime03
            'She must be quite a fighter.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- She must be quite a fighter.')
                jump banditshideoutfirsttime03
            'She’s performing. I try not to smirk.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- She’s performing. I try not to smirk.')
                label banditshideoutfirsttime03:
                    $ glaucia_metwith = 1
                    $ glaucia_questionstoday += 1
                    if (whitemarshes_attacked and not glaucia_about_nomoreundead) or (whitemarshes_destroyed and not glaucia_about_nomoreundead) or (whitemarshes_nomoreundead and not glaucia_about_nomoreundead):
                        jump banditshideoutfirsttime03alt
                    if day >= 6:
                        $ custom1 = "I heard about your arrival to the peninsula, but didn’t expect we’d see you at our doorstep. We don’t have much to discuss, tell me you ain’t stupid enough to provoke my hand."
                    else:
                        $ custom1 = "I wasn’t aware of your arrival to the peninsula, yet here you are, at my very doorstep. I don’t have much to discuss with someone of your trade, tell me you ain’t stupid enough to provoke my hand."
                    menu:
                        '“A palfrey, this time,” her confident, powerful voice matches her straight posture. She reaches for the bottom of {color=#f6d6bd}[horsename]’s{/color} neck, slowly, allowing it to accept the touch after a moment of hesitation. “It’s more for running than combat, I believe? The saurian was dangerous, but slower, without much stamina.” You look for a reason why she would lecture you about your own trade, then notice the curious eyes of her band, listening to every word.
                        '
                        'It may be the first horse they’ve ever seen.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be the first horse they’ve ever seen.')
                            $ at_activate = 1
                            $ at = 0
                            menu:
                                '“Stranger,” she looks at you again and steps back. “[custom1]”
                                '
                                ' (disabled)' ( condition="at == 0" ):
                                    pass
                                '“I see no reason why we can’t have a friendly conversation.”' ( condition="at == 'friendly'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “I see no reason why we can’t have a friendly conversation.”')
                                    $ glaucia_firstattitude = "friendly"
                                    $ glaucia_friendship -= 1
                                    $ custom1 = "Her voice grows colder. “I see plenty. For all I know, you’re yet another city spy. If I were to learn you’re here more to hinder our {i}work{/i},” she pauses, “than to fight beasts, I’d have a light heart letting you bleed your neck out right where you are.” You look to your left and right. No matter how many hours of training you have behind you, the sheer number of opponents would overwhelm you. “But let us leave the threats for later. Take a stroll with me, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, someone pushes you forward with the blunt edge of a spear."
                                    $ at_activate = 0
                                    $ at = 0
                                    jump banditshideoutfirsttime04
                                '“And I’m surprised to see you’re open to having a talk with a roadwarden. Life gets funny sometimes.”' ( condition="at == 'playful' and not banditshideout_knowsaboutlumberjackcamp" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “And I’m surprised to see you’re open to having a talk with a roadwarden. Life gets funny sometimes.”')
                                    $ glaucia_firstattitude = "playful"
                                    $ glaucia_friendship += 0
                                    $ custom1 = "“Not a smart risk for you to take, but very well,” she pauses. “For all I know, you’re yet another city spy, but I’d rather make sure you won’t hinder our {i}work{/i},” she pauses, then invites you to follow her with a nod. “Let’s take a stroll, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, you hear a simple command from a man behind you. “Walk.” Judging by the way the he holds his spear, you have no real choice."
                                    $ at_activate = 0
                                    $ at = 0
                                    jump banditshideoutfirsttime04
                                'I smile. “I’m starting to think you’re not lumberjacks.”' ( condition="at == 'playful' and banditshideout_knowsaboutlumberjackcamp" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I smile. “I’m starting to think you’re not lumberjacks.”')
                                    $ glaucia_firstattitude = "playful"
                                    $ glaucia_friendship += 1
                                    $ custom1 = "She frowns, then lets out an amused grunt. “{color=#f6d6bd}Hovlavan{/color} truly sends their brightest souls to us. Put it to good use, and not to hindering our {i}work{/i},” she pauses, then invites you to follow her with a nod. “Let’s take a stroll, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, you hear a simple command from a man behind you. “Walk.” Judging by the way the way he holds his spear, you have no real choice."
                                    $ at_activate = 0
                                    $ at = 0
                                    jump banditshideoutfirsttime04
                                '“I have a few questions for you.”' ( condition="at == 'distanced'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I have a few questions for you.”')
                                    $ glaucia_firstattitude = "distanced"
                                    $ glaucia_friendship -= 1
                                    $ custom1 = "She raises her chin, looking at something above you. “Do I look like someone who hopes to prattle with an outsider? Say {i}yes{/i} and you’ll lose your teeth,” she adds before you let out a word. “For all I know, you’re yet another city spy. If I were to learn you’re here more to hinder our {i}work{/i},” she pauses, “than to fight beasts, I’d have a light heart letting you bleed your neck out right where you are.” You look to your left and right. No matter how many hours of training you have behind you, the sheer number of opponents would overwhelm you. “But let us leave the threats for later. Take a stroll with me, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, someone pushes you forward with the blunt edge of a spear."
                                    $ at_activate = 0
                                    jump banditshideoutfirsttime04
                                '“I don’t {i}provoke{/i}. I either cut, or I don’t. For now, let’s have a talk.”' ( condition="at == 'intimidating'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I don’t {i}provoke{/i}. I either cut, or I don’t. For now, let’s have a talk.”')
                                    $ glaucia_firstattitude = "intimidating"
                                    $ glaucia_friendship += 1
                                    $ custom1 = "Her smile is brief, but marks her voice. “We’ve things to talk about now? I’m all ears. Take a stroll with me, I ain’t missing a chance to enjoy the rest of the summer.” The tension of the group around you isn’t as thick, and as you follow the woman north, the others keep their distance."
                                    $ at_activate = 0
                                    $ at = 0
                                    jump banditshideoutfirsttime04
                                '“Trust me, I’m far from being a threat. Just let me ask you a few questions and I’m out of your sight.”' ( condition="at == 'vulnerable'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Trust me, I’m far from being a threat. Just let me ask you a few questions and I’m out of your sight.”')
                                    $ glaucia_firstattitude = "vulnerable"
                                    $ glaucia_friendship -= 2
                                    $ custom1 = "She raises the brow over her healthy eye, looking at the rest of her band. “So that’s why you have a {i}running{/i} mount,” the mocking chuckle spreads among the others. “Do I look like someone who hopes to prattle with an outsider? Say {i}yes{/i} and you’ll lose your teeth,” she suddenly gets serious. You look to your left and right. No matter how many hours of training you have behind you, the sheer number of opponents would overwhelm you. “For all I know, you’re yet another city spy, not someone who would help us with our {i}work{/i},” she pauses. “But let us leave the threats for later. Take a stroll with me, if you have any muscles left. And speak loudly, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, someone’s hand pushes you forward."
                                    $ at_activate = 0
                                    $ at = 0
                                    jump banditshideoutfirsttime04

    label banditshideoutfirsttime03alt:
        $ glaucia_about_nomoreundead = 1
        if orentius_spared:
            $ glaucia_firstattitude = "vulnerable"
            $ custom6 = "Our watchers noticed the commotion at {color=#f6d6bd}Marshes{/color}. We’ve you to thank for it, I’ve heard,” she gives you an angry scowl. “Too bad you didn’t seek my help before. Now getting rid of the necromancers will be only more difficult.”"
            $ glaucia_friendship -= 2
            menu:
                '“A palfrey, this time,” her confident, powerful voice matches her straight posture. She reaches for the bottom of {color=#f6d6bd}[horsename]’s{/color} neck, slowly, allowing it to accept the touch after a moment of hesitation. “It’s more for running than combat, I believe? The saurian was dangerous, but slower, without much stamina.” You look for a reason why she would lecture you about your own trade, then notice the curious eyes of her band, listening to every word. It may be the first horse they’ve ever seen.
                \n\n“Stranger,” she looks at you again, then steps back. “[custom6]”
                \n\nShe puts a hand on her side. “Take a stroll with me, I ain’t missing a chance to enjoy the rest of the summer.” She heads north, and before you decide what to do next, someone pushes you forward.
                '
                'I guess I go north, then.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess I go north, then.')
                    jump banditshideoutfirsttime04a
        else:
            $ glaucia_firstattitude = "intimidating"
            $ quest_spyonwhitemarshes = 2
            if whitemarshes_destroyed:
                $ custom6 = "Our watchers noticed the commotion at {color=#f6d6bd}Marshes{/color}. We’ve you to thank for it, I’ve heard,” she gives you a polite nod. “The price was high, but the risk of having necromancers in the north was much greater. I applaud your judgment.”"
                $ glaucia_friendship += 3
                $ glaucia_friendship_tier += 1
            elif orentius_banished:
                $ custom6 = "Our watchers noticed the commotion at {color=#f6d6bd}Marshes{/color}. We’ve you to thank for it, I’ve heard,” she gives you a polite nod. “I’d rather see the necromancer pay the price of his deeds... But at least he’s away from my land. Good job, warden.”"
                $ glaucia_friendship += 2
                $ glaucia_friendship_tier += 2
            elif orentius_convinced:
                $ custom6 = "Our watchers noticed the commotion at {color=#f6d6bd}Marshes{/color}. We’ve you to thank for it, I’ve heard,” she gives you a polite nod. “I’d rather see the necromancer pay the price of his deeds... But at least he’s away from my land. I can only hope you were right to keep him among his crazy followers.”"
                $ glaucia_friendship += 1
                $ glaucia_friendship_tier += 1
            menu:
                '“A palfrey, this time,” her confident, powerful voice matches her straight posture. She reaches for the bottom of {color=#f6d6bd}[horsename]’s{/color} neck, slowly, allowing it to accept the touch after a moment of hesitation. “It’s more for running than combat, I believe? The saurian was dangerous, but slower, without much stamina.” You look for a reason why she would lecture you about your own trade, then notice the curious eyes of her band, listening to every word. It may be the first horse they’ve ever seen.
                \n\n“Stranger,” she looks at you again, then steps back. “[custom6]”
                \n\nHer smile is brief, but marks her voice. “Take a stroll with me, I ain’t missing a chance to enjoy the rest of the summer.” The tension of the group around you isn’t as thick, and as you follow the woman north, the others keep their distance.
                '
                'I guess I go north, then.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess I go north, then.')
                    jump banditshideoutfirsttime04a

    label banditshideoutfirsttime04:
        menu:
            '[custom1]
            '
            'I guess I go north, then.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I guess I go north, then.')
                label banditshideoutfirsttime04a:
                    show areapicture banditshideout00c at basicfade
                    menu:
                        'The neglected path leads to a pond, through the rocks sticking out of the ground, fallen branches, and the rotten deck covering a wide puddle. There are some signs of repairs made on the bridge for fishers, but there are also some broken logs and a boat with a large hole in its hull.
                        \n\n{color=#f6d6bd}Glaucia{/color} and two of her guards walk with you in silence, surrounded by the screeching beasts around and above you. She takes leisurely strides, and as you step onto the bridge, looking across the pond, you can see that the woods surround it from all sides, like the walls of a dungeon chamber, with green and gray saurians basking both on the banks and in the shallow water. The frogs, flies, and black birds shatter any guise of peace.
                        \n\nThe wood beneath you is slippery. Whenever the woman makes a sudden movement, you flinch, preparing your shell to push her away.
                        \n\n“Don’t have any doubts,” she speaks calmly, looking in the distance. “I have little trust to offer you, and even less patience. It’s better that we meet this way, instead of on the road,” she turns toward you, and moves her hand behind her back. “But if you have no good reason to talk to me, you can scat right away. This land needs no soldiers, roadwarden, and chiefly no cityfolk.”
                        '
                        '“I could use your knowledge to help people. I’m sure you know these woods well.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use your knowledge to help people. I’m sure you know these woods well.”')
                            $ custom1 = "“There are some who could use another hand, I’ll agree, but there are also those who deserve nothing better than to be thrown into an elk pit. If you want my help, make me believe you can tell them apart.”\n\n"
                            jump banditshideoutfirsttime05
                        '“How do I know if I have a {i}good{/i} reason?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do I know if I have a {i}good{/i} reason?”')
                            $ custom1 = "She gazes at you, then, without asking for permission, pats your shoulder. “If {i}I{/i} can benefit from it,” she gives you a warm smile, “it means you’re fine.”\n\n"
                            jump banditshideoutfirsttime05
                        '“You’ve been heard.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve been heard.”')
                            $ custom1 = "“We’ll see about that. I’ll judge your deeds, not words.” "
                            jump banditshideoutfirsttime05

    label banditshideoutfirsttime05:
        $ questionpreset = "glaucia1"
        show areapicture banditshideout01 at basicfade
        $ quarters += 1
        menu:
            '[custom1]Without another word, she leads you back, then through the gate. The old, rotting roof of the only building is starting to bend under its own weight, but its condition is only slightly worse than that of the area around it. The broken tools, soggy planks and logs, the broken fence of an animal pen, and the waist-high nettle leaves growing on every scrap of ground that’s not been beaten down by boots - the hamlet smells of putridity.
            \n\nThe screeching of animals isn’t as overwhelming here, but unlike in the other settlements, there’s hardly any labor to fill the emptiness. The bandits either follow you, or sit around idly. There’s firewood gathered by the wall, and you see someone eating a piece of cold, roasted meat, but it seems like no one is eager to grab a hammer, a needle, or a carving knife.
            \n\n{color=#f6d6bd}Glaucia{/color} doesn’t stop, making you follow her around the long shelter. She keeps her eyes straight ahead, not commenting on anything you walk by. With every step, her mail jangles slightly, breaking the silence. Your eyes either wander around, or stare at the back of her head.
            '
            '(glaucia1 set)':
                pass

label banditshideoutregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[banditshideout_fluff] [banditshideout_description2]
        '
        'I enter the hamlet.' if glaucia_annoyed != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            jump banditshideoutglauciaregular01
        'Glaucia won’t “waste her time” on me today. (disabled)' if glaucia_annoyed == day:
            pass
        'I ask someone for a spot where I could spend the night.' ( condition="not banditshideout_aboutrest and quarters >= world_daylength-20" ):
            jump banditshideout_aboutrest01
        'I head to the pond.' if not banditshideout_aboutcleanwater:
            jump banditshideout_aboutcleanwater01
        'I travel back to the cairn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel back to the cairn.')
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

label banditshideoutafterinteraction01:
    $ can_items = 1
    if glaucia_firstattitude == "friendly":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The highwaymen stay close to you, not allowing you to approach your blade."
        else:
            $ banditshideout_description2 = "Even though the highwaymen keep an eye on you, they let you search your bundles without their assistance."
    elif glaucia_firstattitude == "playful":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "Even though the highwaymen keep an eye on you, they let you search your bundles without their assistance."
        else:
            $ banditshideout_description2 = "Some of the highwaymen observe you from a distance, but are busy with their own chores and chatter."
    elif glaucia_firstattitude == "distanced":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The highwaymen stay close to you, not allowing you to approach your blade."
        else:
            $ banditshideout_description2 = "Even though the highwaymen keep an eye on you, they let you search your bundles without their assistance."
    elif glaucia_firstattitude == "intimidating":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "Some of the highwaymen observe you from a distance, but are busy with their own chores and chatter."
        else:
            $ banditshideout_description2 = "A few of the bandits welcome you by mentioning your trade, and while you’re being observed, no one reaches for their weapon."
    elif glaucia_firstattitude == "vulnerable":
        if glaucia_friendship <= 5:
            $ banditshideout_description2 = "The bandits stay close to you, pushing you forward and commenting that “you look around too much.” Whenever you try to do something at your bundles, they watch your hands, sometimes stopping you so they can get a better look, allegedly to make sure you don’t have “poison or a dagger there.”"
        else:
            $ banditshideout_description2 = "The highwaymen stay close to you, not allowing you to approach your blade."
    menu:
        'You get back to {color=#f6d6bd}[horsename]{/color}. [banditshideout_description2]
        '
        'I enter the hamlet.' if glaucia_annoyed != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            jump banditshideoutglauciaregular01
        'Glaucia won’t “waste her time” on me today. (disabled)' if glaucia_annoyed == day:
            pass
        'I ask someone for a spot where I could spend the night.' ( condition="not banditshideout_aboutrest and quarters >= world_daylength-20" ):
            jump banditshideout_aboutrest01
        'I head to the pond.' if not banditshideout_aboutcleanwater:
            jump banditshideout_aboutcleanwater01
        'I travel back to the cairn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel back to the cairn.')
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

label banditshideoutaftertalkingtoglaucia01:
    if not glaucia_invitingtojoin and not glaucia_invitingtojoin_discarded and glaucia_friendship >= 8 and quest_glauciasupport == 2 and quest_runaway == 2:
        if (glaucia_about_nomoreundead and whitemarshes_nomoreundead) or (glaucia_about_nomoreundead and whitemarshes_destroyed):
            if quest_galerockssupport == 3 or quest_galerockssupport == 4:
                menu:
                    'Before you leave the hideout, {color=#f6d6bd}Glaucia{/color} pulls your shoulder, making you look into her emerald eyes.
                    \n\n“You’re more capable than I expected,” she picks her words with care. “Come here if the things in the city go poorly for you. I could use a rider.”
                    \n\nShe pushes you away and turns around, continuing her stroll.
                    '
                    'I observe her for a moment. “I’ll think about it.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe her for a moment. “I’ll think about it.”')
                        $ glaucia_invitingtojoin = 1
                        if pc_goal == "iwanttostartanewlife":
                            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
                        $ pc_goal_iwantnewlife_bandits = 1
                        jump banditshideoutafterinteraction01
                    'I take a deep breath. I’d never join some {i}bandits{/i}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath. I’d never join some {i}bandits{/i}.')
                        $ glaucia_invitingtojoin_discarded = 1
                        jump banditshideoutafterinteraction01
                    'I don’t respond.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t respond.')
                        $ glaucia_invitingtojoin = 1
                        if pc_goal == "iwanttostartanewlife":
                            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
                        $ pc_goal_iwantnewlife_bandits = 1
                        jump banditshideoutafterinteraction01
    if glaucia_questionstoday or glaucia_friendship >= 6:
        jump banditshideoutafterinteraction01
    else:
        $ glaucia_friendship -= 1
        $ glaucia_annoyed = day
        $ can_items = 1
        if armor <= 2:
            $ custom1 = "After you reach the gate, you realize that her grasp has actually hurt you, despite your armor. The guards block the way back, giving you harsh looks."
        else:
            $ custom1 = "As you pass the gate, her guards block the way back, giving you harsh looks."
        menu:
            'You try to turn away, but her strong hand pulls your shoulder. “Didn’t I tell you to not waste my time unless you have a {i}good{/i} reason for it?”
            \n\nYou start to explain yourself, but she pushes you away, like a merchant would do to a beggar on a street. “Next time you come here, be sure I have something to gain from it, outsider. Scat.” [custom1]
            '
            'I travel back to the cairn.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel back to the cairn.')
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

label banditshideout_aboutrest01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask someone for a spot where I could spend the night.')
    $ can_items = 1
    $ banditshideout_aboutrest = 1
    menu:
        'The woman you ask gives you a puzzled look. “There’s a tavern on the northern road, and a few villages in the west...” You try to explain what you mean, and a man without an ear laughs, then speaks with a different accent. “Ne a chance. Nae warden cuts my throat this night, nor on any other.”
        '
        'I enter the hamlet.' if glaucia_annoyed != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            jump banditshideoutglauciaregular01
        'Glaucia won’t “waste her time” on me today. (disabled)' if glaucia_annoyed == day:
            pass
        'I ask someone for a spot where I could spend the night.' ( condition="not banditshideout_aboutrest and quarters >= world_daylength-20" ):
            jump banditshideout_aboutrest01
        'I head to the pond.' if not banditshideout_aboutcleanwater:
            jump banditshideout_aboutcleanwater01
        'I travel back to the cairn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel back to the cairn.')
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

label banditshideout_aboutcleanwater01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the pond.')
    $ banditshideout_aboutcleanwater = 1
    $ can_items = 1
    menu:
        'A man with a bare chest gets in your way. “And where do ye think ye’re going? We need no spy eyes around here, and we aren’t going to keep ya ugly mug safe from monsters. Buy yaself a tub in an inn.”
        '
        'I enter the hamlet.' if glaucia_annoyed != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the hamlet.')
            jump banditshideoutglauciaregular01
        'Glaucia won’t “waste her time” on me today. (disabled)' if glaucia_annoyed == day:
            pass
        'I ask someone for a spot where I could spend the night.' ( condition="not banditshideout_aboutrest and quarters >= world_daylength-20" ):
            jump banditshideout_aboutrest01
        'I head to the pond.' if not banditshideout_aboutcleanwater:
            jump banditshideout_aboutcleanwater01
        'I travel back to the cairn.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel back to the cairn.')
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
